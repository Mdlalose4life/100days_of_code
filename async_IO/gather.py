import asyncio
from datetime import datetime

async def async_sleep(num):
    print(f"Sleeping {num} seconds.")
    await asyncio.sleep(num)


async def main():
    start = datetime.now()
    
    coro_obj = []
    for i in range(1, 6):
        coro_obj.append(async_sleep(i))
    
    await asyncio.gather(*coro_obj)
        
    duration = datetime.now() - start
    print(f"It took {duration.total_seconds():.2f} seconds.")
    
asyncio.run(main())