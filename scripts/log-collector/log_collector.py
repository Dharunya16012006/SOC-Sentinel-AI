"""
SOC Sentinel AI
Module: Log Collection Engine

Author: Dharunya
"""

class LogCollector:

    def __init__(self):
        self.log_file = "logs/sample/sample_log.txt"

    def run(self):

        print("=" * 50)
        print("SOC Sentinel AI")
        print("Reading Sample Logs")
        print("=" * 50)

        try:

            with open(self.log_file, "r") as file:

                logs = [line.strip() for line in file if line.strip()]

                print(f"\nTotal Logs Found : {len(logs)}\n")

                for log in logs:
                    print(log)

        except FileNotFoundError:
            print("Log file not found.")


if __name__ == "__main__":
    collector = LogCollector()
    collector.run()