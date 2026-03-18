from __future__ import annotations

import re
import warnings
from typing import Any, Dict, List

# Domain heuristics for multi-domain reasoning
DOMAIN_HINTS = {
    "D1": ["ingest", "parser", "udm", "forwarder", "log", "collection", "agent"],
    "D2": ["yara", "rule", "query", "detect", "detection", "correlation", "alert"],
    "D3": ["api", "sdk", "integration", "endpoint", "connector", "plugin"],
    "D4": ["threat intel", "ioc", "misp", "virustotal", "c2", "malware"],
    "D5": ["mitre", "attack", "tactic", "technique", "framework", "mapping"],
    "D6": ["soar", "playbook", "automation", "response", "incident", "remediation"],
    "D7": ["asset", "discovery", "inventory", "surface", "enumerate"],
    "D8": ["vulnerability", "cve", "patch", "exploit", "weakness"],
    "D9": ["gap", "risk", "assessment", "coverage", "score", "posture"],
}


def infer_primary_domain(text: str) -> str:
    """Infer primary domain from text hints."""
    low = text.lower()
    best = "D9"
    best_score = 0
    for domain, hints in DOMAIN_HINTS.items():
        score = sum(1 for h in hints if h in low)
        if score > best_score:
            best_score = score
            best = domain
    return best


def infer_secondary_domains(text: str) -> List[str]:
    """Infer secondary domains (related but not primary)."""
    low = text.lower()
    scores = {}
    for domain, hints in DOMAIN_HINTS.items():
        score = sum(1 for h in hints if h in low)
        if score > 0:
            scores[domain] = score

    primary = infer_primary_domain(text)
    secondary = [d for d, _ in sorted(scores.items(), key=lambda x: -x[1]) if d != primary][:2]
    return secondary


def extract_signals(text: str) -> List[Dict[str, str]]:
    """Extract candidate telemetry signals from detection text."""
    signals: List[Dict[str, str]] = []

    event_patterns = re.findall(r"Event (?:ID )?\d{4,5}|EID \d{4,5}", text, re.IGNORECASE)
    for ep in set(event_patterns):
        signals.append(
            {
                "name": f"windows_{ep.lower().replace(' ', '_')}",
                "source": ep,
                "description": f"Windows event: {ep}",
                "criticality": "primary",
            }
        )

    telemetry_keywords = {
        "sysmon": "Sysmon event logs",
        "edr": "EDR telemetry",
        "firewall": "Network firewall logs",
        "dns": "DNS query logs",
        "http": "HTTP/HTTPS traffic logs",
        "process execution": "Process execution events",
        "file activity": "File system activity",
        "registry": "Windows registry changes",
        "network connection": "Network connection logs",
        "auth": "Authentication/login events",
        "script": "Script execution logs",
        "api call": "API call logs",
    }
    low = text.lower()
    for keyword, description in telemetry_keywords.items():
        if keyword in low:
            signals.append(
                {
                    "name": keyword.replace(" ", "_"),
                    "source": description,
                    "description": f"Captures {description.lower()}",
                    "criticality": "supporting",
                }
            )

    if signals:
        return signals
    return [
        {
            "name": "generic_process_execution",
            "source": "EDR / SIEM",
            "description": "Process execution and parent-child relationships",
            "criticality": "primary",
        }
    ]


def extract_mitre_techniques(text: str) -> List[Dict[str, str]]:
    """Extract MITRE ATT&CK technique references."""
    techniques: List[Dict[str, str]] = []
    patterns = re.findall(r"T\d{4}(?:\.\d{3})?", text)

    tactic_map = {
        "1059": "execution",
        "1085": "defense-evasion",
        "1197": "defense-evasion",
    }

    for tid in set(patterns):
        base_tid = tid.split(".")[0]
        tactic = tactic_map.get(base_tid, "execution")
        techniques.append({"technique_id": tid, "tactic": tactic, "description": f"MITRE technique {tid}"})

    if techniques:
        return techniques
    return [
        {
            "technique_id": "T1059.001",
            "tactic": "execution",
            "description": "Command and Scripting Interpreter: PowerShell",
        }
    ]


def extract_udm_fields(text: str) -> List[Dict[str, Any]]:
    """Extract potential UDM or detection schema fields."""
    fields: List[Dict[str, Any]] = []
    field_patterns = re.findall(r"([a-zA-Z_]+\.[a-zA-Z0-9_\.]+)", text)

    known_fields = {
        "process.name": "Executable name",
        "process.parent.name": "Parent process name",
        "process.command_line": "Full command line",
        "file.name": "File name",
        "file.path": "File system path",
        "file.hashes": "File hash values",
        "network.dns.question": "DNS query domain",
        "network.ip_traffic.src_ref": "Source IP address",
        "resource.name": "Resource/asset name",
    }

    seen = set()
    for fp in field_patterns:
        if fp not in seen and fp in known_fields:
            fields.append(
                {
                    "field_name": fp,
                    "source": known_fields[fp],
                    "description": f"UDM field for {known_fields[fp].lower()}",
                    "examples": [],
                }
            )
            seen.add(fp)

    if fields:
        return fields

    return [
        {
            "field_name": "process.name",
            "source": "Process execution logs",
            "description": "Executable name from process event",
            "examples": ["powershell.exe", "cmd.exe", "notepad.exe"],
        },
        {
            "field_name": "process.command_line",
            "source": "Process execution logs",
            "description": "Full command line arguments",
            "examples": [],
        },
    ]


def build_workflow_reasoning_unit(doc: Dict[str, Any]) -> Dict[str, Any]:
    """Transform raw detection docs into structured workflow reasoning traces."""
    text = doc["text"]
    title = doc["title"]
    path = doc["path"]

    primary = infer_primary_domain(text)
    secondary = infer_secondary_domains(text)
    signals = extract_signals(text)
    techniques = extract_mitre_techniques(text)
    fields = extract_udm_fields(text)

    threat_behavior = (
        f"Adversary attempting {title.lower()} using techniques to evade detection and maintain persistence"
    )

    return {
        "threat_scenario": title,
        "source_corpus": path,
        "signals": signals,
        "correlation": {
            "threat_behavior": threat_behavior,
            "mitre_techniques": techniques,
            "reasoning": (
                f"The threat {title.lower()} aligns with "
                f"{', '.join(t['technique_id'] for t in techniques[:2])} and requires correlation "
                "across multiple signal sources to reliably detect."
            ),
        },
        "udm_mapping": {
            "fields": fields,
            "query_template": (
                f"SELECT * FROM logs WHERE {fields[0]['field_name'] if fields else 'process.name'} "
                "AND correlation_window < 5m"
            ),
        },
        "gap_analysis": {
            "current_coverage": (
                f"Standard {primary} domain tools likely capture {signals[0]['source']} events."
            ),
            "missing_gaps": [
                {
                    "gap": f"Detection of {signals[i]['name']}",
                    "impact": "High false negatives if adversary uses evasion",
                    "requirement": f"Enable {signals[i]['source']}",
                    "priority": "high" if i == 0 else "medium",
                }
                for i in range(min(2, len(signals)))
            ],
            "recommendations": [
                {
                    "recommendation": (
                        f"Correlate {signals[0]['source']} with file system changes within 5m window"
                    ),
                    "effort": "medium",
                    "preconditions": "File system logging must be enabled",
                },
                {
                    "recommendation": (
                        f"Create allowlist for {title.lower()} scenarios in "
                        f"{secondary[0] if secondary else 'D6'} domain"
                    ),
                    "effort": "low",
                    "preconditions": "Known benign processes must be documented",
                },
            ],
        },
        "rule_logic": {
            "rule_name": f"detect_{title.lower().replace(' ', '_')}",
            "evidence": [
                {
                    "evidence_type": signals[i]["name"],
                    "condition": f"{signals[i]['source']} with anomalous pattern",
                    "source": signals[i]["source"],
                }
                for i in range(min(2, len(signals)))
            ],
            "correlation_logic": "all_present_within 5m",
            "alert_confidence": "high",
        },
        "implementation_code": {
            "rule_format": "udm_query",
            "code_snippet": (
                f"rule: detect_{title.lower().replace(' ', '_')}\n"
                "evidence:\n"
                f"  - signal_1: [{fields[0]['field_name'] if fields else 'process.name'} = 'suspicious']\n"
                "  - signal_2: [correlation_window < 5m]\n"
                "correlation: all_present\n"
                "alert_confidence: high\n"
            ),
            "comments": "Adjust fields and thresholds based on your environment.",
        },
        "validation": {
            "assumptions": [
                f"All {signals[0]['source']} sources are enabled and ingested",
                "Time sync across all collection points is accurate",
                "Baseline of normal behavior for your environment is established",
            ],
            "false_positive_mitigation": [
                {
                    "fp_scenario": f"Legitimate {title.lower()} activity from approved processes",
                    "mitigation": "Whitelist known-good executables and process paths",
                },
                {
                    "fp_scenario": "High-volume legitimate activity overwhelming alert queue",
                    "mitigation": "Add time-based thresholds or rate limits",
                },
            ],
            "constraints": [
                {
                    "constraint": f"Requires {', '.join(s['source'] for s in signals[:2])} collection",
                    "impact": "Cannot detect if these sources are disabled",
                },
                {
                    "constraint": "5-minute correlation window may miss fast attacks",
                    "impact": "Consider reducing window if latency permits",
                },
            ],
        },
        "metadata": {
            "source_corpus": path,
            "threat_category": title,
            "domain": primary,
            "secondary_domains": secondary,
            "example_type": "positive",
        },
    }


def distill_docs_to_workflow_reasoning_units(docs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [build_workflow_reasoning_unit(d) for d in docs]


# Backward-compatible wrappers (deprecated)
def infer_domain(text: str) -> str:
    warnings.warn("infer_domain() is deprecated; use infer_primary_domain()", DeprecationWarning, stacklevel=2)
    return infer_primary_domain(text)


def build_reasoning_unit(doc: Dict[str, Any]) -> Dict[str, Any]:
    warnings.warn(
        "build_reasoning_unit() is deprecated; use build_workflow_reasoning_unit()",
        DeprecationWarning,
        stacklevel=2,
    )
    return build_workflow_reasoning_unit(doc)


def distill_docs_to_reasoning_units(docs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    warnings.warn(
        "distill_docs_to_reasoning_units() is deprecated; use distill_docs_to_workflow_reasoning_units()",
        DeprecationWarning,
        stacklevel=2,
    )
    return distill_docs_to_workflow_reasoning_units(docs)
