# Import pandas package
import pandas as pd

# Import Data
data = pd.read_csv("country_vaccinations.csv")

# Activate column names
pd.set_option('display.max_columns', None)

# Three first line
Three_first_line = data.head(3)

# Select daily vaccination per million for the selected country (single condition)
daily_vaccination_per_million_country = data[data.country == 'France'].daily_vaccinations_per_million

# Select daily vaccination per million for the selected country and Data (Multiple condition)
daily_vaccination_per_million_country_date = data[(data.country == 'France') & (data.date == '2020-12-31')].\
    daily_vaccinations_per_million

# Filtering for data related to france and Germany
Germany_France_Data = data[data.country.isin(['France', 'Germany'])]

# Filtering for data not related to france and Germany
Not_Germany_France_Data = data[~data.country.isin(['France', 'Germany'])]


