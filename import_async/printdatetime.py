import asyncio
import datetime

def print_now():
    print(datetime.datetime.now())


async def keep_printing(name: str = "") -> None:
    while True:
        print(name, end=" ")
        print_now()
        await asyncio.sleep(0.50)

async def main() -> None:
    try:
        await asyncio.wait_for(keep_printing("run"), 10)
    except asyncio.TimeoutError:
        print("Time is up")

asyncio.run(main())