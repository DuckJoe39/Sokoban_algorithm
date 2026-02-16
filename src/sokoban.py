from search import Problem

#  __   __                  ____          _         _   _
#  \ \ / /__  _   _ _ __   / ___|___   __| | ___   | | | | ___ _ __ ___
#   \ V / _ \| | | | '__| | |   / _ \ / _` |/ _ \  | |_| |/ _ \ '__/ _ \
#    | | (_) | |_| | |    | |__| (_) | (_| |  __/  |  _  |  __/ | |  __/
#    |_|\___/ \__,_|_|     \____\___/ \__,_|\___|  |_| |_|\___|_|  \___|
class Sokoban(Problem):
    """
    A Sokoban problem instance for search algorithms.
    Come up with your own representation for the state.
    """

    def __init__(self, board):
        """
        Initializes the Sokoban problem.
        :param board: List of strings, each string represent a row of the game board
        """
        self.walls = set()
        self.goals = set()
        initial_boxes = set()
        initial_player = None

        for r, row in enumerate(board):
            for c, col in enumerate(row):
                if col == '%':
                    self.walls.add((r, c))
                elif col == '.':
                    self.goals.add((r, c))
                elif col == 'b':
                    initial_boxes.add((r, c))
                elif col == 'B':
                    initial_boxes.add((r, c))
                    self.goals.add((r, c))
                elif col == 'P':
                    initial_player = (r, c)
        
        initial_state = (initial_player, frozenset(initial_boxes))
        super().__init__(initial_state)

        # Remember to call the parent constructor with initial state
        # super().__init__(...)

    def actions(self, state):
        """Returns the list of valid actions from the current state."""
        player_pos, boxes = state
        r, c = player_pos
        actions = []
        directions = {
            'U': (-1, 0),
            'D': (1, 0),
            'L': (0, -1),
            'R': (0, 1)
        }
        for action, (dr, dc) in directions.items():
            new_r, new_c = r + dr, c + dc
            new_pos = (new_r, new_c)

            if new_pos in self.walls:
                continue

            if new_pos in boxes:
                beyond_r, beyond_c = new_r + dr, new_c + dc
                beyond_pos = (beyond_r, beyond_c)

                if beyond_pos in self.walls or beyond_pos in boxes:
                    continue

                actions.append(action)
            else:
                actions.append(action)

        return actions

    def result(self, state, action):
        """Returns the resulting state after applying the action."""
        player_pos, boxes = state
        r, c = player_pos
        dr, dc = 0, 0
        if action == 'U': dr, dc = -1, 0
        elif action == 'D': dr, dc = 1, 0
        elif action == 'L': dr, dc = 0, -1
        elif action == 'R': dr, dc = 0, 1
        new_player_pos = (r + dr, c + dc)
        new_boxes = set(boxes)

        if new_player_pos in boxes:
            new_boxes.remove(new_player_pos)
            beyond_pos = (new_player_pos[0] + dr, new_player_pos[1] + dc)
            new_boxes.add(beyond_pos)

        return (new_player_pos, frozenset(new_boxes))

    def is_goal(self, state):
        """Checks if all boxes are on goal positions."""
        _, boxes = state
        return boxes == self.goals

    def h(self, state):
        """Heuristic function for the problem. This should return a
        non-negative estimate of the cost to reach the goal from the
        given state."""

        _, boxes = state
        total_distance = 0

        for box in boxes:
            min_dist = float('inf')
            for goal in self.goals:
                dist = abs(box[0] - goal[0]) + abs(box[1] - goal[1])
                if dist < min_dist:
                    min_dist = dist
            total_distance += min_dist

        return total_distance
