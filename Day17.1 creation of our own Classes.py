class User:
    def __init__(self, user_id):   # Constructor function
        self.id = user_id
        self.followers=0
        self.following=0
    
    def follow(self,user):             #Addition of methods to class
        user.followers += 1
        self.following += 1



user1=User("001")
user2=User("99")

user1.follow(user1)
user2.follow(user1)
user1.follow(user2)

print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)