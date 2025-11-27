from decimal import Decimal

from discount_engine.services.rules.base import DiscountRule


class BankDiscountRule(DiscountRule):
    name = "bank_discount"

    async def apply(self, cart_items, customer, current_price, payment_info=None):
        if payment_info and payment_info.bank_name == "ICICI":
            return current_price * Decimal("0.10")
        return Decimal("0")
