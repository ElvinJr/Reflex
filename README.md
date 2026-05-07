# Primera página web con Reflex

## Descripción
Este es un proyecto básico en Python utilizando el framework **Reflex** y **Poetry** para la gestión de dependencias. La aplicación consiste en una página web interactiva con una temática oscura que incluye un botón tipo ruleta.

## Características
- Interfaz moderna en tonos oscuros (Dark mode).
- Título principal y mensaje de bienvenida.
- Juego de ruleta: Elige un color (Rojo, Negro o Blanco) y gira para ganar o perder.

## Requisitos Previos
Antes de comenzar, asegúrate de tener instalado:
- **Python 3.10** o superior.
- **Poetry** (gestor de dependencias).
- **Node.js LTS** (necesario para el frontend de Reflex).
- **Visual Studio Code** (recomendado para desarrollo).

## Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/ElvinJr/Reflex.git
   cd Reflex/pagina
   ```

2. **Instalar dependencias con Poetry:**
   ```bash
   poetry install
   ```

## Ejecución

Para iniciar la aplicación en modo desarrollo, ejecuta:
```bash
poetry run reflex run
```
La aplicación estará disponible en `http://localhost:3000`.

## Instrucciones de Despliegue
Para correr el proyecto en cualquier máquina después de clonar:
1. Asegúrate de que las dependencias de sistema (Python, Node.js) estén instaladas.
2. Ejecuta `poetry install` dentro de la carpeta `pagina` para configurar el entorno virtual.
3. Inicia el servidor con `poetry run reflex run`.