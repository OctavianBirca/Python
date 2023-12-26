class Container:
    is_empty = True
    value = None


def setContainerValue(class_name, value):
    class_name.value = value
    if class_name.value != None:
        class_name.is_empty = False
    return class_name.value, class_name.is_empty
    
def unsetContainerValue(class_name):
    if class_name.is_empty == False:
        class_name.value = None
        class_name.is_empty = True
        return class_name.value, class_name.is_empty
    
def printContainerValue(class_name):
    if class_name.is_empty == True:
        print ("The container is empty")
    elif class_name.is_empty == False:
        print("The value of the container is ", Container.value)

    
#####
# checks the container
printContainerValue(Container)

#sets a new value for the container
setContainerValue(Container, 123)

# checks the container
printContainerValue(Container)

# empts the container    
unsetContainerValue(Container)

# checks the container
printContainerValue(Container)


