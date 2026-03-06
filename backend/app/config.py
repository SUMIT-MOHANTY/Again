import os
RETRY_COUNT = int(os.getenv('RETRY_COUNT', '3'))
RETRY_WAIT = float(os.getenv('RETRY_WAIT', '0.5'))
CB_FAILURE_THRESHOLD = int(os.getenv('CB_FAILURE_THRESHOLD', '5'))
CB_RECOVERY_TIMEOUT = int(os.getenv('CB_RECOVERY_TIMEOUT', '30'))
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+asyncpg://user:pass@localhost/db')
