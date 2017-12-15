# -*- coding: utf-8 -*-

"""WRAPPERS

This module contains wrappers for adding additional features to functions

:Author: Samuel Farrens <samuel.farrens@cea.fr>

:Version: 1.0

:Date: 15/12/2017

"""

from inspect import getargspec


def add_agrs_kwargs(func):
    """Add Args and Kwargs

    This wrapper adds support for additional arguments and keyword arguments to
    any callable function

    Parameters
    ----------
    func : function
        Callable function

    Returns
    -------
    function wrapper

    """

    def wrapper(*args, **kwargs):

        props = getargspec(func)

        if 'args' not in props:

            args = args[:len(props[0])]

        if 'kwargs' in props:

            return func(*args, **kwargs)

        else:

            return func(*args)

    return wrapper
