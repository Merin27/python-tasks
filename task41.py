

def sort_dicts(phones,model):
    return sorted(phones, key=lambda x:x[model])


phones=[{'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]


sorted_phones = sort_dicts(phones,'model')

print("Sorted list of dictionaries:",sorted_phones)
