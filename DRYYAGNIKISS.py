# 1. DRY Principle - Don’t Repeat Yourself
'''Every piece of knowledge or logic should exist in only ONE place in your code. It applies not only to code, but also to: Business rules, Configuration, Data models, Documentation, Tests'''
# 1.1 Why DRY matters
'''
1. Fewer Bugs - Fix in one place and not in 5 different files
2. Easier Maintainance - Change logic once and everything updates automatically
3. Cleaner, readable code - less duplication and clear intent
4. Safer OOP design - encourages abstraction, reuse, composition
'''
# 1.2 Example
# DRY Violation - Bad - Same logic repeated - If tax rate changes → change in multiple places
class Order:
    def calculate_total(self, price, quantity):
        total = price * quantity
        tax = total * 0.1
        return total + tax
class Invoice:
    def calculate_total(self, price, quantity):
        total = price * quantity
        tax = total * 0.1
        return total + tax
# DRY solution using a shared method
class PriceCalculator: # common logic
    @staticmethod
    def calculate(price, quantity):
        total = price * quantity
        tax = total * 0.1
        return total + tax
class Order:
    def total(self, price, quantity):
        return PriceCalculator.calculate(price, quantity) # reuse
class Invoice:
    def total(self, price, quantity):
        return PriceCalculator.calculate(price, quantity) # reuse
# 1.3 GOOD DRY vs BAD DRY
'''
BAD DRY - DRY does not mean:Create massive base classes,Over-abstract too early.
GOOD DRY - Extract real duplication, Not “maybe duplication”
'''
# 1.4 When to apply DRY
'''
1. Same logic appears 2+ times
2. Logic represents a business rule
3. Changes are likely
'''
# 2. YAGNI Principle - You Aren’t Gonna Need It
'''Always implement things when you actually need them, never when you just foresee that you need them. Don’t build for tomorrow. Build for today. Don’t add functionality until you actually need it.'''
# 2.1 Why DRY matters
'''
1. A bloated, overly complex system - increased complexity
2. Slower delivery of the core functionality - delayed value
3. More code to test, maintain, and debug - wasted time & effort
4. Features no one asked for - higher maintenance costs
'''
# 2.2 Example
# YAGNI Violation Example (Over-Engineering) - Adding future features “just in case”
class PaymentProcessor:
    def pay_by_credit_card(self, amount):
        print(f"Paid {amount} by credit card")
    def pay_by_paypal(self, amount): # Unused methods, Confusing, More maintenance
        pass  # maybe later
    def pay_by_crypto(self, amount): # Unused methods, Confusing, More maintenance
        pass  # maybe later
    def refund(self, amount): # Unused methods, Confusing, More maintenance
        pass  # future requirement
# YAGNI-Compliant Version (Simple)
class PaymentProcessor:
    def pay(self, amount):
        print(f"Paid {amount} by credit card")
# 2.3 YAGNI Exceptions
'''
Here are cases where it is acceptable to go beyond current needs:

Security and compliance requirements: You may need to prepare for data protection, auditing, or regulatory constraints up front.
Architecture with known long-term constraints: For example, if you are writing code for a high-availability system, some abstractions or patterns may be required from day one.
Reusable libraries or frameworks: If you are building tools for other developers, some flexibility may be expected.
'''
# 3. KISS Principle - Keep It Simple, Stupid
'''Most systems work best if they are kept simple rather than made complex. Therefore, simplicity should be a key goal in design. Choose the simplest solution that works. Write code that is: Easy to read, Easy to understand, Easy to change'''
# 3.1 Why KISS matters
'''
1. Code Is Read More Than Written - Simple code is easier to understand. Future you (or teammates) will thank you
2. Fewer Bugs - Complexity creates bugs. Simple logic → fewer edge cases
3. Easier Maintenance - Easy to change, Easy to debug
4. Better Team Collaboration - Everyone understands simple code
'''
# 3.2 Example
# KISS Violation Example - overengineered for a four-function calculator.
from abc import ABC, abstractmethod
class Operation(ABC):
    @abstractmethod
    def calculate(self, a, b):
        pass
class Addition(Operation):
    def calculate(self, a, b):
        return a + b
class Subtraction(Operation):
    def calculate(self, a, b):
        return a - b
class Calculator:
    def execute(self, op: Operation, a, b):
        return op.calculate(a, b)
# KISS-Compliant Version (Simple)
class Calculator:
    def calculate(self, operator, a, b):
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            if b == 0:
                raise ValueError("Division by zero")
            return a / b
        else:
            raise NotImplementedError(f"Unknown operator: {operator}")
# 3.3  How to apply KISS principle
'''
1. Write Code for Humans, Not Machines
Optimizing for readability and clarity helps everyone on the team. Your future self will thank you.

2. Avoid Premature Abstraction
Abstractions should emerge from repetition or clear need, not from imagination.

3. Favor Composition Over Inheritance
Simple, flat structures often work better than deep hierarchies.

4. Keep Functions Short
Small functions are easier to understand and test. If a function is hard to name, it’s probably doing too much.

5. Use Familiar Constructs
Stick to patterns and structures that are widely recognized. Do not reinvent the wheel when a simple List, Map, or loop can do the job.
'''