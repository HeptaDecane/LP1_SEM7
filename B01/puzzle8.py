goal = [['1' , '2' , '3'] , ['4' , '5' , '6'] , ['7' , '8' , '0']]

def get_pos(element):
    for row in range(len(goal)):
        if element in goal[row]:
            return row , goal[row].index(element)

class Node:
    def __init__(self , data , level):
        self.data = data
        self.level = level
        self.fval = self.calculate_heuristic() + self.level

    def calculate_heuristic(self):
        cost = 0
        for row in range(len(self.data)):
            for col in range(len(self.data)):
                r , c = get_pos(self.data[row][col])
                cost += abs(row - r) + abs(col - c)
        return cost

    def shuffle(self , x1 , y1 , x2 , y2):
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(self.data)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

    def copy(self , root):
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def find(self , x):
        for i in range(0 , len(self.data)):
            for j in range(0 , len(self.data)):
                if self.data[i][j] == x:
                    return i,j

    def generate_child(self):
        x,y = self.find('0')
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for i in val_list:
            child = self.shuffle(x , y , i[0] , i[1])
            if child is not None:
                child_node = Node(child , self.level+1)
                children.append(child_node)
        return children

    def is_equal(self , state):
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if self.data[i][j] != state.data[i][j]:
                    return False
        return True

    def set_min_cost(self, state):
        self.level = min(self.level, state.level)
        self.fval = min(self.fval, state.fval) 

    def get_cost(self):
        return str(self.fval)

    def print_node(self):
        for i in self.data:
            for j in i:
                print(j,end=" ")
            print("")


def propogate(j , open_list , closed_list):
    id = -1
    for k in closed_list[j].generate_child():
        if closed_list[j].fval < k.fval:
            k.set_min_cost(closed_list[j])
        for x in range(len(closed_list)):       
            if x.is_equal(k):
                id = x
                break
        if id != -1:
            propogate(k , open_list , closed_list)

def update_list(i , open_list , closed_list):
    id = -1
    for j in range(len(open_list)):             
        if(i.is_equal(open_list[j])):
            id = j
            break
    if id != -1:
        open_list[j].set_min_cost(i)
    else:
        for j in range(len(closed_list)):      
            if(i.is_equal(closed_list[j])):
                id = j
                break
            if(id != -1):
                if(i.fval < closed_list[j].fval):
                    closed_list[j].set_min_cost(i)
                    propogate(j , open_list , closed_list)
            else:
                open_list.append(i)             

def print_list(lis):
    for i in lis:
        i.print_node()
    print('\n')

if __name__ == "__main__":
    print("Enter the start state matrix : ")
    start = []
    for i in range(0 , 3):
        temp = input().split(" ")
        start.append(temp)
    start_node = Node(start , 0)
    open_list = []
    closed_list = []
    open_list.append(start_node)

    while True:
        current_state = open_list[0]
        print("\nCurrent State : ")
        current_state.print_node()

        if current_state.calculate_heuristic() == 0:
            print("\n\nTotal Cost of sorting = " + current_state.get_cost())
            break

        closed_list.append(open_list[0])
        
        del open_list[0]
        
        for i in current_state.generate_child():
            update_list(i , open_list , closed_list)
        
        open_list.sort(key = lambda x:x.fval, reverse = False)