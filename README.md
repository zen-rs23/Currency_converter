# FX Converter

## Project Description:
The FX Converter web app enables users to obtain the latest and historical currency conversion rates. By utilizing data from the Frankfurt API, users can easily select two different currencies and receive up-to-date exchange rates, as well as the ability to select a historical date to view past rates. The application offers a user-friendly interface built with Streamlit.

## Python Files & Functions:

1. api.py - python script that will contain the code for making API calls.
2. frankfurter.py - Python script that will contain the functions used for calling relevant Frankfurter endpoints and extracting information.
3. currency.py - Python script that will contain the function used for formatting the results to be displayed in the Streamlit app.
4. app.py - Main Streamlit python script used for managing users’ inputs and displaying results

**api.py:**
This module is responsible for making direct HTTP calls to external web services. The primary goal of having a separate module for API-related actions is to modularize the application, isolating direct interactions with web endpoints and ensuring better maintainability.

1. get(url): This function is a utility function designed to make HTTP GET requests to any provided URL, specifically tailored to fetch data from web APIs.

**frankfurter.py:**
The frankfurter.py script acts as an intermediary layer between the main app and the Frankfurt API, a popular tool for fetching current and historical currency exchange rates. The script helps in abstracting the API endpoints and provides a streamlined interface to fetch necessary data without getting into the intricacies of the API details. 

1. get_available_currencies(): This function provides a list of all the available currency codes that the Frankfurt API supports.
2. get_latest_rate(from_currency, to_currency): Given a source currency (e.g., 'USD') and a target currency (e.g., 'EUR'), this function fetches the most recent conversion rate between them.
3. get_historical_rate(from_currency, to_currency, date): This function is similar to get_latest_rate, but instead of fetching the most recent rate, it fetches the conversion rate for a specified past date.

**currency.py:**
This file is responsible for providing formatted strings that represent the conversion results, ready to be displayed in the Streamlit web app. It handles the mathematical computation of the conversion and the inverse rate, and then neatly packages that information into a human-readable format.

1. format_conversion(date, from_currency, to_currency, rate, amount): The function first calculates the converted_amount by multiplying the amount with the rate. The inverse_rate is computed by taking the reciprocal of the rate. Using these calculated values and the provided parameters, the function creates a formatted string that describes the conversion process in detail.

**app.py:**
The app.py file serves as the primary interface for the FX Converter web application. It utilizes Streamlit, a Python library, to create an interactive web-based interface for currency conversion. It manages user input, displays currency selection options, provides fields for the amount to be converted, shows the latest/historical conversion rate, and the formatted conversion result.

1. st.title("FX Converter"): This sets the main title of the web application to "FX Converter".
2. st.number_input(...): This component creates an input field where users can specify the amount they want to convert.
3. The app fetches available currencies using the frankfurter.get_available_currencies() function.
4. st.selectbox(...): Two dropdown selection boxes are created using this component, one for the source currency and the other for the target currency. 
5. st.button("Get Latest Rate"): This button, when clicked, triggers the fetching of the latest conversion rate between the selected currencies.
6. st.date_input("Select date"): This component allows users to pick a historical date for which they want to check the conversion rate.
7. st.button("Get Historical Rate"): When clicked, this button fetches the historical conversion rate for the selected date.

The app.py essentially integrates functionalities provided in other script files (frankfurter.py and currency.py), uses them based on user input, and then presents the results in an interactive web interface using Streamlit.

## Instructions to Run the Web App:

### Prerequisites:
Ensure that you have the following installed:

1. Python: The web app is written in Python, and you will need it to execute the script. If you haven't installed Python, you can download and install Visual Studio Code and install Python Extension for Visual Studio Code.
2. pip: It is the package installer for Python. It usually comes with the Python installation.

**Installing Required Libraries:**
Install the necessary Python libraries using pip. These libraries include streamlit for web app rendering and requests for API calls. The command `pip install streamlit requests` is a shell (or command prompt) command and should be executed directly in your terminal or command prompt.

**Running the Web App:**
With the necessary libraries installed and while being in the project directory, run the Streamlit app using the command `streamlit run app.py`.

**Accessing the Web App:**
Once the command is executed, Streamlit will provide an output that indicates the server is running. It will display a local URL (typically http://localhost:8501/). 
This URL opens automatically without performing any extra steps.

**Using the Web App:**
1. Input the amount you wish to convert.
2. Choose the source and target currencies from the dropdown lists.
3. Click on the "Get Latest Rate" button to fetch the latest conversion rate.
4. Alternatively, select a date and click on the "Get Historical Rate" button to fetch the historical conversion rate for that date.

**Exiting the Web App:**
To stop the Streamlit server and exit the app, simply go back to the terminal and press CTRL + C.

*The above instructions provide a comprehensive guide on how to set up, run, use, and close the FX Converter web app.*
