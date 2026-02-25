# C1w4_deep Neural Network

📊 **Progress:** `20` Notes | `99` Screenshots

---

<a id="node-381"></a>
## Deep L-layer Neural Network

<br>


<a id="node-382"></a>
### 1 By the fourth week of the course, students have learned about forward propagation and

> [!NOTE]
> 1 By the fourth week of the course, students have learned about forward propagation and
> back propagation in the context of a neural network, as well as logistic regression,
> vectorization, and the importance of random weight initialization.
>
> 2 With this foundational knowledge, the focus of the fourth week is on putting these ideas
> together to implement a deep neural network.
>
> 3 A deep neural network is a neural network with multiple hidden layers, as opposed to a
> shallow model like logistic regression, which is a one-layer neural network.  4 The number
> of hidden layers in a neural network is a matter of degree and can vary depending on the
> problem at hand. While there is no easy way to predict the ideal depth for a network, it is
> common to try different values and evaluate their performance on a development set or
> across validation data.
>
> 5 Notation is used to describe the architecture and activations of deep neural networks.
> Specifically, L denotes the number of layers, and N superscript [l] denotes the number of
> nodes in layer l. a[l] denotes the activations in layer l, and W[l] and b[l] are used to
> compute the value of z[l] in layer l.
>
> 6 x represents the input features, as well as the activations of layer zero, while a[L]
> represents the predicted output or y-hat of the neural network.
>
> 7 The course website provides a notation sheet or guide that students can refer to if they
> forget what a particular symbol or term means.
>
> 8 In the next video, the course will go into more detail about what forward propagation
> looks like in a deep neural network.

<br>

  <a id="node-383"></a>
  <p align="center"><kbd><img src="assets/7074fd67924abe7337db9908e6e9df02949a8d6c.png" width="100%"></kbd></p>
  <br>


<a id="node-384"></a>
## Forward Propagation In Deep Network

<br>


<a id="node-385"></a>
### 1 The video discusses the process of forward propagation in a deep L-layer neural

> [!NOTE]
> 1 The video discusses the process of forward propagation in a deep L-layer neural
> network using a single training example, followed by the vectorized version, where
> forward propagation is carried out on the entire training set.
>
> 2 The activations for layer one are computed using the formula z1 = w1*x + b1 and a1
> = g(z1), where w1 and b1 are the parameters affecting the activations in layer one and
> g is the activation function for layer one.
>
> 3 The activations for subsequent layers are computed in a similar way, using the
> activation values from the previous layer, until the activations for the final layer, layer L,
> are computed, giving the estimated output y hat.
>
> 4 The forward propagation equation for a single training example is generalized as zl =
> wl*a(l-1) + bl, where a0 = x and a(l-1) is the activation value from the previous layer.
>
> 5 The vectorized version of forward propagation involves stacking the vectors z and a
> for all training examples and carrying out the same computations using matrix
> multiplication.
>
> 6 The video recommends using a for loop to compute activations for all layers in a deep
> neural network, as it is difficult to implement it without one.
>
> 7 Understanding matrix dimensions is crucial when implementing a deep neural
> network to minimize bugs and ensure correct implementation.

> [!NOTE]
> 1 In the previous video, the speaker explained what a deep L-layer neural network is and the notation used to describe it.
>  2 In this video, the focus is on performing forward propagation in a deep network for a single training example x, and later on for the entire training set.
>  3 For a single training example x, the activations for the first layer are computed by taking the dot product of the input vector x and the parameters w1 for layer one, and adding the bias vector b1. Then, the activation function g is applied to this value to obtain the activations for layer one. This process is repeated for each subsequent layer until the estimated output y hat is obtained.
>  4 The general rule for computing the activations for a layer l in a deep network is zl = wl * al-1 + bl, followed by al = g(zl), where al-1 is the activation of the previous layer.
>  5 To perform forward propagation for the entire training set, the training examples are stacked horizontally to form a matrix X. The same process for computing the activations for a single training example is then applied to the entire matrix, yielding a matrix of activations A for all layers in the network.
>  6 In this process, a For loop is used to compute the activations for each layer. While explicit For loops are generally avoided in neural network implementation, there is no way to implement forward propagation without a For loop in this case.
>  7 When implementing deep neural networks, it is important to be systematic and careful with matrix dimensions in order to increase the odds of a bug-free implementation. The speaker recommends taking the time to think through matrix dimensions carefully when debugging code.

<br>

  <a id="node-386"></a>
  <p align="center"><kbd><img src="assets/e306bf35e053bb1d81944fb44f004eb86738b0b8.png" width="100%"></kbd></p>
  > [!NOTE]
  > Vẫn phải for loop cho các l = 1-L. Không có cách nào khác.

  <br>


<a id="node-387"></a>
## Getting Your Matrix Dimension Rights

<br>


<a id="node-388"></a>
### 1 One debugging tool to check the correctness of deep neural network implementation

> [!NOTE]
> 1 One debugging tool to check the correctness of deep neural network implementation
> is to work through the dimensions of the matrices involved.
>
> 2 The dimensions of the weight matrix, W, is determined by the number of hidden units
> in the current and previous layer. The dimensions of the bias vector, B, is equal to the
> number of hidden units in the current layer.
>
> 3 The activation vector, Z, for each layer is a vector of dimension equal to the number of
> hidden units in that layer.
>
> 4 For input features, x, and activation vector, Z, to have the same dimension, the weight
> matrix, W, must have dimensions equal to the number of hidden units in the current
> layer by the number of features or hidden units in the previous layer.
>
> 5 In vectorized implementation, the dimensions of Z and X will change, but the
> dimensions of W and B will remain the same.
>
> 6 The dimensions of dw and db, the gradients of the weight and bias, respectively,
> should be the same as the dimensions of W and B.

> [!NOTE]
> 1 When implementing a deep neural network, one of the debugging tools often used to check the correctness of the code is to work through the dimensions of matrices being used.
>  2 The first step in forward propagation is to compute Z1, which is equal to W1 times the input features x plus b1, where n1 is the number of hidden units in the first hidden layer.
>  3 The dimensions of the matrix W1 must be n1 by n0, where n0 is the number of input features.
>  4 More generally, the dimensions of the weight matrix W for layer L must be nL by nL-1.
>  5 The dimensions of the bias vector b for layer L must be nL by 1.
>  6 When implementing backpropagation, the dimensions of dw (the gradient of the weight matrix) should be the same as the dimensions of the weight matrix W. Similarly, the dimensions of db (the gradient of the bias vector) should be the same as the dimensions of the bias vector b.
>  7 The dimensions of the activation vector a and the output vector z for a given layer L should be the same.
>  8 When working with multiple examples at a time, the dimensions of the input matrix X and the output matrix Z will change, but the dimensions of the weight matrix W and the bias vector b will remain the same.
>  9 The key is to check the dimensions of all matrices and vectors to make sure they match the requirements of the neural network architecture.

<br>

  <a id="node-389"></a>
  <p align="center"><kbd><img src="assets/167408accb1a84bffe5826adf8140ea634c4e321.png" width="100%"></kbd></p>
  <br>

  <a id="node-390"></a>
  <p align="center"><kbd><img src="assets/f747b1f12f7e552e3386ab371ad460c6637d2589.png" width="100%"></kbd></p>
  <br>


<a id="node-391"></a>
## Why Deep Representations?

<br>


<a id="node-392"></a>
### 1 Deep neural networks are effective for many problems and require a lot of

> [!NOTE]
> 1 Deep neural networks are effective for many problems and require a lot of
> hidden layers.
>
> 2 The first layer of a neural network is typically a feature detector or edge
> detector for images.
>
> 3 The neural network looks for simple things like edges and then composes
> them in later layers to learn more complex functions.
>
> 4 This simple-to-complex hierarchical representation applies to other types of
> data like speech recognition.
>
> 5 Deep neural networks can detect surprisingly complex things, like faces or
> phrases, despite computing seemingly simple functions.
>
> 6 The circuit theory suggests that deep neural networks can compute more
> functions than shallow networks.
>
> 7 Deep learning draws loose inspiration from the way the human brain detects
> simple things and builds them up into more complex objects.

> [!NOTE]
> 1 Deep neural networks work well because they can learn simple to complex hierarchical representations:
>  • The earlier layers of a neural network detect simple functions like edges, and later layers build more complex functions by composing the simpler ones together.
>  • This compositional representation applies to various types of data, not just images, and is especially useful in tasks like face recognition and speech recognition.
>  2 Deep neural networks are inspired by the human brain:
>  • The human brain starts off by detecting simple things like edges and then builds up to detect more complex objects.
>  • While analogies between deep learning and the human brain can be dangerous, there is some truth to this being how the human brain works.
>  3 Circuit theory provides intuition for why deep networks work well:
>  • Circuit theory is used to think about what types of functions can be computed with different logic gates, such as AND gates, OR gates, and NOT gates.
>  • Functions can be computed with a relatively small but deep neural network.
>  • If the same function is computed with a shallow network, it requires exponentially more hidden units to achieve the same level of performance as a deep network.

<br>

  <a id="node-393"></a>
  <p align="center"><kbd><img src="assets/472435e29276e7e1ac692c93832b7296d1f0ac73.png" width="100%"></kbd></p>
  <br>

  <a id="node-394"></a>
  <p align="center"><kbd><img src="assets/636e0510f5aa789b7813c408dce3e4f4b416f2b9.png" width="100%"></kbd></p>
  > [!NOTE]
  > Có nghĩa là với 1 simple L-layer network thì shallower network
  > phải có số hidden unit gấp nhiều lần theo cấp luỹ thừa thì mới
  > sánh bằng

  <br>


<a id="node-395"></a>
## Building Blocks Of Deep Neural Networks

<br>


<a id="node-396"></a>
### 1 Deep neural networks can be built by putting together the building blocks of

> [!NOTE]
> 1 Deep neural networks can be built by putting together the building blocks of
> forward propagation and backpropagation.
>
> 2 Each layer has parameters (weights and biases) that are used in the forward
> propagation step to compute activations of that layer and in the backward
> propagation step to compute derivatives with respect to the parameters and
> activations of the previous layer.
>
> 3 Forward propagation involves feeding input features through the network
> and computing activations for each layer using its parameters and activations
> from the previous layer. These activations are cached for later use in the
> backward propagation step.
>
> 4 Backward propagation involves computing derivatives with respect to the
> parameters and activations of each layer, starting from the output layer and
> going backwards to the input layer. These derivatives are used to update the
> parameters of the network in order to minimize a cost function.
>
> 5 Each iteration of training through a neural network involves one forward
> propagation step followed by one backward propagation step.

> [!NOTE]
> Sure, here is a more detailed summary of the video:
>  1 In the earlier videos from this week, as well as from the videos from the past several weeks, you've already seen the basic building blocks of forward propagation and backpropagation, the key components you need to implement a deep neural network.
>  2 To put these components together and build a deep neural network, you can start with a network of a few layers and pick one layer to focus on the computations for that layer.
>  3 For layer L, you have some parameters wl and bl, and for the forward propagation, you will input the activations al-1 from your previous layer and output al. You compute zl = wl * al-1 + bl, and then al = g(zl), where g is the activation function.
>  4 To store the value zl for later use in backpropagation, you can cache it as well.
>  5 For the backpropagation step, you need to implement a function that inputs da(l) and outputs da(l-1), given the derivatives with respect to these activations, and tells you how much do I wish al-1 changes the computed derivatives respect to activations from a previous layer.
>  6 Within this function, you need to use wl and bl, and it turns out along the way you end up computing dzl. This backward function can also output dwl and dbl, but you can use red arrows to denote the backward iteration.
>  7 If you can implement these two functions, then the basic computation of the neural network will be as follows: take the input features a0, feed that in, and compute the activations of the first layer, let's call that a1. Then you feed that to the second layer and using w2 and b2, you compute the activations in the next layer a2, and so on, until eventually, you end up outputting al which is equal to y hat.
>  8 Along the way, you cached all of these values z, so you can use them in backpropagation.
>  9 For the backpropagation step, you are going backwards and computing gradients by feeding in da(l) to compute da(l-1), and so on, until you get da(2) da(1). Along the way, backpropagation also outputs dwl, dbl, which are used to update the weights.
>  10 Inside the backward function, you will use the parameters wl and bl, and it turns out that you will end up computing the dz's as well.
>  11 One iteration of training through a neural network involves starting with a(0) which is x and going through forward propagation and backpropagation to update the weights

<br>

  <a id="node-397"></a>
  <p align="center"><kbd><img src="assets/21e28bf8a8fad54af96ba8ce55d0d1b3c2e58fbb.png" width="100%"></kbd></p>
  <br>

  <a id="node-398"></a>
  <p align="center"><kbd><img src="assets/b54491604283df45732352adfec9f05f29808f25.png" width="100%"></kbd></p>
  <br>


<a id="node-399"></a>
## Forward And Backward Propagation

<br>


<a id="node-400"></a>
### 1 Recap of the basic building blocks of implementing a deep neural network:

> [!NOTE]
> 1 Recap of the basic building blocks of implementing a deep neural network:
> forward propagation and backward propagation.
>
> 2 Forward propagation involves inputting a^l-1 and outputting a^l and the cache,
> z^l. The activation function is applied to z^l, and if a vectorized implementation is
> used, b is Python broadcasting and a^l is g applied element-wise to z.
>
> 3 The forward function is initialized with a^0, which is the input features for one
> training example or the input features for the entire training set.
>
> 4 Backward propagation involves inputting da^l and outputting da^l-1, dw^l, and
> db^l.
>
> 5 The equations for computing these derivatives are dz^l = da^l * g^l prime(z^l),
> dw^l = dz^l * a^l-1, db^l = dz^l, and da^l-1 = w^l transpose * dz^l.
>
> 6 A vectorized implementation of the backward function involves dz^l = da^l * g^l
> prime(z^l), dw^l = 1/m * dz^l * a^l-1 transpose, db^l = 1/m * np.sum(dz^l, axis=1,
> keepdims=True), and da^l-1 = w^l transpose * dz^l.
>
> 7 The output y-hat is used to compute the loss, which allows for backward
> iteration to compute the derivatives.
>
> 8 The backward recursion is initialized with da^l, which is equal to y/a + (1-y)/(1-a)
> for binary classification.
>
> 9 To implement forward propagation and backward propagation for a three-layer
> neural network, the input data x is initialized for the forward recursion and da^2
> and da^1 are passed backwards for the backward recursion.

> [!NOTE]
> Sure, here's a more detailed response with the main ideas indexed:
>  1 The basic building blocks of implementing a deep neural network are forward propagation and backward propagation steps for each layer.
>  2 Forward propagation takes the input a^l-1 and outputs a^l and cache z^l. To make function calls easier, w^l and b^l are cached as well. The equation for the forward function is w^l\/a^l-1+b^l, and a^l equals the activation function applied to z. A vectorized implementation is just w^l\/a^l-1+b, with b being a Python broadcasting, and a^l equals g applied element-wise to z.
>  3 The forward function is initialized by feeding a^0, which is equal to x, into the first function in the chain, and repeating this allows computation of forward propagation from left to right.
>  4 Backward propagation takes da^l as input and outputs da^l-1, dw^l, and db^l. The steps to compute these are as follows: Dz^l = da^l element-wise product with g(l)'(z(l)); dw^l = dz^l times a^l-1; db^l = dz^l; and da^l-1 = w^l transpose times dz^l. A vectorized implementation is dz^l = da^l element-wise product with g(l)'(z(l)), dw^l = 1/m times dz^l times a^l-1 transpose, db^l = 1/m times np.sum(dz^l, axis=1, keepdims=True), and da^l-1 = w^l transpose times dz^l.
>  5 The input x is passed through the layers with activation functions, and the output y-hat is used to compute the loss, which allows for backward iteration to compute the derivatives dW^3, db^3, dW^2, db^2, dW^1, db^1. The cache is also computed against z^1, z^2, and z^3, and da^2 and da^1 are passed backwards to compute da^0.
>  6 The forward recursion is initialized with the input data x, and the backward recursion uses the formula da of l = y / a + (1 - y) / (1 - a) for logistic regression in binary classification.

<br>

  <a id="node-401"></a>
  <p align="center"><kbd><img src="assets/5b5e2668fd08cff1299b350c6d9d6a27a952078f.png" width="100%"></kbd></p>
  <br>

  <a id="node-402"></a>
  <p align="center"><kbd><img src="assets/75eecb6505649b377195c45713c0d9309580bc43.png" width="100%"></kbd></p>
  <br>

  <a id="node-403"></a>
  <p align="center"><kbd><img src="assets/b25f8f9f7e312bea30ac482a947471860f4c639c.png" width="100%"></kbd></p>
  <br>

  <a id="node-404"></a>
  <p align="center"><kbd><img src="assets/82a3ee52157c20a5bb598d9db1782e0ef921c214.png" width="100%"></kbd></p>
  > [!NOTE]
  > Although I have to say, even today when I implement
  > a learning algorithm, sometimes even I'm surprised
  > when my learning algorithm implementation works
  > and it's because a lot of the complexity of machine
  > learning comes from the data rather than from the
  > lines of codes. Sometimes you feel like you
  > implement a few lines of code, not quite sure what it
  > did, but it almost magically works, and it's because a
  > lot of magic is actually not in the piece of code you
  > write which is often not too long

  <br>


<a id="node-405"></a>
## Parameters Vs Hyperparams

> [!NOTE]
> 1 Hyperparameters are important for developing effective deep neural networks:
>  2 When developing a deep neural network, it is not only important to organize the parameters such as W and B, but also the hyperparameters. Hyperparameters are the parameters that control the values of the actual parameters W and B.
>  3 Hyperparameters include learning rate, number of iterations, number of hidden layers, and activation function:
>  4 Some examples of hyperparameters include the learning rate alpha, which determines how the parameters W and B evolve, the number of iterations of gradient descent, the number of hidden layers (L), and the number of hidden units. Additionally, the choice of activation function, such as RELU, tangent, or sigmoid function, in the hidden layers is also a hyperparameter.
>  5 Empirical process of trying out different hyperparameter settings:
>  6 Finding the best values for hyperparameters is often an empirical process that involves trying out different hyperparameter settings and evaluating their impact on the cost function J. This may involve trying different values of alpha, the number of hidden layers, the number of hidden units, and so on. Based on the outcome, adjustments can be made until an optimal set of hyperparameters is found.
>  7 Deep learning involves many hyperparameters and is an empirical process:
>  8 Deep learning involves a large number of hyperparameters, which can make it a challenging process. To determine the optimal values of hyperparameters, it is often necessary to try out a range of values and iterate until the best combination is found. This process is often referred to as an empirical process, which means that a lot of trial and error is involved.
>  9 Intuition for hyperparameters may not carry over to different applications:
>  10 Researchers often work on a variety of applications within deep learning, and the intuition for hyperparameters may not always carry over from one application to another. It is often necessary to try out a range of values and evaluate their impact on the cost function J. Additionally, even within the same application, the optimal values of hyperparameters may change over time.

<br>


<a id="node-406"></a>
### 1 Developing deep Neural Nets requires organizing not only parameters, but

> [!NOTE]
> 1 Developing deep Neural Nets requires organizing not only parameters, but
> also hyper parameters.
>
> 2 Hyper parameters include the learning rate alpha, number of iterations,
> number of hidden layers, number of hidden units, activation function,
> momentum term, mini-batch size, and regularization parameters.
>
> 3 Hyper parameters control the ultimate parameters W and B.
>
> 4 Deep learning is an intricate process that involves trying out different hyper
> parameter settings.
>
> 5 Applying deep learning is an empirical process that involves trying out many
> different values and seeing what works.
>
> 6 There are systematic ways to try out a range of values for hyper parameters.
>
> 7 The best value for hyper parameters might change over time, even if working
> on the same problem.

<br>

  <a id="node-407"></a>
  <p align="center"><kbd><img src="assets/f850519d8c40e568e7af30c90a2d914d88371ed4.png" width="100%"></kbd></p>
  <br>

  <a id="node-408"></a>
  <p align="center"><kbd><img src="assets/edf0df0d5b1ca6865bfaa653907a133ac8e1ab68.png" width="100%"></kbd></p>
  > [!NOTE]
  > Empirical process: Đại khái là phải thử nhiều giá trị khác nhau của Hyper params

  > [!NOTE]
  > Different problem different choices for hyper params: 
  > Đại khái là khi apply qua 1 vấn đề mới thì nên lặp lại quá trình thử 
  > sai để chọn hyper params vì mỗi vấn đề mỗi khác.

  > [!NOTE]
  > Vài tháng check lại: 
  > Và dù đã chọn được hyper params tốt rồi thì vài tháng nên check lại
  > một lần vì sự thay đổi của CPU, GPU khiến mọi thứ thay đổi theo

  <br>


<a id="node-409"></a>
## Deep Learning & Brain

<br>


<a id="node-410"></a>
### The article discusses the loose analogy between deep learning and the

> [!NOTE]
> The article discusses the loose analogy between deep learning and the
> human brain. While the structure of a neural network may resemble a
> biological neuron, the complexity of a single neuron is far greater than
> what is currently understood. There is still much unknown about how the
> brain learns and whether it uses similar algorithms to backpropagation
> and gradient descent. The author notes that the analogy between deep
> learning and the brain may have been useful in the past, but as the field
> has progressed, it is breaking down. Finally, the author provides a
> summary of the video, which covers how to implement forward and
> backpropagation in deep neural networks.

<br>

  <a id="node-411"></a>
  <p align="center"><kbd><img src="assets/c15a221fbde3e37ebb2bb9657d3fbc93ecd69861.png" width="100%"></kbd></p>
  > [!NOTE]
  > Đại khái là nó giông giống neuron thôi chứ hiện giờ ngay cả
  > neuroscientist cũng chưa hiểu Neuron nó hoạt động, học như thế
  > nào

  <br>


<a id="node-412"></a>
## Quiz: Key Concepts On Deep Neural Network

<br>

<a id="node-413"></a>

<p align="center"><kbd><img src="assets/34c701b1cf135fe547bbd684778fd64b35618493.png" width="100%"></kbd></p>

<br>

<a id="node-414"></a>

<p align="center"><kbd><img src="assets/843dcbcafa58b86a9a5e6a3451f7b845c8625286.png" width="100%"></kbd></p>

<br>

<a id="node-415"></a>

<p align="center"><kbd><img src="assets/0f560ac7ff45ffafa606d6ae68461cc0706b2b3b.png" width="100%"></kbd></p>

<br>

<a id="node-416"></a>

<p align="center"><kbd><img src="assets/e9de2062157d00e2f46571826833c8220cb266e2.png" width="100%"></kbd></p>

> [!NOTE]
> Đánh nhầm

<br>

<a id="node-417"></a>

<p align="center"><kbd><img src="assets/33e9627279bad9308aa31e26f298e431d8fabcd4.png" width="100%"></kbd></p>

<br>

<a id="node-418"></a>

<p align="center"><kbd><img src="assets/7d9c9a38acc29f3d9422cce3bd7cd65c8dba31e7.png" width="100%"></kbd></p>

<br>

<a id="node-419"></a>

<p align="center"><kbd><img src="assets/45b849e69def279dfc7658d32b7a7b7958d4ddb4.png" width="100%"></kbd></p>

<br>

<a id="node-420"></a>

<p align="center"><kbd><img src="assets/a834123743ac7ce011dbe6de80b77b639e48302d.png" width="100%"></kbd></p>

<br>

<a id="node-421"></a>

<p align="center"><kbd><img src="assets/dedfa36e840936225b621db71d4697ce1977b4f7.png" width="100%"></kbd></p>

<br>

<a id="node-422"></a>

<p align="center"><kbd><img src="assets/68c9adea19cbb6598eda38590fadd77516dd37c0.png" width="100%"></kbd></p>

<br>

<a id="node-423"></a>

<p align="center"><kbd><img src="assets/08af278abddc26b18bde80cac6d55be6dc0d5c46.png" width="100%"></kbd></p>

<br>


<a id="node-424"></a>
## Programming Assignments: Build Your Deep Neural Network: Step By Step

<br>


<a id="node-425"></a>
### 1 - Packages

<br>

  <a id="node-426"></a>
  <p align="center"><kbd><img src="assets/55a6b0cf5e0f2a00f8f5470675f186312c881151.png" width="100%"></kbd></p>
  <br>

  <a id="node-427"></a>
  <p align="center"><kbd><img src="assets/f18592b6c9b9e2a3ae352f700389d5000157ac32.png" width="100%"></kbd></p>
  <br>


<a id="node-428"></a>
### 2 - Outline

<br>

  <a id="node-429"></a>
  <p align="center"><kbd><img src="assets/bc515481b06cce9435bab09942d3453362b554e4.png" width="100%"></kbd></p>
  <br>

  <a id="node-430"></a>
  <p align="center"><kbd><img src="assets/02b7a558243945d799c32ecfc43b4b6479f30baf.png" width="100%"></kbd></p>
  <br>

  <a id="node-431"></a>
  <p align="center"><kbd><img src="assets/7eb9c721925c0c73aefce95b777d9f644addf757.png" width="100%"></kbd></p>
  <br>


<a id="node-432"></a>
### 3 - Initialization

<br>

<a id="node-433"></a>
- 3.1 - 2-layer Neural Network
  <br>

    <a id="node-434"></a>
    <p align="center"><kbd><img src="assets/041ce5d3fcae18937a068d9b5cd99ea0022cd7d0.png" width="100%"></kbd></p>
    <br>

    <a id="node-435"></a>
    <p align="center"><kbd><img src="assets/d089d090884db6600a41df5f90f90c3da3b26526.png" width="100%"></kbd></p>
    <br>

    <a id="node-436"></a>
    <p align="center"><kbd><img src="assets/7349fc1fab0579069077ae5476bf7b2701f875b3.png" width="100%"></kbd></p>
    <br>

<a id="node-437"></a>
- 3.2 - L-layer Neural Network
  <br>

    <a id="node-438"></a>
    <p align="center"><kbd><img src="assets/5e1ad743a832f6dc84b225ebeb33cab64642fadd.png" width="100%"></kbd></p>
    <br>

    <a id="node-439"></a>
    <p align="center"><kbd><img src="assets/8a6f3cdbddfeb730b2c0bb7a038a571c29097ce4.png" width="100%"></kbd></p>
    <br>

    <a id="node-440"></a>
    <p align="center"><kbd><img src="assets/18bc9b6c283457a694dd4ced10c1b4c5f6c6c391.png" width="100%"></kbd></p>
    <br>

    <a id="node-441"></a>
    <p align="center"><kbd><img src="assets/3aaeebcd30f7089afcbdcafaf592a977a4ab7d57.png" width="100%"></kbd></p>
    <br>


<a id="node-442"></a>
### 4 - Forward Propagation Module

<br>

<a id="node-443"></a>
- 4.1 - Linear Forward
  <br>

    <a id="node-444"></a>
    <p align="center"><kbd><img src="assets/85681bf6535ba996a103476cd7c6430ca15b31f8.png" width="100%"></kbd></p>
    <br>

    <a id="node-445"></a>
    <p align="center"><kbd><img src="assets/2b949656638745e50094e891d9a35d791eb38b4b.png" width="100%"></kbd></p>
    <br>

    <a id="node-446"></a>
    <p align="center"><kbd><img src="assets/3633aa385f2fa94e04b0866abd88fea624d4a2cd.png" width="100%"></kbd></p>
    <br>

<a id="node-447"></a>
- 4.2 - Linear-Activation Forward
  <br>

    <a id="node-448"></a>
    <p align="center"><kbd><img src="assets/1747fe1258d99596ab00a70b7fa4bb586b1c5820.png" width="100%"></kbd></p>
    <br>

    <a id="node-449"></a>
    <p align="center"><kbd><img src="assets/5e1f1a4bfbcefdf83e3af7b8047be94eb033f6ba.png" width="100%"></kbd></p>
    <br>

    <a id="node-450"></a>
    <p align="center"><kbd><img src="assets/0effdcb2f5bae3482f399b536b38d0ea2a0ec233.png" width="100%"></kbd></p>
    <br>

    <a id="node-451"></a>
    <p align="center"><kbd><img src="assets/f545dee05d28688aec24b7c5da5a3d087628e7de.png" width="100%"></kbd></p>
    <br>

<a id="node-452"></a>
- 4.3 - L-Layer Model
  <br>

    <a id="node-453"></a>
    <p align="center"><kbd><img src="assets/2da8d82f9ba297b0ba5860f84704a5d5bfb2ae2e.png" width="100%"></kbd></p>
    <br>

    <a id="node-454"></a>
    <p align="center"><kbd><img src="assets/4b508dad8d7d7d1745c3a820fe414194075a57bc.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/4b508dad8d7d7d1745c3a820fe414194075a57bc.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/e197566dd83100780a3750df9e640777b3f07f3f.png" width="100%"></kbd></p>
    > [!NOTE]
    > for l in range(1, L) -> l = 1,2...L-1

    <br>

    <a id="node-455"></a>
    <p align="center"><kbd><img src="assets/c993af907b28a3ada25b3c7f5d7abc816067dd10.png" width="100%"></kbd></p>
    <br>


<a id="node-456"></a>
### 5 - Cost Function

<br>

  <a id="node-457"></a>
  <p align="center"><kbd><img src="assets/655b71cd317b342568b905fc0b4977ef777322b6.png" width="100%"></kbd></p>
  <br>

  <a id="node-458"></a>
  <p align="center"><kbd><img src="assets/92cfb5212b0e1f070b3e8b2a39d9cc1fde4b6c34.png" width="100%"></kbd></p>
  <br>

  <a id="node-459"></a>
  <p align="center"><kbd><img src="assets/5579a44e165f088d194b8e390e3fb2e8fc45573d.png" width="100%"></kbd></p>
  <br>


<a id="node-460"></a>
### 6 - Backward Propagation Module

<br>

  <a id="node-461"></a>
  <p align="center"><kbd><img src="assets/a40554257c41628f42cb402a53d1a2c9a31cbf55.png" width="100%"></kbd></p>
  <br>

  <a id="node-462"></a>
  <p align="center"><kbd><img src="assets/f67a068afe0a6eb9529350658e8a471c19390895.png" width="100%"></kbd></p>
  > [!NOTE]
  > keepdims = True sẽ ngăn không để Python nó biến kết quả đang matrix 2D
  > thành array vector 1D

  <br>

<a id="node-463"></a>
- 6.1 - Linear Backward
  <br>

    <a id="node-464"></a>
    <p align="center"><kbd><img src="assets/83711cb8a7cb804eefdabee280c9fecfbd4b0000.png" width="100%"></kbd></p>
    <br>

    <a id="node-465"></a>
    <p align="center"><kbd><img src="assets/bddaf365d085bed46dda563384c4dfe58267e138.png" width="100%"></kbd></p>
    <br>

    <a id="node-466"></a>
    <p align="center"><kbd><img src="assets/af4e71ee06bd0bfaffa5d8eca06ff1a73bae5afb.png" width="100%"></kbd></p>
    <br>

<a id="node-467"></a>
- 6.2 - Linear-Activation Backward
  <br>

    <a id="node-468"></a>
    <p align="center"><kbd><img src="assets/9a5ce77d6c67c23d09b8539b8fe00c826de42b38.png" width="100%"></kbd></p>
    <br>

    <a id="node-469"></a>
    <p align="center"><kbd><img src="assets/cd2952ab7de4de00d1e7b029dbc7b0d1d197de9f.png" width="100%"></kbd></p>
    <br>

<a id="node-470"></a>
- 6.3 - L-Model Backward
  <br>

    <a id="node-471"></a>
    <p align="center"><kbd><img src="assets/948eadac69941cc8dba2b53785bdc6dcd532c961.png" width="100%"></kbd></p>
    <br>

    <a id="node-472"></a>
    <p align="center"><kbd><img src="assets/b972c2ac62316c50e8ed1f0d1f6ca6da23876825.png" width="100%"></kbd></p>
    <br>

    <a id="node-473"></a>
    <p align="center"><kbd><img src="assets/bffe0ef7e14b09af201918dfd8a1e73ed693d6e4.png" width="100%"></kbd></p>
    <br>

    <a id="node-474"></a>
    <p align="center"><kbd><img src="assets/cac50955db94cec4044d493ff81bf10ac90019cb.png" width="100%"></kbd></p>
    <br>

<a id="node-475"></a>
- 6.4 - Update Parameters
  <br>

    <a id="node-476"></a>
    <p align="center"><kbd><img src="assets/de54abb21aae31506c2732164e39e6c1be56aa68.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/de54abb21aae31506c2732164e39e6c1be56aa68.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/95c68374f92bce0ac85254842454e4535ae4be71.png" width="100%"></kbd></p>
    <br>

    <a id="node-477"></a>
    <p align="center"><kbd><img src="assets/8c7a329c18a3bd1de228d08c33bf90baf0d67261.png" width="100%"></kbd></p>
    <br>

    <a id="node-478"></a>
    <p align="center"><kbd><img src="assets/601342f9343628098e25ed393237e98bb0e6cb33.png" width="100%"></kbd></p>
    <br>


<a id="node-479"></a>
### Tóm Lược Quy

> [!NOTE]
> TÓM LƯỢC QUY
> TRÌNH CHO DỄ HIỂU

<br>

  <a id="node-480"></a>
  <p align="center"><kbd><img src="assets/300d979cf179690b595b21792bb2e654d2def1e0.png" width="100%"></kbd></p>
  <br>

  <a id="node-481"></a>
  <p align="center"><kbd><img src="assets/9b0b5f048f926820fc80c71972f37b23160a9431.png" width="100%"></kbd></p>
  <br>

<a id="node-482"></a>

<p align="center"><kbd><img src="assets/f83d687841d9d6da17ed03515222f103673a39b6.png" width="100%"></kbd></p>

<br>


<a id="node-483"></a>
## Programming Assignment: Deep Neural Network - Application

> [!NOTE]
> Build and train a deep L-layer neural network, and apply it to 
> the very important problem of classifying cat images from 
> non-cat images.  :)

<br>


<a id="node-484"></a>
### 1 - Packages

<br>

  <a id="node-485"></a>
  <p align="center"><kbd><img src="assets/448c1b82a231c06f3d92db28e8830b8180c49009.png" width="100%"></kbd></p>
  <br>


<a id="node-486"></a>
### 2 - Load and Process the Dataset

<br>

  <a id="node-487"></a>
  <p align="center"><kbd><img src="assets/71be1c371c6e191908fa079a88cb7da600d9b62f.png" width="100%"></kbd></p>
  <br>

  <a id="node-488"></a>
  <p align="center"><kbd><img src="assets/801b17ff2e66d229f477fb0ff511e53d64336cfb.png" width="100%"></kbd></p>
  <br>

  <a id="node-489"></a>
  <p align="center"><kbd><img src="assets/c956c7d54c48eafff2e6111359b1ef8c7fd63344.png" width="100%"></kbd></p>
  <br>


<a id="node-490"></a>
### 3 - Model Architecture

<br>

<a id="node-491"></a>
- 3.1 - 2-layer Neural Network
  <br>

    <a id="node-492"></a>
    <p align="center"><kbd><img src="assets/67b4ce8e65ef1fe4c90638ab455726a5ddd5664c.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/67b4ce8e65ef1fe4c90638ab455726a5ddd5664c.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/d53c62bc02e18e03f04efc2e6b348ef249018bc3.png" width="100%"></kbd></p>
    <br>

<a id="node-493"></a>
- 3.2 - L-layer Deep Neural Network
  <br>

    <a id="node-494"></a>
    <p align="center"><kbd><img src="assets/eddd9d4271981bd12f80cf1daeb0e8fb7db9c645.png" width="100%"></kbd></p>
    <br>

<a id="node-495"></a>
- 3.3 - General Methodology
  <br>

    <a id="node-496"></a>
    <p align="center"><kbd><img src="assets/c03ee3c5b903e142fc65553e8f1029253c3fbd65.png" width="100%"></kbd></p>
    <br>


<a id="node-497"></a>
### 4 - Two-layer Neural Network

<br>

<a id="node-498"></a>
- Exercise 1 - two_layer_model
  <br>

    <a id="node-499"></a>
    <p align="center"><kbd><img src="assets/03867d90f747657fde02f59a318e74e80539a910.png" width="100%"></kbd></p>
    <br>

    <a id="node-500"></a>
    <p align="center"><kbd><img src="assets/6aa978f2bdee25c442414bba4b8ca45249a65530.png" width="100%"></kbd></p>
    <br>

    <a id="node-501"></a>
    <p align="center"><kbd><img src="assets/d6801d4428d05e3bc8f085253682c6d2fb3b5840.png" width="100%"></kbd></p>
    <br>

    <a id="node-502"></a>
    <p align="center"><kbd><img src="assets/1b933a39f0443b65a9f36895fd9704a7342986cb.png" width="100%"></kbd></p>
    <br>

    <a id="node-503"></a>
    <p align="center"><kbd><img src="assets/2ec57aedf5f00a459908a92328ee49c2bef25c61.png" width="100%"></kbd></p>
    <br>

<a id="node-504"></a>
- 4.1 - Train the model
  <br>

    <a id="node-505"></a>
    <p align="center"><kbd><img src="assets/dc987d21f3e72715ad0e4f492b54aa802d45a18b.png" width="100%"></kbd></p>
    <br>

    <a id="node-506"></a>
    <p align="center"><kbd><img src="assets/1e4dc2edbddf2eed7e6468002f2b839038a37f55.png" width="100%"></kbd></p>
    <br>

    <a id="node-507"></a>
    <p align="center"><kbd><img src="assets/a8e6f5ba9f50476f1b8a20d958cd60821d445cb8.png" width="100%"></kbd></p>
    > [!NOTE]
    > Note: You may notice that running the model on fewer iterations (say
    > 1500) gives better accuracy on the test set. This is called **"early
    > stopping"** and you'll hear more about it in the next course. Early stopping
    > is a way to prevent overfitting.

    <br>


<a id="node-508"></a>
### 5 - L-layer Neural Network

<br>

<a id="node-509"></a>
- Exercise 2 - L_layer_model
  <br>

    <a id="node-510"></a>
    <p align="center"><kbd><img src="assets/1cbee86782e97a9ddac888b104d7ef06b029156e.png" width="100%"></kbd></p>
    <br>

    <a id="node-511"></a>
    <p align="center"><kbd><img src="assets/cd3358f275c4044094fe4d454744c560e1e16d67.png" width="100%"></kbd></p>
    <br>

    <a id="node-512"></a>
    <p align="center"><kbd><img src="assets/e82877da15919e7d5e768dc77a74745806048a1b.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/e82877da15919e7d5e768dc77a74745806048a1b.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/ffd31bb02a8eea78be92a1ab7d1f28f9dbca06d4.png" width="100%"></kbd></p>
    <br>

<a id="node-513"></a>
- 5.1 - Train the model
  <br>

    <a id="node-514"></a>
    <p align="center"><kbd><img src="assets/e7cff91153db2bb440319621cbbcce5b8c68e3e8.png" width="100%"></kbd></p>
    <br>

    <a id="node-515"></a>
    <p align="center"><kbd><img src="assets/4e491e1fc91a1e80633b3524da71cebf58abc123.png" width="100%"></kbd></p>
    > [!NOTE]
    > In the next course on "Improving deep neural networks," you'll be 
    > able to obtain even higher accuracy by systematically 
    > **searching for better hyperparameters: learning_rate, 
    > layers_dims, or num_iterations, for example.**

    <br>


<a id="node-516"></a>
### 6 - Results Analysis

<br>

  <a id="node-517"></a>
  <p align="center"><kbd><img src="assets/800089899f640dd703e8c18278aa618510d37878.png" width="100%"></kbd></p>
  <br>


<a id="node-518"></a>
### 7 - Test with your own image (optional/ungraded exercise)

<br>

  <a id="node-519"></a>
  <p align="center"><kbd><img src="assets/d77a0eca5807f2181b33bd559dfd15dea4878c07.png" width="100%"></kbd></p>
  <br>

<a id="node-520"></a>

<p align="center"><kbd><img src="assets/08cad1747d6ca6aeb2bacb85de875a23f6e02242.png" width="100%"></kbd></p>

<br>


<a id="node-521"></a>
## References

> [!NOTE]
> **Week 2:
>  • GitHub**: \_Implementing a Neural Network from Scratch in Python – An Introduction\_ (Denny Britz, 2015)
>  • \_Why normalize images by subtracting dataset's image mean, instead of the current image mean in deep learning?\_ (Stack Exchange)
> **Week 3:** • \_CS231n: Convolutional Neural Networks for Visual Recognition\_ (Stanford University)
> **Week 4:**\_Autoreload of modules in IPython\_ (Stack Overflow)

<br>

