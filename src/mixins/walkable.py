from src.mixins.print_sym import PrintSymbolMixin

class WalkableMixin:
    def __do_nothing():
        pass

    _on_enter = __do_nothing

    def trigger_enter_event(self, *args, **kwargs):
        self._on_enter(*args, **kwargs)
