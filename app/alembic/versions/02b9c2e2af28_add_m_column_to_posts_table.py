"""add m column to posts table

Revision ID: 02b9c2e2af28
Revises: f29f518a5ffd
Create Date: 2022-05-15 04:43:31.909366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02b9c2e2af28'
down_revision = 'f29f518a5ffd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String, nullable=False))
    pass


def downgrade():
    pass
