# Screen Microphysics and Observers

This note is the informal companion to `paper/screen_microphysics_and_observer_synchronization.tex`.

It is written in the style of the book, but it is intentionally a standalone extra document.
Its job is to explain, in plain language, how one might go from an actual arrangement of local
screen registers all the way to patches, records, observers, interaction, and synchronization.

## Status

- Side project.
- Constructive and explanatory.
- Not part of the compact recovered core.
- Not a claim that the exact OPH ultraviolet completion is already known.

## The Big Goal

The real constructive goal is stronger than saying "reality is information."

It is this:

> Write down a concrete screen made of finite local quantum registers, say exactly how those
> registers are encoded in actual qubits, say exactly which local constraints and local
> interactions they obey, and then show how patches, records, observers, and shared
> objectivity could arise from that one underlying system.

That is a build problem, not just a slogan problem.

## Why This Note Exists

The main OPH papers already give more structure than people sometimes realize.

They already say that the screen should be described by finite local degrees of freedom, with
constraints, patch algebras, overlaps, and edge-sector structure. What is still missing is the
middle layer that a builder would ask for:

- what exactly sits on a link or site
- how it is encoded in actual qubits
- what is measured locally
- what counts as a record
- what counts as an observer
- how two observers compare and reconcile what they know

This note is about that middle layer.

## What This Note Does And Does Not Claim

It does claim:

- that OPH needs a concrete screen microphysics program
- that one reference architecture should be written down explicitly
- that records, observers, and synchronization should be treated as dynamical patterns
- that a simulator blueprint can be useful before final closure is proved

It does not claim:

- that the unique correct screen microphysics has already been identified
- that a qubit simulator automatically gives the full gravity branch
- that observer emergence is solved just by saying "records exist"
- that synchronization is trivial once overlaps exist

## A First Working Picture

Think of the screen as a constrained quantum system on a triangulated sphere.

```text
triangulated sphere
      +
finite link registers
      +
vertex constraints
      +
patch observables
      +
overlap comparison rules
      =
one candidate microscopic screen
```

The simplest constructive choice is not to invent an exotic architecture immediately.
It is to choose one reference architecture close to the existing OPH regulator language:

- a triangulated `S^2`
- finite-dimensional registers on oriented links
- Gauss-type constraints at vertices
- plaquette or face probes
- patch-boundary observables
- explicit overlap records

That does not prove the architecture is final. It only gives the side project something concrete to build.

## A Reference Architecture

The reference architecture in this side project is a finite gauge-register or quantum-link style screen.

Here is the picture:

```text
      o----e12----o
     / \          / \
    /   \   f1   /   \
 e31    e23    e24   e45
  /       \    /       \
 o----e13----o----e34---o

each oriented link  -> finite logical register
each vertex         -> constraint projector
each face           -> curvature / plaquette probe
```

At first, that may sound abstract. But it is already much closer to a build than a vague statement
that geometry and observers somehow emerge from information.

The constructive question is now clear:

1. What exactly is stored in each logical register?
2. How many physical qubits are needed to encode it?
3. Which local operations preserve the constraints?
4. Which observables define a patch?
5. Which observables can two patches compare on an overlap?

For a useful phase-1 build, the answer should be explicit all the way down:

- each oriented link carries one finite logical gauge register
- selected vertices or coarse cells carry small record-qubit banks
- each vertex has a local admissibility or Gauss check
- each face has a plaquette or curvature probe
- the same microscopic model also contains the repair layer

## From Single Registers To Qubits

The first technical move is not yet about observers. It is about encoding.

Suppose a link register has `d` allowed logical states. Then a qubit implementation needs at least
`ceil(log2 d)` qubits for that register, plus any ancillas used for constraint checking, record
storage, or error flags.

The important thing is not only the number of qubits. It is the whole translation package:

- which logical basis states are allowed
- which qubit basis states represent them
- which qubit states are invalid padding states
- which qubit operators implement logical shifts, phases, and projectors
- how vertex constraints are checked and enforced

If this translation is not written down, then there is no real microphysics program yet.

## From Registers To Patches

Once the local degrees of freedom are fixed, patches can be defined more sharply.

A patch is not just a geometric cap on the sphere. A patch is:

- a region of the triangulation
- together with the observables that remain meaningful for that region
- together with the boundary rules needed to handle gauge constraints correctly

That is why patch algebras matter. They tell us what a local observer can actually query.

## From Patches To Overlaps

The next step is overlap structure.

Two patches do not share everything. They share only the observables that belong to both patch descriptions.

That gives a natural operational meaning to overlap:

```text
patch P observables
        intersect
patch Q observables
        =
shared overlap observables
```

This is also where edge sectors become important. Shared information often lives at the boundary,
not deep in the interior. In a constructive model, overlap data is the natural place to store
compareable records.

That shared overlap layer should be kept small and explicit. A good first dictionary would include:

- collar or boundary sector labels
- selected shared bits or shared charges
- one mismatch syndrome saying where two patch descriptions disagree

That is enough to make local repair meaningful without pretending that whole quantum states can be cloned or fully synchronized.

## From Overlaps To Records

A record is not just any correlation.

A useful record should be:

- locally writable
- locally readable later
- stable for long enough to matter
- checkable against overlap data

That last point is important. If a bit of information cannot be checked again from shared observables,
it is a poor candidate for the kind of objectivity OPH needs.

The natural place to look for shareable records is therefore in overlap-accessible observables and
their associated edge-sector labels.

## From Records To Observers

An observer is not a ghost outside the screen.

An observer is a stable pattern inside the screen microphysics that:

- has access to a patch
- carries internal records
- updates those records
- compares selected overlap data with neighbors
- persists long enough to support a coherent viewpoint

This is a pattern criterion, not a consciousness criterion.

That distinction matters:

- an observer pattern is an operational structure inside the dynamics
- a consciousness claim is a much stronger philosophical claim

This side project only needs the first one.

One useful refinement from the paper draft is that an observer-pattern should include not only a patch and records,
but also an update interface: something that reads local records, queries overlap data, and changes later local actions.

## From Observers To Synchronization

Two observers do not need identical internal states.

What they need is compatibility on the observables they both use to talk about the same world.

So synchronization means something more modest and more precise:

1. detect a mismatch on shared overlap records
2. identify whether the mismatch is noise, staleness, or a real disagreement
3. apply a local repair or reconciliation rule
4. reduce the mismatch without breaking the underlying constraints
5. stabilize a shared account of the overlap

This gives a constructive meaning to "shared objectivity." It is not a miracle. It is a repeated
local consistency process.

```text
observer A record
        |
        v
shared overlap check
        |
        v
mismatch syndrome
        |
        v
local repair / update
        |
        v
reduced disagreement
```

For a first build, three repair styles are worth distinguishing:

- syndrome-based local repair
- dissipative mismatch damping
- record-mediated higher-level update

The best phase-1 default is the first one. It is the most local, the easiest to debug, and the closest to the existing OPH repair language.

## What An Actual Build Would Need

A real build would need much more than a nice verbal picture.

At minimum it would need:

- one chosen screen architecture
- one explicit register map
- one exact qubit encoding
- one list of local constraint projectors
- one list of local update operators
- one patch and overlap observable dictionary
- one record criterion
- one observer criterion
- one synchronization or repair loop
- one small-lattice benchmark suite

Without those pieces, the project is still pre-constructive.

The first concrete build should also be deliberately modest:

- an octahedral or comparably small spherical screen
- `G = Z_2` on links for the first debugging pass
- one record qubit per coarse patch or cap
- at least three overlapping patches
- one syndrome-based overlap repair rule

## What Success Would Look Like

A first small simulator would not need to recover all of physics.

It would only need to show a few clear things:

- constraints can be imposed and tracked
- patch observables can be queried consistently
- overlap data can be compared by neighboring observer-patterns
- records can remain stable over useful timescales
- mismatch can be reduced by a local repair rule

That would already be a major step forward because it would turn the observer story into something testable.

It should also fail in controlled ways when the design is wrong. Good negative controls include:

- breaking gauge covariance on purpose
- removing the record-stabilization layer
- asking the repair map to synchronize too much instead of only the declared shared observable family

## A First Research Program

The cleanest way to attack the side project is in stages.

### Stage 1. Fix one reference architecture

Choose one finite gauge-register or quantum-link style screen and commit to it as the working model.
Do not wait for the final answer before writing anything.

### Stage 2. Write the qubit encoding

For each logical register, say exactly how many qubits it needs and which qubit states represent the
allowed logical states.

Start with the cheapest sensible sequence:

- `Z_2` or small `Z_N` finite-group registers first
- then one small nonabelian group such as `S_3`
- only then a more ambitious quantum-link truncation

### Stage 3. Define patch and overlap observables

Write down what a patch can measure and what two patches can compare.

### Stage 4. Define records and observer patterns

Say which observables count as records and what dynamical conditions promote a subsystem into an
observer-pattern.

### Stage 5. Define synchronization

Choose one explicit repair or reconciliation rule and say how mismatch is detected and reduced.

### Stage 6. Build a small benchmark

Start with a tiny triangulation, a tiny observer set, and a small diagnostic suite.

### Stage 7. Compare back to OPH closure tasks

Only after the constructive model exists should it be mapped back onto the existing microphysics,
observer, and reality task branches.

## Relation To The Existing Completion Work

This side project is not a substitute for the main completion tree.

It is a sidecar that can sharpen the meaning of several downstream tasks:

- the direct microphysics lane around edge heat-kernel or Casimir behavior
- the reality-side finite patch-net embedding problem
- the observer-side record, Born-rule, and continuation packages

That means the side project is useful even before it closes anything formally.

## Scope Discipline

This note should keep three distinctions visible at all times:

- simulator blueprint is not theorem-level derivation
- observer pattern is not consciousness theory
- synchronization of overlap data is not full continuum closure

If those distinctions remain clear, the side project will stay honest and useful.

## Immediate Next Drafting Moves

The next concrete moves are:

- expand the qudit-to-qubit encoding into an explicit register table
- write one toy overlap dictionary for two neighboring patches
- write one toy observer definition in terms of record access and persistence
- write one explicit synchronization loop with a mismatch syndrome and repair update
