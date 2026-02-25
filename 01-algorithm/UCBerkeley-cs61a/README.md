## Recursion
---
## Class   
- Attributes
- Methods
    
🔹 Object Oriented Programming (OOP)   
-  Abstraction barriers enforce the **boundaries** between different aspects of a large program.
-  Object-oriented programming is particularly well-suited to programs that model systems that have separate but interacting parts.
-  Discussion_07 -- elegant code design


🔹 Inheritence
- Base class (parent class) & Subclass (child class)
    - A subclass inherits the attributes of its base class, but may **override** certain attributes, including certain methods.
    - With inheritance, we only specify what is **different** between the subclass and the base class. Anything that we leave unspecified in the subclass is automatically assumed to behave just as it would for the base class.
    - Python supports the concept of a subclass inheriting attributes from multiple base classes -- multiple inheritance.


 🔹 Modular Design
 - Large programs can benefit from modular design, which means that the whole program is broken up into small, fairly (not completely since they have to interact) independent parts that are isolated by data abstraction barriers
 - Principle: isolate different parts of a program that address different concerns

---
## Data Abstraction
---
## Mutability
Linked List vs. List  

List (mutable) vs. Tuple (immutable)
- pass-by-value(copy) vs pass-by-reference
    - 🔹 pass-by-value (copy)
        - A new copy of the data is made
        - Changes don’t affect the original
    - 🔹 pass-by-refernce
        - A reference (pointer) to the original object is passed
        - Mutations affect the original
```python     
>>> ones = Link(1)
>>> ones.rest = ones
>>> [ones.first, ones.rest.first, ones.rest.rest.first, ones.rest.rest.rest.first]
[1, 1, 1, 1]
>>> ones.rest is ones
True
```
      
Key:  
- Names point to objects.
- Assignment rebinds names.
- Mutation changes objects.  


 🔹 Functional Recursion vs. Mutating Recursion
- Functional recursion:
    - Think in terms of values
    - Always return something
    - Never modify self
- Mutating recursion:
    - Think in terms of pointers
    - Modify attributes
    - Often return None
---
## Iterator & Generator
- Stream
---
## Reading material for this course: 
- https://www.composingprograms.com/
---
## Additional Reading Material: 
- Python syntax and data structure: *"Dive Into Python3"* http://getpython3.com/diveintopython3/index.html
---
