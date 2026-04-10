# Gemma 4 Swarm & Training Pipeline Refactor Design

## Objective
Refactor the Agentic SOC Factory to support Gemma 4 (E2B/E4B) with a focus on platform-agnostic training and robust telemetry.

## Architecture
- **Ingestion:** `SigmaGitHubScraper` for vendor-neutral detection logic.
- **Training:** Google Drive-based MCP relay to Google Colab.
- **Telemetry:** `PipelineHealthCheck` (dataset size/schema) and `SignalDriftDetector` (Jaccard-based content drift).
- **Dashboard:** Tabbed Streamlit view for Loss Curves, GPU usage, and Pipeline Health.
- **Swarm Agents:**
    - `ThreatHunter`: Indicator extraction from raw docs.
    - `PlatformTranslator`: SPL to KQL (and others) translation.
    - `GapAnalysisAgent`: Detection coverage gap identification.
    - `SelfHealingAgent`: Autonomous data pipeline correction.

## Technical Details
- **Language:** Python 3.10+
- **Data Stores:** SQLite (`artifacts/factory.db`)
- **Key Files:**
    - `agentic_soc_factory/telemetry/health.py`: Health & Drift logic.
    - `agentic_soc_factory/ingestion/web_scraper.py`: Platform-agnostic scraping.
    - `agentic_soc_factory/training/colab_mcp_client.py`: GDrive bridge.
    - `agentic_soc_factory/agents/factory_agents.py`: Gemma-optimized swarm.

## Verification
- All new components verified via TDD in `tests/`.
- Dashboard updated to visualize new telemetry tables.
- Scraper successfully parses Sigma YAML to internal `workflow_unit` schema.
