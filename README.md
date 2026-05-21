# Analysis of Data with 10,000+ Rows

This project showcases dashboards created using Power BI, Python, and Excel. The dashboards include KPIs, and interactive filters (e.g. 'year'). The [Python script](/visualization/main.py) uses Pandas for extracting and cleaning CSV data, plotly.express for visualizations and charts, and Streamlit for configuring and launching a web page. In the Excel file, Pivot Tables are used to create filtered datasets for charts as well as inserting Slicers. Data is also cleaned and formatted in the Excel file using functions such as **COUNTA**, **AVERAGE**, and **SUM**.

The visualization files are as follows:

- Excel: [Movies Dashboard.xlsx](/visualization/Movies%20Dashboard.xlsx)
- Python: [main.py](/visualization/main.py)
- Power BI: [Synthetic Flight Passenger Dashboard.pbix](/visualization/Synthetic%20Flight%20Passenger%20Data%20Dashboard.pbix)

## Data Sources

The free, public CSV data sources were acquired from Kaggle. They can be found in their respective folders: [Movies dataset](/datasets/Movies_dataset.csv), and [Flight passenger data](/datasets/synthetic_flight_passenger_data.csv).

- **Synthetic Airline Passenger and Flight Data**: This synthetic dataset simulates 10,000 individual airline passengers and their associated flight details. It was designed for data analytics projects, including regression, classification, clustering, and time series forecasting. Each row represents a passenger's booking and flight experience, including demographic details, travel purpose, booking behavior, flight status, satisfaction score, and more [[source](https://www.kaggle.com/datasets/keatonballard/synthetic-airline-passenger-and-flight-data/data)].
- **Latest 10000 Movies Dataset from TMDB**: This movies dataset can be used for a variety of purposes, depending on the goals and the insights that need to be derived from the data. Examples include movie analysis, recommendation systems, and popularity measurement. [[source](https://www.kaggle.com/datasets/nagrajdesai/latest-10000-movies-dataset-from-tmdb)].

## Python Usage

The commands below should be run in the terminal from the project root.

1. Install the required dependencies: `pip install streamlit pandas plotly`.
2. Run the dashboard: `streamlit run visualization/main.py`.
3. This should open in the browser at **http://localhost:8501**.