"""fauxdata validate command."""

from __future__ import annotations

import polars as pl
import typer
from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from fauxdata.schema import load_schema
from fauxdata.validator import validate_dataset

console = Console()


def run(dataset_path: str, schema_path: str):
    """Validate an existing dataset against a YAML schema."""
    schema = load_schema(schema_path)

    rprint(Panel(
        f"[bold cyan]fauxdata validate[/bold cyan]  [dim]{dataset_path}[/dim]",
        expand=False,
    ))

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

    rprint(f"  Loaded [bold]{len(df)}[/bold] rows, [bold]{len(df.columns)}[/bold] columns")

    if not schema.validation_rules:
        rprint("[yellow]No validation rules defined in schema.[/yellow]")
        raise typer.Exit()

    all_passed, results = validate_dataset(df, schema)

    t = Table(title="Validation Results", show_header=True, header_style="bold")
    t.add_column("#")
    t.add_column("Rule", style="cyan")
    t.add_column("Column")
    t.add_column("Passed", justify="right")
    t.add_column("Failed", justify="right")
    t.add_column("Status")

    for r in results:
        status = "[green]PASS[/green]" if r["ok"] else "[red]FAIL[/red]"
        t.add_row(
            str(r["step"]),
            r["rule"],
            r["column"],
            str(r["passed"]),
            str(r["failed"]),
            status,
        )

    console.print(t)

    if all_passed:
        rprint("[bold green]All validation rules passed.[/bold green]")
    else:
        rprint("[bold red]Some validation rules failed.[/bold red]")
        raise typer.Exit(code=1)
