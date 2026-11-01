# Guía de Depuración

## Verificar codificación de un archivo Python sospechoso

```bash
file src/chuspacalc/modulos/civil/herramienta.py
python3 -c "with open('src/chuspacalc/modulos/civil/herramienta.py', 'rb') as f: print(f.read()[:200])"
```

Si el archivo tiene caracteres extraños, convertirlo a UTF-8:

```bash
iconv -f latin1 -t utf-8 archivo.py -o archivo_fixed.py
```

## Depurar un módulo de cálculo con pdb

Insertar en el código:

```python
import pdb; pdb.set_trace()
```

O usando la sintaxis moderna (Python 3.7+):

```python
breakpoint()
```

Ejecutar desde la raíz del proyecto:

```bash
python -m chuspacalc
```

Comandos útiles dentro de pdb:

| Comando | Descripción |
|---|---|
| n | Siguiente línea |
| s | Entrar a la función |
| c | Continuar ejecución |
| p variable | Imprimir valor de variable |
| l | Ver código alrededor |
| q | Salir |

## Depurar un widget PySide6 con QT_QPA_PLATFORM=offscreen

```bash
QT_QPA_PLATFORM=offscreen python -m pytest tests/ -v
```

Para un test específico de UI:

```bash
QT_QPA_PLATFORM=offscreen python -m pytest tests/ui/test_widget.py -v
```

Para correr la aplicación completa:

```bash
QT_QPA_PLATFORM=offscreen python -m chuspacalc
```

## Verificar imports rotos

```bash
python3 -c "import chuspacalc" 2>&1
python3 -c "from chuspacalc.modulos.civil import herramienta" 2>&1
```

## Activar trazas de depuración

```bash
CHUSPACALC_DEBUG=1 python -m chuspacalc
```

O en el código:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```
