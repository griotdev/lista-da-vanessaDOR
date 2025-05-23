"""Test module for PDF generator functionality."""
import os
import tempfile
from typing import TYPE_CHECKING

import pytest
from fpdf import FPDF

from src.services.pdf_generator import CustomPDF, create_exercises_pdf

if TYPE_CHECKING:
    from _pytest.capture import CaptureFixture
    from _pytest.fixtures import FixtureRequest
    from _pytest.logging import LogCaptureFixture
    from _pytest.monkeypatch import MonkeyPatch
    from pytest_mock.plugin import MockerFixture


class TestCustomPDF:
    """Test cases for CustomPDF class."""

    def test_footer_creation(self) -> None:
        """Test that footer is properly created with repository information."""
        pdf = CustomPDF()
        pdf.add_page()
        pdf.footer()
        
        # Verify PDF was created without errors
        assert pdf.page_no() == 1

    def test_wrap_text_to_lines_short_text(self) -> None:
        """Test text wrapping with text that fits in one line."""
        pdf = CustomPDF()
        pdf.add_page()
        pdf.set_font("Courier", size=10)
        
        text = "short line"
        max_width = 100.0
        
        wrapped_lines = pdf.wrap_text_to_lines(text, max_width)
        
        assert len(wrapped_lines) == 1
        assert wrapped_lines[0] == "short line"

    def test_wrap_text_to_lines_long_text(self) -> None:
        """Test text wrapping with text that needs multiple lines."""
        pdf = CustomPDF()
        pdf.add_page()
        pdf.set_font("Courier", size=10)
        
        # Create a long line that will definitely need wrapping
        text = "this is a very long line of code that should definitely be wrapped when it exceeds the maximum width"
        max_width = 50.0  # Small width to force wrapping
        
        wrapped_lines = pdf.wrap_text_to_lines(text, max_width)
        
        assert len(wrapped_lines) > 1
        # Verify all original words are preserved
        original_words = text.split()
        wrapped_words = " ".join(wrapped_lines).split()
        assert original_words == wrapped_words

    def test_wrap_text_to_lines_empty_text(self) -> None:
        """Test text wrapping with empty text."""
        pdf = CustomPDF()
        pdf.add_page()
        pdf.set_font("Courier", size=10)
        
        text = ""
        max_width = 100.0
        
        wrapped_lines = pdf.wrap_text_to_lines(text, max_width)
        
        assert len(wrapped_lines) == 1
        assert wrapped_lines[0] == ""

    def test_wrap_text_to_lines_single_long_word(self) -> None:
        """Test text wrapping with a single word that exceeds max width."""
        pdf = CustomPDF()
        pdf.add_page()
        pdf.set_font("Courier", size=10)
        
        text = "verylongwordthatexceedsmaxwidth"
        max_width = 10.0  # Very small width
        
        wrapped_lines = pdf.wrap_text_to_lines(text, max_width)
        
        assert len(wrapped_lines) == 1
        assert wrapped_lines[0] == text  # Should keep the long word as is


class TestCreateExercisesPDF:
    """Test cases for create_exercises_pdf function."""

    def test_create_pdf_nonexistent_directory(self, capsys: "CaptureFixture[str]") -> None:
        """Test PDF creation with non-existent directory."""
        result = create_exercises_pdf("/nonexistent/path", "output.pdf")
        
        assert result is False
        captured = capsys.readouterr()
        assert "does not exist" in captured.out

    def test_create_pdf_with_c_files(self) -> None:
        """Test PDF creation with actual C files."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a test C file with long lines
            test_file_path = os.path.join(temp_dir, "test.c")
            test_content = """#include <stdio.h>

int main() {
    // This is a very long comment that should definitely be wrapped when it exceeds the maximum width available in the PDF
    printf("This is also a very long printf statement that contains multiple arguments and should be wrapped properly");
    return 0;
}"""
            
            with open(test_file_path, 'w', encoding='utf-8') as f:
                f.write(test_content)
            
            output_file = os.path.join(temp_dir, "test_output.pdf")
            
            result = create_exercises_pdf(temp_dir, output_file)
            
            assert result is True
            assert os.path.exists(output_file)
            assert os.path.getsize(output_file) > 0

    def test_create_pdf_empty_directory(self) -> None:
        """Test PDF creation with directory containing no C files."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a non-C file
            test_file_path = os.path.join(temp_dir, "test.txt")
            with open(test_file_path, 'w', encoding='utf-8') as f:
                f.write("This is not a C file")
            
            output_file = os.path.join(temp_dir, "test_output.pdf")
            
            result = create_exercises_pdf(temp_dir, output_file)
            
            assert result is True
            assert os.path.exists(output_file)

    def test_create_pdf_with_encoding_issues(self, mocker: "MockerFixture") -> None:
        """Test PDF creation when file reading encounters encoding issues."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a test C file
            test_file_path = os.path.join(temp_dir, "test.c")
            with open(test_file_path, 'w', encoding='utf-8') as f:
                f.write("int main() { return 0; }")
            
            # Mock file reading to raise an exception
            mock_open = mocker.mock_open()
            mock_open.side_effect = UnicodeDecodeError('utf-8', b'', 0, 1, 'invalid start byte')
            
            with mocker.patch('builtins.open', mock_open):
                output_file = os.path.join(temp_dir, "test_output.pdf")
                result = create_exercises_pdf(temp_dir, output_file)
                
                assert result is True  # Should still succeed and create PDF

    def test_create_pdf_with_very_long_lines(self) -> None:
        """Test PDF creation with C files containing very long lines."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a test C file with extremely long lines
            test_file_path = os.path.join(temp_dir, "long_lines.c")
            long_line = "printf(" + "\"This is an extremely long string that should definitely be wrapped across multiple lines when rendered in the PDF because it exceeds the available width by a significant margin and contains many words that need to be properly distributed across lines\"" + ");"
            test_content = f"""#include <stdio.h>

int main() {{
    {long_line}
    // {" ".join(["word"] * 50)}  // Very long comment
    return 0;
}}"""
            
            with open(test_file_path, 'w', encoding='utf-8') as f:
                f.write(test_content)
            
            output_file = os.path.join(temp_dir, "test_output.pdf")
            
            result = create_exercises_pdf(temp_dir, output_file)
            
            assert result is True
            assert os.path.exists(output_file)
            assert os.path.getsize(output_file) > 0