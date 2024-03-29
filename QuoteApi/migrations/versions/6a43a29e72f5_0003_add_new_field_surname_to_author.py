"""0003 add new field:surname to Author

Revision ID: 6a43a29e72f5
Revises: 68fceef60e41
Create Date: 2024-03-10 14:27:15.668833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a43a29e72f5'
down_revision = '68fceef60e41'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('authors', schema=None) as batch_op:
        batch_op.add_column(sa.Column('surname', sa.String(length=32), server_default='Petrov', nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('authors', schema=None) as batch_op:
        batch_op.drop_column('surname')

    # ### end Alembic commands ###
