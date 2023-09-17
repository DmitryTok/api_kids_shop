import datetime

from kids_shop.logger import logger


def time_checker(func):

    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        total_time = end_time - start_time
        logger.info(f'Function: {func.__name__} | Time: {total_time}')
        return result
    return wrapper
