#single inheritance
class status:
    def uploadImage(self,imageurl):
        self.image=imageurl
        print(f"{self.image} is uploaded to your status")
class statusv1(status):
    def addcaption(self,text=None):
        self.caption=text
        print(f'"{self.caption}" is added to your status')
sravani=status()
sravani.uploadImage('selfie.png')
hema=statusv1()
hema.uploadImage('GoodMrng.png')
hema.addcaption("Morning Friends!!!")
#1to2 inheritance
class status:
    def uploadImage(self,imageurl):
        self.image=imageurl
        print(f"{self.image} is uploaded to your status")
class statusv1(status):
    def addcaption(self,text=None):
        self.caption=text
        print(f'"{self.caption}" is added to your status')
class statusv2(status):
    def like(self):
        print(f'You can like status')
sravani=status()
sravani.uploadImage('selfie.png')
hema=statusv1()
hema.uploadImage('GoodMrng.png')
hema.addcaption("Morning Friends!!!")
vaishnavi=statusv2()
vaishnavi.uploadImage("Coffee.png")
vaishnavi.like()
#multiple inheritance
class status:
    def uploadImage(self,imageurl):
        self.image=imageurl
        print(f"{self.image} is uploaded to your status")
class statusv1(status):
    def addcaption(self,text=None):
        self.caption=text
        print(f'"{self.caption}" is added to your status')
class statusv2(status):
    def like(self):
        print(f'You can like status')
class statusv3(statusv1,statusv2):
    def addMusic(self,music):
        self.music=music
        print(f'{self,music}...is added to your status')
class statusv4(statusv3):
    def videolength(self,video):
        self.video=video
        print(f'{self.video}is uploaded to your status')
sravani=status()
sravani.uploadImage('selfie.png')
hema=statusv1()
hema.uploadImage('GoodMrng.png')
hema.addcaption("Morning Friends!!!")
vaishnavi=statusv2()
vaishnavi.uploadImage("Coffee.png")
vaishnavi.like()
deepika=statusv3()
deepika.uploadImage("mountains_and_Trees.png")
deepika.addcaption("no wifi")
deepika.like()
deepika.addMusic("Nature.mp3")
nikitha=statusv4()
nikitha.uploadImage("Sunrise.png")
nikitha.addcaption("Nothing")
nikitha.like()
nikitha.addMusic("Music")
nikitha.videolength("Somevideo.mp4")
#supper()method
class Instagram:
    def __init__(self,username):
        self.username=username
        self.post=[]
        print(f"{self.username.center(40,'-')}")
class Instagramv1(Instagram):
    def __init__(self,username,bio):
        super().__init__(username)
        self.bio=bio
        print(f'bio uploaded')
dinesh=Instagram('dinesh123')
sanjay=Instagramv1("sanjay","coder")
#supper() method 
class Instagram:
    def __init__(self,username):
        self.username=username
        self.post=[]
        print(f"{self.username.center(40,'-')}")
    def uploadpost(self,image):
        self.post=[]
        print(f"{image} is posted")
class Instagramv1(Instagram):
    def __init__(self,username,bio):
        super().__init__(username)
        self.bio=bio
        print(f'bio uploaded')
    def uploadpost(self,post,music):
        super().uploadpost(post)
        self.music=music
        print(f"")
