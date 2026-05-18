# Threat Intel Aggregator

A Python-based cybersecurity automation tool that collects, parses, and organizes threat intelligence indicators such as malicious IP addresses, domains, URLs, file hashes, and malware-related IOCs.

## Project Purpose

This project simulates how SOC analysts and threat intelligence teams collect and enrich indicators of compromise from multiple intelligence sources to support alert triage, investigation, and incident response.

## Key Features

- Collects threat indicators from structured JSON sources
- Parses IP addresses, domains, URLs, and hashes
- Deduplicates repeated indicators
- Categorizes IOCs by type
- Generates a simple markdown threat intelligence report
- Designed for SOC, threat intelligence, and security automation practice

## Skills Demonstrated

- Python scripting
- Threat intelligence analysis
- IOC handling
- JSON parsing
- Security automation
- SOC workflow documentation
- Report generation

## Technologies Used

- Python
- JSON
- REST API concepts
- Markdown reporting
- Git/GitHub

## Folder Structure

```text
data/        Sample IOC input files
reports/     Generated threat intelligence reports
screenshots/ Screenshots of tool output
main.py      Main Python script
