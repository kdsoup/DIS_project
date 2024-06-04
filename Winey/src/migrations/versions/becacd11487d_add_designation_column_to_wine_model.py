"""Add designation column to Wine model

Revision ID: becacd11487d
Revises: 28326e7dc42e
Create Date: 2024-05-22 22:48:12.600984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'becacd11487d'
down_revision = '28326e7dc42e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wine', schema=None) as batch_op:
        batch_op.add_column(sa.Column('designation', sa.String(length=100), nullable=True))
        batch_op.alter_column('country',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wine', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
        batch_op.alter_column('country',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
        batch_op.drop_column('designation')

    # ### end Alembic commands ###