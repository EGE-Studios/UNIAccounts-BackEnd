"""empty message

Revision ID: f469bbec3ae9
Revises: 80d2528e0842
Create Date: 2023-05-26 09:09:04.957586

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'f469bbec3ae9'
down_revision = '80d2528e0842'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('forgot_codes',
    sa.Column('user_name', sa.String(length=255), nullable=False),
    sa.Column('code', sa.String(length=255), nullable=False),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('is_removed', sa.Boolean(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('forgot_codes')
    # ### end Alembic commands ###
