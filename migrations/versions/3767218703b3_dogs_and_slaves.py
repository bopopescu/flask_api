"""dogs and slaves

Revision ID: 3767218703b3
Revises: 
Create Date: 2019-04-24 17:04:52.238155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3767218703b3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('species', sa.String(length=80), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('slave',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sex', sa.String(length=80), nullable=False),
    sa.Column('dog_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['dog_id'], ['dog.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('slave')
    op.drop_table('dog')
    # ### end Alembic commands ###