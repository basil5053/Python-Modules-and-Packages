# 📝 Task – Python Modules and Packages

# 📂 Project Structure
```
my_project/
│
├── main.py
│
└── mypackage/
    ├── __init__.py
    ├── calc_utils.py
    └── weather_utils.py
```

---

## 📄 Instructions

1. **Inside `calc_utils.py`**
   - Create a function `square(n)` → returns the square of a number.  
   - Create a function `cube(n)` → returns the cube of a number.  

2. **Inside `weather_utils.py`**
   - Create a function `today_weather(city)` → prints today’s weather message for the city.  
   - Create a function `forecast(city)` → prints the weather forecast for the next days.  

3. **Inside `main.py`**
   - Import your modules from the package.  
   - Call the functions to:  
     - Calculate the square and cube of a number.  
     - Print the weather and forecast for a city of your choice.  

4. **Run your program**
   ```bash
   python main.py
   ```

---

## 🎯 Expected Outcome
When you run the program, you should see results like:
```
25
27
The weather in Riyadh is sunny with mild temperature.
The forecast for Riyadh is rainy for the next two days.
```
