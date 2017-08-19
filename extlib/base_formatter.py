# formatter.py
from abc  import abstractmethod, ABCMeta

class Formatter(metaclass=ABCMeta):
    # contract definition

    @abstractmethod
    def headings(self, headers):
        #raise NotImplementedError
        pass

    @abstractmethod
    def row(self, rowdata):
        #raise NotImplementedError
        pass
