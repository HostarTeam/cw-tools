from typer import Typer


app = Typer()


@app.command()
def hello(name: str):
    print(f'Hello {name}')


@app.command()
def goodbye(name: str):
    print(f'Goodbye {name}')
