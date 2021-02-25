import pandas as pd
import requests as r

df = pd.read_csv('Dell Data Velocity.csv')

df = pd.DataFrame(df)
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

longitudes = []
latitudes = []

rows_collected = 0

for index, row in df.iterrows():
  city = row["CITY_SHIPPING"].replace(" ", "+")
  state = row["STATE_SHIPPING"].replace(" ", "+")
  zip_code = row["ZIP_SHIPPING"].replace(" ", "+")
  request_string = f"https://nominatim.openstreetmap.org/search?city={city}&state={state}&postalcode={zip_code}&format=json"
  data = r.get(request_string)

  if data.status_code == 200:
    # print(data.json())
    rows_collected += 1
  else:
    break

  if len(data.json()) <= 0:
    longitudes.append(0)
    latitudes.append(0)
  else:
    data = data.json()[0]
    longitudes.append(data["lon"])
    latitudes.append(data["lat"])
  
  print(f"{rows_collected} rows collected out of {df.shape[0]}", end="\r", flush=True)

    
print(rows_collected)

df["LAT"] = latitudes
df["LON"] = longitudes

with open(data_path, 'w') as f:
  df.to_csv(f)