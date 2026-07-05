import logging
from api_client import call_api

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(filename)s-%(levelname)s-%(message)s')

logger = logging.getLogger(__name__)

logger.info("Application started")
result1= call_api("Expalin langraph in simple terms")
print(result1)

result2 = call_api("") #empty prompt
print(result2)