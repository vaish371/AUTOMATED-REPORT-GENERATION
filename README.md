# AUTOMATED-REPORT-GENERATION

*NAME*: BURRA VAISHNAVI

*INTERN ID*: CT04DM713 

*DOMAIN*: PYTHON PROGRAMMING 

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

*DESCRIPTION*: I have performed AUTOMATED-REPORT-GENERATION task.

     i have used tools those are:
     
           1. Core Programming Language:
           
                        Python: This is the primary programming language in which the entire report generation logic is written.
                        
           2. Key Python Libraries (Installed via pip):
           
                 pandas:
                 
                     Purpose: Essential for data manipulation and analysis.
                     
                           * It's used to: Read the sales_data.csv file (pd.read_csv).
                           
                           * Perform calculations like summing total sales (df['Sales'].sum()).
                           
                           * Group data (e.g., sales by region, sales by product) (df.groupby()).
                           
                           * Handle missing or non-numeric data (pd.to_numeric, dropna).
                           
                     How it was used: import pandas as pd
                     
              fpdf2 (or fpdf):
              
                    Purpose: A library specifically designed for creating PDF documents from Python. It allows you to:
                    
                         * Create new PDF pages.
                         
                         * Set fonts, colors, and text sizes.
                         
                         * Add text, images, and tables.
                         
                         * Control page breaks and positioning.
                         
                         * How it was used: from fpdf import FPDF
                         
              matplotlib.pyplot:
              
                    Purpose: A widely used plotting library for creating static, animated, and interactive visualizations in Python. It's used to:
                    
                         * Generate the bar chart for sales by region.
                         
                         * Save the plot as an image file (PNG).
                         
                         * How it was used: import matplotlib.pyplot as plt

        3. Development Environment/Applications:

               These are the platforms or programs where you wrote and ran the code:

             * Google Colaboratory (Colab):

                       Purpose: A free cloud-based Jupyter notebook environment provided by Google.
                       
                       It allows you to write and execute Python code directly in your browser, with access to free computing resources (including GPUs/TPUs if needed).
                       
                       How it was used: This is where you were primarily running your code, installing libraries, and uploading/downloading files.
                       
            * Command Prompt (Windows) / Terminal (macOS/Linux):

                      Purpose: A command-line interface (CLI) used to interact with your operating system.
                      
                      How it was used: In the initial troubleshooting, you were using py generate_report.py to run the script locally on your computer, and cd to navigate directories. 
                      
            * Text Editor (e.g., Notepad, Notepad++, VS Code):

                      Purpose: A basic program for writing and editing plain text files.
                      
                      How it was used: likely used a text editor to create and save the generate_report.py and sales_data.csv files on  local computer before uploading them to Colab or running them locally.
