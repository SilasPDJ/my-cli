import argparse
from utils.pdfmerge import generate_pdf_merge


class Cli:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(
            description="CLI Aleatório - Escolha uma opção")
        self.parser.add_argument(
            "-v", "--version", action="version", version="%(prog)s 1.0.0")

        self.subparsers = self.parser.add_subparsers(
            dest="subcommand", help="Comandos disponíveis")

        merge_pdf = self.subparsers.add_parser(
            'generate_pdf_merge', help="Juntar arquivos PDF", aliases=['pdf-merge'])
        merge_pdf.add_argument(
            "dir", type=str, help="initial dir folder containing the pdfs to get merged")
        merge_pdf.add_argument(
            "-save", type=str, default=None, help="Diretório final para a mesclagem dos PDFs.")

        merge_pdf.add_argument(
            "-rev", default=True, help="if files sorting shall be reversed")

        # Parse the arguments
        args = self.parser.parse_args()

        # Check which subcommand was provided and call the corresponding function
        if args.subcommand == 'generate_pdf_merge':
            generate_pdf_merge(args.dir, args.dst, args.rev)
        else:
            # Handle the case where no subcommand is provided or an unrecognized subcommand is given
            print("Subcommand not recognized. Please provide a valid subcommand.")
            self.parser.print_help()


if __name__ == "__main__":
    # Create an instance of the Cli class to trigger argument parsing and function calls
    Cli()
