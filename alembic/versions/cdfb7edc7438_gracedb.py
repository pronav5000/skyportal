"""GraceDB migration

Revision ID: cdfb7edc7438
Revises: 0a4e98db3bcb
Create Date: 2023-05-28 20:40:26.222474

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'cdfb7edc7438'
down_revision = '0a4e98db3bcb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'gcnevents',
        sa.Column(
            'gracedb_log',
            postgresql.JSONB(astext_type=sa.Text()),
            server_default='{}',
            nullable=False,
        ),
    )
    op.add_column(
        'gcnevents',
        sa.Column(
            'gracedb_labels',
            postgresql.JSONB(astext_type=sa.Text()),
            server_default='{}',
            nullable=False,
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('gcnevents', 'gracedb_labels')
    op.drop_column('gcnevents', 'gracedb_log')
    # ### end Alembic commands ###