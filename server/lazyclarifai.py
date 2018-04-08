from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from lazyfood import lazyfood

app = ClarifaiApp(api_key='ae776170d518477493e5e62f3849ba4d')
lf = lazyfood()

model = app.models.get('food-items-v1.0')

image = ClImage('https://www.almanac.com/sites/default/files/styles/primary_image_in_article/public/images/carrots.jpg?itok=_nIMWR5y')

tags =model.predict([image])
i=0
for tag in tags['outputs'][0]['data']['concepts']:
	if i==0:	
		term =tag['name']
		print term
		lf.search(term)
		i=1
