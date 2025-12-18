#  Given a list of names, print only the ones that contain “a” or “A”.

# ```python
# Input: ["Meera", "John", "Kavi", "Sona"]
# Output: Meera Kavi Sona
# Explanation: These names include the letter 'a'
# ```  

def is_finding(names):
    if len(names) == 0:
        print("Invalid Input")
    else:
        variables = "a","A"
        result = ""
        for i in range(0,len(names),+1):
            # print(names[i])
            if names[i] == variables:
                print(names[i])
is_finding(["Meera", "John", "Kavi", "Sona"])