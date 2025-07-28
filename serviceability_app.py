import streamlit as st
import pandas as pd

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
    page_title="Retail Serviceability Dashboard",
    page_icon="🛍️",
    layout="wide"
)

# Custom CSS for horizontal layout
st.markdown("""
<style>
    .service-container {
        display: flex;
        overflow-x: auto;
        gap: 10px;
        padding: 15px 0;
    }
    .service-pill {
        white-space: nowrap;
        padding: 8px 12px;
        border-radius: 20px;
        font-size: 14px;
        font-weight: 500;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .available {
        background-color: #e8f5e9;
        color: #2e7d32;
    }
    .not-available {
        background-color: #ffebee;
        color: #c62828;
    }
    .metric-card {
        border-radius: 10px;
        padding: 15px;
        background-color: #f8f9fa;
        margin-bottom: 20px;
    }
    .card-title {
        font-size: 12px;
        color: #6c757d;
        margin-bottom: 5px;
    }
    .card-value {
        font-size: 18px;
        font-weight: bold;
        color: #343a40;
    }
</style>
""", unsafe_allow_html=True)

# App Header
st.title("🛍️ Retail Serviceability Dashboard")
st.markdown("Select a city to view serviceability across retail channels")

# City Selection
selected_city = st.selectbox("SELECT CITY", df["City"].unique())

# Filter data for selected city
result = df[df["City"] == selected_city].reset_index(drop=True)

# Basic Info Section
st.subheader("Basic Information")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="card-title">CLUSTER</div>
        <div class="card-value">{}</div>
    </div>
    """.format(result["Cluster"][0]), unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="card-title">CG HEAD</div>
        <div class="card-value">{}</div>
    </div>
    """.format(result["CG head"][0]), unsafe_allow_html=True)

# Serviceability Section - Horizontal Layout
st.subheader("Serviceability Status")
st.markdown("Scroll horizontally to view all channels →")

service_cols = df.columns[3:]  # All columns after CG head

# Create horizontal scrollable container
st.markdown('<div class="service-container">', unsafe_allow_html=True)

for col in service_cols:
    status = result[col][0]
    status_class = "available" if status == "YES" else "not-available"
    status_text = "✓" if status == "YES" else "✗"
    
    st.markdown(f"""
    <div class="service-pill {status_class}" title="{col}">
        {col.split('/')[0].split(',')[0][:15]} {status_text}
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption(f"Last updated: {pd.Timestamp.now().strftime('%B %d, %Y')}")
