#task2
def observed():
    observations = list()
    for each_time in range(7):
        observedvalue= input("Please enter an observation: ")
        observations.append(observedvalue)
    return observations

def run():
    print("Counting observations...")
    observedList= observed()
    observed_set=set()
    for each_item in observedList:
        value_number= (each_item, observedList.count(each_item))
        observed_set.add(value_number)
    print(observed_set)

run()
