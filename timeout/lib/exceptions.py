#!/usr/bin/env python3

"""Contains custom exceptions with additional functionality."""

import logging
from typing import Callable, Optional


class LogException(Exception):
    """Custom exception for logging exceptions before being raised."""

    def __init__(self, message: str, log: Callable = logging.getLogger().error) -> None:
        """Initialize.

        :param message: message to log
        :param log: logger callable
        """
        log(message)
        super().__init__(message)


class TimeoutExceededError(LogException):
    """Custom exception for logging and raising an exception when a timeout occurs."""

    def __init__(self, function_name: Optional[str], timeout: int) -> None:
        """Initialize.

        :param function_name: name of function
        :param timeout: timeout in seconds
        """
        message = f"Function '{function_name}' experienced a timeout error; exceeded '{timeout}' seconds."
        super().__init__(message)
