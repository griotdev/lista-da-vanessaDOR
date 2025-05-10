"""Utility functions for file handling and sorting."""
import re
from typing import List, Union


def natural_sort_key(s: str) -> List[Union[int, str]]:
    """
    Generate a key for natural sorting of strings containing numbers.
    
    Natural sorting orders items like: 1, 2, 3, 10, 11 instead of 1, 10, 11, 2, 3.
    
    Args:
        s: The string to generate a sort key for
        
    Returns:
        A list of integers and strings that can be used as a sort key
    """
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('([0-9]+)', s)] 