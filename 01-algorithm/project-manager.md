Programming Project Setup
## 1️⃣ Create a project folder
* Keeps code, dependencies, and virtual environment organized

**Code**

```bash
mkdir my_project
cd my_project
```

---

## 2️⃣ Create a virtual environment (ONE per project)
* Isolates packages per project
* Prevents version conflicts (e.g., one project needs `openai==1.x`, another needs a different version)
* Avoids breaking other projects or system Python

**Rule**

> **One project = one virtual environment**

**Code**

```bash
python -m venv .venv
```

Creates:

```
.venv/
```

---

## 3️⃣ Activate the virtual environment

**Why**

* Ensures `pip install` installs packages **only for this project**
* Ensures `python` uses the project’s isolated environment

**How**

```bash
source .venv/bin/activate
```

**Check**

```bash
which python
```

Should show:

```
.../my_project/.venv/bin/python
```

---

## 4️⃣ Install project dependencies

**Why**

* Packages must be installed **inside the active virtual environment**

**How**

```bash
python -m pip install <package-name>
```

Example:

```bash
python -m pip install openai
```

---

## 5️⃣ Open the project in VS Code

**Why**

* VS Code needs to know which Python environment to use

**How**

```bash
code .
```

(or open the folder manually)

---

## 6️⃣ Select the correct Python interpreter (VS Code)

**Why**

* Prevents `ModuleNotFoundError`
* Ensures VS Code uses `.venv`, not system Python

**How**

1. `Command + Shift + P`
2. `Python: Select Interpreter`
3. Choose:

```
.venv/bin/python
```

---

## 7️⃣ Verify everything works

**Terminal**

```bash
python -c "import sys; print(sys.executable)"
```

**Expected**

```
.../my_project/.venv/bin/python
```

---

## 🧾 Project structure (recommended)

```
my_project/
├── .venv/
├── main.py
├── requirements.txt   (optional but recommended)
└── README.md
```

---

## 🔁 For every new project, repeat:

1. New folder
2. New `.venv`
3. Activate `.venv`
4. Install packages
5. Select interpreter in VS Code

---

## 🧠 Key mental model (remember this)

* **pyenv** → Python *version*
* **venv** → Python *packages per project*
* **pip installs into the currently active Python**

---

## 🚫 Common mistakes to avoid

* Installing packages without activating `.venv`
* Reusing one virtual environment for multiple projects
* Letting VS Code use system Python

---

If you want, I can:

* Turn this into a **1-page PDF note**
* Add **auto-activation** of `.venv`
* Add a **requirements.txt workflow**

Just tell me 👍
