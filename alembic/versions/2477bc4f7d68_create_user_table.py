"""create user table

Revision ID: 2477bc4f7d68
Revises: 
Create Date: 2023-03-16 15:48:42.097054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2477bc4f7d68'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False, primary_key=True, autoincrement=True), sa.Column('email', sa.String(), nullable=False, unique=True), sa.Column('username', sa.String(), nullable=False), sa.Column('password', sa.String(), nullable=False), sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.text('now()')), sa.Column('updated_at', sa.DateTime(), nullable=True))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
