#!/usr/bin/env python3
import asyncio
import time

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    s = time.perf_counter()

    await asyncio.gather(count(), count(), count())
    elapsed = time.perf_counter() - s
    print(f"executed in {elapsed:0.2f} seconds")

asyncio.run(main())