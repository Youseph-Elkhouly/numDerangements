def numDerangements(n):
    # Base cases
    if n == 0:
        return 1
    elif n == 1:
        return 0
    # Recursive case: Calculating derangement for current n
    return (n - 1) * (numDerangements(n - 1) + numDerangements(n - 2))

# Testing code
def main():
    testArgs = [[1, 0], [2, 1], [3, 2], [4, 9], [5, 44]]
    for arg in testArgs:
        nArg, answer = arg
        result = numDerangements(nArg)
        if result != answer:
            print(f"Failed numDerangements test with arg n={nArg}.\nExpected: {answer}, Got: {result}")
        else:
            print(f"Passed numDerangements test with arg n={nArg}.")

if __name__ == '__main__':
    main()
