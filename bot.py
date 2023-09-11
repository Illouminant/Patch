from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import random


app = Flask(__name__)


@app.route("/bot", methods=["POST"])
def bot():
  message = request.values.get("Body", "").lower()
  res = MessagingResponse()
  res_message = res.message()


  if "help" in message:
    res_message.body("""
*нι тнere, мy ɴαмe ιѕ pαтcн!* 🐶\n_Here is a list of all that I am capable of, I'm so excited to get talking with you!_\n
_*hello, hi*_\n_If you type \"hello\" or \"hi\" in any way as a part of your message, I'll greet you back! This is a simple test command to be sure that I'm working._\n
_*dog, doggo, puppo*_\n_If you type \"dog\", \"doggo\" or \"puppo\" in any way as a part of your message, I'll send a random image of a dog! I'm a dog myself, so of course I'd show some love to my siblings!_\n
_*question*_\n_If you type \"question\" in any way as a part of your message, I'll give you my honest answer! ~Except not really because I'm a bot so it'll be randomised.~_
""")


  elif "hello" in message or "hi" in message:
    res_message.body("Hello! 👋")


  elif "dog" in message or "doggo" in message or "puppo" in message:
    r = requests.get("https://dog.ceo/api/breeds/image/random")
    data = r.json()
    res_message.media(data["message"])


  elif "question" in message:
    answer = ["Yes!",
              "No!",
              "Perhaps!",
              "Why do you ask?"
    ]
    res_message.body(f"{random.choice(answer)}") # Maybe change this to random.seed() later, and find a way to include the message contents


  else:
    res_message.body("Wha? I'm only a bot, whatever I know is hardcoded! Maybe try sending *\"help\"* to see what I'd recognise.")


  return str(res)


if __name__ == "__main__":
  app.run()
