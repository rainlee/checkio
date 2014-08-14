from collections import deque
def check_connection(network, first, second):
    networks = list(network)
     
    # BFS
    queue = deque([])
    queue.append(first)
     
    while len(queue) != 0:
        first = queue.popleft()
        #print(first)
 
        for friends in networks:
            robots = friends.split('-')
            if first in robots:
                other = robots[0] if robots[1] == first else robots[1]
                if other == second:  # found
                    return True;
                else:
                    queue.append(other)
                    networks.remove(friends)
             
    return False