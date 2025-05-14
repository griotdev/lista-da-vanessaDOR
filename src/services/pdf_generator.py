"""Module for creating PDFs from C source files."""
import os
from typing import Optional
from fpdf import FPDF

from src.utils import natural_sort_key


class CustomPDF(FPDF):
    """Custom PDF class that adds a footer to each page."""
    
    def footer(self) -> None:
        """Add footer to each page with repository information."""
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Repository link
        self.cell(0, 10, 'Feito com Lista da vanessaDOR', 0, 0, 'R')
        self.ln(4)
        self.cell(0, 10, 'https://github.com/griotdev/lista-da-vanessador', 0, 0, 'R')


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
        
    pdf = CustomPDF()
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
                    lineNumber = 1
                    for line in content.split('\n'):
                        # Set gray color for line number
                        pdf.set_text_color(128, 128, 128)  # Gray color
                        pdf.cell(20, 5, f"{lineNumber}", ln=0)
                        # Reset to black for code content
                        pdf.set_text_color(0, 0, 0)  # Black color
                        pdf.cell(0, 5, f"\t{line}", ln=True)
                        lineNumber += 1
                    pdf.cell(0, 5, f"Total de linhas: {lineNumber-1}", ln=True)
            except Exception as e:
                pdf.cell(0, 5, f"Erro ao ler arquivo {c_file}: {str(e)}", ln=True)
            
            pdf.cell(0, 10, "", ln=True)
            pdf.add_page()
    
    pdf.output(output_file)
    return True 