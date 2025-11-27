from decimal import Decimal

from discount_engine.models.models import (
    BrandTier,
    CartItem,
    CustomerProfile,
    PaymentInfo,
    Product,
)

puma_tshirt = Product(
    id="PUMA-TSHIRT-001",
    brand="PUMA",
    brand_tier=BrandTier.REGULAR,
    category="tshirt",
    base_price=Decimal("1000"),
    current_price=Decimal("1000"),
)

cart_items = [CartItem(product=puma_tshirt, quantity=1, size="M")]

customer = CustomerProfile(id="CUST-123", tier="SILVER")

payment_info = PaymentInfo(method="CARD", bank_name="ICICI", card_type="CREDIT")
