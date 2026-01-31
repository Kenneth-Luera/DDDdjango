from value_objects import Email, Role, AccountStatus, Balance
import uuid

class User:
    def __init__(self, user_id: uuid.UUID, username: str, email: Email, rol: Role, account: AccountStatus, balance: Balance):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.rol = rol
        self.account = account
        self.balance = balance

    def change_role(self, new_role: Role):
        self.rol = new_role

    def update_account_status(self, new_status: AccountStatus):
        self.account = new_status

    def update_balance(self, amount: Balance):
        self.balance = amount