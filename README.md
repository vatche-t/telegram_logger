# logger-telegram-v
logger-telegram-v is a Python library for sending logs to Telegram. With this library, you can easily integrate logging into your Python applications and have the logs sent directly to a Telegram chat.

## Installation
You can install logger-telegram-v using pip:

```css
pip install logger-telegram-v
```
## Usage
To use logger-telegram-v, you need to first create a Telegram bot and get the bot token. You can follow the instructions here to create a new bot.

Once you have the bot token, you can use the telegram_logger decorator to decorate your functions:

```python
from logger_telegram_v.telegram_logger import telegram_logger

@telegram_logger(token='YOUR_BOT_TOKEN', chat_ids=[CHAT_ID])
def my_function():
    # Your function code here
    pass
```
+ Replace YOUR_BOT_TOKEN with your Telegram bot token and CHAT_ID with the ID of the Telegram chat where you want to receive the logs.

+ You can also specify the log level to send to Telegram by passing the level parameter to the telegram_logger decorator. The possible values are DEBUG, INFO, SUCCESS, and ERROR. If no level is specified, all log levels will be sent.

```python
@telegram_logger(token='YOUR_BOT_TOKEN', chat_ids=[CHAT_ID], level='INFO')
def my_function():
    # Your function code here
    pass
```


Last updated on: 2024-02-14

Last updated on: 2024-02-14

Last updated on: 2024-02-14

Last updated on: 2024-02-19

Last updated on: 2024-02-19

Last updated on: 2024-02-21

Last updated on: 2024-03-01

Last updated on: 2024-03-03

Last updated on: 2024-03-04

Last updated on: 2024-03-06

Last updated on: 2024-03-10

Last updated on: 2024-03-17

Last updated on: 2024-03-24

Last updated on: 2024-04-01

Last updated on: 2024-04-10

Last updated on: 2024-04-12

Last updated on: 2024-04-13

Last updated on: 2024-04-15

Last updated on: 2024-04-30

Last updated on: 2024-04-30

Last updated on: 2024-05-02

Last updated on: 2024-05-03

Last updated on: 2024-05-05

Last updated on: 2024-05-06

Last updated on: 2024-05-08

Last updated on: 2024-12-01

Last updated on: 2024-12-01