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

    def __init__(self, ds:str, ds_type:str):
        '''
        We can pass in a location of a data source that is a file or a url
        '''
        if ds_type == "url":
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


    def is_key (self, item:str):
        '''
        True if the item is a key false otherwise.
        '''
        return item in self.keys


    def get_paths (self, key:str) -> list:
        '''
        If the item is not a key return None
        If the item is root return item
        If the item is a key and not root return the path
        return all the *unique*  paths
        A path is a list from root to the key.

        sample input: [['items', 'tags'], ['items', 'tags'], ['items', 'tags'], ['items', 'owner', 'reputation'], ['items', 'owner', 'link'], ['items', 'is_answered'], ['items', 'supin', 'tags']]
        ['items', 'owner', 'link', 'https://stackoverflow.com/users/4815264/james-mcdowell'], ['items', 'is_answered', False], ['has_more', True]]

        if key is "items" expected output is: items
        if the key is "is_answered" output is: [['items', 'is_answered']]
        if the key is "tags" output is: [['items', 'tags']]
        '''
        result = []

        #print(self.db)

        if key in self.get_all_keys():

            for item in self.db:
                #print (item)
                if key in item:
                    #print(item)
                    if item[0] == key:
                        return key
                    else:
                        #print(item)
                        index_item = item.index (key)
                        result.append(item[:index_item+1])
            return result[0]
        else:
            return "none"




    def get_value (self, path:list) -> typing.Any:
        '''
        return the value if found or None

        '''








def main():

    rp = ResultProcessor ("explorer_test2.json", "file")
    print (rp.db)
    #print (rp.get_depth(max)) #longest path from root to leaf
    #print (rp.get_depth(min))
    #print (rp.get_all_keys())
    #print(rp.is_key("display_name")) #True
    #print(rp.is_key("namez")) #False

    print(rp.get_paths("tags"))


    return



if __name__ == "__main__":
    main()
