import os
import csv

with open('Analysis/analysis.txt', 'a') as f:

    election_csv = os.path.join(".", "Resources", "election_data.csv") # "." since both folders areat the same "level"


    # Open and read csv
    with open(election_csv) as csv_file:
        
        csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
        csv_header = next(csv_file)

    # Calculate the total number of votes cast
    # The complete list of candidates who received votes

        total_votes = 0
        candidates = dict()

        for i in csv_reader:
            total_votes = total_votes + 1
            
            if i[2] in candidates:
                candidates[i[2]] =  candidates[i[2]] + 1

            else:
                candidates[i[2]] = 1  
        
        print(f"Total Votes: {total_votes}")
        f.write(f"Total Votes: {total_votes}")

    # The complete list of candidates who received votes
    # The winner of the election based on popular vote
        max_value = 0
        max_key = 0

        for key, value in candidates.items():
            calc = value/total_votes
            percentage = calc*100
            print(f"{key}: {round(percentage, 3)}% ({value})")
            f.write(f"{key}: {round(percentage, 3)}% ({value})")
            if value > max_value:
                max_value = value
                max_key = key
        
        print(f"Winner: {max_key}")
        f.write(f"Winner: {max_key}")


               

             


        




