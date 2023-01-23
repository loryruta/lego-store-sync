"""Add bl_synced_at field in InventoryItem

Revision ID: 54e02469a44e
Revises: b7cf97ae91b4
Create Date: 2023-01-23 14:36:19.031510

"""
from alembic import op
import sqlalchemy as sa


revision = '54e02469a44e'
down_revision = 'b7cf97ae91b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('inventory_items', sa.Column('bl_synced_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('inventory_items', 'bl_synced_at')
    # ### end Alembic commands ###
