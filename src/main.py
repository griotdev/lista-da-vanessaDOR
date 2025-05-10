import os
import re
from fpdf import FPDF
# oi gente
def natural_sort_key(s):
    """Function to enable natural sorting (e.g., 1, 2, 3,..., 10, 11 instead of 1, 10, 11, 2, 3)"""
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('([0-9]+)', s)]

def create_exercises_pdf(root_folder, output_file="exercises.pdf"):
    if not os.path.exists(root_folder):
        print(f"Erro: Diretório '{root_folder}' não existe.")
        return
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

if __name__ == "__main__":
    pasta_exercicios = input("Digite o caminho da pasta com os exercícios: ")
    nome_arquivo_saida = input("Digite o nome do arquivo PDF de saída: ")
    
    if not nome_arquivo_saida.lower().endswith('.pdf'):
        nome_arquivo_saida += '.pdf'
    
    pasta_exercicios = os.path.abspath(pasta_exercicios)
    
    create_exercises_pdf(pasta_exercicios, nome_arquivo_saida)
    print(f"Procurando arquivos .c em: {pasta_exercicios}")
    print("PDF foi criado com sucesso!")
