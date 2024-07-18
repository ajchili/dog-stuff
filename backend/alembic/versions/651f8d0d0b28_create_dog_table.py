"""create dog table

Revision ID: 651f8d0d0b28
Revises: 
Create Date: 2024-07-18 18:52:34.158359

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '651f8d0d0b28'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "dog",
        sa.Column('id', sa.Interval, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(50), nullable=False)
    )


def downgrade() -> None:
    op.drop_table("dog")
