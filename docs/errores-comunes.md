# Errores Comunes al Contribuir

## Introducción

Este documento recopila errores frecuentes encontrados por estudiantes al trabajar con ChuspaCalc y sus respectivas soluciones.

---

## 1. ModuleNotFoundError al importar el paquete del proyecto

### Síntoma

```bash
ModuleNotFoundError: No module named '<nombre_del_paquete>'
```

### Causa

El entorno virtual no está activado o las dependencias no están instaladas.

### Solución

```bash
pip install -r requirements.txt
```

---

## 2. pytest no encuentra pruebas

### Síntoma

```bash
collected 0 items
```

### Causa

Las pruebas no están ubicadas en el directorio correcto.

### Solución

```bash
pytest
```

Verificar que los archivos estén dentro de `tests/`.

---

## 3. Error de pre-commit

### Síntoma

```bash
pre-commit failed
```

### Causa

No se instalaron los hooks.

### Solución

```bash
pre-commit install
```

---

## 4. ImportError por archivo faltante

### Síntoma

```bash
ImportError
```

### Causa

Falta un archivo `__init__.py`.

### Solución

Agregar el archivo faltante dentro del paquete.

---

## 5. Error al instalar dependencias

### Síntoma

```bash
Could not find a version that satisfies the requirement
```

### Causa

Versión incompatible de Python.

### Solución

```bash
python --version
```

Verificar la versión requerida por el proyecto.

---

## 6. Error al ejecutar pytest

### Síntoma

```bash
command not found: pytest
```

### Causa

pytest no está instalado.

### Solución

```bash
pip install pytest
```

---

## 7. Error al hacer commit

### Síntoma

```bash
nothing to commit
```

### Causa

Los cambios no fueron guardados.

### Solución

Guardar los archivos antes de ejecutar:

```bash
git add .
git commit -m "docs: actualización"
```

---

## 8. Error de rama incorrecta

### Síntoma

Pull Request enviado desde una rama equivocada.

### Causa

Se trabajó sobre main.

### Solución

Crear una rama nueva desde dev.

```bash
git checkout dev
git checkout -b nueva-rama
```

---

## 9. Error de conflictos al fusionar

### Síntoma

```bash
Merge conflict
```

### Causa

Cambios incompatibles entre ramas.

### Solución

Actualizar la rama y resolver conflictos manualmente.

```bash
git pull
```

---

## 10. Error de permisos en GitHub

### Síntoma

```bash
Permission denied
```

### Causa

No existe acceso de escritura al repositorio principal.

### Solución

Trabajar mediante fork y Pull Request.
