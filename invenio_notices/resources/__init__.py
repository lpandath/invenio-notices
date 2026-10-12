# SPDX-FileCopyrightText: 2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Notices REST resources."""

from .config import NoticesResourceConfig
from .resources import NoticesResource

__all__ = ("NoticesResource", "NoticesResourceConfig")
