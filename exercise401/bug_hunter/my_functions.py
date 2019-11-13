def boxes_required(qty, box_capacity=6):
    """
    Calculate how many egg boxes will be required for a given quatity of eggs.
    :param qty: Number of eggs
    :param box_capacity: How many eggs will fit in a box
    :return: The number of boxes that are required
    """
    reminder = qty % box_capacity
    extra = 0 if reminder == 0 else 1
    return int((qty - reminder) / box_capacity) + extra
