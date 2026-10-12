def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(100) == 212
