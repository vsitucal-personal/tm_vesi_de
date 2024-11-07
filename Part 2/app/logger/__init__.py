import logging
import sys
import os


class Logger:
    """
    Logger class
    """

    logger = None
    logger_name = None
    handler = None

    @classmethod
    def get_logger(
        cls,
        log_level=os.getenv("LOG_LEVEL", "INFO"),
        logger_name='Logger',
        propagate_log=False
    ):
        """
        Creates a logger instance for python logging.
        :param log_level: Log level
        :param logger_name: Logger name
        :param propagate_log: propagates log
        :return cls.logger: The previously created instance if
        an instance has already been created.
        """

        if not cls.logger:
            logger = logging.getLogger(logger_name)
            handler = logging.StreamHandler(sys.stdout)

            log_format = '[%(asctime)s][%(module)s][%(levelname)s]' \
                         '[%(funcName)s]: %(message)s'
            date_format = '%Y-%m-%d %H:%M:%S'

            log_formatter = logging.Formatter(log_format,
                                              datefmt=date_format)
            handler.setFormatter(log_formatter)

            logger.propagate = propagate_log
            logger.addHandler(handler)
            logger.setLevel(log_level)

            cls.logger_name = logger_name
            cls.logger = logger
            cls.handler = handler

        return cls.logger

    @classmethod
    def destroy_logger(cls):
        """
        Destroy the logger instance
        :return: None
        """

        if cls.logger:
            cls.handler.flush()
            cls.handler.close()
            root_logger = logging.getLogger(cls.logger_name)
            for handle in root_logger.handlers:
                handle.close()
                root_logger.removeHandler(handle)
            cls.logger = None
            cls.logger_name = None
