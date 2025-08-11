#method overriding
class normaluser:
    def playvideo(self,name):
        print(f"\n{name} is playing video with :\n1.Normal Quality\n2.Ads run\n3.No background play\n4.Limited videos download\n4.Music with ads")
class premiumUser(normaluser):
    def playvideo(self,name):
        print(f"\n{name}is playing video with :\n1.High Quality\n2.No Ads run\n3.background play\n4.videos download\n4.Music without ads")
vishwas=normaluser()
raj=premiumUser()
vishwas.playvideo('vishwas')
raj.playvideo('raj')
print("_________")
class normaluser:
    def playvideo(self,name):
        print(f"\n{name} is playing video with :\n1.Normal Quality\n2.Ads run\n3.No background play\n4.Limited videos download\n4.Music with ads")
class premiumUser(normaluser):
    def playvideo(self,name):
        print(f"\n{name}is playing video with :\n1.High Quality\n2.No Ads run\n3.background play\n4.videos download\n4.Music without ads")
def play_video(user,username):
    user.playvideo(username)
vishwas=normaluser()
goutham=premiumUser()
reddy=normaluser()
varma=premiumUser()
play_video(vishwas,"vishwas")
play_video(goutham,'goutham')
play_video(reddy,'reddy')
play_video(varma,'varma')
#opertional overloaded
class number:
    def __init__(self,n):
        self.n=n
    def __add__(self,other):
        return self.n+other.n
    def __sub__(self,other):
        return self.n-other.n
    def __mul__(self,other):
        return self.n*other.n
    def __str__(self):
        return f"{self.n}"
    def __lt__(self,other):
        return self.n<other.n
    def __gt__(self,other):
        return self.n > other.n
    def __eq__ (self,other):
        return self.n == other.n
number1=number(10)
number2=number(20)
print(number1+number2)
print(number1-number2)
print(number1*number2)
print(number1)
print(number1<number2)
print(number1>number2)
print(number1==number2)

#postviewer
class PostViewer: 
    def __init__(self, owner_name, private_account=False):
        self.owner_name = owner_name 
        self.__private_account = private_account  
        self.posts = []  
        self.followers = []
    def add_post(self, photo_url):
        self.posts.append(photo_url)
        self.posts.append(photo_url)
        print(f"{self.owner_name} added a new post.")
    def set_privacy(self, private_status):
        self.__private_account = private_status

        if private_status:
            print(f"{self.owner_name}'s account is now Private.")
        else:
            print(f"{self.owner_name}'s account is now Public.")
    def follow(self, follower_name):
        if follower_name not in self.followers:
            self.followers.append(follower_name)
            print(f"{follower_name} is now following {self.owner_name}.")
        else:
            print(f"{follower_name} is already following {self.owner_name}.")
    def view_posts(self, viewer_name):
        if not self.__private_account or viewer_name in self.followers:
            print(f"Posts by {self.owner_name}:")
            for post in self.posts:
                print(post)
        else:
            print(f"{self.owner_name}'s account is private. Follow them to view posts.")
sanjay=PostViewer("sanjay",True)       
sanjay.add_post("python course") 
sanjay.add_post("flask course")            
sanjay.add_post("sql course")            
sanjay.add_post("softskills course")            

dinesh=PostViewer("dinesh")
post=['candid pic', 'professional pic']  
for i in post:
    dinesh.add_post(i)
dinesh.follow("sanjay")
sanjay.follow("dinesh")
sanjay.view_posts("dinesh")  
dinesh.view_posts("sanjay")                  