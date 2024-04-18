# Instantiate empty dictionaries and constants
LLM_Dict = {}
Articles_Dict = []
NUM_ARTICLES = 10

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
        print("3. Get rankings")
        print("-1. Exit")

        selection = input("Please enter your choice (1-5): ")
        print()

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
        print()
        getPercentResults()
        runMenu()
    elif userChoice == 2:
        # Another function call for option 2
        print()
        getArticleResults()
        runMenu()
    elif userChoice == 3:
        # Another function call for option 3
        print()
        getRankings()
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
        print(f"success rate: {numberHuman/NUM_ARTICLES*100}%")


        print()  # Adds a blank line for better separation between entries

def getRankings():
    # Initialize an empty list to store (LLM, ratio) tuples
    LLM_ratios = []

    for key, values in LLM_Dict.items():
        numberHuman = 0
        numberMachine = 0
        for value in values:
            if "human" in value:
                numberHuman += 1
            if "machine" in value:
                numberMachine += 1

        # To avoid division by zero, check if numberHuman is not zero
        if numberHuman > 0:
            ratio = numberHuman / NUM_ARTICLES
        else:
            # Handle the case where numberHuman is 0; you might assign a default value
            # such as 0 or skip adding this LLM to the list.
            ratio = 0  # or continue to skip this entry

        # Append the (LLM, ratio) tuple to the list
        LLM_ratios.append((key, ratio))

    # Sort the list by the ratio in ascending order
    LLM_ratios.sort(key=lambda x: x[1], reverse=True)

    # Print the sorted results
    print("LLM Rankings by Human Response to number of Articles Ratio:")
    for LLM, ratio in LLM_ratios:
        print(f"{LLM}: Ratio = {ratio:.2f}")
    print()



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
        print()
    display_table(Articles_Dict)


runMenu()