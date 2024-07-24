import time

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)

placeholder = st.empty()


def translate_gender(gender):
    if gender == "Man":
        return "Мужской"
    else:
        return "Женский"


def translate_mood(mood):
    if mood == "angry":
        return "Раздраженное"
    elif mood == "sad":
        return "Грустное"
    elif mood == "surprise":
        return "Удивленное"
    elif mood == "fear":
        return "Испуганное"
    elif mood == "happy":
        return "Счастливое"
    elif mood == "disgust":
        return "Брезгливое"
    else:
        return "Нейтральное"


while True:
    st.markdown("""
                    <style>
                    p {
                        font-size:30px;       
                    }
                    [data-testid=column] {
                        text-align: center;
                    }
                    h1 {
                        margin-left: 5%;
                    }
                    img {
                        margin-left: 55%;
                    }
                    </style>
                    """, unsafe_allow_html=True)
    run = pd.read_csv("visits_20-27-59_12-7-2024.csv", delimiter=";")
    statistics = pd.read_csv("day_data.csv", delimiter=";")
    with placeholder.container():

        most_frequent, longest, last = st.columns(3, gap='medium', vertical_alignment='center')
        by_time, statistics_data = st.columns(2, gap='medium', vertical_alignment='center')

        with most_frequent:
            st.title("Чаще всех в кадре")
            visits = run.loc[run['id'] == statistics["most_frequent_visitor"].values[0]]
            visits_count = len(visits)
            gender = visits["gender"].values[0]
            age = round(sum(visits["age"]) / visits_count)
            visiting_time = sum(visits["time"])
            if gender == "Man":
                st.image("images/male.png", width=300)
            else:
                st.image("images/female.png", width=300)
            st.write(f"Время в кадре - {visiting_time}c")
            st.write(f"Количество появлений в кадре - {visits_count}")
            st.write(f"Возраст - {age}")

        with longest:
            st.title("Дольше всех в кадре")
            visits = run.loc[run['id'] == statistics["longest_visitor"].values[0]]
            visits_count = len(visits)
            gender = visits["gender"].values[0]
            age = round(sum(visits["age"]) / visits_count)
            visiting_time = sum(visits["time"])
            if gender == "Man":
                st.image("images/male.png", width=300)
            else:
                st.image("images/female.png", width=300)
            st.write(f"Время в кадре - {visiting_time}c")
            st.write(f"Количество появлений в кадре - {visits_count}")
            st.write(f"Возраст - {age}")

        with last:
            st.title("Последний в кадре")
            visits = run.loc[run['id'] == run['id'].iat[-1]]
            visits_count = len(visits)
            gender = visits["gender"].values[0]
            age = round(sum(visits["age"]) / visits_count)
            visiting_time = sum(visits["time"])
            if gender == "Man":
                st.image("images/male.png", width=300)
            else:
                st.image("images/female.png", width=300)
            st.write(f"Время в кадре - {visiting_time}c")
            st.write(f"Количество появлений в кадре - {visits_count}")
            st.write(f"Возраст - {age}")

        with by_time:
            fig = px.histogram(data_frame=run, x="visit_time")
            fig.update_layout(
                bargap=0.2,
                xaxis_title="Время",
                yaxis_title="Количество посещений",
                font=dict(
                    size=50,
                    color="Black"
                )
            )
            st.write(fig)

        with statistics_data:
            st.write(f"Самое частое настроение - {translate_mood(str(statistics["average_mood"].values[0]))}")
            st.write(f"Среднее время в кадре - {str(round(statistics["average_time"].values[0], 2))}c")
            st.write(f"Наиболее частый пол - {translate_gender(str(statistics["average_gender"].values[0]))}")
            st.write(f"Средний возраст - {str(round(statistics["average_age"].values[0]))}")
        time.sleep(5)
