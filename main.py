from finance_tracker.expenses import Expense
from finance_tracker.expense_manager import ExpenseManager
from finance_tracker.file_handler import save_expenses, load_expenses
from finance_tracker.reports import category_report


# ---------- UI FUNCTIONS ----------
def print_header():
    print("=" * 60)
    print("          PERSONAL FINANCE TRACKER")
    print("=" * 60)


def print_menu():
    print("\n" + "=" * 40)
    print("              MAIN MENU")
    print("=" * 40)
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. Search Expenses")
    print("4. Generate Monthly Report")
    print("5. View Category Breakdown")
    print("6. Set/Update Budget")
    print("7. Export Data to CSV")
    print("8. View Statistics")
    print("9. Backup/Restore Data")
    print("0. Exit")
    print("=" * 40)


# ---------- MAIN CLASS ----------
class FinanceTracker:
    def __init__(self):
        self.manager = ExpenseManager()
        self.manager.expenses = load_expenses()

    def run(self):
        print_header()

        while True:
            print_menu()
            choice = input("\nEnter your choice (0-9): ").strip()

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.search_expenses()
            elif choice == "4":
                self.generate_monthly_report()
            elif choice == "5":
                self.view_category_breakdown()
            elif choice == "6":
                self.set_budget()
            elif choice == "7":
                self.export_data()
            elif choice == "8":
                self.view_statistics()
            elif choice == "9":
                self.backup_restore()
            elif choice == "0":
                print("\n" + "=" * 60)
                print("Thank you for using Personal Finance Tracker!")
                print("=" * 60)
                save_expenses(self.manager.expenses)
                break
            else:
                print("❌ Invalid choice! Please enter 0-9.")

    # ---------- FEATURES ----------
    def add_expense(self):
        print("\n--- ADD NEW EXPENSE ---")
        date = input("Date (YYYY-MM-DD): ")
        amount = input("Amount: ")
        category = input("Category: ")
        description = input("Description: ")

        try:
            expense = Expense(date, amount, category, description)
            self.manager.add_expense(expense)
            save_expenses(self.manager.expenses)
            print("Expense added successfully!")
        except Exception as e:
            print("Error:", e)

    def view_expenses(self):
        print("\n--- ALL EXPENSES ---")
        if not self.manager.expenses:
            print("No expenses found.")
            return

        for i, e in enumerate(self.manager.expenses, start=1):
            print(f"{i}. {e.date} | ₹{e.amount} | {e.category} | {e.description}")

    def search_expenses(self):
        print("\n--- SEARCH EXPENSES ---")
        keyword = input("Enter keyword (category/description): ").lower()

        results = [
            e for e in self.manager.expenses
            if keyword in e.category.lower() or keyword in e.description.lower()
        ]

        if not results:
            print("No matching expenses found.")
            return

        for e in results:
            print(f"{e.date} | ₹{e.amount} | {e.category} | {e.description}")

    def generate_monthly_report(self):
        print("\n--- MONTHLY REPORT ---")
        print("Feature coming soon!")

    def view_category_breakdown(self):
        print("\n--- CATEGORY BREAKDOWN ---")
        report = category_report(self.manager.expenses)

        if not report:
            print("No data available.")
            return

        for category, amount in report.items():
            print(f"{category:<15} : ₹{amount}")

    def set_budget(self):
        print("\n--- SET / UPDATE BUDGET ---")
        print("Feature coming soon!")

    def export_data(self):
        print("\n--- EXPORT DATA ---")
        print("Feature coming soon!")

    def view_statistics(self):
        print("\n--- STATISTICS ---")
        print("Feature coming soon!")

    def backup_restore(self):
        print("\n--- BACKUP / RESTORE ---")
        print("Feature coming soon!")
