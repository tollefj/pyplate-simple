from rich.console import Console
from rich.table import Table

console = Console()


def print_colored(text, style):
    console.print(text, style=style)


def print_table(data, columns, title=None):
    table = Table(title=title)
    for column in columns:
        table.add_column(column)

    for row in data:
        table.add_row(*row)

    console.print(table)


def newline(times=1):
    print("\n" * times)
