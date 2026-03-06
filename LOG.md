# Log

## 2026-03-06

- Initial implementation of `fauxdata` CLI
- Stack: pointblank 0.22 (native generation + validation), polars, typer, rich, pyfiglet, questionary
- Commands: `init`, `generate`, `validate`, `preview`
- Example schemas: `people.yml`, `orders.yml`, `events.yml`
- All schemas generate and validate cleanly (all rules PASS)
- `locale` field at schema level maps to pointblank `country=` param
