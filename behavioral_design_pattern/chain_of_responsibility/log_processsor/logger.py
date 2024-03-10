from behavioral_design_pattern.chain_of_responsibility.log_processsor.log_processor import DebugLogProcessor, \
    InfoLogProcessor, WarningLogProcessor, ErrorLogProcessor


class Logger:
    def __init__(self):
        error_log_processor = ErrorLogProcessor()
        warning_log_processor = WarningLogProcessor(error_log_processor)
        info_log_processor = InfoLogProcessor(warning_log_processor)
        debug_log_processor = DebugLogProcessor(info_log_processor)
        self._logger = debug_log_processor

    def get_logger(self):
        return self._logger
