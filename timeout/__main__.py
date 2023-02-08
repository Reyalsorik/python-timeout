#!/usr/bin/env python3

"""Contains the logic for handling a timeout."""

import signal
from functools import wraps
from types import FrameType
from typing import Callable, Optional

from timeout.lib.exceptions import TimeoutExceededError


class Timeout(object):
    """Responsible for handling a timeout."""

    def __init__(self, timeout: int) -> None:
        """Initialize.

        :param timeout: timeout in seconds
        """
        self.timeout = timeout
        self.function = None

    def __call__(self, function, *args, **kwargs) -> Callable:
        """Callable.

        :param function: function to wrap
        """
        @wraps(function)
        def _wrapper(*_args, **_kwargs) -> Callable:
            """Wrap function."""
            self.function = function.__name__
            signal.signal(signal.SIGALRM, self._handler)
            signal.alarm(self.timeout)
            results = function(*_args, **_kwargs)
            signal.alarm(0)
            return results
        return _wrapper

    def _handler(self, signum: int, frame: Optional[FrameType], *args, **kwargs) -> None:
        """Alarm handler.

        :param signum: signal number
        :param frame: frame to handle
        """
        raise TimeoutExceededError(self.function, self.timeout)
