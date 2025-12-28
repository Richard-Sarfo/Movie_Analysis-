import json

def extract_data(data):
        """Extract 'name' values from a list of dictionaries."""
        return [d["name"] for d in data]

#function to extract data from a dictionary in the dataframe 
def extract_name(data, key='name'):
    """Parse JSON/dict and extract value by key, returning None if invalid."""
    if data is None or data == '':
        return None
    
    # If data is a string, parse it as JSON
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except:
            return None
    
    # If data is a dict, get the specified key
    if isinstance(data, dict):
        return data.get(key)
    
    return None

#Extracting director names 
def get_director(credits):
    """Return the director's name from credits dict, or None if not found."""
    crew = credits.get('crew', [])
    for person in crew:
        if isinstance(person, dict) and person.get('job') == 'Director':
            return person.get('name')
    return None


def separate_data(df, column):
    """Clean column by removing brackets/quotes and replacing commas with pipes."""
    df[column] = (
        df[column]
        .astype(str)
        .str.replace("[", "", regex=False)
        .str.replace("]", "", regex=False)
        .str.replace(",", "|", regex=False)
        .str.replace("'", "", regex=False)  
    )
    return df

