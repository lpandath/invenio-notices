# SPDX-FileCopyrightText: 2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Notices resource."""

from flask_resources import Resource, route


class NoticesResource(Resource):
    """Resource with the acknowledge endpoint."""

    def create_url_rules(self) -> list:
        """Create the URL rules for the notices resource."""
        return [route("POST", self.config.routes["acknowledge"], self.acknowledge)]

    def acknowledge(self) -> dict:
        """Record that the current user acknowledged a notice."""
        raise NotImplementedError
