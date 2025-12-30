# __init__() is a constructor method which helps to
# set initial values while instatiating a class.

# __init__() will get called with the attributes set in __init__(),
# when a class is instantiated.

# The '__' before and after the method name denotes that
# the method is private. It's called private or magic methods
# since it's called internally and automatically.


Class Method vs Static Method : 

| Feature                | Static Method   | Class Method   |
| ---------------------- | --------------- | -------------- |
| Decorator              | `@staticmethod` | `@classmethod` |
| First argument         | None            | `cls`          |
| Access class variables | ❌               | ✅              |
| Modify class state     | ❌               | ✅              |
| Called via class       | ✅               | ✅              |
| Typical use            | Utility logic   | Class behavior |

Use static method when :
    Logic is independent of class & instance
    Function logically belongs to the class
    Example: validation, calculation, helpers

Use class method when :
    Logic needs class data
    You want to modify class variables
    You need alternative constructors

    