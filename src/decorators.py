from functools import wraps


def accepts(*types):
    def accepter(func):
        if len(types) + 1 != func.__code__.co_argcount:
            raise ValueError('The number of types should be the same as the number of arguments in the decorated function.')

        @wraps(func)
        def decorated(*args):
            argtypes = tuple(map(type, args[1:]))
            if any(not isinstance(arg, t) for t, arg in zip(argtypes, args[1:])):
                raise TypeError(f'{func.__name__} expects {types}, got {argtypes}')
            return func(*args)

        return decorated
    return accepter
