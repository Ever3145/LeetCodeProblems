def finalValueAfterOperations(operations):
    X = 0

    for operator in operations:
        if operator == '--X' or operator == 'X--':
            X -=  1
        else:
            X += 1
    return X
