class SMP:
    def __init__(self,username,posts,followers):
        self.username = username
        self.posts = posts
        self.followers = followers
        self.user_details = [] 

    def add_post(self):
        user = {
            'name': self.username, # 0(1)
            'followers': self.followers, # 0(1)
            'posts': self.posts    # 0(1)
        }

        self.user_details.append(user) # we are appending the user details with the user # o(n)
        return self.posts # 0(1)

    def Follow(self):
        for user in self.user_details:  # o(n)
            if user['name'] == self.username: # 
                user['followers']+=1 # o(1)
                break # o(1)
            else: # o(1)
                return "User details not found" # o(1)
        return user # o(1)
           
    # f(n) = o(n) +

    def UnFollow(self):
        for user in self.user_details:  
            if user['name'] == self.username: 
                user['followers']-=1 
                break 
            else: 
                return "User details not found" 
        return user    

    def info(self):
        return self.user_details

name = input("Enter your name: ")
post = input("make a post: ")
follower_num = int(input("how many followers do you have( be honesttttt 😏 ): "))
social_media = SMP(name, post, follower_num)

print(social_media.add_post())

print(social_media.Follow())

print(social_media.UnFollow())

print(social_media.info())


print("name: obasola ")
print("followers: 90")
print("posts: I want to rule the world")