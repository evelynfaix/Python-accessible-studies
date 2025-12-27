# scraper_example.py - simple page title and headings extractor
import requests
from bs4 import BeautifulSoup

def extract_title_and_headings(url):
    r = requests.get(url, timeout=10)
    if r.status_code != 200:
        print('Error fetching page', r.status_code)
        return
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.title.string if soup.title else 'No title'
    headings = [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2'])]
    print('Title:', title)
    for h in headings:
        print('Heading:', h)

if __name__ == '__main__':
    url = input('Enter URL to scrape: ').strip()
    if url:
        extract_title_and_headings(url)
    else:
        print('No URL provided')
