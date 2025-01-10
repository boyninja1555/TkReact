import os
import typer

app = typer.Typer()

@app.command()
def init(name: str, path = "."):
    """Initialize a new TkReact project"""
    print(f"Project {name} initialized at \"{os.path.abspath(path)}\"")

if __name__ == "__main__":
    app()
