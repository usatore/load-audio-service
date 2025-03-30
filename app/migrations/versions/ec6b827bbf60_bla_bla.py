"""Bla bla

Revision ID: ec6b827bbf60
Revises: 35b6e64ba093
Create Date: 2025-03-30 19:43:43.289153

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec6b827bbf60'
down_revision: Union[str, None] = '35b6e64ba093'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
