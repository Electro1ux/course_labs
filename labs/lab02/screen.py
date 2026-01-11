import pygame
import typer
import time

app = typer.Typer()

def colorful_render(screen, font, text, position):
    colors = [(255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 0, 255), (255, 0, 255)]
    x, y = position

    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        char_surface = font.render(char, True, color)
        screen.blit(char_surface, (x, y))
        x += char_surface.get_width()
        pygame.display.flip()
        time.sleep(0.2)  # пауза для эффекта "печатающейся строки"

@app.command()
def main(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(
        False,
        "--formal",
        "-f",
        help="Использовать формальное приветствие."),
):
    if formal:
    greeting = f"Добрый день, {name} {lastname}!".strip()
    else:
    greeting = f"Привет, {name}!"


    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Greeting App")
    screen.fill((0, 0, 0))  # черный фон

    font = pygame.font.SysFont(None, 75)
    text_rect = font.render(greeting, True, (255, 255, 255)).get_rect()
    text_rect.center = (screen_width // 2, screen_height // 2)

    colorful_render(screen, font, greeting, (text_rect.x, text_rect.y))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    app()
