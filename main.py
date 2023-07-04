def test_a():
    print("testing a")


def test_b():
    print("testing b")


def test_c():
    print("testing c")
    test_a()
    test_b()


if __name__ == '__main__':
    test_c()
