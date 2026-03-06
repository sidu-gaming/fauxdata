"""Export functions for fauxdata datasets."""

from __future__ import annotations

from pathlib import Path

import polars as pl


def export_dataset(df: pl.DataFrame, path: str | Path, fmt: str) -> Path:
    """Export a DataFrame to the given format and path. Returns the output path."""
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)

    if fmt == "csv":
        df.write_csv(out)
    elif fmt == "parquet":
        df.write_parquet(out)
    elif fmt == "json":
        df.write_json(out)
    elif fmt == "jsonl":
        df.write_ndjson(out)
    else:
        raise ValueError(f"Unsupported format: {fmt}. Use csv, parquet, json, or jsonl.")

    return out


def default_output_path(schema_name: str, fmt: str) -> str:
    return f"{schema_name}.{fmt}"
