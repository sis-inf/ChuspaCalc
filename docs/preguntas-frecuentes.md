# Preguntas Frecuentes — Suite ChuspaCalc

## Que es ChuspaCalc?

ChuspaCalc es un proyecto que integra diferentes herramientas diseñadas para apoyar el trabajo en diversas áreas de la ingeniería. Permite a los usuarios aplicar conceptos teóricos en situaciones reales mediante soluciones digitales, centralizando herramientas que normalmente estan dispersas.

## Para quien esta dirigido ChuspaCalc?

ChuspaCalc esta dirigido a estudiantes de ingenieria, docentes y profesionales que necesiten herramientas de cálculo o análisis en su trabajo diario.

## Que herramientas incluye la suite?

La suite incluye las siguientes herramientas:

- **Calculadora de Vigas:** cálculo de momentos flectores y fuerzas cortantes en estructuras simples.
- **Conversor de Unidades:** transformación de medidas técnicas (presión, fuerza, longitud) al Sistema Internacional (SI).
- **Análisis Estadístico:** procesamiento de datos experimentales y cálculo de desviaciones estándar.
- **Diseño de Mezclas:** cálculo de proporciones para materiales de construcción según normativas.

## Como se instala ChuspaCalc?

Sigue estos pasos para instalar el proyecto:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/sis-inf/ChuspaCalc.git
   cd ChuspaCalc
   ```
2. Instala las dependencias:
   ```bash
   npm install
   ```
3. Ejecuta el proyecto:
   ```bash
   npm start
   ```

## Que plataformas soporta ChuspaCalc?

ChuspaCalc funciona en cualquier plataforma que soporte Node.js, incluyendo Windows, macOS y Linux.

## Como puedo contribuir al proyecto?

Para contribuir a ChuspaCalc se sigue el metodo Forking Workflow:

1. Haz un fork del repositorio.
2. Crea una rama con el nombre sugerido en el issue correspondiente.
3. Realiza tus cambios siguiendo los estandares de codigo del proyecto.
4. Abre un Pull Request con el titulo del issue y completa la descripcion del PR.

Para mas detalles, consulta el archivo `CONTRIBUTING.md` del repositorio.

## Que areas de ingenieria cubre ChuspaCalc?

El proyecto contempla herramientas para distintas ramas de ingenieria: Sistemas, Informatica, Industrial, Civil, Electronica y Mecanica.

## Como sincronizo mi fork con los ultimos cambios del upstream?

Para actualizar tu fork con los cambios mas recientes del repositorio principal:

```bash
 git checkout dev
 git pull upstream dev
```

Despues puedes subir los cambios actualizados a tu fork:

```bash
 git push origin dev
```

## Puedo trabajar en mas de una issue simultaneamente?

Si. Se recomienda crear una rama independiente para cada issue.

Ejemplo:

```bash
 git checkout -b fix/error-login
 git checkout -b docs/actualizar-faq
```

Cada issue debe tener su propia rama y su propio Pull Request.

## Que pasa si mi Pull Request tiene conflictos de merge?

Debes actualizar tu rama con los cambios mas recientes de `dev` y resolver los conflictos manualmente.

```bash
 git checkout dev
 git pull upstream dev
 git checkout mi-rama
 git merge dev
```

Luego corrige los conflictos y realiza un nuevo commit.

## Por que fue cerrado mi Pull Request sin merge?

Un Pull Request puede cerrarse sin merge por diferentes motivos:

* No cumple los criterios del issue.
* Tiene conflictos sin resolver.
* Modifica archivos no relacionados.
* Duplica trabajo ya realizado por otro contribuidor.

Revisa los comentarios de los revisores para conocer el motivo exacto.

## Como se si mi codigo pasa el CI antes de abrir el Pull Request?

Puedes ejecutar las pruebas localmente antes de subir los cambios.

```bash
 pytest
```

Tambien puedes ejecutar las herramientas de calidad definidas por el proyecto.

```bash
 ruff check .
```

## Como verifico que estoy trabajando sobre mi fork?

Puedes revisar los repositorios remotos configurados:

```bash
 git remote -v
```

Debes tener configurados `origin` para tu fork y `upstream` para el repositorio principal.

## Como creo una nueva rama para trabajar en una issue?

Primero sincroniza la rama `dev` y luego crea una rama nueva:

```bash
 git checkout dev
 git pull upstream dev
 git checkout -b tipo/descripcion-corta
```

Ejemplo:

```bash
 git checkout -b docs/faq-workflow-forks
```

## Que hago despues de terminar una contribucion?

Debes agregar los cambios, crear un commit y subir la rama a tu fork.

```bash
 git add .
 git commit -m "docs: actualizar preguntas frecuentes - Closes #362"
 git push origin fix-docs/faq-workflow-forks
```
Luego abre un Pull Request hacia la rama `dev` del repositorio principal.
