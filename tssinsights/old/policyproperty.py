from abc import ABC, abstractmethod


class PolicyProperty(ABC):

    @staticmethod
    @abstractmethod
    def check_property() -> bool:
        pass

    @staticmethod
    @abstractmethod
    def description() -> None:
        pass


Policy = list[tuple[int, int, int], list[PolicyProperty]]

