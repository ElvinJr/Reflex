# Documentación del Proyecto: Primera Página Web con Reflex

## Introducción
Este proyecto representa el primer acercamiento al desarrollo web utilizando **Reflex**, un framework de Python que permite construir aplicaciones web full-stack sin necesidad de escribir Javascript explícitamente. Se utilizó **Poetry** para garantizar un manejo limpio y reproducible de las dependencias.

## Pasos de Instalación y Desarrollo
1. **Configuración de Carpeta**: Se creó la carpeta `pagina` para organizar el código.
2. **Entorno con Poetry**: Se inicializó el proyecto con `poetry init` y se agregó `reflex`.
3. **Inicialización de Reflex**: Se configuró la estructura base mediante `poetry run reflex init`.
4. **Desarrollo Frontend y Lógica**: Se implementó el estado de la aplicación en Python para manejar la lógica de la ruleta y el diseño en colores negros.

## Problemas Encontrados y Soluciones
- **Problema**: La inicialización de Reflex fallaba al intentar instalar Bun automáticamente debido a políticas de ejecución de PowerShell.
- **Solución**: Se instaló **Node.js LTS** de forma manual y se forzó a Reflex a utilizar `npm` mediante la variable de entorno `REFLEX_USE_NPM=True`. Esto permitió una instalación exitosa sin conflictos de permisos.

## Resultados Obtenidos
Se logró una aplicación funcional que:
- Muestra una interfaz estética y sencilla.
- Permite la interacción del usuario mediante selección de radio y botones.
- Procesa la lógica de victoria/derrota de forma instantánea en el servidor y la refleja en el cliente.

## Conclusiones Personales sobre Reflex
Reflex es una herramienta sumamente potente para desarrolladores de Python. Su capacidad para manejar el estado del frontend directamente desde clases de Python simplifica enormemente el flujo de trabajo. Aunque requiere una configuración inicial de dependencias externas (Node/Bun), una vez listo, el desarrollo es ágil y eficiente.
