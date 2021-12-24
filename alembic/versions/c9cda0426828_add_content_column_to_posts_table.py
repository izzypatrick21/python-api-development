"""add content column to posts table

Revision ID: c9cda0426828
Revises: 2da1da6d8349
Create Date: 2021-12-24 01:22:27.440064

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9cda0426828'
down_revision = '2da1da6d8349'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts', 'content')
