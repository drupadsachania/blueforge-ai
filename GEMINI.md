# Detection Engineering LLM Factory - GEMINI.md

This project is a cloud-native, semi-automated pipeline designed to continuously convert SOC (Security Operations Center) detection engineering documentation into fine-tuned, evaluated LLM artifacts.

## Project Overview

The "Agentic SOC Factory" automates the lifecycle of transforming raw security documentation into specialized language models (like Qwen-3.5 4B) optimized for detection engineering tasks.

### Core Architecture & Flow
1.  **Ingestion:** Scans `secops_rag/` for markdown documentation.
2.  **Distillation:** Uses LLMs to distill documentation into "reasoning units."
3.  **Dataset Construction:** Compiles units into JSONL datasets with quality gates (deduplication, schema validation, and leakage/overlap checks).
4.  **Orchestration:** Managed by either a `FactorySupervisorAgent` (direct run) or `FactoryAutomationDaemon` (scheduled/continuous runs).
5.  **Routing & Providers:** Dispatches LLM calls to OpenAI, Anthropic, Gemini, or Ollama with built-in circuit breaking and fallback logic.
6.  **Training:** Integrates with Google Colab for QLoRA fine-tuning, using Google Drive for telemetry and artifact exchange.
7.  **Evaluation:** Runs evaluation suites to verify model performance.
8.  **Export:** Converts fine-tuned weights to GGUF format and generates Ollama Modelfiles.
9.  **Monitoring:** A Streamlit dashboard provides visibility into run states, telemetry, and event timelines.

### Key Technologies
- **Language:** Python 3.10+ (using `from __future__ import annotations`).
- **Data Stores:** SQLite (`artifacts/factory.db`) for run state, jobs, and telemetry.
- **Web/API:** FastAPI (event ingestion) and Streamlit (monitoring dashboard).
- **LLM Integration:** OpenAI, Anthropic, Google Gemini, and Ollama (local GGUF).
- **Validation:** Pydantic and JSON Schema.

---

## Building and Running

### Prerequisites
- Python 3.10 or higher.
- API keys for relevant LLM providers (configured in `.env`).

### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your credentials
```

### Key Commands
The project uses `agentic_soc_factory.cli` as the main entry point.

| Task | Command |
| :--- | :--- |
| **Run Once** | `python -m agentic_soc_factory.cli daemon-once` |
| **Start Scheduler** | `python -m agentic_soc_factory.cli daemon` |
| **Run Supervisor** | `python -m agentic_soc_factory.cli supervisor --tasks tasks.sample.json` |
| **Event API** | `python -m agentic_soc_factory.cli event-api --port 8787` |
| **Dashboard** | `streamlit run dashboard/app.py` |
| **Testing** | `pytest` |
| **GGUF Export** | `python -m agentic_soc_factory.cli export --merged-model-dir <dir> --gguf-out <file>` |

---

## Development Conventions

### 1. Agent-Based Pipeline
The logic is modularized into specialized agents located in `agentic_soc_factory/agents/factory_agents.py`:
- `DocDistillerAgent`: Handles documentation ingestion and distillation.
- `DatasetBuilderAgent`: Creates training/validation datasets.
- `ModelRouterAgent`: Implements the routing policy.
- `CostGovernorAgent`: Tracks token usage and costs.
- `EvalAgent`: Executes evaluation suites.

### 2. Configuration Strategy
- **JSON-as-YAML:** Files in `config/` (e.g., `routing.yaml`, `providers.yaml`) are actually stored as JSON for dependency-free parsing via `json.loads()`.
- **Environment Variables:** Used for secrets and path overrides (e.g., `FACTORY_DB_PATH`).

### 3. Data Integrity
- All dataset records must validate against schemas in the `schemas/` directory.
- `artifacts/factory.db` is the source of truth for all automation state and telemetry.

### 4. Code Style
- Strict use of type hints and `dataclasses`.
- Modular architecture with clear separation between `pipeline`, `routing`, `providers`, and `automation`.
- Comprehensive testing via `pytest`, including integration dry runs and edge case validation.
