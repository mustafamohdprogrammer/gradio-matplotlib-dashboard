import pandas as pd
import matplotlib.pyplot as plt
import gradio as gr 

# Load the dataset
df = pd.read_csv('sample_sales_data.csv')

# plot function
def plot_chart(chart_type):
    fig, ax = plt.subplots(figsize = (10, 6))

    if chart_type == 'Line Plot':
        ax.plot(df['Month'], df['Sales'], marker= 'o',label='sales',color='royalblue')
        ax.plot(df['Month'], df['Profit'], marker= 'o',label='profit',color='orange')
        ax.set_title('Sales and Profit Over Time')
        ax.set_xlabel('Month')
        ax.set_ylabel('Amount')
        ax.legend()
    elif chart_type == 'Bar Chart':
        ax.bar(df['Month'], df['Sales'], color='cornflowerblue', label='Sales')
        ax.bar(df['Month'], df['Profit'], color='lightgreen', label='Profit', alpha=0.7)
        ax.set_title("Sales vs Profit per Month")
        ax.set_xlabel('Month')
        ax.set_ylabel('Amount')
        ax.legend()
    elif chart_type == 'Scatter Plot':
        ax.scatter(df['Sales'], df['Profit'], color='purple', alpha=0.6)
        ax.set_title('Sales vs Profit Scatter Plot')
        ax.set_xlabel('Sales')
        ax.set_ylabel('Profit')
    elif chart_type == 'Pie Chart':
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(df['Sales'], labels=df['Month'], autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
        ax.set_title("Sales Share per Month")
        return fig
    elif chart_type == 'Histogram':
        ax.hist(df['Profit'], bins=8, color='orange', edgecolor='black')
        ax.set_title("Profit Distribution")
    elif chart_type == "Box Plot":
        ax.boxplot(df['Profit'], patch_artist=True, boxprops=dict(facecolor='skyblue'))
        ax.set_title("Profit Spread")

    ax.set_xlabel("Month" if chart_type not in ["Scatter Plot", "Histogram", "Box Plot", "Pie Chart"] else "")
    ax.set_ylabel("Amount (₹)")
    ax.grid(True)
    ax.legend(loc='best') if chart_type in ["Line Plot", "Bar Chart"] else None

    return fig



# Gradio interface

demo = gr.Interface(
    fn = plot_chart,
    inputs = gr.Dropdown(
         ["Line Plot", "Bar Chart", "Pie Chart", "Scatter Plot", "Histogram", "Box Plot"],
        label="Choose Chart Type"
    ),
     outputs="plot",
    title="📈 Interactive Sales & Profit Dashboard",
    description="Select a chart type to visualize your monthly sales and profit trends"
)

demo.launch()