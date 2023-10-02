from fastapi import FastAPI, HTTPException, Query
from typing import List, Dict, Optional
import csv

app = FastAPI()

# Load CSV file data
data = []
with open('seattle-weather.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)

# Get all data
#ex /api/data
@app.get("/api/data", response_model=List[Dict[str, str]])
async def get_data():
    return data

# Get row by id
#ex /api/data/1
@app.get("/api/data/{id}", response_model=Dict[str, str])
async def get_data_by_id(id: int):
    if id < len(data):
        return data[id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")

# Query by date and weather with limit
# ex: /api/query?weather=rain&limit=5
@app.get("/api/query", response_model=List[Dict[str, str]])
async def get_data(limit: Optional[int] = Query(None), date: Optional[str] = Query(None),
                   weather: Optional[str] = Query(None)):
    filtered_data = data
    if date:
        filtered_data = [row for row in filtered_data if row['date'] == date]
    if weather:
        filtered_data = [row for row in filtered_data if row['weather'] == weather]
    if limit:
        filtered_data = filtered_data[:limit]
    if len(filtered_data) == 0:
        raise HTTPException(status_code=404, detail="No result was found")
    return filtered_data
