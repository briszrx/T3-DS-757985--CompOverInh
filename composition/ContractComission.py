from dataclasses import dataclass
from Commission import Commission


@dataclass
class ContractCommission(Commission):
    """Representa el sistema de comisiones basado por el númeor de contratos realicados"""

    commission: float = 100
    contracts_landed: int = 0

    def get_payment(self) -> float:
        """Retorna la comisión a pagar"""
        return self.commission * self.contracts_landed