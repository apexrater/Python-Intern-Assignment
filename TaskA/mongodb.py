import logging
from motor.motor_asyncio import AsyncIOMotorClient

logger = logging.getLogger(__name__)

# MongoDB connection URL
MONGODB_URL = "mongodb+srv://rawatkushagra252:UBBHCAPbbACbfxk7@cluster0.s37xsax.mongodb.net/"

# Function to connect to MongoDB
def connect_to_mongodb():
    try:
        # Connect to MongoDB
        client = AsyncIOMotorClient(MONGODB_URL)
        logger.info("Connected to MongoDB")
        return client
    except Exception as e:
        logger.error(f"Error connecting to MongoDB: {e}")
        return None

# Connect to MongoDB
client = connect_to_mongodb()

# Select database
if client:
    db = client["TaskA"]
else:
    db = None
