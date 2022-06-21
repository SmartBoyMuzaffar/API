"""create post table

Revision ID: f29f518a5ffd
Revises: 
Create Date: 2022-05-11 12:38:34.254193

"""
from alembic import op
from fastapi import FastAPI
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f29f518a5ffd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column("title", sa.String, nullable=False))


def downgrade():
    op.drop_table("posts")