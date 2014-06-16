# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Copyright (C) 2013 Yahoo! Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


class EntropyException(Exception):
    """Base class for exceptions emitted from entropy."""
    def __init__(self, message):
        super(EntropyException, self).__init__(message)


class TimeoutException(EntropyException):
    """Exceptions because of timeouts, eg. when the job queue has been empty
    really long.
    """
    def __init__(self, message):
        super(TimeoutException, self).__init__(message)


class EngineStoppedException(EntropyException):
    """Exception raised when engine is shutdown."""
    def __init__(self, message):
        super(EngineStoppedException, self).__init__(message)


class NoSuchEngineException(EntropyException):
    """Exception raised when performing operations on a non-existent engine.
    """
    def __init__(self, message):
        super(NoSuchEngineException, self).__init__(message)


class NoEnginesException(EntropyException):
    """Exception raised when there are no known engines."""
    def __init__(self, message):
        super(NoEnginesException, self).__init__(message)
