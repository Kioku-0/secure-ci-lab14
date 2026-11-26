def sum_integers(a, b):
    """Складывает только два целых числа."""
    if not isinstance(a, int) or isinstance(a, bool):
        raise ValueError("a must be an integer")
    if not isinstance(b, int) or isinstance(b, bool):
        raise ValueError("b must be an integer")
    return a + b
