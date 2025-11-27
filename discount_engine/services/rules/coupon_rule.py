from decimal import Decimal
from discount_engine.services.rules.base import DiscountRule


class CouponDiscountRule(DiscountRule):
    name = "coupon_discount"

    async def apply(self, cart_items, customer, current_price, payment_info=None):
        # Coupon logic will be added later in Phase 6
        return Decimal("0")
