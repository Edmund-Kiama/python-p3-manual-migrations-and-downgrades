"""Renaming students to scholars

Revision ID: 2aa47c3eb04f
Revises: 791279dd0760
Create Date: 2025-02-21 15:38:22.178564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2aa47c3eb04f'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
