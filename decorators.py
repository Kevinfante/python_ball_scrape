from functools import wraps
import traceback

def exception_handler(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            # print('e handler')
            return f(*args, **kwargs)
        except ValueError as e:
            return (traceback.format_exception(e))[3], 404
        except Exception as e:
            print('bye: ')
    return decorated

