"""Compatibility package for DocType module resolution.

This app keeps DocType folders at:
omnexa_reporting_compliance/doctype/*

Frappe can resolve controllers under:
omnexa_reporting_compliance.omnexa_reporting_compliance.doctype.*
when Module == "Omnexa Reporting Compliance".

Expose the parent doctype directory on this package path so both layouts work.
"""

from __future__ import annotations

import os

_PARENT_DOCTYPE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "doctype"))
if os.path.isdir(_PARENT_DOCTYPE_DIR) and _PARENT_DOCTYPE_DIR not in __path__:
	__path__.append(_PARENT_DOCTYPE_DIR)
