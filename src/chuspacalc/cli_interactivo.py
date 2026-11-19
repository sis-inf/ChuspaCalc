"""
Modo interactivo (REPL) para ChuspaCalc CLI.

Permite elegir una herramienta registrada, ingresar sus parámetros uno a
uno con validación de tipos y mostrar el resultado del cálculo.
"""

from typing import Any

from chuspacalc.registry import obtener_herramientas

# Descripción de una herramienta tal como la entrega el registry.
Herramienta = dict[str, Any]

# Valores que puede tomar un parámetro ingresado por el usuario.
ValorParametro = int | float | str


def ejecutar_interactivo() -> None:
    """
    Ejecuta el bucle interactivo (REPL) de la CLI.

    Muestra el menú de herramientas obtenidas del registry, solicita al
    usuario cada parámetro de la herramienta elegida, valida su tipo
    (``int``, ``float`` o ``str``) y muestra el resultado. El bucle se
    repite hasta que el usuario elige ``0`` o no hay herramientas
    registradas.

    Returns:
        None: La función no devuelve valor; interactúa por consola.

    Raises:
        Exception: Se propaga cualquier excepción que lance la función
            de la herramienta seleccionada al ejecutarse.
    """
    while True:
        print("\n=== ChuspaCalc MODO INTERACTIVO ===\n")

        # 1. Obtener herramientas desde el registry (OBLIGATORIO)
        herramientas: list[Herramienta] = obtener_herramientas()

        if not herramientas:
            print("No hay herramientas registradas.")
            return

        # 2. Mostrar lista dinámica
        for i, h in enumerate(herramientas, start=1):
            print(f"{i}. {h['nombre']}")

        print("0. Salir")

        # 3. Selección con validación
        try:
            opcion: int = int(input("\nSelecciona una herramienta: "))
        except ValueError:
            print("❌ Debes ingresar un número")
            continue

        if opcion == 0:
            print("Saliendo...")
            break

        if opcion < 1 or opcion > len(herramientas):
            print("❌ Opción inválida")
            continue

        herramienta: Herramienta = herramientas[opcion - 1]

        # 4. Pedir parámetros dinámicamente
        parametros: dict[str, ValorParametro] = {}

        print(f"\n--- {herramienta['nombre']} ---\n")

        for param in herramienta["parametros"]:
            while True:
                entrada: str = input(f"Ingrese {param['nombre']}: ")
                valor: ValorParametro

                # 5. VALIDACIÓN DE TIPOS
                if param["tipo"] == "int":
                    if not entrada.isdigit():
                        print("❌ Debe ser entero")
                        continue
                    valor = int(entrada)

                elif param["tipo"] == "float":
                    try:
                        valor = float(entrada)
                    except ValueError:
                        print("❌ Debe ser decimal")
                        continue

                elif param["tipo"] == "str":
                    if not entrada.strip():
                        print("❌ No puede estar vacío")
                        continue
                    valor = entrada

                else:
                    valor = entrada

                parametros[param["nombre"]] = valor
                break

        # 6. Ejecutar función real
        resultado = herramienta["funcion"](**parametros)

        # 7. Mostrar resultado
        print("\n=== RESULTADO ===\n")
        print(resultado)
