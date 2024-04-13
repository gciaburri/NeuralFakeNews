# Need: Filereader, LLM Hashmaps, Algorithm to process data in
# hashmap, and a way to display the data.

# instantiate a data structure that will house the data to be able to query it
# could use a dictionary (hash map, python calls it dictionary)

# example1: storing with articles as a key, followed by if each 
# grover thought it was a machine generated code for each LLM

# article 1 : yes, yes, no, no, yes, 500 words 
# article 2 : no, yes, yes, yes, no, 870 words
# article 3 : yes, no, yes, yes, yes, 400 words

# example2: storing with LLMs as key 

# ChatGPT4 : yes, yes, no, yes, no
# Claude : no, yes, yes, no, no
# Jurassic : no, no, no, yes, yes

# Instantiate empty dictionary
LLM_Dict = {}

# Open the file and read line by line
with open('results.txt', 'r') as file:
    for line in file:
        # Strip newline characters and any leading/trailing whitespace
        line = line.strip()
        
        # Split the line at the first comma to separate the key from the values
        key, values_string = line.split(',', 1)
        
        # Split the rest of the string by commas to get individual values
        values_list = values_string.split(',')
        
        # Strip any extra spaces around the values
        values_list = [value.strip() for value in values_list]
        
        # Add to dictionary with the key stripped of extra spaces
        LLM_Dict[key.strip()] = values_list

# Now LLM_Dict contains all keys and their corresponding lists as values
print(LLM_Dict)