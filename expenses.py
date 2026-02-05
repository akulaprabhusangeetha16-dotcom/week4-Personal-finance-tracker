from datetime import datetime

class Expense:
    def __init__(self, date, amount, category, description):
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.amount = float(amount)
        self.category = category
        self.description = description

    def to_dict(self):
        return {
            "date": self.date.isoformat(),
            "amount": self.amount,
            "category": self.category,
            "description": self.description
        }
