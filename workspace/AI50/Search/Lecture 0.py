"""
CS50 AI with Python: Search
LECTURE 0:

agent: entity that perceives its environment and acts upon that environment.
state: configuration of the agent in its environment.
initial state: state in which the agent begins. Starting point for search algorithm.
actions: choices that can be made in any given state.

Actions(s): returns the set of actions that can be executed in state s
transition model: a description of what state results from performing any applicable action in any state.
RESULT(s,a): returns the state resulting from performing action a in state s.

state space: the set of allŚ states reachable from the initial state by any sequence of models.
goal test: way to determine whether a given state is a goal state.
path cost: numerical cost associated with a given path. each path will be given a numeric cost.
           rather than finding a solution. find the least expensive cost.



Search Problem:
    initial state: state where we begin
    actions: action we can take.
    transition model: define what happens when we go from a state and one action to where we reach.
    goal test: know if we reached a goal.
    path cost function: by following a sequence of actions, what's the cost.

    optimal solution: solution that has the lowest path cost among all solutions.


node: data structure that keeps track of
        - a state
        - a parent (node that generated this node, parent of this node0
        - an action (action applied to parent to get node)
        - a path cost (from initial state to node)
frontier:  a set of paths available from a start node
expand node: consider possible actions from the state that node is representing. 

Approach
        1) Start with a frontier that contains initial state.
        2) Repeat:
            a) If the frontier is empty, then no solution.
            b) Remove a node from the frontier.
            c) if node contains goal state, return the solution.
            d) Expand node, add resulting nodes to the frontier

Revised Approach
        1) Start with a frontier that contains the initial state.
        2) Start with an empty explored set.
        3) Repeat:
            a) If the frontier is empty, then no solution.
            b) Remove a node from the frontier.
            c) if node contains goal state, return the solution.
            d) Add the node to the explored set
            e) Expand node, add resulting nodes to the frontier if they aren't already
               in the frontier or the explored set.

What order to remove elements:
DFS:
    Treat frontier like a STACK
    Stack: last in, first out. last thing added to frontier, first thing to remove from frontier
BFS:
    Treat frontier like a QUEUE
    Queue: first-in first-out data type. Earlier arrive in the frontier, earlier you get explored.

(DFS) Depth-First search: search algorithm that always expands the deepest node in the frontier.
(BFS) Breadth-First search: search algorithm tat always explores the shallowest node in the frontier.

"""

import sys


# TODO: learn about list[x:y]
# Frontier DFS 40:00
class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]


"""
52:00
How would you make your AI make smarter decisions

uninformed search: search strategy that uses no problem specific knowledge
informed search: search strategy that sues problem specific knowledge to find solutions more efficiently



(GBFS) greedy best-first search: 
    search algorithm that expands the node that is closest to the goal, as estimated by a heuristic function h(n)
        heuristic = estimate how close we are to goal
        h(n) = takes state of input and returns estimate of how close we are to the goal
            Manhattan distance = geographically how close we are to the goal, no walls.

A* search:
    search algorithm that expands node with lowest value of g(n)[cost to reach node] + h(n)[estimated cost to goal]
    optimal if:
        h(n) is admissible (never overestimates true cost)
        h(n) is consistent (for every node n and successor n' with step cost c, h(n)<=h(n') + c)



Search when another agent is actively deterring Agent from reaching goal

Minimax: -1,0,1
    Assign a value to state of winning/losing 
    MAX aims to maximize score
    MIN aims to minimize score

Game
    So: initial state
    PLAYER(s): returns which player to move in state s
    ACTIONS(s): returns legal move in state s
    RESULT(s,a): returns state after action a taken in state s
    TERMINAL(s): checks if state s is a terminal state
    UTILITY(s): final numerical value for terminal state s
    
Minimax
    Given a state s:
        MAX picks action a in ACTIONS(s) that produces highest value of MIN-VALUE(RESULT(s,a))
        MIN picks action a in ACTIONS(s) that produces smallest value of MAX-VALUE(RESULT(s,a))
        
        function MAX-VALUE(state):
            if TERMINAL(state):
                return UTILITY(state)
            v = -infinity
            for action in ACTIONS(state):
                v = MAX(v,MIN-VALUE(RESULT(state,action)))
            return v
        
        function MIN-VALUE(state):
            if TERMINAL(state):
                return UTILITY(state)
            v = +infinity
            for action in ACTIONS(state):
                v = MIN(v,MAX-VALUE(RESULT(state,action)))
            return v
    
    
Alpha-Beta Pruning
    Search efficiently if you remove nodes to optimize space. Makes searches efficient.

Depth-Limited Minimax
    After x number of moves, don't consider any more moves
    evaluation function: function that estimates the expected utility of the game form a given state
"""