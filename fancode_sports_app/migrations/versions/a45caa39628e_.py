"""empty message

Revision ID: a45caa39628e
Revises: 75938a37a1b3
Create Date: 2023-07-16 12:17:02.343603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a45caa39628e'
down_revision = '75938a37a1b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('news',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('sportId', sa.Integer(), nullable=False),
    sa.Column('tourId', sa.Integer(), nullable=False),
    sa.Column('matchId', sa.Integer(), nullable=False),
    sa.Column('createdAt', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.ForeignKeyConstraint(['matchId'], ['matches.id'], ),
    sa.ForeignKeyConstraint(['sportId'], ['sport.id'], ),
    sa.ForeignKeyConstraint(['tourId'], ['tour.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('news')
    # ### end Alembic commands ###
