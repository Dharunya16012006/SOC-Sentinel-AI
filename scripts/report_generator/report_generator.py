"""
SOC Sentinel AI
Module: Report Generator

Author: Dharunya
"""


class ReportGenerator:

    def __init__(self):
        self.report_path = "reports/incident_report.txt"

    def generate(self, events):

        with open(self.report_path, "w") as report:

            report.write("=" * 70 + "\n")
            report.write("SOC Sentinel AI Incident Report\n")
            report.write("=" * 70 + "\n\n")

            report.write(f"Total Events : {len(events)}\n\n")

            for count, event in enumerate(events, start=1):

                report.write("-" * 70 + "\n")
                report.write(f"Event #{count}\n")
                report.write(f"Type            : {event.event_type}\n")
                report.write(f"Severity        : {event.severity}\n")
                report.write(f"Raw Log         : {event.raw_log}\n")

                if event.alert:
                    report.write(f"Alert           : {event.alert}\n")

                if event.explanation:
                    report.write(f"Explanation     : {event.explanation}\n")

                if event.recommendation:
                    report.write(f"Recommendation  : {event.recommendation}\n")

                report.write("\n")

        print("\n✅ Incident report generated successfully.")
        print(f"📄 Report saved to: {self.report_path}")

        