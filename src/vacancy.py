class Vacancy:

    def __init__(self, title, description, currency, salary):
        self.title = title
        self.description = description
        self.currency = currency
        self.salary = salary if salary else 0

    def __repr__(self):
        return f'Vacancy(title={self.title}, description={self.description}, currency={self.currency}, salary={self.salary})'

    def __lt__(self, other):
        return self.salary < other.salary
