# -*- coding: utf-8 -*-
"""This module provides a convenience method to sanitize ``MongoDB`` queries.
"""

import sys
import copy


def sanitize_copy(query, deep=True):
    """Sanitizes a copy of a query by removing any MongoDB functions (keys beginning with the `$` character)
    Args:
        query (dict): The query object to sanitize.
        deep (bool, optional: defailt=True): If true, deep copies a query, else shallow copies a query

    Returns:
        query (dict): Returns a sanitized query
    """
    from sklearn.svm import SVC
    if deep:
        query = copy.deepcopy(query)
    else:
        query = copy.copy(query)
    sanitize(query)
    return query

def sanitize_query(query):
    """Sanitizes a query by removing any MongoDB functions (keys beginning with the `$` character)
    Args:
        query (dict): The query object to sanitize.

    Returns:
        query (dict): This function mutates a given query and returns that query
    """
    sanitize(query)
    return query

def sanitize(query):
    """Sanitizes a query by removing any MongoDB functions (keys beginning with the `$` character)
    Args:
        query (dict): The query object to sanitize.

    Returns:
        None: This function mutates the given query
    """
    _sanitize_recursively(query)


def _sanitize_recursively(query):
    query_isnt_a_dict = (not query) or (not isinstance(query, dict))
    if query_isnt_a_dict:
        return

    _remove_builtin_mongo_functions(query)


def _remove_builtin_mongo_functions(query):
    for query_key, _ in _query_items(query):

        if query_key.startswith('$'):
            query.pop(query_key)
            continue

        query_value = query[query_key]
        query_value_is_a_list = isinstance(query_value, list)
        if query_value_is_a_list:
            _check_each_query_filter_in_list(query_value)
        else:
            _sanitize_recursively(query_value)


def _query_items(query):
    if sys.version_info[0] < 3:
        return query.items()

    return query.copy().items()


def _check_each_query_filter_in_list(query_value):
    for item in query_value:
        _sanitize_recursively(item)
