class User:
    'Class for all users'
    user_count=0
    def __init__(self, name , age , adress ):
        self.name = name
        self.age = age
        self.adress = adress

    def User_param(self):
        print(f'{self.name} from {self.adress}')

USER_1 = User('Ivan', 22, 'Rostov')
USER_1.User_param()
