"""fauxdata CLI entry point."""

from __future__ import annotations

from typing import Optional

import pyfiglet
import typer
from rich import print as rprint
from rich.console import Console

app = typer.Typer(
    name="fauxdata",
    help="Generate and validate fake datasets from YAML schemas.",
    add_completion=False,
    no_args_is_help=True,
)
console = Console()


def _banner():
    banner = pyfiglet.figlet_format("fauxdata", font="slant")
    rprint(f"[bold cyan]{banner}[/bold cyan]")
    rprint("[dim]Generate and validate realistic fake datasets[/dim]\n")


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        _banner()


@app.command("init")
def init_cmd(
    name: Optional[str] = typer.Option(None, "--name", "-n", help="Schema name"),
):
    """Create a schema template interactively."""
    from fauxdata.commands.init import run
    run(name=name)


@app.command("generate")
def generate_cmd(
    schema: str = typer.Argument(..., help="Path to YAML schema file"),
    rows: Optional[int] = typer.Option(None, "--rows", "-r", help="Number of rows to generate"),
    out: Optional[str] = typer.Option(None, "--out", "-o", help="Output file path"),
    fmt: Optional[str] = typer.Option(None, "--format", "-f", help="Output format: csv, parquet, json, jsonl"),
    seed: Optional[int] = typer.Option(None, "--seed", "-s", help="Random seed for reproducibility"),
    validate: bool = typer.Option(False, "--validate", "-v", help="Run validation after generating"),
):
    """Generate a fake dataset from a YAML schema."""
    from fauxdata.commands.generate import run
    run(schema_path=schema, rows=rows, out=out, fmt=fmt, seed=seed, validate=validate)


@app.command("validate")
def validate_cmd(
    dataset: str = typer.Argument(..., help="Path to dataset file (csv, parquet, json, jsonl)"),
    schema: str = typer.Argument(..., help="Path to YAML schema file"),
):
    """Validate an existing dataset against a YAML schema."""
    from fauxdata.commands.validate import run
    run(dataset_path=dataset, schema_path=schema)


@app.command("preview")
def preview_cmd(
    dataset: str = typer.Argument(..., help="Path to dataset file"),
    rows: int = typer.Option(10, "--rows", "-r", help="Number of rows to preview"),
):
    """Show a preview and column statistics for a dataset."""
    from fauxdata.commands.preview import run
    run(dataset_path=dataset, rows=rows)
