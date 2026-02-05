def category_report(expenses):
    report = {}
    for e in expenses:
        report[e.category] = report.get(e.category, 0) + e.amount
    return report
