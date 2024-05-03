def solve_quadratic_equation(a: int, b: int, c: int) -> list[float]:
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return []
    elif discriminant == 0:
        return [-b / (2 * a)]
    # discriminant > 0
    return [(-b + discriminant ** 0.5) / (2 * a), (-b + discriminant ** 0.5) / (2 * a)]


def solve_quadratic_equation_and_check(a: int, b: int, c: int) -> list[int]:
    solutions = solve_quadratic_equation(a, b, c)
    for solution in solutions:
        if not solution.is_integer():
            return []
        solution = int(solution)
        if a * solution ** 2 + b * solution + c != 0:
            return []
    return solutions
