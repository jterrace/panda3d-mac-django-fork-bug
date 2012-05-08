import unittest
import os
import multiprocessing

def some_func(q):
    print 'child', os.getpid()
    
    from direct.showbase.ShowBase import ShowBase
    print 'imported'
    ShowBase()
    print 'aftershowbase'
    q.put(3)

class SimpleTest(unittest.TestCase):
    def test_something(self):
        
        q = multiprocessing.Queue()
        p = multiprocessing.Process(target=some_func, args=[q])
        p.start()
        print 'parent', os.getpid()
        dude = q.get()
        p.join()
        print 'dude', dude

if __name__ == '__main__':
    unittest.main()
