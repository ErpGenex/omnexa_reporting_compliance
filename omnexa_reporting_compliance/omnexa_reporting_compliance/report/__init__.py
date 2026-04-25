"""Compatibility package for Report module resolution.

Expose parent report directory for module imports that resolve through:
omnexa_reporting_compliance.omnexa_reporting_compliance.report.*
"""

from __future__ import annotations

import os

_PARENT_REPORT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "report"))
if os.path.isdir(_PARENT_REPORT_DIR) and _PARENT_REPORT_DIR not in __path__:
	__path__.append(_PARENT_REPORT_DIR)
