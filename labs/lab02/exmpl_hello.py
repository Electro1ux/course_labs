import sys
import time
import typer

app = typer.Typer()


def colorful_print(text: str, delay: float = 0.05) -> None:
    colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m"]
    reset = "\033[0m"
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        sys.stdout.write(color + char + reset)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # перенос строки после текста


@app.command()
def main(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(
        False,
        "--formal",
        "-f",
        help="Использовать формальное приветствие.",
    ),
) -> None:
    greeting = f"Добрый день, {name} {lastname}!" if formal else f"Привет, {name}!"
    colorful_print(greeting)


if __name__ == "__main__":
    app()
