
class Config:
    # Use env variables
    # account_sid = os.environ.get('ACCOUNT_SID')
    # auth_token = os.environ.get('AUTH_TOKEN')
    # my_cell = os.environ.get('MY_CELL')
    # twilio_number = os.environ.get('TWILIO_NUMBER')

    # Or enter them directly
    account_sid = "your_twilio_account_sid"
    auth_token = "your_twilio_auth_token"
    cells = ["+12345678901", "+18008675309"]
    twilio_number = "your_twilio_number"