# SPDX-FileCopyrightText: 2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Configuration of the notices resource."""

from typing import ClassVar

from flask_resources import ResourceConfig


class NoticesResourceConfig(ResourceConfig):
    """Configuration of the notices resource."""

    blueprint_name = "invenio_notices"
    url_prefix = "/notices"
    routes: ClassVar[dict] = {"acknowledge": "/<key>/acknowledge"}
