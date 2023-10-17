import pytest
from calculator import calculate


def test_add():
  """Tests the addition operation."""

  num1 = 2
  num2 = 3
  operator = "+"
  expected_result = 5

  result = calculate(num1, num2, operator)

  assert result == expected_result


def test_subtract():
  """Tests the subtraction operation."""

  num1 = 2
  num2 = 3
  operator = "-"
  expected_result = -1

  result = calculate(num1, num2, operator)

  assert result == expected_result


def test_multiply():
  """Tests the multiplication operation."""

  num1 = 2
  num2 = 3
  operator = "*"
  expected_result = 6

  result = calculate(num1, num2, operator)

  assert result == expected_result

  num3 = -4
  result2 = calculate(num1,num3,operator)
  expected_result2 = -8
  assert result2 == expected_result2


def test_divide():
  """Tests the division operation."""

  num1 = 2
  num2 = 3
  operator = "/"
  expected_result = 0.6666666666666666

  result = calculate(num1, num2, operator)

  assert result == expected_result

  num3 = -4
  result2 = calculate(num1,num3,operator)
  expected_result2 = -0.5
  assert result2 == expected_result2

def test_divide_by_zero():
  """Tests that division by zero raises a ZeroDivisionError exception."""

  num1 = 2
  num2 = 0
  operator = "/"

  with pytest.raises(ZeroDivisionError):
    calculate(num1, num2, operator)

    