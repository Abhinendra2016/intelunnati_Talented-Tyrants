import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import pickle
import base64
import plotly.express as px


model = pickle.load(open('model.pkl', 'rb'))



df = px.data.iris()

@st.cache
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("image.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: 100% 100%;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)



st.markdown(
    "<h1 class='left-corner'>Smart Mobile Phone Price Prediction</h1>",
    unsafe_allow_html=True
)

st.markdown("<h3>The Price Ranges are Categorized as follows:</h3>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .cost {
        font-size: 25px;
    }
    </style>
    """
    "<p><span class='cost'> Low Cost (Under 10k)</span></p>"
    "<p><span class='cost'> Medium Cost (Between 10k-30k)</span></p>"
    "<p><span class='cost'> High Cost (Between 30K-50k)</span></p>"
     "<p><span class='cost'> Very High Cost (Above 50K)</span></p>",

    unsafe_allow_html=True
)

ram = st.number_input("What is the RAM capacity of your phone in MB?")

int_memory = st.number_input("What is the storage capacity of your internal memory in GB?")

battery_power = st.number_input("Please provide the battery capacity in milliampere-hours (mAh).")


sim = st.selectbox("Does your phone support dual SIM cards?", ("Yes", "No"))
if sim == "Yes":
    dual_sim = 1
else:
    dual_sim = 0

speed = st.selectbox("Does your phone support 4G?", ("Yes", "No"))
if speed == "Yes":
    four_g = 1
else:
    four_g = 0

speed_2 = st.selectbox("Does your phone have other supporting networks?", ("Yes", "No"))

n_cores = st.number_input("How many processor cores does your phone have?")
pc = st.number_input("What is the resolution of the main camera in megapixels?")

mobile_wt = st.number_input("What is the weight of your phone in grams?")

px_height = st.number_input("What is the vertical pixel resolution?")

px_width = st.number_input("What is the horizontal pixel resolution?")

fc = st.number_input("What is the resolution of the front camera in megapixels?")


bluetooth = st.selectbox("Does your phone have Bluetooth functionality?", ("Yes", "No"))

if bluetooth == "Yes":
    blue = 1
else:
    blue = 0

clock_speed = st.number_input("What is the clock speed of the microprocessor?", value=2.0)



m_dep = st.number_input("What is the thickness or depth of your phone in cm?")



sch = st.number_input("What is the screen height in cm?")
scw = st.number_input("What is the screen width in cm?")
talk_time = st.number_input("What is the maximum duration of continuous talk time for your phone?")

if speed_2 == "Yes":
    three_g = 1
else:
    three_g = 0

ts = st.selectbox("Is your phone touch screen?", ("Yes", "No"))
if ts == "Yes":
    touch_screen = 1
else:
    touch_screen = 0

w = st.selectbox("Does your phone have Wi-Fi?", ("Yes", "No"))
if w == "Yes":
    wifi = 1
else:
    wifi = 0

hide_streamlit_style = """
<style>
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

data = [[battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory, m_dep, mobile_wt, n_cores, pc,
         px_height, px_width, ram, sch, scw, talk_time, three_g, touch_screen, wifi]]

result = model.predict(data)

if result[0] == 0:
    result_2 = "Low Cost"
elif result[0] == 1:
    result_2 = "Medium Cost"
elif result[0] == 2:
    result_2 = "High Cost"
else:
    result_2 = "Very High Cost"

if st.button('Submit'):
    st.write("<h3>Your phone falls within the specified category {} Price Range</h3>".format(result_2), unsafe_allow_html=True)
else:
    st.write('')

