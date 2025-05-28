import streamlit as st

# Configuración de página
st.set_page_config(
    page_title="DiDi Shop Processes",
    layout="wide",
    initial_sidebar_state="auto",
    page_icon="🍊"
)

# CSS personalizado
st.markdown("""
    <style>
        html, body, .main, section.main {
            background-color: #FFEEDB !important;
            color: #333333 !important;
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h2, h3 {
            color: #FF6600 !important;
        }
        .link-block {
            background-color: #FFF1E0;
            padding: 1.2rem;
            margin-bottom: 1rem;
            border-left: 6px solid #FF6600;
            border-radius: 8px;
            box-shadow: 1px 1px 3px rgba(0,0,0,0.05);
        }
        a {
            color: #0072CE !important;
            text-decoration: none !important;
        }
        a:hover {
            text-decoration: underline !important;
        }

        /* Alineación del selectbox con su label */
        .stSelectbox {
            margin-top: -10px !important;
            padding-bottom: 0 !important;
        }
        div[data-baseweb="select"] {
            border: 1px solid #FFB366 !important;
            border-radius: 8px !important;
            background-color: #FFF3E6 !important;
            width: 300px !important;
            margin-top: -5px;
        }
        div[data-baseweb="select"] * {
            font-family: 'Segoe UI', sans-serif;
            font-size: 16px;
        }

        /* Separación del título con el top */
        .block-container {
            padding-top: 3rem !important;
        }
    </style>
""", unsafe_allow_html=True)

# Encabezado
st.markdown("## 🍊 **DiDi Shop – Process Hub**")
st.markdown("Select a department and click on the corresponding resource.")
st.markdown("---")

# Diccionario de departamentos
departments = {
    "Communications": {
        "📄 Link to presentation": "https://docs.google.com/spreadsheets/d/1MarketingSheet",
        "📘 Link to SOP": "https://drive.google.com/file/d/branding_guide",
        "📁 Link to Google Drive": "https://docs.google.com/spreadsheets/d/17DYMCeRVqdAWDGQi--XU0NnkQ8EXjV6aV7cZw9OaBxk/edit?gid=663680167#gid=663680167"
    },
    "Retailer promotions": {
        "📄 Link to presentation": "https://docs.google.com/spreadsheets/d/1MarketingSheet",
        "📘 Link to SOP": "https://drive.google.com/file/d/branding_guide",
        "📁 Link to Google Drive": "https://docs.google.com/spreadsheets/d/17DYMCeRVqdAWDGQi--XU0NnkQ8EXjV6aV7cZw9OaBxk/edit?gid=663680167#gid=663680167"
    },
    "C-side meeting agenda": {
        "🗓️ Weekly agenda": "https://docs.google.com/spreadsheets/d/1MarketingSheet"
    },
    "C-side presentations": {
        "📊 Weekly Review": "https://docs.google.com/spreadsheets/d/1MarketingSheet",
        "🧠 Monthly Strategy": "https://docs.google.com/spreadsheets/d/1MarketingSheet",
        "📝 Postmortem": "https://docs.google.com/spreadsheets/d/1MarketingSheet"
    }
}

# Menú desplegable
st.markdown("**Select a department**")
department = st.selectbox("", list(departments.keys()))

# Mostrar enlaces del departamento seleccionado
st.subheader(f"📎 Available links for {department}:")
for name, url in departments[department].items():
    st.markdown(
        f"""
        <div class='link-block'>
            <a href="{url}" target="_blank">{name}</a>
        </div>
        """,
        unsafe_allow_html=True
    )
