class State:
    def __init__(self, tiles):
        """
        Parameters
        ----------
        tiles: 2d list
            A list of list of tiles.  All are numbers except for
            the blank, which is a " "
            Ex) [[2, 6, 1], [7, " ", 3], [5, 8, 4]]
        """
        self.tiles = tiles
        self.prev = None
    

    def __repr__(self):
        """
        Returns
        -------
        A printable string representation of the board
        """
        s = ""
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                s += "{} ".format(self.tiles[i][j])
            s += "\n"
        return s
    
    def __eq__(self, other):
        ret = True
        N = len(self.tiles)
        for i in range(N):
            for j in range(N):
                ret = ret and self.tiles[i][j] == other.tiles[i][j]
        return ret
    

    def __hash__(self):
        return hash(tuple([tuple(x) for x in self.tiles]))

    def __lt__(self, other):
        """
        Overload the less than operator so that ties can
        be broken automatically in a heap without crashing
        Parameters
        ----------
        other: State
            Another state
        
        Returns
        -------
        Result of < on string comparison of __str__ from self
        and other
        """
        return str(self) < str(other)
    
    def copy(self):
        """
        Return a deep copy of this state
        """
        tiles = []
        for i in range(len(self.tiles)):
            tiles.append([])
            for j in range(len(self.tiles[i])):
                tiles[i].append(self.tiles[i][j])
        return State(tiles)
    
    def is_goal(self):
        """
        Returns
        -------
        True if this is a goal state, False otherwise
        """
        res = True
        N = len(self.tiles)
        count = 1
        for i in range(N):
            for j in range(N):
                if count < N*N-1 and self.tiles[i][j] != count:
                    res = False
                count += 1
        return res

    def _find_blank(self):
        N = len(self.tiles)
        ret = (None, None)
        for i in range(N):
            for j in range(N):
                if self.tiles[i][j] == " ":
                    ret = (i, j)
        return ret

    def get_neighbs(self):
        """
        Get the neighboring states

        Returns
        -------
        list of State
            A list of the neighboring states
        """
        N = len(self.tiles)
        neighbs = []
        (i, j) = self._find_blank()
        for (i2, j2) in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]:
            if i2 >= 0 and j2 >= 0 and i2 < N and j2 < N:
                state = self.copy()
                state.tiles[i][j], state.tiles[i2][j2] = state.tiles[i2][j2], state.tiles[i][j]
                neighbs.append(state)
        return neighbs
    
    def solve(self):
        """
        Find a shortest path from this state to a goal state

        Returns
        -------
        list of State
            A path from this state to a goal state, where the first 
            element is this state and the last element is the goal
        """
        from linkedlist import DoublyLinkedList
        visited = set([])
        on_frontier = set([])
        frontier = DoublyLinkedList()
        finished = False
        frontier.add_last(self)
        # TODO: Fill this in
        
        solution = []
        return solution


state = State([[2, 8, 4], [5, " ", 7], [1, 3, 6]])
print(state)
"""
print(state)
print(state._find_blank())
for n in state.get_neighbs():
    print(n, n.is_goal(), "\n\n")
"""
    
state.solve()
