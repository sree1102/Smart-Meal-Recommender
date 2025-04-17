import streamlit as st
import pandas as pd
import random

# Load data
df = pd.read_csv("food.csv")

# Fix column names
df.columns = df.columns.str.strip()

# Title
st.title("🥗 AI-Powered Smart Meal Planner")

# Sidebar - User Inputs
st.sidebar.header("User Profile")
age = st.sidebar.number_input("Age", 18, 100, 25)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
weight = st.sidebar.number_input("Weight (kg)", 30, 200, 70)
height = st.sidebar.number_input("Height (cm)", 100, 250, 170)
activity = st.sidebar.selectbox("Activity Level", ["Sedentary", "Lightly active", "Moderately active", "Very active"])

goal = st.sidebar.selectbox("Goal", ["Maintain Weight", "Fat Loss", "Weight Gain"])

# BMI Calculation
bmi = round(weight / ((height / 100) ** 2), 1)
st.sidebar.markdown(f"**BMI:** {bmi}")

# BMR Calculation
if gender == "Male":
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
else:
    bmr = 10 * weight + 6.25 * height - 5 * age - 161

# Activity multiplier
activity_factors = {
    "Sedentary": 1.2,
    "Lightly active": 1.375,
    "Moderately active": 1.55,
    "Very active": 1.725
}
calories = bmr * activity_factors[activity]

# Goal adjustment
if goal == "Fat Loss":
    calories -= 300
elif goal == "Weight Gain":
    calories += 300

calories = int(calories)
st.sidebar.markdown(f"**Calorie Target: {calories} kcal/day**")

# Shuffle button
shuffle = st.button("Shuffle Meal Plan")

# Target per meal
meal_targets = {
    "Breakfast": 0.3,
    "Lunch": 0.35,
    "Dinner": 0.35
}

meal_plan = {}
macro_totals = {"Calories": 0, "Protein": 0, "Fat": 0, "Fiber": 0}

st.subheader("Your Daily Meal Plan")

for meal, fraction in meal_targets.items():
    cal_limit = calories * fraction
    filtered = df[df["Data.Kilocalories"] < cal_limit].copy()
    chosen = filtered.sample(2, random_state=None if shuffle else 42)

    meal_plan[meal] = chosen

    macro_totals["Calories"] += chosen["Data.Kilocalories"].sum()
    macro_totals["Protein"] += chosen["Data.Protein"].sum()
    macro_totals["Fat"] += chosen["Data.Fat.Total Lipid"].sum()
    macro_totals["Fiber"] += chosen["Data.Fiber"].sum()

    st.markdown(f"### {meal}")
    st.dataframe(chosen[["Description", "Data.Kilocalories", "Data.Protein", "Data.Fiber", "Data.Fat.Total Lipid"]].reset_index(drop=True))

# Show macro summary
st.markdown("## Macro Summary")
st.markdown(f"**Calories:** {round(macro_totals['Calories'], 1)} kcal")
st.markdown(f"**Protein:** {round(macro_totals['Protein'], 1)} g")
st.markdown(f"**Fat:** {round(macro_totals['Fat'], 1)} g")
st.markdown(f"**Fiber:** {round(macro_totals['Fiber'], 1)} g")

# Download button
final_df = pd.concat(meal_plan.values(), keys=meal_plan.keys()).reset_index(level=0).rename(columns={"level_0": "Meal"})
csv = final_df.to_csv(index=False)
st.download_button("📥 Download Meal Plan as CSV", data=csv, file_name="daily_meal_plan.csv", mime="text/csv")


# Export meal plan as CSV for Power BI usage
final_df.to_csv("meal_plan_export.csv", index=False)
