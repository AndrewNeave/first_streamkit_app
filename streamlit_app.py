import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('Build Your Own Smoothie')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#Set index
my_fruit_list = my_fruit_list.set_index('Fruit')
#Pick fruits
streamlit.multiselect('Pick some fruits:',list(my_fruit_list.index))
#Display Table on page
streamlit.dataframe(my_fruit_list)
