from solution import suma_mod


def test_suma_mod_basica():
    assert suma_mod(7, 5, 4) == 0


def test_suma_mod_residuo_dos():
    assert suma_mod(8, 9, 5) == 2


def test_suma_mod_residuo_seis():
    assert suma_mod(10, 3, 7) == 6


def test_suma_mod_numeros_grandes():
    assert suma_mod(100, 200, 13) == 1
