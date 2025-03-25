import streamlit as st

# Назва вашого додатка
st.title("Конвертер одиниць вимірювання")

# Вибір категорії одиниць
category = st.selectbox("Оберіть категорію:", ["Довжина", "Вага", "Температура"])

# Конвертер довжини
if category == "Довжина":
    units = {"Метри": 1, "Кілометри": 0.001, "Міліметри": 1000, "Міли": 0.000621371}
    from_unit = st.selectbox("Від:", list(units.keys()))
    to_unit = st.selectbox("До:", list(units.keys()))
    value = st.number_input("Введіть значення:", min_value=0.0, step=0.1)
    converted_value = value * units[to_unit] / units[from_unit]
    st.write(f"Результат: {converted_value} {to_unit}")

# Конвертер ваги
elif category == "Вага":
    units = {"Кілограми": 1, "Грами": 1000, "Тонни": 0.001, "Фунти": 2.20462}
    from_unit = st.selectbox("Від:", list(units.keys()))
    to_unit = st.selectbox("До:", list(units.keys()))
    value = st.number_input("Введіть значення:", min_value=0.0, step=0.1)
    converted_value = value * units[to_unit] / units[from_unit]
    st.write(f"Результат: {converted_value} {to_unit}")

# Конвертер температури
elif category == "Температура":
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
    
    st.write(f"Результат: {converted_value} {to_unit}")

# Вивід підсумкового результату
st.write("Дякуємо за використання нашого конвертера!")
