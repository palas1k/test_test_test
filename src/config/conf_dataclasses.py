from dataclasses import dataclass


@dataclass(slots=True)
class LoggingConfig:
    level: str
    human_readable_logs: bool = True
