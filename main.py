"""
SOC Sentinel AI
Main Controller

Author: Dharunya
"""

import os
import sys

# Add module paths
sys.path.append(os.path.join(os.getcwd(), "scripts", "log_collector"))
sys.path.append(os.path.join(os.getcwd(), "scripts", "detection_engine"))
sys.path.append(os.path.join(os.getcwd(), "scripts", "ai-analyzer"))
sys.path.append(os.path.join(os.getcwd(), "scripts", "report_generator"))

from log_collector import LogCollector
from report_generator import ReportGenerator


def main():

    print("=" * 70)
    print("SOC Sentinel AI")
    print("AI-Assisted Security Operations Platform")
    print("=" * 70)

    print("\nLoading Modules...")

    collector = LogCollector()
    report = ReportGenerator()

    print("✔ Log Collector Loaded")
    print("✔ Report Generator Loaded")

    print("\nStarting Log Analysis...\n")

    # Run the complete pipeline
    events = collector.run()

    # Generate Incident Report
    if events:
        report.generate(events)

    print("\n" + "=" * 70)
    print("SOC Sentinel AI Execution Completed")
    print("=" * 70)


if __name__ == "__main__":
    main()