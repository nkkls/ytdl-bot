from flask import Flask
from threading import Thread
import random
app = Flask('')

@app.route('/')
def home():
  return 'the bot is now ready!'

def run():
  app.run(
    host='0.0.0.0',
    port=random.randint(2000,9000)
  )

def keepalive():
  t = Thread(target=run)
  t.start()
