import asyncio

async def coro_func():
    return "Hello, asyncio!"

async def main():
    print("The entry point of a corotine.")
    results = await coro_func()
    print(results)

asyncio.run(main())