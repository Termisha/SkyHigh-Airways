"""empty message

Revision ID: b9ec0cbcdef3
Revises: 84d1dd9b6471
Create Date: 2024-11-06 23:17:36.959826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9ec0cbcdef3'
down_revision = '84d1dd9b6471'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('flights', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.Date(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('flights', schema=None) as batch_op:
        batch_op.drop_column('date')

    # ### end Alembic commands ###
