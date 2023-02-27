# These statements, commonly used with reading and writing files. 
# A context manager is an object that is notified when a context (a block of code) starts and ends. You commonly use one with the with statement

# file objects are context managers
with open('Chapter-29/file1.txt', 'w') as fileobj:
    fileobj.write("\n I am Deepali Ghadia")
    
    
# creating your own context manager
# Has two magic methods => __enter__() and __exit__() method
class ContextManager():
    def __init__(self):
        print('init method called') # init method is called as soon as we create instance of a class and then other operations are performed
         
    def __enter__(self):
        print('enter method called')
        return self
     
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')
 
with ContextManager() as manager:
    print('with statement block')
    
    '''
    init method called
    enter method called
    with statement block
    exit method called
    '''