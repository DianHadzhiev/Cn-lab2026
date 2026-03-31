# Setup

Simply run `source setup.sh`. That's it!

# Running code

First, ensure that your environment is set up.
You can check this by running `python3 --version`.
The output should be _Python 3.11.11_; if it is not, redo the [setup](#setup) step.

```bash
# Run A1
python3 -m a1_chat_client

# Run A3
python3 -m a3_chat_server

# Run A5
python3 -m a5_http_server

# Run A6
python3 -m a6_dns_server

# Run A7
python3 -m a7_unreliable_chat

# Run A8
python3 -m a8_game
```

# Running the sample server(s) (for A1)

To run the server your chat client will connect to, execute in a different terminal:

```bash
(cd infrastructure; python3 -m reliable_server)
```

If any errors occur, ensure that you first executed the [setup](#setup) step.

# Uploading to CodeGrade

Execute `python3 export.py a1` (or replace `a1` with the correct assignment) to create a zip archive.
Then, upload it to CodeGrade.
