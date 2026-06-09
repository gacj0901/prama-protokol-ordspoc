# Model Evolution

ORDSPOC is a structural proof-of-concept, not a calibrated cyber-risk model.
This document records the intended evolution of the demonstration logic so that
changes remain inspectable and reproducible.

## v0.1.0 Baseline

The initial demonstration established the core contrast:

- Technique or stage counting can rank longer human-gated paths above shorter
  autonomous orchestration paths.
- PRAMA-style trajectory measurement separates paths by autonomous coupling,
  persistence and recovery.
- The demo used only abstract, dimensionless `demand` and `autonomy` values.

The expected baseline ordering was:

```text
A2 > A1 > A0 >> B > C
```

## v0.2.0 Structural Refinement

Version 0.2.0 strengthens the proof-of-concept without changing the project
positioning.

The accumulator `Xi` is now non-saturating:

```text
Xi(t) = retention * Xi(t-1) + Delta(t)
```

The displayed `collapse_xi_norm` remains clamped to `[0, 1]` for readability,
while `collapse_xi_norm_raw` is preserved in the JSON output and table as
`collapse_raw`. This keeps the console output legible while retaining the
structural magnitude needed for later analysis.

The release also adds an adversarial pair:

- `D interrupted autonomous burst`
- `E sustained escalation without recovery`

This pair clarifies that ACI is explanatory, not decisive. D has higher ACI
than E, but PRAMA ranks E above D because sustained escalation without recovery
outweighs an interrupted burst.

The v0.2.0 expected ordering is:

```text
A2 > A1 > A0 > E > D >> B > C
```

## Invariants

The demonstration remains safe and structural:

- No attack techniques are modeled.
- No operational procedures are modeled.
- All trajectories are synthetic and deterministic.
- The model remains a proof-of-concept, not a calibrated cyber-risk model.
