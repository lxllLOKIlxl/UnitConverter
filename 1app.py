import streamlit as st
import pandas as pd  # Для збереження історії

# Додавання стилів
st.markdown(
    """
    <style>
    .stTextInput, .stNumberInput, .stSelectbox {
        background: rgba(255, 255, 255, 0.8); 
        border: 2px solid #4CAF50; 
        border-radius: 8px; 
        padding: 5px;
    }
    .result-box {
        background: rgba(240, 255, 240, 0.9); 
        border: 2px solid #4CAF50; 
        border-radius: 8px;
        padding: 10px;
        margin-top: 10px;
        font-weight: bold;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Назва додатка
st.markdown("<h3 style='text-align: center;'>🌟 Конвертер одиниць вимірювання 🌟</h3>", unsafe_allow_html=True)

# Історія конвертацій
if "history" not in st.session_state:
    st.session_state["history"] = []

# Вибір категорії
category = st.selectbox("🔍 Оберіть категорію:", ["Довжина", "Вага", "Температура", "Об'єм", "Швидкість"])

# Конвертери
if category == "Довжина":
    st.subheader("📏 Конвертер довжини")
    units = {"Метри": 1, "Кілометри": 0.001, "Міліметри": 1000, "Міли": 0.000621371}
    from_unit = st.selectbox("Від:", list(units.keys()))
    to_unit = st.selectbox("До:", list(units.keys()))
    value = st.number_input("Введіть значення:", min_value=0.0, step=0.1)
    converted_value = value * units[to_unit] / units[from_unit]
    st.markdown(f'<div class="result-box">Результат: {converted_value} {to_unit} ✅</div>', unsafe_allow_html=True)
    st.session_state["history"].append(f"Довжина: {value} {from_unit} → {converted_value} {to_unit}")

elif category == "Вага":
    st.subheader("⚖️ Конвертер ваги")
    units = {"Кілограми": 1, "Грами": 1000, "Тонни": 0.001, "Фунти": 2.20462}
    from_unit = st.selectbox("Від:", list(units.keys()))
    to_unit = st.selectbox("До:", list(units.keys()))
    value = st.number_input("Введіть значення:", min_value=0.0, step=0.1)
    converted_value = value * units[to_unit] / units[from_unit]
    st.markdown(f'<div class="result-box">Результат: {converted_value} {to_unit} 🏋️‍♂️</div>', unsafe_allow_html=True)
    st.session_state["history"].append(f"Вага: {value} {from_unit} → {converted_value} {to_unit}")

elif category == "Температура":
    st.subheader("🌡️ Конвертер температури")
    from_unit = st.selectbox("Від:", ["Цельсій", "Фаренгейт", "Кельвін"])
    to_unit = st.selectbox("До:", ["Цельсій", "Фаренгейт", "Кельвін"])
    value = st.number_input("Введіть значення:", min_value=-273.15, step=0.1)

    if from_unit == "Цельсій" and to_unit == "Фаренгейт":
        converted_value = (value * 9/5) + 32
    elif from_unit == "Фаренгейт" and to_unit == "Цельсій":
        converted_value = (value - 32) * 5/9
    elif from_unit == "Цельсій" and to_unit == "Кельвін":
        converted_value = value + 273.15
    elif from_unit == "Кельвін" and to_unit == "Цельсій":
        converted_value = value - 273.15
    else:
        converted_value = value  # Якщо одиниці однакові

    st.markdown(f'<div class="result-box">Результат: {converted_value} {to_unit} 🔥</div>', unsafe_allow_html=True)
    st.session_state["history"].append(f"Температура: {value} {from_unit} → {converted_value} {to_unit}")

elif category == "Об'єм":
    st.subheader("💧 Конвертер об'єму")
    units = {"Літри": 1, "Мілілітри": 1000, "Галони": 0.264172}
    from_unit = st.selectbox("Від:", list(units.keys()))
    to_unit = st.selectbox("До:", list(units.keys()))
    value = st.number_input("Введіть значення:", min_value=0.0, step=0.1)
    converted_value = value * units[to_unit] / units[from_unit]
    st.markdown(f'<div class="result-box">Результат: {converted_value} {to_unit} 💧</div>', unsafe_allow_html=True)
    st.session_state["history"].append(f"Об'єм: {value} {from_unit} → {converted_value} {to_unit}")

elif category == "Швидкість":
    st.subheader("🚀 Конвертер швидкості")
    units = {"Метри/секунду": 1, "Кілометри/годину": 3.6, "Міли/годину": 2.23694}
    from_unit = st.selectbox("Від:", list(units.keys()))
    to_unit = st.selectbox("До:", list(units.keys()))
    value = st.number_input("Введіть значення:", min_value=0.0, step=0.1)
    converted_value = value * units[to_unit] / units[from_unit]
    st.markdown(f'<div class="result-box">Результат: {converted_value} {to_unit} 🚀</div>', unsafe_allow_html=True)
    st.session_state["history"].append(f"Швидкість: {value} {from_unit} → {converted_value} {to_unit}")

# Відображення історії
st.subheader("📜 Історія конвертацій")
if st.session_state["history"]:
    st.write(pd.DataFrame(st.session_state["history"], columns=["Операція"]))

# Підпис автора
st.markdown(
    "<div style='text-align: left; font-size: 12px; color: gray;'>Програму виконав Студент 1 курсу Мемех Олег</div>",
    unsafe_allow_html=True
)
