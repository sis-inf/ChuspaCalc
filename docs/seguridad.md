# Política de Seguridad

## Introducción

La seguridad es un aspecto importante del proyecto ChuspaCalc. Este documento describe el procedimiento para reportar vulnerabilidades de forma responsable, los tiempos de respuesta esperados y las políticas de divulgación utilizadas por el proyecto.

## Alcance de seguridad

Se consideran relevantes para la seguridad los siguientes componentes:

* Código fuente Python.
* Dependencias instaladas mediante pip.
* Entornos virtuales (venv).
* Archivos de configuración.
* Procesamiento y almacenamiento de datos.
* Integraciones con APIs externas.
* Gestión de credenciales y secretos.
* Flujos de autenticación y autorización.

Cualquier problema que afecte la confidencialidad, integridad o disponibilidad de la información entra dentro del alcance de esta política.

## Cómo reportar una vulnerabilidad

### Canal de reporte

Las vulnerabilidades deben reportarse de manera privada a los mantenedores del proyecto. No se recomienda abrir issues públicos para vulnerabilidades activas.

### Información requerida

El reporte debe incluir:

* Descripción detallada del problema.
* Pasos para reproducirlo.
* Impacto potencial.
* Versión afectada.
* Evidencias disponibles.
* Posible solución si se conoce.

### Tiempo de respuesta

* Confirmación de recepción: hasta 7 días.
* Evaluación inicial: hasta 14 días.
* Seguimiento periódico mientras se analiza el problema.

## Lo que NO es una vulnerabilidad

Los siguientes casos normalmente no se consideran vulnerabilidades:

* Errores tipográficos.
* Problemas visuales sin impacto de seguridad.
* Solicitudes de nuevas funcionalidades.
* Problemas ya corregidos.
* Configuraciones incorrectas del entorno local.
* Advertencias sin evidencia de explotación.

## Política de divulgación

### Proceso

1. Recepción del reporte.
2. Validación de la vulnerabilidad.
3. Desarrollo de una corrección.
4. Pruebas de la solución.
5. Publicación de la actualización.
6. Divulgación responsable.

### Tiempos de divulgación

La información técnica completa será publicada únicamente cuando exista una corrección disponible para los usuarios afectados.

## Buenas prácticas

* Mantener dependencias actualizadas.
* Utilizar entornos virtuales.
* Evitar almacenar contraseñas en el código fuente.
* Revisar periódicamente dependencias vulnerables.
* Aplicar el principio de mínimo privilegio.

## Contacto

Utilice los canales oficiales definidos por los mantenedores del proyecto para reportar problemas de seguridad.
