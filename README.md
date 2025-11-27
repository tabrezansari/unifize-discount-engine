# Unifize Discount Engine

<p align="center">
  <img src="https://img.shields.io/github/actions/workflow/status/tabrezansari/unifize-discount-engine/tests.yaml?branch=main" alt="CI Status">
  <img src="https://img.shields.io/badge/python-3.11-blue" alt="Python Version">
  <img src="https://img.shields.io/github/v/release/tabrezansari/unifize-discount-engine" alt="Latest Release">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
</p>

A modular, extensible discount calculation engine for a fashion e-commerce platform.
Implements brand discounts, category deals, coupon validation, and bank offers using a clean **Rule Pipeline** based on the **Strategy Pattern**.

---

## 🔥 Features

- Pluggable discount rules (Strategy Pattern)
- Rule pipeline: **Brand → Category → Coupon → Bank**
- Coupon validation:
  - Brand exclusions
  - Category restrictions
  - Customer tier requirements
- Clean separation of:
  - Rule logic
  - Service orchestration
  - Validation
- Fully async-ready architecture
- Pytest test suite
- Example runner included (`examples/run_example.py`)
- Architecture diagram included

---

## 📦 Installation & Environment Setup

### Clone the repository

```bash
git clone https://github.com/tabrezansari/unifize-discount-engine.git
cd unifize-discount-engine
```

### Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate     # Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Verify installation

```bash
pytest -q
```

(Optional) Add project to PYTHONPATH:

```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
```

---

## ▶️ Running the Example

```bash
python -m examples.run_example
```

Expected output:

```
Original Price: 1000
Final Price: 486
Applied Discounts: {...}
```

---

## 🧪 Running Tests

```bash
python -m pytest -q
```

---

## 🧩 Project Structure

```
discount_engine/
    models/                 → Core data models
    services/
        rules/              → Brand, Category, Coupon, Bank rule implementations
        validators/         → Validation logic
        discount_service.py → Orchestrates rule pipeline
examples/                   → Example runner
tests/                      → Pytest suite
assets/                     → Architecture diagram(s)
README.md
requirements.txt
```

---

## 🧠 Architecture Overview

### Strategy Pattern (Rule Modules)

Each discount type is its own isolated class:

- BrandDiscountRule
- CategoryDiscountRule
- CouponDiscountRule
- BankDiscountRule

All inherit from a shared base:

```python
class DiscountRule(ABC):
    async def apply(self, cart_items, customer, current_price, payment_info) -> Decimal:
        ...
```

### Rule Pipeline (DiscountService)

1. Brand discount
2. Category discount
3. Coupon validation & application
4. Bank offer

Each rule returns:

```
Decimal discount_amount
```

---

## 📊 Architecture Diagram (Figma)

![Architecture](assets/discount_engine_diagram.png)

---

## 📝 Assumptions

- Discounts come from assignment dummy data
- Single active coupon at a time
- Happy-path required only
- Async structure future-proofs external API integrations
- No conflict resolver for overlapping discounts

---

## 🧠 Technical Decisions

- Strategy Pattern → modular rules
- Pipeline Architecture → predictable order
- Validation Layer → early invalidation
- Async-first → scalable for integrations
- Separation of concerns → modular testing & maintainability

---

## 🚀 Future Enhancements

- Config-driven discount engine
- Multi-coupon stacking
- Buy X Get Y
- Tiered pricing engine
- AB testing

---

## 🔐 Branch Protection Rules

- PR required for develop/main
- CI must pass before merge
- Pre-commit enforced formatting

---

## 👤 Author

**Tabrez Ansari**
Engineering Manager Candidate – Unifize
GitHub: https://github.com/tabrezansari
