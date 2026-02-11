# OOPS - purpose is designing structured, reusable, and maintainable software.
'''OOPS - organizing code which uses classes and objects to represent real world entities and their behaviour.
Object - attributes that has data
Methods - actions of objects
Class - collection of objects (blueprint for creating objects) - defines a set of attributes and methods that created objects (instances) can have'''
# Class
'''Class - 1. Classes are created by keyword class
2. Attributes are the variables that belong to a class
3. Attributes are always public and can be accessed using the dot (.) operator. Example: Myclass.Myattribute'''
# Creating a class
class Dog:
    species = "Canine" # class attribute (shared by all instances of the class)
    def __init__(self,name,age): #__init__() - constructor method that runs automatically when a new object is created, used to initialize object data
        self.name=name # instance attribute - unique to each Dog object created from the class
        self.age=age   # instance attribute - unique to each Dog object created from the class
        # self refers to current object being passed, allowing each object to store and access its own data
# __init__ 
'''this method in Python is a constructor. It runs automatically when a new object of a class is created. Its main purpose is to initialize the object’s attributes and set up its initial state. When an object is created, memory is allocated for it, and __init__ helps organize that memory by assigning values to attributes.'''
# __init__ with parameters
'''we can pass multiple parameters to set up different attributes'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("Alice",30)
p2=Person("Bob",25)
print(p1.name,p1.age)
print(p2.name,p2.age)
# Default parameters in __init__
class Dog:
    def __init__(self,name,breed="Mixed",age=1):
        self.name=name
        self.breed=breed
        self.age=age
d1=Dog("Buddy")
d2=Dog("Max","Golden Retriever",5) # defaults are overwritten by the provided values
print(d1.name,d1.breed,d1.age)
print(d2.name,d2.breed,d2.age)
# __init__ method with inheritance - when using inheritance, both parent and child classes can have __init__ methods
class A:
    def __init__(self):
        print("A init is called")
class B(A):
    def __init__(self):
        super().__init__() # call parent __init__
        print("B init is called")
obj=B()
# Object
'''An Object is an instance of a Class. It represents a specific implementation of the class and holds its own data. An object consists of:

State: It is represented by the attributes and reflects the properties of an object.
Behavior: It is represented by the methods of an object and reflects the response of an object to other objects.
Identity: It gives a unique name to an object and enables one object to interact with other objects.'''
# creating object - object instantiation
class Dog:
    species="Canine" # class attribute
    def __init__(self,name,age):
        self.name=name
        self.age=age
dog1=Dog("Buddy",3)
print(dog1.name)
print(dog1.species)
# 4 pillars of OOP - Inheritance, Polymorphism, Encapsulation, Data Abstraction
# 1. Inheritance 
'''allows a class (called a child or derived class) to inherit attributes and methods from another class (called a parent or base class)'''
class Animal: #parent class
    def __init__(self,name):
        self.name=name
    def info(self):
        print("Animal name:", self.name)
class Dog(Animal): # child of Animal class
    def sound(self):
        print(self.name,"barks")
d=Dog("Buddy")
d.info() # calls parent method info()
d.sound() # calls child method sound()
# Need for inheritance
'''1. Promotes code reusability by sharing attributes and methods across classes.
2. Models real-world hierarchies like Animal -> Dog or Person -> Employee.
3. Simplifies maintenance through centralized updates in parent classes.
4. Enables method overriding for customized subclass behavior.
5. Supports scalable, extensible design using polymorphism.'''
# super() Function
'''1. super() function is used to call methods from a parent (superclass) inside a child (subclass). It allows you to extend or override inherited methods while still reusing the parent’s functionality.
2. Return a proxy object which represents the parent's class.
3. why use super() - 
No need to hardcode parent class names , useful when class hierarchies change.
Works with single, multiple, and multilevel inheritance.
Improves code reusability and maintainability.
Prevents duplicate initialization in complex hierarchies.'''
class Animal:
    def __init__(self,name):
        self.name=name
    def info(self):
        print("Animal name:",self.name)
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name) # ensures that parent class functionality is reused without needing to rewrite the code in the child class by initializing inherited attribute (name)
        # super() automatically calls self so no need to mention self
        self.breed=breed
    def details(self):
        print(self.name, "is a" ,self.breed)
d=Dog("Buddy","Golden Retriever")
d.info()
d.details()
# Types of inheritance
# 1.1 single inheritance - a child class inherits from just one parent class
class Person:
    def __init__(self,name):
        self.name=name
class Employee(Person):
    def show_role(self):
        print(self.name,"is an employee")
emp=Employee("sarah")
print("Name:",emp.name)
emp.show_role()
# 1.2 Multiple inheritance - a child class can inherit from more than one parent class
class Person:
    def __init__(self,name):
        self.name=name
class Job:
    def __init__(self,salary):
        self.salary=salary
class Employee(Person,Job):
    def __init__(self, name,salary):
        Person.__init__(self,name)
        Job.__init__(self,salary)
    def details(self):
        print(self.name,"earns",self.salary)
emp=Employee("Josh",80000)
emp.details()
# 1.3 Multilevel inheritance - a class is derived from another derived class (like a chain)
class Person:
    def __init__(self,name):
        self.name=name
class Employee(Person):
    def show_role(self):
        print(self.name,"is an employee")
class Manager(Employee):
    def department(self,dept):
        print(self.name,"manages",dept,"department")
mgr=Manager("Joy")
mgr.show_role()
mgr.department("HR")
# 1.4 Hierarchical inheritance - multiple child classes inherit from the same parent class
class Person:
    def __init__(self,name):
        self.name=name
class Employee(Person):
    def role(self):
        print(self.name,"is a employee")
class Intern(Person):
    def role(self):
        print(self.name,"is an intern")
emp=Employee("David")
emp.role()
intern=Intern("Eva")
intern.role()
# 1.5 Hybrid inheritance - combination of more than one type of inheritance
# this example - single + multilevel + multiple inheritance
class Person:
    def __init__(self,name):
        self.name=name
class Employee(Person):
    def role(self):
        print(self.name,"is an employee")
class Project:
    def __init__(self,project_name):
        self.project_name=project_name
class TeamLead(Employee,Project):
    def __init__(self,name,project_name):
        Employee.__init__(self,name)
        Project.__init__(self,project_name)
    def details(self):
        print(self.name,"leads project:", self.project_name)
lead=TeamLead("Sophia","AI Development")
lead.role()
lead.details()
# 2. Polymorphism 
'''ability of the same method or operation to behave differently based on object or context. It mainly includes compile-time and runtime polymorphism'''
# 2.1 compile-time polymorphism
'''deciding which method or operation to run during compilation, usually through method or operator overloading
   Languages like Java or C++ support this. But Python doesn’t because it’s dynamically typed it resolves method calls at runtime, not during compilation. So, true method overloading isn’t supported in Python, though similar behavior can be achieved using default or variable arguments.
'''
# method overloading
class Calculator:
    def addition(self,a=1,b=1,*args):
        result=a+b 
        for num in args:
            result+=num
        return result
calc=Calculator()
print(calc.addition())
print(calc.addition(4))
print(calc.addition(1,2))
print(calc.addition(1,2,3))
print(calc.addition(1,2,3,4))
# 2.2 run-time polymorphism
'''Runtime polymorphism means that the behavior of a method is decided while program is running, based on the object calling it.
In Python, this happens through Method Overriding a child class provides its own version of a method already defined in the parent class. Since Python is dynamic, it supports this, allowing same method call to behave differently for different object types'''
# 2.2.1 method overriding
class Animal:
    def sound(self):
        print("some generic sound")
class Dog(Animal):
    def sound(self):
        print("Bow")
class Cat(Animal):
    def sound(self):
        print("Meow")
animals=[Animal(),Dog(),Cat()]
for i in animals:
    i.sound()
# 2.2.2 operator overloading
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=Student(m1,m2)
        return s3
s1=Student(50,90)
s2=Student(20,35)
s3=s1+s2
print(s3.m1,s3.m2)
# 2.2.3 duck typing - polymorphism in functions
'''In Python, polymorphism lets functions accept different object types as long as they support needed behavior. Using duck typing, Python focuses on whether an object has right method not its type allowing flexible and reusable code. Duck Typing is a type system used in dynamic languages. For example, Python, Perl, Ruby, PHP, Javascript, etc. where the type or the class of an object is less important than the method it defines. Using Duck Typing, we do not check types at all. Instead, we check for the presence of a given method or attribute '''
class Pen:
    def use(self):
        print("writing")
class Eraser:
    def use(self):
        print("erasing")
def give_functionality(tool):
    return tool.use()
give_functionality(Pen())
give_functionality(Eraser())
# 3. Encapsulation 
''' Encapsulation is about protecting data inside a class.
It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.
This prevents accidental changes to your data and hides the internal details of how your class works.'''
# Need for encapsulation
'''1. Protects data from unauthorized access and accidental modification.
2. Controls data updates using getter/setter methods with validation.
3. Enhances modularity by hiding internal implementation details.
4. Simplifies maintenance through centralized data handling logic.
5. Reflects real-world scenarios like restricting direct access to a bank account balance.'''
# Access Specifiers
'''Access specifiers define how class members (variables and methods) can be accessed from outside the class. They help in implementing encapsulation by controlling the visibility of data.
Types 1. Public 2. Protected 3. Private'''
# 3.1 Public Members
'''Public members are variables or methods that can be accessed from anywhere inside the class, outside the class or from other modules. By default, all members in Python are public. They are defined without any underscore prefix '''
class Employee:
    def __init__(self, name):
        self.name = name   # public attribute

    def display_name(self):   # public method
        print(self.name)

emp = Employee("John")
emp.display_name()   # Accessible
print(emp.name)      # Accessible
# 3.2 Protected Members
'''Protected members are variables or methods that are intended to be accessed only within the class and its subclasses. They are not strictly private but should be treated as internal. In Python, protected members are defined with a single underscore prefix. Protected members should not be accessed outside the class hierarchy, but Python does not enforce this rule strictly. '''
class Employee:
    def __init__(self,name,age):
        self.name=name # public variable
        self._age=age # protected variable
class Manager(Employee):
    def show_age(self):
        print("Age is",self._age) # accessible in child class
mgr=Manager("Josh",25)
print(mgr.name) # accessible bcz of public attribute
mgr.show_age() # accessible bcz of subclass is used for accessing
# 3.3 Private Members
'''Private members are variables or methods that cannot be accessed directly from outside the class. They are used to restrict access and protect internal data. In Python, private members are defined with a double underscore prefix '''
# 3.3.1 Name Mangling
'''Python applies name mangling by internally renaming them (e.g., __salary becomes _ClassName__salary) to prevent direct access.
Name mangling is especially useful when working with inheritance. It prevents subclasses from accidentally overriding important methods.'''
'''Name mangling : 
1. Name mangling applies to names starting with __.
2. It helps avoid name conflicts in inheritance.
3. It is not strict privacy, but a protective feature.
4. Best used when designing classes meant to be extended.
When to use name mangling:
1. You want to prevent accidental overrides in subclasses
2. You are writing reusable or framework-level classes
3. You want clearer separation between internal and external attributes
'''
# name mangling example - 1st way of doing it
class Parent:
    def __init__(self):
        self.__show()
    def show(self):
        print("parent class")
    __show=show
class Child(Parent):
    def show(self):
        print("child class")
obj=Child()
obj.show()
# name mangling example -  2nd way of doing it
class Parent:
    def __init__(self):
        self.__show()   # Calls Parent's private method
    def __show(self):
        print("parent class")
class Child(Parent):
    def show(self):
        print("child class")
obj = Child()   # Calls Parent.__init__ → Parent.__show()
obj.show()
# private members
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    def show_salary(self):
        print("salary is", self.__salary)
emp=Employee("Laura","120000")
print(emp.name)
emp.show_salary()
#print(emp.__salary) Throws an error as we cannot access private variables/ members outside the class
# Protected and Private methods
'''Protected method - Use a single underscore (_) before a method name to indicate it is protected meant to be used within class or its subclasses. Private method - Use a double underscore (__) to define a private method accessible only within class due to name mangling.'''
'''Unlike other programming languages, Python does not enforce access modifiers like public, private or protected at the language level. However, it follows naming conventions and uses a technique called name mangling to support encapsulation'''
class Account:
    def __init__(self):
        self.balance=100
    def _show_balance(self):
        print("Balance is $",self.balance)
    def __update_balance(self,amount):
        self.balance+=amount
    def deposit(self,amount):
        if amount>0:
            self.__update_balance(amount)
            self._show_balance()
        else:
            print("Invalid deposit amount please deposit amount greater than zero")
acc=Account()
acc._show_balance() # works but not great way of accessing (can be accessed by using public method like below)
acc.deposit(600)
# Getter and Setter methods
'''getter and setter methods are used to access and modify private attributes safely. Instead of accessing private data directly, these methods provide controlled access, allowing you to:
Read data using a getter method.
Update data using a setter method with optional validation or restrictions.'''
class Employee:
    def __init__(self):
        self.__salary=90000
    def get_salary(self):
        print("salary is $",self.__salary)
    def set_salary(self,amount):
        if amount>0:
            self.__salary=amount
            print("updated salary is $", self.__salary)
        else:
            print("Invalid salary")
emp=Employee()
emp.get_salary()
emp.set_salary(140000)
# 4. Abstraction
'''hides the internal implementation details while exposing only the necessary functionality. It helps focus on "what to do" rather than "how to do it. In Python abstraction is used to hide the implementation details from the user and expose only necessary parts, making the code simpler and easier to interact with.'''
# Abstract Base Class
'''In Python, an Abstract Base Class (ABC) is used to achieve data abstraction by defining a common interface for its subclasses. It cannot be instantiated directly and serves as a blueprint for other classes.'''
'''Abstract classes are created using abc module and @abstractmethod decorator, allowing developers to enforce method implementation in subclasses while hiding complex internal logic.'''
from abc import ABC, abstractmethod
class Greeting(ABC):
    @abstractmethod
    def wish(self):
        pass
class English(Greeting):
    def wish(self):
        print("Hello")
class Telugu(Greeting):
    def wish(self):
        print("Namaste")
eng=English()
eng.wish()
tel=Telugu()
tel.wish()
# 4.1 Components of Abstraction
'''Abstraction in Python is made up of key components like abstract methods, concrete methods, abstract properties and class instantiation rules. These elements work together to define a clear and enforced structure for subclasses while hiding unnecessary implementation details. '''
# 4.1.1 Abstract Method
'''Abstract methods are method declarations without a body defined inside an abstract class. They act as placeholders that force subclasses to provide their own specific implementation, ensuring consistent structure across derived classes'''
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self): # abstract method
        pass
class Dog(Animal):
    def sound(self):
        print("Bow")
d=Dog()
d.sound()
# 4.1.2 Concrete Method
'''Concrete methods are fully implemented methods within an abstract class. Subclasses can inherit and use them directly, promoting code reuse without needing to redefine common functionality'''
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def greet(self): # concrete method
        print("Hello, Animal here!!")
class Dog(Animal):
    def sound(self):
        print("Bow")
d=Dog()
d.sound()
d.greet()
# 4.1.3 Abstract Properties
'''Abstract properties work like abstract methods but are used for properties. These properties are declared with @property decorator and marked as abstract using @abstractmethod. Subclasses must implement these properties. Preferred when the property is a characteristic of the class rather than its action, like Animal is a species, employee has salary and rectangle has area'''
'''Even though a property is implemented using a method internally, it represents state, not behavior. @property allows us to compute the value while preserving attribute-style access, which improves encapsulation and design clarity.'''
from abc import ABC, abstractmethod
class Animal(ABC):
    @property
    @abstractmethod
    def species(self):
        pass
class Dog(Animal):
    @property
    def species(self):
        print("canine")
d=Dog()
d.species # see that there is no () when calling species (no d.species()) - it acts like a state/attribute but not behavior
# 4.1.4 Abstract Class Instantiation
'''Abstract classes cannot be instantiated directly. This is because they contain one or more abstract methods or properties that lack implementations. Attempting to instantiate an abstract class results in a TypeError.'''
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
#animal = Animal() - Throws an error as abstract class cannot be instantiated
# 5. Types of variables
# 5.1 Instance Variables (Non-Static Variables)
'''Instance variables are associated with individual instances (objects) of a class. Each object has its own copy of these variables. They are defined within the class but outside of any method. Instance variables represent the state of an object and can have different values for different instances of the class.'''
class Person:
    def __init__(self,name,age):
        self.name=name # instance variable
        self.age=age # instance variable
# 5.2 Class Variables (Static Variables)
'''Class variables are shared among all instances of a class. They are declared within the class and outside of any method using the @classmethod decorator or directly under the class definition. Class variables are used to represent attributes that are common to all instances of the class.'''
class Circle:
       pi = 3.14159  # class variable
       def __init__(self, radius):
           self.radius = radius  # instance variable
# 5.3 Local Variables 
'''Local variables are defined within a method and have scope only within that method. They cannot be accessed from outside the method. These variables are temporary and exist only during the execution of the method.'''
class Calculator:
       def add(self, x, y):
           result = x + y  # local variable
           return result
# 5.4 Parameter Variables
'''Parameter variables are used to pass values to methods or constructors. They are placeholders for the values that will be provided when the method is called or the object is created.'''
class Rectangle:
       def __init__(self, width, height):
           self.width = width      # instance variable
           self.height = height    # instance variable
# 6. Types of Functions
# 6.1 Instance Methods
'''Instance methods are functions that are associated with individual instances of a class. They have access to the instance's attributes and can modify its state. They are typically used to model behavior that is specific to each object created from the class. Instance methods are often used for actions or operations that affect the object's internal state.'''
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius * self.radius

circle = Circle(5)
area = circle.calculate_area()  # Calling instance method
# 6.2 Static Methods
'''Class methods are functions associated with the class itself, not its instances. They can access class-level attributes but not instance attributes. Class methods are often used for utility functions that are not directly related to instance-specific behavior.'''
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

result = MathUtils.add(5, 3)  # Calling class method
# Method Resolution Order
'''Method Resolution Order (MRO) defines the order in which Python searches for a method in a class and its parent classes. It becomes important when the same method exists in more than one class in an inheritance chain, especially in multiple inheritance. Usually left to right during inheritance.Python uses the C3 linearization algorithm to decide the order in which classes are searched when a method is called. This algorithm produces a single, consistent order that respects both inheritance and the order in which parent classes are written.'''
# Example
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
# Method Resolution Order D->B->C->A
    



