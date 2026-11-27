# 📜 Historial de Comandos CLI

Esta guía explica cómo utilizar el **historial de comandos** de ChuspaCalc, una funcionalidad que permite ver los comandos ejecutados anteriormente y repetirlos fácilmente.

---

## 🎯 ¿Qué es el historial de comandos?

El historial de comandos es un registro de todas las ejecuciones realizadas a través del CLI de ChuspaCalc. Permite:

- **Revisar** los comandos que ya ejecutaste.
- **Repetir** invocaciones anteriores sin tener que reescribirlas.
- **Auditar** el uso de las herramientas.
- **Aprender** de ejemplos previos.

---

## 🚀 Cómo ver el historial

### Desde la línea de comandos

```bash
ChuspaCalc historial
$ ChuspaCalc historial
ID   Fecha                 Comando
1    2026-06-28 10:30:15   viga --longitud 5.0 --carga 10.0
2    2026-06-28 10:35:22   tension --longitud 100 --corriente 20
3    2026-06-28 11:00:05   columna --altura 4.0 --seccion IPE200
4    2026-06-28 11:15:30   geometria --radio 2.5

ChuspaCalc repetir <ID>
ChuspaCalc historial --repetir
