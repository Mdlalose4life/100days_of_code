import asyncio
import aiohttp

async def scrape_page(session, url):
    print(f"Scrapping {url}")
    async with session.get(url) as response:
        return len(await response.text())
    
async def main():
    url = [
            'https://example.com/posts/1',
            'https://example.com/posts/2',
            'https://example.com/posts/3',
            'https://example.com/posts/4',
            'https://example.com/posts/5',
            'https://example.com/posts/6',
            'https://example.com/posts/7',
            'https://example.com/posts/8',
            ]
    
    coro_obj = []

    async with aiohttp.ClientSession() as session:
        for url in url:
            coro_obj.append(
                scrape_page(session, url)
            )
        results = await asyncio.gather(*coro_obj)

    for url, length in zip(url, results):
        print(f"{url}->{length}")

asyncio.run(main())