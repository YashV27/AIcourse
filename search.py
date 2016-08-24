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

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    #print "what?:",problem.getSuccessors((5,5))
    "Two solutions- first using stack and second using priority queue"
    "first,using stacks. This method avoids log(n) overhead associated with priority queues"
    
    
    " Goal state =  problem.goal"

    start=[(problem.getStartState(),'',0)]
    fringe=util.Stack()
    cldset=set([])
    soln=[]
    
    if (problem.__str__() == "CornersProblem"):
        start=[(problem.getStartState(),'',0,list(problem.corners))]

    fringe.push(start)
    while(fringe.isEmpty()==False):
        node = fringe.pop()
        #lastnode = node[-1]
        currentPos = node[-1][0]
        goalCheck = node[-1][0]
        setparm = node[-1][0]

        if (problem.__str__() == "CornersProblem"):
            goalCheck = node[-1]
            setparm = (currentPos,tuple(node[-1][3]))

        if problem.isGoalState(goalCheck):
            soln=node
            break
        if setparm not in cldset:
            child_nodes=problem.getSuccessors(currentPos)
            cldset.add(setparm)
            for cn in child_nodes:
                if (problem.__str__() == "CornersProblem"):
                    cnv = [x for x in node[-1][3] if x!=cn[0]]
                    cn=(cn[0],cn[1],cn[2],cnv)

                arr=node+[cn]
                fringe.push(arr)
    else:
        return 'failure'
    
    solnarr=[soln[i][1] for i in range(1,len(soln))]
    return solnarr
    
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    start=[(problem.getStartState(),'',0)]
    fringe=util.Queue()
    cldset=set([])
    soln=[]

    if (problem.__str__() == "CornersProblem"):
        start=[(problem.getStartState(),'',0,list(problem.corners))]

    fringe.push(start)
    while(fringe.isEmpty()==False):
        node = fringe.pop()
        #lastnode = node[-1]
        currentPos = node[-1][0]
        goalCheck = node[-1][0]
        setparm = node[-1][0]
    
        if (problem.__str__() == "CornersProblem"):
            goalCheck = node[-1]
            setparm = (currentPos,tuple(node[-1][3]))

        if problem.isGoalState(goalCheck):
            soln=node
            break
        if setparm not in cldset:
            child_nodes=problem.getSuccessors(currentPos)
            cldset.add(setparm)
            for cn in child_nodes:
                if (problem.__str__() == "CornersProblem"):
                    cnv = [x for x in node[-1][3] if x!=cn[0]]
                    cn=(cn[0],cn[1],cn[2],cnv)

                arr=node+[cn]
                fringe.push(arr)
    else:
        return 'failure'

    solnarr=[soln[i][1] for i in range(1,len(soln))]
    return solnarr
    #return []

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    start=[(problem.getStartState(),'',0)]
    fringe=util.PriorityQueue()
    cldset=set([])
    soln=[]
    if (problem.__str__() == "CornersProblem"):
        start=[(problem.getStartState(),'',0,list(problem.corners))]

    fringe.push(start,0)
    while(fringe.isEmpty()==False):
        (node,cost) = fringe.prpop()
        #lastnode = node[-1]
        currentPos = node[-1][0]
        goalCheck = node[-1][0]
        setparm = node[-1][0]
        
        if (problem.__str__() == "CornersProblem"):
            goalCheck = node[-1]
            setparm = (currentPos,tuple(node[-1][3]))

        if problem.isGoalState(goalCheck):
            soln=node
            break
        if setparm not in cldset:
            child_nodes=problem.getSuccessors(currentPos)
            cldset.add(setparm)
            
            for cn in child_nodes:
                if (problem.__str__() == "CornersProblem"):
                    cnv = [x for x in node[-1][3] if x!=cn[0]]
                    cn=(cn[0],cn[1],cn[2],cnv)
                
                arr=node+[cn]
                cncost=cn[2]
                fringe.push(arr,cost+cncost)
    else:
        return 'failure'
        
    solnarr=[soln[i][1] for i in range(1,len(soln))]
    return solnarr

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
    start=[(problem.getStartState(),'',0)]
    heuristicvar = start[0][0]
    fringe=util.PriorityQueue()
    cldset=set([])
    soln=[]

    if (problem.__str__() == "CornersProblem"):
        start=[(problem.getStartState(),'',0,list(problem.corners))]
        heuristicvar = start[0]

    hn=heuristic(heuristicvar,problem)
    gn=0
    fn=gn+hn
    fringe.push(start,fn)

    while(fringe.isEmpty()==False):
        (node,fn) = fringe.prpop()
        heuristicvar = node[-1][0]
        #lastnode = node[-1]
        currentPos = node[-1][0]
        goalCheck = node[-1][0]
        setparm = node[-1][0]

        if (problem.__str__() == "CornersProblem"):
            goalCheck = node[-1]
            heuristicvar = node[-1]
            setparm = (currentPos,tuple(node[-1][3]))
        
        hn = heuristic(heuristicvar,problem)
        if problem.isGoalState(goalCheck):
            soln=node
            break

        if setparm not in cldset:
            child_nodes=problem.getSuccessors(currentPos)
            cldset.add(setparm)

            for cn in child_nodes:
                cnheuristicvar = cn[0]

                if (problem.__str__() == "CornersProblem"):
                    cnv = [x for x in node[-1][3] if x!=cn[0]]
                    cn=(cn[0],cn[1],cn[2],cnv)
                    cnheuristicvar = cn

                arr=node+[cn]
                cnhn=heuristic(cnheuristicvar,problem)
                cngn=cn[2]
                cnfn=cnhn+cngn
                fringe.push(arr,fn+cnfn-hn)
        
    else: 
        return 'failure'

    solnarr=[soln[i][1] for i in range(1,len(soln))]
    return solnarr


    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
