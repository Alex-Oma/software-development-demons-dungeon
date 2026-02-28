from collections import deque


class Chaser:
    '''
    The `Chaser` class is responsible for implementing pathfinding logic for an enemy character in the game.
    It uses a breadth-first search (BFS) algorithm to find the shortest path from the enemy's current position
    to the player's position on the game map. The class constructs a graph representation of the game map,
    where each node corresponds to a walkable tile, and edges represent possible movements between tiles.
    The `find_path` method returns the next step for the enemy to take towards the player,
    while ensuring that it avoids obstacles and other enemies.
    '''
    def __init__(self, game):
        self.game = game
        # Initialize the graph representation of the game map
        self.graph = {}
        # Define possible movement directions (8 directions: up, down, left, right, and diagonals)
        self.ways = [-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [1, -1], [1, 1], [-1, 1]
        # Get the game level map to construct the graph
        self.map = game.map.get_game_level_map()
        # Construct the graph representation of the game map
        self.get_graph()

    def find_path(self, start, goal):
        '''
            This method finds the next step for the enemy to take towards the player using a breadth-first search algorithm.
            It takes the starting position of the enemy and the goal position (player's position) as input and returns the
            next step for the enemy to move towards the player. The method constructs a path from the goal back
            to the start by following the visited nodes, and returns the last step in the path, which is the next
            position for the enemy to move to. If there are no valid paths, it returns the starting position.
        :param start:
        :param goal:
        :return: next step for the enemy to move towards the player
        '''
        # Perform a breadth-first search to find the path from the start to the goal
        self.visited = self.breadth_first_search(start, goal, self.graph)
        path = [goal]
        step = self.visited.get(goal, start)

        # Construct the path from the goal back to the start by following the visited nodes
        while step and step != start:
            path.append(step)
            step = self.visited[step]

        # Return the last step in the path, which is the next position for the enemy to move to
        return path[-1]

    def breadth_first_search(self, start, goal, graph):
        '''
            This method implements the breadth-first search (BFS) algorithm to explore the graph and find the path
            from the start node to the goal node. It uses a queue to keep track of nodes to explore and a dictionary
            to keep track of visited nodes and their parents. The method iteratively explores neighboring nodes until
            it reaches the goal or exhausts all possibilities. It also ensures that it does not revisit nodes or
            move into positions occupied by other enemies.
        :param start:
        :param goal:
        :param graph:
        :return: a dictionary of visited nodes and their parents
        '''
        queue = deque([start])
        visited = {start: None}

        # Use a queue to explore the graph in a breadth-first manner
        while queue:
            # Pop the current node from the front of the queue
            cur_node = queue.popleft()
            # If the current node is the goal, we have found the path and can break out of the loop
            if cur_node == goal:
                break
            # Get the next nodes (neighbors) of the current node from the graph
            next_nodes = graph[cur_node]

            # Iterate through the next nodes and add them to the queue if they have not been visited and are not occupied by other enemies
            for next_node in next_nodes:
                # Check if the next node has not been visited and is not occupied by other enemies before adding it to the queue
                if next_node not in visited and next_node not in self.game.objects_manager.enemies_positions:
                    # Add the next node to the queue for further exploration
                    queue.append(next_node)
                    # Mark the next node as visited and store the current node as its parent for path reconstruction
                    visited[next_node] = cur_node

        # Return the dictionary of visited nodes and their parents, which can be used to reconstruct the path from the goal back to the start
        return visited

    def get_next_nodes(self, x, y):
        # This method generates the next possible nodes (positions) for the enemy to move to from the current position (x, y).
        # It checks the surrounding tiles based on the defined movement directions (self.ways) and returns a list of valid
        # next positions that are not walls (obstacles) and not occupied by other enemies.
        return [(x + dx, y + dy) for dx, dy in self.ways if (x + dx, y + dy) not in self.game.map.world_map]

    def get_graph(self):
        # This method constructs the graph representation of the game map by iterating through each tile in the map and
        # checking if it is walkable (not a wall). For each walkable tile, it adds an entry to the graph dictionary
        # with the tile's coordinates as the key and a list of adjacent walkable tiles (generated by get_next_nodes) as the value.
        # This graph is then used for pathfinding in the find_path method.
        for y, row in enumerate(self.map):
            for x, col in enumerate(row):
                if not col:
                    # For each walkable tile (where col is 0), add it to the graph with its adjacent walkable tiles
                    self.graph[(x, y)] = self.graph.get((x, y), []) + self.get_next_nodes(x, y)