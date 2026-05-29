"""Insert test data

Revision ID: 18b18dda638f
Revises: 61d56e8ea818
Create Date: 2026-05-29 14:58:59.668434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18b18dda638f'
down_revision = '61d56e8ea818'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
    INSERT INTO categories (name)
    VALUES ('Phones')
    """)

    op.execute("""
    INSERT INTO products
    (name, price, active, category_id)
    VALUES
    ('iPhone 15', 999, 1, 1)
    """)


def downgrade():
    op.execute("DELETE FROM products")

    op.execute("DELETE FROM categories")
