import multiprocessing

class Myprocess(multiprocessing.Process):
    def run(self):
        print('called run method in process: %s' %self.name)
        return 

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = Myprocess()
        jobs.append(p)
        p.start()
        p.join()


