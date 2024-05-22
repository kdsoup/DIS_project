"""Initial migration.

Revision ID: 28326e7dc42e
Revises: bb23ecb912bb
Create Date: 2024-05-22 22:33:48.932977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28326e7dc42e'
down_revision = 'bb23ecb912bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wine', schema=None) as batch_op:
        batch_op.add_column(sa.Column('country', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('points', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('price', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('province', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('region_1', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('region_2', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('variety', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('winery', sa.String(length=100), nullable=True))
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wine', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
        batch_op.drop_column('winery')
        batch_op.drop_column('variety')
        batch_op.drop_column('region_2')
        batch_op.drop_column('region_1')
        batch_op.drop_column('province')
        batch_op.drop_column('price')
        batch_op.drop_column('points')
        batch_op.drop_column('country')

    # ### end Alembic commands ###
