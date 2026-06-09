# ORDSPOC — Orchestration Risk Demonstrator: Structural Proof-of-Concept

**Aptadynamic PRAMA Protokol: Structural Measurement Layer for monitor Autonomous Orchestration Risk**

ORDSPOC is a structural, safe and reproducible proof-of-concept for contrasting discrete stage counting with trajectory-level measurement of autonomous orchestration risk.

## Problem

Technique counting catalogs inventory, but autonomous orchestration is trajectory-level risk. A plain count of discrete stages can make human-gated or non-orchestrated paths appear equal to, or greater than, sustained autonomous orchestration.

## What This Demonstrates

PRAMA separates trajectories by autonomous coupling, persistence and recovery. The demo uses abstract, dimensionless variables only:

- `demand` in `[0, 1]`
- `autonomy` in `[0, 1]`

It compares five synthetic trajectories where stage count alone does not discriminate the intended structural risk ordering.

## What This Does Not Demonstrate

This is not a calibrated cyber-risk model. It contains no attack techniques, does not model operational procedures and must not be used as an offensive tool.

## Quick Use

```bash
python src/prama_cyber_contrast.py
```

The script prints a table and writes:

- `results/example_run.json`
- `examples/sample_output.txt`

In PowerShell, read generated outputs with explicit UTF-8 decoding:

```powershell
Get-Content examples\sample_output.txt -Encoding UTF8
Get-Content results\example_run.json -Encoding UTF8
```

## Interpreting The Output

`stage_count` is the discrete baseline. In the demonstration, A2/A1/A0 have 6 stages, while B/C have 8 stages, so counting alone can make B and C appear equal or higher risk.

`ACI` is the Autonomous Coupling Index, computed as mean `demand x autonomy`. PRAMA then combines coupling, persistence, intensity and recovery difficulty into a structural score. The expected ordering is:

```text
A2 > A1 > A0 >> B > C
```

## License

MIT License.  `1-15109169911`.

## Suggested Provisional Citation

© 2026. AptadinamiK G. A. C. J., ORDSPOC: Orchestration Risk Demonstrator, Structural Proof-of-Concept, 
