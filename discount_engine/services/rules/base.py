from abc import ABC, abstractmethod
from decimal import Decimal
from typing import List, Optional

from discount_engine.models.models import CartItem, CustomerProfile, PaymentInfo


class DiscountRule(ABC):
    """
    Strategy base class for discount rules.
    Ensures each discount rule returns a discount amount (Decimal),
    based on the current cart price and applied conditions.
    """

    name: str = "base_rule"

    @abstractmethod
    async def apply(
        self,
        cart_items: List[CartItem],
        customer: CustomerProfile,
        current_price: Decimal,
        payment_info: Optional[PaymentInfo] = None,
    ) -> Decimal:
        """
        Each rule calculates and returns ONLY the discount amount.
        DiscountService will subtract it and maintain the final price.
        """
        pass
