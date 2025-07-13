
# 📊 SmartSales Dashboard

**Tagline:** *Visualize, Analyze, and Discover Business Insights in Seconds!*

## 📝 Description

SmartSales Dashboard is a Python-based interactive visualization tool built using **Gradio** and **Matplotlib**. This project helps users analyze monthly sales and profit data through a beautiful and intuitive dashboard. Whether you want to load a sample dataset or upload your own CSV file, this tool provides dynamic insights via Line Charts, Bar Charts, and Pie Charts.

---

## 📁 Project Structure

```
SmartSalesDashboard/
│
├── preloaded_data_dashboard.py       # Dashboard using a built-in dataset
├── user_chart_dashboard.py           # User-upload dashboard with file upload & insights
├── sales_analysis.ipynb              # Jupyter analysis notebook
├── sample_sales_data.csv             # Sample sales dataset
├── requirements.txt                  # Required dependencies
├── README.md                         # Project documentation (this file)
├── outputs/
│   ├── Dashboard_view_1.jpg
│   ├── Dashboard_view_2.jpg
│   ├── Dashboard_view_3.jpg
│   ├── Dashboard_view_4.jpg
│   └── Dashboard_view_5.jpg
```

---

## 🚀 Features

- Upload your own CSV file or use built-in data
- Choose from different chart types (Line, Bar, Pie)
- Toggle between visual themes (`ggplot`, `classic`)
- View auto-generated sales insights
- Exportable dashboard views

---

## 📦 Installation

Make sure Python 3.8+ is installed, then run:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

**To run the preloaded dashboard:**
```bash
python preloaded_data_dashboard.py
```

**To use the interactive upload dashboard:**
```bash
python user_chart_dashboard.py
```

The interface will open in your browser using Gradio.

---

## 🖼️ Sample Output

Below are the sample visualizations produced by the dashboard:

![Dashboard View 1](outputs/Dashboard_view_1.jpg)
![Dashboard View 2](outputs/Dashboard_view_2.jpg)
![Dashboard View 3](outputs/Dashboard_view_3.jpg)
![Dashboard View 4](outputs/Dashboard_view_4.jpg)
![Dashboard View 5](outputs/Dashboard_view_5.jpg)

---

## 📌 Requirements

The project dependencies are listed in `requirements.txt`, including:

- gradio
- matplotlib
- pandas

---

## 📬 Feedback

If you find this useful or have suggestions, feel free to reach out!
