from datetime import datetime as dt
from src.add import add

def lambda_handler(event, context):
    number1 = event['number1']
    number2 = event['number2']
    res = add(number1, number2)

    now = dt.now()
    print("Commit at ", now)
    return {
        "time" : str(now),
        "result" : res
    }


