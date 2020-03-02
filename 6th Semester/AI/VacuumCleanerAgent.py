def simpleVacuumCleanerAgent(status, location):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location == "B":
        return "Left"

def main():
    board = {"A" : "Dirty", "B", "Dirty"}
    initial_state = ["A", "Dirty"]
    state = initial_state
    while True:
        action = 

