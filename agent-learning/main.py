import asyncio
from metagpt.logs import logger
from runnable_coder import RunnableCoder


async def main():
    msg = "write a function that calculates the sum of a list"
    role = RunnableCoder()
    logger.info(msg)
    result = await role.run(msg)
    logger.info(result)

asyncio.run(main())
