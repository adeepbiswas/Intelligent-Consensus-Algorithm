import torch
from ICA import GE
from Blockchain import Transaction
from pandas import read_csv
from Nodes import Node
import time
from pandas import DataFrame


node_df = read_csv('nodesdata_n.csv')


def test(lower, counterl, timel, wh1, bh1, wh2, bh2, wout, bout, d):
    # Adding Nodes
    ge = GE()

    ge.d = d
    nodes = []
    blockchain = []
    nodeList = []

    for i in range(lower, lower+50):
        nodes.append('node' + str(i))

    for i in range(0, len(nodes)):
        node = nodes[i]
        globals()[node] = Node(node_df.iloc[i][0], node_df.iloc[i][1], node_df.iloc[i][2], node_df.iloc[i][3],
                               node_df.iloc[i][4],
                               node_df.iloc[i][5], node_df.iloc[i][6], i, blockchain)
        # print(node_df[i][0], node_df[i][1], node_df[i][2], node_df[i][3], node_df[i][4],
        #       node_df[i][5], node_df[i][6], i)
        globals()[node].addNodeToTheNetwork(nodeList, wh1, bh1, wh2, bh2, wout, bout, ge.d)
        wh1 = globals()[node].nnparams[0]  # 7x4
        bh1 = globals()[node].nnparams[1]  # 1x4
        wh2 = globals()[node].nnparams[2]  # 4x2
        bh2 = globals()[node].nnparams[3]  # 1x2
        wout = globals()[node].nnparams[4]  # 2x1
        bout = globals()[node].nnparams[5]  # 1x2

    # print("before Transacrtion initialization")
    # for i in range(0, len(nodeList)):
    #     print("node", i + 1, ":", nodeList[i].score)

    # Initiating Transaction
    ge.nodeList = nodeList
    start = time.time()
    ge.transactionInitialization()
    # print("node index list:", ge.nodeIndexList)
    # print("Small pool dict", ge.smallPoolDict)
    print("old difficulty:", ge.d)
    #
    ge.sortSmallPool()
    # print(ge.smallPool[0].id, ge.smallPool[0].score)

    # print("After Transacrtion initialization")
    # for i in range(0, len(nodeList)):
    #     print("node", i + 1, ":", nodeList[i].score)

    ge.difficultyUpdator()

    counter = 0

    while True:
        if len(ge.smallPool) < 0.1 * len(nodeList) or len(ge.smallPool) > 0.2 * len(nodeList):
            counter = counter + 1
            if ge.difficultyUpdator() == 0:
                break
            ge.selectSmallPool()
        else:
            break

    ge.sortSmallPool()
    print("Counter Value:", counter)

    print("new difficulty:", ge.d)
    counterl.append(counter)

    end = time.time()
    timetaken = end - start
    print("Time taken:", timetaken)
    timel.append(timetaken)

    return wh1, bh1, wh2, bh2, wout, bout, ge.d

    # for i in range(0, len(ge.smallPool)):
    #     print("small list node:", ":", ge.smallPool[i].score, "id:", ge.smallPool[i].id)

    #print("\nNode selected for mining the transaction:", ge.smallPool[0].id, "with score:", ge.smallPool[0].score)

    # transaction = Transaction(1, 0, 5000)
    # ge.smallPool[0].addToBlockchain(transaction)

    # print("\nTransaction added to blockchain")
    # print(blockchain)


wh1 = torch.ones(7, 4).type(torch.FloatTensor)  # 7x4
bh1 = torch.Tensor([0, 0, 0, 0])  # 1x4
wh2 = torch.ones(4, 2).type(torch.FloatTensor)  # 4x2
bh2 = torch.Tensor([0, 0])  # 1x2
wout = torch.ones(2, 1).type(torch.FloatTensor)  # 2x1
bout = torch.Tensor([0, 0])  # 1x2
d=0
lower = 0
counterl = []
timet = []

while lower + 50 < 1001:
    print("------------------------------")
    wh1, bh1, wh2, bh2, wout, bout, d = test(lower, counterl, timet, wh1, bh1, wh2, bh2, wout, bout, d)
    lower = lower + 50

counter_df = DataFrame(counterl)
time_df = DataFrame(timet)

counter_df.to_csv('countervalues.csv')
time_df.to_csv('time.csv')
