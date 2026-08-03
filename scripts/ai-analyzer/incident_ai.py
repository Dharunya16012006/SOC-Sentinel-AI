"""
SOC Sentinel AI
Module: AI Incident Analyzer

Author: Dharunya
"""


class AIAnalyzer:

    def __init__(self):
        pass

    def analyze(self, event):
        """
        Analyze a SecurityEvent object and enrich it
        with an explanation and recommendation.
        """

        if event.event_type == "Authentication Failure":

            event.explanation = (
                "Multiple failed login attempts may indicate a brute-force attack "
                "or invalid user credentials."
            )

            event.recommendation = (
                "Review the source IP address, monitor repeated login failures, "
                "and enable Multi-Factor Authentication (MFA) if possible."
            )

        elif event.event_type == "Authentication Success":

            event.explanation = (
                "A successful user authentication was detected."
            )

            event.recommendation = (
                "Verify that the login originated from an authorized user "
                "and a trusted device."
            )

        elif event.event_type == "PowerShell Execution":

            event.explanation = (
                "PowerShell execution was detected. While PowerShell is commonly "
                "used by administrators, attackers also use it for malware "
                "execution and post-exploitation activities."
            )

            event.recommendation = (
                "Review the executed PowerShell command, verify the user account, "
                "and investigate any unusual script activity."
            )

        elif event.event_type == "USB Activity":

            event.explanation = (
                "A removable USB storage device was connected to the system."
            )

            event.recommendation = (
                "Verify whether the USB device is authorized and monitor "
                "for possible data exfiltration."
            )

        elif event.event_type == "File Activity":

            event.explanation = (
                "A file deletion event was detected on the endpoint."
            )

            event.recommendation = (
                "Confirm whether the file deletion was expected and review "
                "user activity around the event."
            )

        else:

            event.explanation = (
                "No AI explanation is currently available for this event."
            )

            event.recommendation = (
                "Perform a manual investigation and review related logs."
            )

        return event


if __name__ == "__main__":

    # Simple test
    from types import SimpleNamespace

    sample_event = SimpleNamespace(
        event_type="PowerShell Execution",
        explanation="",
        recommendation=""
    )

    ai = AIAnalyzer()

    result = ai.analyze(sample_event)

    print("=" * 60)
    print("SOC Sentinel AI")
    print("AI Incident Analyzer Test")
    print("=" * 60)

    print(f"\nEvent Type      : {result.event_type}")
    print(f"\nExplanation     : {result.explanation}")
    print(f"\nRecommendation  : {result.recommendation}")

    print("\n" + "=" * 60)