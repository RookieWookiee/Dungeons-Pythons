from src.mixins.print_sym import PrintSymbolMixin
from src.mixins.walkable import WalkableMixin

class OccupiableMixin(WalkableMixin):
    def __init__(self):
        self.occupant = None

    def trigger_enter_on_occupant(self, *args, **kwargs):
        if self.occupant is not None:
            self.occupant._on_enter(*args, **kwargs)

    _on_enter = trigger_enter_on_occupant
