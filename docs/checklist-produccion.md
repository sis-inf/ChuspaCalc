# Checklist de Producción — Distribución de ChuspaCalc

## Introducción

Esta lista de verificación debe revisarse antes de distribuir una nueva
versión de ChuspaCalc para uso real en un curso. Su objetivo es asegurar
que la aplicación sea estable, completa y esté correctamente empaquetada
antes de llegar a los estudiantes.

---

## 1. Compatibilidad multiplataforma

- [ ] ¿Se verificó que la aplicación arranca correctamente en **Windows**?
- [ ] ¿Se verificó que la aplicación arranca correctamente en **Linux**?
- [ ] ¿Se verificó que la aplicación arranca correctamente en **macOS**?
- [ ] ¿El pipeline de CI multiplataforma pasa sin errores en las 3 plataformas?
- [ ] ¿Se probó la aplicación en una máquina limpia (sin dependencias de desarrollo preinstaladas)?

## 2. Ejecutables standalone

- [ ] ¿Se generaron los ejecutables standalone para cada plataforma (PyInstaller u otra herramienta)?
- [ ] ¿Se probó que cada ejecutable abre la ventana principal sin errores?
- [ ] ¿El tamaño del ejecutable es razonable (sin dependencias innecesarias empaquetadas)?
- [ ] ¿Se probaron los ejecutables en una máquina distinta a la que los generó?

## 3. Catálogo de herramientas

- [ ] ¿El archivo `docs/herramientas.md` lista todas las herramientas actualmente implementadas?
- [ ] ¿Cada herramienta en el catálogo corresponde a un módulo real en `src/chuspacalc/modulos/`?
- [ ] ¿Se eliminaron del catálogo las herramientas planificadas que aún no existen?
- [ ] ¿La descripción de cada herramienta es clara para un estudiante sin experiencia previa?

## 4. Suite de tests

- [ ] ¿Se ejecutó `pytest` completo y todos los tests pasan?
- [ ] ¿Se verificó la cobertura de tests de los módulos críticos (core, registry)?
- [ ] ¿Se ejecutó `ruff check .` sin errores?
- [ ] ¿Se corrieron los hooks de `pre-commit` sin fallos?

## 5. Documentación para el usuario final

- [ ] ¿`README.md` tiene instrucciones de instalación actualizadas?
- [ ] ¿`docs/instalacion.md` refleja los pasos reales de instalación con pip?
- [ ] ¿`docs/preguntas-frecuentes.md` cubre los problemas más comunes reportados por estudiantes en cursos anteriores?

## 6. Empaquetado y publicación

- [ ] ¿La versión en `pyproject.toml` fue incrementada correctamente?
- [ ] ¿`CHANGELOG.md` refleja los cambios de esta versión?
- [ ] ¿Si se publica en PyPI, se probó la instalación con `pip install chuspacalc` desde un entorno limpio?
- [ ] ¿Se generó un tag de versión en git correspondiente al release?

## 7. Validación final con usuarios reales

- [ ] ¿Al menos un estudiante o ayudante probó la aplicación antes del lanzamiento oficial?
- [ ] ¿Se recopiló feedback sobre la primera impresión de uso (Inicio Rápido)?
- [ ] ¿Existe un canal de soporte definido para reportar problemas durante el curso (issues de GitHub, grupo de Telegram, etc.)?

---

## Registro de evidencias para la aprobación del MVP v0.1.0

Cada verificación debe registrarse en la tabla de responsables, indicando:

- **Ítem revisado:** control específico del checklist.
- **Responsable:** persona que realizó o validó la verificación.
- **Fecha:** fecha de ejecución o revisión (AAAA-MM-DD).
- **Resultado:** Aprobado, Pendiente, No aprobado o Excepción aceptada.
- **Evidencia:** enlace o referencia verificable que respalde el resultado.

### Evidencias aceptadas

- **CI:** enlace a la ejecución específica de GitHub Actions, con su resultado.
- **Pruebas:** enlace al informe, registro o artefacto de pruebas ejecutadas.
- **Incidencias:** enlace al issue correspondiente, indicando su estado.
- **Validaciones manuales:** registro reproducible con entorno, versión, pasos y resultado.

No se debe marcar un control como aprobado sin evidencia verificable.
Una ejecución fallida o una incidencia abierta no constituye evidencia de aprobación.

### Verificaciones pendientes

Para cada control pendiente, registrar el motivo, responsable, acción necesaria,
fecha prevista de resolución y enlace a la incidencia o seguimiento, si existe.
Mantener el resultado como Pendiente hasta completar y verificar la revisión.

### Excepciones aceptadas

Documentar el control afectado, motivo, riesgo, impacto, responsable de aceptar
el riesgo, fecha de aceptación, medidas de mitigación y enlace a la decisión.
Una excepción aceptada no equivale a una verificación aprobada.

### Relación con los criterios de salida

Antes de aprobar el MVP v0.1.0, contrastar las evidencias con
`tests/plan/criterios-de-salida.md`: cobertura requerida, ausencia de bugs
Críticos o Altos abiertos, casos del sprint ejecutados, informe aprobado,
revisión de seguridad completada y documentación actualizada.

El umbral de cobertura debe definirse y verificarse antes de la aprobación.
No declarar aprobado el MVP mientras existan criterios sin evidencia
o pendientes sin una decisión formal documentada.

---

## Responsable de la verificación

| Ítem revisado | Responsable | Fecha | Resultado | Evidencia |
| --- | --- | --- | --- | --- |
|               |             |       |           |           |

---

## Notas finales

Si algún punto de este checklist no se cumple, **no se recomienda distribuir
la versión** hasta resolverlo, salvo que el equipo decida explícitamente
asumir el riesgo y documentar la excepción en este mismo archivo.