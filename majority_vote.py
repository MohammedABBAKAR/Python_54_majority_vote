
# todo Majority Vote
# ? Create a function that returns the majority vote in a list. A majority vote is an element that occurs > N/2 times in a list (where N is the length of the list).

#  ! Examples
#*  majority_vote(["A", "A", "B"]) ➞ "A"

# * majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"

# * majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None
# ! Notes
# ? The frequency of the majority element must be strictly greater than 1/2.
# ? If there is no majority element, return None.
# ? If the list is empty, return None.




def majority_vote(lst):
    item = 0
    if lst ==[]:
        return None
    # for x in lst:
    #     if x == "A":
    #         item += 1
    # return item
    lst2 = [x for x in lst if x== "A"]
    if len(lst2) > len(lst)//2:
        return "A"
print(majority_vote([]))
print(majority_vote(["A", "A", "B"]))
print(majority_vote(["A", "B", "B", "A", "C", "C"]))
print(majority_vote(["A", "A", "A", "B", "C", "A"]) )



# ! ////////////////////////////////////////////////////////////////////////


def majority_vote(lst):
    if not lst:
        return None  

    for item in set(lst):  
        if lst.count(item) > len(lst) // 2:  
            return item 

    return None  


print(majority_vote(["A", "A", "B"]))  
print(majority_vote(["A", "A", "A", "B", "C", "A"]))  
print(majority_vote(["A", "B", "B", "A", "C", "C"])) 
print(majority_vote([])) 
