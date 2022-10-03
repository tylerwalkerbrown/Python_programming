```python
print('Hello there!')
```

    Hello there!



```python
concat = "Hello" + " " + "there" + "!"
```


```python
concat[0:5]
```




    'Hello'




```python
string = "\"Hello there!\""
```


```python
string
```




    '"Hello there!"'




```python
#4
float(3.78E5)
```




    378000.0




```python
#5
b = 'A'
print(str(b))
```

    A



```python
x = 4
y = 6
z = 4
```

This simple program is to test if x is an even or odd number. This checks if the x value is divisible by 2 which would indicate an even number and prints out 'odd' for else.


```python
if x%2 == 0:
      print('Even')
else:
      print('Odd')
print('Done with conditional')
```

    Even
    Done with conditional


Here we have an if statement that checks to see if the numbers are divisible by 2 or 3. If x passes the first statement checking if it is divisible by 2 then it will go into the nested loop where the second if statement will check if it is divisible by 3 and if it passes it will print a result then if not it will print the else statement as seen below. 
    If the statment doesnt pass the first test and it is not divisible by two and is divisible by 3 then the program will print 'divisible by 3...'


```python
if x%2 == 0:
        if x%3 == 0:
            print('Divisible by 2 and 3')
        else:
            print('Divisible by 2 and not by 3')
elif x%3 == 0:
    print('Divisible by 3 and not by 2')
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Input In [1], in <cell line: 1>()
    ----> 1 if x%2 == 0:
          2         if x%3 == 0:
          3             print('Divisible by 2 and 3')


    NameError: name 'x' is not defined



```python
if x < y and x < z:
      print('x is least')
elif y < z:
      print('y is least')
else:
      print('z is least')
```

    z is least


Below we have a program that tests to see between three variables what the highest odd number.    


```python
if x%2 != 0 and y%2 != 0 and z%2 != 0:
      print(max(x, y, z))
if x%2 != 0 and y%2 != 0 and z%2 == 0:
      print(max(x, y))
if x%2 != 0 and y%2 == 0 and z%2 != 0:
      print(max(x, z))
if x%2 == 0 and y%2 != 0 and z%2 != 0:
      print(max(y, z))
if x%2 != 0 and y%2 == 0 and z%2 == 0:
      print(x)
if x%2 == 0 and y%2 != 0 and z%2 == 0:
      print(y)
if x%2 == 0 and y%2 == 0 and z%2 != 0:
      print(z)
if x%2 == 0 and y%2 == 0 and z%2 == 0:
      print('Does not contain an odd number.')
```

    Does not contain an odd number


Here is a more efficient route to get the highest odd number. I modified the else statment to display no odds when there are nop odds within the variables.


```python
answer = max(x, y, z)
```


```python
if x%2 != 0:
      result = x
if y%2 != 0 and y > answer:
      result = y
if z%2 != 0 and z > answer:
      result = z
else:
    result = 'No odds'
print(result)
```

    No odds



```python
#Python can also support assignments of if else statements
x = y if y > z else z
```
