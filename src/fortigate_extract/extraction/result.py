from __future__ import annotations

from dataclasses import dataclass, field

from model.config import FGConfig


@dataclass(slots=True)
class ExtractionResult:
    config: FGConfig

    report_views: dict[str, list] = field(
        default_factory=dict
    )