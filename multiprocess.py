import multiprocessing

def spawn(num):
    print('Spawned', num)


if __name__ == '__main__':
    for i in range(50):
        p = multiprocessing.Process(target=spawn, args=(i,))
        p.start()
        p.join()
