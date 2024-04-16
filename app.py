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
Articles_Dict = []

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

def menu():
    while True:  # This starts an infinite loop that will keep asking the user for input until a valid one is given
        print("What would you like to view?")
        print("1. Get overall results")
        print("2. Get results by Article")
        print("3. Option 3")
        print("4. Option 4")
        print("5. Option 5")
        print("-1. Exit")

        selection = input("Please enter your choice (1-5): ")

        # Check if the input is a digit and within the range 1-5
        if selection == "-1":
            print("Exiting the menu.")
            return None  # Return None or you could use another specific value to indicate the exit
        if selection.isdigit() and 1 <= int(selection) <= 5:
            return int(selection)  # Return the integer value of selection
        else:
            print("Invalid input. Please enter a number between 1 and 5.")
        



def runMenu():
    userChoice = menu()

    if userChoice is None:
        print("You chose to exit the menu.")
        return  # Exit the runMenu function

    if userChoice == 1:
        getPercentResults()
        runMenu()
    elif userChoice == 2:
        # Another function call for option 2
        getArticleResults()
        runMenu()
    elif userChoice == 3:
        # Another function call for option 3
        print("Option 3 selected.")  # Placeholder
        runMenu()
    elif userChoice == 4:
        # Another function call for option 4
        print("Option 4 selected.")  # Placeholder
        runMenu()
    elif userChoice == 5:
        # Another function call for option 5
        print("Option 5 selected.")  # Placeholder
        runMenu()


def getPercentResults():
    for key, values in LLM_Dict.items():
        print(f"LLM Model: {key}")
        numberHuman = 0
        numberMachine = 0
        for index, value in enumerate(values, start=1):
            # print(f"  {index}. {value}")
            if "human" in value:
                numberHuman += 1
            if "machine" in value:
                numberMachine += 1
            
        print(f"Number of times Grover thinks a human wrote the article: {numberHuman}")
        print(f"Number of times Grover thinks a machine wrote the article: {numberMachine}")
        print(f"success rate: {numberMachine/10*100}%")


        print()  # Adds a blank line for better separation between entries
# Usage
# user_choice = menu()
# print(f"You selected option {user_choice}.")
# commit comment testing
def getArticleResults():
    with open('articleResults.txt', 'r') as file:
        for line in file:
            # Strip newline character and split by comma
            parts = line.strip().split(', ')
            
            # Assuming the first part is the title and the rest are the results
            title = parts[0]
            results = parts[1:]
            
            # Append to the list as a dictionary
            Articles_Dict.append({
                'Title': title,
                'Results': results
                }
            )
    def display_table(articles):
        # Print the header
        print(f"{'Title':<70}{'GPT-4':<10}{'Gemini':<10}{'Jurrasic':<10}{'Claude':<10}{'Coral':<10}")
        print("-" * 130)  # Print a line for separation

        # Print each article's results
        for article in articles:
            # Ensure all result fields are filled, if not fill them with 'N/A'
            results = [res if res else 'N/A' for res in article['Results']]
            print(f"{article['Title'][:77]:<70}{results[0]:<10}{results[1]:<10}{results[2]:<10}{results[3]:<10}{results[4]:<10}")
    display_table(Articles_Dict)
    
runMenu()