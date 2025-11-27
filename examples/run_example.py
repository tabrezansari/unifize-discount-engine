import asyncio

from discount_engine.data.fake_data import cart_items, customer, payment_info
from discount_engine.services.discount_service import DiscountService


async def main():
    service = DiscountService()
    result = await service.calculate_cart_discounts(
        cart_items=cart_items, customer=customer, payment_info=payment_info
    )

    print("Original Price:", result.original_price)
    print("Final Price:", result.final_price)
    print("Applied Discounts:", result.applied_discounts)
    print("Message:", result.message)


asyncio.run(main())
