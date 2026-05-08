# Informe Técnico: Desarrollo de Aplicación Web con Reflex

## 1. Introducción
Este proyecto documenta la creación de una página web interactiva utilizando el ecosistema de **Python** con el framework **Reflex**. Se ha priorizado el uso de **Poetry** para la gestión de dependencias y **GitHub** para el control de versiones, siguiendo las mejores prácticas de desarrollo de software.

---

## 2. Herramientas y Requisitos
Para el desarrollo exitoso del proyecto se utilizaron las siguientes herramientas:
- **Lenguaje**: Python 3.11+
- **Framework**: Reflex (Full-stack Python)
- **Gestor de Paquetes**: Poetry
- **Entorno de Desarrollo**: Visual Studio Code
- **Runtime de Frontend**: Node.js LTS

---

## 3. Arquitectura del Código
La aplicación utiliza una arquitectura basada en **Estados**, donde la lógica del servidor y la interfaz del usuario están sincronizadas automáticamente.

### Ilustración de la Lógica (State)
```python
class State(rx.State):
    # Definición de variables de estado
    colors: list[str] = ["Rojo", "Negro", "Blanco"]
    selected_color: str = "Rojo"
    result_color: str = ""
    message: str = ""

    # Función principal de la ruleta
    def spin(self):
        self.result_color = random.choice(self.colors)
        if self.selected_color == self.result_color:
            self.message = f"¡Felicidades, ganaste!"
        else:
            self.message = f"Perdiste, inténtalo de nuevo."
```

### Ilustración de la Interfaz (UI)
Se utilizó un diseño basado en **VStack** (pilas verticales) para mantener la simplicidad y el enfoque en el botón interactivo.
```python
def index():
    return rx.center(
        rx.vstack(
            rx.heading("CASINO ROYALE", size="9", weight="bold", color="#FFD700"),
            rx.box(
                # UI de la apuesta y el visualizador del resultado
                rx.center(rx.text(State.result_color, size="9")),
                background="rgba(20, 0, 0, 0.6)",
                border="2px solid #FFD700",
            ),
            rx.button("¡APUESTA Y GIRA!", on_click=State.spin),
        ),
        background="radial-gradient(circle, #7a0000 0%, #1a0000 100%)",
    )
```

---

## 4. Guía de Solución de Problemas (Troubleshooting)

| Error Común | Causa Probable | Solución |
| :--- | :--- | :--- |
| `AttributeError: 'State' has no attribute 'set_x'` | Reflex no generó el setter automático. | Definir manualmente la función `set_x` en la clase `State`. |
| `Execution Policy Restricted` | PowerShell bloquea scripts externos (como Bun). | Ejecutar `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` o instalar Node.js manualmente. |
| `Port 3000 already in use` | Otra instancia de la app o proceso está usando el puerto. | Cerrar la terminal anterior o usar `taskkill /F /IM node.exe` (con precaución). |
| `Node.js not found` | Node no está en las variables de entorno (PATH). | Agregar `C:\Program Files\nodejs` al PATH del sistema y reiniciar la terminal. |

---

## 5. Resultados Obtenidos
La aplicación presenta un comportamiento fluido con un diseño oscuro profesional.

### Vista Previa
![Resultado de la aplicación](https://github.com/ElvinJr/Reflex/blob/main/Imagen/Screenshot%202026-05-07%20212715.png)


---

## 6. Conclusiones
Reflex permite a los desarrolladores de Python entrar al mundo del desarrollo web con una curva de aprendizaje mínima, eliminando la necesidad de manejar HTML/JS complejos mientras se mantiene una estructura robusta y escalable.
