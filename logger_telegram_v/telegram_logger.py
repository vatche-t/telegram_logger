from loguru import logger
import telegram
from functools import wraps

def telegram_logger(token, chat_ids):
    def decorator(func):
        bot = telegram.Bot(token=token)

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                logger.info(result)
                for chat_id in chat_ids:
                    bot.send_message(chat_id=chat_id, text=str(result))
                return result
            except Exception as e:
                logger.exception(e)
                for chat_id in chat_ids:
                    bot.send_message(chat_id=chat_id, text=str(e))
                raise

        return wrapper

    return decorator