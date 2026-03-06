from alembic import op
import sqlalchemy as sa
from sqlalchemy_utils import EncryptedType, AesEngine

# revision identifiers, used by Alembic.
revision = 'xxxx'
 down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'documents',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('content', EncryptedType(sa.String, sa.text(''), AesEngine, 'pkcs5'), nullable=False),
        sa.Column('metadata', EncryptedType(sa.String, sa.text(''), AesEngine, 'pkcs5')),
    )

def downgrade():
    op.drop_table('documents')
