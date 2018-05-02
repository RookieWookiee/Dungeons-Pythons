class ConsumableMixin:
    def __init__(self, effect):
        self.effect = effect

    def consume(self, *args, **kwargs):
        raise NotImplemented

    @classmethod
    def generate(cls, obj):
        raise NotImplemented
