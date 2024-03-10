from log_processsor.constants import LogLevel
from log_processsor.logger import Logger

if __name__ == "__main__":
    log = Logger().get_logger()
    log.log(LogLevel.DEBUG.value, "We are logging debug log")
    log.log(LogLevel.INFO.value, "We are logging info log")
    log.log(LogLevel.WARNING.value, "We are logging warning log")
    log.log(LogLevel.ERROR.value, "We are logging error log")
