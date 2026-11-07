import pandas as pd


def add_two_numbers(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def sum_list(numbers: list[float]) -> float:
    """Return the sum of a list of numbers."""
    return sum(numbers)


def sum_dataframe_column(df: pd.DataFrame, column: str) -> float:
    """Return the sum of a specific column in a pandas DataFrame."""
    return df[column].sum()


if __name__ == "__main__":
    # Example 1: Sum two numbers
    num1, num2 = 15, 27
    print(f"Sum of {num1} + {num2} = {add_two_numbers(num1, num2)}")

    # Example 2: Sum a list of numbers
    nums = [10, 20, 30, 40, 50]
    print(f"Sum of list {nums} = {sum_list(nums)}")

    # Example 3: Sum using pandas
    data = {"Item": ["A", "B", "C"], "Value": [100, 250, 150]}
    df = pd.DataFrame(data)
    print("\nDataFrame:")
    print(df)
    print(f"Total Value (pandas sum): {sum_dataframe_column(df, 'Value')}")

