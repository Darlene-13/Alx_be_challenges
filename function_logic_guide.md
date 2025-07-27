# The Logic Behind Function Design 🤔

## Step 1: What Am I Trying To Do?

### Ask Yourself These Questions:

**🤔 "Do I need to DO something or GET something back?"**

- **DO something** → Use `print()`, modify variables, change state
- **GET something back** → Use `return`

```python
# I want to DO something (just print)
def say_hello(name):
    print(f"Hello {name}!")  # No return needed

# I want to GET something back (calculate and return)
def add_numbers(a, b):
    result = a + b
    return result  # I need this value later!
```

---

## Step 2: The "Information Flow" Questions

**🤔 "Does my function need information from the outside?"**

- **YES** → Add parameters
- **NO** → No parameters needed

```python
# Needs info from outside
def greet_person(name, age):  # I need name and age!
    return f"Hi {name}, you're {age} years old"

# Doesn't need outside info
def get_current_time():  # I can figure this out myself
    import datetime
    return datetime.datetime.now()
```

**🤔 "Will the same information usually be the same?"**

- **Usually the same** → Use default parameters
- **Always different** → Required parameters

```python
# Usually pizza, but sometimes different
def order_food(food="pizza", quantity=1):
    return f"Ordering {quantity} {food}"

# Always need both pieces of info
def calculate_rectangle_area(length, width):  # No defaults make sense
    return length * width
```

---

## Step 3: The "Complexity" Questions

**🤔 "Am I doing ONE simple thing or managing MULTIPLE related things?"**

- **ONE simple thing** → Function
- **MULTIPLE related things** → Class with methods

```python
# One simple thing - just calculate
def calculate_tax(price, tax_rate):
    return price * tax_rate

# Multiple related things - manage a whole shopping cart
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0
    
    def add_item(self, item, price):
        self.items.append(item)
        self.total += price
    
    def get_total(self):
        return self.total
```

**🤔 "Do I need to remember information between function calls?"**

- **YES** → Use a class (objects remember state)
- **NO** → Just use functions

```python
# Need to remember the score between games
class GameScore:
    def __init__(self):
        self.score = 0
    
    def add_points(self, points):
        self.score += points
        return self.score

# Don't need to remember anything
def double_number(num):
    return num * 2
```

---

## Step 4: The "Return Value" Decision Tree

```
Do I need the result later? 
├── YES → Use return
│   ├── One value? → return value
│   ├── Multiple values? → return tuple/dict
│   └── Success/failure? → return True/False
└── NO → Just print or modify things
```

### Examples:

```python
# Need result later - RETURN IT
def calculate_discount(price, percent):
    discount = price * (percent / 100)
    return discount  # I'll use this number!

# Just showing info - PRINT IT  
def show_menu():
    print("1. Pizza")
    print("2. Burger")
    print("3. Salad")
    # No return - just displaying

# Need to know if something worked - RETURN BOOLEAN
def save_file(filename, data):
    try:
        with open(filename, 'w') as f:
            f.write(data)
        return True  # Success!
    except:
        return False  # Failed!

# Multiple pieces of info - RETURN DICT/TUPLE
def analyze_text(text):
    return {
        'word_count': len(text.split()),
        'char_count': len(text),
        'first_word': text.split()[0]
    }
```

---

## Step 5: The "Inner Function" Question

**🤔 "Do I have a helper task that ONLY makes sense inside this function?"**

```python
def process_student_grades(grades):
    # This helper only makes sense here
    def calculate_letter_grade(score):
        if score >= 90: return 'A'
        elif score >= 80: return 'B'
        elif score >= 70: return 'C'
        else: return 'F'
    
    # Use the helper for each grade
    letter_grades = []
    for grade in grades:
        letter_grades.append(calculate_letter_grade(grade))
    
    return letter_grades
```

---

## My Real Thinking Process (Example)

Let's say I want to make a "Bank Account" system:

### 🤔 Step 1: What am I doing?
"I want to manage money - deposit, withdraw, check balance"

### 🤔 Step 2: One thing or multiple?
"Multiple related things" → **CLASS**

### 🤔 Step 3: What info do I need to remember?
"Current balance, account holder name" → **Instance variables**

### 🤔 Step 4: What should return values be?
- Deposit: "Do I need to know new balance?" → **Return new balance**
- Withdraw: "Could this fail?" → **Return True/False or new balance**
- Check balance: "I need the number" → **Return balance**

```python
class BankAccount:
    def __init__(self, owner_name, starting_balance=0):
        self.owner = owner_name
        self.balance = starting_balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance  # Return new balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return False  # Can't withdraw - not enough money
        self.balance -= amount
        return self.balance  # Return new balance
    
    def check_balance(self):
        return self.balance  # Just return the number
    
    def get_account_info(self):
        return {  # Multiple pieces of info
            'owner': self.owner,
            'balance': self.balance
        }
```

---

## Quick Decision Cheat Sheet 📝

| If you want to... | Use... |
|------------------|---------|
| **Just show something** | `print()` (no return) |
| **Calculate and use later** | `return value` |
| **Check if something worked** | `return True/False` |
| **Get multiple pieces of info** | `return dict/tuple` |
| **Remember info between calls** | `class` |
| **Do one simple task** | `function` |
| **Manage related tasks** | `class` |
| **Sometimes use default info** | `default parameters` |
| **Helper that's only used inside** | `inner function` |

The key is asking: **"What does the person using this function NEED from it?"**