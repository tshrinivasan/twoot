# Twoot

A python script to send a given text to twitter as tweet and mastodon as toot.

- Edit the twoot.py
- Fill the API keys for twitter and mastodon
- Run it as `python3 twoot.py`


# TODO

- if charecter count is > 280, it wont publish. Make it to publish as a thread, if length > 280


# Using with emacs

I have a cruid hack way to use the same with emacs.

- copy the twoot.py to /bin
- Open Emacs
- Type something
- Select the text as region
- Press M-| 
- It will ask for command to run
- type as `twoot.py`
- Done. The selected text at the region will be given as input for the twoot.py and it will be published.

# Note

This is not the standard way to integrate things with Emacs. Have to write the same code in elisp to post in twitter and toot at the same time.
Till, I learn list and implement on the emacs way, hope this hack is fine.


# LICENSE

GPL v3
