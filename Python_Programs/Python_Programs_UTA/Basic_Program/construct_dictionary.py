
def construct_dictionary(names_list, ages_list, scores_list):
    dict = {}
    sample_list = []
    
    for i in range(0,len(names_list)):
        sample_list.append(ages_list[i])
        sample_list.append(scores_list[i])
        
        if scores_list[i] >= 60:
            sample_list.append("pass")
        else:
            sample_list.append("fail")

        dict[names_list[i]] = sample_list.copy()
        sample_list.clear()
        


    return dict    
            



names_list = ["paul", "saul", "steve", "chimpy"]
ages_list = [28, 59, 22, 5]
scores_list = [59, 85, 55, 60]

print(construct_dictionary(names_list,ages_list,scores_list))

"""

def create_dictionary_from_list_q5_sample(names, ages, scores):
    sample_dict = {}
    for index in range(0, len(names)):
        if scores[index] >= 60:
            sample_dict[names[index]] = [ages[index], scores[index], "pass"]
        else:
            sample_dict[names[index]] = [ages[index], scores[index], "fail"]

    return sample_dict

"""    
