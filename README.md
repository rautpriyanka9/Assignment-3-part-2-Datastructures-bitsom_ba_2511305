# 🍽️ Restaurant Menu & Order Management System

## 📌 Overview
This project implements a **Restaurant Order Management System** using Python's core data structures such as **lists, dictionaries, and nested structures**.

The system simulates real-world restaurant operations including:
- Menu display
- Cart management
- Inventory tracking
- Sales analysis

---

## 🧠 Concepts Used
- Dictionaries & Nested Dictionaries  
- Lists & List of Dictionaries  
- Loops (for, while)  
- Conditional Statements (if-else)  
- Functions  
- String Formatting  
- Deep Copy (copy.deepcopy)  

---

## 📂 File Structure

restaurant_management.py

---

## 🚀 Tasks Implemented

### 🔹 Task 1 — Explore the Menu
- Display menu grouped by category (Starters, Mains, Desserts)
- Show availability status of each item
- Compute:
  - Total number of items
  - Total available items
  - Most expensive item
  - Items priced below ₹150

---

### 🔹 Task 2 — Cart Operations
- Add items to cart with validation:
  - Check if item exists in menu
  - Check availability
- Update quantity if item already exists
- Remove items from cart
- Generate Order Summary:
  - Subtotal
  - GST (5%)
  - Total payable amount

---

### 🔹 Task 3 — Inventory Tracker
- Create deep copy of inventory using `copy.deepcopy()`
- Demonstrate independence of original and backup
- Deduct stock based on cart orders
- Prevent negative stock
- Generate reorder alerts for low-stock items

---

### 🔹 Task 4 — Sales Log Analysis
- Calculate total revenue per day
- Identify best-selling day
- Find most ordered item
- Update sales log with new data
- Print all orders using `enumerate()`

---

## ▶️ How to Run

```bash
python restaurant_management.py