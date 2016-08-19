from caesar import encrypt
import webapp2

rot13_form="""
<!DOCTYPE html>
<html>
    <head>
        <title> Caesar Page </title>
    </head>
    <body>
        <h1>Enter some text to ROT13!</h1>
        <form method="post">
            <textarea name="text" placeholder="%(text)s" style="height: 100px; width: 400px;"></textarea><br><br>
            <input type="submit" value="Submit" />
        </form>
    </body>
</html
"""

#answer = encrypt("Hello, Zach!", 2)
#print(answer)
# => prints Jgnnq, Bcej!

class MainHandler(webapp2.RequestHandler):

    def write_form(self, text=""):
               self.response.out.write(rot13_form % {'text': text})

    def get(self):
        self.write_form()

    def post(self):
        text = self.request.get('text')

        self.write_form(text)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
