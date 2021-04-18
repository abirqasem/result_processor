# result_processor


[AQ Blog on list comprehension](http://learnin60seconds.logdown.com/posts/6858469-manipulating-tabular-data-using-python-s-list-comprehension)



###Completion Tasks

1. We need to investigate why `get_all_keys ()` returns an empty set with our JSON data. It works fine with SO API results but produces an empty set when I feed it our JSON data. The issue is either our data is weird (_unlikely, but would be nice to check that out_) or the `dict_generator` code is buggy. This is the most likely cause. The code is a bit complex but a great way to learn `yield` and `recursion`. 
2. If we fix 1 above `get_paths` should work but we will have to test it
3. In `get_paths` currently we do `items->owner->reputation` but we should do `items[0]->owner->reputation` to `items[n]->owner->reputation` lists. This would be really helpful to `get_values(path)` function. 
4. AQ has a sketch of how `get_values` can be done please see in tests.py. Not happy with it but it will work for now I think.
5. While number 3 negates the need for removing duplicates from n dimnesional list the problem is a great coding assignment and perhaps a content into one of our *hard* topic courses. You should give it a try with my help. The intial problem defintion is as follows: (*it needs more refinement*)

>Given an n dimensional array of atomic elements remove all dupicate items. 

* An item_1 and item_2 are duplicate if 
  * `item_1` == item_2 if they are atomic.
  * `item_1` and `item_2` have identical elements in the same order. for example 

[1,2,[3,4]] is equal to [1,2,[3,4]] but not [1,2,[4,3]] 

You can see from this example the input/output has to be thought of very carefully.


