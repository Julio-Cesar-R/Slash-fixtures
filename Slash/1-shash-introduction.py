import slash


def suma(a, b):
    return a + b


def test_1():
    slash.logger.debug("Prueba numero 1")


def test_2():
    slash.logger.debug("Prueba numero 2")
    res = suma(5, 5)
    assert res == 10
    print(res)


def test_3():
    slash.logger.debug("Prueba numero 3")


ejec = test_2()
