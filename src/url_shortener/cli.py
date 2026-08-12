import argparse
import sys
from shortener import shorten_url

def main():
    parser = argparse.ArgumentParser(description="Shorten long URLs via CLI.")
    parser.add_argument("url", nargs="?", help="The long URL to shorten")
    parser.add_argument("--api-key", help="Bitly API key (if using Bitly)")
    parser.add_argument("--provider", choices=["tinyurl", "bitly"], default="tinyurl", help="Service provider")

    args = parser.parse_args()

    target_url = args.url
    if not target_url:
        target_url = input("Enter URL to shorten: ").strip()

    if not target_url:
        print("Error: No URL provided.", file=sys.stderr)
        input("\nPress Enter to exit...")
        sys.exit(1)

    try:
        short_url = shorten_url(target_url, api_key=args.api_key, provider=args.provider)
        print(f"Shortened URL: {short_url}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
    finally:
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()