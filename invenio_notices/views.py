# SPDX-FileCopyrightText: 2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Views for invenio-notices."""

from flask import Blueprint, Flask

from .resources import NoticesResource, NoticesResourceConfig


def create_notices_bp(_app: Flask) -> Blueprint:
    """Create the notices resource blueprint."""
    return NoticesResource(NoticesResourceConfig()).as_blueprint()
