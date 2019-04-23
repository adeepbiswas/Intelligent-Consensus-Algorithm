from Nodes import Node
import torch
from ICA import GE
from Blockchain import Transaction

ge = GE()

#Adding Nodes
blockchain = []
nodeList = []
wh1 = torch.ones(7, 4).type(torch.FloatTensor)#7x4
bh1 = torch.Tensor([0, 0 ,0, 0])#1x4
wh2 = torch.ones(4, 2).type(torch.FloatTensor)  # 4x2
bh2 = torch.Tensor([0, 0])  # 1x2
wout = torch.ones(2, 1).type(torch.FloatTensor) #2x1
bout = torch.Tensor([0, 0]) #1x2
ge.d = 50

node1 = Node(0.906, 24, 0, 20000, 0, 0, 11, 0, blockchain)
node1.addNodeToTheNetwork(nodeList, wh1, bh1, wh2, bh2, wout, bout, ge.d)
wh1 = node1.nnparams[0]#7x4
bh1 = node1.nnparams[1]#1x4
wh2 = node1.nnparams[2]# 4x2
bh2 = node1.nnparams[3]# 1x2
wout = node1.nnparams[4]#2x1
bout = node1.nnparams[5] #1x2
print("Node1 Training:", node1.score)

node2 = Node(0.989, 12, 0.9, 23089, 3, 0, 12, 1, blockchain)
node2.addNodeToTheNetwork(nodeList, wh1, bh1, wh2, bh2, wout, bout, ge.d)

wh1 = node2.nnparams[0]#7x4
bh1 = node2.nnparams[1]#1x4
wh2 = node2.nnparams[2]# 4x2
bh2 = node2.nnparams[3]# 1x2
wout = node2.nnparams[4]#2x1
bout = node2.nnparams[5] #1x2
print("Node2 Training:",node2.score)

node3 = Node(0.921, 12, 0.2, 60000, 2, 0, 10, 2, blockchain)
node3.addNodeToTheNetwork(nodeList, wh1, bh1, wh2,
                          bh2, wout, bout, ge.d)
print("Node3 Training:", node3.score)

wh1 = node3.nnparams[0]#7x4
bh1 = node3.nnparams[1]#1x4
wh2 = node3.nnparams[2]# 4x2
bh2 = node3.nnparams[3]# 1x2
wout = node3.nnparams[4]#2x1
bout = node3.nnparams[5] #1x2


node4 = Node(0.913, 10, 0.4, 30000, 1, 3, 13, 3, blockchain)
node4.addNodeToTheNetwork(nodeList, wh1, bh1, wh2,
                          bh2, wout, bout, ge.d)
print("Node4 Training:", node4.score)

wh1 = node4.nnparams[0]#7x4
bh1 = node4.nnparams[1]#1x4
wh2 = node4.nnparams[2]# 4x2
bh2 = node4.nnparams[3]# 1x2
wout = node4.nnparams[4]#2x1
bout = node4.nnparams[5] #1x2

node5 = Node(0.921, 14, 0.1, 3000, 2, 4, 14, 4, blockchain)
node5.addNodeToTheNetwork(nodeList, wh1, bh1, wh2,
                          bh2, wout, bout, ge.d)
print("Node5 Training:", node5.score)

node6 = Node(0.95, 15, 0, 50, 0, 0, 15, 5, blockchain)
node6.addNodeToTheNetwork(nodeList, wh1, bh1, wh2, bh2, wout, bout, ge.d)
wh1 = node6.nnparams[0]#7x4
bh1 = node6.nnparams[1]#1x4
wh2 = node6.nnparams[2]# 4x2
bh2 = node6.nnparams[3]# 1x2
wout = node6.nnparams[4]#2x1
bout = node6.nnparams[5] #1x2
print("Node6 Training:", node6.score)

node7 = Node(0.98, 16, 0, 20000, 0, 0, 12, 6, blockchain)
node7.addNodeToTheNetwork(nodeList, wh1, bh1, wh2, bh2, wout, bout, ge.d)
wh1 = node7.nnparams[0]#7x4
bh1 = node7.nnparams[1]#1x4
wh2 = node7.nnparams[2]# 4x2
bh2 = node7.nnparams[3]# 1x2
wout = node7.nnparams[4]#2x1
bout = node7.nnparams[5] #1x2
print("Node7 Training:", node7.score)

node8 = Node(0.4, 19, 3, 34000, 3, 0, 17, 7, blockchain)
node8.addNodeToTheNetwork(nodeList, wh1, bh1, wh2, bh2, wout, bout, ge.d)
wh1 = node8.nnparams[0]#7x4
bh1 = node8.nnparams[1]#1x4
wh2 = node8.nnparams[2]# 4x2
bh2 = node8.nnparams[3]# 1x2
wout = node8.nnparams[4]#2x1
bout = node8.nnparams[5] #1x2
print("Node8 Training:", node8.score)

node9 = Node(0.977, 18, 0, 28000, 0, 0, 10, 8, blockchain)
node9.addNodeToTheNetwork(nodeList, wh1, bh1, wh2, bh2, wout, bout, ge.d)
wh1 = node9.nnparams[0]#7x4
bh1 = node9.nnparams[1]#1x4
wh2 = node9.nnparams[2]# 4x2
bh2 = node9.nnparams[3]# 1x2
wout = node9.nnparams[4]#2x1
bout = node9.nnparams[5] #1x2
print("Node9 Training:", node9.score)

node10 = Node(0.942, 11, 0, 23406, 0, 0, 9, 9, blockchain)
node10.addNodeToTheNetwork(nodeList, wh1, bh1, wh2, bh2, wout, bout, ge.d)
wh1 = node10.nnparams[0]#7x4
bh1 = node10.nnparams[1]#1x4
wh2 = node10.nnparams[2]# 4x2
bh2 = node10.nnparams[3]# 1x2
wout = node10.nnparams[4]#2x1
bout = node10.nnparams[5] #1x2
print("Node10 Training:", node10.score)

#Initiating Transaction
ge.nodeList = nodeList
ge.transactionInitialization()
#print("node index list:", ge.nodeIndexList)
# print("Small pool dict", ge.smallPoolDict)
print("difficulty:", ge.d)
#
ge.sortSmallPool()
#print(ge.smallPool[0].id, ge.smallPool[0].score)

for i in range(0, len(nodeList)):
    print("node", i + 1, ":", nodeList[i].score)

ge.difficultyUpdator()

counter = 0

while True:
    if len(ge.smallPool) < 0.2*len(nodeList) or len(ge.smallPool) > 0.5*len(nodeList):
        counter = counter + 1
        ge.difficultyUpdator()
        ge.selectSmallPool()
    else:
        break


ge.sortSmallPool()
print("Counter Value:", counter)

print("new difficulty:", ge.d)

for i in range(0, len(ge.smallPool)):
    print("small list node:", ":", ge.smallPool[i].score, "id:", ge.smallPool[i].id)

print("\nNode selected for mining the transaction:", ge.smallPool[0].id, "with score:", ge.smallPool[0].score)

transaction = Transaction(1, 0, 5000)
ge.smallPool[0].addToBlockchain(transaction)

print("\nTransaction added to blockchain")
print(blockchain)