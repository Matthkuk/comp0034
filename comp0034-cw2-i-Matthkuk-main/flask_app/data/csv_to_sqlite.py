from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine, types

# Define the database file name and location
db_1415 = Path(__file__).parent.joinpath("1415.db")
db_1516 = Path(__file__).parent.joinpath("1516.db")
db_1617 = Path(__file__).parent.joinpath("1617.db")
db_1718 = Path(__file__).parent.joinpath("1718.db")
db_1819 = Path(__file__).parent.joinpath("1819.db")

# Create a connection to file as a SQLite database (this automatically creates the file if it doesn't exist)
engine1415 = create_engine("sqlite:///" + str(db_1415), echo=False)
engine1516 = create_engine("sqlite:///" + str(db_1516), echo=False)
engine1617 = create_engine("sqlite:///" + str(db_1617), echo=False)
engine1718 = create_engine("sqlite:///" + str(db_1718), echo=False)
engine1819 = create_engine("sqlite:///" + str(db_1819), echo=False)
fb_engine = [engine1415, engine1516, engine1617, engine1718, engine1819]

# Read the football data to a pandas dataframe
fb_1415 = Path(__file__).parent.joinpath("fb_cleaned1415.csv")
fb_1516 = Path(__file__).parent.joinpath("fb_cleaned1516.csv")
fb_1617 = Path(__file__).parent.joinpath("fb_cleaned1617.csv")
fb_1718 = Path(__file__).parent.joinpath("fb_cleaned1718.csv")
fb_1819 = Path(__file__).parent.joinpath("fb_cleaned1819.csv")
fb_csv = [fb_1415, fb_1516, fb_1617, fb_1718, fb_1819]

football = []
for i in range(5):
    read_file = pd.read_csv(fb_csv[i])
    football.append(read_file)
    football[i]['id'] = range(1, len(football[i]) + 1)

# Write the data to tables in a sqlite database
dtype_fb = {
    "HomeTeam": types.TEXT(),
    "AwayTeam": types.TEXT(),
    "FTHG": types.INTEGER(),
    "FTAG": types.INTEGER(),
    "FTR": types.TEXT(),
    "HS": types.INTEGER(),
    "AS": types.INTEGER(),
    "HST": types.INTEGER(),
    "AST": types.INTEGER(),
}

for i in range(5):
    football[i].to_sql(
        "Matches", fb_engine[i], if_exists="append", index=False, dtype=dtype_fb
    )
