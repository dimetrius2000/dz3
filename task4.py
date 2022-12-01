import hashlib
import uuid


cech_dict = {'https://vk.com/feed': 'f035d6ec3afc92d705faf7b30c14aac88aee0f442d5ced604771c809eee774f461e5d10e9760928adf2c422b06de652e27106e27968812d744c5e4ba790ac16f:e2e4b29cdadd4933af2fa60eedd132e3'}

url = (input("url:"))

def ceching_url(url):
        salt = uuid.uuid4().hex
        if url in cech_dict.keys():
                print('кеш найден:')
                print(cech_dict.values())
        else:
                print('кеш записан:')
                cech_dict[url] = hashlib.sha512(salt.encode() + url.encode()).hexdigest() + ':' + salt
                print(cech_dict)
                

ceching_url(url) 







 
