class ConversationState:
    def __init__(self):
        self.excluded_prices = []
    
    def mark_expensive(self):
        if "high" not in self.excluded_prices:
            self.excluded_prices.append("high")
        elif "medium" not in self.excluded_prices:
            self.excluded_prices.append("medium")
            
    def reset(self):
        self.excluded_prices = []