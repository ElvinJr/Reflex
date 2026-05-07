import reflex as rx

config = rx.Config(
    app_name="pagina",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)