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
Course start date: 2026/3/17
