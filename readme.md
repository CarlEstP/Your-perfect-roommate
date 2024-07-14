# APP Web development of 'Your perfect Roommate'

A practical case that combines data science, data analysis, and the real estate sector. The goal is to demonstrate how to use data science to solve complex problems in a real business context.

The case will analyze and determine which roommate is ideal among 100 possible candidates based on the responses to a total of 17 questions for sharing an apartment with multiple rooms, where at least some of them are already occupied.

We will see how to transform a real-world challenge into a practical solution using data science tools such as Python, Pandas, Streamlit, and Numpy. Additionally, Streamlit is used to create an interactive application after processing the dataset and extracting the solution based on user inputs.

## Tecnologías utilizadas

- Python
- Pandas
- Numpy
- Scikit-learn
- Matplotlib
- Seaborn
- Plotly
- Streamlit

## Case of use example

![header_photo](https://github.com/CarlEstP/app_inquilino_ideal/blob/main/src/exa.PNG)

- _Practical case adapted from the proposal of the DS4B channel_

## Description of the App Logic

1. Start the app from app.py, generating the frontend with the help of Streamlit.

2. Access the functions.py file to reformat the tenant identifiers entered in the form.

3. Execute the function to search for compatible roomates (Refer to the Jupyter notebook logica.ipynb for more details):

- Use the OneHotEncoder library and calculate the similarity matrix using dot product.
- Define the target range, find the minimum and maximum values, and rescale the matrix.
- Create a new dataframe with Pandas.
- Search for compatible tenants considering how many tenants already reside and how many need to be added to the property.
- The function will return a list of compatible tenants and their similarity data.

4. If there is a valid result, display the compatibility table and graph.
