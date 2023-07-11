import asyncio
async def coro_func():
    print("Hello, async")

async def main():
    print("I am to host an await funtion")
    await coro_func()

asyncio.run(main())