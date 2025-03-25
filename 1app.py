import streamlit as st
import streamlit.components.v1 as components

# Додавання стилів
st.markdown(
    """
    <style>
    .stTextInput, .stNumberInput, .stSelectbox {
        background: rgba(255, 255, 255, 0.8);  /* Прозора оболонка */
        border: 2px solid #4CAF50;  /* Зелені контури */
        border-radius: 8px;  /* Заокруглені кути */
        padding: 5px;
    }
    .result-box {
        background: rgba(240, 255, 240, 0.9);  /* Світло-зелена підкладка */
        border: 2px solid #4CAF50;  /* Зелені контури */
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

# Назва вашого додатка
st.markdown("<h3 style='text-align: center;'>🌟 Конвертер одиниць вимірювання 🌟</h3>", unsafe_allow_html=True)

# Вибір категорії одиниць
category = st.selectbox("🔍 Оберіть категорію:", ["Довжина", "Вага", "Температура"])

# Конвертер довжини
if category == "Довжина":
    st.subheader("📏 Конвертер довжини")
    units = {"Метри": 1, "Кілометри": 0.001, "Міліметри": 1000, "Міли": 0.000621371}
    from_unit = st.selectbox("Від:", list(units.keys()))
    to_unit = st.selectbox("До:", list(units.keys()))
    value = st.number_input("Введіть значення:", min_value=0.0, step=0.1)
    converted_value = value * units[to_unit] / units[from_unit]
    st.markdown(f'<div class="result-box">Результат: {converted_value} {to_unit} ✅</div>', unsafe_allow_html=True)

# Конвертер ваги
elif category == "Вага":
    st.subheader("⚖️ Конвертер ваги")
    units = {"Кілограми": 1, "Грами": 1000, "Тонни": 0.001, "Фунти": 2.20462}
    from_unit = st.selectbox("Від:", list(units.keys()))
    to_unit = st.selectbox("До:", list(units.keys()))
    value = st.number_input("Введіть значення:", min_value=0.0, step=0.1)
    converted_value = value * units[to_unit] / units[from_unit]
    st.markdown(f'<div class="result-box">Результат: {converted_value} {to_unit} 🏋️‍♂️</div>', unsafe_allow_html=True)

# Конвертер температури
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

# Подяка з емодзі
st.write("💖 Дякуємо за використання нашого конвертера! 💖")

# Додавання підпису автора
st.markdown(
    "<div style='text-align: left; font-size: 12px; color: gray;'>Програму виконав Студент 1 курсу Мемих Олег</div>",
    unsafe_allow_html=True
)

