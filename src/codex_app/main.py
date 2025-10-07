import os

import typer
from dotenv import load_dotenv

app = typer.Typer(help="Codex entegrasyonu için örnek CLI")


@app.command()
def hello(name: str = "world"):
    """Basit bir selamlama komutu."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY", "")
    typer.echo(f"Hello, {name}! OPENAI_API_KEY {'var' if api_key else 'yok'}.")


@app.command()
def config():
    """Konfigürasyonun özetini yazdırır."""
    load_dotenv()
    base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    typer.echo(f"BASE_URL: {base_url}")


if __name__ == "__main__":
    app()
