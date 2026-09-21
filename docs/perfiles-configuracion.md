# ⚙️ Configuración de la aplicación

Este documento describe el estado actual del sistema de configuración en Escuadra.

---

## 📌 Estado actual

Actualmente, la aplicación cuenta con un sistema de configuración básico pero funcional. 

El módulo `src/escuadra/config/loader.py` se encarga de **cargar y guardar** un único archivo de configuración en formato YAML.

---

## 🗂️ Archivo de configuración

La configuración se almacena en un archivo llamado `config.yaml` ubicado en el directorio de configuración del usuario:

| Sistema operativo | Ruta del archivo |
|-------------------|------------------|
| **Windows** | `%APPDATA%/Escuadra/config.yaml` |
| **Linux** | `~/.config/escuadra/config.yaml` |
| **macOS** | `~/Library/Application Support/Escuadra/config.yaml` |

---

## 🧩 Parámetros gestionados

Actualmente, `loader.py` solo maneja **un único parámetro** dentro de `config.yaml`:

| Clave | Tipo | Descripción | Valor por defecto |
|-------|------|-------------|-------------------|
| `font_scale` | `float` | Escala global del tamaño de la fuente en la interfaz. | `1.0` |

### Ejemplo de `config.yaml`

```yaml
font_scale: 1.2