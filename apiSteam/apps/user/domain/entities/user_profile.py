class UserProfileEntity:
    def __init__(self, user_id, nickname=None, age=None, gender=None, description=None):
        self.user_id = user_id
        self.nickname = nickname
        self.age = age
        self.gender = gender
        self.description = description