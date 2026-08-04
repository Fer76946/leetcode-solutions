class MyHashMap:

    def __init__(self):
        self.mappy = {}

    def put(self, key: int, value: int) -> None:
        self.mappy[key] = value

    def get(self, key: int) -> int:
        return self.mappy.get(key, -1)

    def remove(self, key: int) -> None:
        if key in self.mappy:
            del self.mappy[key]