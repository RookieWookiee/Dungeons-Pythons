class WalkableMixin:
    def __do_nothing(self, obj):
        return True

    _on_enter = __do_nothing
    _on_leave = __do_nothing

    def trigger_enter_event(self, *args, **kwargs):
        self._on_enter(*args, **kwargs)

    def trigger_leave_event(self, *args, **kwargs):
        self._on_leave(*args, **kwargs)
