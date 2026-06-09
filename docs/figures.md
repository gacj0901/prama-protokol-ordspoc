# Figure Tables

These simple Markdown tables can be transformed into figures later.

## Stage Count Comparison

| family | stage_count |
|---|---:|
| A2 autonomous orchestration extreme | 6 |
| A1 autonomous orchestration high | 6 |
| A0 autonomous orchestration moderate | 6 |
| B human-gated orchestration | 8 |
| C non-orchestrated control | 8 |

## ACI Comparison

| family | expected ACI relation |
|---|---:|
| A2 autonomous orchestration extreme | highest |
| A1 autonomous orchestration high | high |
| A0 autonomous orchestration moderate | moderate |
| B human-gated orchestration | low |
| C non-orchestrated control | lowest |

## PRAMA Risk Score Comparison

| family | expected PRAMA relation |
|---|---:|
| A2 autonomous orchestration extreme | highest |
| A1 autonomous orchestration high | lower than A2 |
| A0 autonomous orchestration moderate | lower than A1 |
| B human-gated orchestration | much lower than A0 |
| C non-orchestrated control | lowest |

## Expected Ordering

```text
A2 > A1 > A0 >> B > C
```
