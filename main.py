from caesar import encrypt
import webapp2
import cgi
import re

USER_RE = re.compile(r"^[a-zA-Z]$")
def valid_text(text):
    return USER_RE.match(text)

rot13_form="""
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
            p.error {
                color: red;
            }
        </style>
    </head>
    <body>
        <form method="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rotate" value="0">
                <p class="error"></p>
            </div>
            <textarea type="text" name="text">%(text)s</textarea>
            <br>
            <input type="submit" value="Submit" />
        </form>
    </body>
</html>
"""

#answer = encrypt("Hello, Zach!", 2)
#print(answer)
# => prints Jgnnq, Bcej!

class MainHandler(webapp2.RequestHandler):

    def write_form(self, text="", rotate=""):
               self.response.out.write(rot13_form % {'text': text,
                                    'rotate': rotate })

    def get(self):
        self.write_form()

    def post(self):
        text = self.request.get('text')
        text = cgi.escape(text, quote=True)
        rotate = self.request.get('rotate')
        ans = ""

        for i in text:
            if valid_text( i ):
                ans += encrypt( i, rotate)
            else:
                ans += cgi.escape( i , quote=True)

        self.write_form( ans, rotate )

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
