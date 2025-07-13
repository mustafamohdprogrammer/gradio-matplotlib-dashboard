import pandas as pd
import matplotlib.pyplot as plt
import gradio as gr
import numpy as np


default_df = pd.read_csv('sample_sales_data.csv')

def generate_plot(chart_type,theme,file):
    # load the dataset
    try:
        if file is not None:
            df = pd.read_csv(file.name)
        else:
            df = default_df.copy()
    except:
        return "❌ Error: Invalid CSV uploaded",None
    #check if required columns exist
    if not set(['Month', 'Sales', 'Profit']).issubset(df.columns):
        return "❌ Error: CSV must contain 'Month', 'Sales', and 'Profit' columns", None

    # Apply theme
    plt.style.use('classic' if theme == "Classic" else 'ggplot')
    fig, ax = plt.subplots(figsize=(10, 6))

      # Plot types
    if chart_type == "Line Plot":
        ax.plot(df['Month'], df['Sales'], marker='o', label='Sales', color='royalblue')
        ax.plot(df['Month'], df['Profit'], marker='s', label='Profit', color='seagreen')
        ax.set_title("Monthly Sales & Profit Trend")
        
        # Highlight best and worst
        best_month = df['Sales'].idxmax()
        worst_month = df['Sales'].idxmin()
        ax.scatter(df.loc[best_month, 'Month'], df.loc[best_month, 'Sales'], color='gold', s=150, label='Best Month')
        ax.scatter(df.loc[worst_month, 'Month'], df.loc[worst_month, 'Sales'], color='red', s=150, label='Worst Month')

    elif chart_type == "Bar Chart":
        ax.bar(df['Month'], df['Sales'], label='Sales', color='cornflowerblue')
        ax.bar(df['Month'], df['Profit'], label='Profit', color='lightgreen', alpha=0.7)
        ax.set_title("Sales vs Profit per Month")

    elif chart_type == "Pie Chart":
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(df['Sales'], labels=df['Month'], autopct='%1.1f%%', startangle=90, colors=plt.cm.Set3.colors)
        ax.set_title("Sales Share per Month")
        return "", fig

    elif chart_type == "Scatter Plot":
        ax.scatter(df['Sales'], df['Profit'], color='purple', s=100)
        ax.set_title("Sales vs Profit")

    elif chart_type == "Histogram":
        ax.hist(df['Profit'], bins=8, color='orange', edgecolor='black')
        ax.set_title("Profit Distribution")

    elif chart_type == "Box Plot":
        ax.boxplot(df['Profit'], patch_artist=True, boxprops=dict(facecolor='skyblue'))
        ax.set_title("Profit Spread")

    ax.set_xlabel("Month" if chart_type not in ["Scatter Plot", "Histogram", "Box Plot", "Pie Chart"] else "")
    ax.set_ylabel("Amount (₹)")
    if chart_type in ["Line Plot", "Bar Chart"]:
        ax.legend()
    ax.grid(True)
    return "", fig



# Gradio UI
with gr.Blocks() as dashboard:
    gr.Markdown("## 📊 Interactive Sales & Profit Dashboard")
    gr.Markdown("Upload your monthly data or use the sample dataset. Select the chart and see insights!")

    with gr.Row():
        chart_type = gr.Dropdown(choices=["Line Plot", "Bar Chart", "Pie Chart", "Scatter Plot", "Histogram", "Box Plot"],
                                 label="Chart Type", value="Line Plot")
        theme = gr.Radio(choices=["ggplot", "Classic"], value="ggplot", label="Theme")
        file = gr.File(label="Upload CSV", file_types=[".csv"])

    output_text = gr.Textbox(label="📌 Insights", interactive=False)
    plot_output = gr.Plot()

    chart_type.change(fn=generate_plot, inputs=[chart_type, theme, file], outputs=[output_text, plot_output])
    theme.change(fn=generate_plot, inputs=[chart_type, theme, file], outputs=[output_text, plot_output])
    file.change(fn=generate_plot, inputs=[chart_type, theme, file], outputs=[output_text, plot_output])

dashboard.launch()
