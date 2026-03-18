"""
Data Generation Toolkit for Workflow Reasoning Examples

This module provides factories for creating synthetic and semi-synthetic
detection workflow examples for SFT training.

Strategies:
1. Real-world mining: Extract from existing detection rules/docs
2. Synthetic generation: Build from threat models (MITRE ATT&CK)
3. Augmentation: Create negative/boundary variants from positive examples
"""

from typing import Dict, List, Any
import json
from dataclasses import dataclass


@dataclass
class ThreatScenario:
    """Base threat scenario metadata."""
    name: str
    description: str
    mitre_techniques: List[Dict[str, str]]
    primary_domain: str
    secondary_domains: List[str]


# ============================================================================
# MITRE ATT&CK-based Generation (Synthetic)
# ============================================================================

MITRE_THREATS = {
    "T1059.001": {
        "name": "Command and Scripting Interpreter: PowerShell",
        "description": "Attacker executes commands via PowerShell to maintain access or perform reconnaissance",
        "tactic": "execution",
        "typical_signals": ["process_execution", "script_block_logging", "command_line_auditing"],
        "typical_gaps": ["script_content_inspection", "obfuscation_detection"],
        "primary_domain": "D2",  # Detection/rules
        "secondary_domains": ["D5", "D9"],  # ATT&CK mapping, gap analysis
    },
    "T1087.001": {
        "name": "Account Discovery: Local Account",
        "description": "Adversary enumerates local user accounts for lateral movement planning",
        "tactic": "discovery",
        "typical_signals": ["process_execution", "api_call_logs", "wmi_activity"],
        "typical_gaps": ["baseline_of_normal_discovery"],
        "primary_domain": "D2",
        "secondary_domains": ["D7", "D9"],  # Asset discovery, gap analysis
    },
    "T1547.001": {
        "name": "Boot or Logon Autostart Execution: Registry Run Keys",
        "description": "Adversary modifies registry to achieve persistence across reboots",
        "tactic": "persistence",
        "typical_signals": ["registry_modification", "process_execution", "file_creation"],
        "typical_gaps": ["registry_content_monitoring", "real_time_alerting"],
        "primary_domain": "D2",
        "secondary_domains": ["D8", "D9"],  # Vulnerability assessment, gap analysis
    },
}


def generate_from_mitre_technique(technique_id: str) -> Dict[str, Any]:
    """
    Generate a workflow reasoning unit from a MITRE technique.
    This is synthetic but reflects real-world detection patterns.
    """
    if technique_id not in MITRE_THREATS:
        raise ValueError(f"Unknown technique: {technique_id}")
    
    threat = MITRE_THREATS[technique_id]
    
    return {
        "threat_scenario": threat["name"],
        "source_corpus": f"synthetic/mitre/{technique_id}",
        
        "signals": [
            {
                "name": sig.lower().replace(" ", "_"),
                "source": f"Windows / EDR ({sig})",
                "description": f"Monitors {sig.lower()}",
                "criticality": "primary" if i == 0 else "supporting"
            }
            for i, sig in enumerate(threat["typical_signals"])
        ],
        
        "correlation": {
            "threat_behavior": threat["description"],
            "mitre_techniques": [
                {
                    "technique_id": technique_id,
                    "tactic": threat["tactic"],
                    "description": threat["name"]
                }
            ],
            "reasoning": f"This {threat['tactic']} behavior requires correlation across "
                        f"{', '.join(threat['typical_signals'][:2])} to reliably detect."
        },
        
        "udm_mapping": {
            "fields": [
                {
                    "field_name": "process.name",
                    "source": "Process execution logs",
                    "description": "Executable name",
                    "examples": ["cmd.exe", "powershell.exe"]
                },
                {
                    "field_name": "process.command_line",
                    "source": "Process execution logs",
                    "description": "Full command line with arguments",
                    "examples": []
                },
                {
                    "field_name": "registry.path",
                    "source": "Registry monitoring",
                    "description": "Windows registry key path",
                    "examples": ["HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"]
                }
            ],
            "query_template": f"SELECT * FROM logs WHERE {threat['typical_signals'][0].lower().replace(' ', '_')} "
                            "AND correlation_window < 5m"
        },
        
        "gap_analysis": {
            "current_coverage": f"Standard {threat['tactic']} detections likely monitor basic "
                              f"{threat['typical_signals'][0].lower()}",
            "missing_gaps": [
                {
                    "gap": f"Lack of {gap} for this {threat['tactic']} behavior",
                    "impact": "High false negatives; adversary avoids detection",
                    "requirement": f"Enable detailed {gap} collection",
                    "priority": "high"
                }
                for gap in threat["typical_gaps"][:2]
            ],
            "recommendations": [
                {
                    "recommendation": f"Correlate {threat['typical_signals'][0].lower()} with "
                                    f"{threat['typical_signals'][1].lower() if len(threat['typical_signals']) > 1 else 'follow-on activity'} "
                                    "within 5-minute window",
                    "effort": "medium",
                    "preconditions": f"Both {threat['typical_signals'][0].lower()} and secondary signal must be collected"
                },
                {
                    "recommendation": f"Create baseline of normal {threat['tactic']} activity in your environment",
                    "effort": "low",
                    "preconditions": "Historical data must be available for analysis"
                }
            ]
        },
        
        "rule_logic": {
            "rule_name": f"detect_{threat['name'].lower().replace(' ', '_').replace(':', '')}",
            "evidence": [
                {
                    "evidence_type": sig.lower().replace(" ", "_"),
                    "condition": f"Anomalous {sig.lower()} pattern detected",
                    "source": threat["typical_signals"][i] if i < len(threat["typical_signals"]) else sig
                }
                for i, sig in enumerate(threat["typical_signals"][:2])
            ],
            "correlation_logic": "all_present_within 5m",
            "alert_confidence": "high"
        },
        
        "implementation_code": {
            "rule_format": "udm_query",
            "code_snippet": f"""rule: detect_{threat['name'].lower().replace(' ', '_').replace(':', '')}
evidence:
  - signal_1: [process.name = 'suspicious' OR registry.path CONTAINS 'Run']
  - signal_2: [correlation_window < 5m]
correlation: all_present
alert_confidence: high
fp_mitigation: whitelist known_good_processes
""",
            "comments": "Adjust patterns and thresholds based on your environment."
        },
        
        "validation": {
            "assumptions": [
                f"All {threat['typical_signals'][0].lower()} sources are enabled",
                "Time synchronization is accurate across collection points",
                f"Baseline of normal {threat['tactic']} behavior is established"
            ],
            "false_positive_mitigation": [
                {
                    "fp_scenario": f"Legitimate {threat['tactic'].lower()} activity from IT operations",
                    "mitigation": "Whitelist known-good user/system accounts and process paths"
                },
                {
                    "fp_scenario": "High-volume legitimate activity overwhelming alert queue",
                    "mitigation": "Add time-based thresholds or rate-limiting rules"
                }
            ],
            "constraints": [
                {
                    "constraint": f"Requires detailed {threat['typical_signals'][0].lower()} collection",
                    "impact": "Cannot detect if this signal source is disabled or filtered"
                },
                {
                    "constraint": "5-minute correlation window may miss fast-moving attacks",
                    "impact": "Consider reducing window for critical threats"
                }
            ]
        },
        
        "metadata": {
            "source_corpus": f"synthetic/mitre/{technique_id}",
            "threat_category": threat["name"],
            "domain": threat["primary_domain"],
            "secondary_domains": threat["secondary_domains"],
            "example_type": "positive"
        }
    }


# ============================================================================
# Negative Example Generation
# ============================================================================

def generate_negative_variant(positive_unit: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create a negative example from a positive one.
    
    Flaws to introduce:
    - Missing critical signals
    - Incorrect MITRE mapping
    - Incomplete gap analysis
    - Weak false positive mitigation
    """
    negative = json.loads(json.dumps(positive_unit))  # Deep copy
    
    negative["metadata"]["example_type"] = "negative"
    
    # Introduce flaws
    # 1. Remove a critical signal
    if len(negative["signals"]) > 1:
        negative["signals"] = negative["signals"][1:]  # Drop primary signal
    
    # 2. Incomplete gap analysis
    negative["gap_analysis"]["recommendations"] = negative["gap_analysis"]["recommendations"][:1]
    negative["gap_analysis"]["missing_gaps"] = negative["gap_analysis"]["missing_gaps"][:1]
    
    # 3. Weak FP mitigation
    negative["validation"]["false_positive_mitigation"] = [
        {"fp_scenario": "Unknown", "mitigation": "Investigate"}
    ]
    
    # 4. Add a correction field
    negative["correction"] = {
        "issue": "This detection logic has gaps; proper approach would be:",
        "problems": [
            "Missing critical signals leads to high false negatives",
            "Incomplete gap analysis misses operational constraints",
            "Weak false positive mitigation causes alert fatigue"
        ],
        "corrected_approach": "See positive example for proper reasoning"
    }
    
    return negative


# ============================================================================
# Boundary Case Generation
# ============================================================================

def generate_boundary_case(positive_unit: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create a boundary case: ambiguous scenario requiring careful reasoning.
    
    Example: Detection that could work but requires specific preconditions.
    """
    boundary = json.loads(json.dumps(positive_unit))
    boundary["metadata"]["example_type"] = "boundary"
    
    # Add uncertainty
    boundary["rule_logic"]["alert_confidence"] = "medium"
    
    # Add complex constraints
    boundary["validation"]["constraints"].append({
        "constraint": "Detection depends on rare signal combination",
        "impact": "May produce inconsistent results across different environments"
    })
    
    # Add note about when this might fail
    boundary["validation"]["false_positive_mitigation"].append({
        "fp_scenario": "Detection may fail if threat actor uses variant techniques",
        "mitigation": "Requires continuous threat intel updates and rule refinement"
    })
    
    boundary["reasoning_note"] = (
        "This detection is sound in theory but requires careful tuning to your environment. "
        "Recommend pilot testing with lower confidence threshold before production deployment."
    )
    
    return boundary


# ============================================================================
# Mining from Real Detection Rules (Template)
# ============================================================================

def mine_from_sigma_rule(sigma_rule: Dict[str, Any]) -> Dict[str, Any]:
    """
    Convert a SIGMA rule into a workflow reasoning unit.
    
    SIGMA is a generic detection rule format; this extracts the workflow.
    """
    title = sigma_rule.get("title", "Unknown threat")
    description = sigma_rule.get("description", "")
    
    # Extract detection logic
    detection_section = sigma_rule.get("detection", {})
    selection_keys = [k for k in detection_section.keys() if k not in ["condition", "timeframe"]]
    
    # Build workflow unit from SIGMA structure
    unit = {
        "threat_scenario": title,
        "source_corpus": f"sigma/{sigma_rule.get('id', 'unknown')}",
        
        "signals": [
            {
                "name": f"sigma_field_{i}",
                "source": "SIGMA-compatible SIEM",
                "description": f"Detection field: {k}",
                "criticality": "primary" if i == 0 else "supporting"
            }
            for i, k in enumerate(selection_keys[:3])
        ],
        
        "correlation": {
            "threat_behavior": description,
            "mitre_techniques": [
                {"technique_id": t, "tactic": "unknown", "description": t}
                for t in sigma_rule.get("tags", [])
                if t.startswith("T")
            ],
            "reasoning": f"SIGMA rule correlates {len(selection_keys)} detection fields"
        },
        
        "udm_mapping": {
            "fields": [
                {
                    "field_name": k,
                    "source": "SIEM/EDR logs",
                    "description": f"From SIGMA rule: {k}",
                    "examples": []
                }
                for k in selection_keys[:3]
            ],
            "query_template": f"Implement SIGMA rule: {sigma_rule.get('id', 'unknown')}"
        },
        
        "gap_analysis": {
            "current_coverage": f"SIGMA provides detection logic",
            "missing_gaps": [
                {
                    "gap": "SIGMA rule may not capture all threat variants",
                    "impact": "Coverage depends on your log sources",
                    "requirement": "Tune rule for your environment",
                    "priority": "medium"
                }
            ],
            "recommendations": [
                {
                    "recommendation": "Convert SIGMA rule to your native SIEM/EDR query format",
                    "effort": "low",
                    "preconditions": "SIGMA rule is syntactically valid"
                }
            ]
        },
        
        "rule_logic": {
            "rule_name": f"sigma_{sigma_rule.get('id', 'unknown').split('-')[0]}",
            "evidence": [
                {
                    "evidence_type": f"field_{i}",
                    "condition": f"SIGMA condition: {k}",
                    "source": "SIEM/EDR"
                }
                for i, k in enumerate(selection_keys[:2])
            ],
            "correlation_logic": sigma_rule.get("detection", {}).get("condition", "unknown"),
            "alert_confidence": "medium"
        },
        
        "implementation_code": {
            "rule_format": "sigma",
            "code_snippet": json.dumps(sigma_rule, indent=2)[:500],
            "comments": "Source SIGMA rule; convert to your platform"
        },
        
        "validation": {
            "assumptions": ["SIGMA rule fields match your log structure"],
            "false_positive_mitigation": [
                {
                    "fp_scenario": "Depends on SIGMA rule specificity",
                    "mitigation": "Test in non-production environment first"
                }
            ],
            "constraints": [
                {
                    "constraint": "SIGMA rule may need platform-specific tuning",
                    "impact": "FP/FN rates vary by SIEM/EDR implementation"
                }
            ]
        },
        
        "metadata": {
            "source_corpus": f"sigma/{sigma_rule.get('id', 'unknown')}",
            "threat_category": title,
            "domain": "D2",
            "secondary_domains": ["D5"],
            "example_type": "positive"
        }
    }
    
    return unit


# ============================================================================
# Batch Generation
# ============================================================================

def generate_dataset_batch(
    num_synthetic: int = 100,
    num_negative_variants: int = 30,
    num_boundary_cases: int = 20
) -> List[Dict[str, Any]]:
    """
    Generate a mixed batch of examples for training.
    """
    units = []
    
    # 1. Synthetic from MITRE
    technique_ids = list(MITRE_THREATS.keys())
    for i in range(num_synthetic):
        tid = technique_ids[i % len(technique_ids)]
        unit = generate_from_mitre_technique(tid)
        units.append(unit)
    
    # 2. Negative variants (from first N positive examples)
    for i in range(min(num_negative_variants, len(units))):
        negative = generate_negative_variant(units[i])
        units.append(negative)
    
    # 3. Boundary cases (from next N positive examples)
    for i in range(num_negative_variants, min(num_negative_variants + num_boundary_cases, len(units))):
        boundary = generate_boundary_case(units[i])
        units.append(boundary)
    
    return units


# ============================================================================
# Example Usage
# ============================================================================

if __name__ == "__main__":
    # Generate a small batch
    batch = generate_dataset_batch(num_synthetic=3, num_negative_variants=1, num_boundary_cases=1)
    
    print(f"Generated {len(batch)} examples:\n")
    for i, unit in enumerate(batch):
        print(f"{i+1}. {unit['threat_scenario']} ({unit['metadata']['example_type']})")
        print(f"   Signals: {len(unit['signals'])}")
        print(f"   Gaps: {len(unit['gap_analysis']['missing_gaps'])}")
        print(f"   Domain: {unit['metadata']['domain']}")
        print()
    
    # Show first example in detail
    print("=" * 80)
    print("First example (detailed):")
    print("=" * 80)
    print(json.dumps(batch[0], indent=2)[:1000])
    print("...")
