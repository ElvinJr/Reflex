"""Versión Casino Royale - Optimizada y Fluida (Sin Animaciones Pesadas)"""

import reflex as rx
import random
import asyncio

from rxconfig import config

class State(rx.State):
    """Estado estilo Casino optimizado para fluidez."""
    colors: list[str] = ["Rojo", "Negro", "Blanco"]
    selected_color: str = "Rojo"
    result_color: str = "?"
    message: str = "🎯 ¡Hagan sus apuestas, señores!"
    is_spinning: bool = False
    result_bg: str = "rgba(255, 255, 255, 0.1)"

    async def spin(self):
        if self.is_spinning:
            return
            
        self.is_spinning = True
        self.message = "🎰 ¡Sorteando resultado...!"
        self.result_color = "?"
        self.result_bg = "rgba(255, 255, 255, 0.1)"
        
        # Pequeña espera para dar emoción (sin animaciones pesadas)
        await asyncio.sleep(1)
        
        self.result_color = random.choice(self.colors)
        
        if self.selected_color == self.result_color:
            self.message = f"👑 ¡JACKPOT! Salió {self.result_color}. ¡Felicidades!"
            self.result_bg = "rgba(0, 255, 127, 0.2)" # Verde éxito
        else:
            self.message = f"💸 La casa gana. Salió {self.result_color}. ¿Otra vez?"
            self.result_bg = "rgba(255, 69, 58, 0.2)" # Rojo fallo
            
        self.is_spinning = False

    def set_selected_color(self, color: str):
        self.selected_color = color
        self.message = f"Has apostado al {color}."

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            # Título Neon Gold
            rx.vstack(
                rx.icon("clover", size=50, color="#FFD700"),
                rx.heading("REFLEX CASINO ROYALE", size="9", weight="bold", color="#FFD700"),
                rx.text("LA SUERTE ESTÁ EN TUS MANOS", size="2", letter_spacing="4px", color="white", opacity=0.8),
                align="center",
                margin_bottom="2.5em",
                padding="1em",
                border="2px solid #FFD700",
                border_radius="xl",
                box_shadow="0 0 20px rgba(255, 215, 0, 0.2)",
            ),
            
            # El Tablero de Juego (Fluido y sin lag)
            rx.box(
                rx.vstack(
                    # Visualizador de Resultado Estático y Elegante
                    rx.center(
                        rx.text(State.result_color, size="9", weight="bold", color="white"),
                        width="180px", height="180px",
                        border_radius="30px", # Cuadrado redondeado elegante
                        border="4px solid #FFD700",
                        background=State.result_bg,
                        box_shadow="0 10px 30px rgba(0,0,0,0.5)",
                        margin_y="1.5em",
                        transition="background 0.5s ease",
                    ),
                    
                    rx.text("ELIGE TU COLOR", size="4", weight="bold", color="#FFD700"),
                    
                    rx.radio_group(
                        State.colors,
                        value=State.selected_color,
                        on_change=State.set_selected_color,
                        direction="row",
                        spacing="6",
                        size="3",
                        color_scheme="amber",
                    ),
                    
                    rx.button(
                        "¡GIRAR AHORA!",
                        on_click=State.spin,
                        loading=State.is_spinning,
                        size="4",
                        width="100%",
                        bg="#FFD700",
                        color="#4B0000",
                        font_weight="bold",
                        _hover={"bg": "#FFE033", "transform": "translateY(-2px)"},
                        margin_top="1em",
                    ),
                    
                    # Consola de resultados
                    rx.box(
                        rx.text(State.message, text_align="center", color="white", font_size="1.1em"),
                        padding="1.2em",
                        border_radius="lg",
                        background="rgba(0,0,0,0.4)",
                        border="1px solid rgba(255,215,0,0.3)",
                        margin_top="1em",
                        width="100%",
                    ),
                    spacing="4",
                    align="center",
                ),
                padding="3em",
                border_radius="35px",
                background="rgba(20, 0, 0, 0.6)",
                backdrop_filter="blur(10px)",
                border="2px solid rgba(255, 215, 0, 0.4)",
                box_shadow="0 25px 50px rgba(0,0,0,0.7)",
                width="480px",
            ),
            
            rx.text("Desarrollado con Reflex Pro | 2026", color="white", opacity=0.4, margin_top="3em"),
            align="center",
            width="100%",
        ),
        min_height="100vh",
        background="radial-gradient(circle at center, #7a0000 0%, #3d0000 50%, #1a0000 100%)",
        padding_y="4em",
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark",
        accent_color="amber",
        radius="large",
    )
)
app.add_page(index, title="Casino Reflex Royale")
