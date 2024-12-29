# software_development_project
Steps Involved
Step 1: Project Prerequisites

Created a GitHub account and initialized a new repository with README.md and .gitignore files.
Installed necessary packages including pandas, streamlit, and plotly-express.
Created a Render.com account and linked it to GitHub.
Installed and configured VS Code, setting the Python interpreter to match the virtual environment.

Step 2: Data Acquisition

Downloaded the car advertisement dataset (vehicles_us.csv) and placed it in the root directory of the project.
I also did some data clean up and pre-processing to separate and evaluate data types into the new cleaned_vehicles_us.csv dataset

Step 3: Exploratory Data Analysis

Created an EDA.ipynb Jupyter notebook to conduct exploratory data analysis.
Created histograms and scatterplots using the plotly-express library.
The visualizations were first prototyped in Jupyter notebook and then integrated into the web application.

Step 4: Web Application Development

Created an app.py file in the root directory of the project.
Imported necessary modules like streamlit, pandas, and plotly_express.
Loaded the CSV data into a pandas DataFrame.
Incorporated various streamlit components into the app like headers, histograms, scatter plots, and checkboxes.
Updated README file to include a basic project description and instructions for other users to run the project on their local machine.

Step 5: Deployment to Render 

Added a streamlit configuration file to the GitHub repository.
Created a new web service linked to the GitHub repository in Render.
Configured the Render web service to install necessary packages and run the app.py file.
Deployed the final version of the application on Render.
Verified the application's accessibility at: https://software-development-project-magu.onrender.com

Conclusion

This project successfully demonstrated the end-to-end development of a data-driven web application for analyzing car advertisements. 
Through systematic implementation of key software development phases - from initial setup and data preprocessing to deployment - we created a functional, publicly accessible analytics platform.
The project effectively combined several modern technologies and practices:

Data analysis tools (pandas, plotly-express) for processing and visualizing vehicle data
Streamlit framework for creating an interactive web interface
Version control through GitHub for code management
Cloud deployment via Render.com for public accessibility

The resulting application (accessible at https://software-development-project-magu.onrender.com) provides users with interactive visualizations and insights into the car advertisement market. The use of Jupyter notebooks for initial exploration, followed by integration into a web application, showcases a practical approach to data-driven software development.
This project lays a foundation for future enhancements, such as implementing additional analytics features, optimizing performance, or expanding the dataset. The modular structure and use of industry-standard tools ensure the application can be readily maintained and scaled as needed.