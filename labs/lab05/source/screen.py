import time

import typer

app = typer.Typer(add_completion=False)

ANSI_COLORS = [
    "\033[31m",  # red
    "\033[32m",  # green
    "\033[33m",  # yellow
    "\033[34m",  # blue
    "\033[35m",  # magenta
]
ANSI_RESET = "\033[0m"


def headless_typewriter(text: str, delay: float = 0.05) -> None:
    for i, ch in enumerate(text):
        color = ANSI_COLORS[i % len(ANSI_COLORS)]
        typer.echo(color + ch + ANSI_RESET, nl=False)
        time.sleep(delay)
    typer.echo("")


@app.command()
def main(
    name: str,
    lastname: str = typer.Option(
        "",
        help="Фамилия пользователя.",
    ),
    formal: bool = typer.Option(
        False,
        "--formal",
        "-f",
        help="Формальное приветствие.",
    ),
    gui: bool = typer.Option(
        False,
        "--gui",
        help="Включить графический режим (pygame).",
    ),
) -> None:
    if formal:
        greeting = f"Добрый день, {name} {lastname}!".strip()
    else:
        greeting = f"Привет, {name}!"

    if not gui:
        headless_typewriter(greeting, delay=0.05)
        return

    import pygame

    def colorful_typewriter_gui(screen, font, text, center, delay=0.08):
        colors = [
            (255, 0, 0),
            (0, 255, 0),
            (255, 255, 0),
            (0, 0, 255),
            (255, 0, 255),
        ]

        full_surface = font.render(text, True, (255, 255, 255))
        full_rect = full_surface.get_rect(center=center)
        x0, y0 = full_rect.topleft

        for i in range(1, len(text) + 1):
            screen.fill((0, 0, 0))

            x = x0
            for j, ch in enumerate(text[:i]):
                color = colors[j % len(colors)]
                ch_surface = font.render(ch, True, color)
                screen.blit(ch_surface, (x, y0))
                x += ch_surface.get_width()

            pygame.display.flip()
            time.sleep(delay)

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Greeting App")

    font = pygame.font.SysFont(None, 75)

    colorful_typewriter_gui(
        screen=screen,
        font=font,
        text=greeting,
        center=(400, 300),
        delay=0.08,
    )

    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    app()
