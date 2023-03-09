from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


# used link below for Graph class, explained it very well
# https://www.section.io/engineering-education/dijkstra-python/ 


"""CA304 project by Jamie Clarke 18398783"""

#Input Descriptions 
#All Inputs are in Json format 
""""
AddRouter -
{
     'name' : 'A'
}
"""
"""
Connect - 
{
	"from":"A",
	"to":"B",
	"weight": 5
}
"""
"""
RemoveRouter - 
{
	"name": "A"
}
"""
"""
RemoveConnection - 
{
	"from":"A",
	"to":"B"
}
"""
"""
Route - 
{
	"from":"A",
	"to":"B"
}
"""

#Example of input/output 
"""
AddRouter - 
input -
{
     'name' : 'A'
}
output - 
{
	"status": "success"
}
or if error 
output - 
{
	"status": "Error, node already exists"
}
"""
"""
Connect -
input - 
{
	"from":"A",
	"to":"B",
	"weight": 5
}
output - 
{
	"status": "success"
}
or if connection already exists
output - 
{
	"status": "updated"
}
or if both routers do not exist 
output - 
{
	"status": "Error, router does not exist"
}
"""
"""
RemoveRouter - 
input - 
{
	"name": "A"
}
output -
{
	"status": "success"
} 
"""
"""
RemoveConnection -
input - 
{
	"from":"A",
	"to":"B"
}
output - 
{
	"status": "success"
} 
"""
"""
Route - 
input - 
{
	"from":"A",
	"to":"B"
}
output - 
{
	"status": "success"
}
"""

app = FastAPI()

class AddRouter(BaseModel):
    name : str
 
@app.post("/addrouter/")

def addrouter(name: AddRouter):
    my_graph = Graph()
    if name in my_graph.nodes:
        return "Error, node already exists"
    else:
        my_graph.add_node(name)
        return "status :" " success"



tags_metadata = [
    {
        "name" : "AddRouter",
        "description" : "A function to add a router to nodes[], takes input from User in form of 1 letter, then adds to my_graph.nodes"
    }
]



class RemoveRouter(BaseModel):
    name: str

@app.post("/removerouter/")

def removerouter(name: RemoveRouter):
    my_graph = Graph()
    if name in my_graph.nodes:
        my_graph.remove_node(name)
        return  "status :" " success"
    else:
        return "error, router has not been added"



tags_metadata = [
    {
        "name" : "RemoveRouter",
        "description" : "A function to remove a router from nodes[], takes input from User in form of 1 letter, then removes from my_graph.nodes"
    }
]

class RemoveConnection(BaseModel):
    From : str
    to : str

@app.post("/removeconnection/")
def removeconnection(name: RemoveConnection):
    my_graph = Graph()
    node1 = name.From
    node2 = name.to
    return my_graph.remove_edges(node1, node2)


tags_metadata = [
    {
        "name" : "RemoveConnection",
        "description" : "Removes the connection between two routers, only takes 2 parameters, the two routers names" 
    }
]


class Connect(BaseModel):
    From: str
    to: str
    weight: int



@app.post("/connect/")
def connect(name : Connect):
    my_graph = Graph()
    if name.From and name.to not in my_graph.edges:
        my_graph.add_edges(name)
        return "success"
    elif name.From or name.to in my_graph.edges:
       return "updated"
    else:
        return "Error, router does not exist"



tags_metadata = [
    {
        "name" : "Connect",
        "description" : "A function to connect two routers together, user must enter the 2 routers names, followed by the weight(cost between two routers)"
    }
]


class Route(BaseModel):
    From : str
    to : str
#not working 
@app.post("/route/")
def route(name: Route):
    Graph.minDistance(name.From, name.to)


tags_metadata = [
    {
        "name": "Route",
        "description": "Returns the shortest route between the two routers"
    }
]

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []


     #add nodes to nodes[]
    def add_node(self, name):
        if name in self.nodes:
            return -1
        
        elif name not in self.nodes:
            self.nodes.append(name)
            return 0

    #got help online for this 
    #remove nodes from nodes[]
    def remove_node(self, name):
        if name  in self.nodes:
            self.nodes.remove(name)
            return -1
        else:
            return 0

#function to add connection between two routers
    def add_edges(self ,From, to, weight):
        if(From not in self.edges) or (to not in self.edges):
            return {"status": "Error, router does not exist"}
        else:
            temp = []
            temp.append(From, to)
            if temp not in self.edges:
                self.edges.append(temp)
                return {"status": "success"}



#function to remove connection 
    def remove_edges(self, node1, node2):
        if node2 in self.Edge[node1]:
            self.Edge[node1].remove(node2)
            self.Edge[node2].remove(node1)
            return {"status": "success"}
            
    
#function for finding shortest distance, online help 
    def minDistance(self, distArray, vistSet):
        min = self.INF
        #unvisited nodes
        for v in range(self.V):
            if distArray[v] < min and vistSet[v] == False:
                min = distArray[v]
                min_index = v

        return min_index

