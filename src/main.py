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
    
    # Get directory - from args or user input
    if args.directory:
        pasta_exercicios = os.path.abspath(args.directory)
    else:
        pasta_exercicios = input("Digite o caminho da pasta com os exercícios: ")
        pasta_exercicios = os.path.abspath(pasta_exercicios)
    
    # Get output filename - from args or user input
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
