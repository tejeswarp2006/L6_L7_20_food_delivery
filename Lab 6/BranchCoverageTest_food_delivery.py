import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time


# delivery_charge branches
def test_delivery_charge_invalid_low():
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(0, 200, False)


def test_delivery_charge_invalid_high():
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(16, 200, False)


def test_delivery_charge_free():
    assert delivery_charge(5, 500, False) == 0


def test_delivery_charge_leq_3():
    assert delivery_charge(3, 100, False) == 20


def test_delivery_charge_leq_8():
    assert delivery_charge(8, 100, False) == 40


def test_delivery_charge_gt_8_rain():
    assert delivery_charge(12, 100, True) == 90


# apply_coupon branches
def test_apply_coupon_none():
    assert apply_coupon(300, None, True) == 300


def test_apply_coupon_invalid():
    with pytest.raises(ValueError, match="invalid coupon"):
        apply_coupon(300, "INVALID", True)


def test_apply_coupon_welcome_not_first():
    with pytest.raises(ValueError, match="coupon only for first order"):
        apply_coupon(300, "WELCOME", False)


def test_apply_coupon_welcome_first():
    assert apply_coupon(300, "WELCOME", True) == 200


def test_apply_coupon_under_min():
    assert apply_coupon(150, "SAVE50", True) == 150


def test_apply_coupon_valid_save50():
    assert apply_coupon(250, "SAVE50", False) == 200


# estimated_time branches
def test_estimated_time_base():
    assert estimated_time(10, False, False) == 55


def test_estimated_time_peak_only():
    assert estimated_time(10, True, False) == 65


def test_estimated_time_busy_only():
    assert estimated_time(10, False, True) == 70


def test_estimated_time_peak_and_busy():
    assert estimated_time(10, True, True) == 85