"""empty message

Revision ID: 6926f554024d
Revises: 4bc3581b0207
Create Date: 2023-07-15 23:15:05.041539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6926f554024d'
down_revision = '4bc3581b0207'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('matches',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('tourId', sa.Integer(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('format', sa.String(length=50), nullable=False),
    sa.Column('startTime', sa.TIMESTAMP(), nullable=False),
    sa.Column('endTime', sa.TIMESTAMP(), nullable=False),
    sa.Column('recUpdatedAt', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('createdAt', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('matches')
    # ### end Alembic commands ###
