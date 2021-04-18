import processor


def scratch ():
    data = {"ab":5, "cd": {"x":5, "y":"2"}}
    path = "[\"cd\"] [\"y\"]"

    print (eval("data" + path))

    #print (data["cd"]["y"])













def tests():
  print ("rrr")

def main():
    scripts()

if __name__ == "__main__":
    scratch()
