"""empty message

Revision ID: 8bcc707f9066
Revises: fa0b6ff9f6da
Create Date: 2022-02-01 15:26:13.888439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8bcc707f9066"
down_revision = "fa0b6ff9f6da"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("User", sa.Column("is_admin", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("User", "is_admin")
    # ### end Alembic commands ###
