import hashlib
import requests

import sys
import json

from time import time

spacer = '\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'

if __name__ == '__main__':
    # What is the server address? IE `python3 miner.py https://server.com/api/`
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    print(spacer)
    print('Lambda School - Wallet App')

    # Input miner id or user id here
    miner_id = input('Please input your id: ')
    print(spacer)

    # Run forever until interrupted
    is_running = True

    while is_running:

        # Display input options
        print(
            f"What would you like to do? \n [1] Check Balance   [2] Check Transactions   [3] Change User [4] Quit")
        choice = int(input('Please enter your option: '))
        print(spacer)

        # Error handling for incorrect input
        while choice not in [1, 2, 3, 4]:
            print(
                "Invalid option. Please, choose: \n[1] Check Balance   [2] Check Transactions   [3] Change User [4] Quit")
            choice = int(input('Please enter your option: '))
            print(spacer)

        if choice == 1:
            # Post Data to get miner balance
            post_data = {"id": miner_id}
            # Make post request to blockchain
            r = requests.post(
                url=node + "/transactions/balance", json=post_data)
            data = r.json()
            print(f"Your balance is {data['balance']}")
            print(spacer)
        elif choice == 2:
            # Post Data to get miner balance
            post_data = {"id": miner_id}
            # Make post request to blockchain
            r = requests.post(
                url=node + "/transactions", json=post_data)
            data = r.json()
            print(f"Transaction History:")
            for transactions in data["transactions"]:
                print(transactions)
            # print(data["transactions"])
            print(spacer)
        elif choice == 3:
            miner_id = input('Please input your id: ')
        else:
            is_running = False
