from pymongo import MongoClient

client = MongoClient()
test_obj = {'a': 'abc', 'b': 'xyz', 'c': 'asd'}

def find_object(primary_key):
    '''Finds and returns an object matching the primary key.
    Returns None if not found'
    '''
    my_object = my_collection.find_one({'b': 'xyz'})
    print(test_obj)

def update_object(new_object):
    '''Updates an object if it exxists, inserts if does not exists'''
    test_obj = my_collection.find_one({'a': 'abc'})
    if test_obj is None:
        raise ValueError('Not Found!')
    test_obj['details'].append({'type': 'mobile', 'data': '555-555-5432'})
    my_collection.update({'name': 'Contact Name'}, my_object)

def remove_object(primary_key):
    '''deletes the object mstching primary_key.
    returns True if deleted, False if not found'''
    del_result = my_collection.delete_one({'name': 'Contact Name'})
