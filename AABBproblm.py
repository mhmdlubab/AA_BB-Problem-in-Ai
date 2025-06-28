from collections import deque # it's like a queue, we'll use it for BFS

# to add colors in the console using the print function
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m' # we need to do it in the end of the fstring to reset or the next print calls will be the last color we changed to text to

class node:
    def __init__(self, state, parent = None):
        self.state = state
        self.parent = parent

    # function to return True or False based on comparing the state(we called the function from) to a goal we feed to the function
    def goalTest(self, goal):
        if (self.state == goal):
            return True
        return False

    # function to return a list of all possible children for a state, and an empty state if there are no children
    def children(self):
        children = []
        emptySquareIndex = self.state.index('_') # to determine what are the valid moves
        # if the empty square is in the first place[index 0]
        if (emptySquareIndex == 0):
            children.extend(self.emptySquareIsFirst(self.state))
        # if the empty square is in the second place[index 1]
        if (emptySquareIndex == 1):
            children.extend(self.emptySquareIsSecond(self.state))
        # if the empty square is in the third place[index 2]
        if (emptySquareIndex == 2):
            children.extend(self.emptySquareIsThird(self.state))
        # if the empty square is in the forth place[index 3]
        if (emptySquareIndex == 3):
            children.extend(self.emptySquareIsForth(self.state))
        # if the empty square is in the fifth place[index 4]
        if (emptySquareIndex == 4):
            children.extend(self.emptySquareIsFifth(self.state))
        return children
    
    # function to generate children if the empty square is in the first place[index 0]
    def emptySquareIsFirst(self, myList):
        children = [] 
        newState = myList.copy() # we have to use copy or it will refrence the self.state itself
        if (newState[1] == 'B'):
            newState[0], newState[1] = newState[1], newState[0]
            child_node = node(newState, self)
            children.append(child_node)
        newState = myList.copy() # after we changed the newState we reset it back to mylist to check for other availasble moves
        if (newState[2] == 'B'): 
            newState[0], newState[2] = newState[2], newState[0]
            child_node = node(newState, self)
            children.append(child_node)
        return children
    
    # function to generate children if the empty square is in the second place[index 1]
    def emptySquareIsSecond(self, myList):
        children = [] 
        newState = myList.copy() # we have to use copy or it will refrence the self.state itself
        if (newState[0] == 'A'):
            newState[0], newState[1] = newState[1], newState[0]
            child_node = node(newState, self)
            children.append(child_node)
        newState = myList.copy() # after we changed the newState we reset it back to mylist to check for other availasble moves
        if (newState[2] == 'B'): 
            newState[1], newState[2] = newState[2], newState[1]
            child_node = node(newState, self)
            children.append(child_node)
        newState = myList.copy() # after we changed the newState we reset it back to mylist to check for other availasble moves
        if (newState[3] == 'B'): 
            newState[1], newState[3] = newState[3], newState[1]
            child_node = node(newState, self)
            children.append(child_node)
        return children
    
    # function to generate children if the empty square is in the third place[index 2]
    def emptySquareIsThird(self, myList):
        children = [] 
        newState = myList.copy() # we have to use copy or it will refrence the self.state itself
        if (newState[0] == 'A'):
            newState[0], newState[2] = newState[2], newState[0]
            child_node = node(newState, self)
            children.append(child_node)
        newState = myList.copy() # after we changed the newState we reset it back to mylist to check for other availasble moves
        if (newState[1] == 'A'): 
            newState[1], newState[2] = newState[2], newState[1]
            child_node = node(newState, self)
            children.append(child_node)
        newState = myList.copy() # after we changed the newState we reset it back to mylist to check for other availasble moves
        if (newState[3] == 'B'): 
            newState[2], newState[3] = newState[3], newState[2]
            child_node = node(newState, self)
            children.append(child_node)
        newState = myList.copy() # after we changed the newState we reset it back to mylist to check for other availasble moves
        if (newState[4] == 'B'): 
            newState[2], newState[4] = newState[4], newState[2]
            child_node = node(newState, self)
            children.append(child_node)
        return children
    
    # function to generate children if the empty square is in the forth place[index 3]
    def emptySquareIsForth(self, myList):
        children = [] 
        newState = myList.copy() # we have to use copy or it will refrence the self.state itself
        if (newState[1] == 'A'):
            newState[1], newState[3] = newState[3], newState[1]
            child_node = node(newState, self)
            children.append(child_node)
        newState = myList.copy() # after we changed the newState we reset it back to mylist to check for other availasble moves
        if (newState[2] == 'A'): 
            newState[2], newState[3] = newState[3], newState[2]
            child_node = node(newState, self)
            children.append(child_node)
        newState = myList.copy() # after we changed the newState we reset it back to mylist to check for other availasble moves
        if (newState[4] == 'B'): 
            newState[3], newState[4] = newState[4], newState[3]
            child_node = node(newState, self)
            children.append(child_node)
        return children
    
    # function to generate children if the empty square is in the fifth place[index 4]
    def emptySquareIsFifth(self, myList):
        children = [] 
        newState = myList.copy() # we have to use copy or it will refrence the self.state itself
        if (newState[2] == 'A'):
            newState[2], newState[4] = newState[4], newState[2]
            child_node = node(newState, self)
            children.append(child_node)
        newState = myList.copy() # after we changed the newState we reset it back to mylist to check for other availasble moves
        if (newState[3] == 'A'): 
            newState[3], newState[4] = newState[4], newState[3]
            child_node = node(newState, self)
            children.append(child_node)
        return children

def main():
    print("Hello, this code is used to transform a list from one state to another,\nthere are 2 As and 2 Bs and one empty slot(block) all the time, aka a list of 5 positions, \nvalid movees are:\n A moving to the right one block to swap with empty slot, or A jumping over one block also to the right to fill the empty slot\n B moving to the left one block to swap with empty slot, or B jumping over one block also to the left to fill the empty slot")

    startState = input("Enter your start state (use _ for empty square): ")
    while (len(startState) != 5 ):
        startState = input("Please enter all five positions: ")
    startState = startState.upper()

    goalState = input("Enter your goal state (use _ for empty square): ")
    while (len(goalState) != 5 ):
        goalState = input("Please enter all five positions: ")
    goalState = goalState.upper()

    print("Your Start State is:", startState)
    print("Your Goal State is:", goalState)

    # we change the inputs from strings to lists
    startState = list(startState)
    goalState = list(goalState)
    # set the initial state
    initialState = node(startState)

    # Breadth-First-Search(BFS):
    # define the variables for the search
    currentState = None
    openList = deque() # to create a queue
    openList.append(initialState) # to add initial state to the queue from the back
    closeList = []
    # the BFS iterations:
    while (openList): # while the openList is not empty
        currentState = openList.popleft()
        closeList.append(currentState) # add the currentState to the close list
        # check if the currentState is the goal
        if (currentState.goalTest(goalState)):
           break
        # get the children of the currentState
        children = currentState.children()
        # check whether there are children or not
        if (children): # if there are then add them to openList 
            for obj in children:
                if obj not in closeList and obj not in openList: # if they are not already in the close list or open list then add them to open list
                    openList.append(obj) # add from the back
    
    # to get the path to the solution(or to the last state if we got out of the loop bfore finding the solution, aka to get the path to a blocked state)
    solutionPath = deque()
    while(currentState.parent != None): # until we reach the initialState, aka the root, becuase it has no parent(parent = None)
        solutionPath.appendleft(currentState)
        currentState = currentState.parent
    solutionPath.appendleft(currentState) # add the root here becuase it won't be added in the loop above
    # to print the whole path
    for obj in solutionPath:
        print(obj.state)
    
    # to check if wee found the solution or the openlist became empty before we did, aka it's an impossible combination
    if (solutionPath.pop().goalTest(goalState)): # to pop the last one in the path, will be either the goal or a Blocked State
        print(f"{GREEN}Success, Goal Found!!!{RESET}")
    else:
        print(f"{RED}Fail, The above is a BLOCKED State, Goal Not Found!!!{RESET}")

main()