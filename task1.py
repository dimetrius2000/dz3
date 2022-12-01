import functools
import time

def timer(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"{func.__name__} took {runtime:.4f} secs")
        return result
    return _wrapper

@timer
def create_list():
    newlist = []
    for x in range(100):
        newlist.append(x)
    print(newlist)
    return ('')
    
@timer
def create_dictionary():
    new_dict = {}
    for z in range(1, 100):
        new_dict[z-1] = z
    print(new_dict)
    return ('')



print(create_list())
print(create_dictionary())
print('------------------------------------------------------------------------------------------------------------------------------------')



@timer
def gettintfrom_list():
    newlist = [1,2,34,5,5]
    for i in range(len(newlist)):
        print(i)
    return ('')
    
@timer
def gettingfrom_dictionary():
    new_dict_2 = {0:1,1:2,2:3,2:4,5:5}
    for i in range(len(new_dict_2)):
        print(i)
    return ('')

print(gettintfrom_list())
print(gettingfrom_dictionary())
print('------------------------------------------------------------------------------------------------------------------------------------')



@timer
def deletefrom_list():
    newlist = [1,2,3,4,5]
    newlist[:] = [x for x in newlist if x & 1]
    print(newlist)
 
    return ('')
    
@timer
def deletefrom_dictionary():
    new_dict_3 = {0:1,1:2,2:3,3:4,4:5}
    delete = [key for key in new_dict_3 if key == 2]
    for key in delete:
        del new_dict_3[key]
    
    print(new_dict_3)
    return ('')

print(deletefrom_list())
print(deletefrom_dictionary())


