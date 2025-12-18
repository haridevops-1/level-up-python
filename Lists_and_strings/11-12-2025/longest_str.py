# Given a string, find the longest continuous block of lowercase characters.
#  If no lowercase letter exists, print "".
# Input: "AAabcXYZpqrs123hello"
#  Output: "hello"


# def longest_lowercase(word):
#     longest = ""
#     current = ""
#     for i in word:
#         if i.islower():
#             current = current + i
#         else:
#             if len(longest) < len(current):
#                 longest = current
#             current = ""
#     if len(longest) < len(current):
#         longest = current
        
#     print(longest)
            
# longest_lowercase("AAabcXYZpqrsdf123hello")   
        