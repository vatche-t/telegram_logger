class Logger:
    def __init__(self, api_key, chat_id, log_level):
        self.api_key = api_key
        self.chat_id = chat_id
        self.log_level = log_level

    def debug(self, message):
        pass

    def info(self, message):
        pass

    def success(self, message):
        pass

    def warning(self, message):
        pass

    def error(self, message):
        pass
