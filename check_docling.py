try:
    import docling
    print("Docling is installed!")
except ImportError as e:
    print(f"Docling not found: {e}")
except Exception as e:
    print(f"Error importing docling: {e}")
