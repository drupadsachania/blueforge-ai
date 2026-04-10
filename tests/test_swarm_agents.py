import pytest
from agentic_soc_factory.agents.factory_agents import ThreatHunter, PlatformTranslator

def test_threat_hunter_extracts_indicators():
    # RED: ThreatHunter not implemented
    hunter = ThreatHunter()
    raw_doc = "Suspicious process execution observed. Source IP 10.0.0.5 communicating with malicious.com"
    
    findings = hunter.hunt(raw_doc)
    
    assert "indicators" in findings
    assert "10.0.0.5" in str(findings["indicators"])
    assert "malicious.com" in str(findings["indicators"])

def test_platform_translator_to_sentinel():
    # RED: PlatformTranslator not implemented
    translator = PlatformTranslator()
    splunk_query = 'index=security EventID=4624 | stats count by user'
    
    kql_query = translator.translate(splunk_query, target_platform="sentinel")
    
    assert "SecurityEvent" in kql_query
    assert "summarize" in kql_query.lower()
