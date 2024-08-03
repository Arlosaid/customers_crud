"""customer table

Revision ID: 82a22c93777c
Revises: 
Create Date: 2024-08-02 23:45:15.487973

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '82a22c93777c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
        sa.Column('telefono', sa.String(length=10), nullable=False),
        sa.Column('nombre', sa.String(length=50), nullable=True),
        sa.Column('apellido', sa.String(length=50), nullable=True),
        sa.Column('edad', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('telefono')
    )
    op.create_index(op.f('ix_customer_telefono'), 'customer', ['telefono'], unique=False)
    # ### end Alembic commands ###



def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_customer_telefono'), table_name='customer')
    op.drop_table('customer')
    # ### end Alembic commands ###