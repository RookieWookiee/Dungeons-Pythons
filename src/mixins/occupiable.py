from src.mixins.print_sym import PrintSymbolMixin
from src.mixins.walkable import WalkableMixin

class OccupiableMixin(WalkableMixin):
    def __init__(self):
        self.occupant = None

    def trigger_enter_event(self, *args, **kwargs):
        if self.occupant is not None:
            self.occupant._on_enter(*args, **kwargs)

    def trigger_leave_event(self, *args, **kwargs):
        if self.occupant is None:
            raise ValueError('There is no occupant')

        self.occupant = None

    _on_enter = trigger_enter_event
    _on_leave = trigger_leave_event
