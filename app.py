import streamlit as st
import pandas as pd
import json
import time
import os

st.set_page_config(page_title="Real-Time Data Pipeline Dashboard", layout="wide")
st.title("📊 Live Transaction Streaming Analytics Dashboard")
st.markdown("This dashboard updates in real-time by reading data processed through an Apache Kafka streaming pipeline.")

DATA_FILE = "live_metrics.json"

# Set up visual containers
metric_row = st.columns(3)
chart_row = st.columns(2)

# Infinite loop simulating a real-time UI websocket interface
while True:
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            
        if data:
            df = pd.DataFrame(data)
            
            # 1. Compute Metrics
            total_revenue = df['amount_usd'].sum()
            total_count = len(df)
            avg_ticket = df['amount_usd'].mean()
            
            with metric_row[0]:
                st.metric(label="Total Processed Volume", value=f"${total_revenue:,.2f}")
            with metric_row[1]:
                st.metric(label="Successful Transcaton Count", value=f"{total_count} events")
            with metric_row[2]:
                st.metric(label="Average Basket Size", value=f"${avg_ticket:.2f}")
                
            # 2. Render Charts
            with chart_row[0]:
                st.subheader("Revenue Contribution by Payment Type")
                revenue_by_type = df.groupby('type')['amount_usd'].sum()
                st.bar_chart(revenue_by_type)
                
            with chart_row[1]:
                st.subheader("Latest Live Event Registry")
                st.dataframe(df[['time', 'user', 'amount_usd', 'type']].tail(10), use_container_width=True)

    time.sleep(1) # Refresh rate limit
    st.rerun() # Tell Streamlit to re-execute the block to pull new metrics