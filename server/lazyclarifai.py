from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from lazyfood import lazyfood

class lazyclarifai:
	app = ClarifaiApp(api_key='ae776170d518477493e5e62f3849ba4d')
	lf = lazyfood()

	model = app.models.get('food-items-v1.0')
	ingredientlist =[]

	def start(self, filename):
		image = ClImage(file_obj=open(filename, 'rb'))

		tags =model.predict([image])
		i=0
		for tag in tags['outputs'][0]['data']['concepts']:
			if i==0: #tag['value']>=.97: #i==0:	
				term =tag['name']
				ingredientlist.append(term)
				#print term
				#lf.search(term)
				i=1
	def search(self):
		lf.search(ingredientlist)#i might have gotten confused? 
