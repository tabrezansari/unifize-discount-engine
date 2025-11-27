from decimal import Decimal
from typing import Dict, List, Optional

from discount_engine.models.models import (
    CartItem,
    CustomerProfile,
    DiscountedPrice,
    PaymentInfo,
)
from discount_engine.services.rules.bank_rule import BankDiscountRule
from discount_engine.services.rules.brand_rule import BrandDiscountRule
from discount_engine.services.rules.category_rule import CategoryDiscountRule
from discount_engine.services.rules.coupon_rule import CouponDiscountRule
from discount_engine.services.validators.cart_validator import CartValidator


class DiscountService:
    """
    DiscountService orchestrates discount calculation using a pipeline of modular rules.
    Rule order:
    1. Brand → 2. Category → 3. Coupon → 4. Bank
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

        from decimal import Decimal


from typing import Dict, List, Optional

from discount_engine.models.models import (
    CartItem,
    CustomerProfile,
    DiscountedPrice,
    PaymentInfo,
)
from discount_engine.services.rules.bank_rule import BankDiscountRule
from discount_engine.services.rules.brand_rule import BrandDiscountRule
from discount_engine.services.rules.category_rule import CategoryDiscountRule
from discount_engine.services.rules.coupon_rule import CouponDiscountRule
from discount_engine.services.validators.cart_validator import CartValidator


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

        validator = CartValidator()
        is_valid, message = await validator.validate_coupon(code, cart_items, customer)

        if not is_valid:
            print(f"[Validation Failed] {message}")
            return False

        return True
