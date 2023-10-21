import abc


class FormatRepository(abc.ABC):
    @abc.abstractmethod
    def write(self, row): ...
    @abc.abstractmethod
    def get_data(self): ...


# DAO - DATA ACCESS OBJECT
