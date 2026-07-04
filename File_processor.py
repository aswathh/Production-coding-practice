import os
from typing import List
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(filename)s-%(levelname)s-%(message)s')
logger = logging.getLogger(__name__)

def get_numbers(file_path:str)->List[int]:
    numbers:List[int] = []
    try:
        with open(file_path,"r") as f:
            for line in f:
                line = line.strip()
                if line:
                    numbers.append(int(line))
        logging.info(f"Successfully read {len(numbers)} numbers from {filepath}")
    except FileNotFoundError:
        logging.error(f"File not found in the path:{file_path}")
    except ValueError:
        logging.error(f"Invalid number in the file {file_path}")
    return numbers

numbers = os.getenv("FILE_PATH","Fileprocessor.txt")

if numbers:
    total = sum(numbers)
    logger.info(f"sum of numbers:{total}")
else:
    logger.warning("No numbers found to process")
