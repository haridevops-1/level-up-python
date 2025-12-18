# 1. An online shopping platform receives coupon codes typed by customers,
# but many of them contain spaces, symbols, or uppercase characters.
#  Your task is to clean the coupon code so it contains only uppercase alphabets and digits; remove everything else.

def receive_coupon_code(sentence):
    if len(sentence) == 0:
        print("Invalid Input")
    else:
        result = ""
        alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        for el in range(0,len(sentence)):
            if sentence[el] in alpha or sentence[el] == " " or sentence[el] in numbers:
                result += sentence[el].upper()
        return result
    
print(receive_coupon_code("ab#12!cd@EF3"))
# Output: AB12CDEF3