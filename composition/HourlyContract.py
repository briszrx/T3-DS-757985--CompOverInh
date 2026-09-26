from dataclasses import dataclass
from Contract import Contract


@dataclass
class HourlyContract(Contract):
    """Tipo de contrato de un empleado que se le paga por hora."""

    pay_rate: float
    hours_worked: int = 0
    employer_cost: float = 1000

    def get_payment(self) -> float:
        return self.pay_rate * self.hours_worked + self.employer_cost