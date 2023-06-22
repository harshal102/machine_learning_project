from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
import sys
app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("we are testing custom exception")
    except Exception as e:
        housing=HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("we are testing login module")

    logging.info("we are testing login module")
    return "Starting machin lerning project"


if __name__=="main":
    app.run(debug=True)
