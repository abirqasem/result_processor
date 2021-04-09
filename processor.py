import json
import typing
import requests


def dict_generator(indict, pre=None):
    '''
    Borrowed code from SO - for now this helps us build the data structure easily - # TODO: we will replace it with our
    code eventually. We do not want to store the final values of a JSON tree. This needs to be optimized
    '''
    pre = pre[:] if pre else []
    if isinstance(indict, dict):
        for key, value in indict.items():
            if isinstance(value, dict):
                for d in dict_generator(value, pre + [key]):
                    yield d
            elif isinstance(value, list) or isinstance(value, tuple):
                for v in value:
                    for d in dict_generator(v, pre + [key]):
                        yield d
            else:
                yield pre + [key, value]
    else:
        yield pre + [indict]



class ResultProcessor(object):
    """This object gets a JSON data and makes it super easy to query"""

    def __init__(self, ds:str, type:str):
        '''
        We can pass in a location of a data source that is a file or a url
        '''
        if type == "url":
            self.db =  list(dict_generator(requests.get(ds).json()))
        else:
            with open(ds, "r") as f:
                self.db = list(dict_generator(json.load (f)))
            f.close()

        self.keys = set ()
        for l in self.db:
            self.keys = self.keys| set(l[0:-1])

    def get_all_keys (self):
        return self.keys

    def get_depth (self,f:typing.Callable):
        return f ([len(l) for l in self.db])

    def get_size (self):
        return len(self.db)


    def isKey (self, item:str):
        '''
        True if the item is a key false otherwise.
        '''
        return

    def get_paths (self, key:str) -> list:
        '''
        If the item is not a key return None
        If the item is a key return a *list* of all paths that leads to the key

        A path is a list from root to the key.

        '''
        return


    def get_value (self, path:list) -> typing.Any:
        '''
        return the value if found or None

        '''




    



def main():

    rp = ResultProcessor ("explorer_test1.json", "file")
    #print (rp.db)
    print (rp.get_depth(max))
    print (rp.get_depth(min))
    #print (rp.get_items_at(0))
    print (rp.get_all_keys())


    return



if __name__ == "__main__":
    main()
