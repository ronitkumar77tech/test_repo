import re
import unicodedata

def slugify(text: str) -> str:
    """Convert arbitrary text into a clean, URL-safe slug.
    
    Example: 'Hello World! 2026' -> 'hello-world-2026'
    """
    if not text or not isinstance(text, str):
        return ""
    
    # Normalize unicode characters to ASCII
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
    # Remove non-alphanumeric characters
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    # Replace whitespace and repeated dashes with a single dash
    return re.sub(r'[-\s]+', '-', text)
