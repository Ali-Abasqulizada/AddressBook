def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
