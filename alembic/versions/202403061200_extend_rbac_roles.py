from alembic import op
import sqlalchemy as sa

revision = '202403061200'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # extend role enum - PostgreSQL needs a new enum type then replace column
    role_enum = sa.Enum('Admin','Librarian','Member','Guest', name='role_enum')
    role_enum.create(op.get_bind(), checkfirst=True)
    op.alter_column('roles', 'name', type_=role_enum, existing_type=sa.VARCHAR(), nullable=False)
    # insert default permissions
    perms = [
        {'module':'books','action':'create','description':'Create books'},
        {'module':'books','action':'read','description':'Read books'},
        {'module':'books','action':'update','description':'Update books'},
        {'module':'books','action':'delete','description':'Delete books'},
        {'module':'reports','action':'export','description':'Export reports'},
    ]
    op.bulk_insert(sa.table('permissions', sa.column('module'), sa.column('action'), sa.column('description')), perms)

def downgrade():
    op.alter_column('roles', 'name', type_=sa.String(), existing_type=sa.Enum(name='role_enum'))
    role_enum = sa.Enum(name='role_enum')
    role_enum.drop(op.get_bind())
