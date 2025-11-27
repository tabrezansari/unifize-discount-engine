from decimal import Decimal
from typing import List, Optional

from discount_engine.models.models import (
    CartItem,
    CustomerProfile,
    DiscountedPrice,
    PaymentInfo,
)


class DiscountService:
    async def calculate_cart_discounts(
        self,
        cart_items: List[CartItem],
        customer: CustomerProfile,
        payment_info: Optional[PaymentInfo] = None,
    ) -> DiscountedPrice:

        applied_discounts = {}
        original_price = sum(
            item.product.base_price * item.quantity for item in cart_items
        )
        current_price = original_price

        # Brand discount - 40%
        brand_discount = current_price * Decimal("0.40")
        applied_discounts["brand_discount"] = brand_discount
        current_price -= brand_discount

        # Category discount - 10%
        category_discount = current_price * Decimal("0.10")
        applied_discounts["category_discount"] = category_discount
        current_price -= category_discount

        # Bank offer - ICICI 10%
        if payment_info and payment_info.bank_name == "ICICI":
            bank_discount = current_price * Decimal("0.10")
            applied_discounts["bank_discount"] = bank_discount
            current_price -= bank_discount

        return DiscountedPrice(
            original_price=original_price,
            final_price=current_price,
            applied_discounts=applied_discounts,
            message="Applied brand, category and optional bank discount"
        )

    async def validate_discount_code(
        self,
        code: str,
        cart_items: List[CartItem],
        customer: CustomerProfile,
    ) -> bool:
        return True
