import asyncio
import aiohttp
import scrape_books
import mongodb

async def scrape_books_and_store():
    async with aiohttp.ClientSession() as session:
        db = mongodb.connect_to_mongodb()
        tasks = [scrape_books.scrape_books_page(session, page_number) for page_number in range(1, 51)]
        books_data = await asyncio.gather(*tasks)
        await mongodb.insert_books_data(db, [book for page in books_data for book in page])

async def main():
    await scrape_books_and_store()
    print("Scraping and storing of books data completed.")

if __name__ == "__main__":
    asyncio.run(main())
