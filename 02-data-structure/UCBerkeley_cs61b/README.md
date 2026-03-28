## Git
- saves copies of our code that can be retrieved
- git init
- git add
- git status
- git commit -m "message the user have about this commit update"
- git restore
---
## Java vs. Python
##### Python
```python
print("Hello World")
```
##### Java
```java
void main() {
    IO.println("Hello World");
}
```
- the code we want to run goes inside void main(){} function in Java
- in Java, we use { } to do beginnings and endings of thing instead of indentation
- in jv, statements end with semicolon


##### Python
```python
x = 0
while x < 5:
    print(x)
    x += 1
```
##### Java
```java
void main() {
    int x; // must first initialize the variable, we can also initialize using int x = 0
    x = 0;
    while (x < 5){
        IO.println(x);
        x += 1;
    }

    x = "horse"; // bug/error, type of a variable can not be changed
    String x = "horse";  // bug/error, the type of a variable can not be changed once the variable is declared/initialized
}
```
- in Java, we must initialize/declare variables and specify their type
- the type of a variable does not change/can not be changed
- types are checked by compiler and type errors are detected before the code even runs

##### Python
```python
def larger(x, y):
    if x > y:
        return x
    return y
```
##### Java
```java
int larger(int x, int y) {
    if (x > y){
        return x;
    }
    return y;
}

void main(){
    IO.print(larger(3, 10));
    IO.print(larger("cat", "dog"));  // bug/error, not allowed/inappropriate argument type
}
```
- in Java, the input parameters must be declared type when defining
- functions must also have a return type, and there is one and ONLY one return type
  - functions can only return one thing, and that one thing must have a specific type   
- functions also get type checked
---
## Class & Object Oriented Programming
- static
    - static functions are class methods/functions instead of instance methods. Static functions are accessed through class_name.static_func_name()
    - static variables define class variable instead of insstance attributes
    - static methods must access an instance variable/attribute via a specific instance

---
#### Pass by value
- Java ONLY **pass by value**, does NOT **pass by reference**
- information is stored in memory as a sequence of ones and zeros
    - e.g. 72 stored as 01001000, the letter H stored as 01001000 (same as the number 72), True stored as 00000001
- each Java type has a different way to interpret the bits:
    - 8 primitive types in Java: byte, short, int, long, float, double, boolean, char
    - everything else, including arrays, is a **reference type**
- given variables b and a:
    - b = a **copies** all the bits from a into b  
```java
Dog a = new Dog(name=lucky, weight=80);
Dog b;
b = a;
b.weight = 100
```
- now if we print(a.weight) we will see that a.weight = 100 too,
- in Java, **new** returns the address of the newly created object, therefore a is a reference, and when we copy b from a/assign b = a, we are copying the address of the object into b; thus when we change b, the object that a refers to changes too 
```java
int a = 100;
int b = a;
a = 50;
```
- since b = a copies all bits from a to b, when we assign int b = a we copies the bits for the integer 100 into b, then when we change a later, it does not affect b
```java
double average(double a, double b){
    return (a + b)/2;
}

void main(){
    double x = 5.5;
    double y = 10.5;
    double avg = average(x, y);
}
```
- passing parameters obeys the same rule: simply **copy the bits** to the new scope -- **pass by value**
    - therefore when we pass in x, y into average(a, b), a copies the value bits of double 5.5 from x and b copies the value bitd of double 10.5 from y 
---
## Resources
- Textbook: https://github.com/Berkeley-CS61B/sp26-gitbook
- Java Visualizer: https://cscircles.cemc.uwaterloo.ca/java_visualize/
---
Course start date: 2026/3/17
