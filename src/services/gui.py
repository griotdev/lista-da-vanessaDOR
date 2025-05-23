"""GUI interface for the PDF generator application using Tkinter."""
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from src.services.pdf_generator import create_exercises_pdf


class PDFGeneratorGUI:
    """
    Graphical user interface for the PDF generator application.

    This class provides a Tkinter-based GUI for selecting a directory with
    C source files and specifying an output PDF file name.
    """

    def __init__(self, root: tk.Tk) -> None:
        """
        Initialize the GUI components.

        Args:
            root: The Tkinter root window
        """
        self.root = root
        self.root.title("Lista da Vanessador - Gerador de PDF")
        self.root.geometry("1220x650")
        self.root.resizable(True, True)
        self.root.configure(bg="#f0f0f0")

        self.directory_path = tk.StringVar()
        self.output_filename = tk.StringVar()

        # Configure styles
        self._configure_styles()

        self._create_widgets()
        self._center_window()

    def _configure_styles(self) -> None:
        """Configure custom styles for widgets."""
        style = ttk.Style()
        # Style for browse buttons
        style.configure(
            "Browse.TButton",
            font=("Arial", 10, "bold"),
            padding=5
        )

        # Style for the generate button
        style.configure(
            "Generate.TButton",
            font=("Arial", 12, "bold"),
            padding=8
        )

        # Style for frames
        style.configure(
            "Card.TFrame",
            background="#ffffff",
            borderwidth=2,
            relief="groove"
        )

    def _center_window(self) -> None:
        """Center the window on the screen."""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def _create_widgets(self) -> None:
        """Create and place all UI elements in the window."""
        # Create a main frame
        main_frame = ttk.Frame(self.root, padding="20", style="Card.TFrame")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Title
        title_frame = ttk.Frame(main_frame)
        title_frame.pack(fill=tk.X, pady=(0, 20))

        title_label = ttk.Label(
            title_frame,
            text="Gerador de PDF para Arquivos C",
            font=("Arial", 18, "bold")
        )
        title_label.pack(side=tk.LEFT)

        # Add an icon (simulated with text for now)
        icon_label = ttk.Label(
            title_frame,
            text="📄",
            font=("Arial", 24)
        )
        icon_label.pack(side=tk.RIGHT)

        # Directory selection
        dir_frame = ttk.Frame(main_frame)
        dir_frame.pack(fill=tk.X, pady=5)

        dir_label = ttk.Label(dir_frame, text="Pasta com os exercícios:", width=20)
        dir_label.pack(side=tk.LEFT, padx=(0, 5))

        dir_entry = ttk.Entry(dir_frame, textvariable=self.directory_path, width=40)
        dir_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        browse_button = ttk.Button(
            dir_frame,
            text="Escolher Pasta",
            command=self._browse_directory,
            style="Browse.TButton"
        )
        browse_button.pack(side=tk.RIGHT)

        # Output file name
        file_frame = ttk.Frame(main_frame)
        file_frame.pack(fill=tk.X, pady=5)

        file_label = ttk.Label(file_frame, text="Nome do arquivo PDF:", width=20)
        file_label.pack(side=tk.LEFT, padx=(0, 5))

        file_entry = ttk.Entry(file_frame, textvariable=self.output_filename, width=40)
        file_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        save_button = ttk.Button(
            file_frame,
            text="Escolher Local",
            command=self._browse_output_file,
            style="Browse.TButton"
        )
        save_button.pack(side=tk.RIGHT)

        # Generate button
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=20)

        generate_button = ttk.Button(
            button_frame,
            text="GERAR PDF",
            command=self._generate_pdf,
            width=20,
            style="Generate.TButton"
        )
        generate_button.pack()

        # Status label
        status_frame = ttk.Frame(main_frame, style="Card.TFrame")
        status_frame.pack(fill=tk.X, pady=10, padx=5)

        self.status_var = tk.StringVar()
        self.status_var.set("Pronto para gerar o PDF")
        status_label = ttk.Label(
            status_frame,
            textvariable=self.status_var,
            font=("Arial", 10),
            padding=10
        )
        status_label.pack(fill=tk.X)

        # Footer
        footer_frame = ttk.Frame(main_frame)
        footer_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        author_text = ttk.Label(
            footer_frame,
            text="By: André Rodrigues e Pedro Giroldo",
            font=("Arial", 8)
        )
        author_text.pack(side=tk.LEFT)

        footer_text = ttk.Label(
            footer_frame,
            text="Lista da vanessaDOR - github.com/griotdev/lista-da-vanessador",
            font=("Arial", 8)
        )
        footer_text.pack(side=tk.RIGHT)

    def _browse_directory(self) -> None:
        """Open a directory selection dialog and update the directory path."""
        directory = filedialog.askdirectory(
            title="Selecionar pasta com exercícios",
            initialdir=os.path.expanduser("~")  # Start from user's home directory
        )
        if directory:
            self.directory_path.set(directory)
            self.status_var.set(f"Pasta selecionada: {directory}")

    def _browse_output_file(self) -> None:
        """Open a file save dialog and update the output filename."""
        filetypes = [("PDF Files", "*.pdf"), ("All Files", "*.*")]
        filename = filedialog.asksaveasfilename(
            title="Salvar PDF como",
            initialdir=os.path.expanduser("~"),
            defaultextension=".pdf",
            filetypes=filetypes
        )
        if filename:
            self.output_filename.set(filename)
            self.status_var.set(f"Arquivo de saída: {filename}")

    def _generate_pdf(self) -> None:
        """
        Generate the PDF using the selected directory and output filename.

        Validates inputs, calls the PDF generation function, and displays the result.
        Shows progress updates in the status bar.
        """
        directory = self.directory_path.get().strip()
        output_file = self.output_filename.get().strip()

        # Validate inputs
        if not directory:
            messagebox.showerror(
                "Erro",
                "Por favor, selecione a pasta com os exercícios."
            )
            return

        if not output_file:
            messagebox.showerror(
                "Erro",
                "Por favor, informe o nome do arquivo PDF de saída."
            )
            return

        # Ensure directory exists
        if not os.path.exists(directory):
            messagebox.showerror(
                "Erro",
                f"O diretório '{directory}' não existe."
            )
            return

        # Ensure the output file has .pdf extension
        if not output_file.lower().endswith('.pdf'):
            output_file += '.pdf'
            self.output_filename.set(output_file)

        # Update status and cursor
        self.status_var.set(f"⏳ Gerando PDF... Procurando arquivos .c em: {directory}")
        self.root.update()

        try:
            success = create_exercises_pdf(directory, output_file)

            if success:
                self.status_var.set("✅ PDF foi criado com sucesso!")
                self.root.config(cursor="")
                messagebox.showinfo(
                    "Sucesso",
                    f"PDF '{output_file}' foi criado com sucesso!"
                )
            else:
                self.status_var.set("❌ Ocorreu um erro ao gerar o PDF.")
                self.root.config(cursor="")
                messagebox.showerror(
                    "Erro",
                    "Ocorreu um erro ao gerar o PDF."
                )
        except Exception as e:
            self.status_var.set(f"❌ Erro: {str(e)}")
            self.root.config(cursor="")
            messagebox.showerror("Erro", f"Erro ao gerar o PDF: {str(e)}")


def run_gui() -> None:
    """
    Start the GUI application.

    Creates a Tkinter root window and initializes the GUI.
    """
    root = tk.Tk()
    PDFGeneratorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    run_gui()
