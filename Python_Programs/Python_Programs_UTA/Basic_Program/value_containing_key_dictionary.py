
def key_names(sample,number):
    output_list = []
    for keys in sample.keys():
        if number in sample[keys]:
            output_list.append(keys)
    output_list.sort()
    return output_list

sample = {"rabbit" : [1, 2, 3],
          "kitten" : [2, 2, 6],
          "lioness": [6, 8, 9]}

n = 2

print(key_names(sample,n))
            
        
