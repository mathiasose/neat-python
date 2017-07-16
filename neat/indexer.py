from uuid import uuid4


class SequentialIndexer(object):
    def __init__(self, first):
        self.next_id = first

    def get_next(self, result=None):
        '''
        If result is not None, then we return it unmodified.  Otherwise,
        we return the next ID and increment our internal counter.
        '''
        if result is None:
            result = self.next_id
            self.next_id += 1
        return result


class UUIDIndexer(SequentialIndexer):
    """
    Uses random universally unique identifiers as indices.
     With a size of 128 bits per index, collisions are impossible for all practical purposes.
    """

    def __init__(self, first=None):
        super().__init__(first=first)

    def get_next(self, result=None):
        if result is None:
            result = uuid4().int
        return result
