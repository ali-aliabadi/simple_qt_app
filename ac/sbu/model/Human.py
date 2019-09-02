class Human:
    def __init__(self, name, family) -> None:
        self._name = name
        self.family = family

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def __str__(self) -> str:
        return 'Human[name : \'' + self._name + '\', family_name : \'' + self.family + '\']'
