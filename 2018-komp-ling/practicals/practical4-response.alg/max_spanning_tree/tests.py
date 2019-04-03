import unittest
import max_spanning_tree
import time


class max_spanning_tree_tests(unittest.TestCase):
    def test_heads(self):
        graph_matrix = [[0, 2, 4, 0, 5],
                        [4, 0, 3, 0, 5],
                        [7, 2, 0, 0, 0],
                        [0, 0, 4, 0, 5],
                        [0, 1, 0, 0, 0]]
        heads = max_spanning_tree.check_heads(graph_matrix)
        self.assertEqual(heads, [3])

        graph_matrix = [[0, 2, 4, 4, 5],
                        [4, 0, 3, 0, 5],
                        [7, 2, 0, 0, 0],
                        [0, 0, 4, 0, 5],
                        [0, 1, 0, 0, 0]]
        heads = max_spanning_tree.check_heads(graph_matrix)
        self.assertEqual(heads, [])

        graph_matrix = [[0, 2, 4, 0, 5],
                        [4, 0, 3, 0, 5],
                        [7, 2, 0, 0, 0],
                        [0, 0, 4, 6, 5],
                        [0, 1, 0, 0, 0]]
        heads = max_spanning_tree.check_heads(graph_matrix)
        self.assertEqual(heads, [3])

        graph_matrix = [[1, 2, 4, 0, 5],
                        [0, 0, 3, 0, 5],
                        [0, 2, 0, 0, 0],
                        [0, 0, 4, 0, 5],
                        [0, 1, 0, 0, 0]]
        heads = max_spanning_tree.check_heads(graph_matrix)
        self.assertEqual(heads, [0, 3])


    def test_check_connection(self):
        graph_matrix = [[0, 2, 4, 0, 5],
                        [4, 0, 3, 0, 0],
                        [0, 2, 0, 0, 0],
                        [0, 0, 4, 0, 5],
                        [0, 1, 0, 0, 0]]
        connection = max_spanning_tree.check_connection(graph_matrix, 0, 4, already_visited=[])
        self.assertEqual(connection, True)
        connection = max_spanning_tree.check_connection(graph_matrix, 0, 3, already_visited=[])
        self.assertEqual(connection, False)
        connection = max_spanning_tree.check_connection(graph_matrix, 2, 4, already_visited=[])
        self.assertEqual(connection, True)
        connection = max_spanning_tree.check_connection(graph_matrix, 2, 0, already_visited=[])
        self.assertEqual(connection, True)

    def test_tree(self):
        graph_matrix = [[0, 5, 5, 0, 0],
                        [0, 0, 0, 1, 0],
                        [0, 2, 0, 0, 1],
                        [0, 1, 0, 0, 2],
                        [0, 0, 1, 0, 0]]
        tree_matrix = [[0, 5, 5, 0, 0],
                       [0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 2],
                       [0, 0, 0, 0, 0]]
        tree = max_spanning_tree.find_max_spanning_tree(graph_matrix)
        self.assertEqual(tree, tree_matrix)

        graph_matrix = [[0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0],
                        [0, 2, 0, 0, 1],
                        [0, 1, 0, 0, 2],
                        [0, 0, 1, 0, 0]]
        tree_matrix = None
        tree = max_spanning_tree.find_max_spanning_tree(graph_matrix)
        self.assertEqual(tree, tree_matrix)

        graph_matrix = [[0, 5, 5, 0, 0],
                        [0, 0, 0, 1, 0],
                        [9, 2, 0, 0, 1],
                        [0, 1, 0, 0, 2],
                        [0, 0, 1, 0, 0]]
        tree_matrix = [[0, 5, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [9, 0, 0, 0, 0],
                       [0, 1, 0, 0, 2],
                       [0, 0, 1, 0, 0]]
        tree = max_spanning_tree.find_max_spanning_tree(graph_matrix)
        self.assertEqual(tree, tree_matrix)



if __name__ == '__main__':
    unittest.main()