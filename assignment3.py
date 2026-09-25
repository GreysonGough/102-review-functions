def isPerfectSquare(number):
    if number > 0 and number ** 0.5 == int(number**0.5):
        return True
    else:
        return False
        