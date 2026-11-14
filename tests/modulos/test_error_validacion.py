from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def test_error_validacion_es_subclase_de_value_error():
    assert issubclass(ErrorValidacion, ValueError)


def test_error_validacion_se_captura_con_except_value_error():
    try:
        raise ErrorValidacion("mensaje")
    except ValueError as error:
        assert isinstance(error, ErrorValidacion)
    else:
        assert False, "La excepción debía ser capturada"


def test_error_validacion_conserva_el_mensaje():
    error = ErrorValidacion("mensaje")

    assert str(error) == "mensaje"
