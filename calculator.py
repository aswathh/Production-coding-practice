# Task 1(Beginner):
import logging


logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(levelname)s-%(message)s')
logger = logging.getLogger(__name__)

def add(a:int,b:int)-> int:
    return a+b
try:
    result= add(4,5)
    logger.info(f"Addition result:{result}")

except Exception:
    logger.error("Addition failed",exc_info=True)

print(result)


