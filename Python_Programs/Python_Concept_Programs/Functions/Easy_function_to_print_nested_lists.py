
names = [10,20,30,'rajesh','ramesh',['vizag','kakinada',[350,360],'Eluru']]

# to display nested list items using for loop is complex because it will have repeated code

# functions are used to reuse code

def print_nested(list_item):
    for each in list_item:
        if isinstance(each, list):
            print_nested(each)       #recursive function 
        else:
            print(each)    



print_nested(names)        