from src.mixins.print_sym import PrintSymbolMixin
from src.mixins.walkable import WalkableMixin

class OccupiableMixin(WalkableMixin):
    def __init__(self):
        self.occupant = None
