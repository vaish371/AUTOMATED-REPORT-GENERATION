import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt
import os # To handle file paths

# --- Configuration ---
DATA_FILE = 'sales_data (1).csv' # Add the (1)
REPORT_OUTPUT_FILE = 'sales_report.pdf'
PLOT_OUTPUT_FILE = 'sales_by_region_plot.png'
REPORT_TITLE = "Quarterly Sales Performance Report"
AUTHOR = "Automated Report System"

# --- 1. Data Reading ---
def read_data(filepath):
    """Reads data from a CSV file."""
    try:
        df = pd.read_csv(filepath)
        print(f"Successfully read data from {filepath}")
        return df
    except FileNotFoundError:
        print(f"Error: Data file '{filepath}' not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: Data file '{filepath}' is empty.")
        return None
    except Exception as e:
        print(f"An error occurred while reading data: {e}")
        return None

# --- 2. Data Analysis ---
def analyze_data(df):
    """Performs basic sales analysis."""
    if df is None or df.empty:
        print("No data to analyze.")
        return None, None, None

    # Ensure 'Sales' column is numeric
    df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
    df.dropna(subset=['Sales'], inplace=True) # Drop rows where Sales couldn't be converted

    total_sales = df['Sales'].sum()
    sales_by_region = df.groupby('Region')['Sales'].sum().reset_index()
    sales_by_product = df.groupby('Product')['Sales'].sum().reset_index()

    print("Data analysis complete.")
    return total_sales, sales_by_region, sales_by_product

# --- 3. Data Visualization ---
def create_sales_plot(sales_by_region_df, output_path):
    """Creates a bar plot of sales by region and saves it as an image."""
    if sales_by_region_df is None or sales_by_region_df.empty:
        print("No data to plot.")
        return False

    plt.figure(figsize=(8, 5))
    plt.bar(sales_by_region_df['Region'], sales_by_region_df['Sales'], color='skyblue')
    plt.xlabel('Region')
    plt.ylabel('Total Sales')
    plt.title('Total Sales by Region')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout() # Adjust layout to prevent labels from overlapping

    try:
        plt.savefig(output_path)
        return True
    except Exception as e:
        print(f"Error saving plot: {e}")
        return False
    finally:
        plt.close() # Close the plot to free up memory

# --- 4. Report Generation (using fpdf2) ---
def generate_pdf_report(total_sales, sales_by_region_df, sales_by_product_df, plot_image_path, output_filepath):
    """Generates a formatted PDF report."""
    if total_sales is None:
        print("Cannot generate report due to missing analysis data.")
        return

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title
    pdf.set_font("Arial", "B", 24)
    pdf.cell(0, 10, REPORT_TITLE, 0, 1, "C")
    pdf.ln(10) # Line break

    # Author and Date
    pdf.set_font("Arial", "", 10)
    pdf.cell(0, 5, f"Prepared by: {AUTHOR}", 0, 1, "C")
    pdf.cell(0, 5, f"Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}", 0, 1, "C")
    pdf.ln(15)

    # Executive Summary
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Executive Summary", 0, 1, "L")
    pdf.set_font("Arial", "", 12)
    summary_text = (
        f"This report provides an overview of sales performance. "
        f"The total sales across all regions and products is ${total_sales:,.2f}. "
        "Detailed breakdowns by region and product are provided below, along with a visual representation of regional sales."
    )
    pdf.multi_cell(0, 7, summary_text)
    pdf.ln(10)

    # Sales by Region Plot
    if os.path.exists(plot_image_path):
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, "Sales by Region", 0, 1, "L")
        pdf.image(plot_image_path, x=pdf.get_x() + 10, w=150) # Adjust x and w for placement
        pdf.ln(10)
    else:
        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 10, "Sales by Region plot could not be generated.", 0, 1, "L")
        pdf.ln(5)


    # Sales by Region Table
    if sales_by_region_df is not None and not sales_by_region_df.empty:
        pdf.add_page() # New page for tables
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, "Detailed Sales by Region", 0, 1, "L")
        pdf.ln(5)

        pdf.set_font("Arial", "B", 10)
        # Table Headers
        col_width = pdf.w / 3.5 # Adjusted column width
        pdf.cell(col_width, 8, "Region", 1, 0, "C")
        pdf.cell(col_width, 8, "Total Sales ($)", 1, 1, "C")

        pdf.set_font("Arial", "", 10)
        for index, row in sales_by_region_df.iterrows():
            pdf.cell(col_width, 8, str(row['Region']), 1, 0, "L")
            pdf.cell(col_width, 8, f"{row['Sales']:,.2f}", 1, 1, "R")
        pdf.ln(10)

    # Sales by Product Table
    if sales_by_product_df is not None and not sales_by_product_df.empty:
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, "Detailed Sales by Product", 0, 1, "L")
        pdf.ln(5)

        pdf.set_font("Arial", "B", 10)
        # Table Headers
        col_width = pdf.w / 3.5
        pdf.cell(col_width, 8, "Product", 1, 0, "C")
        pdf.cell(col_width, 8, "Total Sales ($)", 1, 1, "C")

        pdf.set_font("Arial", "", 10)
        for index, row in sales_by_product_df.iterrows():
            pdf.cell(col_width, 8, str(row['Product']), 1, 0, "L")
            pdf.cell(col_width, 8, f"{row['Sales']:,.2f}", 1, 1, "R")
        pdf.ln(10)

    # Footer
    pdf.set_y(-15) # Position at 1.5 cm from bottom
    pdf.set_font("Arial", "I", 8)
    pdf.cell(0, 10, f"Page {pdf.page_no()}/{{nb}}", 0, 0, "C")

    pdf.output(output_filepath)
    print(f"Report generated successfully: {output_filepath}")

    # Clean up generated plot image
    if os.path.exists(plot_image_path):
        os.remove(plot_image_path)


# --- Main Execution Flow ---
if __name__ == "__main__":
    df = read_data(DATA_FILE)
    if df is not None:
        total_sales, sales_by_region, sales_by_product = analyze_data(df.copy()) # Use .copy() to avoid SettingWithCopyWarning
        plot_generated = create_sales_plot(sales_by_region, PLOT_OUTPUT_FILE)

        generate_pdf_report(total_sales, sales_by_region, sales_by_product, PLOT_OUTPUT_FILE, REPORT_OUTPUT_FILE)
    else:
        print("Report generation aborted due to data reading errors.")
