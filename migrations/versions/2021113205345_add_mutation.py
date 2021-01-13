"""add_mutation

Revision ID: 2a37372b500b
Revises: 4846477cc810
Create Date: 2021-01-13 20:53:45.367742

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a37372b500b'
down_revision = '4846477cc810'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'mutation',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
        sa.Column('date', sa.Date, nullable=False),
        sa.Column('thing', sa.String),
        sa.Column('from_id', sa.Integer),
        sa.Column('to_id', sa.Integer),
        sa.Column('amount', sa.Integer),
    )


def downgrade():
    op.drop_table('mutation')
