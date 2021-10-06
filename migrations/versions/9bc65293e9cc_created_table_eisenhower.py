"""Created table Eisenhower

Revision ID: 9bc65293e9cc
Revises: 4a5f33ed73ee
Create Date: 2021-10-05 00:19:42.307392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9bc65293e9cc'
down_revision = '4a5f33ed73ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('eisenhowers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('eisenhowers')
    # ### end Alembic commands ###
