def create_youtube_video(tittle, description):
	video = {"Tittle": tittle, "Description": description, "Likes": 0, "Dislikes": 0, "Comments": {"Username": ""}}
	return video

def likes(video):
	if "likes" in video:
		video ["likes"]++
	return video

def dislikes(video):
	if "Dislikes" in video:
		video ["Dislikes"]++
	return video
	
def add_comment(youtubevideo, username, comment_text):
		




