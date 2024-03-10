from abc import ABC, abstractmethod
from behavioral_design_pattern.chain_of_responsibility.log_processsor.constants import LogLevel


class ILogProcessor(ABC):
    @abstractmethod
    def log(self, log_level: int, msg: str):
        pass


class LogProcessor(ILogProcessor):
    def __init__(self, next_log_processor: ILogProcessor = None):
        self.next_log_processor = next_log_processor

    def log(self, log_level: int, msg: str):
        if self.next_log_processor:
            self.next_log_processor.log(log_level, msg)


class DebugLogProcessor(LogProcessor):
    def __init__(self, next_log_processor: ILogProcessor = None):
        super().__init__(next_log_processor)

    def log(self, log_level: int, msg: str):
        if log_level == LogLevel.DEBUG.value:
            print(f"{LogLevel.DEBUG.name}: ", msg)
        else:
            super().log(log_level, msg)


class InfoLogProcessor(LogProcessor):
    def __init__(self, next_log_processor: ILogProcessor = None):
        super().__init__(next_log_processor)

    def log(self, log_level: int, msg: str):
        if log_level == LogLevel.INFO.value:
            print(f"{LogLevel.INFO.name}: ", msg)
        else:
            super().log(log_level, msg)


class WarningLogProcessor(LogProcessor):
    def __init__(self, next_log_processor: ILogProcessor = None):
        super().__init__(next_log_processor)

    def log(self, log_level: int, msg: str):
        if log_level == LogLevel.WARNING.value:
            print(f"{LogLevel.WARNING.name}: ", msg)
        else:
            super().log(log_level, msg)


class ErrorLogProcessor(LogProcessor):
    def __init__(self, next_log_processor: ILogProcessor = None):
        super().__init__(next_log_processor)

    def log(self, log_level: int, msg: str):
        if log_level == LogLevel.ERROR.value:
            print(f"{LogLevel.ERROR.name}: ", msg)
        else:
            super().log(log_level, msg)
