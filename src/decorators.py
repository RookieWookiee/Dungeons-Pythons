from functools import wraps
from src.mixins.walkable import WalkableMixin


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


def validate_move(func):
    @wraps(func)
    def decorated(self, direction):
        if self.hero is None:
            raise ValueError('A hero must be spawned first')
        if direction not in ('up', 'down', 'left', 'right'):
            raise ValueError('Invalid direction')

        dx = 1 if direction == 'right' else (-1 if direction == 'left' else 0)
        dy = 1 if direction == 'down' else (-1 if direction == 'up' else 0)

        from_row, from_col = self.hero.row, self.hero.col
        target_row, target_col = from_row + dy, from_col + dx

        if target_row < 0 or target_row >= len(self.grid):
            return False
        if target_col < 0 or target_col >= len(self.grid[target_row]):
            return False

        if not isinstance(self.grid[target_row][target_col], WalkableMixin):
            return False

        return func(self, target_row, target_col)

    return decorated
