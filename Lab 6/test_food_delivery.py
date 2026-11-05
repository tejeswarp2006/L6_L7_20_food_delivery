import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time


# ---------------------------------------------------------------------------
# delivery_charge Tests
# ---------------------------------------------------------------------------
def test_delivery_charge_invalid_low():
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(0, 200, False)


def test_delivery_charge_invalid_high():
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(16, 200, False)


def test_delivery_charge_high_order():
    assert delivery_charge(5, 500, False) == 0


def test_delivery_charge_distance_leq_3():
    assert delivery_charge(2, 200, False) == 20


def test_delivery_charge_distance_leq_8():
    assert delivery_charge(5, 200, False) == 40


def test_delivery_charge_distance_gt_8():
    assert delivery_charge(10, 200, False) == 60


def test_delivery_charge_with_rain():
    assert delivery_charge(10, 200, True) == 90


# ---------------------------------------------------------------------------
# apply_coupon Tests
# ---------------------------------------------------------------------------
def test_apply_coupon_none():
    assert apply_coupon(300, None, False) == 300


def test_apply_coupon_invalid_code():
    with pytest.raises(ValueError, match="invalid coupon"):
        apply_coupon(300, "INVALID", False)


def test_apply_coupon_welcome_not_first_order():
    with pytest.raises(ValueError, match="coupon only for first order"):
        apply_coupon(300, "WELCOME", False)


def test_apply_coupon_welcome_first_order():
    assert apply_coupon(300, "WELCOME", True) == 200


def test_apply_coupon_order_below_200():
    assert apply_coupon(150, "SAVE50", True) == 150


def test_apply_coupon_save50():
    assert apply_coupon(300, "SAVE50", False) == 250


# ---------------------------------------------------------------------------
# estimated_time Tests
# ---------------------------------------------------------------------------
def test_estimated_time_normal():
    assert estimated_time(5, False, False) == 35


def test_estimated_time_peak_only():
    assert estimated_time(5, True, False) == 45


def test_estimated_time_busy_only():
    assert estimated_time(5, False, True) == 50


def test_estimated_time_peak_and_busy():
    assert estimated_time(5, True, True) == 55