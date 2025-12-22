def safe_call(func, a, b):
    try:
        return True, func(a, b), None
    except (ZeroDivisionError, TypeError, ValueError, IndexError, KeyError) as e:
        return False, None, type(e).__name__
