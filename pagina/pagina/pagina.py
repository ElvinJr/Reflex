"""Primera página web con Reflex - Ruleta Interactiva"""

import reflex as rx
import random

from rxconfig import config

class State(rx.State):
    """The app state."""
    colors: list[str] = ["Rojo", "Negro", "Blanco"]
    selected_color: str = "Rojo"
    result_color: str = ""
    message: str = ""
    is_spinning: bool = False

    def set_selected_color(self, color: str):
        self.selected_color = color

    def spin(self):
        self.is_spinning = True
        # Simular giro
        self.result_color = random.choice(self.colors)
        
        if self.selected_color == self.result_color:
            self.message = f"¡Felicidades, ganaste! Salió {self.result_color}."
        else:
            self.message = f"Perdiste, inténtalo de nuevo. Salió {self.result_color}."
        
        self.is_spinning = False

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.vstack(
            rx.heading("Primera página web con Reflex", size="9", color_scheme="gray"),
            rx.text(
                "¡Bienvenido a esta experiencia interactiva! Prueba tu suerte con nuestra ruleta.",
                size="5",
                color_scheme="gray",
            ),
            
            rx.divider(width="100%", margin_y="2em"),
            
            rx.vstack(
                rx.text("Elige un color:", size="4", weight="bold"),
                rx.radio_group(
                    State.colors,
                    value=State.selected_color,
                    on_change=State.set_selected_color,
                    direction="row",
                    spacing="4",
                ),
                rx.button(
                    "Girar Ruleta",
                    on_click=State.spin,
                    size="4",
                    color_scheme="gray",
                    variant="solid",
                    margin_top="1em",
                ),
                rx.cond(
                    State.message != "",
                    rx.box(
                        rx.text(State.message, size="5", weight="bold", color="white"),
                        padding="1.5em",
                        border_radius="lg",
                        bg="rgba(255, 255, 255, 0.1)",
                        margin_top="2em",
                        width="100%",
                        text_align="center",
                    ),
                ),
                spacing="4",
                padding="2em",
                border="1px solid rgba(255,255,255,0.1)",
                border_radius="xl",
                width="100%",
                align="center",
            ),
            
            spacing="5",
            justify="center",
            min_height="85vh",
            align="center",
        ),
        padding="2em",
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        accent_color="gray",
    )
)
app.add_page(index, title="Ruleta Reflex")
