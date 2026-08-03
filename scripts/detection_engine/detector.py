"""
SOC Sentinel AI
Module: Detection Engine

Author: Dharunya
"""


class DetectionEngine:

    def __init__(self):
        self.failed_logins = 0

    def analyze(self, event):

        if event.event_type == "Authentication Failure":

            self.failed_logins += 1

            if self.failed_logins >= 5:
                event.alert = "🚨 Possible Brute Force Attack"

        elif event.event_type == "PowerShell Execution":

            event.alert = "⚠ Suspicious PowerShell Activity"

        elif event.event_type == "USB Activity":

            event.alert = "⚠ USB Device Connected"

        elif event.event_type == "File Activity":

            event.alert = "⚠ Sensitive File Activity"

        return event