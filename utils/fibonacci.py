def fibonacci_until(upper_limit):
    previous_element, current_element = 0, 1
    while True:
        if current_element > upper_limit:
            break
        yield current_element
        previous_element, current_element = current_element, previous_element + current_element
