"""
SOC Sentinel AI
Main Controller

Author: Dharunya
"""

import os
import sys

# Add module paths
sys.path.append("scripts/log-collector")
sys.path.append("scripts/detection-engine")
sys.path.append("scripts/ai-analyzer")
sys.path.append("models")

from log_collector import LogCollector
from detector import DetectionEngine
from incident_ai import AIAnalyzer
from security_event import SecurityEvent


def main():

    print("=" * 70)
    print("SOC Sentinel AI")
    print("AI-Assisted Security Operations Platform")
    print("=" * 70)

    collector = LogCollector()
    detector = DetectionEngine()
    ai = AIAnalyzer()

    print("\n✅ Modules Loaded Successfully")

    print("\nLoaded Modules")
    print("--------------------------")
    print("✔ Log Collector")
    print("✔ Detection Engine")
    print("✔ AI Incident Analyzer")
    print("✔ Security Event Model")

    print("\nProject initialized successfully.")


if __name__ == "__main__":
    main()
    