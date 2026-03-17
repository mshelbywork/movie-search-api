from fastapi import FastAPI
from app.schemas import InputSchema, OutputSchema

data_set = {
  "Blade Runner 2049": {
    "genre": ["Sci-Fi", "Drama"],
    "type": "movie",
    "director": "Denis Villeneuve",
    "lead_actors": ["Ryan Gosling", "Harrison Ford"],
    "release_year": "2017-10-06",
    "rating": 8.0
  },
  "The Dark Knight": {
    "genre": ["Action", "Crime", "Drama"],
    "type": "movie",
    "director": "Christopher Nolan",
    "lead_actors": ["Christian Bale", "Heath Ledger"],
    "release_year": "2008-07-18",
    "rating": 9.0
  },
  "Inception": {
    "genre": ["Sci-Fi", "Action"],
    "type": "movie",
    "director": "Christopher Nolan",
    "lead_actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"],
    "release_year": "2010-07-16",
    "rating": 8.8
  },
  "Breaking Bad": {
    "genre": ["Crime", "Drama"],
    "type": "tv",
    "director": "Vince Gilligan",
    "lead_actors": ["Bryan Cranston", "Aaron Paul"],
    "release_year": "2008-01-20",
    "rating": 9.5
  },
  "The Social Network": {
    "genre": ["Drama"],
    "type": "movie",
    "director": "David Fincher",
    "lead_actors": ["Jesse Eisenberg", "Andrew Garfield"],
    "release_year": "2010-10-01",
    "rating": 7.7
  },
  "Interstellar": {
    "genre": ["Sci-Fi", "Adventure"],
    "type": "movie",
    "director": "Christopher Nolan",
    "lead_actors": ["Matthew McConaughey", "Anne Hathaway"],
    "release_year": "2014-11-07",
    "rating": 8.6
  },
  "Stranger Things": {
    "genre": ["Sci-Fi", "Horror"],
    "type": "tv",
    "director": "The Duffer Brothers",
    "lead_actors": ["Millie Bobby Brown", "Finn Wolfhard"],
    "release_year": "2016-07-15",
    "rating": 8.7
  },
  "Fight Club": {
    "genre": ["Drama"],
    "type": "movie",
    "director": "David Fincher",
    "lead_actors": ["Brad Pitt", "Edward Norton"],
    "release_year": "1999-10-15",
    "rating": 8.8
  },
  "The Matrix": {
    "genre": ["Sci-Fi", "Action"],
    "type": "movie",
    "director": "The Wachowskis",
    "lead_actors": ["Keanu Reeves", "Laurence Fishburne"],
    "release_year": "1999-03-31",
    "rating": 8.7
  },
  "True Detective": {
    "genre": ["Crime", "Drama"],
    "type": "tv",
    "director": "Nic Pizzolatto",
    "lead_actors": ["Matthew McConaughey", "Woody Harrelson"],
    "release_year": "2014-01-12",
    "rating": 8.9
  }
}


app = FastAPI()

@app.get('/')
def root():
    return {'health':'API online'}

@app.get ('/view_all')
def view_all():
    return data_set

#pull up all info by name
@app.get('/movie')
def name_search(name: str):
    return data_set[name]

@app.get('/filter')
def filter_by(genre_search: str):
    results=[]
    for key, details in data_set.items():

        if genre_search in data_set[key]['genre']:
            results.append( {key:details})
        else:
            pass
    return results

