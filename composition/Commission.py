from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Commission(ABC):
    """Representa el proceso de pago por comisión"""

    @abstractmethod
    def get_payment(self) -> float:
        """Devuelve la comisión a ser pagada"""