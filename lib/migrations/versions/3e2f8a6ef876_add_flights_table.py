"""add flights table

Revision ID: 3e2f8a6ef876
Revises: 
Create Date: 2023-05-29 10:09:59.792097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e2f8a6ef876'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flights',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('departure_city', sa.String(), nullable=True),
    sa.Column('arrival_city', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('flights')
    # ### end Alembic commands ###
