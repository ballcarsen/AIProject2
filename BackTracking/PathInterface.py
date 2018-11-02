import abc

class PathInterface(abc.ABC):

    @abc.abstractmethod
    def __lt__(self, other):
        pass