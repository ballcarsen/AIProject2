import abc

class VariableInterface(abc.ABC):

    @abc.abstractmethod
    def setCompareVal(self, bts):
        pass
