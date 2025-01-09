import pymongo


class ExpenseMongoClient:
    def __init__(
            self,
            host: str,
            port: int,
            db_name: str = "expense_tracker",
            collection_name: str = "expenses",
    ):
        self.client = pymongo.MongoClient(host, port)
        self.db = self.client.get_database(db_name)
        self.collection = self.db.get_collection(collection_name)

    def add_expense(self, user_id: int, amount: int, category: str, description: str):
        self.collection.insert_one({
            "user_id": user_id,
            "amount": amount,
            "category": category,
            "description": description,
        })

    def get_expenses(self, user_id: int) -> list:
        cursor = self.collection.find({'user_id': user_id})
        return [
            {
                "amount": expense["amount"],
                "category": expense["category"],
                "description": expense["description"]
            }
            for expense in cursor
        ]

    def get_categories(self, user_id: int) -> list:
        result = self.get_expenses(user_id)
        result = list(map(lambda x: x['category'], result))
        return list(set(result))

    def get_expenses_by_category(self, user_id: int, category: str) -> list:
        result = self.collection.find({'user_id': user_id, 'category': category})
        return [
            {
                "amount": expense["amount"],
                "category": expense["category"],
                "description": expense["description"]
            }
            for expense in result
        ]

    def get_total_expense(self, user_id: int):
        result = self.get_expenses(user_id)
        result = list(map(lambda x: int(x['amount']), result))
        return sum(result)

    def get_total_expense_by_category(self, user_id: int):
        categories = self.get_categories(user_id)
        result = dict()
        for category in categories:
            result[category] = 0
            records = self.get_expenses_by_category(user_id, category)
            for record in records:
                result[category] += record['amount'] 
        return result   
