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

# Streamlit UI
st.title("🚀 Serviceability Check")
st.write("Select a city to see its cluster, CG head, and serviceability.")

# Dropdown to select city
selected_city = st.selectbox("Select City", df["City"].unique())

# Filter data for selected city
result = df[df["City"] == selected_city].reset_index(drop=True)

# Display Cluster and CG Head
st.subheader("📍 Basic Info")
col1, col2 = st.columns(2)
col1.metric("Cluster", result["Cluster"][0])
col2.metric("CG Head", result["CG head"][0])

# Display Serviceability (YES/NO columns)
st.subheader("🛒 Serviceability")
service_cols = df.columns[3:]  # All columns after CG head

for col in service_cols:
    st.write(f"**{col}:** {result[col][0]}")