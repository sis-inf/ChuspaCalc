# 🖥️ Modo Interactivo (REPL) del CLI

Esta guía explica cómo utilizar el **modo interactivo** (REPL) de ChuspaCalc, una funcionalidad que permite ejecutar cálculos y herramientas desde una consola interactiva.

---

## 🎯 ¿Qué es el modo interactivo?

El modo interactivo (REPL - Read-Eval-Print Loop) es una **consola interactiva** donde podés:

- Ejecutar herramientas de cálculo.
- Realizar pruebas rápidas.
- Experimentar con las funcionalidades.
- Ver resultados en tiempo real.

---

## 🚀 Cómo iniciar el modo interactivo

### Desde la línea de comandos

```bash
ChuspaCalc interactiva

$ ChuspaCalc interactiva
🖥️  Modo interactivo de ChuspaCalc

ChuspaCalc> listar
- viga      - Cálculo de reacciones en vigas
- tension   - Cálculo de caída de tensión

ChuspaCalc> usar viga
📐 Ingresa los parámetros de la viga:
  longitud (m) > 5.0
  carga (kN) > 10.0
  material > acero

Resultado:
  Momento flector: 12.50 kN·m
  Cortante máximo: 5.00 kN

ChuspaCalc> salir
   ¡hasta luego!
