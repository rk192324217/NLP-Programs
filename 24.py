dialog = [
    "Hello",
    "Can you help me?",
    "Thank you"
]

for utterance in dialog:
    if utterance.endswith("?"):
        act = "Question"
    elif utterance.lower().startswith("thank"):
        act = "Thanking"
    else:
        act = "Statement"

    print(f"'{utterance}' -> {act}")
