# SPDX-FileCopyrightText: 2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Notices resource."""

from flask import abort
from flask_login import current_user
from flask_resources import Resource, request_parser, resource_requestctx, route
from marshmallow import fields

from invenio_notices.services import NoticesService

request_view_args = request_parser(
    {"key": fields.Str()},
    location="view_args",
)


class NoticesResource(Resource):
    """Resource with the acknowledge endpoint."""

    def create_url_rules(self) -> list:
        """Create the URL rules for the notices resource."""
        return [route("POST", self.config.routes["acknowledge"], self.acknowledge)]

    @request_view_args
    def acknowledge(self) -> dict:
        """Record that the current user acknowledged a notice."""
        if not current_user.is_authenticated:
            abort(403)
        key = resource_requestctx.view_args["key"]
        NoticesService().acknowledge(current_user.id, key)
        return {"acknowledged": key}
