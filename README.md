# Expense Tracker Telegram Bot

This is a Telegram bot that helps users track their expenses and generate various reports based on categories, totals, and individual expenses. It uses MongoDB to store the expense data and allows users to interact with the bot through various commands.

## Features

- **Add Expense**: Users can add their expenses with details such as amount, category, and description.
- **View Expenses**: Users can view their expenses, optionally filtered by category.
- **View Categories**: Users can see the different categories of expenses they've recorded.
- **Total Expense**: Users can view the total amount they have spent.
- **Total Expense by Category**: Users can view the total expenses per category.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/hopedeveloper08/expense_tracker
    cd expense_tracker
    ```

2. **Install dependencies**:
    Install the required Python packages by running:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up MongoDB**:
    - Ensure that MongoDB is installed and running on your local machine or a remote server.
    - If running locally, the bot will connect to MongoDB on `localhost` with port `27017` by default.

4. **Create your Telegram Bot**:
    - Create a new bot on Telegram by talking to [BotFather](https://core.telegram.org/bots#botfather).
    - Copy the token provided by BotFather.

5. **Set the token**:
    - In the `get_token.py` file, set the `TOKEN` variable to your bot's token.

6. **Run the bot**:
    After configuring the token and ensuring MongoDB is running, start the bot with:
    ```bash
    python bot.py
    ```

## Commands

- **/start**: Start the bot and receive a greeting message.
- **/add_expense <amount> <category> <description>**: Add an expense entry with the specified amount, category, and description.
    - Example: `/add_expense 500 Food Lunch at a cafe`
- **/get_expenses [category]**: Retrieve a list of all expenses, optionally filtered by a category.
    - Example: `/get_expenses Food`
- **/get_categories**: Retrieve all the categories of expenses recorded by the user.
- **/get_total**: Get the total expenses recorded by the user.
- **/get_total_by_category**: Get the total expenses for each category.

## Code Structure

- **`db.py`**: Contains the `ExpenseMongoClient` class that interacts with MongoDB to store and retrieve expenses.
- **`bot.py`**: Contains the logic for the Telegram bot, including the commands and handlers.
- **`get_token.py`**: Stores the Telegram Bot API token.

## Example Usage

Once the bot is running, you can interact with it through Telegram by sending commands. For instance, to add an expense:

1. Send the command `/add_expense 1000 Entertainment Movie ticket`.
2. To check your expenses, send `/get_expenses`.
3. To check the total expenses by category, send `/get_total_by_category`.
