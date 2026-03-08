# Detection Engineering LLM Factory

This repository implements a cloud-native, semi-automated pipeline that continuously converts SOC detection engineering documentation into evaluated LLM artifacts.

## Architecture

Pipeline stages:

1. SOC document ingestion
2. reasoning distillation
3. dataset construction + quality gates
4. automation supervisor
5. routed LLM provider calls
6. scheduled training jobs
7. telemetry + event tracking
8. evaluation harness
9. model export (GGUF/Ollama)
10. dashboard monitoring

Core flow:

`secops_rag -> pipeline -> supervisor -> routing/providers -> automation daemon -> Colab training -> drive telemetry/events -> evaluation -> GGUF export -> Streamlit dashboard`

## Repository Layout

```text
agentic_soc_factory/
  agents/
  automation/
  evaluation/
  export/
  pipeline/
  reporting/
  routing/
  cli.py

dashboard/
  app.py

colab/
  qwen35_4b_qlora_free_colab.ipynb

config/
  automation.yaml
  routing.yaml
  providers.yaml

secops_rag/
artifacts/
schemas/
tests/
```

## Cloud Setup

### 1) Install dependencies

```bash
pip install -r requirements.txt
```

### 2) Configure environment

Copy `.env.example` to `.env` and set provider credentials, SMTP settings, and optional Google Drive values.

### 3) Stable CLI entrypoint

```bash
python -m agentic_soc_factory.cli <command>
```

Supported commands:

- `supervisor`
- `daemon`
- `daemon-once`
- `event-api`
- `export`

### 4) SQLite run state

Database path: `artifacts/factory.db`

Required tables are created on startup:

- `jobs`
- `events`
- `notifications`
- `training_telemetry`

### 5) Colab training + telemetry contract

Notebook: `colab/qwen35_4b_qlora_free_colab.ipynb`

Telemetry file format:

`{run_id}_telemetry.json`

Required fields:

- `run_id`
- `phase`
- `step`
- `loss`
- `gpu_minutes`
- `status`
- `timestamp`
- `artifact`

Automation lifecycle states:

`queued -> running -> waiting_colab -> training -> export -> eval -> completed/failed`

## GitHub Actions Automation

Workflow: `.github/workflows/automation.yml`

What it does daily:

1. installs dependencies
2. runs `daemon-once`
3. polls telemetry/state from SQLite
4. optionally downloads Drive artifacts
5. uploads artifacts/reports as workflow artifacts

Required GitHub secrets (as applicable):

- `GOOGLE_DRIVE_FOLDER_ID`
- `GOOGLE_DRIVE_CREDENTIALS_JSON`

## Streamlit Cloud Deployment

Dashboard app: `dashboard/app.py`

The dashboard reads from `artifacts/factory.db` and shows:

- active runs
- run state
- telemetry metrics
- event timeline
- evaluation results

For hosted environments, mount/sync `artifacts/factory.db` into the app runtime (or sync telemetry/artifacts from Drive before app start).

## Typical Operations

Run one automation cycle:

```bash
python -m agentic_soc_factory.cli daemon-once --tasks tasks.sample.json --corpus-root secops_rag --db artifacts/factory.db --artifacts-root artifacts --profile default
```

Run long-lived scheduler:

```bash
python -m agentic_soc_factory.cli daemon --tasks tasks.sample.json --corpus-root secops_rag --db artifacts/factory.db --artifacts-root artifacts --profile default
```

Start event API:

```bash
python -m agentic_soc_factory.cli event-api --db artifacts/factory.db --host 0.0.0.0 --port 8787
```
