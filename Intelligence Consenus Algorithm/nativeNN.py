## neural network in pytorch
import torch
import tensorflow as tf
#from globalenv import difficulty where this function returns the current difficulty value
from ICA import GE

class Neural:

    epoch = 1  # Setting training iterations
    lr = 0.1  # Setting learning rate
    inputlayer_neurons = 7  # X.shape[1]  # number of features in data set
    hiddenlayer1_neurons = 4  # number of hidden layers neurons
    hiddenlayer2_neurons = 2
    output_neurons = 1  # number of neurons at output layer

    def __init__(self, cpr, ot, er,stake, wr, selec, extime):
        self.cpr = 10*cpr
        self.ot = 7*ot
        self.er = -10*er
        self.stake = 4*stake
        self.wr = -4*wr
        self.selec = -1*selec
        self.extime = 7*(1/extime)
        self.d = 0.0000

        # Input array
        self.X = torch.Tensor([[cpr, ot, er, stake, wr, selec, extime]])

    # Output
    #y = torch.Tensor([[1], [1], [0]])
    #d = difficulty()


    # Sigmoid Function
    def sigmoid(self, x):
        return 1 / (1 + torch.exp(-1*x))


    # Derivative of Sigmoid Function
    def derivatives_sigmoid(self, x):
        return (torch.exp(-1*x))/((torch.exp(-1*x) + 1)**2)
        #return x * (1 - x)

    # def indentity(self, x):
    #     return x
    #
    # def derivative_indentity(self, x):
    #     return x/x
    #
    # def prerelu(self, x):
    #     print("original x:", x)
    #     x = x.numpy()
    #     print("old x:", x)
    #     x = self.lr * x
    #     print("new x", x)
    #     return torch.Tensor(x)
    #
    # def dervative_prerelu(self, x):
    #     return self.lr


    def nnInitializer(self):
        # Variable initialization


        # weight and bias initialization
        wh1 = torch.rand(self.inputlayer_neurons, self.hiddenlayer1_neurons).type(torch.FloatTensor)#7x4
        bh1 = torch.rand(1, self.hiddenlayer1_neurons).type(torch.FloatTensor)#1x4
        wh2 = torch.rand(self.hiddenlayer1_neurons, self.hiddenlayer2_neurons).type(torch.FloatTensor)  # 4x2
        bh2 = torch.rand(1, self.hiddenlayer2_neurons).type(torch.FloatTensor)  # 1x2
        wout = torch.rand(self.hiddenlayer2_neurons, self.output_neurons) #2x1
        bout = torch.rand(1, self.output_neurons) #1x2

        return wh1, bh1, wh2, bh2, wout, bout

    def nnTraining(self, wh1, bh1, wh2, bh2, wout, bout, d):
        output, hidden_layer_activations1, hidden_layer_activations2 = self.forward(wh1, bh1, wh2, bh2, wout, bout)
        wh1, bh1, wh2, bh2, wout, bout, score = self.backward(output, hidden_layer_activations1, hidden_layer_activations2,
                                                       wh1, bh1, wh2, bh2, wout, bout, d)
        return wh1, bh1, wh2, bh2, wout, bout, score

    def generateScore(self, wh1, bh1, wh2, bh2, wout, bout):
        output, hidden_layer_activations1, hidden_layer_activations2 = self.forward(wh1, bh1, wh2, bh2, wout, bout)
        #print(wh1, bh1, wh2, bh2, wout, bout)
        #print(self.X)
        return output.item()

    def forward(self, wh1, bh1, wh2, bh2, wout, bout):
        hidden_layer_input1 = torch.mm(self.X, wh1)
        # print("------------------------------------------------------------------------")
        # print("X", self.X)
        # print("wh1", wh1)
        # print("hidden_layer_input1", hidden_layer_input1)

        hidden_layer_input2 = hidden_layer_input1 + bh1
        #print("hidden_layer_input2", hidden_layer_input2)

        # to_be_divided = torch.Tensor([1000000, 1000000, 1000000, 1000000])
        # hidden_layer_input2 = hidden_layer_input2/to_be_divided
        #print("hidden_layer_input2 divided", hidden_layer_input2)

        #hidden_layer_activations1 = self.sigmoid(hidden_layer_input2)
        hidden_layer_activations1 = hidden_layer_input2

        #print("hidden_layer_activations1", hidden_layer_activations1)

        hidden_layer_input3 = torch.mm(hidden_layer_activations1, wh2)
        #print("hidden_layer_input3", hidden_layer_input3)

        hidden_layer_input4 = hidden_layer_input3 + bh2
        #print("hidden_layer_input4", hidden_layer_input4)

        #hidden_layer_activations2 = self.sigmoid(hidden_layer_input4)
        hidden_layer_activations2 = hidden_layer_input4

        #print("hidden_layer_activations2", hidden_layer_activations2)


        output_layer_input1 = torch.mm(hidden_layer_activations2, wout)
        #print("output_layer_input1", output_layer_input1)

        output_layer_input = output_layer_input1 + bout
        #print("output_layer_input", output_layer_input)
        #output = self.sigmoid(output_layer_input)
        output = output_layer_input

        return output, hidden_layer_activations1, hidden_layer_activations2


    def backward(self, output, hidden_layer_activations1, hidden_layer_activations2, wh1, bh1, wh2, bh2, wout, bout, d):
        # Backpropagation
        E = 1
        if (output <= (d + 10)) and (output >= (d - 10)):
            E = 1
        else:
            if output > (d + 10):
                E = (output - (d + 10)) + 1
            elif output < (d - 10):
                E = ((d - 10) - output) + 1

        # slope_output_layer = self.derivatives_sigmoid(output)
        # slope_hidden_layer1 = self.derivatives_sigmoid(hidden_layer_activations1)
        # slope_hidden_layer2 = self.derivatives_sigmoid(hidden_layer_activations2)

        slope_output_layer = self.derivatives_sigmoid(output)
        slope_hidden_layer1 = self.derivatives_sigmoid(hidden_layer_activations1)
        slope_hidden_layer2 = self.derivatives_sigmoid(hidden_layer_activations2)

        #print(slope_hidden_layer1)

    #reshaping it to 2x2
        abc = tf.reshape(slope_hidden_layer1, [2, 2])
        #print("new", tf.Session().run(abc))

        d_output = E * slope_output_layer
        Error_at_hidden_layer = torch.mm(d_output, wout.t())

        #print(Error_at_hidden_layer)

        #d_hiddenlayer1 = Error_at_hidden_layer * slope_hidden_layer1
        #arg = tf.convert_to_tensor(tf.Session().run(abc), dtype=tf.float32)
        #print(arg)
        qwe = torch.Tensor(tf.Session().run(abc))
        #print(qwe)
        d_hiddenlayer1 = Error_at_hidden_layer * qwe
        d_hiddenlayer2 = Error_at_hidden_layer * slope_hidden_layer2

    #reshaping it 1x4
        bcd = tf.reshape(d_hiddenlayer1, [1, 4])
        qwe = torch.Tensor(tf.Session().run(bcd))
        wouto = torch.mm(hidden_layer_activations2.t(), d_output) * self.lr + wout
        bouto = d_output.sum() * self.lr + bout
    #   wh1 += torch.mm(self.X.t(), d_hiddenlayer1) * self.lr
        wh1o = torch.mm(self.X.t(), qwe) * self.lr + wh1
        bh1o = d_output.sum() * self.lr + bh1
        wh2o = torch.mm(hidden_layer_activations1.t(), d_hiddenlayer2) * self.lr + wh2
        bh2o = d_output.sum() * self.lr + bh2

        #print('actual :\n', d, '\n')
        #print('predicted :\n', output.item())
        #print("Parameters:", (d_output.sum()).item())

        return wh1o, bh1o, wh2o, bh2o, wouto, bouto, output.item()


    def nnReceive(self, wh1, bh1, wh2, bh2, wout, bout, d):
        nwh1, nbh1, nwh2, nbh2, nwout, nbout, score = self.nnTraining(wh1, bh1, wh2, bh2, wout, bout, d)
        #print("receive:", wh1, bh1, wh2, bh2, wout, bout)
        return nwh1, nbh1, nwh2, nbh2, nwout, nbout, score

    def verifyScore(self, cpr, ot, er, stake, wr, selec, extime, wh1, bh1, wh2, bh2, wout, bout):
        X = torch.Tensor([[cpr, ot, er, stake, wr, selec, extime]])
        score, a, b = self.forward(wh1, bh1, wh2, bh2, wout, bout)
        return score




