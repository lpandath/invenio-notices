# SPDX-FileCopyrightText: 2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Create invenio-notices branch."""

# revision identifiers
revision = "a1c5525f3527"
down_revision = None
branch_labels = ("invenio_notices",)
depends_on = "dbdbc1b19cf2"


def upgrade() -> None:
    """Upgrade database."""


def downgrade() -> None:
    """Downgrade database."""
