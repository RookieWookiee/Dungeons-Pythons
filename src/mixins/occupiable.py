from src.mixins.walkable import WalkableMixin


class OccupiableMixin(WalkableMixin):
    def __init__(self):
        self.occupant = None

    def trigger_enter_event(self, obj):
        if self.occupant is not None:
            ret = self.occupant.trigger_enter_event(obj)
            if not ret:
                return

        self.occupant = obj
        self.sym = obj.sym
        return True

    def trigger_leave_event(self):
        if self.occupant is None:
            raise ValueError('There is no occupant')

        self.occupant = None
        self.sym = self.__class__.sym

    _on_enter = trigger_enter_event
    _on_leave = trigger_leave_event
