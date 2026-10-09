# SPDX-FileCopyrightText: 2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Module tests."""

from flask import Flask

from invenio_notices import InvenioNotices, __version__


def test_version() -> None:
    """Test version import."""
    assert __version__


def test_init() -> None:
    """Test extension initialization."""
    app = Flask("testapp")
    InvenioNotices(app)
    assert "invenio-notices" in app.extensions

    app = Flask("testapp")
    ext = InvenioNotices()
    assert "invenio-notices" not in app.extensions
    ext.init_app(app)
    assert "invenio-notices" in app.extensions


def test_init_config() -> None:
    """Test config defaults."""
    app = Flask("testapp")
    InvenioNotices(app)
    assert app.config["NOTICES"] == []
    assert app.config["NOTICES_FEATURES"] == {}
