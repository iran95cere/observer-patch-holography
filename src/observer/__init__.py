"""Observer Patch Holography — Core observer module.

This module provides the foundational primitives for constructing
consistency-preserving observer patches across holographic state spaces.

See book/chapter-01-consistency.md for theoretical background.

Note (personal fork): I'm using this to work through the consistency
checker examples from chapter 3. Added lazy_imports flag below for
faster startup when only ObserverPatch is needed.
"""

from .patch import ObserverPatch
from .lineage import LineageTracker
from .consistency import ConsistencyChecker

__all__ = [
    "ObserverPatch",
    "LineageTracker",
    "ConsistencyChecker",
]

__version__ = "0.1.0"
__author__ = "FloatingPragma contributors"
