import os
import uvicorn
import json
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from typing import Optional, List
from rake_nltk import Rake

import mysql.connector

# Establoshing connection to the MYSQL server.
db = mysql.connector.connect(host="mysql", user="root", passwd="my_secret_pw", database="YouTube_API")
mycursor = db.cursor()

# Rake is used to optimze the search result by extracting key words using NLTK.
r = Rake()

app = FastAPI()

# API routes
@app.get("/get")
async def paginated(page_number: int = 1):

    cursor_lead = (page_number*10) - 10
    mycursor.execute('SELECT * FROM Shorts limit %s, %s', (cursor_lead, 10))
    data = list(mycursor.fetchall())
    return json.dumps(data, indent=4)

@app.get("/search")
async def search(search_query: str = "short video"):

    keywords = r.extract_keywords_from_text(search_query)
    ranked = r.get_ranked_phrases()

    result = []
    
    for i in ranked:
        search_term = ("%" + i + "%")
        partial_response = mycursor.execute("SELECT * FROM Shorts WHERE title LIKE \"%s\" OR description LIKE \"%s\"", (search_term, search_term))
        if partial_response == None:
            return "its nothing here"
        else:
            result = result + partial_response

    return json.dumps(result, indent=4)

# For local development. Not required if running uvicorn from cli.
if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')



