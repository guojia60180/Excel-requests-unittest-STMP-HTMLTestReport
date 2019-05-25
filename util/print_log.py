#Author guo
import logging
def initlogging(logFilename,e):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s-%(levelname)s-%(message)s',
        datefmt='%y-%m-%d %H:%M',
        filename=logFilename,
        filemode='a'
    )

    fh = logging.FileHandler(logFilename, encoding='utf-8')
    logging.getLogger().addHandler(fh)
    log = logging.exception(e)
    return log