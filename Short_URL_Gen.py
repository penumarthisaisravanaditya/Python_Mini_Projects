# pip install pyshorteners
import pyshorteners
long_url = input("Enter the URL to shorten: ")
shortener = pyshorteners.Shortener()
short_url = shortener.tinyurl.short(long_url)
print(f"Shortened URL is: {short_url}")