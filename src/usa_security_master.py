"""
This Script saves Security Master type data for US Equities using the financedatabase package
"""
import financedatabase as fd
import pandas as pd

# Directory to export CSV files to
DATA_DIR = r"/Users/talhajamal/Desktop/Code/Python Projects/Daily Market Update/data"

equities = fd.Equities()

# Pull list of countries 
COUNTRIES = pd.DataFrame(data=equities.options('country'),
                         columns=["Countries"])

# Pull US Sector Names
USA_SECTORS = pd.DataFrame(data=equities.options(selection='sector',
                                                 country='United States'),
                           columns=["Sectors"])

# Pull US Indistries Names
USA_INDUSTRIES = pd.DataFrame(data=equities.options(selection='industry',
                                                    country='United States'),
                              columns=["Industries"])

# Pull US Industry Groups

USA_INDUSTRY_GROUPS = pd.DataFrame(data=equities.options(selection='industry_group',
                                                         country='United States'),
                                   columns=["Industry Groups"])

# Pull all of USA securities in a single Data Frame
USA = pd.DataFrame(equities.select(country="United States")
                   ).reset_index()


# Push dataframes to CSV files
COUNTRIES.to_csv(DATA_DIR+"/countries.csv",
                 sep=',',
                 header=True,
                 index=False)
USA_SECTORS.to_csv(DATA_DIR+"/usa_sectors.csv",
                   sep=',',
                   header=True,
                   index=False)
USA_INDUSTRIES.to_csv(DATA_DIR+"/usa_industries.csv",
                      sep=',',
                      header=True,
                      index=False)
USA_INDUSTRY_GROUPS.to_csv(DATA_DIR+"/usa_industry_groups.csv",
                           sep=',',
                           header=True,
                           index=False)
USA.to_csv(DATA_DIR+"/USA.csv",
           sep=',',
           header=True,
           index=False)
