import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculates the BMI for each pair of height and weight.

    Parameters:
    - height: List of heights in cm (int or float).
    - weight: List of weights in kg (int or float).

    Returns:
    - List of BMIs (float) for each element.

    Raises:
    - ValueError if the lists have different lengths or contain non-numeric values.
    """
    try:
        if len(height) != len(weight):
            ValueError("Lists must have the same length.")
        if isinstance(height, (int, float)) == False or isinstance(weight, (int, float)) == False:
            ValueError("Values must be int or float.")
        h = np.array(height)
        w = np.array(weight)
        bmi = w / (h ** 2)
        return [float(x) for x in bmi]
    except Exception as error:
        print(error)
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Compares each BMI to a limit and returns a list of booleans.

    Parameters:
    - bmi: List of BMIs (int or float).
    - limit: Threshold value to compare (int).

    Returns:
    - List of booleans, True if BMI >= threshold, otherwise False.

    Raises:
    - ValueError if `bmi` contains non-numeric values or if `limit` is not an integer.
    """
    try:
        if isinstance(bmi, (int, float)) == False or isinstance(limit, (int)) == False:
            ValueError("Values must be int or float.")
        b = np.array(bmi)
        lBool = b >= limit
        return [bool(x) for x in lBool]
    except Exception as error:
        print(error)
        return []
