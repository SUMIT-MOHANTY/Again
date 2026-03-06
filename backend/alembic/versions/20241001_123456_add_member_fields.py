from alembic import op
import sqlalchemy as sa

revision = "20241001_123456"
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('members', sa.Column('avatar_path', sa.String(), nullable=True))
    op.add_column('members', sa.Column('status', sa.String(), server_default='active'))
    op.add_column('members', sa.Column('role_id', sa.Integer(), sa.ForeignKey('roles.id'), nullable=True))

def downgrade():
    op.drop_column('members', 'role_id')
    op.drop_column('members', 'status')
    op.drop_column('members', 'avatar_path')
