"""add user table

Revision ID: 40b01e4306b3
Revises: 02b9c2e2af28
Create Date: 2022-05-15 04:58:23.488067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40b01e4306b3'
down_revision = '02b9c2e2af28'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
