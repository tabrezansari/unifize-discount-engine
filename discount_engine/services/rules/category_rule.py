from decimal import Decimal
from discount_engine.services.rules.base import DiscountRule


class CategoryDiscountRule(DiscountRule):
    name = "category_discount"

    async def apply(self, cart_items, customer, current_price, payment_info=None):
        # Hardcoded 10% category discount
        return current_price * Decimal("0.10")
