"""empty message

Revision ID: 6acef9b730b0
Revises: 
Create Date: 2022-03-12 12:15:15.147350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6acef9b730b0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ads',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(length=120), nullable=True),
    sa.Column('data_create', sa.Date(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ads_description'), 'ads', ['description'], unique=True)
    op.create_index(op.f('ix_ads_title'), 'ads', ['title'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_ads_title'), table_name='ads')
    op.drop_index(op.f('ix_ads_description'), table_name='ads')
    op.drop_table('ads')
    # ### end Alembic commands ###
