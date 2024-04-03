import asyncio
import logging
import users
import posts
from mongodb import client, db

logging.basicConfig(level=logging.INFO)

async def task():
    
    logging.info("Inside task of taskA")

    # Fetch users' data from API asynchronously
    user_data = await users.fetch_users()

    # Insert users' data into database asynchronously
    await users.insert_users(user_data)

    # Fetch all user IDs from the database
    user_cursor = db.User.find({}, projection={"_id": 1})
    user_ids = [user["_id"] async for user in user_cursor]

    # Fetch posts for each user in parallel (using asynchronous operations)
    tasks = [posts.fetch_posts(user_id) for user_id in user_ids]
    posts_data = await asyncio.gather(*tasks)

    # Populate users in database with fetched posts asynchronously
    for user_id, post_data in zip(user_ids, posts_data):
        await posts.populate_posts(user_id, post_data)

    logging.info("Task completed successfully")

if __name__ == "__main__":
    asyncio.run(task())
