import argparse


class Cli:
    def __init__(self) -> None:
        self.parser = parser = argparse.ArgumentParser(
            description="CLI Aleatório - Escolha uma opção")
        # self.parser.version = "1.0.0"
        self.parser.add_argument(
            "-v", "--version", action="version", version="%(prog)s 1.0.0")

        self.subparsers = self.parser.add_subparsers(help="Comandos disponíveis")
        
        self.parser.add_argument()

        self.parser.parse_args()


if __name__ == "__main__":
    args = Cli()
    # Restante do seu código aqui...
