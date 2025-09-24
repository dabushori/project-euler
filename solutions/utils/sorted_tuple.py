class SortedTuple(tuple):
    def __new__(cls, elements):
        return super(SortedTuple, cls).__new__(cls, sorted(elements))
