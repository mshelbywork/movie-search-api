Movie search api with search, filtering, and sorting capibilities.

filter by:
    -genre
    -movie | tv
    -director
    -lead actor/actresses
    -date
sort by:
    rating
    alphabetical (tied to query param)
    chronological

considerations:
initial build will pull from a dictionary with precreated data. I think possibly writing to a file or even a database would be more practical if I have to consider scaling up later down the line. 
    -since I'm not adding entries through the api right now that feels like overkill.

edge cases:
-missinng/incomplete data entries
-endpoint failures
-user query errors 

api should gracefully handle errors and validate data sent to and from the user.
    pydantic schemas for customer sending and receiving
    raise helpful error messages for incomplete or missing data.
    
    search endpoints should function independently. Meaning if data is missing for genre it shouldn't affect a request to filter by director.
        -all query params optional?

organaztion:
Will follow Fastapi standard file managment
    possibly a seperate directory if I ever add a front end to this.




