#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import logging
import traceback
from logging.handlers import RotatingFileHandler


class Log:
    _root = None
    _logger = None

    @staticmethod
    def get():
        # Construct the name of the logger based on the file path
        code_file = traceback.extract_stack()[-2].filename  # Get the file path of the caller
        if Log._root not in os.path.abspath(code_file):
            raise Exception(f'The file calling the method is outside the home directory: "{code_file}"')
        relpath = os.path.relpath(code_file, Log._root).replace('.py', '').replace('/', '.')
        root_name = os.path.basename(Log._root)
        return logging.getLogger(f"{root_name}.{relpath}")

    @staticmethod
    def init(home):
        assert os.path.isdir(home), f'invalid home directory: "{home}"'
        Log._root = os.path.abspath(home)
        log_dir = os.path.join(Log._root, 'logs')
        if not os.path.isdir(log_dir):
            os.mkdir(log_dir)
        Log._configure_root_logger(log_dir)

    @staticmethod
    def filter(name, level):
        level = str.upper(level)
        assert level in {'DEBUG', 'INFO', 'WARNING', 'ERROR'}
        logging.getLogger(name).setLevel(getattr(logging, level))

    @staticmethod
    def _configure_root_logger(log_dir):
        log_fmt = '[%(asctime)s | %(name)s  line %(lineno)s| %(levelname)s]  %(message)s'
        formatter = logging.Formatter(log_fmt, datefmt="%Y/%m/%d %H:%M:%S")

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        log_filepath = os.path.join(log_dir, "rotating.log")
        log_file_handler = RotatingFileHandler(filename=log_filepath, maxBytes=1e5, backupCount=3)
        log_file_handler.setFormatter(formatter)

        root_logger_name = os.path.basename(Log._root)
        root_logger = logging.getLogger(root_logger_name)
        root_logger.addHandler(log_file_handler)
        root_logger.addHandler(stream_handler)
        root_logger.setLevel(logging.DEBUG)  # default level


if __name__ == '__main__':
    import os, time

    log_dir = os.path.dirname(__file__)
    Log.init(log_dir)  # project root directory
    log = Log.get()
    for count in range(20):
        log.info(f"logger count: {count}")
        time.sleep(1)

