### The following demonstrates some differences between Python and Java.


### Time honored tradition of "Hello World!"

### Python
```python
print("Hello World!")
```
### Java
```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
```
#### Observations:
* Python is simple. Only requires passing a string to a built in function.
* Java requires an individual to understand at least three concepts; a class, a method, and method parameters. 
    * https://docs.oracle.com/javase/tutorial/getStarted/application/index.html


### Diving deeper: 

### Python Program:
```python
#  This program prints greetings based on a user's first name and age

#  For a multi-line comment
#  Comment line 2

greeting_of_the_day = 'welcome, adventurer!'
special_greeting = 'welcome, your highness!'
default_greeting = ", howdy adventurer!"  # One can use double quotes for strings

names = ['rachel', 'jennifer', 'paul', 'james']
special_name = 'sarah'

name = input('What is your first name? ')
age = int(input('How old are you? '))

# converting name to lowercase for comparison
name = name.lower()

if names.__contains__(name) and age >= 21:
    print(greeting_of_the_day.title())
    print(name.title() + ' A special drink awaits you!')
elif special_name.__eq__(name):
    print(special_greeting.title())
    print(name.title() + ',A special feasts awaits you in the castle!')
elif name.startswith('a') and age >= 21:
    print('A drink awaits you, ' + name.title() + ' well done!')
else:
    print(name.title() + default_greeting.title())
```

### Java Program:
```java
import java.util.Arrays;
import java.util.Scanner;

/**
 * This program prints greetings based on a user's first name and age
 */
public class CustomGreeter {

    public static void main(String[] args) {

        var greetingOfTheDay = "Welcome, adventurer!";
        var specialGreeting = "Welcome, your highness!";
        var defaultGreeting = ", howdy adventurer!";

        var names = new String[]{"rachel", "jennifer", "paul", "james"};
        var specialName = "sarah";

        // This collects input from the user. Notice the ceremony involved with the Scanner class
        Scanner input = new Scanner(System.in);
        System.out.println("What is your first name? ");
        var name = input.nextLine();
        System.out.println("What is your age? ");
        var age = input.nextInt();
        input.close();

        // Comparison to Python - a string array does not contain the 'contains' method
        var nameList = Arrays.stream(names).toList();
        //General note - the String class in Java does not have a built-in toTitleCase or capitalize function
        if (nameList.contains(name)&& age >= 21) {
            System.out.println(greetingOfTheDay);
            System.out.println(name + " , A special drink awaits you!");
        }
        else if (specialName.equalsIgnoreCase(name)) {
            System.out.println(specialGreeting);
            System.out.println(name + ", A special feasts awaits you in the castle!");
        }
        else {
            System.out.println(name + defaultGreeting);
        }
    }
}
```
#### What did I use?
* Python version 3.9.5
* Java SE 16

#### My observations:
* *Python is concise*
* *Java is verbose*
* No semicolons, curly braces, or parenthesis in Python!
* Python is a *layout (indentation) sensitive* language
  * Follows *Landin's offsides rule*
* Python follows a set of principles that focus on simplicity, readability, and beautiful code.
  * https://www.python.org/dev/peps/pep-0020/
* More ceremony involved with Java
