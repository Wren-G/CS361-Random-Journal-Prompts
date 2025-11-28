# -----------------------------------------------------------------------------------------------------------
# prompts.py
# Project: CS361 Random Quotes Generator
# Purpose: ZeroMQ REP microservice that returns a random journaling prompt
# Author: Wren Gilbert
# Date: 2025-11-21
# Usage: Run `python prompts.py`. Client sends string 'prompt' as the request;
#        the service responds with a quote string.
# -----------------------------------------------------------------------------------------------------------

import random
import zmq
import time

PROMPT = {
        "Do you enjoy your current lifestyle? If not, why not?",
        "What moment made you grateful this past week?",
        "Write a letter to someone important to you, or your past or future self.",
        "What is something you want to do on your bucket list, or want to add to it?",
        "What helps you get through the day right now?",
        "What is a good deed you would like to do?"
        "Who is a really important person in your life right now?",
        "When was the last time you took a trip?",
        "What do you need to get off your chest?",
        "What is a memory that never fails to make you smile?",
        "What is something you are looking forward to?"
}


def get_quote(request: str) -> str:
    if request.strip().lower() == "prompt":
        return random.choice(PROMPT)
    return "Error: send 'prompt' to receive a prompt."



def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind('tcp://*:5588')
    print('Microservice is running on port 5588...')

    try:
        while True:   
              # wait for next request from client
              message = socket.recv_string()
              response = get_quote(message)
              time.sleep(0.5)
              socket.send_string(response)

    except KeyboardInterrupt:
        print("Shutting down microservice...")
    finally:
        # ensure proper cleanup of zmq context
        context.destroy()

if __name__ == "__main__":
    main()
