import numpy as np

class Node:
    def __init__(self, state, parent=None, action=None, depth=0, heuristic_cost=0, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth
        self.heuristic_cost = heuristic_cost
        self.cost = cost

        self.up = None
        self.down = None
        self.left = None
        self.right = None

    def try_move_up(self):
        blank_loc = [i[0] for i in np.where(self.state == 0)]
        i = blank_loc[0]
        j = blank_loc[1]
        if i == 0:
            return self.state
        upper_cell = self.state[i-1, j]
        new_sate = self.state.copy()
        new_sate[i, j] = upper_cell
        new_sate[i-1, j] = 0
        return new_sate

    def try_move_down(self):
        blank_loc = [i[0] for i in np.where(self.state == 0)]
        i = blank_loc[0]
        j = blank_loc[1]
        if i == 2:
            return self.state
        lower_cell = self.state[i+1, j]
        new_state = self.state.copy()
        new_state[i, j] = lower_cell
        new_state[i+1, j] = 0
        return new_state

    def try_move_left(self):
        blank_loc = [i[0] for i in np.where(self.state == 0)]
        i = blank_loc[0]
        j = blank_loc[1]
        if j == 0:
            return self.state
        left_cell = self.state[i, j-1]
        new_state = self.state.copy()
        new_state[i, j] = left_cell
        new_state[i, j-1] = 0
        return new_state

    def try_move_right(self):
        blank_loc = [i[0] for i in np.where(self.state == 0)]
        i = blank_loc[0]
        j = blank_loc[1]
        if j == 2:
            return self.state
        right_cell = self.state[i, j+1]
        new_state = self.state.copy()
        new_state[i, j] = right_cell
        new_state[i, j+1] = 0
        return new_state

    @staticmethod
    def get_heuristic_cost(current_state, goal_state):
        cost = np.sum(current_state != goal_state) - 1
        return max(cost, 0)

    def print_path(self):
        node = self
        path = []
        while node is not None:
            path.append(node)
            node = node.parent

        while path:
            node = path.pop()
            print('action:', node.action)
            print(node.state)
            print('f = {} + {} = {}\n'.format(node.depth, node.heuristic_cost, node.cost))

    def a_star_search(self, goal_state):
        self.heuristic_cost = Node.get_heuristic_cost(self.state, goal_state)
        self.cost = self.depth + self.heuristic_cost

        queue = [self]
        visited = set()

        while queue:
            queue = sorted(queue, key=lambda x: x.cost)
            current_node = queue.pop(0)
            visited.add(tuple(current_node.state.reshape(9)))

            if np.array_equal(current_node.state, goal_state):
                current_node.print_path()
                return True

            new_state = current_node.try_move_up()
            if tuple(new_state.reshape(9)) not in visited:
                depth = current_node.depth+1
                heuristic_cost = Node.get_heuristic_cost(new_state, goal_state)
                cost = depth + heuristic_cost
                current_node.up = Node(state=new_state, parent=current_node, action='UP', depth=depth, heuristic_cost=heuristic_cost, cost=cost)
                queue.append(current_node.up)

            new_state = current_node.try_move_down()
            if tuple(new_state.reshape(9)) not in visited:
                depth = current_node.depth+1
                heuristic_cost = Node.get_heuristic_cost(new_state, goal_state)
                cost = depth + heuristic_cost
                current_node.down = Node(state=new_state, parent=current_node, action='DOWN', depth=depth, heuristic_cost=heuristic_cost, cost=cost)
                queue.append(current_node.down)

            new_state = current_node.try_move_left()
            if tuple(new_state.reshape(9)) not in visited:
                depth = current_node.depth+1
                heuristic_cost = Node.get_heuristic_cost(new_state, goal_state)
                cost = depth + heuristic_cost
                current_node.left = Node(state=new_state, parent=current_node, action='LEFT', depth=depth, heuristic_cost=heuristic_cost, cost=cost)
                queue.append(current_node.left)

            new_state = current_node.try_move_right()
            if tuple(new_state.reshape(9)) not in visited:
                depth = current_node.depth+1
                heuristic_cost = Node.get_heuristic_cost(new_state, goal_state)
                cost = depth + heuristic_cost
                current_node.right = Node(state=new_state, parent=current_node, action='RIGHT', depth=depth, heuristic_cost=heuristic_cost, cost=cost)
                queue.append(current_node.right)


if __name__ == '__main__':
    state1 = np.array([1, 2, 3, 8, 6, 4, 7, 5, 0]).reshape(3, 3)
    state2 = np.array([1, 3, 4, 8, 6, 2, 7, 0, 5]).reshape(3, 3)
    state3 = np.array([2, 8, 1, 0, 4, 3, 7, 6, 5]).reshape(3, 3)
    goal_state = np.array([1, 2, 3, 8, 0, 4, 7, 6, 5]).reshape(3, 3)
    node = Node(state=state3)
    node.a_star_search(goal_state)
