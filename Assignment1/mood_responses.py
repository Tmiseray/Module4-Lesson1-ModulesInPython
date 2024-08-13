def mood_response(mood):
    if mood == 'happy':
        return "\nThat's great! There's many things to be happy about in life!"
    elif mood == 'sad':
        return "\nOh no! I'm sorry to hear that! Maybe a comedy like 'Deadpool' could brighten your day."
    elif mood == 'excited':
        return "\nOh really?! It must be your birthday or a big event today! Either way, CONGRATULATIONS!!"
    else:
        return "\nMy apologies.. I don't understand how to process that mood..."