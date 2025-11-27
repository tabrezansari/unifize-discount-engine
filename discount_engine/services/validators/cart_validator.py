from typing import Tuple


class CartValidator:
    """
    Validation module for discount codes.

    Supports:
    - Brand exclusions
    - Category restrictions
    - Customer tier checks
    """

    async def validate_coupon(
        self,
        code: str,
        cart_items,
        customer,
    ) -> Tuple[bool, str]:

        code = code.upper()

        # EXAMPLE SCENARIOS (these mirror real e-commerce logic):

        # 1) SUPER69 excluding PUMA
        if code == "SUPER69":
            for item in cart_items:
                if item.product.brand.lower() == "puma":
                    return False, "Coupon SUPER69 is not valid on PUMA products."

        # 2) TSHIRT10 only for T-shirt category
        if code == "TSHIRT10":
            for item in cart_items:
                if item.product.category.lower() != "tshirt":
                    return False, "Coupon TSHIRT10 is only valid on T-shirts."

        # 3) VIPONLY requires VIP tier
        if code == "VIPONLY":
            if customer.tier.upper() != "VIP":
                return False, "Only VIP customers can use this coupon."

        # Default: valid coupon
        return True, "Coupon is valid."
