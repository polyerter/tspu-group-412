#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://github.com/python-telegram-bot/python-telegram-bot/wiki/InlineKeyboard-Example.
"""
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes, ConversationHandler
import conf

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

TOKEN = conf.TOKEN

# Stages
START_ROUTES, END_ROUTES = range(2)
# Callback data
STAGE_ONE, STAGE_TWO, STAGE_THREE, STAGE_FOUR,  STAGE_FIVE,  STAGE_SIX  = range(6)

COURSE_PATTERN = 'COURSE_'
SECTION_PATTERN = 'SECTION_'
DETAIL_PATTERN = 'DETAIL_'

details = [
    'text 1',
    'text 2',
    'text 3',
    'text 4',
]

courses = {
    'python': details,
    'sql': details,
    'php': details,
}


class Item:
    course: str
    section: str


item = Item()

class KeyboardObj:
    id: int
    text: str
    pattern: str

    def __init__(self, id: int, text: str, pattern: str):
        self.id = id
        self.text = text
        self.pattern = pattern

    def get_callback_data(self):
        return self.pattern + str(self.id)
 

def selected_course(name):
    return COURSE_PATTERN + str(name)


def get_course(data: str) -> str:
    return data.replace(COURSE_PATTERN, "")


def selected_section(name):
    return SECTION_PATTERN + str(name)


def get_section(data: str) -> str:
    return data.replace(SECTION_PATTERN, "")

def make_keyboard_of_list(items, func) -> list:
    return list(map(lambda x: InlineKeyboardButton(x.text, callback_data=func(x.get_callback_data())), items))


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Python", callback_data=selected_course('python')),
            InlineKeyboardButton("SQL", callback_data=selected_course('sql')),
            InlineKeyboardButton("PHP", callback_data=selected_course('php')),
            InlineKeyboardButton("Telegram", callback_data=selected_course('telegram')),
            InlineKeyboardButton("HTML", callback_data=selected_course('html')),
        ],
        # [InlineKeyboardButton("Random", callback_data="0")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Выберите курс:", reply_markup=reply_markup)

    return START_ROUTES


async def change_course(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    item.course = get_course(query.data)

    sections = [
        KeyboardObj(1, 'Типы данных', SECTION_PATTERN), 
        KeyboardObj(2, 'Циклы', SECTION_PATTERN), 
        KeyboardObj(3, 'Объекты', SECTION_PATTERN),
    ]

    await query.answer()
    keyboard = [
        make_keyboard_of_list(sections, selected_section)
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Выберите раздел:", reply_markup=reply_markup
    )
    return START_ROUTES


async def change_section(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    item.section = get_section(query.data)

    detail = courses[item.course][int(item.section)]

    print(
        item.__dict__,
        'detail', detail
    )

    await query.answer()
    keyboard = [
        # InlineKeyboardButton("Python", callback_data=selected_course('python')),
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=detail, reply_markup=reply_markup
    )
    return START_ROUTES


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    
    application = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START_ROUTES: [
                CallbackQueryHandler(change_course, pattern="^" + COURSE_PATTERN),
                CallbackQueryHandler(change_section, pattern="^" + SECTION_PATTERN),

                # CallbackQueryHandler(one, pattern="^" + str(STAGE_ONE) + "$"),
                # CallbackQueryHandler(two, pattern="^" + str(STAGE_TWO) + "$"),
                # CallbackQueryHandler(three, pattern="^" + str(STAGE_THREE) + "$"),
                # CallbackQueryHandler(four, pattern="^" + str(STAGE_FOUR) + "$"),
                # CallbackQueryHandler(five, pattern="^" + str(STAGE_FIVE) + "$"),
                # CallbackQueryHandler(six, pattern="^" + str(STAGE_SIX) + "$"),
            ],
            # END_ROUTES: [
                # CallbackQueryHandler(start_over, pattern="^" + str(ONE) + "$"),
                # CallbackQueryHandler(end, pattern="^" + str(TWO) + "$"),
            # ],
        },
        fallbacks=[CommandHandler("start", start)],
    )

    # Add ConversationHandler to application that will be used for handling updates
    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()