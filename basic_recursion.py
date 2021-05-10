import json


def is_simple (var):
    '''
    returns true if the variable is a simple data
    '''
    return isinstance(var, (float, int, str))




def get_children (node):
    '''
    gets the subscript if the node is a list, keys if it is a dictionary
    or an empty list if the node is a simple data type
    '''
    if isinstance(node, list):
        return list(range(0, len(node)))
    elif isinstance(node, dict):
        return list(node.keys())
    else:
        return []



def process (node):
    '''
    recursively process data
    '''

    # check if the node is simple if you are you are done for that branch
    if is_simple (node):
        print (node) # print it
        return node
    else:
        # the following code works for both list and dicts because we already wrote
        # a nice convienence method that will get us the children
        children = get_children(node)
        for child in children:
            # for each we process recursively
            process (child)

def process_with_yield (node):
    '''
    recursively process data
    '''

    # check if the node is simple if you are you are done for that branch
    if is_simple (node):
        yield node
    else:
        # the following code works for both list and dicts because we already wrote
        # a nice convienence method that will get us the children
        children = get_children(node)
        for child in children:
            # for each we process recursively
            yield process (child)




def main():
    fn = "/Users/abirqasem/lpa/inspector/test.json"
    file = open(fn, "r")
    data = json.load (file)
    process(data)
    print(list(process_with_yield(data)))

    file.close()



if __name__ == "__main__":
    main()
