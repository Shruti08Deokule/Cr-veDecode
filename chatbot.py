# chatbot.py

chat_memory = []

def get_bot_response(user_input):
    user_input = user_input.strip().lower()

    if "cravings" in user_input and "what" in user_input:
        return "Cravings are signals from your body or brain — they may reflect nutritional needs or emotional states."

    elif "types" in user_input:
        return "Types of cravings include: Sweet, Salty, Spicy, Crunchy, Junk, and Emotional cravings."

    elif "sweet" in user_input:
        return "Sweet cravings may be linked to chromium deficiency or emotional stress. Try fruits or cinnamon tea."

    elif "salty" in user_input:
        return "Salty cravings may signal sodium imbalance. Try soup, olives, or homemade trail mix."

    elif "spicy" in user_input:
        return "Spicy cravings may reflect desire for stimulation or variety. Enjoy it mindfully and stay hydrated!"

    elif "junk" in user_input and "avoid" in user_input:
        return "To avoid junk, keep healthy snacks nearby, stay hydrated, and manage stress with activities like walking or journaling."

    elif "healthy alternative" in user_input:
        return "Instead of chips → try roasted chickpeas. Instead of chocolate → go for dates or almonds. Small swaps matter!"

    elif "how" in user_input and "health" in user_input:
        return "Cravings can affect weight, mood, and digestion. Uncontrolled cravings may lead to bingeing or low energy."

    elif user_input in ["yes", "yes please", "sure", "yup"]:
        return "What else would you like to know?\nOptions:\n- What are cravings?\n- Types\n- Sweet/Salty/Spicy Meaning\n- Healthy alternatives\n- Avoid junk\n- Cravings and health"

    elif user_input in ["no", "nah", "nope"]:
        return "Thanks for using CraveDecode 💙\nHave a nice day!"

    else:
        return "I’m still learning! Try asking about cravings, sweet cravings, or healthy alternatives."
