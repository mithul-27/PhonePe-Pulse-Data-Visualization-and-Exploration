# PhonePe-Pulse-Data-Visualization-and-Exploration

## Problem Statement:
The Phonepe pulse Github repository contains a large amount of data related to various metrics and statistics. The goal is to extract this data and process it to obtain insights and information that can be visualized in a user-friendly manner.
The solution must include the following steps:
- Extract data from the Phonepe pulse Github repository through scripting and clone it..
- Transform the data into a suitable format and perform any necessary cleaning and pre-processing steps.
- Insert the transformed data into a SQL database for efficient storage and retrieval.
- Create a live geo visualization dashboard using Streamlit and Plotly in Python to display the data in an interactive and visually appealing manner.
- Fetch the data from the SQL database to display in the dashboard.
- Provide at least 10 different dropdown options for users to select different facts and figures to display on the dashboard.
The solution must be secure, efficient, and user-friendly. The dashboard must be easily accessible and provide valuable insights and information about the data in the Phonepe pulse Github repository.

## Approach:
- Data extraction: Clone the Github using scripting to fetch the data from the Phonepe pulse Github repository and store it in a suitable format such as CSV or JSON.
- Data transformation: Use a scripting language such as Python, along with libraries such as Pandas, to manipulate and pre-process the data. This may include cleaning the data, handling missing values, and transforming the data into a format suitable for analysis and visualization.
- Database insertion: Use the sql-connector-python library in Python to connect to a SQL database and insert the transformed data using SQL commands.
- Dashboard creation: Use the Streamlit and Plotly libraries in Python to create an interactive and visually appealing dashboard. Plotly's built-in geo map functions can be used to display the data on a map and Streamlit can be used to create a user-friendly interface with multiple dropdown options for users to select different facts and figures to display.
- Data retrieval: Use the sql-connector-python library to connect to the SQL database and fetch the data into a Pandas dataframe. Use the data in the dataframe to update the dashboard dynamically.
- Deployment: Ensure the solution is secure, efficient, and user-friendly. Test the solution thoroughly and deploy the dashboard publicly, making it accessible to users.
This approach leverages the power of Python and its numerous libraries to extract, transform, and analyze data, and to create a user-friendly dashboard for visualizing the insights obtained from the data.

## Results:
The result of this project will be a live geo visualization dashboard that displays information and insights from the Phonepe pulse Github repository in an interactive and visually appealing manner. The dashboard will have at least 10 different dropdown options for users to select different facts and figures to display. The data will be stored in a MySQL database for efficient retrieval and the dashboard will be dynamically updated to reflect the latest data. Users will be able to access the dashboard from a web browser and easily navigate the different visualizations and facts and figures displayed. The dashboard will provide valuable insights and information about the data in the Phonepe pulse Github repository, making it a valuable tool for data analysis and decision-making.

Overall, the result of this project will be a comprehensive and user-friendly solution for extracting, transforming, and visualizing data from the Phonepe pulse Github repository

![Screenshot (22)](https://github.com/user-attachments/assets/5428b211-7464-4202-8cbb-ceda03c7c0f3)

![Screenshot (23)](https://github.com/user-attachments/assets/39cd3479-5fc8-4119-a6ee-e6f50a4bd720)
