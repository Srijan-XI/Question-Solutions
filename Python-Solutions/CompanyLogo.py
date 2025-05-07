def companyLogo(s):
    # Dictionary to store the count of each character
    literal_cnts = {}
    
    # Create a set of distinct characters in the input string
    dist_letters = set(s)
    
    # Count the occurrences of each character and store in the dictionary
    for char in dist_letters:
        literal_cnts[char] = s.count(char)
    
    # Sort the dictionary items by count (descending) and ASCII value (ascending for ties)
    sorted_kv = sorted(literal_cnts.items(), key=lambda x: (x[1], -ord(x[0])), reverse=True)
    
    # Get the top 3 most frequent characters
    top_3 = sorted_kv[:3]
    
    # Handle cases where the top 3 characters have the same or similar frequencies
    if top_3[0][1] == top_3[1][1] and top_3[0][1] > top_3[2][1]:
        # Sort the first two characters if their frequencies are the same
        top_3[:2] = sorted(top_3[:2])
    elif top_3[1][1] == top_3[2][1]:
        # Sort the last two characters if their frequencies are the same
        top_3[1:] = sorted(top_3[1:])
    elif top_3[0][1] == top_3[1][1] == top_3[2][1]:
        # Sort all three characters if their frequencies are the same
        top_3 = sorted(top_3)
    
    # Print the top 3 characters and their frequencies
    for k, v in top_3:
        print(k, v)

if __name__ == '__main__':
    # Take input string from the user
    S = input()
    # Call the function to process the input string
    companyLogo(S)