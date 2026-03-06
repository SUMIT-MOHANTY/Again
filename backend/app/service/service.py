from ..client.http_client import ResilientClient
from ..util.uuid_gen import gen_uuid
client = ResilientClient()
async def fetch_external_data():
    url = 'https://httpbin.org/get'
    response = await client.get(url)
    return response.json()
