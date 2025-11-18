import asyncio
import time

async def heavy_task(id):
    print(f"Start {id}")
    await asyncio.sleep(2)  # I/O wait (non blocking)
    print(f"End {id}")
    return id

async def main():
    start = time.time()

    tasks = [asyncio.create_task(heavy_task(i)) for i in range(5)]
    results = await asyncio.gather(*tasks)

    print("Results:", results)
    print("Total Time:", time.time() - start)

asyncio.run(main())
