import os
import logging
from dotenv import load_dotenv
from typing import List

load_dotenv()
logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(levelname)s-%(message)s')
logger = logging.getLogger(__name__)

def read_numbers(file_path:str)->List[int]:
    numbers:List[int]=[]
    try:
        with open(file_path,"r") as f:
            for line in f:
                line = line.strip() 
                if line:
                    numbers.append(int(line))
        logger.info(f"Successfully read {len(numbers)} numbers from the {file_path}")
    except FileNotFoundError:
        logger.error(f"file not found{file_path}",exc_info = True)
    except ValueError:
        logger.error(f"Invalid number in the given file:{file_path}",exc_info=True)
    
    return numbers
input_path:str =os.getenv("FILE_PATH","Fileprocessor.txt")
numbers = read_numbers(input_path)
if numbers:
    total = sum(numbers)
    logger.info(f"Total sum:",{total})
else:
    logger.warning("No numbers found in the process")
