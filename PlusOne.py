def plusOne(digits):
    ln = len(digits) - 1
    old_int = 0
    result = []
    for i in range(len(digits)):
        old_int += digits[i] * 10 ** (ln - i)
    new_int = old_int + 1
    for dg in str(new_int):
        result.append(int(dg))

    return result
