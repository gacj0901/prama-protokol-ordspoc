# Method Note

ORDSPOC is a structural proof-of-concept, not a calibrated cyber-risk model. It demonstrates how trajectory-level measurement can separate abstract orchestration paths that discrete counting treats poorly.

## Variables

`demand` is a dimensionless value in `[0, 1]` representing the structural load or pressure carried by a stage.

`autonomy` is a dimensionless value in `[0, 1]` representing how much the stage proceeds through autonomous coordination rather than human-gated sequencing.

The Autonomous Coupling Index is:

```text
ACI = mean(demand x autonomy)
```

ACI is intentionally simple. It does not claim to measure real-world capability or operational effectiveness. It measures abstract coupling between pressure and autonomous progression.

ACI is explanatory, not decisive. PRAMA can rank sustained escalation above interrupted bursts even when mean coupling is lower.

## PRAMA Terms

`Delta(t)` is the per-stage orchestration delta. In this demo it is the pointwise coupling `demand(t) x autonomy(t)`.

`Xi(t)` is accumulated structural load. The minimal aptadynamic core updates it deterministically with bounded accumulation and mild retention from previous stages.

`lambda(t)` is permissivity. Higher autonomous coupling produces higher permissivity, which means less friction against continued orchestration.

`Theta(t)` is the threshold surface. It increases when permissivity is low and decreases when permissivity is high.

The regime label is assigned from normalized collapse pressure. Low pressure is `stable`, mid pressure is `elevated`, high pressure is `critical` and extreme pressure is `collapse-adjacent`.

## Why Counting Does Not Discriminate

A stage count treats every stage as equivalent. In the provided trajectories, the autonomous families A2, A1 and A0 have 6 stages, while B and C have 8 stages. Counting therefore suggests B and C are at least as large as the A-family paths.

That is the methodological gap: the important difference is not only how many steps exist, but how tightly demand and autonomy are coupled over time.

## Why PRAMA Discriminates

PRAMA separates trajectories by coupling, persistence and recovery. A trajectory with fewer stages can be structurally more intense when its stages repeatedly combine high demand with high autonomy. A trajectory with more stages can remain lower risk when coupling is weak, human-gated or non-persistent.

In this demonstration the intended ordering is:

```text
A2 > A1 > A0 > E > D >> B > C
```

## Limitations And Future Work

This demo uses synthetic values and fixed formulas. It should not be interpreted as calibrated cyber-risk scoring. Future work would require empirical grounding, sensitivity analysis, uncertainty handling, validation datasets, domain review and governance boundaries for appropriate use.
