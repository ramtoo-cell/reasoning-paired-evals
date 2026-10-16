# Method and experiment protocol

## Research question
Does an intervention improve success on the same reasoning tasks?

## Implemented method
Match unique task IDs, compute candidate minus baseline accuracy, bootstrap paired differences, and use an exact two-sided binomial test on discordant pairs. The bootstrap resamples tasks, not independent model outputs.

## Assumptions and failure modes
Assumes independent tasks and binary outcomes. Correlated task families need cluster resampling. The percentile interval is approximate; exploratory comparisons require multiplicity correction.

## Proposed next experiment — not yet performed
Collect a held-out set of expert-reviewed audit or policy reasoning tasks. Use stable task IDs, preregister the comparison, and record model and prompt versions. Double-review a subset, adjudicate disagreements, and publish anonymized artifacts only when permitted. Separate exploratory analysis from confirmatory results. The fixture is insufficient to estimate real-world performance.

## Scope
The implementation is deliberately inspectable. Validation checks common malformed inputs; it is not a hardened service for adversarial payloads. Apply external input-size limits for large files. No model API is called by this repository.
