"""fix: add VARCHAR lengths

Revision ID: 81857efdd2a8
Revises: 
Create Date: 2025-07-16 15:14:15.404962

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '81857efdd2a8'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bookings')
    op.drop_index(op.f('email'), table_name='newsletter_subscriptions')
    op.drop_table('newsletter_subscriptions')
    op.drop_table('reviews')
    op.alter_column('destination_images', 'destination_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('destination_images', 'image_url',
               existing_type=mysql.VARCHAR(length=500),
               type_=sa.String(length=255),
               nullable=False)
    op.create_index(op.f('ix_destination_images_id'), 'destination_images', ['id'], unique=False)
    op.drop_constraint(op.f('destination_images_ibfk_1'), 'destination_images', type_='foreignkey')
    op.create_foreign_key(None, 'destination_images', 'destinations', ['destination_id'], ['id'], ondelete='CASCADE')
    op.alter_column('destinations', 'country_name',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=255),
               nullable=False)
    op.alter_column('destinations', 'region',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=255),
               nullable=False)
    op.alter_column('destinations', 'slug',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=255),
               nullable=False)
    op.alter_column('destinations', 'city',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=255),
               existing_nullable=True)
    op.alter_column('destinations', 'description',
               existing_type=mysql.TEXT(),
               type_=sa.String(length=255),
               existing_nullable=True)
    op.alter_column('destinations', 'airport',
               existing_type=mysql.VARCHAR(length=150),
               type_=sa.String(length=255),
               existing_nullable=True)
    op.alter_column('destinations', 'image_url',
               existing_type=mysql.TEXT(),
               type_=sa.String(length=255),
               existing_nullable=True)
    op.drop_index(op.f('slug'), table_name='destinations')
    op.create_index(op.f('ix_destinations_id'), 'destinations', ['id'], unique=False)
    op.create_index(op.f('ix_destinations_slug'), 'destinations', ['slug'], unique=True)
    op.create_index(op.f('ix_leads_id'), 'leads', ['id'], unique=False)
    op.create_index(op.f('ix_package_categories_id'), 'package_categories', ['id'], unique=False)
    op.alter_column('package_images', 'package_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.create_index(op.f('ix_package_images_id'), 'package_images', ['id'], unique=False)
    op.create_index(op.f('ix_packages_id'), 'packages', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_packages_id'), table_name='packages')
    op.drop_index(op.f('ix_package_images_id'), table_name='package_images')
    op.alter_column('package_images', 'package_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.drop_index(op.f('ix_package_categories_id'), table_name='package_categories')
    op.drop_index(op.f('ix_leads_id'), table_name='leads')
    op.drop_index(op.f('ix_destinations_slug'), table_name='destinations')
    op.drop_index(op.f('ix_destinations_id'), table_name='destinations')
    op.create_index(op.f('slug'), 'destinations', ['slug'], unique=True)
    op.alter_column('destinations', 'image_url',
               existing_type=sa.String(length=255),
               type_=mysql.TEXT(),
               existing_nullable=True)
    op.alter_column('destinations', 'airport',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=150),
               existing_nullable=True)
    op.alter_column('destinations', 'description',
               existing_type=sa.String(length=255),
               type_=mysql.TEXT(),
               existing_nullable=True)
    op.alter_column('destinations', 'city',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=True)
    op.alter_column('destinations', 'slug',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=100),
               nullable=True)
    op.alter_column('destinations', 'region',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=100),
               nullable=True)
    op.alter_column('destinations', 'country_name',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=100),
               nullable=True)
    op.drop_constraint(None, 'destination_images', type_='foreignkey')
    op.create_foreign_key(op.f('destination_images_ibfk_1'), 'destination_images', 'destinations', ['destination_id'], ['id'])
    op.drop_index(op.f('ix_destination_images_id'), table_name='destination_images')
    op.alter_column('destination_images', 'image_url',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=500),
               nullable=True)
    op.alter_column('destination_images', 'destination_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.create_table('reviews',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('author', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('review_descp', mysql.TEXT(), nullable=True),
    sa.Column('review_rating', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('newsletter_subscriptions',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('subscribed_at', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index(op.f('email'), 'newsletter_subscriptions', ['email'], unique=True)
    op.create_table('bookings',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('full_name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('phone', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('package_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('number_of_people', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('total_price', mysql.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('travel_date', sa.DATE(), nullable=True),
    sa.Column('status', mysql.VARCHAR(length=20), server_default=sa.text("'pending'"), nullable=True),
    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.ForeignKeyConstraint(['package_id'], ['packages.id'], name=op.f('bookings_ibfk_1')),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
