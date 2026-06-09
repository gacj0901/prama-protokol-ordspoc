#!/usr/bin/env python3
"""ORDSPOC structural proof-of-concept.

Safety notice:
Esta demo no contiene técnicas de ataque, no modela procedimientos operativos y no debe usarse como herramienta ofensiva.

Method note:
This is a structural proof-of-concept, not a calibrated cyber-risk model.
"""

from __future__ import annotations

import json
from pathlib import Path
from statistics import mean

PROJECT = "ORDSPOC — Orchestration Risk Demonstrator: Structural Proof-of-Concept"
THESIS = (
    "Technique counting catalogs inventory, but autonomous orchestration is "
    "trajectory-level risk. PRAMA separates trajectories by autonomous coupling, "
    "persistence and recovery."
)
SAFETY_SCOPE = (
    "Esta demo no contiene técnicas de ataque, no modela procedimientos "
    "operativos y no debe usarse como herramienta ofensiva."
)
METHOD_NOTE = "This is a structural proof-of-concept, not a calibrated cyber-risk model."
GENERATED_AT = "2026-06-08T00:00:00Z"


def clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    """Bound a value to a closed interval."""
    return max(lower, min(upper, value))


def xi_accumulate(previous_xi: float, delta: float, retention: float = 0.72) -> float:
    """Accumulate structural load with retained, non-saturating memory."""
    return max(0.0, (previous_xi * retention) + delta)


def xi_reference(values: list[float]) -> float:
    """Return the trajectory reference load."""
    if not values:
        return 0.0
    return clamp(mean(values))


def lambda_permissivity(aci: float, xi_ref: float) -> float:
    """Estimate permissivity from autonomous coupling and retained load."""
    return clamp((0.65 * aci) + (0.35 * xi_ref))


def theta_threshold(permissivity: float) -> float:
    """Set a structural threshold lowered by permissive coupling."""
    return clamp(0.88 - (0.42 * permissivity), 0.28, 0.88)


def collapse_xi_norm(xi_ref: float, threshold: float) -> float:
    """Normalize accumulated load against the threshold surface."""
    if threshold <= 0:
        return 1.0
    collapse_xi_norm_raw = xi_ref / threshold
    return clamp(collapse_xi_norm_raw)


def orchestration_delta(stages: list[dict[str, float]]) -> list[float]:
    """Compute pointwise abstract coupling Delta(t)."""
    return [clamp(stage["demand"] * stage["autonomy"]) for stage in stages]


def autonomous_coupling_index(stages: list[dict[str, float]]) -> float:
    """ACI = mean(demand x autonomy)."""
    deltas = orchestration_delta(stages)
    return clamp(mean(deltas)) if deltas else 0.0


def baseline_count(stages: list[dict[str, float]]) -> int:
    """Discrete baseline: every stage counts equally."""
    return len(stages)


def _regime(collapse_norm: float) -> str:
    if collapse_norm >= 0.92:
        return "collapse-adjacent"
    if collapse_norm >= 0.72:
        return "critical"
    if collapse_norm >= 0.42:
        return "elevated"
    return "stable"


def _risk_level(score: float) -> str:
    if score >= 85:
        return "extreme"
    if score >= 70:
        return "high"
    if score >= 45:
        return "moderate"
    if score >= 20:
        return "low"
    return "minimal"


def assess_trajectory(stages: list[dict[str, float]]) -> dict[str, float | int | str]:
    """Assess one abstract trajectory with the minimal PRAMA core."""
    deltas = orchestration_delta(stages)
    xi_values: list[float] = []
    xi = 0.0
    for delta in deltas:
        xi = xi_accumulate(xi, delta)
        xi_values.append(xi)

    aci = autonomous_coupling_index(stages)
    intensity = clamp(max(deltas) if deltas else 0.0)
    persistence = xi_reference(xi_values)
    permissivity = lambda_permissivity(aci, persistence)
    threshold = theta_threshold(permissivity)
    collapse_raw = persistence / threshold if threshold > 0 else 0.0
    collapse_norm = collapse_xi_norm(persistence, threshold)
    recovery_gap = clamp(persistence - threshold + (0.35 * permissivity))
    irreversibility = clamp((0.7 * recovery_gap) + (0.3 * xi_values[-1] if xi_values else 0.0))

    risk_score = clamp(
        (0.30 * aci) +
        (0.18 * persistence) +
        (0.12 * intensity) +
        (0.40 * irreversibility)
    ) * 100.0

    return {
        "stage_count": baseline_count(stages),
        "ACI": round(aci, 3),
        "regime": _regime(collapse_norm),
        "risk_level": _risk_level(risk_score),
        "risk_score": round(risk_score, 1),
        "intensity": round(intensity, 3),
        "persistence": round(persistence, 3),
        "irreversibility": round(irreversibility, 3),
        "permissivity_lambda": round(permissivity, 3),
        "threshold_theta": round(threshold, 3),
        "collapse_xi_norm_raw": round(collapse_raw, 3),
        "collapse_xi_norm": round(collapse_norm, 3),
    }


def _repeat(demand: float, autonomy: float, count: int) -> list[dict[str, float]]:
    return [{"demand": demand, "autonomy": autonomy} for _ in range(count)]


def _ramp(start: float, end: float, count: int) -> list[float]:
    if count <= 1:
        return [start]
    return [start + i * (end - start) / (count - 1) for i in range(count)]


def trajectories() -> list[dict[str, object]]:
    """Return deterministic abstract trajectories."""
    e_demand = _ramp(0.57, 0.78, 8)
    e_autonomy = [0.59 + i * (0.70 - 0.59) / 7 for i in range(8)]
    return [
        {
            "family": "A2 autonomous orchestration extreme",
            "stages": _repeat(0.96, 0.96, 6),
        },
        {
            "family": "A1 autonomous orchestration high",
            "stages": _repeat(0.86, 0.88, 6),
        },
        {
            "family": "A0 autonomous orchestration moderate",
            "stages": _repeat(0.68, 0.72, 6),
        },
        {
            "family": "B human-gated orchestration",
            "stages": _repeat(0.74, 0.20, 8),
        },
        {
            "family": "C non-orchestrated control",
            "stages": _repeat(0.34, 0.06, 8),
        },
        {
            "family": "D interrupted autonomous burst",
            "stages": [
                {"demand": 0.98, "autonomy": 0.92},
                {"demand": 0.96, "autonomy": 0.90},
                {"demand": 0.35, "autonomy": 0.20},
                {"demand": 0.95, "autonomy": 0.91},
                {"demand": 0.34, "autonomy": 0.19},
                {"demand": 0.93, "autonomy": 0.90},
                {"demand": 0.32, "autonomy": 0.18},
                {"demand": 0.30, "autonomy": 0.17},
            ],
        },
        {
            "family": "E sustained escalation without recovery",
            "stages": [
                {"demand": demand, "autonomy": autonomy}
                for demand, autonomy in zip(e_demand, e_autonomy)
            ],
        },
    ]


def build_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for item in trajectories():
        stages = item["stages"]
        assert isinstance(stages, list)
        metrics = assess_trajectory(stages)
        rows.append({"family": item["family"], **metrics})
    return rows


def render_table(rows: list[dict[str, object]]) -> str:
    columns = [
        "family",
        "stage_count",
        "ACI",
        "regime",
        "risk_level",
        "risk_score",
        "intensity",
        "persistence",
        "collapse_raw",
        "irreversibility",
    ]
    widths = {column: len(column) for column in columns}
    for row in rows:
        row["collapse_raw"] = row["collapse_xi_norm_raw"]
        for column in columns:
            widths[column] = max(widths[column], len(str(row[column])))

    lines = [SAFETY_SCOPE, METHOD_NOTE, ""]
    header = " | ".join(column.ljust(widths[column]) for column in columns)
    divider = "-+-".join("-" * widths[column] for column in columns)
    lines.extend([header, divider])
    for row in rows:
        lines.append(" | ".join(str(row[column]).ljust(widths[column]) for column in columns))
    return "\n".join(lines)


def write_artifacts(rows: list[dict[str, object]], output: str) -> None:
    root = Path(__file__).resolve().parents[1]
    (root / "results").mkdir(exist_ok=True)
    (root / "examples").mkdir(exist_ok=True)

    serializable_rows = []
    for row in rows:
        serializable_rows.append(dict(row))

    payload = {
        "project": PROJECT,
        "generated_at": GENERATED_AT,
        "thesis": THESIS,
        "safety_scope": SAFETY_SCOPE,
        "trajectories": serializable_rows,
        "summary_ordering": [
            "A2 autonomous orchestration extreme",
            "A1 autonomous orchestration high",
            "A0 autonomous orchestration moderate",
            "E sustained escalation without recovery",
            "D interrupted autonomous burst",
            "B human-gated orchestration",
            "C non-orchestrated control",
        ],
        "method_note": METHOD_NOTE,
    }

    with (root / "results" / "example_run.json").open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    (root / "examples" / "sample_output.txt").write_text(output + "\n", encoding="utf-8")


def main() -> None:
    rows = build_rows()
    output = render_table(rows)
    print(output)
    write_artifacts(rows, output)


if __name__ == "__main__":
    main()
