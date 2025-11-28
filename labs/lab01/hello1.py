import typer

# another test comment to conflict

def main(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(False, "--formal", "-f", help="Использовать формальное приветствие."),
):
    greeting = f"Добрый день, {name} {lastname}!" if formal else f"Привет, {name}!"
    print(greeting)


if __name__ == "__main__":
    typer.run(main)

