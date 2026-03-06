# fauxdata

CLI for generating and validating realistic fake datasets from YAML schemas.

Uses [pointblank](https://github.com/posit-dev/pointblank) for both generation and validation.

## Install

```bash
uv sync
```

## Usage

```bash
# Create a schema template
uv run fauxdata init --name people

# Generate a dataset
uv run fauxdata generate schemas/people.yml --rows 1000 --validate

# Validate an existing dataset
uv run fauxdata validate output.csv schemas/people.yml

# Preview a dataset
uv run fauxdata preview output.csv --rows 10
```

## Schema format

```yaml
name: people
description: "People dataset"
rows: 1000
seed: 42
locale: IT          # ISO country code for locale-aware generation

output:
  format: csv       # csv | parquet | json | jsonl
  path: people.csv

columns:
  id:
    type: int
    unique: true
    min: 1
    max: 99999

  name:
    type: string
    preset: name    # name, email, phone_number, city, country_code_2, company, job, uuid4, ipv4...

  age:
    type: int
    min: 18
    max: 90

  status:
    type: string
    values: [active, inactive, pending]   # enum / allowed values

  active:
    type: bool

  signup_date:
    type: date
    min: "2020-01-01"
    max: "2024-12-31"

  score:
    type: float
    min: 0.0
    max: 100.0

validation:
  - rule: col_vals_not_null
    columns: [id, name, email]
  - rule: col_vals_between
    column: age
    min: 18
    max: 90
  - rule: col_vals_regex
    column: email
    pattern: "^[^@]+@[^@]+\\.[^@]+$"
  - rule: rows_distinct
    columns: [id]
```

## Available string presets

`name`, `name_full`, `first_name`, `last_name`, `email`, `phone_number`, `address`, `city`, `state`, `country`, `country_code_2`, `country_code_3`, `postcode`, `company`, `job`, `url`, `domain_name`, `ipv4`, `ipv6`, `user_name`, `text`, `sentence`, `word`, `iban`, `currency_code`, `uuid4`, `md5`, `ssn`, `license_plate`
