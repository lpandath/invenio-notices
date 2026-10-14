# SPDX-FileCopyrightText: 2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Service tests."""

from datetime import UTC, datetime, timedelta, timezone

from invenio_notices.services import NoticesService

service = NoticesService()


def _iso(delta: timedelta, tz: timezone = UTC) -> str:
    return (datetime.now(tz=UTC) + delta).astimezone(tz).isoformat()


def test_is_shown_to_users() -> None:
    """A users notice is only shown to authenticated visitors."""
    notice = {"show_to": "users"}
    assert service._is_shown_to(notice, authenticated=True)
    assert not service._is_shown_to(notice, authenticated=False)


def test_is_shown_to_guests() -> None:
    """A guests notice is only shown to anonymous visitors."""
    notice = {"show_to": "guests"}
    assert not service._is_shown_to(notice, authenticated=True)
    assert service._is_shown_to(notice, authenticated=False)


def test_is_shown_to_all() -> None:
    """An all notice is shown to everyone."""
    notice = {"show_to": "all"}
    assert service._is_shown_to(notice, authenticated=True)
    assert service._is_shown_to(notice, authenticated=False)


def test_is_shown_to_defaults_to_users() -> None:
    """Without show_to the notice is treated as a users notice."""
    assert service._is_shown_to({}, authenticated=True)
    assert not service._is_shown_to({}, authenticated=False)


def test_roles_match_without_required_roles() -> None:
    """A notice without roles matches every visitor."""
    assert service._roles_match(None, set())
    assert service._roles_match([], {"curator"})


def test_roles_match_with_required_roles() -> None:
    """A notice with roles needs at least one of them."""
    assert service._roles_match(["curator"], {"curator", "admin"})
    assert not service._roles_match(["curator"], {"admin"})
    assert not service._roles_match(["curator"], set())


def test_visible_items_plain() -> None:
    """Plain items are shown to everyone."""
    notice = {"items": ["first", "second"]}
    assert service._visible_items(notice, set()) == ["first", "second"]


def test_visible_items_filters_by_role() -> None:
    """Role gated items are dropped for visitors without the role."""
    notice = {
        "items": [
            "plain",
            {"text": "for curators", "roles": ["curator"]},
        ],
    }
    assert service._visible_items(notice, set()) == ["plain"]
    assert service._visible_items(notice, {"curator"}) == [
        "plain",
        "for curators",
    ]


def test_in_time_window_without_window() -> None:
    """A notice without starts_at/ends_at always shows."""
    assert service._in_time_window({})


def test_in_time_window_starts_at() -> None:
    """A notice shows once starts_at has passed."""
    assert service._in_time_window({"starts_at": _iso(timedelta(hours=-1))})
    assert not service._in_time_window({"starts_at": _iso(timedelta(hours=1))})


def test_in_time_window_ends_at() -> None:
    """A notice stops showing after ends_at."""
    assert service._in_time_window({"ends_at": _iso(timedelta(hours=1))})
    assert not service._in_time_window({"ends_at": _iso(timedelta(hours=-1))})


def test_in_time_window_handles_timezones() -> None:
    """Offsets are converted, naive values count as UTC."""
    vienna = timezone(timedelta(hours=1))
    assert service._in_time_window(
        {
            "starts_at": _iso(timedelta(hours=-1), tz=vienna),
            "ends_at": _iso(timedelta(hours=1), tz=vienna),
        },
    )
    naive_past = (datetime.now(tz=UTC) - timedelta(hours=1)).replace(tzinfo=None)
    assert service._in_time_window({"starts_at": naive_past.isoformat()})
