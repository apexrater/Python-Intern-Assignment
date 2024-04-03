import motor.motor_asyncio

MONGODB_URL = "mongodb+srv://rawatkushagra252:UBBHCAPbbACbfxk7@cluster0.s37xsax.mongodb.net/"

def connect_to_mongodb():
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
    return client['TaskB']

async def insert_books_data(db, books_data):
    books_collection = db['BookCatalog']
    await books_collection.insert_many(books_data)
