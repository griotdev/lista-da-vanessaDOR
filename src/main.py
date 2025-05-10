"""Main entry point for the PDF generator application."""
import os
from src.pdf_generator import create_exercises_pdf
from src.cli import parse_arguments, get_user_input

# oi gente

def main() -> None:
    """
    Main function that handles user input and runs the PDF generation process.
    
    First tries to get arguments from the command line, and if not provided,
    prompts the user for input. Then generates a PDF containing all C source 
    files found in the directory.
    """
    args = parse_arguments()
    
    # If command-line arguments are provided, use them
    if args.directory and args.output:
        pasta_exercicios = os.path.abspath(args.directory)
        nome_arquivo_saida = args.output
        if not nome_arquivo_saida.lower().endswith('.pdf'):
            nome_arquivo_saida += '.pdf'
    # Otherwise, get input interactively
    else:
        pasta_exercicios, nome_arquivo_saida = get_user_input()
    
    success = create_exercises_pdf(pasta_exercicios, nome_arquivo_saida)
    
    if success:
        print(f"Procurando arquivos .c em: {pasta_exercicios}")
        print("PDF foi criado com sucesso!")
    else:
        print("Ocorreu um erro ao gerar o PDF.")

if __name__ == "__main__":
    main()
