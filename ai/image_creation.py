import openai
from constants import constants
import webbrowser
from PIL import Image

openai.api_key = constants["openai_api_key"]

# ------------------------------------------------
# response = openai.Image.create(
#   prompt="a cycling race on the Alps",
#   n=1,
#   size="1024x1024"
# )
# image_url = response['data'][0]['url']
# Adding the GUI interface
 
# To convert the image From JPG to PNG : {Syntax}
# img = Image.open("cycling.jpg")
# img.save("cycling.png")
# new_img = img.resize((720,720))
# new_img.show()
# new_img.save("cycling2.png")

# ------------------------------------------------
try:
	response = openai.Image.create_variation(
	  image=open("image2.png", "rb"),
	  n=1,
	  size="1024x1024",

	)
	image_url = response['data'][0]['url']
	print(response)

except openai.error.OpenAIError as e:
  print(e.http_status)
  print(e.error)

# ------------------------------------------------
# response = openai.Image.create_edit(
#   image=open("mage2.png", "rb"),
#   mask=open("mask.png", "rb"),
#   prompt="A sunlit indoor lounge area with a pool containing a flamingo",
#   n=1,
#   size="1024x1024"
# )
# image_url = response['data'][0]['url']

# ------------------------------------------------
# response = openai.Image.create_edit(
#   image=open("image.jpg", "rb"),
#   mask=open("mask.png", "rb"),
#   prompt="A sunlit indoor lounge area with a pool containing a flamingo",
#   n=1,
#   size="1024x1024"
# )
# image_url = response['data'][0]['url']

# ------------------------------------------------

webbrowser.open(image_url) 

# print(image_url)