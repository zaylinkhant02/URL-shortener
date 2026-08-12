import pyshorteners

def shorten_url(url: str, api_key: str = None, provider: str = "tinyurl") -> str:
    if provider.lower() == "bitly":
        if not api_key:
            raise ValueError("Bitly requires an API key.")
        s = pyshorteners.Shortener(api_key=api_key)
        return s.bitly.short(url)
    else:
        s = pyshorteners.Shortener()
        return s.tinyurl.short(url)