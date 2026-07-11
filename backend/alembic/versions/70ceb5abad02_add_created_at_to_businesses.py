"""add_created_at_to_businesses

Revision ID: 70ceb5abad02
Revises: 1bf31450b976
Create Date: 2026-07-10 22:06:18.523480

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "70ceb5abad02"
down_revision: Union[str, Sequence[str], None] = "1bf31450b976"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "businesses",
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_column("businesses", "created_at")