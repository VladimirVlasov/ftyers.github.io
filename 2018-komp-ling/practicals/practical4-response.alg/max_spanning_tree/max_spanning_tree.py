# Kruskal's algorithm
import copy

# input is graph_matrix - list of lists like:
# [[0, 2, 4, 1, 5], [4, 0, 3, 6, 5], [7, 2, 0, 0, 0], [0, 0, 4, 0, 5], [0, 1, 0, 1, 0]]
def check_heads(graph_matrix):
    heads = []
    for node in range(len(graph_matrix)):
        is_head = True
        for current_node, current_node_connections in enumerate(graph_matrix):
            if not current_node == node:
                if current_node_connections[node] != 0 :
                    is_head = False
        if is_head:
            heads.append(node)
    return heads


def find_tree_weight(graph_matrix):
    return sum([sum(connections) for connections in graph_matrix])


def find_max_spanning_tree(graph_matrix):
    heads = check_heads(graph_matrix)
    if len(heads) >= 2:
        print('Too many heads')
        return None
    elif len(heads) == 1:
        return find_max_spanning_tree_for_head(graph_matrix, heads[0])
    else:
        max_weight = 0
        for node in range(len(graph_matrix)):
            graph_matrix_copy = copy.deepcopy(graph_matrix)
            curr_tree = find_max_spanning_tree_for_head(graph_matrix_copy, node)
            if curr_tree is not None:
                curr_weight = find_tree_weight(curr_tree)
                if curr_weight > max_weight:
                    max_tree = curr_tree
                    max_weight = curr_weight
        return max_tree


def check_connection(graph_matrix, source_node, dest_node, already_visited=[], debug=False):
    already_visited.append(source_node)
    if graph_matrix[source_node][dest_node] > 0:
        return True
    else:
        for node in range(len(graph_matrix)):
            if node not in already_visited and graph_matrix[source_node][node] > 0:
                if debug:
                    print('Ask for {} and {} connection'.format(node, dest_node))
                    print('{} are already visited'.format(already_visited))
                curr_connection = check_connection(graph_matrix, node,
                                                   dest_node, already_visited)
                if curr_connection:
                    return True
        return False


def find_max_spanning_tree_for_head(graph_matrix, head):
    for i in range(len(graph_matrix)):
        graph_matrix[i][head] = 0
    tree_matrix = [[0 for i in range(len(graph_matrix))] for j in range(len(graph_matrix))]
    is_connected = False
    while not is_connected:

        max_connection = max([max(connections) for connections in graph_matrix])
        if max_connection == 0:
            return None
        for i in range(len(graph_matrix)):
            for j in range(len(graph_matrix)):
                if graph_matrix[i][j] == max_connection:
                    is_connected_to_head = check_connection(tree_matrix, head, j, already_visited=[])
                    creates_cycle = check_connection(tree_matrix, j, i, already_visited=[])
                    i_and_j_connected = check_connection(tree_matrix, i, j, already_visited=[])
                    if (not is_connected_to_head) and (not creates_cycle) and (not i_and_j_connected):
                        tree_matrix[i][j] = max_connection
                    graph_matrix[i][j] = 0
        is_connected = True
        for node in range(len(graph_matrix)):
            if node != head:
                if not check_connection(tree_matrix, head, node, already_visited=[]):
                    is_connected = False
                    #print('{} is not connected'.format(node))
                    break

    return tree_matrix


if __name__ == '__main__':
    graph_matrix = []
    nodes_count = int(input())
    for _ in range(nodes_count):
        graph_matrix.append([int(num) for num in input().split()])
    result = find_max_spanning_tree(graph_matrix)
    if result is not None:
        for line in result:
            print(' '.join([str(num) for num in line]))
