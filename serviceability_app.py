import streamlit as st
import pandas as pd
from streamlit_extras.card import card

# Load the data
data = {
    "Cluster": ["Ahmedabad", "Bangalore", "Bangalore", "Bangalore", "Bangalore", "Bangalore", "Hyderabad", "Lucknow", "Lucknow", "Pune", "Ranchi", "Bhubaneswar", "Jamshedpur", "Bihar"],
    "City": ["Ahmedabad", "Bengaluru", "Mandya", "Hosur", "Tumkur", "Mysore", "Hyderabad", "Kanpur", "Lucknow", "Pune", "Ranchi", "Bhubaneswar", "Jamshedpur", "Patna"],
    "CG head": ["Dhwajal", "Sri Harsh", "No CG Head", "Sri Harsh", "Sri Harsh", "Sri Harsh", "Basha", "Arif", "Ravi Sharma", "Tejas", "Amit", "NithyaNanda", "Uday kumar Anand", "Abhishek Jha"],
    "Kirana Store": ["YES"]*14,
    "SUPERMARKET": ["YES"]*14,
    "Large Wholesaler": ["YES"]*14,
    "General Stores": ["YES"]*14,
    "Big Condiments": ["NO"]*14,
    "Restaurants, Hotel and Dhabas": ["YES", "YES", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "YES", "YES", "YES", "YES"],
    "Medical Shop": ["YES", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "YES", "YES", "NO"],
    "Bakery/Sweets shop/Confectionery": ["YES", "NO", "NO", "NO", "NO", "NO", "YES", "NO", "NO", "NO", "YES", "YES", "YES", "YES"],
    "Milk parlours": ["YES", "YES", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "YES", "YES", "NO"],
    "Fancy and Cosmetic stores": ["YES", "NO", "NO", "NO", "NO", "NO", "YES", "NO", "NO", "NO", "NO", "YES", "YES", "NO"],
    "Juice Centers": ["NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO"],
    "PG": ["NO", "YES", "YES", "YES", "YES", "YES", "YES", "NO", "NO", "NO", "NO", "NO", "NO", "NO"],
    "Tea Stalls/Hot Chips/ Distributor/ Caterers/Others": ["NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO"]
}

df = pd.DataFrame(data)

# Set page config
st.set_page_config(
    page_title="Serviceability Dashboard",
    page_icon="🛒",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .header {
        font-size: 36px !important;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        padding: 20px;
    }
    .subheader {
        font-size: 24px !important;
        color: #3498db;
        border-bottom: 2px solid #3498db;
        padding-bottom: 10px;
        margin-top: 20px;
    }
    .metric-card {
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        padding: 15px;
        margin-bottom: 15px;
    }
    .yes-service {
        background-color: #e8f5e9;
        padding: 8px;
        border-radius: 5px;
        color: #2e7d32;
        font-weight: bold;
    }
    .no-service {
        background-color: #ffebee;
        padding: 8px;
        border-radius: 5px;
        color: #c62828;
        font-weight: bold;
    }
    .service-item {
        padding: 8px 0;
        border-bottom: 1px solid #eee;
    }
    .select-box {
        background-color: #f5f5f5;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<div class="header">🛍️ Serviceability Dashboard</div>', unsafe_allow_html=True)
st.markdown("Select a city to view its serviceability details across different retail channels.")

# City Selection
with st.container():
    st.markdown('<div class="select-box">', unsafe_allow_html=True)
    selected_city = st.selectbox(
        "Select a City:", 
        df["City"].unique(),
        key="city_select"
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Filter data for selected city
result = df[df["City"] == selected_city].reset_index(drop=True)

# Basic Info Cards
st.markdown('<div class="subheader">Basic Information</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    card(
        title="Cluster",
        content=result["Cluster"][0],
        styles={
            "card": {
                "width": "100%",
                "height": "120px",
                "border-radius": "10px",
                "box-shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                "padding": "20px"
            },
            "title": {
                "font-size": "18px",
                "color": "#7f8c8d"
            },
            "content": {
                "font-size": "24px",
                "font-weight": "bold",
                "color": "#2c3e50"
            }
        }
    )

with col2:
    card(
        title="CG Head",
        content=result["CG head"][0],
        styles={
            "card": {
                "width": "100%",
                "height": "120px",
                "border-radius": "10px",
                "box-shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                "padding": "20px"
            },
            "title": {
                "font-size": "18px",
                "color": "#7f8c8d"
            },
            "content": {
                "font-size": "24px",
                "font-weight": "bold",
                "color": "#2c3e50"
            }
        }
    )

# Serviceability Section
st.markdown('<div class="subheader">Serviceability Details</div>', unsafe_allow_html=True)

service_cols = df.columns[3:]  # All columns after CG head

# Split into two columns for better layout
col1, col2 = st.columns(2)

for i, col in enumerate(service_cols):
    target_col = col1 if i % 2 == 0 else col2
    
    with target_col:
        status = result[col][0]
        if status == "YES":
            st.markdown(f"""
            <div class="service-item">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span>{col}</span>
                    <span class="yes-service">✓ Available</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="service-item">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span>{col}</span>
                    <span class="no-service">✗ Not Available</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #7f8c8d; font-size: 14px;">
    Serviceability Dashboard • Last updated: {date}
</div>
""".format(date=pd.Timestamp.now().strftime("%B %d, %Y")), unsafe_allow_html=True)
