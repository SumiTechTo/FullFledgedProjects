import re
import long_responses as long

def get_response(user_input):
    split_message=re.split(r'\s+|[,;?.-]\s*',user_input.lower())
    response= check_all_messages(split_messages)
    return response
#Testing response
while True:
    print('Bot:'+ get_response(input('You:')))

