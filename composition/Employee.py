from dataclasses import dataclass
from typing import Optional
from Contract import Contract
from Commission import Commission


@dataclass
class Employee:
    """Representación básica de un empleado en la empresa"""

    name: str
    id: int
    contract: Contract
    commission: Optional[Commission] = None

    def compute_pay(self) -> float:
        """Calcula cuanto se le debe pagar al empleado."""
        payout = self.contract.get_payment()
        if self.commission is not None:
            payout += self.commission.get_payment()
        return payout