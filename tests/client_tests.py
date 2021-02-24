import client


def test_in_window():
    assert client.in_window(501) == 400
    assert client.in_window(-1) == 0
    assert client.in_window(45) == 45
    assert client.in_window(133) == 133
