"""empty message

Revision ID: a25ca54fae54
Revises: 9c57c4f80889
Create Date: 2024-11-07 00:52:36.967200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a25ca54fae54'
down_revision = '9c57c4f80889'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bookings')
    op.drop_table('passengers')
    with op.batch_alter_table('seats', schema=None) as batch_op:
        batch_op.add_column(sa.Column('passenger_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('first_name', sa.String(length=30), nullable=False))
        batch_op.add_column(sa.Column('last_name', sa.String(length=30), nullable=False))
        batch_op.add_column(sa.Column('date_of_birth', sa.Date(), nullable=False))
        batch_op.add_column(sa.Column('gender', sa.String(length=10), nullable=False))
        batch_op.add_column(sa.Column('email', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('phone_number', sa.String(length=15), nullable=False))
        batch_op.create_unique_constraint('emailc', ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('seats', schema=None) as batch_op:
        batch_op.drop_constraint('emailc', type_='unique')
        batch_op.drop_column('phone_number')
        batch_op.drop_column('email')
        batch_op.drop_column('gender')
        batch_op.drop_column('date_of_birth')
        batch_op.drop_column('last_name')
        batch_op.drop_column('first_name')
        batch_op.drop_column('passenger_id')

    op.create_table('passengers',
    sa.Column('passenger_id', sa.INTEGER(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=30), nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=30), nullable=False),
    sa.Column('date_of_birth', sa.DATE(), nullable=False),
    sa.Column('gender', sa.VARCHAR(length=10), nullable=False),
    sa.Column('email', sa.VARCHAR(length=100), nullable=False),
    sa.Column('phone_number', sa.VARCHAR(length=15), nullable=False),
    sa.PrimaryKeyConstraint('passenger_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('bookings',
    sa.Column('booking_id', sa.INTEGER(), nullable=False),
    sa.Column('flight_id', sa.INTEGER(), nullable=True),
    sa.Column('seat_number', sa.VARCHAR(length=10), nullable=True),
    sa.Column('booking_date', sa.DATETIME(), nullable=True),
    sa.Column('booking_reference', sa.VARCHAR(length=100), nullable=True),
    sa.Column('passenger_first_name', sa.VARCHAR(length=20), nullable=False),
    sa.Column('passenger_last_name', sa.VARCHAR(length=20), nullable=False),
    sa.Column('passenger_email', sa.VARCHAR(length=100), nullable=True),
    sa.Column('passenger_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['flight_id'], ['flights.flight_id'], ),
    sa.ForeignKeyConstraint(['passenger_id'], ['passengers.passenger_id'], name='fk_bookings_passengers'),
    sa.PrimaryKeyConstraint('booking_id'),
    sa.UniqueConstraint('booking_reference')
    )
    # ### end Alembic commands ###