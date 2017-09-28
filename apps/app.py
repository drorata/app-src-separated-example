import sys
sys.path.insert(0, '.')

from src import code
import click

@click.command()
@click.option('--input', '-i', type=click.STRING)
def cli(input):
    print(code.my_func(input))

if __name__ == "__main__":
    cli()
