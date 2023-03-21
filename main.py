import arguments
import log

args = None

def do_something():
    log.debug('Debug print')
    log.info('Info print')
    print('sup')

def main():
    global args
    args = arguments.get()
    log.init()
    do_something()

if __name__ == '__main__':
    main()