from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from escuadra.core.carrera import Carrera
from escuadra.core.herramienta import Herramienta


class HerramientaKarnaugh(Herramienta):
    nombre = "Mapas de Karnaugh"

    carrera = Carrera.SISTEMAS

    descripcion = (
        "Genera mapas de Karnaugh y realiza simplificaciones "
        "básicas de expresiones booleanas."
    )

    def crear_widget(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)

        titulo = QLabel("Mapas de Karnaugh - Simplificación")
        layout.addWidget(titulo)

        fila = QHBoxLayout()
        fila.addWidget(QLabel("N° variables (2-4):"))
        spin_vars = QSpinBox()
        spin_vars.setRange(2, 4)
        spin_vars.setValue(3)
        fila.addWidget(spin_vars)

        fila.addWidget(QLabel("Minterms ej: 0,1,3:"))
        input_minterms = QLineEdit()
        input_minterms.setPlaceholderText("Ej: 0,1,2,5,6,7")
        fila.addWidget(input_minterms)
        layout.addLayout(fila)

        btn = QPushButton("Generar Mapa")
        layout.addWidget(btn)

        tabla = QTableWidget()
        layout.addWidget(tabla)

        resultado = QLabel("Expresión simplificada: -")
        layout.addWidget(resultado)

        def on_generar():
            try:
                num_vars = spin_vars.value()
                texto = input_minterms.text().strip()
                if not texto:
                    resultado.setText("Ingresa minterms ej: 0,1,3")
                    return

                minterms = [int(x.strip()) for x in texto.split(",") if x.strip()!= ""]
                total = 2 ** num_vars
                tabla_verdad = [0] * total
                for m in minterms:
                    if 0 <= m < total:
                        tabla_verdad[m] = 1

                mapa = generar_mapa_karnaugh(tabla_verdad, num_vars)
                expr = simplificar_expresion(mapa)

                # Visualizar mapa
                if isinstance(mapa, list) and mapa and isinstance(mapa[0], list):
                    tabla.setRowCount(len(mapa))
                    tabla.setColumnCount(len(mapa[0]))
                    for i, row in enumerate(mapa):
                        for j, val in enumerate(row):
                            tabla.setItem(i, j, QTableWidgetItem(str(val)))
                else:
                    tabla.setRowCount(1)
                    tabla.setColumnCount(len(mapa) if isinstance(mapa, list) else 1)
                    if isinstance(mapa, list):
                        for j, val in enumerate(mapa):
                            tabla.setItem(0, j, QTableWidgetItem(str(val)))
                    else:
                        tabla.setItem(0, 0, QTableWidgetItem(str(mapa)))

                resultado.setText(f"Expresión simplificada: {expr}")
            except Exception as e:
                resultado.setText(f"Error: {e}")

        btn.clicked.connect(on_generar)

        return widget