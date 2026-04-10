# BlueForge UI: React Command Center Design Spec

## Objective
Build a professional, secure React-based GUI for BlueForge AI that acts as a control plane for the Infisical-integrated GitHub Actions.

## Core Components
- **VaultGate (Authentication):** Handles Infisical OIDC trust and GitHub PAT storage (session only).
- **Dispatcher (Execution):** JSON-aware task editor that triggers `workflow_dispatch`.
- **Observer (Monitoring):** Real-time dashboard that polls GitHub Action runs and telemetry.

## Security Model (OIDC-First)
- **Zero Secrets in Logs:** Secrets are pulled directly from Infisical by the runner using OIDC.
- **BYOK (Bring Your Own Key):** Users configure OIDC trust in Infisical for their fork.
- **Ephemeral PAT:** GitHub PAT is provided by the user in the UI and used only for dispatch.

## Technical Stack
- **Frontend:** React (Vite), Tailwind CSS, Lucide Icons, Recharts.
- **Backend (Serverless):** GitHub Actions (Compute), GitHub API (Dispatch), Infisical (Vault).

## Implementation Plan
1. **Initialize UI:** Scaffold `dashboard/ui/` with Vite/React/Tailwind.
2. **OIDC Runner:** Refactor `.github/workflows/automation.yml` to use OIDC authentication with Infisical.
3. **Dispatch Logic:** Implement the GitHub API bridge in the React app.
4. **Telemetry Relay:** Create a utility to push runner status to a "status" branch for UI polling.
