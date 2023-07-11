import asyncio
from datetime import datetime

async def async_sleep(num):
    print(f"Sleeping {num} seconds")
    await asyncio.sleep(num)

async def main():
    start = datetime.now()

    for i in range(1, 4):
        await async_sleep(i)

    duration = datetime.now() - start
    print(f"Took off at {duration.total_seconds():.2f} seconds.")

asyncio.run(main())