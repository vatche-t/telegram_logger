from logging import Logger
import logging


class LoggerHandler(logging.Handler):
    def __init__(self, api_key, chat_id, log_level):
        super().__init__()
        self.logger = Logger(api_key, chat_id, log_level)

    def emit(self, record):
        log_entry = self.format(record)
        if record.levelno >= self.logger.log_level:
            if record.levelno == logging.DEBUG:
                self.logger.debug(log_entry)
            elif record.levelno == logging.INFO:
                self.logger.info(log_entry)
            elif record.levelno == logging.WARNING:
                self.logger.warning(log_entry)
            elif record.levelno == logging.ERROR:
                self.logger.error(log_entry)
            elif record.levelno == logging.CRITICAL:
                self.logger.error(log_entry)
