"""setup reservations table and relationships

Revision ID: d4eb0b4aa934
Revises: 4da6f2b0944b
Create Date: 2023-05-29 11:22:31.785957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4eb0b4aa934'
down_revision = '4da6f2b0944b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reservations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reference_code', sa.String(), nullable=True),
    sa.Column('passenger_id', sa.Integer(), nullable=True),
    sa.Column('flight_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['flight_id'], ['flights.id'], name=op.f('fk_reservations_flight_id_flights')),
    sa.ForeignKeyConstraint(['passenger_id'], ['passengers.id'], name=op.f('fk_reservations_passenger_id_passengers')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservations')
    # ### end Alembic commands ###
