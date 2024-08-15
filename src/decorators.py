import sys
from selenium.common.exceptions import TimeoutException

# Exception handling decorator for get_* functions
def get_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print(f"Error! Link for {func.__name__} not found in link manager dictionary", file=sys.stderr)
            return None
        except TimeoutException:
            print(f"Error! Events are not found in {args[1]()}", file=sys.stderr)
            return None
        
    return wrapper