# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    "using stack from util.py"
    stack = util.Stack()
    "initializing closed set to save visited nodes"
    closed = set()
    "assigning the start state to x"
    x = problem.getStartState()
    "initializing the path to the goal"
    actions = []
    "pushing the start state & its path to the stack"
    stack.push((x, actions))

    "loop while stack is not empty"
    while stack.isEmpty() == False:
        "remove leftmost state X from open"
        x, actions = stack.pop()
        if problem.isGoalState(x):
            closed.add(x)
            print("The goal was found using DFS algorithm!")
            return actions
        else:
            "add node x on closed list"
            closed.add(x)
            "iterating over the children of the current node x to find successor, action and stepCost of the node x"
            for successor, action, stepCost in problem.getSuccessors(x):
                "if the node is not visited, push it to the stack and add its action to the path"
                if successor not in closed:
                    stack.push((successor, actions + [action]))
    "end"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    "using queue from util.py"
    queue = util.Queue()
    "initializing closed set to save visited nodes"
    closed = []
    "assigning the start state to x"
    x = problem.getStartState()
    "initializing the path to the goal"
    actions = []
    "pushing the start state & its path to the queue"
    queue.push((x, actions))

    "loop while queue is not empty"
    while queue.isEmpty() == False:
        "remove leftmost state X from open"
        x, actions = queue.pop()
        if problem.isGoalState(x):
            closed.append(x)
            print("The goal was found using BFS algorithm!")
            return actions
        else:
            "add node x on closed list"
            if x not in closed:
                closed.append(x)
                "iterating over the children of the current node x to find successor, action and stepCost of the node x"
                for successor, action, stepCost in problem.getSuccessors(x):
                    "if the node is not visited, push it to the queue and add its action to the path"
                    if successor not in closed:
                        queue.push((successor, actions + [action]))
    "end"

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    "using queue from util.py"
    pq = util.PriorityQueue()
    "initializing closed set to save visited nodes"
    closed = set()
    "assigning the start state to x"
    x = problem.getStartState()
    "initializing the path to the goal"
    actions = []
    "initializing start state cost"
    cost = 0
    "initializing priority"
    priority = 0
    "pushing the start state & its cost, path and priority to the pq"
    pq.push((x, cost, actions), priority)

    "loop while pq is not empty"
    while pq.isEmpty() == False:
        "remove leftmost state X from open"
        x, cost, actions = pq.pop()
        if problem.isGoalState(x):
            closed.add(x)
            print("The goal was found using UCS algorithm!")
            return actions
        else:
            "add node x on closed list"
            if not x in closed:
                closed.add(x)
                "iterating over the children of the current node x to find successor, action and stepCost of the node x"
                for (successor, action, stepCost) in problem.getSuccessors(x):
                    "if the node is not visited, push it to the pq, add its action to the path and add its cost to the total cost"
                    if successor not in closed:
                        pq.push((successor, stepCost + cost, actions + [action]), stepCost + cost)
    "end"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    "using queue from util.py"
    pq = util.PriorityQueue()
    "initializing closed set to save visited nodes"
    closed = []
    "assigning the start state to x"
    x = problem.getStartState()
    "initializing the path to the goal"
    actions = []
    "initializing start state cost"
    cost = 0
    "initializing priority, which is the cost and heuristic"
    priority = cost + heuristic(x, problem)
    "pushing the start state & its cost, path and priority to the pq"
    pq.push((x, cost, actions), priority)

    "loop while pq is not empty"
    while pq.isEmpty() == False:
        "remove leftmost state X from open"
        x, cost, actions = pq.pop()
        if problem.isGoalState(x):
            closed.append(x)
            print("The goal was found using A* algorithm!")
            return actions
        else:
            "add node x on closed list"
            if not x in closed:
                closed.append(x)
                "iterating over the children of the current node x to find successor, action and stepCost of the node x"
                for (successor, action, stepCost) in problem.getSuccessors(x):
                    "if the node is not visited, push it to the pq, add its action to the path and add its cost to the total cost"
                    if successor not in closed:
                        "the priority is the lowest cost + heuristic"
                        priority = stepCost + cost + heuristic(successor, problem)
                        pq.push((successor, stepCost + cost, actions + [action]), priority)
    "end"

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
