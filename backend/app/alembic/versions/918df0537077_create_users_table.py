"""create users table

Revision ID: 918df0537077
Revises: 
Create Date: 2021-01-07 16:08:31.003714

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '918df0537077'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
  op.create_table(
    'users_t',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String(50), nullable=False),
    sa.Column('email',sa.String(60), nullable=False),
  )


def downgrade():
  op.drop_table('users_t')
