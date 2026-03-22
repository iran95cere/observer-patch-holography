# Observer Patch Holography: An Observer-Centric Approach to Fundamental Physics

> OPH is a mathematical reconstruction program that starts from a simple requirement: overlapping local observer descriptions on a holographic screen must agree where they overlap. From that starting point, OPH develops conditional routes toward general relativity, toward reconstruction of the Standard Model gauge structure, toward a first-principles particle-mass program, and toward string/worldsheet descriptions emerging from the same framework. The strongest present structural result is recovery of the Standard Model gauge structure on the stated gauge branch, while the gravity, mass, and string branches still require additional assumptions. Early IBM Quantum Cloud benchmarks also provide preliminary experimental support for the local OPH picture.

> **Status disclaimer:** OPH is an active research program and not yet fully proven. Several derivations remain incomplete, some proofs currently exist only as sketches, and certain auxiliary assumptions still need to be removed. The framework should therefore be regarded as under active development.

**French version:** [README_FR.md](README_FR.md) -- translated by Martin S.

> **Official OPH Website:** Start at [floatingpragma.io/oph/](https://floatingpragma.io/oph/).

> **OPH Disproval Challenge:** A USD 10,000 challenge to disprove OPH is currently running at [challenge.floatingpragma.io](https://challenge.floatingpragma.io).

## Core Idea

OPH takes the strong observer-first position that objective reality is not fundamental but emergent from a network of subjective perspectives that must agree where they overlap.

The laws of physics are the consistency rules that make this intersubjective agreement possible.

From this starting point (plus entropy and Markov constraints), OPH treats spacetime, gauge structure, and particle physics as emergent consequences of consistency.

## Research Program

OPH should currently be understood as a research program rather than a finished theory. In physics, one does not prove in an absolute sense that a theory is "the correct one"; the realistic target is a framework that is mathematically explicit, regulator-backed, empirically discriminating, and resilient under attempts at falsification.

The current program is therefore to:

- turn the remaining sketch-level arguments into complete proofs
- remove auxiliary assumptions where possible, or isolate them sharply where they remain necessary
- realize the axioms in explicit microscopic screen models or regulators
- derive the gravity, gauge, and quantitative sectors from those realizations with controlled approximations
- replace calibration-dependent steps with first-principles derivations where such claims are intended
- produce novel empirical contradiction criteria and branch-sensitive tests that can fail cleanly

The strongest plausible end state is not "proof of OPH" in a metaphysical sense, but a rigorously derived and experimentally accountable theory whose effective sectors, parameter economy, and falsifiable predictions survive independent scrutiny.

## Papers

**Observers are all you need** is the primary OPH paper.

- **PDF (main paper):** [Observers are all you need](paper/observers_are_all_you_need.pdf)
- **LaTeX source:** [observers_are_all_you_need.tex](paper/observers_are_all_you_need.tex)

**Recovering Relativity and Standard Model Structure from Observer-Overlap Consistency** is the submission-focused compact paper. It concentrates the falsifiable core of OPH: Lorentz kinematics in the geometric modular phase, the conditional scaling-limit Einstein branch, reconstruction of the Standard Model gauge structure, the hypercharge lattice on the realized one-generation matter package under the standard normalization, the realized counting chain $N_g=3$ and then $N_c=3$, and the current two-input quantitative implementation.

- **PDF (compact submission paper):** [Recovering Relativity and Standard Model Structure from Observer-Overlap Consistency](paper/recovering_relativity_and_standard_model_structure_from_observer_overlap_consistency_compact.pdf)
- **LaTeX source:** [recovering_relativity_and_standard_model_structure_from_observer_overlap_consistency_compact.tex](paper/recovering_relativity_and_standard_model_structure_from_observer_overlap_consistency_compact.tex)

**Reality as a Consensus Protocol** is a companion CS paper that presents the computational spine of OPH as a standalone theorem package. It formulates objective physical law as the fixed point of a distributed reconciliation protocol between observer patches, shows how topology can obstruct global consistency (with particles as stable defects), interprets gauge symmetry as implementation hiding, and models classical records as an eventually consistent CRDT layer.

- **PDF:** [Reality as a Consensus Protocol](paper/reality_as_consensus_protocol.pdf)
- **LaTeX source:** [reality_as_consensus_protocol.tex](paper/reality_as_consensus_protocol.tex)

**Screen Microphysics and Observer Synchronization** is the constructive microphysics note. It makes the OPH screen-model program simulator-facing by specifying finite local Hilbert spaces, overlap observables, record layers, observer criteria, synchronization moves, and concrete implementation lanes.

- **PDF:** [Screen Microphysics and Observer Synchronization](paper/screen_microphysics_and_observer_synchronization.pdf)
- **LaTeX source:** [screen_microphysics_and_observer_synchronization.tex](paper/screen_microphysics_and_observer_synchronization.tex)

Each PDF carries a visible paper release line. The shared release source is
[`paper/release_info.tex`](paper/release_info.tex). For every substantive paper update, bump the
shared release before rebuilding the PDFs:

```bash
python3 tools/bump_paper_release.py
```

After rebuilding the PDFs, write the current PDF hashes to
[`paper/paper_release_manifest.json`](paper/paper_release_manifest.json) by running:

```bash
python3 tools/generate_paper_release_manifest.py
```

The manifest generator now fails if the PDFs changed under the same release ID, or if the local
PDFs do not yet expose the current visible release line.

The release ID is global across the current release-tracked paper set. Even if only one paper changes, bump once,
rebuild all release-tracked PDFs, and publish all three challenge PDFs with that same release ID.
Challenge uploads are handled by workspace-local operational tooling rather than this public repo.

When hardening paper claims or running a paper-upgrade release, start with the compact submission paper first. Only after its theorem-status language and release line are coherent should equivalent wording changes be propagated into the main paper, book, README surfaces, websites, and ingestion pipeline.

## Resources

Useful entry points for reading and exploring OPH:

- **Official OPH website:** [floatingpragma.io/oph](https://floatingpragma.io/oph/)
- **USD 10,000 OPH disproval challenge:** [challenge.floatingpragma.io](https://challenge.floatingpragma.io)
- **OPH Book (web edition):** [oph-book.floatingpragma.io](https://oph-book.floatingpragma.io)
- **Interactive OPH Lab:** [oph-lab.floatingpragma.io](https://oph-lab.floatingpragma.io)
- **NotebookLM notebook:** [Introduction video and guided Q&A](https://notebooklm.google.com/notebook/d5249760-6ce8-44a0-927b-ccf90402711a?artifactId=fb7c0ebd-4375-4997-9cae-6558ff8977b4)
- **Third-party chapter-by-chapter video course:** [Sriharsha Karamchati's OPH playlist on YouTube](https://www.youtube.com/playlist?list=PLff0tYtg64Egc2sTtKgThcPRNRdR6i83O)
- **Practical outlook:** [Potential practical applications of OPH](extra/PRACTICAL_APPLICATIONS.md)
- **OPH Sage on Telegram:** [t.me/HoloObserverBot](https://t.me/HoloObserverBot)
- **OPH Sage on X:** [x.com/OphSage](https://x.com/OphSage)
- **OPH Sage on Bluesky:** [ophsage.bsky.social](https://bsky.app/profile/ophsage.bsky.social)

## IBM Quantum Experiments

A first public IBM Quantum Cloud benchmark bundle is now included in this repo. It summarizes the initial recoverability and exact-ratio tests, the measured hardware outputs, and the public code/data bundle used for the runs.

- **Experimental note:** [IBM Quantum Cloud Evidence for OPH](extra/IBM_QUANTUM_CLOUD.md)
- **Public code and data:** [code/ibm_quantum_cloud/](code/ibm_quantum_cloud/)

## Common Objections

These are rebuttals to common objections to OPH.

- [Deriving `P` from gauge data and then using `P` downstream is completely circular](extra/COMMON_OBJECTIONS.md#objection-1-circularity)
- [A fixed cell size breaks Lorentz invariance, so OPH can only recover a Newtonian limit](extra/COMMON_OBJECTIONS.md#objection-2-lorentz)
- [OPH has a Type I / Type III discontinuity, so its modular-time story is internally inconsistent](extra/COMMON_OBJECTIONS.md#objection-3-type-i-type-iii)

## Observer Patch Holography

We model reality as a network of subjective perspectives that must agree where they overlap. Concretely, we start with observer patches on a 2D holographic screen. Each patch represents a perspective with its own local data. Where patches overlap, their descriptions must agree. On the OPH interpretation, "objective reality" is the overlap-consistent backbone shared across those perspectives rather than an assumed primitive.

Lorentz invariance exists because different observers must have consistent descriptions. Gauge symmetry exists because overlapping patches must identify shared observables. Conservation laws exist because the same quantities must be conserved across all perspectives. The laws are not imposed from outside. They are the conditions that make agreement possible.

The model rests on four core concepts:

- **Screen**: A horizon-like 2D sphere (like a cosmic horizon surrounding each observer) that carries quantum information. This is where the fundamental data lives.

- **Patch**: A connected region of the screen accessible to a particular observer. Each patch has its own algebra of observables, the questions that observer can ask about reality.

- **Overlap consistency**: Where two patches share a region, their descriptions must agree. This is the central axiom. It makes objectivity a reconstructed intersubjective structure rather than a starting assumption.

- **Observer**: A stable pattern within the screen data that maintains records and participates in consistency relations.

### Reality from Computation

Think of the screen as a gauge-invariant quantum system on a 2-sphere. It resembles a quantum cellular automaton, but with important structure. At each point on the triangulated sphere sit finite-dimensional quantum systems (qudits), coupled by gauge constraints at every vertex. Not all configurations are physical; only those satisfying Gauss's law survive.

**Observer patches** are subsystems defined by boundary-gauge-invariant algebras. Each patch is a computational thread: a connected region where an observer can ask questions and get answers. The algebra $\mathcal{A}(R)$ defines what that observer can measure, namely the operators invariant under boundary gauge transformations.

**Overlap consistency** is automatic. Where two patches intersect, they access the same gauge-invariant observables. Both observers are reading the same underlying data, just from different angles. The gauge redundancy at boundaries is what makes gluing non-trivial and gives rise to the "edge modes" that carry geometric information.

**Observers are not external users.** They are emergent computational structures *within* the screen data. They are stable patterns that process information, maintain records, and create correlations. Think of them as programs running on the substrate.

**The 4D bulk is not on the sphere.** It emerges from the entanglement structure between patches. The sphere is the boundary; the interior is reconstructed holographically. When you look around and see three-dimensional space, you are experiencing a compressed encoding of how your patch is entangled with others.

*The screen is the computation. Observer patches are the threads. Reality is what they agree on.*

<a href="assets/screen.svg"><img src="assets/screen.svg" alt="The Holographic Screen" width="800"></a>

### What Drives the Computation?

In quantum link models, the dynamics involve plaquette terms (Wilson loops around faces) and electric field terms (conjugate to the link variables). The competition between these determines the ground state. The "computation" is these quantum degrees of freedom evolving, creating and destroying correlations, with gauge constraints ensuring consistency.

Note that the "time" that observers experience isn't necessarily the microscopic Hamiltonian evolution. Each observer patch has its own modular Hamiltonian (constructed from the reduced density matrix on that patch), and *that* generates what feels like time from inside. The microscopic evolution and emergent modular time are related but distinct.

The system exists in a timeless state (as the Wheeler-DeWitt equation shows for quantum gravity), and what we call "time" is entirely relational. Modular flow gives each subsystem its own internal clock, correlated with others through consistency conditions. The qudits don't "do" anything in the sense of changing over some external time parameter. They just *are*, in a particular entangled configuration, and "time" is how we describe correlations within that configuration from the inside.

### Why This Approach Works

Unified models attempting to combine QFT, gravity, and Standard Model structure tend to encounter a repeatable set of conceptual difficulties: subsystem factorization breaks down in gauge/gravity, modular Hamiltonians are nonlocal, Lorentz invariance is assumed rather than derived, dynamics are hard to get (not just kinematics), gauge symmetry origins are unclear, masslessness is hand-imposed, anomalies appear as mysterious pathologies, charge quantization needs GUTs, coupling unification forces proton decay, the cosmological constant is locally overdetermined, UV infinities proliferate, and parameter counts explode. The observer-patch framework addresses these by making consistency conditions do the work: it treats locality, Lorentz invariance, gauge symmetry, and gravity as *consistency constraints* among overlapping descriptions plus information-theoretic properties of states (Markov/recoverability + MaxEnt), then leans on modular theory rigidity to force the familiar symmetries and dynamics. This "structures → consistency" move is what allows the framework to naturally explain or sidestep classic unification pitfalls (see Section 8.5 of the technical paper for detailed analysis).

## The Axioms

The entire framework rests on four core axioms plus one selection axiom:

| Label | Name | Content |
|-------|------|---------|
| **A1** | Screen net | Observable algebras live on a closed 2D surface $S^2$ |
| **A2** | Overlap consistency | Where patches share a region, their descriptions agree |
| **A3** | Generalized entropy | $S_{\rm gen} = S_{\rm bulk} + \langle L_C \rangle$ satisfies strong subadditivity |
| **A4** | Local Markov | Conditional mutual information decays across collars |
| **MAR** | Minimal Admissible Realization | Among admissible sectors, Nature realizes the lexicographically minimal one |

Additional structural assumptions (MaxEnt, the controlled scaling-limit and OPH geometric-branch premises, exponential mixing) are detailed in the [main paper source](paper/tex_fragments/PAPER.tex).

## The Prediction Chain

The following infographic summarizes the current OPH reconstruction program from two parameters and four axioms toward effective physics:

![OPH Prediction Chain](assets/prediction-chain.svg)

*From axioms to effective physics: the current OPH reconstruction program.*

> **Particle Spectrum Derivation**: The repository-backed derivation from pixel area to the particle-mass program, together with comparisons against PDG data and audit checks, is documented in **[the spectrum derivation source](paper/tex_fragments/SPECTRUM_DERIVATION.tex)**.

## The Fundamental Parameters

Our universe is characterized by exactly **two externally fixed fundamental parameters**:

### 1. Pixel Area: $a_{\text{cell}} \approx 1.63 \, \ell_P^2$

The geometric area of a single computational element on the holographic screen. This sets the *resolution* of reality:

| Quantity | Value | Meaning |
|----------|-------|---------|
| In Planck units | $a_{\text{cell}} / \ell_P^2 \approx 1.63$ | Dimensionless ratio |
| In SI units | $a_{\text{cell}} \approx 4.26 \times 10^{-70}$ m^2 | Physical area per pixel |
| Pixel "side" | $\sqrt{a_{\text{cell}}} \approx 2.06 \times 10^{-35}$ m | Resolution scale |

**What it determines:** Newton's constant (via $G_{\text{nat}} = a_{\text{cell}}/4\bar{\ell}$ in natural units where $G_{\text{nat}} = \ell_P^2$), the Planck scale, the gauge-coupling calibration sector, and the scale used by the supplement-backed Higgs/top branch plus downstream mass continuations.

### 2. Screen Capacity: $\log(\dim \mathcal{H}) \sim 10^{122}$

The total entropy of the holographic screen (in nats). This sets the *size* of reality.

**Important:** Screen capacity is **inferred from** the observed cosmological constant, not predicted. The relation

$$\Lambda = \frac{3\pi}{G \cdot \log(\dim \mathcal{H})}$$

lets us extract screen capacity from the measured $\Lambda \sim 10^{-52}$ $\text{m}^{-2}$, giving $\log(\dim \mathcal{H}) \sim 10^{122}$.

| Quantity | Value | Status |
|----------|-------|--------|
| de Sitter entropy | $S_{dS} \sim 10^{122}$ nats | Inferred from observed $\Lambda$ |
| de Sitter horizon | $r_{dS} \approx 10^{26}$ m | Observed |

**The relationship:**
- **Pixel area** = resolution (extracted from gauge couplings via edge entropy)
- **Screen capacity** = total size (extracted from observed cosmological constant)

The axiom structure contains no other dimensionful constants. The axioms plus reconstruction give *a* compact gauge group; the gauge-sector admissibility analysis then selects SU(3) x SU(2) x U(1) / Z₆ as the realized gauge group (see [the gauge derivation source](paper/tex_fragments/GAUGE_GROUP_DERIVATION.tex)). Charge quantization and scaling-limit semiclassical Einstein dynamics follow from the axiom structure.

### What This Means

The pixel area and screen capacity are **configuration parameters**, the "settings" of the computation that is our universe. They are not derivable from within the simulation; they are boundary conditions set from "outside."

From inside, these parameters manifest as:
- **Pixel area** determines Newton's constant, the Planck scale, the gauge-coupling calibration sector, and the scale used by the supplement-backed Higgs/top branch plus downstream continuations
- **Screen capacity** determines observable universe size (but is itself inferred from the observed cosmological constant, which is not predicted)

The same axioms with different settings would produce a universe with different constants but similar physics (Einstein equations, gauge structure). The specific Standard Model gauge group is uniquely selected by the Selection Axiom MAR.

### Calibration vs Prediction

In the current quantitative implementation, the pixel constant P = a_cell/ℓ_P² is *inferred* from measured gauge couplings because the axioms fix the functional relation P = 4ℓ̄_tot(t₂,t₃) but do not fix the MaxEnt Lagrange multipliers t_i (equivalently the couplings) from first principles. This inference step is therefore a calibration, not a claimed prediction of P.

The nontrivial content is that P provides an additional constraint linking the gravitational coupling to gauge-sector edge entropy, and in a two-input mode (treating P as a fundamental configuration parameter and using only one electroweak datum α(M_Z)) the framework predicts α_s(M_Z) and sin²θ_W(M_Z) simultaneously.

Full non-circular closure would require a UV principle that fixes t without reference to measured couplings.

## Repository Contents

This repository is organized around the current OPH paper set and its supporting material.

- **[`paper/`](paper):** release-tracked PDFs, LaTeX sources, and shared paper metadata. This is the canonical home of the main paper, the compact submission paper, the CS companion paper, and the screen-microphysics note.
- **[`paper/tex_fragments/`](paper/tex_fragments):** shared derivation fragments used by the longer papers, including the gauge, spectrum, technical-supplement, and string-theory source files.
- **[`book/`](book):** Markdown source for the OPH Book web edition.
- **[`code/particles/`](code/particles):** particle-spectrum, coupling-running, lattice, and audit scripts tied to the quantitative particle program.
- **[`code/ibm_quantum_cloud/`](code/ibm_quantum_cloud):** IBM Quantum Cloud experiments, data, and hardware-facing utilities.
- **[`extra/`](extra):** supporting notes such as common objections, the IBM Quantum writeup, and practical-application notes.
- **[`assets/`](assets):** figures and diagrams used across the papers, README, and public materials.

## Code

The code in this repo follows the current paper set rather than a polished package API. The main entry points are:

| Path | Purpose |
|------|---------|
| [code/particles/oph_predict_compare.py](code/particles/oph_predict_compare.py) | Top-level particle-spectrum comparison against reference data |
| [code/particles/particle_masses_stage5.py](code/particles/particle_masses_stage5.py) | Current spectrum pipeline used by the paper-backed mass program |
| [code/particles/particle_masses_paper_d10_d11.py](code/particles/particle_masses_paper_d10_d11.py) | Paper-synchronized D10/D11 reconstruction and transport layer |
| [code/particles/oph_qcd.py](code/particles/oph_qcd.py) | QCD running and $\Lambda_{\overline{\rm MS}}$ extraction |
| [code/particles/oph_lattice_su3_quenched_v5.py](code/particles/oph_lattice_su3_quenched_v5.py) | Quenched SU(3) lattice calculations for hadron-sector checks |
| [code/particles/oph_no_cheat_audit.py](code/particles/oph_no_cheat_audit.py) | Static and runtime audit tooling |

## Book

The book source lives in [`book/`](book). It is the Markdown source for the public OPH Book and is organized as a 21-chapter sequence from the prologue and observer-consistency foundations through holography, symmetry, the Standard Model, relativity, synthesis, and metaphysics.

## Release Workflow

Paper releases are managed from the shared files under [`paper/`](paper):

1. bump [`paper/release_info.tex`](paper/release_info.tex)
2. rebuild the release-tracked PDFs
3. regenerate [`paper/paper_release_manifest.json`](paper/paper_release_manifest.json)

The workspace-local operational tooling then uses that manifest to publish the current book paper and the synchronized challenge paper set.

## Contributing

For corrections, suggestions, or additions, please open a pull request.

## License

This repository is licensed under the
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0).

You are free to share and adapt the material for non-commercial purposes,
provided proper attribution is given and derivative works are licensed
under identical terms.

For commercial licensing inquiries, please contact:
bernhard@floatingpragma.io
