#INPUTS: INGREDIENTS/DISH NAME ; DESIRED CALORIE RANGE/SERVING SIZE
#OUTPUT: 100 RECIPE NAMES WITH CALORIES AND URL

#!/usr/bin/env python
# coding: utf-8
# NOTES:
#	Display graph comparisons of daily nutrients, nutrients per serving, and nutrients in the entire dish
# 	
# 
# 
import json
import requests
import pandas as pd
import random
import plotly as pl


# trying out what imports we need for graphs
import matplotlib
import matplotlib.pyplot as plt
import chart_studio as plotly
import chart_studio.plotly as py
import plotly.express as px
import plotly.graph_objects as go

url = 'https://api.edamam.com/search' 
api_id = '3f5279fa'
api_key = 'd36b6a5258ab19d217c8d606494aa7c8'
to = 100

ingredients = input("Enter ingredients, or dish name: ")
print("")

desired_calories = input(" Enter desired calorie range (x-y) kcal; Put 0 if youhave no preference: ")

#For if calories don't matter
if desired_calories == 0: 
    desired_calories = ' '

params = {'q' : ingredients , 'app_id' : api_id , 
          'app_key' : api_key, 'calories (kcal)' : desired_calories , 
         'to' : to}
response = requests.get(url, params = params)
recipe = response.json()

#So the index does not go out of range
if recipe['count'] >= 100: 
    recipes_count = 100
else:
    recipes_count = recipe['count']
    
#Output

print("\n Recipes: \n") 
for i in range(0, 100):
    #So it prints random recipes relating
    r = random.randint(0, recipes_count-1)

     #Setting variable names
    dish_name = recipe['hits'][r]['recipe']['label']
    dish_calories = round(recipe['hits'][r]['recipe']['calories'], 2) 
    recipe_url = recipe['hits'][r]['recipe']['url']
    #Print statement
    print(dish_name, "\n Calories:", dish_calories, "\n URL:", recipe_url, '\n')



