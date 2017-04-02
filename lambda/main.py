import logging, subprocess
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):    
  # return subprocess.check_output(['./dig', '@8.8.8.8', 'google.com'])
  logger.info(subprocess.check_output('cd bin && ./test1.sh', shell=True))
  return True
