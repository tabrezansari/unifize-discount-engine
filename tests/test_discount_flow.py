import pytest
from decimal import Decimal

from discount_engine.data.fake_data import cart_items, customer, payment_info
from discount_engine.services.discount_service import DiscountService


@pytest.mark.asyncio
async def test_multiple_discount_stacking():
    service = DiscountService()

    result = await service.calculate_cart_discounts(
        cart_items=cart_items,
        customer=customer,
        payment_info=payment_info,
    )

    assert result.original_price == Decimal("1000")
    assert result.final_price == Decimal("486")
    assert result.applied_discounts["brand_discount"] == Decimal("400")
    assert result.applied_discounts["category_discount"] == Decimal("60")
    assert result.applied_discounts["bank_discount"] == Decimal("54")
