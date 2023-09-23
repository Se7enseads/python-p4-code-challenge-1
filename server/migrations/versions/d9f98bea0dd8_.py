"""empty message

Revision ID: d9f98bea0dd8
Revises: 29e54e848982
Create Date: 2023-09-23 21:08:14.706107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9f98bea0dd8'
down_revision = '29e54e848982'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_restaurants')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('_alembic_tmp_restaurants',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.INTEGER(), nullable=True),
    sa.Column('address', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###