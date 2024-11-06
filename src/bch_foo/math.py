"""Console script for bch_foo."""

import bch_foo

import typer
app = typer.Typer()

@app.command()
def hello(name: str):
    print(f"Hello {name}")

@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


if __name__ == "__main__":
    app()
    exit()










from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main(a,b):
    console.print( int(a) + int(b) )
    """Console script for bch_foo."""
    console.print("Replace this message by putting your code into "
               "bch_foo.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")



if __name__ == "__main__":
    app()
