"""add transaction

Revision ID: 0133e85a81df
Revises: b3bf1ecc739e
Create Date: 2021-01-07 23:26:59.060307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0133e85a81df'
down_revision = 'b3bf1ecc739e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'transaction',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
        sa.Column('date', sa.Date, nullable=False),
        sa.Column('budget_id', sa.Integer, nullable=False),
        sa.Column('thing', sa.String),
        sa.Column('outcome', sa.Integer),
        sa.Column('income', sa.Integer)
    )


def downgrade():
    op.drop_table('transaction')
