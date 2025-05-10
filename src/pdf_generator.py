"""Module for creating PDFs from C source files."""
import os
from typing import Optional
from fpdf import FPDF

from src.utils import natural_sort_key


def create_exercises_pdf(root_folder: str, output_file: str = "exercises.pdf") -> bool:
    """
    Create a PDF containing all C source files found in the given directory.
    
    The function traverses the directory structure recursively, finding all .c files,
    and adds their content to a PDF document with proper formatting.
    
    Args:
        root_folder: Path to the directory containing the C files
        output_file: Name of the output PDF file
        
    Returns:
        True if PDF was created successfully, False otherwise
    """
    if not os.path.exists(root_folder):
        print(f"Error: Directory '{root_folder}' does not exist.")
        return False
        
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Courier", size=10)
    
    for dirpath, dirnames, filenames in os.walk(root_folder):
        dirnames.sort(key=natural_sort_key)
        c_files = [f for f in filenames if f.endswith('.c')]
        c_files.sort(key=natural_sort_key)
        
        for c_file in c_files:
            full_path = os.path.join(dirpath, c_file)
            
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, f"Exercício: {c_file}", ln=True)
            pdf.set_font("Courier", size=10)
            
            try:
                with open(full_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    for line in content.split('\n'):
                        pdf.cell(0, 5, line, ln=True)
            except Exception as e:
                pdf.cell(0, 5, f"Erro ao ler arquivo {c_file}: {str(e)}", ln=True)
            
            pdf.cell(0, 10, "", ln=True)
            pdf.add_page()
    
    pdf.output(output_file)
    return True 