"""
*** Has Deadlock ***
--------------------
Note: Try to solve this task in O(m + n) or O(n) time, where n is a number of vertices and m is a number of edges, since this is what you'll be asked to do during an interview.
In a multithreaded environment, it's possible that different processes will need to use the same resource. A wait-for graph represents the different processes as nodes in a directed graph, where an edge from node i to node j means that the node j is using a resource that node i needs to use (and cannot use until node j releases it).
We are interested in whether or not this digraph has any cycles in it. If it does, it is possible for the system to get into a state where no process can complete.
We will represent the processes by integers 0, ...., n - 1. We represent the edges using a two-dimensional list connections. If j is in the list connections[i], then there is a directed edge from process i to process j.
Write a function that returns True if connections describes a graph with a directed cycle, or False otherwise.
Example
For connections = [[1], [2], [3, 4], [4], [0]], the output should be
hasDeadlock(connections) = true.
This graph contains a cycle.
For connections = [[1, 2, 3], [2, 3], [3], []], the output should be
hasDeadlock(connections) = false.
"""
# connections = [[1], [2], [3, 4], [4], [0]]
def hasDeadlock(connections):
# print(hasDeadlock(connections))
    # find out if the graph has a cycle
    # helper function to see if a nodes children are visited 
    def are_children_visited(vert):
        # print(connections[vert])
        for i in range(len(connections[vert])):
            if connections[vert][i] in visited:
                return True
                # print('yes in visited **********')
            else:
                return False
    # iterating the WHOLE array
    for i in range(len(connections)):
        # keep track of visited verts
        visited = []
        q = []
        # creating a new q every iteration with the current index 
        q.append(i)
        # while there is a vert in the q
        while q:
            cur = q.pop(0)
            # print('current after pop', cur)
            # add the current vert to visited
            visited.append(cur)
            # print('visited after append', visited)
            # iterate the current verts neighbors
            for i in range(len(connections[cur])):
                neighbor = connections[cur][i]
                # print('neighbor just created', neighbor)
                # check if any neighbors OR their neighbors are already in 
                # visited
                # if they are in visited return True there IS a cycle
                if neighbor in visited:
                    if are_children_visited(neighbor):
                        return True
                    # print('neighbor in visited', neighbor)
                    # print('visited', visited)
                # else add the neigbor to the q if not already in the q
                else:
                    if neighbor not in q:
                        q.append(neighbor)
                        # print('q appended neighbor', q)
    # return False if we find no cycle
    return False

