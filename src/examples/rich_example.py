from time import sleep

from rich import print as rprint
from rich.console import Console
from rich.markdown import Markdown
from rich.progress import track
from rich.table import Table

# Rich print with colors and formatting
rprint("[bold red]Hello[/bold red] [italic blue]World![/italic blue]")

# Rich console
console = Console()
console.print("Hello", "World!", style="bold yellow")

# Rich markdown
markdown_text = """
# Markdown Title

This is some *italic* text, and this is **bold** text.

- Item 1
- Item 2
- Item 3

Visit [Rich GitHub Repository](https://github.com/willmcgugan/rich)
"""

markdown = Markdown(markdown_text)
console.print(markdown)

# Rich progress bar
for i in track(range(10), description="Processing"):
    sleep(0.1)

# Rich table
table = Table(title="Rich Table")
table.add_column("ID", justify="right", style="cyan")
table.add_column("Name", style="magenta")
table.add_column("Score", justify="right", style="green")

table.add_row("1", "Alice", "10")
table.add_row("2", "Bob", "12")
table.add_row("3", "Charlie", "9")

console.print(table)
