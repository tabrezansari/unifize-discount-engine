from decimal import Decimal
from typing import List, Optional, Dict

from discount_engine.models.models import (
    CartItem,
    CustomerProfile,
    PaymentInfo,
    DiscountedPrice,
)

from discount_engine.services.rules.brand_rule import BrandDiscountRule
from discount_engine.services.rules.category_rule import CategoryDiscountRule
from discount_engine.services.rules.coupon_rule import CouponDiscountRule
from discount_engine.services.rules.bank_rule import BankDiscountRule


class DiscountService:
    """
    Refactored DiscountService that applies discount rules sequentially.
    """

    def __init__(self):
        # Order matters — matches real e-commerce behavior
        self.rules = [
            BrandDiscountRule(),
            CategoryDiscountRule(),
            CouponDiscountRule(),
            BankDiscountRule(),
        ]

    async def calculate_cart_discounts(
        self,
        cart_items: List[CartItem],
        customer: CustomerProfile,
        payment_info: Optional[PaymentInfo] = None,
    ) -> DiscountedPrice:

        # 1) Original price of the cart (base_price * qty)
        original_price = sum(
            item.product.base_price * item.quantity for item in cart_items
        )

        current_price = original_price
        applied_discounts: Dict[str, Decimal] = {}

        # 2) Apply each rule in exact order
        for rule in self.rules:
            discount = await rule.apply(
                cart_items,
                customer,
                current_price,
                payment_info,
            )

            if discount > 0:
                applied_discounts[rule.name] = discount
                current_price -= discount

        # 3) Return structured response
        return DiscountedPrice(
            original_price=original_price,
            final_price=current_price,
            applied_discounts=applied_discounts,
            message="Applied discount rules (brand → category → coupon → bank).",
        )

    async def validate_discount_code(
        self,
        code: str,
        cart_items: List[CartItem],
        customer: CustomerProfile,
    ) -> bool:
        # Placeholder for Commit 6
        return True
