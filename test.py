import asyncio
from concurrent.futures import ThreadPoolExecutor
import requests

URLS = [
  'https://www.kaidee.com',
  'https://www.python.org',
  'https://www.google.com',
]

async def fetch(executor, url):
  print('Fetching {}'.format(url))
  resp = await asyncio.wrap_future(executor.submit(requests.get, url))
  data = resp.text
  print('{} page is {} bytes'.format(url, len(data)))

async def main():
  with ThreadPoolExecutor(max_workers=3) as executor:
    coros = [fetch(executor, url) for url in URLS]
    await asyncio.gather(*coros)

if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())
