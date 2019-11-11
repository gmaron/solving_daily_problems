# Problem Day 6 (MEDIUM)

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.  
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.




# decode_message_way_1() it's like a binary tree.
# There is duplicated solutions
# This is a O(n^2) solution
def decode_message_way_1(message):
    if message.startswith('0'):
        return 0
    elif len(message)<=1:
        return 1
    result = decode_message_way_1(message[1:])
    if int(message[:2]) <= 26:
        result += decode_message_way_1(message[2:])
    return result


# decode_message_way_with_memo
# With a cache memory you can see what was the previous path
# So it's TC: O(n) and SC: O(n)
def decode_message_way_with_memo(message, memo):

    if message.startswith('0'):
        return 0
    
    # If it is one digit
    elif len(message)<=1:
        return 1
    
    if memo[len(message)] != None:
        return memo[len(message)]

    result = decode_message_way_with_memo(message[1:],memo)

    if int(message[:2]) <= 26:
        result += decode_message_way_with_memo(message[2:],memo)

    memo[len(message)] = result
    return result


encodedCases = ["111", "9242", "768", "1234321"]

for test in encodedCases:
    print(test, "==>" , decode_message_way_with_memo(test,[None]*(len(test)+1)))
