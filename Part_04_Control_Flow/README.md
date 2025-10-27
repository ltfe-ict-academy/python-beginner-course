# Control Flow

## Conditional Statements
- [Conditional Statements in Python](https://realpython.com/python-conditional-statements/)

Frequently, a program needs to skip over some statements, execute a series of statements repetitively, or choose between alternate sets of statements to execute.

That is where control structures come in. A control structure directs the order of execution of the statements in a program.

In a Python program, the if statement is how you perform this sort of decision-making. It allows for conditional execution of a statement or group of statements based on the value of an expression.

## While loops
- [Python while Loops: Repeating Tasks Conditionally](https://realpython.com/python-while-loop/)

In Python, you’ll generally use while loops when you need to repeat a series of tasks an unknown number of times.

The basic syntax of a while loop is shown below:
```python
while condition:
    # code block to be executed
```

The Python while loop has some advanced features that make it flexible and powerful. These features can be helpful when you need to fine-tune the loop to meet specific execution flows. Python provides two keywords that let you modify that behavior:
- **break**: Immediately terminates a loop. The program execution then proceeds with the first statement following the loop body.
- **continue**: Ends only the current iteration. The execution jumps back to the loop header, and the loop condition is evaluated to determine whether the loop will execute again.

