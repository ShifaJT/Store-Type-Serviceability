import streamlit as st
import pandas as pd

# Load full dataset
data = {
    "Cluster": ["Ahmedabad", "Bangalore", "Bangalore", "Bangalore", "Bangalore", "Bangalore", "Hyderabad", "Lucknow", "Lucknow", "Pune", "Ranchi", "Bhubaneswar", "Jamshedpur", "Bihar"],
    "City": ["Ahmedabad", "Bengaluru", "Mandya", "Hosur", "Tumkur", "Mysore", "Hyderabad", "Kanpur", "Lucknow", "Pune", "Ranchi", "Bhubaneswar", "Jamshedpur", "Patna"],
    "CG head": ["Dhwajal", "Sri Harsh", "No CG Head", "Sri Harsh", "Sri Harsh", "Sri Harsh", "Basha", "Arif", "Ravi Sharma", "Tejas", "Amit", "NithyaNanda", "Uday kumar Anand", "Abhishek Jha"],
    "Kirana Store": ["YES"]*14,
    "SUPERMARKET": ["YES"]*14,
    "Large Wholesaler": ["YES"]*14,
    "General Stores": ["YES"]*14,
    "Big Condiments": ["NO"]*14,
    "Restaurants": ["YES", "YES", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "YES", "YES", "YES", "YES"],
    "Medical": ["YES", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "YES", "YES", "NO"],
    "Bakery": ["YES", "NO", "NO", "NO", "NO", "NO", "YES", "NO", "NO", "NO", "YES", "YES", "YES", "YES"],
    "Milk Parlors": ["YES", "YES", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "NO", "YES", "YES", "NO"],
    "Cosmetics": ["YES", "NO", "NO", "NO", "NO", "NO", "YES", "NO", "NO", "NO", "NO", "YES", "YES", "NO"],
    "Juice Centers": ["NO"]*14,
    "PG": ["NO", "YES", "YES", "YES", "YES", "YES", "YES", "NO", "NO", "NO", "NO", "NO", "NO", "NO"],
    "Tea Stalls": ["NO"]*14
}
df = pd.DataFrame(data)

# Configuration
st.set_page_config(
    page_title="National Serviceability Dashboard",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    :root {
        --primary: #3b82f6;
        --success: #10b981;
        --danger: #ef4444;
        --card-bg: #ffffff;
    }
    
    /* Modern metric cards */
    div[data-testid="metric-container"] {
        border: 1px solid #e5e7eb !important;
        border-radius: 10px !important;
        padding: 20px !important;
        background: white !important;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    
    /* Dashboard header */
    .dashboard-title {
        font-size: 2rem;
        font-weight: 700;
        color: #1e3a8a;
        margin-bottom: 0.5rem;
    }
    
    /* Service grid */
    .service-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
        gap: 15px;
        margin: 2rem 0;
    }
    
    .service-card {
        background: white;
        border-radius: 10px;
        padding: 18px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border-left: 4px solid var(--primary);
    }
    
    .service-status {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 14px;
        margin-top: 8px;
    }
    
    .available {
        background-color: #d1fae5;
        color: #065f46;
    }
    
    .unavailable {
        background-color: #fee2e2;
        color: #991b1b;
    }
    
    /* City selector */
    .stSelectbox > div > div {
        border: 2px solid #e5e7eb !important;
        border-radius: 8px !important;
        padding: 10px 14px !important;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .service-grid {
            grid-template-columns: 1fr 1fr;
        }
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

# Get city data
city_data = df[df["City"] == selected_city].iloc[0]

# Key Metrics
st.markdown("### City Overview")
cols = st.columns(4)
cols[0].metric("Cluster", city_data["Cluster"])
cols[1].metric("CG Head", city_data["CG head"])
cols[2].metric("Available Services", f"{sum(1 for x in city_data[3:] if x == 'YES')}/{len(df.columns[3:])}")
cols[3].metric("Coverage", f"{sum(1 for x in city_data[3:] if x == 'YES')/len(df.columns[3:])*100:.0f}%")

# Serviceability Grid
st.markdown("### Service Channel Status")
with st.container():
    st.markdown('<div class="service-grid">', unsafe_allow_html=True)
    
    for service in df.columns[3:]:
        status = city_data[service]
        st.markdown(f"""
        <div class="service-card">
            <div style="font-weight: 600; color: #1f2937">{service}</div>
            <div class="service-status {'available' if status == 'YES' else 'unavailable'}">
                {'Available' if status == 'YES' else 'Not Available'}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption(f"Data current as of {pd.Timestamp.now().strftime('%d %B %Y')} | v2.2")
