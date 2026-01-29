# 📘 Common CS Language Syntax

---

## 🐍 Python

### Variables

```python
x = 10
name = "Alice"
```

### Conditionals

```python
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")
```

### Loops

```python
for i in range(5):
    print(i)

while x > 0:
    x -= 1
```

### Functions

```python
def add(a, b):
    return a + b
```

### Lists / Dictionaries

```python
nums = [1, 2, 3]
info = {"name": "Alice", "age": 20}
```

---

## ☕ Java

### Variables

```java
int x = 10;
String name = "Alice";
```

### Conditionals

```java
if (x > 0) {
    System.out.println("positive");
} else if (x == 0) {
    System.out.println("zero");
} else {
    System.out.println("negative");
}
```

### Loops

```java
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}
```

### Functions (Methods)

```java
static int add(int a, int b) {
    return a + b;
}
```

---

## 🧠 C

### Variables

```c
int x = 10;
char name[] = "Alice";
```

### Conditionals

```c
if (x > 0) {
    printf("positive");
} else if (x == 0) {
    printf("zero");
} else {
    printf("negative");
}
```

### Loops

```c
for (int i = 0; i < 5; i++) {
    printf("%d", i);
}
```

### Functions

```c
int add(int a, int b) {
    return a + b;
}
```

---

## C++

### Variables

```cpp
int x = 10;
string name = "Alice";
```

### Conditionals

```cpp
if (x > 0) {
    cout << "positive";
}
```

### Loops

```cpp
for (int i = 0; i < 5; i++) {
    cout << i;
}
```

### Functions

```cpp
int add(int a, int b) {
    return a + b;
}
```

---

## 🌐 JavaScript

### Variables

```js
let x = 10;
const name = "Alice";
```

### Conditionals

```js
if (x > 0) {
  console.log("positive");
}
```

### Loops

```js
for (let i = 0; i < 5; i++) {
  console.log(i);
}
```

### Functions

```js
function add(a, b) {
  return a + b;
}
```

---



## 📌 Notes

* Python uses **indentation**, not braces
* C / C++ / Java require **semicolons**
* JavaScript is flexible but dangerous without `const` / `let`
* Rust enforces **memory safety at compile time**

Here’s a **general, language-agnostic function declaration note**, clean and ready for **GitHub**.

---

# Function Declaration Syntax (General Guide)

## What Is a Function?

A **function** is a reusable block of code that:

* Performs a specific task
* May accept inputs (**parameters**) (if not, function_name(**void**))
* May return an output (**return value**) (if not, **void** function_name())

---

## General Syntax (Abstract)

```text
return_type function_name(parameter_type parameter_name, ...)
{
    function body
    return value
}
```

---

## Python

```python
def function_name(parameter1, parameter2):
    """Optional docstring"""
    # function body
    return result
```

### Example

```python
def add(a, b):
    return a + b
```

**Notes**

* No return type declaration
* Indentation defines scope
* `return` is optional

---

## C

```c
return_type function_name(type parameter1, type parameter2)
{
    // function body
    return value;
}
```

### Example

```c
int add(int a, int b)
{
    return a + b;
}
```

**Notes**

* Return type is required
* Semicolons required
* Function must be declared before use

---

## C++

```cpp
return_type function_name(type parameter1, type parameter2)
{
    return value;
}
```

Same syntax as C, but supports:

* Function overloading
* Default parameters

---

## Java

```java
access_modifier return_type functionName(type param1, type param2)
{
    return value;
}
```

### Example

```java
public static int add(int a, int b)
{
    return a + b;
}
```

---

## JavaScript

```javascript
function functionName(param1, param2) {
    return value;
}
```

### Arrow Function

```javascript
const add = (a, b) => a + b;
```

---

## Parameters vs Arguments

| Term          | Meaning                         |
| ------------- | ------------------------------- |
| **Parameter** | Variable in function definition |
| **Argument**  | Actual value passed to function |

---

## Return Values

* A function may return:

  * A value
  * Multiple values (language-dependent)
  * Nothing (`void` / `None` / `undefined`)

---

## Function Declaration vs Call

### Declaration

```python
def greet():
    print("Hello")
```

### Call

```python
greet()
```

---


## Scope (Very Important)

### What Is Scope?

**Scope** defines **where a variable can be accessed** in a program.

---

### Common Scope Types

| Scope      | Description                                                      |
| ---------- | ---------------------------------------------------------------- |
| **Global** | Defined outside functions, accessible everywhere                 |
| **Local**  | Defined inside a function, accessible only within it             |
| **Block**  | Defined inside a block (`{}` or indentation), language-dependent |

---

### Scope Example (Conceptual)

```text
global_variable

function() {
    local_variable
}
```

* `global_variable` → accessible inside and outside the function
* `local_variable` → accessible **only inside** the function

---

## Python

### Function Syntax

```python
def function_name(parameter1, parameter2):
    """Optional docstring"""
    # function body
    return result
```

### Scope in Python

```python
x = 10  # global

def example():
    y = 5  # local
    print(x)  # OK
    print(y)  # OK

example()
print(x)  # OK
print(y)  # ❌ NameError
```

**Notes**

* Python uses **function scope**
* No block scope for `if`, `for`, `while`
* Use `global` or `nonlocal` only when necessary

---

## C

### Function Syntax

```c
return_type function_name(type parameter1, type parameter2)
{
    // function body
    return value;
}
```

### Scope in C

```c
int x = 10;  // global

int main() {
    int y = 5;  // local
    if (y > 0) {
        int z = 3;  // block scope
    }
}
```

**Notes**

* C has **global**, **function**, and **block** scope
* Variables exist only within their declared braces `{}`

---

## C++

* Same scopes as C
* Adds **class scope** and **namespace scope**

---

## Java

```java
public static int add(int a, int b)
{
    int sum = a + b; // local
    return sum;
}
```

**Scope Levels**

* Class scope
* Method (function) scope
* Block scope

---

## JavaScript

```javascript
let x = 10; // global

function example() {
    let y = 5; // function scope
    if (true) {
        let z = 3; // block scope
    }
}
```

**Notes**

* `let` / `const` → block scope
* `var` → function scope (avoid)

---

## Parameters and Scope

```python
def add(a, b):
    return a + b
```

* `a` and `b` are **local variables**
* They exist **only inside** the function

---

## Function Declaration vs Call

### Declaration

```python
def greet():
    message = "Hello"  # local
    print(message)
```

### Call

```python
greet()
# message ❌ not accessible here
```

---

## Best Practices

* Minimize global variables
* Prefer local scope
* Pass data via parameters
* Avoid modifying globals unless intentional

---

## TL;DR

* Functions create **their own scope**
* Variables live only within their scope
* Scope rules vary by language, but the concept is universal
* Good scope control = fewer bugs

---

## Best Practices

* Use **descriptive function names**
* Keep functions **small and focused**
* One function = **one responsibility**
* Document inputs and outputs




