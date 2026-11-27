# Changelog - Suite ChuspaCalc (Sprint 2 - v0.2)

**Período:** Del 25 de abril de 2026 al 21 de mayo de 2026.

## 🚀 Módulos y Features Agregados

### Core & UI
* **Arquitectura Base**: Implementación de Ventana Principal, menú dinámico, clase base `Herramienta` y `Registry` de descubrimiento dinámico.
* **Componentes**: Sistema de mensajes reutilizable, despachador de comandos (Command Dispatcher), widget base `WidgetHerramienta` y diálogo "Acerca de".
* **Entry Point**: Configuración del punto de entrada `app.py`.
* **Colaboradores**: @deeviX-41, @JuanPinaya, @brisa-ths, @baltazar-rodrigo, @unknowangxl

### Ingeniería y Ciencias
* **Sistemas**: Convertidor de color, Complemento a 2, conversión de bases numéricas y tablas de verdad.
* **Eléctrica**: Ley de Ohm, cálculo de potencia, divisores de tensión, circuitos serie/paralelo y calculadora de caída de tensión.
* **Civil**: Carga distribuida, deflexión de viga, área de sección, cálculo de momento flector y reacciones en vigas.
* **Geometría**: Conversión de coordenadas, trigonometría y cálculo de áreas.
* **Matemáticas**: Estadísticas (media, mediana, moda), conversor de unidades (longitud/temperatura), potencias, raíces, parser CSV y solucionador de ecuaciones lineales 2x2.
* **Colaboradores**: @YORDY-SG, @MariaPS0023, @Emerick99, @Vizalla, @melanyw777, @deeviX-41, @LinoSimon20, @CoraniLimber, @Alex-Calle-P, @jhaf7712, @NandoTheDreamer, @edsonhuanaco-commits

### IO y Configuración
* **Gestión de Datos**: Historial local, exportador JSON, configuración YAML y sistema de logging básico.
* **Colaboradores**: @Vizalla, @Nailea615, @MariaPS0023, @baltazar-rodrigo, @brisa-ths

---

## 📚 Documentación y Referencias
* **Guías Técnicas**: Catálogo de herramientas, guías de instalación, configuración, dependencias, testing y despliegue.
* **Arquitectura**: Registro de decisiones de arquitectura (ADR), glosario técnico, flujo de usuario, guía para agregar módulos y referencia CLI.
* **Soporte**: Documentación de ejemplos (`ejemplos.md`), preguntas frecuentes (FAQ) y limitaciones del sistema.
* **Colaboradores**: @CoraniLimber, @JuanPinaya, @Ka-rri, @DennisL505, @NICOLEROQUE0, @alizarbelen15, @deviamamani, @MariaPS0023, @Axl20-ai, @brayaDosantos, @unknowangxl, @Nailea615, @baltazar-rodrigo, @alis647, @edsonhuanaco-commits

---

## 🔧 Mantenimiento, Calidad y Pruebas
* **Infraestructura**: CI/CD (GitHub Actions), empaquetado con PyInstaller, Dependabot y configuración de `pyproject.toml`.
* **Calidad de Código**: Implementación de `pre-commit` hooks, `ruff`, `flake8` y `black`.
* **Testing**: Cobertura de pruebas con `pytest-cov`, fixtures para mock config y diseño de casos de prueba integrales.
* **Fixes**: Validaciones matemáticas, ajustes de interfaz (PySide6) y correcciones en el flujo de despacho.
* **Colaboradores**: @JuanPinaya, @NICOLEROQUE0, @Luza25-A, @Carlosx334, @baltazar-rodrigo, @brisa-ths, @Emerick99, @erwinsaul, @deeviX-41, @melanyw777, @claudiaatanacio-cloud, @unknowangxl, @YORDY-SG, @NandoTheDreamer, @Alex-Calle-P, @Vizalla

---

## 📊 Resumen Ejecutivo
* **Total Pull Requests Mergeados**: ~183
* **Contribuidores Únicos**: 44
* **Periodo**: 25 de abril de 2026 - 21 de mayo de 2026

## 🔄 Retrospectiva
* **Logros**: Cultura de documentación técnica sólida, alta modularidad mediante `ToolRegistry` y escalabilidad gracias a la automatización CI/CD.
* **Áreas de mejora**: Estandarización del ciclo de vida de PRs para reducir el volumen de solicitudes cerradas sin mergear.
