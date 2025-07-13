import sys
import pytest
from triangle import Triangle, TriangleType, App

# Tests for Triangle
def test_triangle_equilateral():
    t = Triangle([5, 5, 5])
    assert t.determineType() == TriangleType.EQUILATERAL

def test_triangle_isosceles():
    t = Triangle([5, 5, 3])
    assert t.determineType() == TriangleType.ISOSCELES

def test_triangle_scalene():
    t = Triangle([3, 4, 5])
    assert t.determineType() == TriangleType.SCALENE

def test_triangle_zero_side():
    with pytest.raises(ValueError) as exc:
        Triangle([0, 1, 1])
    assert "A Triangle side cannot be zero" in str(exc.value)

def test_triangle_negative_side():
    with pytest.raises(ValueError) as exc:
        Triangle([-1, 1, 1])
    assert "Side lengths cannot be negative" in str(exc.value)


# Tests for App in CLI mode
def test_parse_cli_valid_args(monkeypatch):
    fake_argv = ["prog", "3", "4", "5"]
    monkeypatch.setattr(sys, 'argv', fake_argv)
    app = App()
    app.parseInput(fake_argv)
    assert app.args == [3, 4, 5]

def test_parse_cli_too_few_args_raises(monkeypatch):
    fake_argv = ["prog", "3", "4"]
    monkeypatch.setattr(sys, 'argv', fake_argv)
    with pytest.raises(NotImplementedError) as exc:
        App().parseInput(fake_argv)
    assert "there must be three arguments" in str(exc.value)

def test_parse_cli_non_integer_arg_raises(monkeypatch):
    fake_argv = ["prog", "3", "4", "five"]
    monkeypatch.setattr(sys, 'argv', fake_argv)
    with pytest.raises(ValueError) as exc:
        App().parseInput(fake_argv)
    assert "Side lengths must be integers" in str(exc.value)

# Tests for App in interactive mode
def test_parse_interactive_single_prompt(monkeypatch):
    inputs = iter(["7 8 9"])
    monkeypatch.setattr('builtins.input', lambda prompt=None: next(inputs))
    app = App()
    app.parseInput([])
    assert app.args == [7, 8, 9]

def test_parse_interactive_retries_until_valid(monkeypatch):
    inputs = iter(["1 2", "1 2 3"])
    monkeypatch.setattr('builtins.input', lambda prompt=None: next(inputs))
    app = App()
    app.parseInput(["only_one_element"])
    assert app.args == [1, 2, 3]


# Integration Tests
def test_output_type_scalene(capsys):
    app = App()
    app.args = [3, 4, 5]
    app.outputType()
    captured = capsys.readouterr()
    assert "The type of triangle with sides 3, 4, and 5 is scalene" in captured.out

def test_output_type_isosceles(capsys):
    app = App()
    app.args = [5, 5, 3]
    app.outputType()
    captured = capsys.readouterr()
    assert "The type of triangle with sides 5, 5, and 3 is isosceles" in captured.out

def test_output_type_equilateral(capsys):
    app = App()
    app.args = [2, 2, 2]
    app.outputType()
    captured = capsys.readouterr()
    assert "The type of triangle with sides 2, 2, and 2 is equilateral" in captured.out
