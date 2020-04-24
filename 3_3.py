import multiprocessing
import time

def foo():
    print('starting function')
    time.sleep(0.1)
    print('finished function')

if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)
    print('process before execution:', p, p.is_alive())
    p.start()
    print('process running:', p, p.is_alive())
    p.terminate()
    print('process terminated:', p, p.is_alive())
    p.join()
    print('process joined:', p, p.is_alive())
    print('process exit code:', p.exitcode)


    