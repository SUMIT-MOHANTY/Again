from sqlalchemy.ext.asyncio import AsyncSession
from .model.models import ApiCallLog, CircuitBreakerState
from .util.logger import logger
async def log_api_call(session: AsyncSession, **kwargs):
    log = ApiCallLog(**kwargs)
    session.add(log)
    await session.commit()
    logger.info(f'Logged API call {log.request_id}')
async def get_cb_state(session: AsyncSession, service_name: str):
    result = await session.get(CircuitBreakerState, {'service_name': service_name})
    return result
async def upsert_cb_state(session: AsyncSession, service_name: str, state: str, failures: int):
    obj = await session.get(CircuitBreakerState, {'service_name': service_name})
    if not obj:
        obj = CircuitBreakerState(service_name=service_name, state=state, failure_count=failures)
        session.add(obj)
    else:
        obj.state = state
        obj.failure_count = failures
    await session.commit()
