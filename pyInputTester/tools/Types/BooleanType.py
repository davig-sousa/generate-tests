class BooleanType:

    def __init__(self):
        self.calls = -1

    def get_boolean(self):
        self.calls += 1
        return True if self.calls % 2 == 0 else False
