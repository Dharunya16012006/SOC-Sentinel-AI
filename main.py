"""
SOC Sentinel AI
Main Controller

Author: Dharunya
"""

import sys
import os

# Add module paths
sys.path.append(os.path.join(os.getcwd(), "scripts", "log_collector"))
sys.path.append(os.path.join(os.getcwd(), "scripts", "detection_engine"))
sys.path.append(os.path.join(os.getcwd(), "scripts", "ai-analyzer"))
sys.path.append(os.path.join(os.getcwd(), "scripts", "report_generator"))

from log_collector import LogCollector
from detector import DetectionEngine
from incident_ai import AIAnalyzer
from report_generator import ReportGenerator


def main():

    print("=" * 70)
    print("SOC Sentinel AI")
    print("AI-Assisted Security Operations Platform")
    print("=" * 70)

    print("\nLoading Modules...")

    collector = LogCollector()
    detector = DetectionEngine()
    ai = AIAnalyzer()
    report = ReportGenerator()

    print("✔ Log Collector Loaded")
    print("✔ Detection Engine Loaded")
    print("✔ AI Incident Analyzer Loaded")
    print("✔ Report Generator Loaded")

    print("\nStarting Log Analysis...\n")

    # Current LogCollector handles the processing and display
    collector.run()

    print("\n" + "=" * 70)
    print("SOC Sentinel AI Execution Completed")
    print("=" * 70)

    print("\n📌 Next Version:")
    print("• Integrate AI Analyzer into the processing pipeline")
    print("• Generate incident reports automatically")
    print("• Connect Dashboard")
    print("• Integrate Windows & Linux VM logs")


if __name__ == "__main__":
    main()

    