## Higher Order Function
---
## Recursion

🔹 Tree

---
## Class   
- Attributes
    - class attribute
    - instance attribute 
- Methods
    - methods are also instance attributes
    - methods vs. functions 
    
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
## Interpreter Design 
🔹 Overall Structure
## REPL
```
(textbook chapter 3 && lab 10)
Read
     |
     v
Evaluate
     |
     v
Print
Loop
```
🔹 Functions
- tokenizer()
    - raw string -> tokens
```python
>>> s = "(+ 2 3)"
>>> tokenize(s)
['(', '+', '2', '3', ')']
```
- parser()
    - tokens -> nested Pair structure / Tree structure
    - Converting parentheses into a linked-tree structure
        - Parentheses define nesting
        - Each '(' creates a new recursive level.
```python
>>> s = "(* 2 (+ 3 4))"
>>> tokenize(s)
['(', '*', '2', '(', '+', '3', '4', ')', ')']
>>> parse(tokenize(s))
Pair('*', Pair(2, Pair(Pair('+', Pair(3, Pair(4, nil))), nil)))
```
Evaluation
- evaluate()
```
scheme_eval(expr):

atom?
   return value

symbol?
   lookup

list?
   special form?
        handle specially
   otherwise:
        eval operator
        eval operands
        apply
```
```python
def scheme_eval(expr, env):

    # 1. Self-evaluating expressions
    if scheme_self_evaluating(expr):
        return expr

    # 2. Symbols (variable lookup)
    if scheme_symbolp(expr):
        return env.lookup(expr)

    # 3. Lists (procedure calls or special forms)
    if not scheme_listp(expr):
        raise SchemeError("malformed list")

    first = expr.first
    rest = expr.rest

    # 4. Special forms
    if scheme_symbolp(first) and first in SPECIAL_FORMS:
        return SPECIAL_FORMS[first](rest, env)

    # 5. Procedure call
    operator = scheme_eval(first, env)
    operands = rest.map(lambda x: scheme_eval(x, env))

    return scheme_apply(operator, operands, env)
```
- apply()
    - 1️⃣ PrimitiveProcedure
    - 2️⃣ LambdaProcedure (user-defined functions)
    - 3️⃣ MuProcedure (later in project)
    - define 3 corresponding classes to handle 3 different kinds of procedures
```python
def scheme_apply(procedure, args, env):

    if isinstance(procedure, PrimitiveProcedure):
        ...

    elif isinstance(procedure, LambdaProcedure):
        ...

    elif isinstance(procedure, MuProcedure):
        ...
```
- mutual recursive call between evaluate(exprssion, current environment) && apply(procedure being called, arguments, env)
```
scheme_eval
     |
     v
evaluate operator & operands
     |
     v
scheme_apply
     |
     v
evaluate procedure body
     |
     v
scheme_eval again

example
>>> (+ (* 2 3) 4)
scheme_eval (+ (* 2 3) 4)
    |
    +-- scheme_eval (* 2 3)
    |        |
    |        +-- scheme_apply (*, (2 3))
    |
    +-- scheme_apply (+, (6 4))
```
- question: there are two evaluation functions -- scheme_eval() and eval_all(), why do we need these two functions? what is the difference between them? Since scheme_eval() is a recursive call, wouldn't eval_all() just be redundant?

🔹 Objects / Classes
- Pair / Linked List
    -  attributes
- Frame
    - keeps track of the bindngs
    - attributes
        - bindings = {}, a dictionary containing bindings[symbol] = value elements
        - parent = None or another Frame object
    - methods
        - define(symbol, value): add (symbol, value) pair to current Frame's bindings
        - lookup(symbol): return the value bound to symbol or parent(s)

🔹 Built-in Functions

🔹 Special Forms  
    - if
    - define
    - quote
    - begin
    - lambda
        - user defined functions 
    - and
    - or
    - cond
    - let
``` python
SPECIAL_FORMS = {
    'and': do_and_form,
    'begin': do_begin_form,
    'cond': do_cond_form,
    'define': do_define_form,
    'if': do_if_form,
    'lambda': do_lambda_form,
    'let': do_let_form,
    'or': do_or_form,
    'quote': do_quote_form,
    'quasiquote': do_quasiquote_form,
    'unquote': do_unquote,
    'mu': do_mu_form,
}
```
---
## SQL
- A SELECT statement describes an output table based on input rows. To write one:
    - 1. Describe the input rows using FROM and WHERE clauses.
      2. Group those rows and determine which groups should appear as output rows using GROUP BY and HAVING clauses.
      3. Format and order the output rows and columns using SELECT and ORDER BY
clauses
---
## Distributed Computing (Chapter. 4)
- Large-scale data processing applications often coordinate effort among multiple computers. A distributed computing application is one in which multiple interconnected but independent computers coordinate to perform a joint computation.
- Message protocol: computers adopt a message protocol that endows meaning to sequences of bytes in order to transfer messages between different computers
    - Message protocols are not particular programs or software libraries. Instead, they are rules that can be applied by a variety of programs, even written in different programming languages. As a result, computers with vastly different software systems can participate in the same distributed system, simply by conforming to the message protocols that govern the system.
- Client/Server architecture/system
    - A drawback of client-server systems is that computing resources become scarce if there are too many clients. Clients increase the demand on the system without contributing any computing resources. 
- Peer-to-Peer system
    - a more equal division of labor
    - The term peer-to-peer is used to describe distributed systems in which labor is divided among all the components of the system. All the computers send and receive data, and they all contribute some processing power and memory. As a distributed system increases in size, its capacity of computational resources increases.
## Distributed Data Processing
- Sometimes a data set too large to be processed by a single machine is instead distributed among many machines, each of which process a portion of the dataset.
- MapReduce && Hadoop
- Parallel Computing
    - From the 1970s through the mid-2000s, the speed of individual processor cores grew at an exponential rate. Much of this increase in speed was accomplished by increasing the clock frequency, the rate at which a processor performs basic operations. In the mid-2000s, however, this exponential increase came to an abrupt end, due to power and thermal constraints, and the speed of individual processor cores has increased much more slowly since then. Instead, CPU manufacturers began to place multiple cores in a single processor, enabling more operations to be performed concurrently. 
---
## Textbook for this course: 
- https://www.composingprograms.com/
---
## Additional Reading Material: 
- Python syntax and data structure: *"Dive Into Python3"* http://getpython3.com/diveintopython3/index.html
- *"Structure and Interpretation of Computer Programs"*
---
## Website tools:
- Python environment vitualizer: Python Tutor  
https://pythontutor.com/visualize.html#mode=display
- Scheme environment vitualizer & interpreter:  
code.cs61a.org
