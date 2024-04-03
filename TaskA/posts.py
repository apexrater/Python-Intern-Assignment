import aiohttp
from mongodb import db
import logging

logger = logging.getLogger(__name__)

async def fetch_posts(user_id):
    """
    Fetch posts' data for a specific user from an API asynchronously.

    Args:
        user_id (str): The ID of the user for which to fetch posts.

    Returns:
        list: A list of posts' data.
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://dummyapi.io/data/v1/user/{user_id}/post", headers={'app-id': '660d41cab9b4011214dff1eb'}) as response:
                response.raise_for_status()  # Raise an exception for HTTP errors
                data = await response.json()
                logger.info(f"Fetched posts data from API for user {user_id}")
                return data["data"]
    except Exception as e:
        logger.error(f"Error fetching posts data for user {user_id}: {e}")
        return []

async def populate_posts(user_id, posts_data):
    """
    Populate a user with their posts in the database asynchronously.

    Args:
        user_id (str): The ID of the user to populate with posts.
        posts_data (list): A list of posts' data to populate.

    Returns:
        None
    """
    try:
        # Check if a document with the specified user_id exists
        existing_doc = await db.Post.find_one({'_id': user_id})
        if existing_doc:
            # If document exists, update it with posts_data
            await db.Post.update_one({'_id': user_id}, {"$set": {"posts": posts_data}})
            logger.info(f"Updated user {user_id} with posts")
        else:
            # If document doesn't exist, insert a new document with user_id and posts_data
            await db.Post.insert_one({'_id': user_id, 'posts': posts_data})
            logger.info(f"Inserted posts for user {user_id}")
    except Exception as e:
        logger.error(f"Error populating posts for user {user_id}: {e}")

