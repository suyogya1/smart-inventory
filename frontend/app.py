import streamlit as st
import requests
import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from llm import get_reorder_suggestions

API_URL = "http://localhost:8000"

# Page settings
st.set_page_config(page_title="SmartInventory Dashboard", layout="centered")
st.title("📦 SmartInventory Dashboard")


st.subheader("📋 Current Inventory")
try:
    response = requests.get(f"{API_URL}/inventory")
    if response.ok:
        inventory = response.json()["inventory"]
        if inventory:
            for name, info in inventory.items():
                quantity = info['quantity']
                if quantity < 10:
                    st.warning(f"⚠️ **{name.capitalize()}** — Low Stock: `{quantity}`")
                else:
                    st.write(f"✅ **{name.capitalize()}** — Quantity: `{quantity}`")
        else:
            st.info("Inventory is currently empty.")
    else:
        st.error("❌ Failed to load inventory.")
except Exception as e:
    st.error(f"Error connecting to backend: {e}")

st.markdown("---")


st.subheader("➕ Add New Item")
with st.form("add_item_form"):
    name = st.text_input("Item Name")
    quantity = st.number_input("Quantity", min_value=0, step=1)
    submitted = st.form_submit_button("Add Item")
    if submitted:
        res = requests.post(f"{API_URL}/inventory", json={"name": name, "quantity": quantity})
        if res.ok:
            st.success(f"✅ Item '{name}' added successfully!")
        else:
            st.error(f"❌ {res.json().get('detail', 'Error adding item.')}")

st.markdown("---")


st.subheader("✏️ Update Existing Item")
with st.form("update_item_form"):
    update_name = st.text_input("Item Name to Update")
    new_quantity = st.number_input("New Quantity", min_value=0, step=1, key="update_quantity")
    update_btn = st.form_submit_button("Update Quantity")
    if update_btn:
        res = requests.put(f"{API_URL}/inventory/{update_name}", params={"quantity": new_quantity})
        if res.ok:
            st.success(f"✅ Quantity for '{update_name}' updated.")
        else:
            st.error(f"❌ {res.json().get('detail', 'Error updating quantity.')}")

st.markdown("---")

st.subheader("🤖 AI Reorder Suggestions")

if st.button("What should I reorder?"):
    try:
        response = requests.get(f"{API_URL}/inventory")
        if response.ok:
            inventory_data = response.json()["inventory"]
            suggestion = get_reorder_suggestions(inventory_data)
            st.success("Here's what the AI recommends:")
            st.write(suggestion)
        else:
            st.error("Failed to fetch inventory.")
    except Exception as e:
        st.error(f"AI request failed: {e}")
