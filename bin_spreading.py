def fill_container(container, object) :
    container.append(object)
    return container

def change_container(first, second, first_item) : 
    second.append(first_item)
    first.remove(first_item)

containers = [ [] 
             for x in range( 10 ) ] 
container_capacity = 10 

objects = [10, 4, 3, 3, 4, 10, 7, 5, 2, 1, 5, 1, 1, 1, 2, 7, 9, 1, 1, 3]

sorted_objects = sorted(objects, reverse=True)

full_containers = []
intermediate_containers = [[]]

# piste optimisation de l'algo 
while sorted_objects[0] == container_capacity : 
    fill_container(containers[0], sorted_objects[0])
    change_container(containers, full_containers, containers[0])
    sorted_objects.remove(sorted_objects[0])

# piste optimisation de l'algo 
while sorted_objects[0] >= container_capacity /2 : 
    fill_container(containers[0], sorted_objects[0])
    change_container(containers, intermediate_containers, containers[0])
    sorted_objects.remove(sorted_objects[0])

while containers : 
    change_container(containers, intermediate_containers, containers[0])
    intermediate_containers.sort()

intermediate_containers[0].append(0)

while sorted_objects : 
    fill_container(intermediate_containers[0], sorted_objects[0]) 
    intermediate_containers[0][0] = sum(intermediate_containers[0]) 
    # if intermediate_containers[0][1] : 
    #     intermediate_containers.remove(intermediate_containers[0][1])
    sorted_objects.remove(sorted_objects[0])
    intermediate_containers.sort()

intermediate_containers.sort(reverse=True)
containers = full_containers + intermediate_containers

print(containers)