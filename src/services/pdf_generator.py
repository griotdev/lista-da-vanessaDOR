"""Module for creating PDFs from C source files."""
import os
from typing import List
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
        self.ln(4)
        self.cell(0, 10, 'By: André Rodrigues e Pedro Giroldo', 0, 0, 'R')
    
    def wrap_text_to_lines(self, text: str, max_width: float) -> List[str]:
        """
        Wrap text to fit within the specified width.
        
        Args:
            text: The text to wrap
            max_width: Maximum width in points
            
        Returns:
            List of wrapped lines
        """
        words = text.split(' ')
        lines = []
        current_line = ""
        
        for word in words:
            # Test if adding this word would exceed the width
            test_line = current_line + (" " if current_line else "") + word
            
            # Get width of test line
            test_width = self.get_string_width(test_line)
            
            if test_width <= max_width:
                current_line = test_line
            else:
                # If current line has content, save it and start new line
                if current_line:
                    lines.append(current_line)
                    current_line = word
                else:
                    # Single word is too long, force break it
                    lines.append(word)
        
        # Add the last line if it has content
        if current_line:
            lines.append(current_line)
        
        return lines if lines else [""]


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
                    
                    # Calculate available width for code content (total width - line number width - margins)
                    page_width = pdf.w - 2 * pdf.l_margin  # Total usable width
                    line_number_width = 20  # Width reserved for line numbers
                    tab_width = pdf.get_string_width("\t")  # Width of tab character
                    available_width = page_width - line_number_width - tab_width
                    
                    for line in content.split('\n'):
                        # Set gray color for line number
                        pdf.set_text_color(128, 128, 128)  # Gray color
                        pdf.cell(line_number_width, 5, f"{lineNumber}", ln=0)
                        
                        # Reset to black for code content
                        pdf.set_text_color(0, 0, 0)  # Black color
                        
                        # Check if line needs wrapping
                        line_content = f"\t{line}"
                        line_width = pdf.get_string_width(line_content)
                        
                        if line_width <= available_width:
                            # Line fits, print normally
                            pdf.cell(0, 5, line_content, ln=True)
                        else:
                            # Line needs wrapping
                            wrapped_lines = pdf.wrap_text_to_lines(line, available_width - tab_width)
                            
                            # Print first wrapped line with tab
                            if wrapped_lines:
                                pdf.cell(0, 5, f"\t{wrapped_lines[0]}", ln=True)
                                
                                # Print continuation lines with proper indentation
                                for wrapped_line in wrapped_lines[1:]:
                                    # Empty line number cell for continuation lines
                                    pdf.set_text_color(128, 128, 128)
                                    pdf.cell(line_number_width, 5, "", ln=0)
                                    pdf.set_text_color(0, 0, 0)
                                    pdf.cell(0, 5, f"\t{wrapped_line}", ln=True)
                        
                        lineNumber += 1
                    
                    pdf.cell(0, 5, f"Total de linhas: {lineNumber-1}", ln=True)
            except Exception as e:
                pdf.cell(0, 5, f"Erro ao ler arquivo {c_file}: {str(e)}", ln=True)
            
            pdf.cell(0, 10, "", ln=True)
            pdf.add_page()
    
    pdf.output(output_file)
    return True 