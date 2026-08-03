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
        os.path.join(os.path.dirname(__file__), "..", "detection-engine")
    )
)

from detector import DetectionEngine


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
        print("Log Collection, Classification & Detection Engine")
        print("=" * 60)

        detector = DetectionEngine()

        try:

            with open(self.log_file, "r") as file:

                logs = [line.strip() for line in file if line.strip()]

                print(f"\nTotal Logs Found : {len(logs)}\n")

                # Summary dictionaries
                event_count = {}
                severity_count = {}

                # Process every log
                for count, log in enumerate(logs, start=1):

                    event, severity = self.classify_event(log)

                    # Send event to Detection Engine
                    alert = detector.analyze(event)

                    # Count events
                    event_count[event] = event_count.get(event, 0) + 1
                    severity_count[severity] = severity_count.get(severity, 0) + 1

                    print("-" * 60)
                    print(f"Event #{count}")
                    print(f"Type      : {event}")
                    print(f"Severity  : {severity}")
                    print(f"Raw Log   : {log}")

                    if alert:
                        print(f"Alert     : {alert}")

                # ==========================
                # Summary
                # ==========================

                print("\n" + "=" * 60)
                print("SOC Sentinel AI Summary")
                print("=" * 60)

                print(f"\nTotal Events : {len(logs)}\n")

                print("Event Summary")
                print("-" * 60)

                for event, count in event_count.items():
                    print(f"{event:<30} : {count}")

                print("\nSeverity Summary")
                print("-" * 60)

                for severity, count in severity_count.items():
                    print(f"{severity:<30} : {count}")

                print("=" * 60)

        except FileNotFoundError:
            print("Log file not found.")


if __name__ == "__main__":
    collector = LogCollector()
    collector.run()