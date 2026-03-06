"""fauxdata preview command."""

from __future__ import annotations

import polars as pl
import typer
from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def run(dataset_path: str, rows: int = 10):
    """Show a preview of a dataset with column statistics."""
    rprint(Panel(f"[bold cyan]fauxdata preview[/bold cyan]  [dim]{dataset_path}[/dim]", expand=False))

    ext = dataset_path.rsplit(".", 1)[-1].lower()
    if ext == "csv":
        df = pl.read_csv(dataset_path)
    elif ext == "parquet":
        df = pl.read_parquet(dataset_path)
    elif ext == "json":
        df = pl.read_json(dataset_path)
    elif ext in ("jsonl", "ndjson"):
        df = pl.read_ndjson(dataset_path)
    else:
        rprint(f"[red]Unsupported file format: .{ext}[/red]")
        raise typer.Exit(code=1)

    rprint(f"  [bold]{len(df)}[/bold] rows × [bold]{len(df.columns)}[/bold] columns\n")

    # Data preview table
    preview_df = df.head(rows)
    t = Table(title=f"First {min(rows, len(df))} rows", show_header=True, header_style="bold magenta")

    for col in preview_df.columns:
        t.add_column(col, overflow="fold", max_width=25)

    for row in preview_df.iter_rows():
        t.add_row(*[str(v) if v is not None else "[dim]null[/dim]" for v in row])

    console.print(t)

    # Column stats
    stats_t = Table(title="Column Statistics", show_header=True, header_style="bold cyan")
    stats_t.add_column("Column", style="cyan")
    stats_t.add_column("Type")
    stats_t.add_column("Nulls", justify="right")
    stats_t.add_column("Unique", justify="right")
    stats_t.add_column("Min")
    stats_t.add_column("Max")

    for col in df.columns:
        series = df[col]
        dtype = str(series.dtype)
        nulls = str(series.null_count())
        unique = str(series.n_unique())

        try:
            if series.dtype in (pl.Int8, pl.Int16, pl.Int32, pl.Int64,
                                 pl.UInt8, pl.UInt16, pl.UInt32, pl.UInt64,
                                 pl.Float32, pl.Float64):
                col_min = str(series.min())
                col_max = str(series.max())
            elif series.dtype == pl.Date or series.dtype == pl.Datetime:
                col_min = str(series.min())
                col_max = str(series.max())
            else:
                col_min = "-"
                col_max = "-"
        except Exception:
            col_min = "-"
            col_max = "-"

        stats_t.add_row(col, dtype, nulls, unique, col_min, col_max)

    console.print(stats_t)
