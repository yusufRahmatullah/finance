"""add_wallet

Revision ID: 4846477cc810
Revises: 0133e85a81df
Create Date: 2021-01-13 18:34:58.418979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4846477cc810'
down_revision = '0133e85a81df'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'wallet',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
        sa.Column('name', sa.String),
        sa.Column('amount', sa.Integer),
        sa.Column('period', sa.Date)
    )


def downgrade():
    op.drop_table('wallet')
