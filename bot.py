from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

from db import ExpenseMongoClient
from get_token import TOKEN


db_client = ExpenseMongoClient("localhost", 27017)


async def start_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="سلام من یک ربات برای ثبت مخارج و ارائه گزارش از اونها برات هستم.",
        reply_to_message_id=update.effective_message.id,
    )


async def add_expense_command_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    user_id = update.effective_user.id
    args = context.args
    amount = int(args.pop(0))
    category = args.pop(0)
    description = ' '.join(args)
    db_client.add_expense(user_id=user_id, amount=amount, category=category, description=description)
    text = 'با موفقیت اضافه شد!'
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
        reply_to_message_id=update.effective_message.id
    )


async def get_expenses_command_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    user_id = update.effective_user.id
    if len(context.args) != 0:
        category = context.args[0]
        expenses = db_client.get_expenses_by_category(user_id, category)
    else:
        expenses = db_client.get_expenses(user_id)
    text ="لیست خرج های تو\n"
    for expense in expenses:
        text += (
            f"{expense['amount']} - {expense['category']} - {expense['description']}\n"
        )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
        reply_to_message_id=update.effective_message.id
    )
        

async def get_categories_command_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    user_id = update.effective_user.id
    categories = db_client.get_categories(user_id)
    text = f"دسته بندی های تو: {', '.join(categories)}"
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
        reply_to_message_id=update.effective_message.id
    )


async def get_total_expense_command_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    user_id = update.effective_user.id
    total = db_client.get_total_expense(user_id)
    text = f"کل خرجی که کردی: {int(total)}"
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
        reply_to_message_id=update.effective_message.id
    )
    

async def get_total_expense_by_category_command_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    user_id = update.effective_user.id
    total_expense = db_client.get_total_expense_by_category(user_id)
    text = "کل خرج های تو در دسته بندی های مختلف:\n"
    for category, expense in total_expense.items():
        text += f"{category}: {expense}\n"
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
        reply_to_message_id=update.effective_message.id
    )


if __name__ == "__main__":
    expense_mongo_client = ExpenseMongoClient("localhost", 27017)
    bot = ApplicationBuilder().token(TOKEN).build()

    bot.add_handler(CommandHandler("start", start_command_handler))
    bot.add_handler(CommandHandler('add_expense', add_expense_command_handler))
    bot.add_handler(CommandHandler('get_expenses', get_expenses_command_handler))
    bot.add_handler(CommandHandler('get_categories', get_categories_command_handler))
    bot.add_handler(CommandHandler('get_total', get_total_expense_command_handler))
    bot.add_handler(CommandHandler('get_total_by_category', get_total_expense_by_category_command_handler))

    bot.run_polling()
