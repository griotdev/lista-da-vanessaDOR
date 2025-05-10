"""Command-line interface for the PDF generator application."""
import os
import argparse
from typing import Tuple, Optional


def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments.
    
    Returns:
        Parsed command line arguments
    """
    parser = argparse.ArgumentParser(
        description="Generate a PDF containing C source files from a directory"
    )
    parser.add_argument(
        "-d", "--directory",
        help="Directory containing C source files to include in the PDF"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output PDF filename"
    )
    return parser.parse_args()


def get_user_input() -> Tuple[str, str]:
    """
    Get user input for the source directory and output file.
    
    Returns:
        Tuple containing (source_directory_path, output_file_path)
    """
    pasta_exercicios = input("Digite o caminho da pasta com os exercícios: ")
    nome_arquivo_saida = input("Digite o nome do arquivo PDF de saída: ")
    
    if not nome_arquivo_saida.lower().endswith('.pdf'):
        nome_arquivo_saida += '.pdf'
    
    pasta_exercicios = os.path.abspath(pasta_exercicios)
    
    return pasta_exercicios, nome_arquivo_saida 