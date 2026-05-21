import pandas as pd
import plotly.express as px
import streamlit as st

# Page Configuration:
st.set_page_config(
    page_title="Flight Passenger Dashboard",
    layout="wide"
)

st.title("✈️ Flight Passenger Analytics Dashboard")

# Load Data:
df = pd.read_csv("./datasets/synthetic_flight_passenger_data.csv")

# Convert datetime column:
df["Departure_Time"] = pd.to_datetime(df["Departure_Time"])

# Extract year/month/day
df["Year"] = df["Departure_Time"].dt.year
df["Month"] = df["Departure_Time"].dt.month_name()

# Sidebar Filters
st.sidebar.header("Filters")

# Year filter
selected_year = st.sidebar.multiselect(
    "Select Year",
    options=sorted(df["Year"].unique()),
    default=sorted(df["Year"].unique())
)

# Airline filter
selected_airline = st.sidebar.multiselect(
    "Select Airline",
    options=sorted(df["Airline"].unique()),
    default=sorted(df["Airline"].unique())
)

# Seat class filter
selected_seat = st.sidebar.multiselect(
    "Select Seat Class",
    options=sorted(df["Seat_Class"].unique()),
    default=sorted(df["Seat_Class"].unique())
)

# Flight status filter
selected_status = st.sidebar.multiselect(
    "Select Flight Status",
    options=sorted(df["Flight_Status"].unique()),
    default=sorted(df["Flight_Status"].unique())
)

# Filter Dataframe
filtered_df = df[
    (df["Year"].isin(selected_year)) &
    (df["Airline"].isin(selected_airline)) &
    (df["Seat_Class"].isin(selected_seat)) &
    (df["Flight_Status"].isin(selected_status))
]

# KPI Section
total_passengers = filtered_df["Passenger_ID"].nunique()
total_revenue = filtered_df["Price_USD"].sum()
avg_satisfaction = filtered_df["Flight_Satisfaction_Score"].mean()
avg_delay = filtered_df["Delay_Minutes"].mean()
delayed_flights = (
    filtered_df["Flight_Status"]
    .eq("Delayed")
    .sum()
)

kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

kpi1.metric(
    label="Total Passengers",
    value=f"{total_passengers:,}"
)

kpi2.metric(
    label="Revenue (USD)",
    value=f"{total_revenue:,.2f}"
)

kpi3.metric(
    label="Avg Satisfaction",
    value=f"{avg_satisfaction:.2f}"
)

kpi4.metric(
    label="Avg Delay (Min)",
    value=f"{avg_delay:.2f}"
)

kpi5.metric(
    label="Delayed Flights",
    value=f"{delayed_flights:,}"
)

st.markdown("---")

# ------------------
# CHARTS
# ------------------

# Flights by Airline
airline_chart = (
    filtered_df["Airline"]
    .value_counts()
    .reset_index()
)

airline_chart.columns = ["Airline", "Flights"]

fig_airline = px.bar(
    airline_chart,
    x="Airline",
    y="Flights",
    title="Flights by Airline"
)

# Revenue by Airline
revenue_chart = (
    filtered_df
    .groupby("Airline")["Price_USD"]
    .sum()
    .reset_index()
)

fig_revenue = px.bar(
    revenue_chart,
    x="Airline",
    y="Price_USD",
    title="Revenue by Airline"
)

# Flight Status Distribution
status_chart = (
    filtered_df["Flight_Status"]
    .value_counts()
    .reset_index()
)

status_chart.columns = ["Flight_Status", "Count"]

fig_status = px.pie(
    status_chart,
    names="Flight_Status",
    values="Count",
    title="Flight Status Distribution"
)

# Satisfaction by Seat Class
seat_chart = (
    filtered_df
    .groupby("Seat_Class")["Flight_Satisfaction_Score"]
    .mean()
    .reset_index()
)

fig_seat = px.bar(
    seat_chart,
    x="Seat_Class",
    y="Flight_Satisfaction_Score",
    title="Average Satisfaction by Seat Class"
)

# Monthly Flights Trend
monthly_chart = (
    filtered_df
    .groupby("Month")
    .size()
    .reset_index(name="Flights")
)

month_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

monthly_chart["Month"] = pd.Categorical(
    monthly_chart["Month"],
    categories=month_order,
    ordered=True
)

monthly_chart = monthly_chart.sort_values("Month")

fig_month = px.line(
    monthly_chart,
    x="Month",
    y="Flights",
    markers=True,
    title="Monthly Flights Trend"
)

# Display Charts
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig_airline, width='stretch')
    st.plotly_chart(fig_status, width='stretch')

with col2:
    st.plotly_chart(fig_revenue, width='stretch')
    st.plotly_chart(fig_seat, width='stretch')

st.plotly_chart(fig_month, width='stretch')

# Data Table
st.subheader("Filtered Dataset")

st.dataframe(filtered_df)

# Download Button
csv = filtered_df.to_csv(index=False)

st.download_button(
    label="Download Filtered Data",
    data=csv,
    file_name="filtered_flight_data.csv",
    mime="text/csv"
)
    


