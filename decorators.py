from functools import wraps
import traceback
import logging
from datetime import date

# adding logging to exception_handler
def logger(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        logging.basicConfig(filename="scrape.log", level=logging.DEBUG,
                            format="%(asctime)s - %(message)s", datefmt='%d-%b-%y %H:%M:%S')
        try:
            # print('e handler')
            return f(*args, **kwargs)
        except ValueError as e:
            logging.info((traceback.format_exception(e))[3])
            return (traceback.format_exception(e))[3], 404
        except Exception as e:
            print('bye: ')
    return decorated

# def exception_handler(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         try:
#             # print('e handler')
#             return f(*args, **kwargs)
#         except ValueError as e:
#             return (traceback.format_exception(e))[3], 404
#         except Exception as e:
#             print('bye: ')
#     return decorated
    # return decorated

