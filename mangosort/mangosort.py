def sort_by_key(my_list=[], keys=[]):
    """
    Reorder your list ASC/DESC based on multiple keys

    Parameters:
        :param (list) my_list: list of objects you want to order
            [{'code': 'beta', 'number': 3}, {'code': 'delta', 'number': 2}]

        :param (list) keys: list of keys and direction to order.
            eg: [{'code': True'}, {'number': False}]

    Returns:
        :return (list) my_list: your list reordered
    """

    if keys:
        first = keys[0]
        remaining = keys[1:]

        current_key = list(first.keys())[0]
        first_value = list(first.values())[0]

        presorted_list = sort_by_key(my_list, remaining)

        return sorted(presorted_list, key=lambda row: row[current_key], reverse=first_value)
    else:
        return my_list


def sort_by_key_desc(my_list=[], keys=[]):
    """
    Reorder your list DESC based on multiple keys

    Parameters:
        :param (list) my_list: list of objects you want to order
            [{'code': 'beta', 'number': 3}, {'code': 'delta', 'number': 2}]

        :param (list) keys: list of keys and direction to order.
            eg: ['code', 'number']

    Returns:
        :return (list) my_list: your list reordered
    """

    if keys:
        first = keys[0]
        remaining = keys[1:]

        presorted_list = sort_by_key_desc(my_list, remaining)

        return sorted(presorted_list, key=lambda row: row[first], reverse=True)
    else:
        return my_list


def sort_by_key_asc(my_list=[], keys=[]):
    """
    Reorder your list ASC based on multiple keys

    Parameters:
        :param (list) my_list: list of objects you want to order
            [{'code': 'beta', 'number': 3}, {'code': 'delta', 'number': 2}]

        :param (list) keys: list of keys and direction to order.
            eg: ['code', 'number']

    Returns:
        :return (list) my_list: your list reordered
    """

    if keys:
        first = keys[0]
        remaining = keys[1:]

        presorted_list = sort_by_key_asc(my_list, remaining)

        return sorted(presorted_list, key=lambda row: row[first], reverse=False)
    else:
        return my_list
