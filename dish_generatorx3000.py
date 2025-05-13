import streamlit as st 
import random

Meat = ["Chicken", "Frikadellen", "Köfte", "Skewers", "Salmon", "Cevapcici"]
Side = ["Cesar Salad", "Chickpea Salad", "Green beans", "Goat cheese with honey", "Asparagus", "Broccolini", "Baby carrots", "Sweet potato", "Butternut Squash"]

st.title("Honey, what's for dinner?")

Protein = None
Side_dish = None 

if st.button("Generated menue"):

   Protein = random.choice(Meat)
   Side_dish = random.choice(Side)

st.write(f"Todays selection: **{Protein}** with **{Side_dish}** Provecho!")
