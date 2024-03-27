'''Decorators module'''
from functools import wraps


def decorator_example():
    '''Decorator to update the timestamp of a project last update.'''
    def build_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            '''Wrapping function to decorator'''

            # Validate kwargs data
            # example = kwargs.get('example', kwargs.get('_example'))

            # Do stuff before function with decorator execution

            executed_func = func(*args, **kwargs)

            # Do stuff after function with decorator execution

            return executed_func

        return wrapper
    return build_decorator
