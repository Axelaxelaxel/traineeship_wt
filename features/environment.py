import logging

logformat="%(levelname)s:%(filename)s:%(lineno)d:%(asctime)s:%(message)s"
logging.basicConfig(filename='./example.log',level=logging.DEBUG,format=logformat) 
def before_all(context):
  logging.info("Automated testing has started")

def before_step(context, step):
  logging.info("Step " + step.name + " has started")