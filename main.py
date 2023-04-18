import logging

logging.basicConfig(
    level=logging.DEBUG,
    filemode='a',
    filename='./logs.txt',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
def main():
    """
    Main function
    """
    logger = logging.getLogger(__name__)
    logger.info('Logging OK')
    

if __name__ == '__main__':
    main()
