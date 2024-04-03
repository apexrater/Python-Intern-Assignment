# Task A: Fetching Users and Posts Data

## Objective

My objective in Task A was to fetch users' data from an external API and their corresponding posts data asynchronously, then store it in a database.

## Functional Requirements

1. **Login to the website and create your app_id**: I obtained an app ID from the website to access the APIs.
2. **Fetch Users data**: Using the API (https://dummyapi.io/data/v1/user) asynchronously, I fetched users' data and stored it in a table named "users" in the database.
3. **Fetch users list from Database**: I asynchronously retrieved the users' list from the database.
4. **Fetch users' corresponding posts data**: For each user, I used the API (https://dummyapi.io/data/v1/user/{{user_id}}/post) asynchronously and stored the posts data in the database.

## Implementation Details

- I utilized the provided API to fetch users' data and posts data asynchronously.
- Employing asynchronous programming techniques such as async/await, I optimized API calls and database operations.
- To store the data, I used a database of choice (e.g., MongoDB, PostgreSQL).
- Ensuring proper authentication, I used the obtained app ID in API requests.
- Following standard coding practices and naming conventions, I maintained clear and maintainable code.

# Task B: Scraping Books Data

## Objective

In Task B, my objective was to scrape books data from a website (http://books.toscrape.com) asynchronously and store it in a database.

## Functional Requirements

1. **Scrape books attributes**: I asynchronously scraped attributes like name, price, availability, and ratings from all 50 pages of the website.
2. **Store data in Database**: Asynchronously, I stored the scraped data in a database.

## Implementation Details

- I employed web scraping techniques to extract book attributes asynchronously from each page of the website.
- Implementing pagination logic, I asynchronously scraped data from all 50 pages.
- To store the scraped data, I asynchronously implemented a database storage mechanism, ensuring appropriate data modeling and schema design.

## Evaluation Criteria

- **Good Code Quality**: My code was well-structured, readable, and followed best practices.
- **Good Code Structure**: I organized the code into modular components with clear separation of concerns.
- **Standard Naming Conventions**: I followed standard naming conventions for variables, functions, and classes.
- **Logic Used**: Employing efficient and logical algorithms, I achieved the desired functionality.
