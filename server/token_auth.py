
# # Your token
# token = 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

from getpass import getpass
from huggingface_hub import notebook_login

def login_with_token():
    token = getpass("Token: ")
    notebook_login(token=token)

login_with_token()


