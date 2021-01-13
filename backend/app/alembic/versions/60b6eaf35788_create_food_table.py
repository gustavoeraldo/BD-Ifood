"""create food table

Revision ID: 60b6eaf35788
Revises: 42ea46fc93b8
Create Date: 2021-01-12 13:45:09.873088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60b6eaf35788'
down_revision = '42ea46fc93b8'
branch_labels = None
depends_on = None


def upgrade():
  op.add_column('users_t', sa.Column('phone1', sa.String))


def downgrade():
    pass
