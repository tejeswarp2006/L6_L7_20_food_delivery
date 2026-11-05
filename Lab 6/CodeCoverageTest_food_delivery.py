import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time


def test_delivery_charge_out_of_range():
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(0, 200, False)


def test_delivery_charge_high_order():
    assert delivery_charge(5, 500, False) == 0


def test_delivery_charge_short_distance():
    assert delivery_charge(2, 200, False) == 20


def test_delivery_charge_medium_distance():
    assert delivery_charge(5, 200, False) == 40


def test_delivery_charge_long_distance_with_rain():
    assert delivery_charge(10, 200, True) == 90


def test_apply_coupon_none():
    assert apply_coupon(300, None, False) == 300


def test_apply_coupon_invalid():
    with pytest.raises(ValueError, match="invalid coupon"):
        apply_coupon(300, "INVALID", False)


def test_apply_coupon_welcome_not_first():
    with pytest.raises(ValueError, match="coupon only for first order"):
        apply_coupon(300, "WELCOME", False)


def test_apply_coupon_under_minimum():
    assert apply_coupon(150, "SAVE50", True) == 150


def test_apply_coupon_valid():
    assert apply_coupon(300, "SAVE50", False) == 250


def test_estimated_time_all_flags():
    assert estimated_time(5, True, True) == 65