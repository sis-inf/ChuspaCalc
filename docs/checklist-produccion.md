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
- [ ] ¿Cada herramienta en el catálogo corresponde a un módulo real en `src/escuadra/modulos/`?
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
- [ ] ¿Si se publica en PyPI, se probó la instalación con `pip install escuadra` desde un entorno limpio?
- [ ] ¿Se generó un tag de versión en git correspondiente al release?

## 7. Validación final con usuarios reales

- [ ] ¿Al menos un estudiante o ayudante probó la aplicación antes del lanzamiento oficial?
- [ ] ¿Se recopiló feedback sobre la primera impresión de uso (Inicio Rápido)?
- [ ] ¿Existe un canal de soporte definido para reportar problemas durante el curso (issues de GitHub, grupo de Telegram, etc.)?

---

## Responsable de la verificación

| Ítem revisado | Responsable | Fecha | Resultado |
|---------------|-------------|-------|-----------|
|               |             |       |           |

---

## Notas finales

Si algún punto de este checklist no se cumple, **no se recomienda distribuir
la versión** hasta resolverlo, salvo que el equipo decida explícitamente
asumir el riesgo y documentar la excepción en este mismo archivo.