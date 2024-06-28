# “斐波那契序列（Fibonacci sequence）是一系列数字，其中除第1个和第2个数字之外，其他数字都是前两个数字之和”
#
# 摘录来自
# 算法精粹：经典计算机科学问题的 Python 实现
# David Kopeck
# 此材料可能受版权保护。
def fib(n: int) -> int:
    if n < 2:  # base case
        return n
    return fib(n - 2) + fib(n - 1)  # recursive case