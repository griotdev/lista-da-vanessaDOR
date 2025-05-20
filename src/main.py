"""Main entry point for the PDF generator application."""
import os
from src.services.pdf_generator import create_exercises_pdf
from src.services.cli import parse_arguments
from src.services.gui import run_gui

# oi gente

def main() -> None:
    """
    Main function that handles user input and runs the PDF generation process.

    Launches the GUI by default when no command-line arguments are provided.
    When arguments are present, runs in CLI mode and processes those arguments.
    Generates a PDF containing all C source files found in the specified directory.
    """
    args = parse_arguments()

    # Launch GUI by default when no directory or output is provided
    if not args.directory and not args.output or args.gui:
        run_gui()
        return

    # CLI mode with arguments
    # Get directory from args
    if args.directory:
        pasta_exercicios = os.path.abspath(args.directory)
    else:
        pasta_exercicios = input("Digite o caminho da pasta com os exercícios: ")
        pasta_exercicios = os.path.abspath(pasta_exercicios)

    # Get output filename from args
    if args.output:
        nome_arquivo_saida = args.output
    else:
        nome_arquivo_saida = input("Digite o nome do arquivo PDF de saída: ")

    # Ensure the output file has .pdf extension
    if not nome_arquivo_saida.lower().endswith('.pdf'):
        nome_arquivo_saida += '.pdf'

    success = create_exercises_pdf(pasta_exercicios, nome_arquivo_saida)

    if success:
        print(f"Procurando arquivos .c em: {pasta_exercicios}")
        print("PDF foi criado com sucesso!")
    else:
        print("Ocorreu um erro ao gerar o PDF.")

if __name__ == "__main__":
    main()
