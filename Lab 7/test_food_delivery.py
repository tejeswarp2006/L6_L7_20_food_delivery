from hypothesis import given, strategies as st, settings
from food_delivery import parse_order, delivery_eta, coupon_discount

@settings(max_examples=200, deadline=None)
@given(st.text() | st.none())
def test_parse_order_no_crash(s):
    try:
        result = parse_order(s)
    except ValueError:
        return  
    except Exception as e:
        assert False, f"parse_order raised unexpected {type(e).__name__} for input {s!r}: {e}"
    assert isinstance(result, dict)

@settings(max_examples=200, deadline=None)
@given(st.text() | st.none())
def test_delivery_eta_no_crash(s):
    try:
        result = delivery_eta(s)
    except ValueError:
        return
    except Exception as e:
        assert False, f"delivery_eta raised unexpected {type(e).__name__} for input {s!r}: {e}"
    assert isinstance(result, int)

@settings(max_examples=200, deadline=None)
@given(st.text() | st.none())
def test_coupon_discount_no_crash(s):
    try:
        result = coupon_discount(s)
    except ValueError:
        return
    except Exception as e:
        assert False, f"coupon_discount raised unexpected {type(e).__name__} for input {s!r}: {e}"
    assert isinstance(result, int)