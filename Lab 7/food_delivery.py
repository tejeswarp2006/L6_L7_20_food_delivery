import math

def parse_order(items_csv):
    if not isinstance(items_csv, str) or not items_csv.strip():
        raise ValueError("Order must be a non-empty string like 'pizza:2,burger:1'")

    order = {}
    for item in items_csv.split(','):
        item = item.strip()
        if not item:
            raise ValueError("Empty item entry in order")

        parts = item.split(':')
        if len(parts) != 2:
            raise ValueError(f"Malformed item entry {item!r} (expected name:qty)")

        name, qty_str = parts[0].strip(), parts[1].strip()
        if not name:
            raise ValueError("Item name cannot be empty")

        try:
            qty = int(qty_str)
        except ValueError:
            raise ValueError(f"Invalid quantity {qty_str!r} for item {name!r}")

        if qty <= 0:
            raise ValueError(f"Quantity must be positive, got {qty} for {name!r}")

        order[name] = qty

    return order


def delivery_eta(distance_km):
    if distance_km is None:
        raise ValueError("Distance is required")

    try:
        distance = float(distance_km)
    except (TypeError, ValueError):
        raise ValueError(f"Invalid distance: {distance_km!r}")

    if math.isnan(distance) or math.isinf(distance):
        raise ValueError("Distance must be a finite number")
    if distance < 0:
        raise ValueError("Distance cannot be negative")

    return int(15 + distance * 4)


def coupon_discount(code):
    if not isinstance(code, str) or not code.strip():
        raise ValueError("Coupon code must be a non-empty string")

    upper = code.strip().upper()
    parts = upper.split('SAVE')

    if len(parts) != 2 or not parts[1]:
        raise ValueError(f"Malformed coupon {code!r} (expected format like SAVE50)")

    try:
        discount = int(parts[1])
    except ValueError:
        raise ValueError(f"Discount amount in {code!r} is not a number")

    if discount < 0:
        raise ValueError("Discount cannot be negative")

    return discount


def main():
    print("==== Running parse_order ====")
    user_input = input("Enter items as name:qty CSV (e.g. pizza:2,burger:1): ")
    try:
        print("Order:", parse_order(user_input))
    except ValueError as e:
        print("Invalid order:", e)

    print("\n==== Running delivery_eta ====")
    user_input = input("Enter distance in km (e.g. 4.5): ")
    try:
        print("ETA in Minutes:", delivery_eta(user_input))
    except ValueError as e:
        print("Invalid distance:", e)

    print("\n==== Running coupon_discount ====")
    user_input = input("Enter a coupon code (e.g. SAVE50): ")
    try:
        print("Discount:", coupon_discount(user_input))
    except ValueError as e:
        print("Invalid coupon:", e)

if __name__ == "__main__":
    main()