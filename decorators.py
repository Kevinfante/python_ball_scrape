from functools import wraps
import traceback


def exception_handler():
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except ValueError:
                print('hello: ', traceback.format_exc)
            except Exception as e:
                print('bye: ')
        return decorated
    return decorator


# def Error_Handler(func):
#     def Inner_Function(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#         except ValueError:
#             print(f"{func.__name__} wrong data types. enter numeric")
#     return Inner_Function
