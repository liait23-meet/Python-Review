def create_youtube_video(tittle, description):
	video = {"Tittle": tittle, "Description": description, "Likes": 0, "Dislikes": 0, "Comments": {}}
	return video

def Likes(video):
	if "Likes" in video:
		video["Likes"] += 1;
	return video


def dislikes(video):
	if "Dislikes" in video:
		video["Dislikes"] +=1;
	return video
	
def add_comment(youtubevideo, username, comment_text):
	youtubevideo["Comments"][username] = comment_text
	return youtubevideo
		
my_video = create_youtube_video("Cats", "All about my cat")
add_comment(my_video, "Lia", "This youtube video is so funny!")
print(my_video)
print(my_video["Comments"])



for L in range (495):
	Likes(my_video)
 
print(my_video)