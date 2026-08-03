from dataclasses import dataclass


@dataclass
class SecurityEvent:

    raw_log: str
    event_type: str
    severity: str
    alert: str | None = None
    explanation: str | None = None
    recommendation: str | None = None

    