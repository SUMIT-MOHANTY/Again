from backend.client.resilient_http_client import client
from backend.models import ExternalRequestLog
from backend.utils.logger import logger
import json
import datetime

class ExternalDataService:
    async def get_resource(self, resource_id: str):
        url = f"https://example.com/api/resource/{resource_id}"
        response = await client.get(url)
        response.raise_for_status()
        payload = response.json()
        log = ExternalRequestLog(
            url=url,
            method="GET",
            status_code=response.status_code,
            response_body=json.dumps(payload),
            fetched_at=datetime.datetime.utcnow(),
        )
        logger.info(f"Fetched external data for {resource_id}")
        return payload
