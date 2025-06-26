import itertools

def generate_wordlist(keywords, suffixes, prefixes=[], output_file="wordlist.txt"):
    """
    Generate a custom wordlist from keywords, suffixes, and prefixes.
    Args:
        keywords (list): Base words (e.g., ["admin", "password"]).
        suffixes (list): Common suffixes (e.g., ["123", "!"]).
        prefixes (list): Common prefixes (e.g., ["super", "my"]).
        output_file (str): Output filename.
    """
    with open(output_file, 'w') as f:
        # Generate all combinations
        for keyword in keywords:
            # Add the keyword itself
            f.write(f"{keyword}\n")
            
            # Add keyword + suffix combinations
            for suffix in suffixes:
                f.write(f"{keyword}{suffix}\n")
            
            # Add prefix + keyword combinations
            for prefix in prefixes:
                f.write(f"{prefix}{keyword}\n")
            
            # Add case variations
            f.write(f"{keyword.upper()}\n")      # ADMIN
            f.write(f"{keyword.lower()}\n")      # admin
            f.write(f"{keyword.capitalize()}\n") # Admin
            
            # Advanced: Mix prefixes + keyword + suffixes
            for prefix, suffix in itertools.product(prefixes, suffixes):
                f.write(f"{prefix}{keyword}{suffix}\n")  # e.g., "superadmin123"

if __name__ == "__main__":
    # Example usage with user input
    keywords = input("Enter base keywords (comma-separated): ").strip().split(',')
    suffixes = input("Enter suffixes (comma-separated, e.g., 123,!): ").strip().split(',')
    prefixes = input("Enter prefixes (comma-separated, e.g., my,super): ").strip().split(',')
    
    # Remove empty strings from inputs
    keywords = [k.strip() for k in keywords if k.strip()]
    suffixes = [s.strip() for s in suffixes if s.strip()]
    prefixes = [p.strip() for p in prefixes if p.strip()]
    
    generate_wordlist(keywords, suffixes, prefixes)
    print(f"[+] Wordlist generated as 'wordlist.txt'!")
