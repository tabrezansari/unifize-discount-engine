from decimal import Decimal

from discount_engine.services.rules.base import DiscountRule


class BrandDiscountRule(DiscountRule):
    """
    Applies brand-specific discount rules.
    In dummy scenario: PUMA has a minimum 40% discount.
    """

    name = "brand_discount"

    async def apply(self, cart_items, customer, current_price, payment_info=None):
        # Hardcoded 40% for PUMA (as per dummy scenario)
        # In a real system this would come from DB/config
        return current_price * Decimal("0.40")
