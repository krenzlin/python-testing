def mean(list_of_numbers):
    """
    Return mean of a list of numbers.

    >>> mean([20, 40])
    30
    """
    return sum(list_of_numbers) / len(list_of_numbers)

if __name__ == '__main__':
    print mean([10, 20]), 'should be 15'
    print mean([100, 300]), 'should be 200'
