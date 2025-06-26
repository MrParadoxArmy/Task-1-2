import argparse
from main import analyze_password
from wordlist import generate_wordlist

# Rest of your existing menu.py code...

def main():
    parser = argparse.ArgumentParser(description="Password Strength Analyzer + Wordlist Generator")
    subparsers = parser.add_subparsers(dest="command", help="Choose a mode")

    # Password analyzer mode
    analyze_parser = subparsers.add_parser("analyze", help="Check password strength")
    analyze_parser.add_argument("password", help="Password to analyze")

    # Wordlist generator mode
    wordlist_parser = subparsers.add_parser("generate", help="Generate a wordlist")
    wordlist_parser.add_argument("-k", "--keywords", required=True, help="Comma-separated base keywords (e.g., 'admin,test')")
    wordlist_parser.add_argument("-s", "--suffixes", required=True, help="Comma-separated suffixes (e.g., '123,!')")
    wordlist_parser.add_argument("-p", "--prefixes", help="Comma-separated prefixes (e.g., 'my,super')")
    wordlist_parser.add_argument("-o", "--output", default="wordlist.txt", help="Output filename")

    args = parser.parse_args()

    if args.command == "analyze":
        strength, feedback = analyze_password(args.password)
        print(f"Password Strength: {strength}")
        if feedback:
            print("Suggestions:")
            for item in feedback:
                print(f"- {item}")
    elif args.command == "generate":
        keywords = [k.strip() for k in args.keywords.split(",")]
        suffixes = [s.strip() for s in args.suffixes.split(",")]
        prefixes = [p.strip() for p in args.prefixes.split(",")] if args.prefixes else []
        generate_wordlist(keywords, suffixes, prefixes, args.output)
        print(f"[+] Wordlist saved to '{args.output}'")

if __name__ == "__main__":
    main()