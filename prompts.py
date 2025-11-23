# -----------------------------------------------------------------------------------------------------------
# random_quotes.py
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
        "This too shall pass.",
        "This moment is not something happening to you, it is something you are making every moment, with every thought.",
        "You are growing, you are changing, but remember that one day you wished to be where you are right now.",
        "You don't have to control your thoughts. You just have to stop letting them control you. — Dan Millman",
        "The greatest weapon against stress is our ability to choose one thought over another. — William James",
        "Between stimulus and response, there is a space. In that space is our power."
        "to choose our response. In our response lies our growth and our freedom. — Viktor E. Frankl",
        "Criticizing yourself all the time or being judgmental of yourself is like wearing sunglasses indoors — Matthew McKay",
        "Tomorrow is a new day. You shall begin it serenely and with too high a spirit to be encumbered with your old nonsense. — Ralph Waldo Emerson",
        "In three words, I can summarize everything I've learned about life. It goes on. — Robert Frost",
        "Out of suffering have emerged the strongest souls; the most massive characters are seared with scars. — Khalil Gibran"
}


def get_quote(request: str) -> str:
    if request.strip().lower() == "prompt":
        return random.choice(PROMPTS)
    return "Error: send 'prompt' to receive a quote."



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
