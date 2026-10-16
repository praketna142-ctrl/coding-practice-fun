import csv 

def Air_bender_Ethnicity(filepath): 
    """Reads the file and finds any mention of Airbender, adding it to the empty dictionary"
        Args: 
            File 
        Return: 
            Air Nomads different backgrounds
     """
    with open(filepath, "r") as fh: 
        reader = csv.DictReader(fh) 
        information = {} 
        for row in reader: 
            ethnicity = row["Ethnicity"]

            if "Air Nomad" in ethnicity:
                information[ethnicity] = information.get(ethnicity, 0) + 1
        return information 


def main(): 
    reading_data = Air_bender_Ethnicity("avatar_characters_data.csv")
    print(reading_data)

if __name__ == "__main__":
    main() 
