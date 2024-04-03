import aiohttp
from bs4 import BeautifulSoup

async def fetch_page(session, url):
    async with session.get(url) as response:
        return await response.text()

async def scrape_books_page(session, page_number):
    url = f"https://books.toscrape.com/catalogue/page-{page_number}.html"
    async with session.get(url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        books = soup.find("section").find(class_="row").find_all("li")
        return [extract_book_data(book) for book in books]

def extract_book_data(book):
    return {
        "title": book.find("h3").find("a").get("title"),
        "price": book.find(class_="product_price").find(class_="price_color").text.strip()[1:],
        "availability": book.find(class_="availability").text.strip(),
        "rating": book.find("p").get("class")[1],
        "image_url": "https://books.toscrape.com" + book.find("img").get("src")[2:]
    }
