import pytest
from pathlib import Path
from agentic_soc_factory.ingestion.web_scraper import SigmaGitHubScraper

def test_sigma_scraper_extracts_yaml_as_workflow_unit():
    # RED: SigmaGitHubScraper not implemented
    scraper = SigmaGitHubScraper()
    
    # Mocking a sigma rule content
    sample_yaml = """
title: Suspicious Login
id: 123
logsource:
    product: windows
    service: security
detection:
    selection:
        EventID: 4624
    condition: selection
"""
    workflow_unit = scraper.parse_sigma_yaml(sample_yaml)
    
    assert "signals" in workflow_unit
    assert workflow_unit["threat_scenario"] == "Suspicious Login"
    assert any(s["name"] == "EventID" for s in workflow_unit["signals"])
