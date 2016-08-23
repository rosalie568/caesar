from caesar import encrypt
import webapp2
import cgi
import re

USER_RE = re.compile(r"^[a-zA-Z]$")
def valid_text(text):
    return USER_RE.match(text)

#answer = encrypt("Hello, Zach!", 2)
#print(answer)
# => prints Jgnnq, Bcej!

class MainHandler(webapp2.RequestHandler):

    def get(self):
        text = ""

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
                    <textarea type="text" name="text">""" + cgi.escape( text, quote=True) + """</textarea>
                    <br>
                    <input type="submit" value="Submit" />
                </form>
            </body>
        </html>
        """

        self.response.write(rot13_form)

    def post(self):

        text = self.request.get('text')
        rotate = int ( self.request.get('rotate') )

        if( text == ""):
            error = "You didn't enter anything"
            self.redirect("/?error" + error)
            return

        ans = encrypt(text, rotate)

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
                    <textarea type="text" name="text">""" + cgi.escape( ans, quote=True) + """</textarea>
                    <br>
                    <input type="submit" value="Submit" />
                </form>
            </body>
        </html>
        """

        self.response.write(rot13_form)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
