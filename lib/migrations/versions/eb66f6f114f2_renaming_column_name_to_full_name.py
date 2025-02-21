"""Renaming column name to full_name

Revision ID: eb66f6f114f2
Revises: 2aa47c3eb04f
Create Date: 2025-02-21 15:48:42.227649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb66f6f114f2'
down_revision = '2aa47c3eb04f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars', 'name', new_column_name = 'full_name')


def downgrade() -> None:
    op.alter_column('scholars', 'full_name', new_column_name = 'name')
