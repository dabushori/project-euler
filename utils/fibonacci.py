def fibonacci_until(upper_limit: int, return_indexes: bool = False):
    previous_element, current_element = 0, 1
    index = 1
    while True:
        if current_element > upper_limit:
            break

        yield index, current_element if return_indexes else current_element
        previous_element, current_element = current_element, previous_element + current_element
        index += 1


def fibonacci_from(lower_limit: int, return_indexes: bool = False):
    previous_element, current_element = 0, 1
    index = 1
    while True:
        if current_element >= lower_limit:
            yield index, current_element if return_indexes else current_element
        previous_element, current_element = current_element, previous_element + current_element
        index += 1
