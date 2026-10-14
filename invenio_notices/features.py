# SPDX-FileCopyrightText: 2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Ready-made feature checks for ``NOTICES_FEATURES``.

A feature check is a no-argument callable returning ``bool``, the notice
shows only while it returns ``True``.
"""

from collections.abc import Callable

from flask import current_app


def config_flag(key: str) -> Callable[[], bool]:
    """Feature is on when the config variable is truthy, flip it at go-live."""
    return lambda: bool(current_app.config.get(key, False))


def endpoint_exists(endpoint: str) -> Callable[[], bool]:
    """Feature is on when the route is registered, presence detection."""
    return lambda: endpoint in current_app.view_functions


def extension_loaded(name: str) -> Callable[[], bool]:
    """Feature is on when the Flask extension is loaded."""
    return lambda: name in current_app.extensions
