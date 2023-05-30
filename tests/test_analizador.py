import json

import pytest

from pytest_lazyfixture import lazy_fixture

from analizador.modelo.analizador import ReglaPalabrasMasUsadas, ReglaConteoPalabras, ReglaTiempoLectura, Analizador


@pytest.fixture(scope="session")
def text_1():
    with open("fixtures/testtext_1.txt", "r", encoding='utf8') as file:
        content = file.read()
    return content


@pytest.fixture(scope="session")
def text_2():
    with open("fixtures/testtext_2.txt", "r", encoding='utf8') as file:
        content = file.read()
    return content


@pytest.fixture(scope="session")
def expected_words_1():
    with open("fixtures/expectedwords_1.json", "r", encoding='utf8') as file:
        words = json.load(file)

    return words


@pytest.fixture(scope="session")
def expected_words_2():
    with open("fixtures/expectedwords_2.json", "r", encoding='utf8') as file:
        words = json.load(file)

    return words


@pytest.fixture
def regla_palabras_ordenadas():
    return ReglaPalabrasMasUsadas()


@pytest.fixture
def regla_conteo_palabras():
    return ReglaConteoPalabras()


@pytest.fixture
def regla_tiempo_lectura():
    return ReglaTiempoLectura()


@pytest.fixture
def analizador():
    return Analizador()


@pytest.mark.parametrize("text, expected", [
    (lazy_fixture("text_1"), {"de", "y", "se", "un", "en", "la", "a", "sus", "javier", "que"}),
    (lazy_fixture("text_2"), {"este", "usted", "hola", "es", "un", "ejemplo", "para", "que", "practique", "puede"}),
    ("", set()),
    ("a", {"a"})
])
def test_regla_palabras_mas_usadas_analiza_texto(regla_palabras_ordenadas, text, expected):
    result = regla_palabras_ordenadas.analizar(text)
    assert set(result) == expected


@pytest.mark.parametrize("text, expected", [
    (lazy_fixture("text_1"), 281),
    (lazy_fixture("text_2"), 21),
    ("a", 1),
    ("", 0)
])
def test_regla_conteo_palabras_analiza_texto(regla_conteo_palabras, text, expected):
    result = regla_conteo_palabras.analizar(text)
    assert result == expected


@pytest.mark.parametrize("text, expected", [
    (lazy_fixture("text_1"), (1, 10)),
    (lazy_fixture("text_2"), (0, 5)),
    ("a", (0, 0)),
    ("", (0, 0))
])
def test_regla_tiempo_lectura_analiza_texto(regla_tiempo_lectura, text, expected):
    result = regla_tiempo_lectura.analizar(text)
    assert result == expected


def test_analizador_tiene_tres_reglas_despues_de_inicializado(analizador):
    assert len(analizador.reglas) == 3


@pytest.mark.parametrize("text, expected_words", [
    (lazy_fixture("text_1"), lazy_fixture("expected_words_1")),
    (lazy_fixture("text_2"), lazy_fixture("expected_words_2")),
    ("", []),
    ("a", ["a"])
])
def test_regla_analisis_separa_palabras(regla_conteo_palabras, text, expected_words):
    result = regla_conteo_palabras._separar_palabras(text)
    assert result == expected_words


@pytest.mark.parametrize("rule, expected_name", [
    (lazy_fixture("regla_palabras_ordenadas"), "palabras_ordenadas"),
    (lazy_fixture("regla_conteo_palabras"), "conteo_palabras"),
    (lazy_fixture("regla_tiempo_lectura"), "tiempo_lectura"),
])
def test_nombre_regla_es_correcto(rule, expected_name):
    assert rule.nombre == expected_name


@pytest.mark.parametrize("text, expected", [
    (lazy_fixture("text_1"), {
        "palabras_ordenadas": ["de", "y", "se", "un", "en", "la", "a", "sus", "javier", "que"],
        "conteo_palabras": 281,
        "tiempo_lectura": (1, 10)
    }),
    (lazy_fixture("text_2"), {
        "palabras_ordenadas": ["este", "usted", "hola", "es", "un", "ejemplo", "para", "que", "practique", "puede"],
        "conteo_palabras": 21,
        "tiempo_lectura": (0, 5)
    }),
    ("", {"palabras_ordenadas": [], "conteo_palabras": 0, "tiempo_lectura": (0, 0)}),
    ("a", {"palabras_ordenadas": ["a"], "conteo_palabras": 1, "tiempo_lectura": (0, 0)}),
])
def test_analizador_analiza_texto(analizador, text, expected):
    result = analizador.procesar(text)
    assert set(result["palabras_ordenadas"]) == set(expected["palabras_ordenadas"]) \
        and result["conteo_palabras"] == expected["conteo_palabras"] \
        and result["tiempo_lectura"] == expected["tiempo_lectura"]