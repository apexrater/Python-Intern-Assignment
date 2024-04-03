import aiohttp
from mongodb import db
from bson import ObjectId
import logging

logger = logging.getLogger(__name__)

async def fetch_users():
    """
    Fetch users' data from an API asynchronously.

    Returns:
        list: A list of users' data.
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://dummyapi.io/data/v1/user", headers={'app-id': '660d41cab9b4011214dff1eb'}) as response:
                response.raise_for_status()  # Raise an exception for HTTP errors
                data = await response.json()
                logger.info("Fetched users data from API")
                return data["data"]
    except Exception as e:
        logger.error(f"Error fetching users data: {e}")
        return []

async def insert_users(users_data):
    """
    Insert users' data into the database asynchronously.

    Args:
        users_data (list): A list of users' data to insert into the database.

    Returns:
        None
    """
    try:
        for user in users_data:
            user["_id"] = user.pop("id")  # Rename 'id' to '_id'
            oid_str = user["_id"]
            user["_id"] = ObjectId(oid_str)  # Convert string id to ObjectId

        await db.User.insert_many(users_data)
        logger.info("Inserted users data into database")
    except Exception as e:
        logger.error(f"Error inserting users data into database: {e}")
