class PrintSymbolMixin:
    def print_sym(self):
        print(self.sym)

    def get_sym(self):
        return self.sym

    def __str__(self):
        return self.sym
