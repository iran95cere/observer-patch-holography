"""Patch module for observer-patch-holography.

This module implements the core patching mechanism that allows observers
to intercept, modify, and record state transitions in a holographic
(fully reproducible) manner. Each patch maintains a lineage chain
consistent with the concepts described in book/chapter-02-lineage.md.
"""

from __future__ import annotations

import hashlib
import json
import time
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional


@dataclass
class PatchRecord:
    """Immutable record of a single patch application.

    Attributes:
        patch_id: Unique identifier derived from content hash.
        parent_id: Identifier of the preceding patch (None for root).
        timestamp: Unix timestamp of patch creation.
        payload: The actual change data carried by this patch.
        metadata: Arbitrary key-value annotations.
    """

    patch_id: str
    parent_id: Optional[str]
    timestamp: float
    payload: Dict[str, Any]
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Serialize this record to a plain dictionary."""
        return {
            "patch_id": self.patch_id,
            "parent_id": self.parent_id,
            "timestamp": self.timestamp,
            "payload": self.payload,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PatchRecord":
        """Deserialize a PatchRecord from a plain dictionary."""
        return cls(
            patch_id=data["patch_id"],
            parent_id=data.get("parent_id"),
            timestamp=data["timestamp"],
            payload=data["payload"],
            metadata=data.get("metadata", {}),
        )


def _compute_patch_id(
    parent_id: Optional[str],
    payload: Dict[str, Any],
    timestamp: float,
) -> str:
    """Derive a deterministic patch identifier from its content.

    The identifier is the first 16 hex characters of the SHA-256 digest
    of the canonical JSON representation of the patch inputs.
    """
    canonical = json.dumps(
        {"parent_id": parent_id, "payload": payload, "timestamp": timestamp},
        sort_keys=True,
        separators=(",", ":"),
    ).encode()
    return hashlib.sha256(canonical).hexdigest()[:16]


class PatchChain:
    """Ordered, append-only sequence of PatchRecords forming a lineage.

    Each new patch references the previous patch by its identifier,
    creating a verifiable chain of state transitions that can be
    replayed to reconstruct any historical state.
    """

    def __init__(self) -> None:
        self._records: List[PatchRecord] = []
        self._index: Dict[str, PatchRecord] = {}

    # ------------------------------------------------------------------
    # Mutation
    # ------------------------------------------------------------------

    def apply(
        self,
        payload: Dict[str, Any],
        metadata: Optional[Dict[str, Any]] = None,
        *,
        timestamp: Optional[float] = None,
    ) -> PatchRecord:
        """Append a new patch to the chain and return its record.

        Args:
            payload: The change data for this patch.
            metadata: Optional annotations (e.g. author, source).
            timestamp: Override the creation time (useful in tests).

        Returns:
            The newly created and stored PatchRecord.
        """
        ts = timestamp if timestamp is not None else time.time()
        parent_id = self._records[-1].patch_id if self._records else None
        patch_id = _compute_patch_id(parent_id, payload, ts)

        record = PatchRecord(
            patch_id=patch_id,
            parent_id=parent_id,
            timestamp=ts,
            payload=payload,
            metadata=metadata or {},
        )
        self._records.append(record)
        self._index[patch_id] = record
        return record

    # ------------------------------------------------------------------
    # Query
    # ------------------------------------------------------------------

    def get(self, patch_id: str) -> Optional[PatchRecord]:
        """Retrieve a patch record by its identifier."""
        return self._index.get(patch_id)

    def head(self) -> Optional[PatchRecord]:
        """Return the most recently applied patch, or None if empty."""
        return self._records[-1] if self._records else None

    def replay(
        self,
        reducer: Callable[[Any, Dict[str, Any]], Any],
        initial_state: Any = None,
    ) -> Any:
        """Reconstruct state by folding all patches through *reducer*.

        Args:
            reducer: ``(state, payload) -> new_state`` pure function.
            initial_state: Seed value passed to the first reducer call.

        Returns:
            The accumulated state after all patches have been applied.
        """
        state = initial_state
        for record in self._records:
            state = reducer(state, record.payload)
        return state

    def __len__(self) -> int:
        return len(self._records)

    def __iter__(self):
        return iter(self._records)
