# Libraries
import slash
import os


def suma():
    a = 3
    b = 4
    c = a + b
    return c


@slash.skipped("No reason")
def test_1():  # Los metodos que ejecutara slash por convencion deben iniciar con la palabra "test_"

    slash.logger.notice("Inicio del test_1")
    valor = suma()
    assert (
        valor == 7
    )  # "Asert" Busca que la condicion se cumpla, notificando errores

    slash.logger.notice("Fin del test_1")


@slash.skipped("No reason")
def test_2():
    print(suma())


# @slash.skipped("No reason")
def test_3():  # Tipos de logs que se pueden escribir
    """
    Este test muestra los tipos de logs que se pueden mostrar en slash
    """
    slash.logger.notice("Log de tipo notice")
    slash.logger.info("Log de tipo Info")
    slash.logger.debug("Log de tipo debug")
    slash.logger.warn("Log de tipo warning")
    slash.logger.error("Log de tipo error")
    slash.logger.critical("Log de tipo critical")


# --------------------------------COMANDOS DE EJECUCION EN SLASH-------------------------------------------
# slash run .\1-slash-introduction.py -vvv
# slash run .\1-slash-introduction.py -vvv -l C:\Users\JROSAS26\Documents\Investigation-projects\Slash-and-fixtures\Session
# slash list
# slash --help (slash -h)

#!------------------------------------------------------------------------------------------------------


@slash.skipped("No reason")
@slash.parametrize("x", [1, 4, 3])
def test_something(x):
    """La parametrizacion sirve para darle diferentes valores a X y ejecutar asi diferentes pruebas

    Args:
        x (_int_): _numero de referencia_
    """
    slash.logger.notice("Starting test")
    x = x * 4
    print(f"El valor de x es {x}")
    assert x >= 9
    slash.logger.notice("End test")
