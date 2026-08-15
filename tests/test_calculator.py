"""使用 TDD 演示计算器的五个行为测试。"""


def test_adds_two_numbers():
    from calculator import add

    assert add(2, 3) == 5


def test_subtracts_two_numbers():
    from calculator import subtract

    assert subtract(7, 4) == 3


def test_multiplies_two_numbers():
    from calculator import multiply

    assert multiply(3, 4) == 12


def test_divides_two_numbers():
    from calculator import divide

    assert divide(8, 2) == 4


def test_raises_number_to_power():
    from calculator import power

    # 故意写错期望值，用于练习 pytest 失败和后续 Git/CI 排错。
    assert power(2, 3) == 10,"故意写错的测试用例"
