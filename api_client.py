import logging
from dotenv import load_dotenv
import os
from typing import Union

load_dotenv()

logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(filename)s-%(levelname)s-%(message)s')

logger = logging.getLogger(__name__)

def call_api(prompt:str)-> Union[str,None]:
    """Here the Groq api key call is happening"""
    api_key = os.getenv("GROQ_API_KEY")
    

    if api_key is None:
        logger.critical("API_key is not found")
        return None
    else:
        logger.info("API_KEY found")

    if prompt.strip() == "":

        logger.warning("Empty prompt recieved skipping api call")
        return None
    
    response = f"Mock response for :{prompt}"
    logger.info(f"API call successful for prompt: '{prompt}'")
    return response
    
