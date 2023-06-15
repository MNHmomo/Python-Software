import re
import LongRes as long\

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1
    
    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
    
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0
    
def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses-------------------------------
    response("Hello!", ['hello', 'hi', 'yello', 'hey', 'heyo'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words = ['how'])
    response("Thank you!", ['i', 'love', 'momo'], required_words = ['momo'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.FAV_GAME, ['your', 'favorite', 'game', 'what', 'game', 'do', 'you', 'like', 'most'], required_words=['favorite', 'game'])
    response(long.LIST_GAME, ['what', 'other', 'games', 'do', 'you', 'like'], required_words=['you', 'games', 'like'])

    best_match = max(highest_prob_list, key = highest_prob_list.get)
    # print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r"\s+|[,;?!.-]\s*", user_input.lower())
    response = check_all_messages(split_message)
    return response

# Testing the Response System
while True:
    print("Bot: " + get_response(input("You: ")))