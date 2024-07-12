import time

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st


@st.cache_data
def get_data(csv_file) -> pd.DataFrame:
    return pd.read_csv(csv_file, delimiter=";")


placeholder = st.empty()

while True:
    run = get_data("visits_20-27-59_12-7-2024.csv")
    statistics = get_data("day_data.csv")
    with placeholder.container():

        most_frequent, longest, last = st.columns(3)
        by_time, statistics_data = st.columns(2)

        with most_frequent:
            visits = run.loc[run['id'] == statistics["most_frequent_visitor"].values[0]]
            visits_count = len(visits)
            gender = visits["gender"].values[0]
            age = round(sum(visits["age"]) / visits_count)
            visiting_time = sum(visits["time"])
            if gender == "Man":
                st.image("images/male.png")
            else:
                st.image("images/female.png")
            st.write(f"Время в кадре - {visiting_time}")
            st.write(f"Количество появлений в кадре - {visits_count}")
            st.write(f"Возраст - {age}")

        with longest:
            visits = run.loc[run['id'] == statistics["longest_visitor"].values[0]]
            visits_count = len(visits)
            gender = visits["gender"].values[0]
            age = round(sum(visits["age"]) / visits_count)
            visiting_time = sum(visits["time"])
            if gender == "Man":
                st.image("images/male.png")
            else:
                st.image("images/female.png")
            st.write(f"Время в кадре - {visiting_time}")
            st.write(f"Количество появлений в кадре - {visits_count}")
            st.write(f"Возраст - {age}")

        with last:
            visits = run.loc[run['id'] == run['id'].iat[-1]]
            visits_count = len(visits)
            gender = visits["gender"].values[0]
            age = round(sum(visits["age"]) / visits_count)
            visiting_time = sum(visits["time"])
            if gender == "Man":
                st.image("images/male.png")
            else:
                st.image("images/female.png")
            st.write(f"Время в кадре - {visiting_time}")
            st.write(f"Количество появлений в кадре - {visits_count}")
            st.write(f"Возраст - {age}")

        with by_time:
            st.markdown("Chart")
            fig = px.histogram(data_frame=run, x="visit_time")
            st.write(fig)

        with statistics_data:
            st.write(f"Среднее настроение - {str(statistics["average_mood"].values[0])}")
            st.write(f"Среднее время в кадре - {str(statistics["average_time"].values[0])}")
            st.write(f"Средний пол - {str(statistics["average_gender"].values[0])}")
            st.write(f"Средний возраст - {str(statistics["average_age"].values[0])}")
        time.sleep(2)
