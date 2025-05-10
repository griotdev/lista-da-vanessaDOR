# Lista da Wanessador

A simple Python application that generates a PDF containing all C source files found in a specified directory.

## Features

- Recursively scans a directory for C source files
- Creates a PDF with all C code found, one exercise per page
- Natural sorting of files (1, 2, 3, ..., 10, 11 instead of 1, 10, 11, ...)
- Support for both command-line arguments and interactive mode

## Installation

1. Clone this repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Interactive Mode

```bash
python -m src.main
```

You will be prompted to enter:

- The path to the directory containing C files
- The name of the output PDF file

### Command-line Mode

```bash
python -m src.main -d /path/to/c/files -o output.pdf
```

Arguments:

- `-d, --directory`: Path to the directory containing C source files
- `-o, --output`: Output PDF filename

## Project Structure

```
.
├── README.md
├── requirements.txt
└── src/
    ├── __init__.py
    ├── main.py
    ├── cli.py
    ├── pdf_generator.py
    └── utils.py
```

## License

This project is open source and available under the MIT License.

## Contributing

Contributions, issues, and feature requests are welcome!
