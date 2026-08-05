"""
SOC Sentinel AI
Module: Log Collection Engine

Author: Dharunya
"""

import os
import sys

# Import Detection Engine
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "detection_engine")
    )
)

# Import AI Analyzer
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "ai-analyzer")
    )
)

# Import Security Event Model
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "models")
    )
)

from detector import DetectionEngine
from incident_ai import AIAnalyzer
from security_event import SecurityEvent


class LogCollector:

    def __init__(self):
        self.log_file = "logs/sample/sample_log.txt"

    def classify_event(self, log):

        if "LOGIN FAILED" in log:
            return "Authentication Failure", "Medium"

        elif "LOGIN SUCCESS" in log:
            return "Authentication Success", "Low"

        elif "POWERSHELL" in log:
            return "PowerShell Execution", "High"

        elif "USB CONNECTED" in log:
            return "USB Activity", "Low"

        elif "FILE DELETED" in log:
            return "File Activity", "Medium"

        else:
            return "Unknown", "Low"

    def run(self):

        print("=" * 60)
        print("SOC Sentinel AI")
        print("Log Collection, Classification, Detection & AI Analysis")
        print("=" * 60)

        detector = DetectionEngine()
        ai = AIAnalyzer()

        try:

            with open(self.log_file, "r") as file:

                logs = [line.strip() for line in file if line.strip()]

                print(f"\nTotal Logs Found : {len(logs)}\n")

                event_count = {}
                severity_count = {}

                for count, log in enumerate(logs, start=1):

                    event_type, severity = self.classify_event(log)

                    # Create Security Event Object
                    event = SecurityEvent(
                        raw_log=log,
                        event_type=event_type,
                        severity=severity
                    )

                    # Detection Engine
                    event = detector.analyze(event)

                    # AI Analyzer
                    event = ai.analyze(event)

                    # Summary Count
                    event_count[event.event_type] = (
                        event_count.get(event.event_type, 0) + 1
                    )

                    severity_count[event.severity] = (
                        severity_count.get(event.severity, 0) + 1
                    )

                    print("-" * 60)
                    print(f"Event #{count}")
                    print(f"Type            : {event.event_type}")
                    print(f"Severity        : {event.severity}")
                    print(f"Raw Log         : {event.raw_log}")

                    if event.alert:
                        print(f"Alert           : {event.alert}")

                    print(f"AI Explanation  : {event.explanation}")
                    print(f"Recommendation  : {event.recommendation}")

                print("\n" + "=" * 60)
                print("SOC Sentinel AI Summary")
                print("=" * 60)

                print(f"\nTotal Events : {len(logs)}\n")

                print("Event Summary")
                print("-" * 60)

                for event_name, total in event_count.items():
                    print(f"{event_name:<30} : {total}")

                print("\nSeverity Summary")
                print("-" * 60)

                for severity_name, total in severity_count.items():
                    print(f"{severity_name:<30} : {total}")

                print("=" * 60)

        except FileNotFoundError:
            print("Log file not found.")


if __name__ == "__main__":
    collector = LogCollector()
    collector.run()

    