import streamlit as st
import pandas as pd
from streamlit_extras.metric_cards import style_metric_cards

# Configuration
st.set_page_config(
    page_title="Enterprise Serviceability Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load data
data = {
    "Cluster": ["Ahmedabad", "Bangalore", "Bangalore"],
    "City": ["Ahmedabad", "Bengaluru", "Mysore"],
    "CG head": ["Dhwajal", "Sri Harsh", "No CG Head"],
    "Kirana Store": ["YES", "YES", "YES"],
    "SUPERMARKET": ["YES", "YES", "YES"],
    "Large Wholesaler": ["YES", "YES", "YES"],
    "General Stores": ["YES", "YES", "YES"],
    "Big Condiments": ["NO", "NO", "NO"],
    "Restaurants": ["YES", "YES", "NO"],
    "Medical": ["YES", "NO", "NO"],
    "Bakery": ["YES", "NO", "NO"],
    "Milk Parlors": ["YES", "YES", "NO"],
    "Cosmetics": ["YES", "NO", "NO"],
    "PG": ["NO", "YES", "YES"],
}
df = pd.DataFrame(data)

# Custom CSS
st.markdown("""
<style>
    /* Base Styling */
    :root {
        --primary: #2563eb;
        --success: #16a34a;
        --danger: #dc2626;
        --card-bg: #ffffff;
    }
    
    /* Dashboard Header */
    .dashboard-header {
        border-bottom: 1px solid #e5e7eb;
        padding-bottom: 1rem;
        margin-bottom: 1.5rem;
    }
    
    /* Serviceability Matrix */
    .service-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
        gap: 12px;
        margin-top: 1.5rem;
    }
    
    .service-card {
        background: var(--card-bg);
        border-radius: 8px;
        padding: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        transition: all 0.2s;
    }
    
    .service-card:hover {
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transform: translateY(-2px);
    }
    
    .service-name {
        font-weight: 500;
        color: #374151;
        margin-bottom: 8px;
        font-size: 14px;
    }
    
    .status-indicator {
        display: flex;
        align-items: center;
        gap: 6px;
        font-weight: 600;
    }
    
    .available {
        color: var(--success);
    }
    
    .unavailable {
        color: var(--danger);
    }
    
    /* Selector Styling */
    .stSelectbox > div > div {
        border: 2px solid #e5e7eb !important;
        border-radius: 8px !important;
        padding: 8px 12px !important;
    }
    
    /* Metric Cards */
    [data-testid="metric-container"] {
        border: 1px solid #e5e7eb !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
with st.container():
    st.markdown("""
    <div class="dashboard-header">
        <h1 style='margin:0;color:#1e40af'>Enterprise Serviceability Matrix</h1>
        <p style='color:#6b7280;margin:0'>Real-time channel availability across retail networks</p>
    </div>
    """, unsafe_allow_html=True)

# City Selector
col1, col2 = st.columns([1, 3])
with col1:
    selected_city = st.selectbox(
        "SELECT LOCATION", 
        df["City"].unique(),
        key="city_select"
    )

# Filter data
result = df[df["City"] == selected_city].iloc[0]

# Key Metrics
with st.container():
    cols = st.columns(4)
    cols[0].metric("Total Channels", len(df.columns[3:]))
    cols[1].metric("Available", sum(1 for x in result[3:] if x == "YES"))
    cols[2].metric("Unavailable", sum(1 for x in result[3:] if x == "NO"))
    cols[3].metric("Coverage", f"{sum(1 for x in result[3:] if x == 'YES')/len(df.columns[3:])*100:.0f}%")
    style_metric_cards()

# Serviceability Grid
st.subheader("Channel Availability Matrix")
with st.container():
    st.markdown('<div class="service-grid">', unsafe_allow_html=True)
    
    for service in df.columns[3:]:
        status = result[service]
        st.markdown(f"""
        <div class="service-card">
            <div class="service-name">{service.replace('/', ' / ')}</div>
            <div class="status-indicator">
                <span class="{'available' if status == 'YES' else 'unavailable'}">
                    {'●' if status == 'YES' else '○'}
                </span>
                <span>{'Available' if status == 'YES' else 'Unavailable'}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption(f"Data refreshed: {pd.Timestamp.now().strftime('%d %b %Y %H:%M')} | v2.1.0")
