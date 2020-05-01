import os, tornado.ioloop, tornado.web
from random import randint

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html", title="on the phone!", phonecaller=self.get_phonecaller(), phonecall_image=self.get_phonecall_image())

	def get_phonecaller(self):
		with open(os.path.join('assets', "funny_names.txt"), 'r') as F:
			funny_names = F.readlines()

		the_split = (len(funny_names) / 2)
		return "{0} {1}".format(funny_names[randint(0, the_split)], funny_names[randint(the_split, len(funny_names))])

	def get_phonecall_image(self):
		for _, _, files in os.walk(os.path.join('assets', 'phones')):
			break

		return files[randint(0, len(files) - 1)]

def run_app():
	return tornado.web.Application([
		(r'/', MainHandler),
		(r'/assets/(.*)', tornado.web.StaticFileHandler, {
			"path" : "assets"
		})
	])

if __name__ == "__main__":
	app = run_app()
	app.listen(8080)
	tornado.ioloop.IOLoop.current().start()