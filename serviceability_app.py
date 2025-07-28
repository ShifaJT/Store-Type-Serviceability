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
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    /* Main container */
    .main {
        background-color: #f8f9fa;
    }
    
    /* Header */
    .header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #2c3e50;
        padding: 1rem 0;
        margin-bottom: 1.5rem;
        border-bottom: 1px solid #e0e0e0;
    }
    
    /* City selector */
    .city-selector {
        background-color: white;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 2rem;
    }
    
    /* Info cards */
    .info-card {
        background-color: white;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
        height: 100%;
    }
    
    .card-title {
        font-size: 1rem;
        color: #7f8c8d;
        margin-bottom: 0.5rem;
    }
    
    .card-value {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2c3e50;
    }
    
    /* Serviceability items */
    .service-container {
        background-color: white;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
    }
    
    .service-item {
        padding: 0.75rem 0;
        border-bottom: 1px solid #f0f0f0;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .service-item:last-child {
        border-bottom: none;
    }
    
    .service-name {
        font-weight: 500;
        color: #34495e;
    }
    
    .service-status {
        font-weight: 600;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.85rem;
    }
    
    .available {
        background-color: #e3f2fd;
        color: #1976d2;
    }
    
    .not-available {
        background-color: #ffebee;
        color: #d32f2f;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #95a5a6;
        font-size: 0.85rem;
        margin-top: 2rem;
        padding-top: 1rem;
        border-top: 1px solid #e0e0e0;
    }
    
    /* Responsive columns */
    @media (max-width: 768px) {
        .responsive-columns {
            flex-direction: column;
        }
    }
</style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<div class="header">📊 Retail Serviceability Dashboard</div>', unsafe_allow_html=True)

# City Selection
with st.container():
    st.markdown('<div class="city-selector">', unsafe_allow_html=True)
    selected_city = st.selectbox(
        "SELECT CITY", 
        df["City"].unique(),
        index=0,
        key="city_select"
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Filter data for selected city
result = df[df["City"] == selected_city].reset_index(drop=True)

# Basic Info Section
st.markdown("### Basic Information")
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="info-card">
        <div class="card-title">Cluster</div>
        <div class="card-value">{result["Cluster"][0]}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="info-card">
        <div class="card-title">CG Head</div>
        <div class="card-value">{result["CG head"][0]}</div>
    </div>
    """, unsafe_allow_html=True)

# Serviceability Section
st.markdown("### Serviceability Overview")
service_cols = df.columns[3:]  # All columns after CG head

# Split into two columns for better layout
col1, col2 = st.columns(2)

for i, col in enumerate(service_cols):
    target_col = col1 if i % 2 == 0 else col2
    
    with target_col:
        status = result[col][0]
        status_class = "available" if status == "YES" else "not-available"
        status_text = "Available" if status == "YES" else "Not Available"
        
        st.markdown(f"""
        <div class="service-item">
            <span class="service-name">{col}</span>
            <span class="service-status {status_class}">{status_text}</span>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    Retail Serviceability Dashboard • Last updated: {date}
</div>
""".format(date=pd.Timestamp.now().strftime("%B %d, %Y")), unsafe_allow_html=True)
