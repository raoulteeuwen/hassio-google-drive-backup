class Version:
    def __init__(self, *args):
        self._identifiers = args

    @classmethod
    def default(cls):
        return Version(0)

    @classmethod
    def parse(cls, version):
        parts = []
        for part in version.split("."):
            parts.append(int(part))
        return Version(*parts)

    def __getitem__(self, key):
        return self._identifiers[key]

    def length(self):
        return len(self._identifiers)

    def _compare(self, other):
        i = 0
        while(i < min(self.length(), other.length())):
            if self[i] < other[i]:
                return -1
            if self[i] > other[i]:
                return 1
            i += 1
        if self.length() < other.length():
            return -1
        if self.length() > other.length():
            return 1
        return 0

    def __lt__(self, other):
        return self._compare(other) < 0

    def __le__(self, other):
        return self._compare(other) <= 0

    def __eq__(self, other):
        return self._compare(other) == 0

    def __ne__(self, other):
        return self._compare(other) != 0

    def __gt__(self, other):
        return self._compare(other) > 0

    def __ge__(self, other):
        return self._compare(other) >= 0

    def __str__(self):
        return ".".join(str(i) for i in self._identifiers)
