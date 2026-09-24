"""
Modo interactivo (REPL) para Escuadra CLI
"""

from escuadra.registry import obtener_herramientas


def ejecutar_interactivo():
    while True:
        print("\n=== ESCUADRA MODO INTERACTIVO ===\n")

        # 1. Obtener herramientas desde el registry (OBLIGATORIO)
        herramientas = obtener_herramientas()

        if not herramientas:
            print("No hay herramientas registradas.")
            return

        # 2. Mostrar lista dinámica
        for i, h in enumerate(herramientas, start=1):
            print(f"{i}. {h['nombre']}")

        print("0. Salir")

        # 3. Selección con validación
        try:
            opcion = int(input("\nSelecciona una herramienta: "))
        except ValueError:
            print("❌ Debes ingresar un número")
            continue

        if opcion == 0:
            print("Saliendo...")
            break

        if opcion < 1 or opcion > len(herramientas):
            print("❌ Opción inválida")
            continue

        herramienta = herramientas[opcion - 1]

        # 4. Pedir parámetros dinámicamente
        parametros = {}

        print(f"\n--- {herramienta['nombre']} ---\n")

        for param in herramienta["parametros"]:
            while True:
                valor = input(f"Ingrese {param['nombre']}: ")

                # 5. VALIDACIÓN DE TIPOS
                if param["tipo"] == "int":
                    if not valor.isdigit():
                        print("❌ Debe ser entero")
                        continue
                    valor = int(valor)

                elif param["tipo"] == "float":
                    try:
                        valor = float(valor)
                    except ValueError:
                        print("❌ Debe ser decimal")
                        continue

                elif param["tipo"] == "str":
                    if not valor.strip():
                        print("❌ No puede estar vacío")
                        continue

                parametros[param["nombre"]] = valor
                break

        # 6. Ejecutar función real
        resultado = herramienta["funcion"](**parametros)

        # 7. Mostrar resultado
        print("\n=== RESULTADO ===\n")
        print(resultado)
