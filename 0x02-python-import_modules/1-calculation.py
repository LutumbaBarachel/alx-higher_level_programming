#!/usr/bin/python3
import calculator_1 as calc

a = 10
b = 5

add_result = calc.add(a, b)
sub_result = calc.subtract(a, b)
mul_result = calc.multiply(a, b)
div_result = calc.divide(a, b)

print("Addition: {}".format(add_result))
print("Subtraction: {}".format(sub_result))
print("Multiplication: {}".format(mul_result))
print("Division: {}".format(div_result))
