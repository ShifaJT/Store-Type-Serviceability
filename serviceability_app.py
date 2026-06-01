import streamlit as st
import pandas as pd

# Load full dataset
data = {
    "Cluster": ["Ahmedabad", "Bangalore", "Bangalore", "Bangalore", "Bangalore", "Bangalore", "Hyderabad", "Lucknow", "Lucknow", "Pune", "Ranchi", "Bhubaneswar", "Jamshedpur", "Bihar", "Chennai"],
    "City": ["Ahmedabad", "Bengaluru", "Mandya", "Hosur", "Tumkur", "Mysore", "Hyderabad", "Kanpur", "Lucknow", "Pune", "Ranchi", "Bhubaneswar", "Jamshedpur", "Patna", "Chennai"],
    "CG head": ["Dhwajal", "Sri Harsh", "No CG Head", "Sri Harsh", "Sri Harsh", "Sri Harsh", "Basha", "Arif", "Ravi Sharma", "Tejas", "Amit", "NithyaNanda", "Uday kumar Anand", "Abhishek Jha", "No CG Head"],

    "Kirana Store": ["YES"] * 15,
    "SUPERMARKET": ["YES"] * 14 + ["NO"],
    "Large Wholesaler": ["YES"] * 15,
    "General Stores": ["YES"] * 15,
    "Big Condiments": ["NO"] * 15,

    "Restaurants": ["YES", "YES", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "YES", "YES", "YES", "YES", "NO"],

    "Medical": ["YES", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "YES", "YES", "NO", "NO"],

    "Bakery": ["YES", "NO", "NO", "NO", "NO", "NO", "YES", "NO", "NO", "NO", "YES", "YES", "YES", "YES", "NO"],

    "Milk Parlors": ["YES", "YES", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "YES", "YES", "NO", "NO"],

    "Cosmetics": ["YES", "NO", "NO", "NO", "NO", "NO", "YES", "NO", "NO", "NO", "NO", "YES", "YES", "NO", "NO"],

    "Juice Centers": ["NO"] * 15,

    "PG": ["NO", "YES", "YES", "YES", "YES", "YES", "YES", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO"],

    "Tea Stalls": ["NO"] * 15
}

df = pd.DataFrame(data)

# Configuration
st.set_page_config(
    page_title="National Serviceability Dashboard",
    page_icon="🌐",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    :root {
        --primary: #3b82f6;
        --success: #10b981;
        --danger: #ef4444;
    }
    
    .dashboard-title {
        font-size: 2rem;
        font-weight: 700;
        color: #1e3a8a;
        margin-bottom: 0.5rem;
    }
    
    .city-header {
        background-color: #f0f9ff;
        border-left: 4px solid var(--primary);
        padding: 12px 20px;
        margin: 15px 0;
        border-radius: 4px;
    }
    
    .service-card {
        background: white;
        border-radius: 8px;
        padding: 12px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin-bottom: 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .service-name {
        font-weight: 500;
        color: #1f2937;
        flex: 1;
    }
    
    .service-status {
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 14px;
    }
    
    .available {
        background-color: #d1fae5;
        color: #065f46;
    }
    
    .unavailable {
        background-color: #fee2e2;
        color: #991b1b;
    }
    
    .service-columns {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 15px;
    }
    
    body, .stSelectbox > div > div {
        color: #1f2937 !important;
    }
</style>
""", unsafe_allow_html=True)

# Dashboard Header
st.markdown('<p class="dashboard-title">🌐 National Retail Serviceability Dashboard</p>', unsafe_allow_html=True)
st.markdown("Comprehensive channel availability across all operational cities")

# City Selection
selected_city = st.selectbox(
    "SELECT CITY",
    df["City"].unique(),
    index=0
)

# Selected City Header
st.markdown(f"""
<div class="city-header">
    <h3 style="color: #1e40af; margin:0;">
        📍 Currently Viewing: <strong>{selected_city}</strong>
    </h3>
</div>
""", unsafe_allow_html=True)

# Get city data
city_data = df[df["City"] == selected_city].iloc[0]

# Key Metrics
st.markdown("### City Overview")
cols = st.columns(4)
cols[0].metric("Cluster", city_data["Cluster"])
cols[1].metric("CG Head", city_data["CG head"])
cols[2].metric(
    "Available Services",
    f"{sum(1 for x in city_data[3:] if x == 'YES')}/{len(df.columns[3:])}"
)
cols[3].metric(
    "Coverage",
    f"{sum(1 for x in city_data[3:] if x == 'YES') / len(df.columns[3:]) * 100:.0f}%"
)

# Serviceability Display
st.markdown("### Service Channel Status")
service_cols = df.columns[3:]

split_index = len(service_cols) // 2
group1 = service_cols[:split_index]
group2 = service_cols[split_index:]

col1, col2 = st.columns(2)

with col1:
    for service in group1:
        status = city_data[service]
        st.markdown(f"""
        <div class="service-card">
            <div class="service-name">{service}</div>
            <div class="service-status {'available' if status == 'YES' else 'unavailable'}">
                {'Available' if status == 'YES' else 'Not Available'}
            </div>
        </div>
        """, unsafe_allow_html=True)

with col2:
    for service in group2:
        status = city_data[service]
        st.markdown(f"""
        <div class="service-card">
            <div class="service-name">{service}</div>
            <div class="service-status {'available' if status == 'YES' else 'unavailable'}">
                {'Available' if status == 'YES' else 'Not Available'}
            </div>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption(f"Data current as of {pd.Timestamp.now().strftime('%d %B %Y')} | v2.3")
