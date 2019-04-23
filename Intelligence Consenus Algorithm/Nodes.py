from nativeNN import Neural
from ICA import GE
import torch
import hashlib


class Node:

    def __init__(self, cpr, ot, er, stake, wr, selec, extime, id, blockchain):
        self.cpr = cpr
        self.ot = ot
        self.er = er
        self.stake = stake
        self.wr = wr
        self.selec = selec
        self.extime = extime
        self.id = id
        self.neural = Neural(cpr, ot, er, stake, wr, selec, extime)
        self.nnparams = []
        self.othernodeparams = []
        self.score = 0.0000
        self.hash = ""
        self.blockchain = blockchain
        self.ge = GE()

    def addNodeToTheNetwork(self, nodeList, cwh1, cbh1, cwh2, cbh2, cwout, cbout, d):
        nodeList.append(self)
        if self.id == 0:
            self.nnparams = [cwh1, cbh1, cwh2, cbh2, cwout, cbout]
            self.broadcastReceiver(True)

            iwh1, ibh1, iwh2, ibh2, iwout, ibout = self.neural.nnInitializer()

            wh1, bh1, wh2, bh2, wout, bout, self.score = self.neural.nnTraining(iwh1, ibh1, iwh2, ibh2, iwout, ibout, d)

            self.nnparams = [wh1, bh1, wh2, bh2, wout, bout]
            self.ge.difficultyInitializer(self.score)

        else:
            wh1, bh1, wh2, bh2, wout, bout, self.score = self.neural.nnReceive(cwh1, cbh1, cwh2, cbh2, cwout, cbout, d)
            self.nnparams = [wh1, bh1, wh2, bh2, wout, bout]

    def broadcastSender(self, nodeList):
        for i in range(0, len(nodeList)):
            if i != self.id:
                nodeList[i].broadcastReceiver(True)

    def broadcastReceiver(self, isTransactionHappening):
        if isTransactionHappening:
            #X = torch.Tensor([[self.cpr, self.ot, self.er, self.stake, self.wr, self.selec, self.extime]])
            self.score, a, b = self.neural.forward(self.nnparams[0], self.nnparams[1], self.nnparams[2], self.nnparams[3],
                                                    self.nnparams[4], self.nnparams[5])


    def broadcastMembershipSender(self, nodeList, nodeParams, d):
        for i in range(0, len(nodeList)):
            if nodeList[i].score > d:
                nodeList[i].othernodeparams.append(nodeParams)

    def verifyScore(self, leaderNode):
        score = self.neural.verifyScore(leaderNode.cpr, leaderNode.ot, leaderNode.er, leaderNode.stake, leaderNode.wr, leaderNode.selec,
                                leaderNode.extime, self.nnparams[0], self.nnparams[1], self.nnparams[2], self.nnparams[3],
                                                    self.nnparams[4], self.nnparams[5])
        if score == leaderNode.score:
            return True
        else:
            return False

    def hashCreation(self):
        input = self.cpr + self.ot + self.er + self.stake + self.wr + self.selec + self.extime
        self.hash = hashlib.sha3_256(input.encode()).hexdigest()

    def verifyHash(self, leaderNode):
        input = leaderNode.cpr + leaderNode.ot + leaderNode.er + leaderNode.stake + leaderNode.wr + leaderNode.selec + leaderNode.extime
        hash = hashlib.sha3_256(input.encode()).hexdigest()
        if hash == leaderNode.hash:
            return True
        else:
            return False

    def getTransactionScore(self, wh1, bh1, wh2, bh2, wout, bout):
        #neuralq = Neural(self.cpr, self.ot, self.er, self.stake, self.wr, self.selec, self.extime)
        self.score = self.neural.generateScore(wh1, bh1, wh2, bh2, wout, bout)

    def addToBlockchain(self, transaction):
        self.blockchain.append(transaction)
