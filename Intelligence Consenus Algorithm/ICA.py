
import random
import collections
from Blockchain import Transaction
from Blockchain import Block
import operator


class GE:

    def __init__(self):
        self.nodeList = []
        self.d = 0.0000
        self.smallPool = []
        self.nodeIndexList = []
        self.smallPoolDict = {}



    def difficultyInitializer(self, score):
        self.d = score


    def difficultyUpdator(self):
        if len(self.smallPool) > 30:
            self.d = self.d + 0.05
        elif len(self.smallPool) < 2:
            self.d = self.d - 0.05
        else:
            return 0

    def transactionInitialization(self):

        lastNode = self.nodeList[len(self.nodeList) - 1]
        wh1 = lastNode.nnparams[0]  # 7x4
        bh1 = lastNode.nnparams[1]  # 1x4
        wh2 = lastNode.nnparams[2]  # 4x2
        bh2 = lastNode.nnparams[3]  # 1x2
        wout = lastNode.nnparams[4]  # 2x1
        bout = lastNode.nnparams[5]  # 1x2

        for i in range(0, len(self.nodeList)):
            self.nodeList[i].getTransactionScore(wh1, bh1, wh2, bh2, wout, bout)

        for i in range(0, len(self.nodeList)):
            if self.nodeList[i].score >= self.d:
                val = self.nodeList[i].score
                self.smallPoolDict[i] = val
                self.smallPool.append(self.nodeList[i])
                self.nodeList[i].selec += 1
                self.nodeIndexList.append(i)


    def sortSmallPool(self):
        for i in range(0, len(self.smallPool) - 1):
            if self.smallPool[i].score < self.smallPool[i+1].score:
                temp = self.smallPool[i]
                self.smallPool[i] = self.smallPool[i+1]
                self.smallPool[i + 1] = temp

    def verification(self):
        if len(self.smallPool) > 10:
            for i in range(1, 10):
                if self.smallPool[i].verifyScore(self.smallPoolDict[0]['node']) == False and\
                        self.smallPool[i].verifyHash(self.smallPoolDict[0]['node']) == False:
                    self.smallPool[i].er += 1
                    return False
                else:
                    return True

    def selectSmallPool(self):
        self.smallPool = []
        for i in range(0, len(self.nodeList)):
            if self.nodeList[i].score >= self.d:
                val = self.nodeList[i].score
                self.smallPoolDict[i] = val
                self.smallPool.append(self.nodeList[i])
                self.nodeList[i].selec += 1
                self.nodeIndexList.append(i)
