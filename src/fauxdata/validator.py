"""Validation of datasets using pointblank."""

from __future__ import annotations

import pointblank as pb
import polars as pl

from fauxdata.schema import SchemaConfig, ValidationRule


def validate_dataset(df: pl.DataFrame, schema: SchemaConfig) -> tuple[bool, list[dict]]:
    """
    Run pointblank validation rules against df.
    Returns (all_passed, results_list).
    """
    if not schema.validation_rules:
        return True, []

    v = pb.Validate(
        data=df,
        tbl_name=schema.name,
        thresholds=pb.Thresholds(warning=1),
    )

    for rule in schema.validation_rules:
        _add_rule(v, rule)

    v.interrogate()

    all_passed = v.all_passed()
    results = _extract_results(v, schema.validation_rules)
    return all_passed, results


def _add_rule(v: pb.Validate, rule: ValidationRule) -> None:
    r = rule.rule

    if r == "col_vals_not_null":
        cols = rule.columns or ([rule.column] if rule.column else [])
        for col in cols:
            v.col_vals_not_null(columns=col)

    elif r == "col_vals_between":
        v.col_vals_between(columns=rule.column, left=rule.min, right=rule.max)

    elif r == "col_vals_gt":
        v.col_vals_gt(columns=rule.column, value=rule.min)

    elif r == "col_vals_lt":
        v.col_vals_lt(columns=rule.column, value=rule.max)

    elif r == "col_vals_ge":
        v.col_vals_ge(columns=rule.column, value=rule.min)

    elif r == "col_vals_le":
        v.col_vals_le(columns=rule.column, value=rule.max)

    elif r == "col_vals_regex":
        v.col_vals_regex(columns=rule.column, pattern=rule.pattern)

    elif r == "col_vals_in_set":
        v.col_vals_in_set(columns=rule.column, set=rule.values)

    elif r == "rows_distinct":
        cols = rule.columns or ([rule.column] if rule.column else None)
        v.rows_distinct(columns_subset=cols)

    elif r == "col_exists":
        cols = rule.columns or ([rule.column] if rule.column else [])
        for col in cols:
            v.col_exists(columns=col)


def _extract_results(v: pb.Validate, rules: list[ValidationRule]) -> list[dict]:
    """Extract per-step results as a list of dicts."""
    results = []
    # Build a flat list of steps (one per column for multi-column rules)
    step = 1
    for rule in rules:
        if rule.rule in ("col_vals_not_null", "col_exists"):
            cols = rule.columns or ([rule.column] if rule.column else [])
            for col in cols:
                results.append(_get_step(v, step, rule.rule, col))
                step += 1
        else:
            col = rule.column or (", ".join(rule.columns) if rule.columns else "-")
            results.append(_get_step(v, step, rule.rule, col))
            step += 1
    return results


def _get_step(v: pb.Validate, i: int, rule: str, column: str) -> dict:
    try:
        passed = v.n_passed(i=i, scalar=True) or 0
        failed = v.n_failed(i=i, scalar=True) or 0
    except Exception:
        passed = 0
        failed = 0
    total = passed + failed
    return {
        "step": i,
        "rule": rule,
        "column": column,
        "passed": passed,
        "failed": failed,
        "total": total,
        "ok": failed == 0,
    }
