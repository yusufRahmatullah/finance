"""add budget

Revision ID: b3bf1ecc739e
Revises: 
Create Date: 2021-01-07 22:06:13.260562

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3bf1ecc739e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'budget',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
        sa.Column('name', sa.String),
        sa.Column('amount', sa.Integer),
        sa.Column('period', sa.Date)
    )


def downgrade():
    op.drop_table('budget')
