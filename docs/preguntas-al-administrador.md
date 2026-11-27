# Preguntas Frecuentes al Administrador

Este documento reúne las preguntas más frecuentes que recibe el administrador del repositorio **ChuspaCalc**. Su objetivo es ayudar a los contribuidores a resolver dudas comunes sin necesidad de esperar una respuesta directa del administrador.

Antes de realizar una consulta, revisa este documento, el archivo `README.md` y `CONTRIBUTING.md`. En muchos casos la respuesta ya se encuentra documentada.

---

# Fork y sincronización

## 1. ¿Cómo actualizo mi fork con los últimos cambios del repositorio principal?

Es recomendable sincronizar tu fork antes de comenzar cualquier trabajo nuevo. Esto te permite trabajar sobre la versión más reciente del proyecto y reduce la probabilidad de conflictos al momento de abrir un Pull Request.

Primero verifica que tengas configurado el repositorio principal como `upstream`:

```bash
git remote -v
```

Deberías ver algo similar a:

```text
origin    https://github.com/TU-USUARIO/ChuspaCalc.git (fetch)
origin    https://github.com/TU-USUARIO/ChuspaCalc.git (push)
upstream  https://github.com/sis-inf/ChuspaCalc.git (fetch)
upstream  https://github.com/sis-inf/ChuspaCalc.git (push)
```

Si `upstream` no existe, agrégalo:

```bash
git remote add upstream https://github.com/sis-inf/ChuspaCalc.git
```

Luego actualiza tu rama local `dev`:

```bash
git checkout dev
git pull upstream dev
```

Finalmente, si deseas mantener tu fork actualizado también en GitHub:

```bash
git push origin dev
```

Se recomienda realizar este procedimiento antes de crear una nueva rama para trabajar en una issue.

---

## 2. ¿Qué diferencia hay entre origin y upstream?

Cuando trabajas con el Forking Workflow existen normalmente dos repositorios remotos:

* **origin**: es tu fork personal.
* **upstream**: es el repositorio oficial del proyecto.

Por ejemplo:

```text
origin   -> https://github.com/TU-USUARIO/ChuspaCalc.git
upstream -> https://github.com/sis-inf/ChuspaCalc.git
```

Los cambios oficiales llegan desde `upstream`, mientras que tus cambios se envían a `origin`.

Comprender esta diferencia evita errores comunes, como intentar enviar cambios directamente al repositorio principal.

---

## 3. ¿Debo crear mi rama desde main o desde dev?

Siempre debes crear tu rama desde `dev`.

La rama `dev` contiene el trabajo de desarrollo más reciente y es la base sobre la que trabajan todos los contribuidores.

Ejemplo:

```bash
git checkout dev
git pull upstream dev
git checkout -b docs/preguntas-al-admin
```

Crear ramas desde `main` puede generar conflictos y complicar la integración posterior.

---

## 4. ¿Cada cuánto debo sincronizar mi fork?

No existe una frecuencia obligatoria, pero es recomendable hacerlo:

* Antes de comenzar una nueva issue.
* Antes de abrir un Pull Request.
* Si llevas varios días trabajando en una rama.
* Cuando observes que otros PR fueron integrados recientemente.

Mantener tu fork actualizado facilita la revisión y reduce conflictos.

---

## 5. ¿Qué hago si olvidé sincronizar antes de comenzar a trabajar?

No es necesario descartar tu trabajo.

Actualiza primero tu rama `dev`:

```bash
git checkout dev
git pull upstream dev
```

Luego vuelve a tu rama de trabajo e incorpora los cambios:

```bash
git checkout mi-rama
git merge dev
```

Si aparecen conflictos deberás resolverlos antes de continuar.

---

# Pull Requests

## 6. ¿Contra qué rama debo abrir mi Pull Request?

Todos los Pull Requests deben abrirse contra la rama `dev`.

Configuración correcta:

```text
Base repository: sis-inf/ChuspaCalc
Base branch: dev
Head repository: TU-USUARIO/ChuspaCalc
Compare branch: tu-rama
```

No abras Pull Requests contra `main` salvo que el administrador lo solicite explícitamente.

---

## 7. ¿Por qué fue rechazado mi Pull Request?

Un Pull Request puede ser rechazado por diferentes motivos:

* No resuelve completamente la issue asignada.
* Incluye cambios no relacionados.
* No sigue las convenciones del proyecto.
* Tiene conflictos de merge.
* El CI está fallando.
* No se realizaron los cambios solicitados durante la revisión.

Un rechazo no significa que el trabajo sea inútil; normalmente indica que necesita ajustes antes de ser aceptado.

---

## 8. ¿Qué significa que mi PR tiene conflictos de merge?

Significa que Git no puede combinar automáticamente tus cambios con los cambios más recientes de la rama `dev`.

Esto suele ocurrir cuando:

* Otro contribuidor modificó los mismos archivos.
* Tu rama estuvo mucho tiempo sin actualizarse.
* Se realizaron cambios estructurales en el proyecto.

Para resolverlo:

```bash
git checkout dev
git pull upstream dev

git checkout mi-rama
git merge dev
```

Git indicará qué archivos requieren atención.

---

## 9. ¿Puedo seguir agregando commits después de abrir un Pull Request?

Sí.

De hecho, es una práctica normal cuando el revisor solicita correcciones.

Realiza los cambios necesarios y luego:

```bash
git add .
git commit -m "fix: corregir observaciones de revisión"
git push origin mi-rama
```

GitHub actualizará automáticamente el Pull Request existente.

---

## 10. ¿Por qué se solicita que un PR tenga un único objetivo?

Porque facilita:

* La revisión del código.
* La identificación de errores.
* La realización de pruebas.
* El seguimiento del historial del proyecto.

Por ejemplo, si una issue trata sobre documentación, el PR no debería incluir cambios de interfaz gráfica o correcciones de módulos.

---

# CI/CD

## 11. ¿Qué es el CI?

CI significa Integración Continua.
| Check | Qué verifica |
|---|---|
| `ruff (lint)` | Estilo y calidad del código Python |
| `ruff (format)` | Formato consistente del código |
| `pytest` | Que todas las pruebas unitarias pasen |

Cada vez que envías cambios, GitHub ejecuta verificaciones automáticas para comprobar que el proyecto sigue funcionando correctamente.

Estas verificaciones ayudan a detectar errores antes de que lleguen a la rama principal de desarrollo.

Los checks de CI verifican automáticamente la calidad del código. Los fallos más frecuentes son:

- **Linter (ruff)**: el código no cumple las reglas de estilo.
- **Tests (pytest)**: alguna prueba falló.
- **Formato**: el código no está formateado correctamente.



## 12. ¿Por qué falló el CI de mi Pull Request?

Las causas más comunes son:

* Errores de sintaxis.
* Pruebas unitarias fallidas.
* Problemas de formato.
* Importaciones incorrectas.
* Archivos faltantes.
* Incumplimiento de reglas definidas por Ruff.

Debes revisar los detalles del workflow para identificar la causa exacta.

---

## 13. ¿Qué es Ruff y qué verifica?

Ruff es una herramienta de análisis estático de código.

Su función es detectar:

* Errores comunes.
* Código redundante.
* Problemas de formato.
* Importaciones incorrectas.
* Incumplimiento de estándares definidos por el proyecto.

Puedes ejecutarlo localmente con:

```bash
ruff check .
```

---

## 14. ¿Qué es Pytest y por qué puede hacer fallar el CI?

Pytest es el sistema de pruebas automatizadas utilizado por el proyecto.

Su objetivo es verificar que las funcionalidades continúan funcionando correctamente después de realizar cambios.

Para ejecutar las pruebas:

```bash
pytest
```

Si alguna prueba falla, deberás corregir el problema antes de abrir o actualizar tu Pull Request.

---

## 15. ¿Cómo puedo verificar localmente lo mismo que verifica el CI?

Antes de hacer push, ejecuta:

```bash
ruff check .
pytest
```

Esto permite detectar muchos errores antes de que GitHub los encuentre.

Realizar esta verificación reduce el tiempo de revisión y evita ciclos innecesarios de corrección.

---

# Issues

## 16. ¿Cómo me asignan una issue?

Primero debes comentar en la issue indicando tu interés en trabajar en ella.

Ejemplo:

```text
Me gustaría trabajar en esta issue.
```

Posteriormente el administrador o un colaborador correspondiente podrá asignártela.

La asignación ayuda a evitar que varias personas trabajen simultáneamente en la misma tarea.

---

## 17. ¿Puedo trabajar en una issue sin estar asignado?

No es recomendable.

Podrías invertir tiempo en una solución que otra persona ya está desarrollando.

Si una issue te interesa, comenta primero y espera confirmación.

---

## 18. ¿Puedo trabajar en más de una issue al mismo tiempo?

Sí, puedes tener un máximo de tres (3) issues asignados simultáneamente.

Esta restricción tiene como objetivo:

* Promover la finalización de tareas antes de asumir nuevas responsabilidades.
* Evitar la acumulación de issues sin progreso.
* Permitir una distribución más equitativa del trabajo entre los colaboradores.

No se realizarán excepciones a esta regla.

Una vez asignada una issue, dispondrás de un máximo de 72 horas (3 días) para completar el trabajo correspondiente y abrir el Pull Request asociado.

Cada issue debe tener:

* Su propia rama.
* Sus propios commits.
* Su propio Pull Request.

Ejemplo:

```text
docs/preguntas-al-admin
fix/error-conversion-binaria
test/pruebas-modulo-viga
```

Mantener el trabajo separado facilita la revisión y evita mezclar cambios.

---

## 19. ¿Qué hago si una issue parece abandonada?

Si observas que una issue asignada lleva mucho tiempo sin actividad:

1. Revisa los comentarios recientes.
2. Consulta respetuosamente si sigue en desarrollo.
3. Espera la decisión del administrador.

La reasignación de una issue depende de la situación particular de cada caso.

---

## 20. ¿Cómo debo referenciar una issue en mis commits?

Todos los commits principales deben incluir la referencia correspondiente cuando sea posible.

Ejemplo:

```bash
git commit -m "docs: actualizar como agregar modulo - Closes #67"
```

Cuando el Pull Request sea aceptado, GitHub cerrará automáticamente la issue asociada.

---

## 21. ¿Qué hago si necesito ayuda durante el desarrollo?

Antes de contactar al administrador:

1. Lee el README del proyecto.
2. Revisa CONTRIBUTING.md.
3. Consulta este documento.
4. Revisa comentarios anteriores en la issue.
5. Busca si otro Pull Request resolvió un problema similar.

Si después de estas verificaciones tu duda continúa, puedes comentar en la issue o en tu Pull Request proporcionando toda la información posible para facilitar la ayuda.
