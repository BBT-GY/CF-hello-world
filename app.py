import os
from flask import Flask
import os.path

if os.path.isfile("setenv.py"):
    print "I found it. I must be LOCAL"
    import setenv
else:
    print "I must be running in PWS"

app = Flask(__name__)

@app.route('/')
def mainmenu():

    return """
    <html>
    <body>
    <center><h1>Hello World!</h1><br/>
    </body>
    </html>"""

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
	
applications:
	name: piperhw123
	memory: 64M
	disk_quota: 256M
	instances: 1
	credentialID: yahata@bbtower.co.jp

print("Test2")
