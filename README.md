# Smart-Meal-Recommender

This project is a complete **end-to-end AI-powered meal planner** that combines:
- Python + Streamlit Web App  
- Power BI Interactive Dashboard  
- CSV Datasets for Meal Data and User Simulation  

Designed to recommend personalized meal plans based on user profile and visualize nutrition trends across goals, gender, meals, and age groups.

---

## 📁 Project Files

| File Name                    | Purpose                                                 |
|------------------------------|---------------------------------------------------------|
| `app.py`                     | Streamlit app to generate daily meal plan               |
| `food.csv`                   | Raw nutrition data used in the app                      |
| `full_meal_dataset.csv`      | Simulated user+meal dataset used for Power BI dashboard |
| `meal planner project.pbix`  | Final Power BI Dashboard file                           |

---

## Streamlit App Features (Python)

- Users enter their **age, gender, weight, height, activity, and goal**
- App calculates:
  - ✅ BMI
  - ✅ Calorie Target
- Auto-generates:
  - ✅ Breakfast, Lunch, Dinner recommendations
  - ✅ Total macro summary (Calories, Protein, Fat, Fiber)
- Includes:
  - Shuffle button
  - CSV download option for meal plan

---

## Power BI Dashboard Highlights

✅ Based on `full_meal_dataset.csv` with 1000+ records

**Key Visuals:**
- Donut chart: Goal-wise Meal Distribution  
- Gender-wise Meal Split  
- Line Chart: Macro Trends by Age  
- Stacked Column: Protein/Fat/Fiber by Meal  
- Pie Chart: Calories by Meal  
- Table: Full meal & user profile breakdown  
- Interactive Filters (Goal, Gender, Meal)

---

## Tools Used

- Python
- Streamlit
- Pandas
- Power BI
- CSV Files

---

## Dashboard Preview

![image](https://github.com/user-attachments/assets/39afd050-1e3b-4162-9d44-2241ee9987fa)
