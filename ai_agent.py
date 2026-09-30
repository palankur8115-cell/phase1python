from datetime import datetime


# ---------- TOOLS ----------

def calculator(expression):
    try:
        # Simple calculator for basic arithmetic
        result = eval(expression, {"__builtins__": {}}, {})
        return f"Result: {result}"
    except:
        return "Sorry, I couldn't calculate that."


def get_time():
    current_time = datetime.now().strftime("%I:%M:%S %p")
    return f"Current time is {current_time}"


# ---------- AI AGENT ----------

def ai_agent(user_input):

    text = user_input.lower()

    # Decide which tool to use
    if "time" in text:
        return get_time()

    elif any(symbol in user_input for symbol in ["+", "-", "*", "/"]):
        return calculator(user_input)

    elif "hello" in text or "hi" in text:
        return "Hello! How can I help you?"

    elif "your name" in text:
        return "I am your simple Python AI Agent."

    else:
        return "I don't know how to handle that yet."


# ---------- CHAT LOOP ----------

print("🤖 Simple AI Agent Started!")
print("Type 'exit' to stop.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Agent: Goodbye! 👋")
        break

    response = ai_agent(user_input)

    print("Agent:", response)