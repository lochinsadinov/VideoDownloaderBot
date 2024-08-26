from db.service import DB


class User(DB):
    def __init__(self, *cols,
                 user_id: int = None,
                 first_name: str = None,
                 last_name: str = None,
                 username: str = None,
                 phone_number: str = None,
                 created_at: str = None, ):
        self.cols = cols
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.phone_number = phone_number
        self.created_at = created_at
