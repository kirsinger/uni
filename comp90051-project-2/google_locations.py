import googlemaps
import pandas as pd
import sys

from datetime import datetime

API_KEY = "AIzaSyA1O_iTXE6Yct_d6yvAisvQ51vqlL6nqfk"
OUTPUT  = "./data_frames/google_distances.pkl"

def main():
    
    #Get the cleaned data as reference
    base_data = pd.read_pickle("./data_frames/clean_data.pkl")
    
    #Set up the client
    gmaps = googlemaps.Client(key=API_KEY)

    #List of origin/destinations we want distances between
    places = [[loc, "victoria"] for loc in base_data.index]
    
    #Query each location, then merge the result
    data = []
    
    for place in places:
        
        print("Querying {}".format(place))
        json = gmaps.distance_matrix(
            " ".join(place), 
            [" ".join(dest) for dest in places]
        )
        
        place_data = pd.DataFrame(
            (row["elements"] for row in json["rows"]),
            index=[place[0]],
            columns=[dest[0] for dest in places]
        )
        
        actual_distances = pd.DataFrame(
            index=place_data.index,
            columns=place_data.columns,
            dtype=float
        ).fillna(0.0)
        
        for row in place_data.index:
            for col in place_data.columns:
                actual_distances.loc[row][col] = place_data.loc[row][col]["distance"]["value"]
        
        data.append(actual_distances)
        
    data = pd.concat(data)
    data.to_pickle(OUTPUT)
    
    print("Done! output saved to {}".format(OUTPUT))
    
if __name__ == "__main__":
    print("\n\nPLEASE NOTE BEFORE RUNNING:")
    print("---------------------------")
    print("""
    You're only allowed a set number of calls to the
    Google distance matrix API each day. 
    This script will use up a big chunk of those calls.
    """)
    print("""
    Chances are the data generated by this script already 
    exists. If it does, it will be stored in: \n
    ./data_frames/google_distances.pkl. \n
    If this data does not exist, type "y" to continue.
    Otherwise type anything else to quit.
    """)
    
    answer = raw_input(">>")
    
    if answer == "y":
        print("scriptifying")
        #main()
    else:
        sys.exit(0)