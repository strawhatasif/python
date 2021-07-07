### The following demonstrates some differences between Python and Java.

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
#### My observations:
* *Python is concise*
* *Java is verbose*
* More ceremony involved with Java
