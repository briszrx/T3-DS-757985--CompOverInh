from abc import ABC, abstractmethod
from dataclasses import dataclass

class Contract(ABC):
    """Representa el contrato y el proceso de pago para un empleado particular"""

    @abstractmethod
    def get_payment(self) -> float:
        """Calcula cuanto pagar al empleado bajo este contrato"""