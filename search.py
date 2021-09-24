# search.py
# Place the starting point in the stack# ---------
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

    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))

# Remember that a search node must contain not only a state but also the information necessary to reconstruct the path (plan) which gets to that state.

#Important note: All of your search functions need to return a list of actions that will lead the agent from the start to the goal. These actions all have to be legal moves (valid directions, no moving through walls).

#Important note: Make sure to use the Stack, Queue and PriorityQueue data structures .

#Algorithms for DFS, BFS, UCS, and A* differ only in the details of how the fringe is managed. 

   
    exploredNode = [] # Keeps record of explored nodes
    ListOfActions = [] # Here we store the actions
    myStack = util.Stack() # We search from the last node DFS 
    myStack.push((problem.getStartState(), ListOfActions)) #place the starting node onto the stack along with the list of actions 
    while myStack:
        currentNode, actions = myStack.pop()  # current position and the actions 
        if not currentNode in exploredNode:  #Check if currentNode has been visited
            if problem.isGoalState(currentNode):# The search is done
                return actions
            exploredNode.append(currentNode)                    
            for successor in problem.getSuccessors(currentNode):        
                location, action, stepCost= successor # lets get the successor info 
                updateActions = actions + [action]  # move towards the new node 
                myStack.push((location, updateActions)) # place new node onto the stack with updated list of actions  
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    exploredNode = [] # Keeps record of explored nodes
    ListOfActions = [] # Here we store the actions
    myQueue = util.Queue() # We search from the first node BFS 
    myQueue.push((problem.getStartState(), ListOfActions)) #place the starting node onto the stack along with the list of actions 
    while myQueue:
        currentNode, actions = myQueue.pop()  # current position and the actions 
        if not currentNode in exploredNode:  #Check if currentNode has been visited
            if problem.isGoalState(currentNode):# The search is done
                return actions
            exploredNode.append(currentNode)
            for successor in problem.getSuccessors(currentNode):
                location, action, stepCost= successor # lets get the successor info 
                updateActions = actions + [action]  # move towards the new node 
                myQueue.push((location, updateActions)) # place new node onto the stack with updated list of actions  
    return []


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    exploredNode = [] # Keeps record of explored nodes
    ListOfActions = [] # Here we store the actions
    myQueue = util.PriorityQueue() #  
    myQueue.push((problem.getStartState(), ListOfActions), problem) #place the starting node onto the stack along with the list of actions 
    while myQueue:
        currentNode, actions = myQueue.pop()  # current position and the actions 
        if not currentNode in exploredNode:  #Check if currentNode has been visited
            if problem.isGoalState(currentNode):# The search is done
                return actions
            exploredNode.append(currentNode)
            for successor in problem.getSuccessors(currentNode):
                location, action, stepCost= successor # lets get the successor info 
                updateActions = actions + [action]  # move towards the new node 
                cost = problem.getCostOfActions(updateActions)   
                myQueue.push((location, updateActions), cost) # place new node onto the stack with updated list of actions  
    return []

#    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
   
    exploredNode = [] # Keeps record of explored nodes
    ListOfActions = [] # Here we store the actions
    myQueue = util.PriorityQueue() #  
    myQueue.push((problem.getStartState(), ListOfActions), heuristic(problem.getStartState(), problem)) # 
    while myQueue:
        currentNode, actions = myQueue.pop()  # current position and the actions 
        if not currentNode in exploredNode:  #Check if currentNode has been visited
            if problem.isGoalState(currentNode):# The search is done
                return actions
            exploredNode.append(currentNode)
            for successor in problem.getSuccessors(currentNode):
                location, action, stepCost= successor # lets get the successor info 
                updateActions = actions + [action]  # move towards the new node 
                cost = problem.getCostOfActions(updateActions) + heuristic(location, problem)
                myQueue.push((location, updateActions), cost) # place new node onto the stack with updated list of actions  
    return []
#    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
