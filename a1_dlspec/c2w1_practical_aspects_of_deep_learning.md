# C2w1_practical Aspects Of Deep Learning

📊 **Progress:** `54` Notes | `131` Screenshots

---

Discover and experiment with a variety of different initialization methods, apply L2 regularization and dropout to avoid model overfitting, then apply gradient checking to identify errors in a fraud detection model.
**Learning Objectives**
 • Give examples of how different types of initializations can lead to different results
 • Examine the importance of initialization in complex neural networks
 • Explain the difference between train/dev/test sets
 • Diagnose the bias and variance issues in your model
 • Assess the right time and place for using regularization methods such as dropout or L2 regularization
 • Explain Vanishing and Exploding gradients and how to deal with them
 • Use gradient checking to verify the accuracy of your backpropagation implementation
 • Apply zeros initialization, random initialization, and He initialization
 • Apply regularization to a deep learning model

<a id="node-524"></a>
## Setting Up Your Machine Learning Application

<br>


<a id="node-525"></a>
### Train Dev Test Sets

<br>

<a id="node-526"></a>
- 1 The course is about practical aspects of deep learning and making neural network work well by \\*optimizing hyperparameters\\*, \\*data setup\\*, and optimization \\*algorithms\\*.  2 Deep learning has been successful in various areas including \\*natural language processing\\*, \\*computer vision\\*, \\*speech recognition\\*, structured data, computer security, and logistics.  3 Intuitions from one application area \\*do not always transfer to another\\*, and it is difficult to guess the best choice of \\*hyperparameters\\* on the first attempt.  4 Applied deep learning is an\\* iterative process\\* where \\*setting up data sets efficiently\\* can help make progress quicker.  5 The workflow of training deep learning algorithms involves \\*training on a training set,\\* using a \\*dev set\\* or hold-out cross-validation set to \\*choose the best model\\*, and \\*evaluating\\* the final model on a \\*test set\\* for an \\*unbiased estimate\\* of its performance.  6 In the previous era of machine learning, a \\*70/30\\* train-test split was widely considered best practice, but in the modern \\*big data\\* era, different rules of thumb are required.
  > 1 The practical aspects of deep learning:
  >  2 Welcome to this course on the practical aspects of deep learning. In this week, you'll learn the **practical aspects** of how to make your neural network work well, ranging from **hyperparameter tuning** to **optimizing your data** and **learning algorithm**to make sure that your neural network runs efficiently.
  >
  >  - Importance of hyperparameter tuning:
  >  4 When training a neural network, you have to make a lot of decisions, such as how many layers will your neural network have, how many **hidden units**should each layer have, what's the learning rate, and what are the **activation** **functions** you want to use for the different layers. It's almost impossible to guess the right values for all of these hyperparameters on your first attempt, so applied machine learning is a highly iterative process where you refine your ideas and choices based on the outcomes of experiments.
  >
  >  - **Transferability** of **intuitions** across **different domains**:
  >  6 Intuitions from one domain or application area often do not transfer to other application areas. The best choices may depend on the amount of data, the number of input features, and the configuration of GPUs and CPUs. So, finding a good choice of network for your application is an iterative process that requires going around the cycle of training, testing, and refining many times.
  >
  >  7 Setting up data sets well:
  >  8 Setting up your data sets well, in terms of your train, development, and test sets can make you much more efficient at the iterative process of finding a good choice of network for your application.
  >
  >  9 The traditional workflow:
  >  10 The workflow is that you keep on training algorithms on your training set and use your development set (also called hold-out cross validation set) to see which of many different models performs best. When you have a final model that you want to evaluate, you can take the best model you have found and evaluate it on your test set to get an unbiased estimate of how well your algorithm is doing.
  >
  >  11 The traditional train/test split:
  >  12 In the previous era of machine learning, it was common practice to split your data according to maybe a 70/30% in terms of a train/test split or a 60/20/20% split in terms of train/dev/test split. However, in the modern big data era, these ratios may not be appropriate anymore.
  >
  >  13 The importance of big data:
  >  14 In the modern big data era, where you might have a million examples in total, it's important to have more data for your training set to make sure that your neural network has enough examples to learn from. In this case, the traditional train/test split ratios may not be appropriate anymore.

  <br>

    <a id="node-527"></a>
    <p align="center"><kbd><img src="assets/5b13c61177a924fe0907f9f96c68bc6d4e7abe81.png" width="100%"></kbd></p>
    > And what I've seen is that intuitions from one domain or from one
    > application area often **do not transfer** to other application areas. And the
    > best choices may **depend on the amount of data** you have, the
    > **number of input features** you have through your **computer
    > configuration** and whether you're training on **GPUs** **or CPUs**. And if
    > so, exactly what **configuration** of GPUs and CPUs...and many other things.

    > Even **very experienced** deep learning people find it almost **impossible** to
    > correctly guess the **best choice of hyperparameters** the very first time. And
    > so today, applied deep learning is a very **iterative process** where you
    > just have to **go around this cycle many times** to hopefully **find a good
    > choice of network** for your application

    <br>

    <a id="node-528"></a>
    <p align="center"><kbd><img src="assets/af06ec8827f713267fe328ee7d4292b6df701253.png" width="100%"></kbd></p>
    > Đại khái là hồi xưa data ít thì chia 7/3/3 còn nay thì thường chỉ 98/1/1 là đủ

    <br>

    <a id="node-529"></a>
    <p align="center"><kbd><img src="assets/f2fadfcd0eea1a3229051302f2b01734fe65a858.png" width="100%"></kbd></p>
    > Đv vấn đề mismatched train/test đại khái là training set và test set
    > có feature khác nhau. Ví dụ ảnh để train thì dùng ảnh chất lượng
    > cao còn ảnh để test thì lại do user upload lên có chất lượng kém.
    > Lời khuyên / nguyên tắc tối thượng là
    >
    > '**Make sure the dev & test come from the same distribution"**Cụ thể trong trường hợp này thì phải dùng web images để  train
    > còn user upload image để cross validation + test

    > Cái nữa là không nhất thiết phải có test sét vì
    > thật ra nó chỉ đóng vai trò 'công bố' tỉ lệ đúng
    > của model 1 cách khách quan. Nếu không có
    > nhu cầu này thì ko cần test set.

    <br>


<a id="node-530"></a>
### Bias / Variance

<br>

<a id="node-531"></a>
- 1 Good machine learning practitioners have a \\*sophisticated understanding\\* of \\*bias\\* and \\*variance\\*.  2 Bias and Variance is e\\*asily learned\\* but \\*difficult to master.\\*  3 In Deep Learning area, there is\\* less discussion\\* of the \\*Bias/Variance trade-off.\\*  4 Bias and variance are visualized through a 2D example in which a straight line represents underfitting, an overly complex curve represents overfitting, and a medium complexity curve represents a reasonable fit.  5 High dimensional problems require metrics such as the \\*train set error\\* and the \\*development set error\\* to \\*understand bias and variance\\*.  6 \\*High variance\\* is determined when an algorithm performs \\*well on the training set\\* but \\*poorly on the development set\\*.  7 \\*High bias\\* is determined when an algorithm is \\*not performing well on the training set\\* and \\*does not fit the data well\\*.  8 \\*High bias\\* and \\*high variance\\* occur when an algorithm is \\*not performing well on the training\\* set and \\*does not generalize well to the development set.\\*  9 Low bias and low variance occur when an algorithm is \\*performing well on the training set\\* and \\*generalizes well to the development set\\*.  10 Analyzing bias and variance is predicated on the \\*assumption\\* that the \\*optimal error is nearly 0%\\*.
  > 1 The importance of understanding Bias and Variance in machine learning: The speaker notes that almost all really good machine learning practitioners have a sophisticated understanding of Bias and Variance. While Bias and Variance are easily learned, they are difficult to master. Even if one has a basic understanding of Bias and Variance, there is often more nuance to it than expected. Understanding these concepts is important for developing effective machine learning models.
  >
  > 2 Bias/Variance trade-off in Deep Learning Error: The speaker notes that while Bias and Variance are still talked about in the context of Deep Learning era, there has been less discussion of the Bias/Variance trade-off. In a simple 2D example, one can plot the data and visualize the Bias and Variance. However, in high-dimensional problems, one cannot plot the data and visualize the decision boundary. Instead, there are a couple of different metrics to understand Bias and Variance.
  >
  >  3 Train set error and development set error: Continuing with the example of cat picture classification, the speaker notes that the two key numbers to look at to understand Bias and Variance are the train set error and the development set error. For instance, if the train set error is 1% and the dev set error is 11%, the algorithm is doing very well on the training set but poorly on the development set, suggesting high variance.
  >
  > 4 High variance vs. high bias: If the train set error is 15% and the dev set error is 16%, the algorithm is not even fitting the training data well, suggesting high bias. In contrast, if the algorithm has 15% training set error and, say, 30% dev set error, it has high bias and high variance. Lastly, if the algorithm has 0.5% training set error and 1% dev set error, it has low bias and low variance.
  >
  > 5 The assumption of Bayes error: The analysis is predicated on the assumption that human-level performance gets nearly 0% error, or more generally, that the optimal error, sometimes called Bayes error, is nearly 0%. If the optimal error or Bayes error were much higher, say, it were 15%, then a classifier with 15% training set error would not be considered to have high bias or high variance. This case presents a unique challenge for analyzing Bias and Variance when no classifier can do very well, for example, if there are really blurry images.

  <br>

    <a id="node-532"></a>
    <p align="center"><kbd><img src="assets/598c207b54539dff68f694953bb46c67f4d5bcfe.png" width="100%"></kbd></p>
    > Vấn đề là đv 2D thì còn plot được, còn nhiều D hơn
    > thì phải có cách khác để nhận biết vấn đề overfitting

    <br>

    <a id="node-533"></a>
    <p align="center"><kbd><img src="assets/95df63f7048f3ff53674e6169b18ab9d1d7e942c.png" width="100%"></kbd></p>
    > Đại khái là những nhận định trên phải giả định **Bayes error** là 0%.
    > Chứ nếu lớn hơn, ví dụ như 14%, thì 15% của training error không
    > phải là high bias.
    >
    > Và thực tế nhiều vấn đề Bayes error ko phải là 0%

    <br>

    <a id="node-534"></a>
    <p align="center"><kbd><img src="assets/765675da083fd8b4ae0e0e75700fd996df2f1b7b.png" width="100%"></kbd></p>
    > Optimal (Bayes) error là gì?

    <br>

    <a id="node-535"></a>
    <p align="center"><kbd><img src="assets/ed0c7158cc998efed6e372e79b119468411ba45f.png" width="100%"></kbd></p>
    <br>


<a id="node-536"></a>
### Basic Recipe For Machine Learning

<br>

<a id="node-537"></a>
- 1 The \\*basic\\* \\*recipe\\* for training a neural network involves \\*diagnosing\\* whether the algorithm has \\*high bias or high variance\\*.  2 If there is a \\*high bias\\*, solutions could be \\*adding more hidden layers,\\* \\*more hidden units,\\* or training it for a\\* longer time.\\* One could also try different neural network \\*architectures\\* to see if there' s a better-suited one for the problem at hand.  3 If there is a \\*high variance\\*, adding \\*more data\\* is the best solution, if possible. If not, \\*regularization\\* or trying a \\*different\\* neural network architecture could help.  4 Selecting the \\*appropriate solution\\* for the problem is \\*essential\\*. If one has a \\*high bias\\* problem, getting \\*more data \\*is \\*not\\* always the most efficient solution.  5 \\*Deep learning\\* has made it easier to reduce bias and variance without necessarily increasing the other.
  <br>

  <a id="node-538"></a>
  - Sure, here's a more detailed answer with indexed style:  In the previous video, the concept of bias and variance in machine learning algorithms was introduced. These concepts can help diagnose issues with an algorithm's performance and guide improvements.  When training a neural network, a basic recipe can be used. After an \\*initial model is trained\\*, the following steps can be taken:  Determine if the algorithm has \\*high bias\\* by evaluating its performance on the training set. If high bias is detected, try \\*increasing the complexity\\* of the network, training for a \\*longer period of time\\*, using \\*more advanced optimization\\* algorithms, or experimenting with \\*different\\* neural network \\*architectures\\*. Continue trying these approaches until bias is reduced to acceptable levels, as indicated by \\*good performance on the training set.\\*  Once bias is under control, evaluate the algorithm for \\*high variance\\* by looking at its performance on the \\*development set.\\* If high variance is detected, try \\*getting more data,\\* using \\*regularization\\* techniques, or experimenting with \\*different neural network architectures\\*. Continue trying these approaches\\* until both bias and variance are at acceptable levels\\*. The set of approaches to try will depend on whether the algorithm has a bias or variance problem. It is \\*important to be clear\\* about \\*which type of problem\\* is present to select the m\\*ost useful approaches\\* to try.  In the past, there was a \\*bias-variance tradeoff\\* where \\*reducing one type of error could increase the other\\*. However, in the era of deep learning and big data, it is possible to reduce bias or variance without hurting the other type of error as much. Increasing the size of the network and getting more data are both effective approaches for reducing error without introducing the tradeoff.  The basic recipe for machine learning presented in the video provides a \\*systematic approach\\* to improving algorithm performance. By \\*understanding\\* the b\\*ias-variance tradeoff\\* and \\*selecting appropriate approaches\\* to try, it is possible to drive down b\\*oth types of error\\* and achieve good performance.
    > Quy trình

    <br>

      <a id="node-539"></a>
      <p align="center"><kbd><img src="assets/d687ba791b5a2df167837b9596bf33e2e4dd77b2.png" width="100%"></kbd></p>
      > High bias -> 
      > - Dùng bigger (more complex) network
      > - Train longer
      > - Different NN architecture (sẽ nói sau)
      >
      > High variace: 
      > - Train in more data
      > - Regularization
      > - Different NN architecture

      > Đv vấn đề **trade off giữa bias vs variance**thì đại khái là ổng nói
      > **ngày xưa thô**i còn với modern n.n thì nếu có **nhiều data** (fix
      > issue high variance) + dùng **big network** (fix issue high bias) thì
      > không hề có chuyện phải trade of giữa bias và variance. Có
      > chăng là '**computational time**'. Và đây chính là **ưu điểm quan trọng**
      > rất lớn của N.N giúp nó phát triển mạnh

      <br>


<a id="node-540"></a>
## Connect With Your Mentors And Fellow Learners On Discourse!

<br>


<a id="node-541"></a>
## Regularizing Your Neural Network

<br>


<a id="node-542"></a>
### Clarification About Upcoming Regularization Video

<br>

<a id="node-543"></a>
- ...
  <br>

    <a id="node-544"></a>
    <p align="center"><kbd><img src="assets/0052073c0d810c633730799aff49c0063fe75606.png" width="100%"></kbd></p>
    <br>


<a id="node-545"></a>
### Regularization

<br>

<a id="node-546"></a>
- 1 \\*Regularization\\* is a technique used to \\*prevent overfitting\\* or \\*reduce variance\\* in neural networks.  2 One common way to perform regularization is by \\*adding a regularization term\\* to the \\*cost function\\* of the network.  3 The most common type of regularization is \\*L2 regularization\\*, which \\*adds a term to the cost function\\* that is proportional to the \\*squared norm of the weight parameters\\* of the network.  4 \\*L1 regularization\\* is an alternative to \\*L2 regularization\\* that adds a term proportional to the \\*absolute value of the weight parameters\\* instead of their squared value. This can \\*make the weight vector sparse\\*, but it is \\*not as commonly used as L2\\* regularization.  5 The\\* regularization parameter\\*, \\*lambda\\*, is used to control the strength of the regularization and is \\*typically set using a development set\\* or cross-validation.  6 Regularization is used \\*not only in logistic regression\\* but also in \\*neural networks\\*, where the regularization term is added to the cost function for all the parameters in the network.  7 L2 regularization in neural networks adds a term proportional to the \\*squared norm\\* \\*of all the weight parameters\\* in the network.  8 Lambda is a hyperparameter that needs to be tuned for regularization to work effectively.
  > 1 What is overfitting and how can it be addressed?
  >  2 If your neural network is overfitting your data, that means it's fitting the training data too well and not generalizing to new, unseen data. One of the main ways to address overfitting is through regularization, which helps to reduce variance in the network.
  >
  >  3 What is regularization and how does it work?
  >  4 Regularization is a technique used to prevent overfitting by adding a penalty term to the cost function. In logistic regression, for example, this penalty term is lambda/2m times the squared L2 norm of the weight vector w. The lambda term is the regularization parameter that needs to be tuned using a development set or cross-validation.
  >
  >  5 What is L2 regularization?
  >  6 L2 regularization is the most common type of regularization used in practice. It works by adding a penalty term to the cost function that is proportional to the squared L2 norm of the weight vector w. The effect of L2 regularization is to shrink the weight vector towards zero, which reduces variance in the network.
  >
  >  7 Why is L2 regularization applied only to the weight vector and not to the bias term?
  >  8 The weight vector w usually has many more parameters than the bias term b, especially in high-dimensional problems where overfitting is more likely to occur. Therefore, adding regularization to w has a greater effect on reducing variance than adding regularization to b.
  >
  >  9 What is L1 regularization?
  >  10 L1 regularization is another type of regularization that works by adding a penalty term to the cost function that is proportional to the L1 norm of the weight vector w. Unlike L2 regularization, L1 regularization tends to produce sparse weight vectors with many zero entries, which can help with model compression.
  >
  >  11 Why is L2 regularization more commonly used than L1 regularization?
  >  12 L2 regularization is used much more often than L1 regularization in practice because it has been shown to produce better generalization performance in many cases. However, L1 regularization may be useful in certain situations where model sparsity is important.
  >
  >  13 How is regularization applied to a neural network?
  >  14 In a neural network, regularization can be applied by adding a penalty term to the cost function that is proportional to the squared L2 norm of all the weight matrices in the network. The regularization parameter lambda needs to be tuned using a development set or cross-validation.
  >
  >  15 What is the formula for the squared L2 norm of a matrix?
  >  16 The squared L2 norm of a matrix is defined as the sum of the squares of all its elements. For a weight matrix w with dimensions n[l] x n[l-1], where l is the layer number, the formula for the squared L2 norm is lambda/2m * sum(i=1 to n[l-1], j=1 to n[l]) w[i,j]^2.
  >
  >  17 How is the lambda parameter represented in Python?
  >  18 Lambda is a reserved keyword in Python, so in the programming exercises, l-a-m-b-d is used instead to represent the lambda regularization parameter.

  <br>

    <a id="node-547"></a>
    <p align="center"><kbd><img src="assets/557adaa8360acbf2d23933ed28e9f97cf6bd7906.png" width="100%"></kbd></p>
    > Đại khái là ôn lại để regularize **Logistic Regression**, add thêm 1
    > R**eg term** bằng **(lambda/2m)* tổng bình phương các weight**
    > nếu là L2, nếu là L1 thì **(lambda/2m)*tổng giá trị tuyệt đối của
    > weight.**
    >
    > Mà đối với L2, tổng bình phương các weight chính là**bình
    > phương của norm** (gọi là L2 norm, **Frobenius norm**) của
    > vector W (=[w1,w2..wn])
    >
    > Make weight vector W **sparse** đại khái là**w_j bị set = 0** khiến
    > **vector hay matrix W có nhiều chỗ 0 gọi là sparse**, **còn L2 thì
    > nó chỉ ém w về gần bằng 0 thôi**
    >
    > Weight decay chính là cách gọi khác của L2 regularization

    <br>

    <a id="node-548"></a>
    <p align="center"><kbd><img src="assets/980f3c1af311424a63f4152279ba8e7e891b0e5c.png" width="100%"></kbd></p>
    > **"Frobenius norm"** The Frobenius norm is a matrix norm that defines
    > the magnitude of  a matrix. It is defined as the**square root of the sum
    > of the squares  of all the elements of a matrix**. In other words, it
    > calculates the **L2  norm of a matrix**. It is commonly used in linear
    > algebra and in the  training of machine learning models, particularly in
    > deep learning. In the context of deep learning, the **Frobenius norm** of
    > the weight  matrix of a layer is often used as a **regularization term** to
    > **encourage** the model to have **small weights**, which helps to prevent
    > **overfitting** and improve the **generalization** performance of the model.
    > The Frobenius norm is also used to measure the **similarity between
    > two matrices**, by calculating the distance between the two matrices.
    >
    > **"Weight decay"**Weight decay is a regularization technique used in
    > training machine learning models, especially neural networks, to
    > p**revent overfittin**g  and improve the generalization performance of the
    > model. It works  by **adding a penalty term to the loss function** that is
    > proportional to  the magnitude of the model weights. **This penalization
    > discourages  the model from having too high weights**, which reduces
    > the  magnitude of weights and therefore the complexity of the model,
    > leading to a better generalization to unseen data. **The term weight
    > decay is often used interchangeably** with **L2 regularization.**

    > Tương tự trong NN cũng add **regularization term** vào **cost function**
    > bằng **tổng bình phương tất cả các weight của toàn network**nhân với
    > lambda/2m. Khi triển khai ra chút xíu thì được kiểu như khi update w thì
    > nhân w với 1 hệ số bằng (**1 - alpha.lambda/m)**nhỏ hơn 1 nên **khiến
    > w nhỏ lại** một chút (trước khi update với derivative (- alpha*dJ/dw) lại
    > gọi là **weight decay**

    <br>

  <a id="node-549"></a>
  - 1 What is overfitting and how can it be addressed?  2 If your neural network is overfitting your data, that means it's fitting the training data too well and not generalizing to new, unseen data. One of the main ways to address overfitting is through regularization, which helps to reduce variance in the network.  3 What is regularization and how does it work?  4 Regularization is a technique used to prevent overfitting by adding a penalty term to the cost function. In logistic regression, for example, this penalty term is lambda/2m times the squared L2 norm of the weight vector w. The lambda term is the regularization parameter that needs to be tuned using a development set or cross-validation.  5 What is L2 regularization?  6 L2 regularization is the most common type of regularization used in practice. It works by adding a penalty term to the cost function that is proportional to the squared L2 norm of the weight vector w. The effect of L2 regularization is to shrink the weight vector towards zero, which reduces variance in the network.  7 Why is L2 regularization applied only to the weight vector and not to the bias term?  8 The weight vector w usually has many more parameters than the bias term b, especially in high-dimensional problems where overfitting is more likely to occur. Therefore, adding regularization to w has a greater effect on reducing variance than adding regularization to b.  9 What is L1 regularization?  10 L1 regularization is another type of regularization that works by adding a penalty term to the cost function that is proportional to the L1 norm of the weight vector w. Unlike L2 regularization, L1 regularization tends to produce sparse weight vectors with many zero entries, which can help with model compression.  11 Why is L2 regularization more commonly used than L1 regularization?  12 L2 regularization is used much more often than L1 regularization in practice because it has been shown to produce better generalization performance in many cases. However, L1 regularization may be useful in certain situations where model sparsity is important.  13 How is regularization applied to a neural network?  14 In a neural network, regularization can be applied by adding a penalty term to the cost function that is proportional to the squared L2 norm of all the weight matrices in the network. The regularization parameter lambda needs to be tuned using a development set or cross-validation.  15 What is the formula for the squared L2 norm of a matrix?  16 The squared L2 norm of a matrix is defined as the sum of the squares of all its elements. For a weight matrix w with dimensions n[l] x n[l-1], where l is the layer number, the formula for the squared L2 norm is lambda/2m * sum(i=1 to n[l-1], j=1 to n[l]) w[i,j]^2.  17 How is the lambda parameter represented in Python?  18 Lambda is a reserved keyword in Python, so in the programming exercises, l-a-m-b-d is used instead to represent the lambda regularization parameter.
    <br>


<a id="node-550"></a>
### Why Regularization Reduces Overfitting?

<br>

<a id="node-551"></a>
- 1 \\*Regularization\\* helps with \\*overfitting\\* and r\\*educing variance\\* problems.  2 The addition of an \\*extra term\\* \\*penalizes weight matrices\\* from being \\*too large\\*.  3 By cranking up \\*lambda\\*, which is the \\*regularization parameter\\*, the weights will be \\*closer to zero\\* and it will \\*simplify the network\\*, making it \\*less prone to overfitting\\*.  4 If the \\*regularization parameter\\* is large, the \\*weights are small\\*, and the activation function is \\*tanh\\*, then each layer will be \\*roughly linear\\* and the \\*whole network will compute a linear function\\*.  5 The network will be computing something \\*not too far from a big linear function,\\* which is a simple function, rather than a complex highly non-linear function, making it \\*less able to overfit\\*.  6 Implementational tip: when implementing regularization, the cost function J is modified by adding an extra term that penalizes the weights being too large.
  > 1 Why does regularization help with overfitting?
  >  2 Regularization helps with overfitting by adding an extra term to the cost function that penalizes large weight values. This penalty term encourages the model to use simpler, more generalizable patterns instead of complex, overfitting ones.
  >  3 Why does it help with reducing variance problems?
  >  4 Reducing variance in a model means making it less sensitive to small changes in the training data. Regularization achieves this by shrinking the weights towards zero, making the model more robust and less prone to overfitting.
  >  5 Intuition behind regularization: simplified neural networks
  >  6 Regularization can be thought of as reducing the complexity of the neural network by shrinking the weights towards zero. This can result in a simpler network that is less prone to overfitting. In the extreme case where the regularization parameter is very large, the weights are effectively zeroed out, resulting in a much simpler network.
  >  7 Intuition behind regularization: impact on activation functions
  >  8 Regularization can also affect the activation functions used in the network. For example, with the tanh activation function, small weights will result in small values for the input to the activation function. This can cause the activation function to behave more like a linear function, resulting in a simpler, more interpretable model.
  >  9 Implementational tip: debugging gradient descent with regularization
  >  10 When implementing gradient descent with regularization, it's important to plot the training and validation error as a function of the regularization parameter. This can help determine the optimal value of the regularization parameter that balances bias and variance in the model.

  <br>

    <a id="node-552"></a>
    <p align="center"><kbd><img src="assets/61b116075666d07a4b7f94c1ad8bb22a7d35f72f.png" width="100%"></kbd></p>
    > Đại khái là tương tự như tác dụng của Reg đ/v các algorithm
    > khác thì đv N.N cũng vậy nó sẽ **'ÉM' (penalize)** cho các các
    > **params w không thể lớn được thậm chí gần = 0**, từ đó nó
    > khiến cho model trở nên **simple** hơn (trong lecture  ổng nói vẽ
    > vậy là có ý như w ở các hidden layer thành gần 0 hết dẫn đến
    > model nó **'dần trở nên như 1 linear regression model'**. Nhưng
    > thực tế không phải w nó bằng 0 mà là nó trở nên nhỏ đi nên giảm
    > độ ảnh hưởng đến model.

    > Penalize có nghĩa là phạt hoặc trừng phạt. Trong
    > khoa học máy  tính, từ này thường được sử dụng
    > để miêu tả việc thêm một điều  kiện giới hạn hoặc
    > hạn chế cho một mô hình trong quá trình huấn
    > luyện, để tránh overfitting và cải thiện hiệu suất tổng
    > quát của mô hình.

    <br>

    <a id="node-553"></a>
    <p align="center"><kbd><img src="assets/b1311d93fac0254d7a0e31d25767e2a095f35d5c.png" width="100%"></kbd></p>
    > Đại khái là nếu sét **lambda lớn** để Regularization tác dụng
    > mạnh **ém weight nhỏ xuống** thì vì z = wa + b, **z cũng sẽ
    > nhỏ lại**
    >
    > vì thế a = g(z) mà g thường là tanh, sigmoid, hay relu thì **đều
    > có tính chất 'LINEAR' trong đoạn z nhỏ**. Hiểu đại khái là sẽ
    > **khiến toàn bộ hệ thống trở nên linear hơn** -> **tăng độ bias,
    > giảm tính variance.**

    > Và khi dùng Regularization thì nhớ add RegTerm
    > khi tính J nếu không sẽ không thấy J giảm khi
    > Iteration Gradient Descent

    > Ví dụ ổng lấy hàm tanh cho thấy nếu z trong
    > khoảng nhỏ quanh 0, thì g(z) sẽ gần như tuyến
    > tính. Đối với sigmoid cũng tương tự.

    <br>

  <a id="node-554"></a>
  - 1 Why does regularization help with overfitting?   2 Regularization helps with overfitting by adding an extra term to the cost function that penalizes large weight values. This penalty term encourages the model to use simpler, more generalizable patterns instead of complex, overfitting ones.  3 Why does it help with reducing variance problems?  4 Reducing variance in a model means making it less sensitive to small changes in the training data. Regularization achieves this by shrinking the weights towards zero, making the model more robust and less prone to overfitting.  5 Intuition behind regularization: simplified neural networks  6 Regularization can be thought of as reducing the complexity of the neural network by shrinking the weights towards zero. This can result in a simpler network that is less prone to overfitting. In the extreme case where the regularization parameter is very large, the weights are effectively zeroed out, resulting in a much simpler network.  7 Intuition behind regularization: impact on activation functions  8 Regularization can also affect the activation functions used in the network. For example, with the tanh activation function, small weights will result in small values for the input to the activation function. This can cause the activation function to behave more like a linear function, resulting in a simpler, more interpretable model.  9 Implementational tip: debugging gradient descent with regularization  10 When implementing gradient descent with regularization, it's important to plot the training and validation error as a function of the regularization parameter. This can help determine the optimal value of the regularization parameter that balances bias and variance in the model.
    <br>


<a id="node-555"></a>
### Dropout Regularization

<br>

<a id="node-556"></a>
- 1 \\*Dropout\\* is a \\*powerful regularization technique\\* to \\*prevent over-fitting\\* in neural networks.  2 Dropout involves \\*randomly setting some nodes to zero\\* during training, which results in a much \\*smaller network\\*.  3 By training on smaller networks for each example, the network can be \\*regularized\\*.  4 There are \\*different ways\\* to implement dropout, with the most common being the \\*inverted dropout technique\\*.  5 \\*Inverted dropout \\*involves generating a \\*random matrix\\* with a \\*probability of eliminating hidden units\\*, \\*element-wise multiplying the activation matrix by the dropout matrix\\*, and \\*scaling up the output.\\*  6 Inverted dropout helps to \\*avoid reducing the expected value of the output \\*while regularizing the network, regardless of the keep probability value used.
  > Sure, I'd be happy to provide more detail with indexed main ideas.
  >  1 Dropout regularization:
  >  2 In addition to L2 regularization, dropout is another powerful technique for regularization in neural networks. Dropout is a regularization technique that randomly sets activations to zero during the training process to prevent overfitting.
  >
  > 3 Applying dropout to a neural network:
  >  4 When applying dropout, we go through each of the layers of the network and set a probability of eliminating a node in the neural network. For each node in each layer, we toss a coin with a 50/50 chance of keeping or eliminating the node. If a node is eliminated, we remove all the outgoing connections from that node, resulting in a much smaller network. We then train this much smaller network using backpropagation.
  >
  > 5 Training with different neural networks:
  >  6 For each training example, we train it using one of these neural networks that we obtain after eliminating nodes with dropout. We repeat this process for each training example, resulting in different neural networks for each example.
  >
  >  7 Implementing dropout using inverted dropout:
  >  8 There are a few ways to implement dropout, but the most common technique is called inverted dropout. Inverted dropout involves creating a random matrix with the same shape as the layer's activations, where each element of the matrix has a certain probability of being set to zero.
  >
  > 9 Keep probability:
  >  10 This probability, also known as keep.prob, determines the probability of keeping each node in the layer. For example, if keep.prob is set to 0.8, there is a 20% chance of eliminating any given node.
  >
  > 11 Scaling up activations:
  >  12 We then take the activations from the layer and multiply them element-wise with the random matrix created using the keep.prob value. This has the effect of zeroing out a certain percentage of the activations. We then scale up the resulting activations by dividing them by the keep.prob value, which ensures that the expected value of the activations is maintained.
  >
  > 13 Benefits of dropout:
  >  14 Using dropout can help to prevent overfitting by reducing the interdependence of the neurons in the network, forcing them to learn more robust features. Dropout has been shown to be a highly effective regularization technique and is widely used in deep learning.

  <br>

    <a id="node-557"></a>
    <p align="center"><kbd><img src="assets/bff8d956146b5584df67235199605a0dfad5c201.png" width="100%"></kbd></p>
    > Đại khái cách làm này là với **mỗi lần train** từ 1 bộ
    > dataset ta sẽ **randomly bỏ bớt một số hidden unit**

    <br>

    <a id="node-558"></a>
    <p align="center"><kbd><img src="assets/d2f05f40bbbaae0755289f44cf16eb89635dbc25.png" width="100%"></kbd></p>
    > Đại khái nó sẽ tạo matrix d3 cùng shape với a3, nhưng mỗi item là 1 - true.
    > 0 - false trong đó **khả năng 1 - true là 80%  khả năng 0 - false là 20%.
    > Gọi là keep-prob = 0,8**
    >
    > a3 = **np.multiply(a3, d3)** sẽ bỏ bớt unit (set = 0)
    >
    > Cuối cùng là lấy a3 = **a3 / 0.8** đại khái là để **cho nó lớn lên lại** để nó
    > **'not change the expected value'**

    <br>

    <a id="node-559"></a>
    <p align="center"><kbd><img src="assets/d31d13e4054c344ba8b7738e890a04d4bf746daf.png" width="100%"></kbd></p>
    > Lúc prediction thì đừng có drop out

    <br>

  <a id="node-560"></a>
  - Sure, I'd be happy to provide more detail with indexed main ideas.  1 Dropout regularization:  2 In addition to L2 regularization, dropout is another powerful technique for regularization in neural networks. Dropout is a regularization technique that randomly sets activations to zero during the training process to prevent overfitting.  3 Applying dropout to a neural network:  4 When applying dropout, we go through each of the layers of the network and set a probability of eliminating a node in the neural network. For each node in each layer, we toss a coin with a 50/50 chance of keeping or eliminating the node. If a node is eliminated, we remove all the outgoing connections from that node, resulting in a much smaller network. We then train this much smaller network using backpropagation.  5 Training with different neural networks:  6 For each training example, we train it using one of these neural networks that we obtain after eliminating nodes with dropout. We repeat this process for each training example, resulting in different neural networks for each example.  7 Implementing dropout using inverted dropout:  8 There are a few ways to implement dropout, but the most common technique is called inverted dropout. Inverted dropout involves creating a random matrix with the same shape as the layer's activations, where each element of the matrix has a certain probability of being set to zero.  9 Keep probability:  10 This probability, also known as keep.prob, determines the probability of keeping each node in the layer. For example, if keep.prob is set to 0.8, there is a 20% chance of eliminating any given node.  11 Scaling up activations:  12 We then take the activations from the layer and multiply them element-wise with the random matrix created using the keep.prob value. This has the effect of zeroing out a certain percentage of the activations. We then scale up the resulting activations by dividing them by the keep.prob value, which ensures that the expected value of the activations is maintained.  13 Benefits of dropout:  14 Using dropout can help to prevent overfitting by reducing the interdependence of the neurons in the network, forcing them to learn more robust features. Dropout has been shown to be a highly effective regularization technique and is widely used in deep learning.
    <br>


<a id="node-561"></a>
### Clarification About Upcoming Understanding Dropout Video

<br>

<a id="node-562"></a>
- ...
  <br>

    <a id="node-563"></a>
    <p align="center"><kbd><img src="assets/7631b753c9be0724b4a2f7ae1540db6db1bdfcdd.png" width="100%"></kbd></p>
    <br>


<a id="node-564"></a>
### Understanding Dropout

<br>

<a id="node-565"></a>
- 1 Dropout is a \\*regularization\\* technique that randomly knocks out units in a neural network, giving the effect of working with a \\*smaller network\\*, which can \\*prevent overfitting\\*.  2 Dropout \\*shrinks the squared norm of the weights\\* by \\*spreading out the weights\\*, which is similar to \\*L2 regularization\\*.  3 The L2 penalty on different ways can be different depending on the size of the activation being multiplied into that way, making dropout an adaptive form of L2 regularization.  4 To implement \\*dropout\\*, a \\*keep-prop\\* is chosen, which is the \\*chance of keeping a unit in each layer\\*, and it is feasible to \\*vary keep-prop by layer\\* to reduce overfitting.  5 It is possible to \\*apply dropout to the input layer\\*, but it is \\*less common in practice\\*.  6 Dropout is frequently used in c\\*omputer visio\\*n due to the\\* large input sizes\\* and lack of data, but should \\*only be used if overfitting occurs.\\*  7 The \\*downside\\* of using dropout is that it introduces \\*additional hyperparameters\\* to search for using cross-validation, and it is important to consider \\*which layers are most prone to overfitting.\\*
  > 1 What is dropout?
  >  2 Dropout is a regularization technique used in neural networks to prevent overfitting. It randomly drops out or "knocks out" units in the network on each iteration, effectively creating a smaller network.
  >
  >  3 How does dropout work as a regularizer?
  >  4 Dropout works as a regularizer by preventing units from relying too heavily on any one feature, forcing them to spread out their weights and not overfit to specific patterns in the data. This leads to a shrinking effect on the squared norm of the weights, similar to the effect of L2 regularization. In fact, dropout can be shown to be an adaptive form of L2 regularization, where the penalty on different weights varies depending on the size of the activation being multiplied into that weight.
  >
  >  5 What is the intuition behind dropout from the perspective of a single unit?
  >  6 The intuition behind dropout from the perspective of a single unit is that, for a unit to do its job, it needs to generate a meaningful output based on its inputs. However, with dropout, inputs can get randomly eliminated, meaning that any one feature could go away at random. This makes the unit reluctant to put too much weight on any one input, and instead, it spreads out its weights and gives a little bit of weight to each of the inputs. This, in turn, has a regularizing effect on the network.
  >
  >  7 How can the keep prop be varied by layer when implementing dropout?
  >  8 The keep prop, which is the chance of keeping a unit in each layer, can be varied by layer when implementing dropout. For example, in a network with three input features and seven hidden units, the first weight matrix (W1) would be 7x3, the second (W2) would be 7x7, and the third (W3) would be 3x7, and so on. The keep prop can be set to a lower value for layers where you worry more about overfitting and a higher value for layers where you worry less about overfitting. In practice, a keep prop of 1.0 is common for the input layer, where you want to keep all the features.
  >
  >  9 What are some implementation tips for using dropout?
  >  10 Some implementation tips for using dropout include:
  >  • Using dropout only if you're worried about overfitting
  >  • Varying the keep prop by layer to apply a more powerful form of dropout to layers with more parameters
  >  • Applying dropout to the input layer only if needed, with a keep prop close to 1.0
  >  • Being mindful of the hyperparameters involved in using dropout and using cross-validation to find the best values
  >  • Being aware that dropout is commonly used in computer vision applications, but it can also be used in other areas where overfitting is a concern.

  <br>

    <a id="node-566"></a>
    <p align="center"><kbd><img src="assets/12acb51f6dfc19fb380e9a681716d0087d805a1b.png" width="100%"></kbd></p>
    > Apply d**ifferent Keep-Prob cho layer khác nhau,** layer nào **nhiều
    > unit** -> **độ overfitting cao** thì cho **K.P nhỏ** (Để dropout nhiều)
    > và ngược lại.
    >
    > Hay dùng trong Computer Vision (do dễ bị overfitting)
    >
    > Downside: Đại khái là J ko còn được define tốt nữa dẫn đến **ko đo
    > lường sự giảm của J** được (trong quá trình G.D vẽ ra **learning
    > curve.** Nên đại khái ổng nói là ổng sẽ **turn off D.O để make sure J
    > giảm dần rồi sau đó mới mở lên.**
    >
    > "So you lose this **debugging tool** to have a plot a draft like this. So
    > what I usually do is **turn off drop out** or if you will **set keep-propped
    > = 1** and run my code and make sure that it is monitored quickly
    > decreasing J. And then **turn on drop out**"

    > Đại khái là vì các feature (ý là input vào một layer, chính là output của layer
    > trước) có thể biến mất tuỳ hứng nên các hidden unit nó sẽ học cách' không
    > phụ thuộc vào 1 feature nào mà sẽ **'spreading out the weights'**

    <br>

  <a id="node-567"></a>
  - 1 What is dropout?  2 Dropout is a regularization technique used in neural networks to prevent overfitting. It randomly drops out or "knocks out" units in the network on each iteration, effectively creating a smaller network.  3 How does dropout work as a regularizer?  4 Dropout works as a regularizer by preventing units from relying too heavily on any one feature, forcing them to spread out their weights and not overfit to specific patterns in the data. This leads to a shrinking effect on the squared norm of the weights, similar to the effect of L2 regularization. In fact, dropout can be shown to be an adaptive form of L2 regularization, where the penalty on different weights varies depending on the size of the activation being multiplied into that weight.  5 What is the intuition behind dropout from the perspective of a single unit?  6 The intuition behind dropout from the perspective of a single unit is that, for a unit to do its job, it needs to generate a meaningful output based on its inputs. However, with dropout, inputs can get randomly eliminated, meaning that any one feature could go away at random. This makes the unit reluctant to put too much weight on any one input, and instead, it spreads out its weights and gives a little bit of weight to each of the inputs. This, in turn, has a regularizing effect on the network.  7 How can the keep prop be varied by layer when implementing dropout?  8 The keep prop, which is the chance of keeping a unit in each layer, can be varied by layer when implementing dropout. For example, in a network with three input features and seven hidden units, the first weight matrix (W1) would be 7x3, the second (W2) would be 7x7, and the third (W3) would be 3x7, and so on. The keep prop can be set to a lower value for layers where you worry more about overfitting and a higher value for layers where you worry less about overfitting. In practice, a keep prop of 1.0 is common for the input layer, where you want to keep all the features.  9 What are some implementation tips for using dropout?  10 Some implementation tips for using dropout include:  • Using dropout only if you're worried about overfitting  • Varying the keep prop by layer to apply a more powerful form of dropout to layers with more parameters  • Applying dropout to the input layer only if needed, with a keep prop close to 1.0  • Being mindful of the hyperparameters involved in using dropout and using cross-validation to find the best values  • Being aware that dropout is commonly used in computer vision applications, but it can also be used in other areas where overfitting is a concern.
    <br>


<a id="node-568"></a>
### Other Regularization Methods

<br>

<a id="node-569"></a>
- 1 Introduction to regularization techniques in neural networks  2 \\*Data augmentation\\* as a regularization technique, including flipping and cropping images to create new examples  3 \\*Early stopping\\* as a technique to prevent overfitting by stopping the training process early  4 How early stopping works by selecting a mid-size parameter value for the neural network  5 Downside of using early stopping and \\*separating optimization and regularization\\* tasks in machine learning.
  > Sure, here's a more detailed answer, still using indexed style:
  >  1 Regularization techniques: In addition to L2 regularization and dropout, there are other techniques for reducing overfitting in neural networks. One such technique is data augmentation, which involves adding synthetic training examples to the dataset by applying random transformations to existing examples, such as flipping an image horizontally or taking random crops. This can help to make the training set less redundant and provide more variety for the model to learn from. Another technique is early stopping, which involves monitoring the validation error as the model is trained and stopping the training process when the error stops improving or starts to increase. This can help to prevent the model from overfitting to the training data by finding the best point at which to stop training.
  >
  > 2 Data augmentation: Data augmentation is a technique for creating additional training examples by applying random transformations to existing examples in the dataset. For example, flipping an image horizontally or taking random crops can help to provide more variety for the model to learn from. This technique can be especially useful when it's difficult or expensive to obtain more data. However, it's important to use transformations that are relevant to the problem at hand, such as flipping a cat image horizontally but not vertically.
  >
  > 3 Early stopping: Early stopping is a technique for preventing overfitting by monitoring the validation error as the model is trained and stopping the training process when the error stops improving or starts to increase. This helps to find the best point at which to stop training and prevent the model from overfitting to the training data. However, it's important to be aware of the potential downsides of early stopping, such as the need to choose an appropriate stopping point and the potential for increased computational cost.
  >
  > 4 Choosing regularization techniques: When choosing regularization techniques for a neural network, it's important to consider the trade-off between reducing bias and reducing variance. L2 regularization can help to reduce variance by penalizing large weights, while dropout can help to reduce variance by randomly dropping out units during training. Data augmentation can also help to reduce variance by providing more variety for the model to learn from. On the other hand, early stopping can help to reduce variance by finding the best point at which to stop training, but may also increase bias if the model is not allowed to train for long enough.
  >
  > 5 Separating optimization and regularization: One approach to machine learning is to separate the tasks of optimization and regularization. In this approach, the focus is on finding the best values of the weights and biases that minimize the cost function, without considering methods for reducing overfitting. After optimizing the cost function, regularization techniques such as L2 regularization, dropout, or data augmentation can be applied to reduce overfitting. This can simplify the process of choosing among the space of possible algorithms and hyperparameters, making machine learning easier to understand and implement.

  <br>

    <a id="node-570"></a>
    <p align="center"><kbd><img src="assets/38a2d25e2506d782bcb5828754d56f556348f2ad.png" width="100%"></kbd></p>
    > Đại khái là tạo thêm data thì sẽ giảm Overfitting

    <br>

    <a id="node-571"></a>
    <p align="center"><kbd><img src="assets/1d53288b55fd7b427b35a663474d761462193acd.png" width="100%"></kbd></p>
    > **Early stoping:**Pros**: Chỉ chạy G.D rồi quyết định stop để lấy ra W.b
    > Cons: V**i phạm phương pháp MỖI LẦN 1 VIỆC - 
    > **Orthogonalization**: Tức là Tập trung giảm J hoặc tập trung 
    > giảm Overfitting -> Nó phải hy sinh việc tìm ra W, b sao cho J min 
    > để đánh đổi việc không bị overfitting
    >
    > **L2_Reg** 
    > Pros Cứ Train cho đã đời mà ko sợ (Overfiting)
    > Cons: là phải chọn **lambda** -> More computational expensive

    <br>

  <a id="node-572"></a>
  - Sure, here's a more detailed answer, still using indexed style:  1 Regularization techniques: In addition to L2 regularization and dropout, there are other techniques for reducing overfitting in neural networks. One such technique is data augmentation, which involves adding synthetic training examples to the dataset by applying random transformations to existing examples, such as flipping an image horizontally or taking random crops. This can help to make the training set less redundant and provide more variety for the model to learn from. Another technique is early stopping, which involves monitoring the validation error as the model is trained and stopping the training process when the error stops improving or starts to increase. This can help to prevent the model from overfitting to the training data by finding the best point at which to stop training.  2 Data augmentation: Data augmentation is a technique for creating additional training examples by applying random transformations to existing examples in the dataset. For example, flipping an image horizontally or taking random crops can help to provide more variety for the model to learn from. This technique can be especially useful when it's difficult or expensive to obtain more data. However, it's important to use transformations that are relevant to the problem at hand, such as flipping a cat image horizontally but not vertically.  3 Early stopping: Early stopping is a technique for preventing overfitting by monitoring the validation error as the model is trained and stopping the training process when the error stops improving or starts to increase. This helps to find the best point at which to stop training and prevent the model from overfitting to the training data. However, it's important to be aware of the potential downsides of early stopping, such as the need to choose an appropriate stopping point and the potential for increased computational cost.  4 Choosing regularization techniques: When choosing regularization techniques for a neural network, it's important to consider the trade-off between reducing bias and reducing variance. L2 regularization can help to reduce variance by penalizing large weights, while dropout can help to reduce variance by randomly dropping out units during training. Data augmentation can also help to reduce variance by providing more variety for the model to learn from. On the other hand, early stopping can help to reduce variance by finding the best point at which to stop training, but may also increase bias if the model is not allowed to train for long enough.  5 Separating optimization and regularization: One approach to machine learning is to separate the tasks of optimization and regularization. In this approach, the focus is on finding the best values of the weights and biases that minimize the cost function, without considering methods for reducing overfitting. After optimizing the cost function, regularization techniques such as L2 regularization, dropout, or data augmentation can be applied to reduce overfitting. This can simplify the process of choosing among the space of possible algorithms and hyperparameters, making machine learning easier to understand and implement.
    <br>


<a id="node-573"></a>
## Setting Up Your Optimization Problem

<br>


<a id="node-574"></a>
### Normalizing Inputs

<br>

<a id="node-575"></a>
- 1 \\*Normalizing inputs\\* can \\*speed up\\* neural network training.  2 The normalization process involves \\*subtracting the mean\\* and \\*normalizing the variances\\* of the input features.  3 It is important to \\*use the same normalization parameters\\* for both \\*training\\* and \\*test\\* sets.  4 Normalizing input features helps to ensure that the\\* cost function\\* is more \\*symmetric\\* and \\*easier to optimize\\*.  5 Features should be on \\*similar scales\\* to avoid \\*elongated cost functions\\* and \\*slow gradient descent\\*.  6 Normalizing features is especially important when the \\*input features\\* come from \\*dramatically different scales.\\*  7 Normalization generally \\*does not harm performance\\*, and is often \\*beneficial in speeding up\\* training.  8 There are other techniques to speed up neural network training that will be discussed in the next section.
  > ure, here's a more detailed answer:
  >
  >  1 Normalizing Inputs: When training a neural network, one technique to speed up the training is to normalize your inputs. This involves two steps:
  >
  >  2 a. Subtract out or zero out the mean: This step involves calculating the mean of the input features using the formula mu = 1/m * sum(x_i) and subtracting it from each training example, so x_i becomes x_i - mu.
  >
  >  3 b. Normalize the variances: In this step, the variance of each feature is calculated using the formula sigma^2 = 1/m * sum(x_i^2) and then each example is divided by this vector sigma. This ensures that each feature has equal variance and results in a more symmetric cost function.
  >
  >  4 Importance of Normalizing Inputs: Normalizing inputs is important because if the features are on very different scales, it's more likely that the cost function will be elongated and the parameters will take on very different values. This results in a more difficult optimization problem, and the gradient descent algorithm may take a lot of steps before it finds the minimum. Normalizing the inputs ensures that the cost function is more symmetric, and gradient descent can go straight to the minimum without oscillating around.
  >
  >  5 When to Normalize Inputs: Normalizing inputs is particularly important when the features come from very different scales, such as one feature ranging from 1-1000 and another from 0-1. However, performing this type of normalization typically doesn't harm the training algorithm, and it's often done regardless of the feature scales. If the features come in on similar scales, such as all ranging from -1 to 1, then this step is less important, but it can still be helpful in speeding up training.
  >
  > 6 Consistency in Normalization: When normalizing the training data, it's important to use the same mu and sigma to normalize the test set. This ensures that the data goes through the same transformation, and the test set is scaled in the same way as the training set.
  >
  >  7 Other Techniques to Speed up Training: There are other techniques to speed up training of neural networks, such as:
  >  8 a. Using an appropriate learning rate
  >  9 b. Using early stopping to prevent overfitting
  >  10 c. Regularization to prevent overfitting
  >  11 d. Using dropout to prevent overfitting
  >  12 e. Using batch normalization to stabilize training
  >  13 f. Using a better optimization algorithm such as Adam, RMSProp, or Adagrad.

  <br>

    <a id="node-576"></a>
    <p align="center"><kbd><img src="assets/af2aa0352e6760a3933aaf9bc3f0bd6ac1d572b2.png" width="100%"></kbd></p>
    <br>

    <a id="node-577"></a>
    <p align="center"><kbd><img src="assets/4b866c80378462d107522c7ed604762112bbed10.png" width="100%"></kbd></p>
    <br>

  <a id="node-578"></a>
  - ure, here's a more detailed answer:  1 Normalizing Inputs: When training a neural network, one technique to speed up the training is to normalize your inputs. This involves two steps:  2 a. Subtract out or zero out the mean: This step involves calculating the mean of the input features using the formula mu = 1/m * sum(x_i) and subtracting it from each training example, so x_i becomes x_i - mu.  3 b. Normalize the variances: In this step, the variance of each feature is calculated using the formula sigma^2 = 1/m * sum(x_i^2) and then each example is divided by this vector sigma. This ensures that each feature has equal variance and results in a more symmetric cost function.  4 Importance of Normalizing Inputs: Normalizing inputs is important because if the features are on very different scales, it's more likely that the cost function will be elongated and the parameters will take on very different values. This results in a more difficult optimization problem, and the gradient descent algorithm may take a lot of steps before it finds the minimum. Normalizing the inputs ensures that the cost function is more symmetric, and gradient descent can go straight to the minimum without oscillating around.  5 When to Normalize Inputs: Normalizing inputs is particularly important when the features come from very different scales, such as one feature ranging from 1-1000 and another from 0-1. However, performing this type of normalization typically doesn't harm the training algorithm, and it's often done regardless of the feature scales. If the features come in on similar scales, such as all ranging from -1 to 1, then this step is less important, but it can still be helpful in speeding up training.  6 Consistency in Normalization: When normalizing the training data, it's important to use the same mu and sigma to normalize the test set. This ensures that the data goes through the same transformation, and the test set is scaled in the same way as the training set.  7 Other Techniques to Speed up Training: There are other techniques to speed up training of neural networks, such as:  8 a. Using an appropriate learning rate  9 b. Using early stopping to prevent overfitting  10 c. Regularization to prevent overfitting  11 d. Using dropout to prevent overfitting  12 e. Using batch normalization to stabilize training  13 f. Using a better optimization algorithm such as Adam, RMSProp, or Adagrad.
    <br>


<a id="node-579"></a>
### Vanishing / Exploding Gradients

<br>

<a id="node-580"></a>
- 1 The problem of data \\*vanishing\\* and \\*exploding\\* gradients in deep neural networks  2 The effect of \\*weight initialization\\* on the vanishing and exploding gradients  3 Mathematical explanation of the effect of weight initialization on the output Y and activations A  4 The intuition behind the \\*exponential increase\\* or \\*decrease\\* of activations with a very deep network  5 The similar exponential increase or decrease of gradients as \\*a function of the number of layers\\*  6 The difficulty of training when gradients are exponentially smaller or larger than L  7 The partial solution to the problem of vanishing and exploding gradients: \\*careful choice of weight initialization\\*
  > 1 The problem of vanishing and exploding gradients: When training a very deep neural network, the derivatives or slopes of the network can sometimes get very small or very large, making training difficult. This is known as the problem of vanishing and exploding gradients.
  >  2 Weight initialization and its impact on the problem: Careful choices of random weight initialization can significantly reduce the problem of vanishing and exploding gradients.
  >  3 The structure of a neural network: A neural network has layers and hidden units, and each layer has weight matrices W1, W2, W3, etc. The output Y is the result of a multiplication of all the weight matrices and the input X.
  >  4 Linear activation function and biases: In the video, the activation function used is a linear function and the bias is ignored to simplify the calculation.
  >  5 The impact of weight matrices on activations: If each weight matrix is slightly larger than 1 times the identity matrix, the activations will increase exponentially as a function of the number of layers L. On the other hand, if each weight matrix is slightly smaller than the identity matrix, the activations will decrease exponentially.
  >  6 The impact of weight matrices on gradients: The same argument can be used to show that the derivatives or gradients of the network will also increase or decrease exponentially as a function of the number of layers.
  >  7 The difficulty of training deep networks: If the activations or gradients increase or decrease exponentially as a function of the number of layers, it can make training difficult, especially if the gradients become exponentially smaller than L.
  >  8 Partial solution to the problem: Careful choice of weight initialization can help to alleviate the problem of vanishing and exploding gradients, but it doesn't completely solve the problem.
  >  9 Importance of weight initialization: Weight initialization is an important aspect of training neural networks and can have a significant impact on the success of the training.
  >  10 Conclusion: Vanishing and exploding gradients can be a significant problem when training deep neural networks, but careful weight initialization can help to mitigate the problem.

  <br>

    <a id="node-581"></a>
    <p align="center"><kbd><img src="assets/5d0b7012fa73bc5216e8ecb3210be504773965f5.png" width="100%"></kbd></p>
    > **Vanishing and Exploding Gradients:**
    > Chữ **gradient** ý muốn nói 'Sự thay đổi của the output of the model
    > do sự thay đổi của tham số' (the change in the output of a model 
    > with respect to a change in its weights)
    >
    > **Vanishing** **gradient** ý nói khi gradient quá nhỏ khiến cho model
    > update rất chậm, khiến quá trình training rất chậm thậm chí dừng
    > luôn.
    >
    > **Exploding** **gradient** thì ngược lại, khiến model update quá nhanh, 
    > khiến kết quả không stable.
    >
    > Một số giải pháp là dùng hàm activation khác như **Relu, Tanh** và **initialization**

    > I - Identity matrix **[1 0; 0 1]**
    >
    > Đại khái ổng giả sử 1 NN như vầy, coi như không dùng activation function
    > - g(z) = z và bỏ qua b giả thì triển khai ra  được y^ là = W[L] (W[L-1]**(L-1))X  (giả sử thêm W của
    > hidden unit bằng nhau)
    >
    > Ý muốn nói có nghĩa là y^ sẽ là một function theo số mũ L Từ đó nếu W của hidden unit nhỏ hơn
    > Identity matrix 1 chút ví dụ như 0.5 0; 0 0,5 thì y^ sẻ nhỏ đi theo cấp luỹ thừa của L tức là sẽ rất rất
    > nhỏ
    >
    > Ngược lại nếu W của hidden unit lớn hơn một chút, thì y^ sẽ lớn theo cấp luỹ thừa
    >
    > Thì ý ổng là tương tự như như ở đây lấy việc **tính activation qua các layer** ra để minh hoạ thì với
    > g**radient nó cũng vậy**, từ đó tạo ra hiện tượng **exploding gradient** và **vanishing gradient**

    <br>

    <a id="node-582"></a>
    <p align="center"><kbd><img src="assets/d7ebe222edc7545580ca85343a69e767a0f63a5e.png" width="100%"></kbd></p>
    <br>

  <a id="node-583"></a>
  - 1 The problem of vanishing and exploding gradients: When training a very deep neural network, the derivatives or slopes of the network can sometimes get very small or very large, making training difficult. This is known as the problem of vanishing and exploding gradients.  2 Weight initialization and its impact on the problem: Careful choices of random weight initialization can significantly reduce the problem of vanishing and exploding gradients.  3 The structure of a neural network: A neural network has layers and hidden units, and each layer has weight matrices W1, W2, W3, etc. The output Y is the result of a multiplication of all the weight matrices and the input X.  4 Linear activation function and biases: In the video, the activation function used is a linear function and the bias is ignored to simplify the calculation.  5 The impact of weight matrices on activations: If each weight matrix is slightly larger than 1 times the identity matrix, the activations will increase exponentially as a function of the number of layers L. On the other hand, if each weight matrix is slightly smaller than the identity matrix, the activations will decrease exponentially.  6 The impact of weight matrices on gradients: The same argument can be used to show that the derivatives or gradients of the network will also increase or decrease exponentially as a function of the number of layers.  7 The difficulty of training deep networks: If the activations or gradients increase or decrease exponentially as a function of the number of layers, it can make training difficult, especially if the gradients become exponentially smaller than L.  8 Partial solution to the problem: Careful choice of weight initialization can help to alleviate the problem of vanishing and exploding gradients, but it doesn't completely solve the problem.  9 Importance of weight initialization: Weight initialization is an important aspect of training neural networks and can have a significant impact on the success of the training.  10 Conclusion: Vanishing and exploding gradients can be a significant problem when training deep neural networks, but careful weight initialization can help to mitigate the problem.
    <br>


<a id="node-584"></a>
### Weight Initialization For Deep Networks

<br>

<a id="node-585"></a>
- 1 Problem of vanishing and exploding gradients in very deep neural networks  2 Partial solution is a better or more \\*careful choice of random initialization\\* for the neural network  3 Example of initializing weights for a single neuron  4 Generalizing to deep networks  5 Setting \\*variance of weights\\* to \\*prevent z from blowing up\\* or becoming \\*too small\\*  6 Setting weight matrix W for a certain layer to \\*np.random.randn\\* times \\*square root of 1 over the number of features\\* that are fed into each neuron in layer l  7 Using a variance of \\*2/n\\* for \\*ReLu\\* activation function, and \\*1/n\\* for TanH activation function  8 Different initialization formulas: \\*Xavier\\* initialization and \\*Yoshua Bengio's\\* formula  9 The \\*variance\\* parameter can be tuned with \\*hyperparameters\\*  10 Importance of choosing a\\* reasonable scaling for weight initialization\\* to avoid exploding or vanishing gradients  11 The trick can help neural networks trained much more quickly
  > Sure, here is a more detailed summary of the video:
  >  1 The video discusses the problem of vanishing and exploding gradients in deep neural networks, where the gradients of the loss function with respect to the weights become either too small or too large, leading to slow or unstable learning.
  >  2 One partial solution to this problem is to use better weight initialization techniques, which can help control the scale of the activations and gradients throughout the network.
  >  3 To understand weight initialization, the video starts with the example of a single neuron, where the input features are multiplied by weights and summed up to produce an activation value, which is then passed through an activation function to produce an output.
  >  4 To prevent the activation values from becoming too large or too small, it is desirable to set the variance of the weights to an appropriate value. In particular, if the number of input features is large, the weights should be scaled down by a factor proportional to the square root of the number of input features, in order to keep the activation value from growing too large.
  >  5 For a deep neural network with multiple layers, the same principle applies, but with the number of input features replaced by the number of units in the previous layer. Specifically, the variance of the weights for each layer should be scaled down by a factor proportional to the square root of the number of units in the previous layer.
  >  6 The video notes that this initialization technique works particularly well with ReLU activation functions, and that a scaling factor of 2/n (rather than 1/n) should be used for ReLU in order to achieve better performance.
  >  7 Other activation functions may require different initialization techniques. For example, the Tanh activation function may require a scaling factor of 1/sqrt(n) instead of 2/sqrt(n), which is known as the Xavier initialization.
  >  8 In practice, the variance of the weights can be adjusted by a hyperparameter, which can be tuned to achieve better performance on a particular task.
  >  9 Overall, weight initialization is an important technique for improving the stability and efficiency of deep learning, and should be carefully considered when designing and training deep neural networks.

  <br>

    <a id="node-586"></a>
    <p align="center"><kbd><img src="assets/3a4290b4cc54fc96801dddaf514cbe2fd9277262.png" width="100%"></kbd></p>
    > Đại khái là ini weight randomly nhưng nhân thêm (element-wise) với:
    >
    > random(...)*sqrt(**2/số feature = unit của layer trước**)  (**2/fan_in**)
    >
    > thì cái này có tên là **He (hoặc Klaiming) - initialization**, work tốt 
    > với reLU, LeakyReLU, ELU, GELU, Swish, Mish.. 
    > Do ông **Kaiming He** phát minh (Ageron p.360)
    >
    > Nếu activation là None, tanh, softmax thì dùng Glorot /Xavier initilization:
    > thay term trong sqrt bằng **1/fan_average**
    >
    > với fan là chỉ số feature vào hoặc ra một layer:
    > nên fan_average là 0.5(số unit layer trước + số unit layer này)
    >
    > Chỗ này ông Andrew bị nhầm, Xavier phải là 1/fan_avg = 2/(n[l-1]+n[l])
    > mới đúng ổng chỉ cái trên là sai.
    >
    > Cái trên **1/fan_in** là **LeCun** initialization work tốt đv **SELU** (Ageron)

    > Nói chung là các công thức ini He/Kaiming - Glorot / Xavier - LeCun khác nhau
    > chút đỉnh ở cái term trong dấu sqrt và mỗi cái sẽ work tốt tuỳ activation function.

    <br>

  <a id="node-587"></a>
  - Sure, here is a more detailed summary of the video:  1 The video discusses the problem of vanishing and exploding gradients in deep neural networks, where the gradients of the loss function with respect to the weights become either too small or too large, leading to slow or unstable learning.  2 One partial solution to this problem is to use \\*better weight initialization techniques\\*, which can help \\*control the scale\\* of the \\*activations\\* \\*and\\* \\*gradients\\* throughout the network.  3 To understand weight initialization, the video starts with the example of a single neuron, where the input features are multiplied by weights and summed up to produce an activation value, which is then passed through an activation function to produce an output.  4 To prevent the activation values from becoming too large or too small, it is desirable to \\*set the variance of the weights to an appropriate value\\*. In particular, if the number of input features is large, the weights should be \\/\\*scaled down by a factor proportional to the square root of the number of input features\\*\\/, in order to keep the activation value from growing too large.  5 For a \\*deep neural network\\* with multiple layers, the same principle applies, but with the number of input features replaced by the \\*number of units in the previous layer\\*. Specifically, the variance of the weights for each layer should be \\/\\*scaled down by a factor proportional to the square root of the number of units in the previous layer.\\*\\/  6 The video notes that this initialization technique works particularly well with \\*ReLU\\* activation functions, and that a scaling factor of 2/n (rather than 1/n) should be used for ReLU in order to achieve better performance.  7 \\*Other activation functions\\* may require different initialization techniques. For example, the \\*Tanh\\* activation function may require a \\*scaling factor of 1/sqrt(n) instead of 2/sqrt(n)\\*, which is known as the \\*Xavier initialization\\*.  8 In practice, the \\*variance of the weights \\*can be \\*adjusted by a hyperparameter\\*, which can be \\*tuned\\* to achieve better performance on a \\*particular task.\\*  9 Overall, \\*weight initialization\\* is an important technique for improving the \\*stability\\* and \\*efficiency\\* of deep learning, and should be carefully considered when designing and training deep neural networks.
    <br>


<a id="node-588"></a>
### Numerical Approximation Of Gradients

<br>

<a id="node-589"></a>
- 1 Backpropagation implementation requires testing to ensure correctness  2 Numerically approximating computations of gradients helps build up to gradient checking  3 Two-sided difference gives a better approximation of the gradient than a one-sided difference  4 Formal definition of a derivative is f of theta plus epsilon minus f of theta minus epsilon over 2 epsilon  5 Error of approximation is on the order of epsilon squared for the formal definition and on the order of epsilon for the two-sided difference  6 Two-sided difference is preferred for gradient checking, even though it runs twice as slow as one-sided difference
  > 1 When implementing backpropagation, it's important to check that your implementation is correct.
  >  2 One way to do this is through gradient checking, which involves approximating the gradient of a function numerically.
  >  3 To approximate the gradient, you can nudge the input variable (e.g. theta) by a small amount (e.g. epsilon) to get two new values of the function (f(theta+epsilon) and f(theta-epsilon)).
  >  4 You can then compute the height of a larger triangle using these two values, which provides a more accurate estimate of the gradient.
  >  5 This method involves taking a two-sided difference, rather than a one-sided difference, which leads to greater accuracy in the approximation.
  >  6 The approximation error for the two-sided difference is on the order of epsilon squared, which is much smaller than the error for the one-sided difference (which is on the order of epsilon).
  >  7 When doing gradient checking, it's important to use the more accurate two-sided difference method, even though it may be slower.
  >  8 The formal definition of the derivative involves taking the limit of the difference quotient as epsilon approaches zero.
  >  9 The approximation error for a non-zero value of epsilon is on the order of epsilon squared.
  >  10 The two-sided difference method involves computing f(theta+epsilon) and f(theta-epsilon), which provides a better approximation of the gradient and reduces the approximation error.

  <br>

    <a id="node-590"></a>
    <p align="center"><kbd><img src="assets/c1ff1c0f8d19e4bc2b2b978a518a3e590fe5f3e2.png" width="100%"></kbd></p>
    > Khúc cuối ổng nói đại khái là vầy, có 2 cách tính gần đúng 
    > giá trị (**dJ/dθ**) để thực hiện việc Gradient Checking - So sánh giá
    > trị gần đúng của dJ/dθ (or dJ/dw, dJ/db) với kết quả của 
    > Gradient descent để đảm bảo G.D đang chạy đúng )
    >
    > Thì dùng '**2 side difference approximation**' sẽ chính xác hơn 
    > là **1-side difference approximation**

    > Đại khái là check xem (trong quá trình backprop) gradient
    > mình tính có đúng không (đây là đ.v việc tự backprop chứ
    > làm bằng Keras thì khỏi bàn)
    > Cách làm là so sánh dJ/dtheta với 'gần đúng của dJ/dtheta) tính bằng
    > [ J(theta+epsilon)-J(theta-epsilon) ] / 2*epsilon
    >
    > Ổng lấy ví dụ hàm J(theta) = theta***3 -> dJ/dtheta = 3*theta**2
    > thì giả dụ với theta = 1 thì tính bằng gần đúng sẽ ra
    > 3.0001 gần bằng với 3*1**2 = 3.
    >
    > Đại khái là ổng minh hoạ việc tính ra term gần đúng của dj/dtheta
    > sẽ gần bằng dj/dtheta lúc Backprop.
    >
    > Còn về cách tính thì nhìn hình là hiểu:
    > dJ/dtheta (derivative / đạo hàm của hàm J w.r.t theta) chính là hệ số
    > góc của tiếp tuyến với hàm J tại theta (=tang của góc bởi tiếp tuyến
    > và phương ngang) -> thì góc này có thể tính gần đúng bằng
    > góc dưới của tam giác màu xanh lá.

    <br>

    <a id="node-591"></a>
    <p align="center"><kbd><img src="assets/af6d2450293ee85e67a4f5d8d2ad9b643b503fae.png" width="100%"></kbd></p>
    > Đại khái là 1 cái thì error giảm (về không) với 1 tốc
    > độ tỉ lệ thuận với bình phương của epsilon nên
    > nhanh hơn cái kia chỉ tỉ lệ thuận với epsilon nên
    > cái đầu chính xác hơn

    <br>

  <a id="node-592"></a>
  - 1 When implementing \\*backpropagation\\*, it's important to \\*check that your implementation is correct.\\*  2 One way to do this is through\\* gradient checking\\*, which involves \\*approximating the gradient of a function numerically\\*.  3 To approximate the gradient, you can \\*nudge\\* the\\* input variable\\* (e.g. \\*theta\\*) by a \\*small amount\\* (e.g. \\*epsilon\\*) to get two new values of the function (\\*f(theta+epsilon) and f(theta-epsilon)\\*).  4 You can then compute the height of a larger triangle using these two values, which provides a more accurate estimate of the gradient.  5 This method involves taking a\\* two-sided difference\\*, rather than a \\*one-sided difference\\*, which leads to \\*greater accuracy\\* in the approximation.  6 The approximation \\*error for the two-sided difference\\* is on the order of \\*epsilon squared\\*, which is much smaller than the \\*error for the one-sided difference\\* (which is on the order of \\*epsilon\\*).  7 When doing gradient checking, it's important to use the more accurate two-sided difference method, even though it may be slower.  8 The formal definition of the derivative involves taking the limit of the difference quotient as epsilon approaches zero.  9 The approximation error for a non-zero value of epsilon is on the order of epsilon squared.  10 The two-sided difference method involves computing f(theta+epsilon) and f(theta-epsilon), which provides a \\*better approximation of the gradient\\* and \\*reduces the approximation error.\\*
    <br>


<a id="node-593"></a>
### Gradient Checking

<br>

<a id="node-594"></a>
- 1 Gradient checking is a technique to debug and verify the correctness of back propagation implementations in neural networks.  2 To implement gradient checking, the first step is to \\*reshape all the network parameters into a giant vector theta. \\* 3 The cost function J is then expressed as a \\*function of theta.\\*  4 Next, all the \\*derivatives\\* of the cost function with respect to the network \\*parameters\\* are also \\*reshaped into a giant vector d theta\\*.  5 To perform gradient checking, a \\*loop\\* is implemented for \\*each component of theta\\*, where a two-sided difference is taken for each component of theta.  6 The \\*difference is then divided by 2 epsilon\\* to \\*approximate\\* the partial derivative of J with respect to that component of theta.  7 The approximation for each component is then computed for every value of i.  8 The d\\*ifference between the approximation and the actual derivative\\* is then computed u\\*sing the Euclidean distance formula\\*.  9 If the \\*difference is very smal\\*l (i.e., less than\\* 10^-7\\*), the derivative approximation is l\\*ikely correct.\\*  10 If the difference is larger, it is possible that there is a bug in the implementation, and the individual components of d theta should be checked to locate the source of the problem.
  > Sure, I'd be happy to provide a more detailed answer for you!
  >  1 Gradient checking is a technique used to debug and verify the implementation and backpropagation process in a neural network. It can save a lot of time and help identify bugs in implementations.
  >  2 To implement gradient checking, the first step is to take all the network parameters, such as W1, B1, etc., and reshape them into a giant parameter vector called theta. This involves reshaping all the W's into vectors and concatenating them with the other parameters.
  >  3 Next, the cost function J is transformed into a function of theta. The derivatives, such as dW[1], db[1], etc., are then reshaped into a giant vector called d theta.
  >  4 To implement gradient checking, a loop is used to compute d theta approx i for each component of theta. This involves taking a two-sided difference of J of theta by nudging theta i up and down by a small amount (epsilon) and computing the difference between these values.
  >  5 The two resulting vectors, d theta approx and d theta, are then compared to check if they are approximately equal. This is done by computing the Euclidean distance between the vectors and normalizing it by the lengths of the vectors.
  >  6 A good value for epsilon is around 10^-7, and if the formula gives a value of 10^-7 or smaller, the derivative approximation is likely correct. If it is around 10^-5, it's worth double-checking the components of the vector. If it is larger than 10^-3, there may be a bug somewhere, and it's important to investigate individual components of d theta to try and track down the source of the problem.
  > Overall, gradient checking is an important technique for debugging and verifying neural network implementations, and can help save time and prevent bugs in the backpropagation process.

  <br>

    <a id="node-595"></a>
    <p align="center"><kbd><img src="assets/0bf9fbbaedcc03a548d1b7c5a661d8743bad538e.png" width="100%"></kbd></p>
    <br>

    <a id="node-596"></a>
    <p align="center"><kbd><img src="assets/bd4d7424cd6ab1ed57c0f7993a4bfb8362bf6446.png" width="100%"></kbd></p>
    > Đại khái là dùng '2-side difference approximation' để tính ra vector
    > **d(θ_approx)** rồi so sánh xem nó có **gần bằng** với **d(θ)**
    > hay không
    >
    > Check bằng công thức trong hình.

    > "So when implementing a neural network, what often happens is 
    > I'll implement foreprop, implement backprop. And then I might find 
    > that this grad check has a relatively **big value**. And then I will 
    > suspect that there **must be a bug**, go in **debug, debug, debug**. 
    > And after debugging for a while, If I find that it **passes grad 
    > check with a small value**, then you can be much **more 
    > confident** that it's then correct."

    > Loop trong vector **Θ** chứa toàn bộ params **θ_i**, để tính  **dθ_i
    > approx** - giá trị approximation của dJ w.r.t từng θ_i,  mỗi cái tính bằng
    > công thức đã biết:
    >
    > **dθ_i = [J(θ_i + epsilon) - J(θ_i - epsilon)] / 2*epsilon**
    >
    > Bỏ vào để ra vector **dΘ_approx**
    >
    > So sánh: Không phải là so từng cái mà là so cả vector **dΘ_approx** với
    > **dΘ** (cái này là từ backprop) bằng cách dùng **Euclidean norm** (còn
    > gọi là L2 norm) của **hiệu 2 vector này**. 
    >
    > Tức là tính norm của **dΘ_approx - dΘ**
    >
    > Công thức tính L2 norm là bằng square root của tổng bình phương các
    > element trong vector.
    >
    > Với cách tính này kiểu như **sqrt của tổng bình phương các sai  lệch**
    > giữa **dθ_i approx** và **dθ_i** vậy
    >
    > So sánh sai lệch này nếu nhỏ hơn 10^-7 thì ok tự tin là tính derivative
    > đúng

    <br>

    <a id="node-597"></a>
    <p align="center"><kbd><img src="assets/2a121a4d874cb2a12bfbcbafbe8cd01174ccfddc.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/2a121a4d874cb2a12bfbcbafbe8cd01174ccfddc.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/e9f43c1e58d04a6f02db0232e471411b7ea1af11.png" width="100%"></kbd></p>
    <br>

  <a id="node-598"></a>
  - Sure, I'd be happy to provide a more detailed answer for you!  1 Gradient checking is a technique used to debug and verify the implementation and \\*backpropagation\\* process in a neural network. It can \\*save a lot of time\\* and help identify bugs in implementations.  2 To implement gradient checking, the first step is to \\*take all the network parameters\\*, such as W1, B1, etc., and \\*reshape them into a giant parameter vector called theta\\*. This involves \\*reshaping all the W's into vectors\\* and \\*concatenating\\* them with the other parameters.  3 Next, the \\*cost function J is transformed into a function of theta\\*. The derivatives, such as dW[1], db[1], etc., are then \\*reshaped into a giant vector called d theta\\*.  4 To implement gradient checking, \\*a loop\\* is used to compute \\*d theta approx I\\* for each component of theta. This involves taking a two-sided difference of J of theta by nudging theta I up and down by a small amount (epsilon) and computing the difference between these values.  5 The two resulting vectors, \\*d theta approx\\* and \\*d theta\\*, are then compared to check if they are approximately equal. This is done by computing the \\*Euclidean distance between the vectors\\* and \\*normalizing it by the lengths of the vectors\\*.  6 A good value for \\*epsilon\\* is around \\*10^-7\\*, and if the formula gives a value of 10^-7 or smaller, the derivative approximation is likely correct. \\*If it is around 10^-5, it's worth double-checking the components of the vector\\*. If it is l\\*arger than 10^-3\\*, there may be a \\*bug somewhere\\*, and it's important to investigate individual components of d theta to try and track down the source of the problem. Overall, gradient checking is an important technique for debugging and verifying neural network implementations, and can help save time and prevent bugs in the backpropagation process.
    <br>


<a id="node-599"></a>
### Gradient Checking Implementation Notes

<br>

<a id="node-600"></a>
- 1 Gradient checking is a \\*useful tool for debugging\\* neural networks.  2 Grad check \\*should not be used during training\\*, only for \\*debugging\\*.  3 If an algorithm \\*fails grad check\\*, look at \\*individual components to identify the bug.\\*  4 Remember to \\*include regularization when using grad check.\\*  5 \\*Dropout\\* is difficult to use with \\*grad check because of its randomness\\*.  6 \\*Turn off dropout\\* when using \\*grad chec\\*k to double check correctness.  7 It is possible that implementation of backpropagation is \\*correct\\* \\*only when weights and biases are close to 0\\*.  8 It is recommended to \\*run grad check\\* at \\*random initialization\\* and \\*after some training\\*.  9 Week 1 materials covered setting up train, dev, and test sets, analyzing bias and variance, regularization, and gradient checking.  10 The programming exercise in week 1 will allow for the application of these concepts.
  > 1 In this video, the speaker shares some practical tips and notes on implementing gradient checking for a neural network.
  >  2 One of the tips is to only use gradient checking for debugging and not during training. This is because computing d theta approx i for all values of i is a slow computation. Instead, backprop should be used to compute d theta for implementing gradient descent.
  >  3 If an algorithm fails grad check, the speaker advises to look at the individual components to identify the bug. By examining the different values of i, the location of the bug can be determined. For example, if the values of theta or d theta are very far off, all corresponding to dbl for some layer, the bug might be in how the derivative with respect to parameters b is being computed.
  >  4 Another tip is to remember the regularization term when doing grad check. If regularization is being used in the cost function, it's important to include that term in the calculation of d theta.
  >  5 Dropout cannot be easily checked with grad check because in every iteration, dropout randomly eliminates different subsets of hidden units. This makes it difficult to compute the cost function J that dropout is doing gradient descent on. Therefore, grad check should be implemented without dropout, and dropout should be turned on afterwards.
  >  6 It's possible that the implementation of backprop may be correct only when w and b are close to 0 and become more inaccurate as w and b become larger. To address this, the speaker suggests running grad check at random initialization and then training the network for a while before running grad check again.
  >  7 Overall, the video covers a range of topics, including setting up train, dev, and test sets, analyzing bias and variance, applying different forms of regularization, and gradient checking. These concepts are further elaborated in the week's programming exercise.

  <br>

    <a id="node-601"></a>
    <p align="center"><kbd><img src="assets/0c81619bb0868d442a47fcbdd5056adb2880cadd.png" width="100%"></kbd></p>
    > Đại khái là so sánh thấy sai khác lớn là biết có bug rồi
    > thì bấy giờ ta sẽ **xem xét đơn lẻ dw, db so với dθ [i]**
    > Giả sử thấy dw thì gần bằng còn db thì khác chứng tỏ sai
    > đâu đó chỗ db. Nói chung là nó sẽ giúp **khoanh vùng bug**Nhớ add **Regularization** term khi tính J (tính J để tính 
    > numerical_gradient)
    >
    > **Tắt Dropout** khi làm Gradient Checking vì nó khiến 
    > tính toán J sai. Làm G.C xong thì bật lên lại

    > "It is not impossible, rarely happens, but it's not impossible
    > that  your implementation of gradient descent is **correct
    > when w and b  are close to 0, so at random initialization**.
    > But that as you run  gradient descent and w and b become
    > bigger, maybe your  implementation of backprop is correct
    > only when w and b is  close to 0, but it **gets more inaccurate
    > when w and b become large**. So one thing you could do, I
    > don't do this very often, but one thing  you could do is **run
    > grad check at random initialization** and then  train the
    > network for a while so that w and b have some time  to
    > wander away from 0, from your small random initial values. "
    >
    > Đại khái là có thể (dù hiếm) xảy ra là back-prop chạy đúng
    > khi W, b nhỏ ~0 còn khi nó lớn hơn 0 thì lại sai. Do đó ý ổng
    > nói là ồng hay run grad check khi ini xong  rồi train một thời
    > gian cho w, b nó thay đổi khỏi 0 thì grad-check lại

    <br>

    <a id="node-602"></a>
    <p align="center"><kbd><img src="assets/f6c261ed638456324c156dfeb334bf75db461b6a.png" width="100%"></kbd></p>
    <br>

    <a id="node-603"></a>
    <p align="center"><kbd><img src="assets/87665d8e384380f5a02e893d0bc0dbb93dbe83dc.png" width="100%"></kbd></p>
    > Đại khái là run G.C khi ini (ban
    > đầu) và khi đã train 1 lúc

    <br>

  <a id="node-604"></a>
  - 1 In this video, the speaker shares some \\*practical tips\\* and \\*notes\\* on implementing gradient checking for a neural network.  2 One of the tips is to only use gradient checking for \\*debugging\\* and \\*not during training\\*. This is because computing d theta approx i for all values of i is a slow computation. Instead, backprop should be used to compute d theta for implementing gradient descent.  3 If an algorithm \\*fails grad check\\*, the speaker advises to look at the \\*individual components to identify the bug\\*. By \\*examining the different values of i\\*, the location of the bug can be determined. For example, if the values of theta or d theta are very far off, all corresponding to dbl for some layer, the bug might be in how the derivative with respect to parameters b is being computed.  4 Another tip is to \\*remember the regularization term when doing grad check\\*. If regularization is being used in the cost function, it's \\*important to include \\*that term in the calculation of d theta.  5 \\*Dropout\\* cannot be easily checked with grad check because in every iteration, dropout \\*randomly eliminates different subsets of hidden unit\\*s. This makes it difficult to compute the cost function J that dropout is doing gradient descent on. Therefore, grad check should be \\*implemented without dropout\\*, and dropout should be turned on afterwards.  6 It's possible that the implementation of backprop may be \\*correct\\* \\*only\\* when w and b are\\* close to 0\\* and become more \\*inaccurate as w and b become larger.\\* To address this, the speaker \\*suggests running grad check at random initialization\\* and then training the network for a while before r\\*unning grad check again\\*.  7 Overall, the video covers a range of topics, including setting up train, dev, and test sets, analyzing bias and variance, applying different forms of regularization, and gradient checking. These concepts are further elaborated in the week's programming exercise.
    <br>


<a id="node-605"></a>
## Quiz

<br>

<a id="node-606"></a>

<p align="center"><kbd><img src="assets/e9eb4bc29df7eaad959ab28fed6bc804f7e14c95.png" width="100%"></kbd></p>

<br>

<a id="node-607"></a>

<p align="center"><kbd><img src="assets/6a3cd44a4f4ef86284d87ed5f77180bbff45d653.png" width="100%"></kbd></p>

<br>

<a id="node-608"></a>

<p align="center"><kbd><img src="assets/da2f2d22536765d1ff2b388f69e6e8bd1b16ce55.png" width="100%"></kbd></p>

<br>

<a id="node-609"></a>

<p align="center"><kbd><img src="assets/7f4858b9574ae96d6a3029554e2820a6aabb0910.png" width="100%"></kbd></p>

<br>

<a id="node-610"></a>

<p align="center"><kbd><img src="assets/203f07bfd72d92898a72ccba11c904a340522311.png" width="100%"></kbd></p>

<br>

<a id="node-611"></a>

<p align="center"><kbd><img src="assets/63f52c4eb81dccc48284aa7973857fe106476877.png" width="100%"></kbd></p>

<br>

<a id="node-612"></a>

<p align="center"><kbd><img src="assets/d64af8d17e72220599dcad1c8c5523191d604f45.png" width="100%"></kbd></p>

<br>

<a id="node-613"></a>

<p align="center"><kbd><img src="assets/244d414ca0ef80b2e4eab41dce981c6a3e16a30d.png" width="100%"></kbd></p>

<br>

<a id="node-614"></a>

<p align="center"><kbd><img src="assets/666852176556d91c9b151cc83652e69cd43b6f8e.png" width="100%"></kbd></p>

<br>

<a id="node-615"></a>

<p align="center"><kbd><img src="assets/5ddff49888e569624bb0e91df2e701335ad12438.png" width="100%"></kbd></p>

<br>

<a id="node-616"></a>

<p align="center"><kbd><img src="assets/87c628e64bda3b5a30fde12ff4ef11a11f754177.png" width="100%"></kbd></p>

<br>

<a id="node-617"></a>

<p align="center"><kbd><img src="assets/b4c7277d80d665633c918aa9b974ab98dd7c874d.png" width="100%"></kbd></p>

<br>


<a id="node-618"></a>
## Programming Assignments

<br>


<a id="node-619"></a>
### How to Download your Notebook

<br>

  <a id="node-620"></a>
  <p align="center"><kbd><img src="assets/8e4687c54a87c6e8a4a74859bcfbbd455aa1b829.png" width="100%"></kbd></p>
  <br>

  <a id="node-621"></a>
  <p align="center"><kbd><img src="assets/61da6aba98143f8b5b32712a2e5c7427685222d7.png" width="100%"></kbd></p>
  <br>


<a id="node-622"></a>
### Programming Assignments 1: Initialization

<br>

  <a id="node-623"></a>
  <p align="center"><kbd><img src="assets/211d5232e652955ecadeef8934f16105b0844c77.png" width="100%"></kbd></p>
  <br>

  <a id="node-624"></a>
  <p align="center"><kbd><img src="assets/7f784452fda0295e7bdc212c4337a545e203b34e.png" width="100%"></kbd></p>
  <br>

  <a id="node-625"></a>
  <p align="center"><kbd><img src="assets/aed2693468142d0fd5b4860da78d0804a9268b1f.png" width="100%"></kbd></p>
  <br>

<a id="node-626"></a>
- 4 - Zero Initialization
  <br>

    <a id="node-627"></a>
    <p align="center"><kbd><img src="assets/e5873a234be300b5e964c48e9a67fcd235746386.png" width="100%"></kbd></p>
    <br>

    <a id="node-628"></a>
    <p align="center"><kbd><img src="assets/0fdbe6f88026387c14980cb765533cab36a4cd2f.png" width="100%"></kbd></p>
    <br>

    <a id="node-629"></a>
    <p align="center"><kbd><img src="assets/53e987a765bfa21a117da6db4639d324267e8320.png" width="100%"></kbd></p>
    <br>

    <a id="node-630"></a>
    <p align="center"><kbd><img src="assets/cb8dfa292df0aae9997b8c197e206561f4df2d21.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/cb8dfa292df0aae9997b8c197e206561f4df2d21.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/14c8a246df20afc42237530db9ddf6ee710a142a.png" width="100%"></kbd></p>
    <br>

<a id="node-631"></a>
- 5 - Random Initialization
  <br>

    <a id="node-632"></a>
    <p align="center"><kbd><img src="assets/b2764591bdc427557b34f8ca199189a9befeda64.png" width="100%"></kbd></p>
    <br>

    <a id="node-633"></a>
    <p align="center"><kbd><img src="assets/f44ff2e897601ab5fd58cdd02b66cd7241419b64.png" width="100%"></kbd></p>
    <br>

    <a id="node-634"></a>
    <p align="center"><kbd><img src="assets/8ff424d637c123549ad12d4258ea77ea13d5beb0.png" width="100%"></kbd></p>
    <br>

    <a id="node-635"></a>
    <p align="center"><kbd><img src="assets/f42097eca03baa3fedb4fbb9601b9ebc6ce18921.png" width="100%"></kbd></p>
    <br>

    <a id="node-636"></a>
    <p align="center"><kbd><img src="assets/71168e31dc899a08ed43333a1dff150359bf7eb7.png" width="100%"></kbd></p>
    <br>

<a id="node-637"></a>
- 6 - He Initialization
  <br>

    <a id="node-638"></a>
    <p align="center"><kbd><img src="assets/660077aa0868630b1e9a202dea3c2009aeb23c46.png" width="100%"></kbd></p>
    <br>

    <a id="node-639"></a>
    <p align="center"><kbd><img src="assets/7c72b727b0a17da6075c38a7bb38e241e2171829.png" width="100%"></kbd></p>
    <br>

    <a id="node-640"></a>
    <p align="center"><kbd><img src="assets/7da22e916a494a87cd6ab49e45585a7ccac26d9c.png" width="100%"></kbd></p>
    <br>

    <a id="node-641"></a>
    <p align="center"><kbd><img src="assets/8177948dda10507e9f7ff02033f3a0cb4e3912bf.png" width="100%"></kbd></p>
    <br>

<a id="node-642"></a>
- 7 - Conclusions
  <br>

    <a id="node-643"></a>
    <p align="center"><kbd><img src="assets/7da80257c3619f96269f380d88bea2eca9adb885.png" width="100%"></kbd></p>
    <br>

    <a id="node-644"></a>
    <p align="center"><kbd><img src="assets/89e6fcfefe98c7cb6f711f71337c2dd8fc918fd8.png" width="100%"></kbd></p>
    <br>


<a id="node-645"></a>
### Programming Assignments 2: Regularization

<br>

<a id="node-646"></a>
- 1 - Packages
  <br>

    <a id="node-647"></a>
    <p align="center"><kbd><img src="assets/adaf2c08d27028d3d5c32185285de4f8fe694229.png" width="100%"></kbd></p>
    <br>

    <a id="node-648"></a>
    <p align="center"><kbd><img src="assets/d0a3383d065f018bdae6f3400595581cb73b4c6a.png" width="100%"></kbd></p>
    <br>

<a id="node-649"></a>
- 2 - Problem Statement
  <br>

    <a id="node-650"></a>
    <p align="center"><kbd><img src="assets/51c1cebb65f58136ecfe05dfc07c153b8826de39.png" width="100%"></kbd></p>
    <br>

<a id="node-651"></a>
- 3 - Loading the Dataset
  <br>

    <a id="node-652"></a>
    <p align="center"><kbd><img src="assets/d95c199ca44b64ce7ba0331b8487108f8f1bfd6b.png" width="100%"></kbd></p>
    <br>

<a id="node-653"></a>
- 4 - Non-Regularized Model
  <br>

    <a id="node-654"></a>
    <p align="center"><kbd><img src="assets/b62db772196c8f7bc59d2ddf64cb4260f7c067de.png" width="100%"></kbd></p>
    <br>

    <a id="node-655"></a>
    <p align="center"><kbd><img src="assets/e72bc9c641c2d1c9328838efa06e2729ab142366.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/e72bc9c641c2d1c9328838efa06e2729ab142366.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/39c5acbeb16ac85644e65299e6c8db440e0cc326.png" width="100%"></kbd></p>
    <br>

    <a id="node-656"></a>
    <p align="center"><kbd><img src="assets/6b7eb7fc65d5dc396f7c65bfd42d8c5050f473ea.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/6b7eb7fc65d5dc396f7c65bfd42d8c5050f473ea.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/366f51177c26c4168e3d80f4d75875d933f4731d.png" width="100%"></kbd></p>
    <br>

<a id="node-657"></a>
- 5 - L2 Regularization
  <br>

    <a id="node-658"></a>
    <p align="center"><kbd><img src="assets/2d6f88fc6089c526f4e79d4d895b9f5ef091d249.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/2d6f88fc6089c526f4e79d4d895b9f5ef091d249.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/a6e7366175afb940e8afd8de0a295a6d769b4dbf.png" width="100%"></kbd></p>
    <br>

    <a id="node-659"></a>
    <p align="center"><kbd><img src="assets/9e6460cfbf711b8ac0915818f7fa730f882eb194.png" width="100%"></kbd></p>
    <br>

    <a id="node-660"></a>
    <p align="center"><kbd><img src="assets/9816eb411e14df306831513f4df7a7eca075be13.png" width="100%"></kbd></p>
    <br>

    <a id="node-661"></a>
    <p align="center"><kbd><img src="assets/03eb1d29ad34b79815d7c21ee5ad2bfc214b8ec1.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/03eb1d29ad34b79815d7c21ee5ad2bfc214b8ec1.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/f2d5f17389d8cc98df4da45de40b78a9fa88c9a4.png" width="100%"></kbd></p>
    <br>

    <a id="node-662"></a>
    <p align="center"><kbd><img src="assets/1d7672b6ffe4a2ca1009e27604f26dbdf19d7e80.png" width="100%"></kbd></p>
    <br>

    <a id="node-663"></a>
    <p align="center"><kbd><img src="assets/2ee8790d397ef1bc559061dfa1aeabd54daf1413.png" width="100%"></kbd></p>
    <br>

    <a id="node-664"></a>
    <p align="center"><kbd><img src="assets/60ec9b78c73f4dbe3262987972c6132dd647da73.png" width="100%"></kbd></p>
    <br>

<a id="node-665"></a>
- 6 - Dropout
  <br>

    <a id="node-666"></a>
    <p align="center"><kbd><img src="assets/04a4ffe1d27f5b5aef92b4c708217ba043080c7c.png" width="100%"></kbd></p>
    <br>

    <a id="node-667"></a>
    <p align="center"><kbd><img src="assets/c58ff45421a0055099586917465ac541e278fb33.png" width="100%"></kbd></p>
    <br>

    <a id="node-668"></a>
    <p align="center"><kbd><img src="assets/20a346a5d9e59d418774c1ccee0cc5028a72941c.png" width="100%"></kbd></p>
    <br>

    <a id="node-669"></a>
    <p align="center"><kbd><img src="assets/d6970c93ebae53fcb749a8e0c3d3b7e05582d711.png" width="100%"></kbd></p>
    <br>

    <a id="node-670"></a>
    <p align="center"><kbd><img src="assets/16e203ab2fea783c00eb71439b4257a860e98722.png" width="100%"></kbd></p>
    <br>

  <a id="node-671"></a>
  - 6.1 - Forward Propagation with Dropout
    <br>

      <a id="node-672"></a>
      <p align="center"><kbd><img src="assets/a394a990000b95a3cf8c394afebb82c523e9d242.png" width="100%"></kbd></p>
      <p align="center"><kbd><img src="assets/a394a990000b95a3cf8c394afebb82c523e9d242.png" width="100%"></kbd></p>
      <p align="center"><kbd><img src="assets/96079debc17e0ef40cdb8a00ba63c118d0eb6060.png" width="100%"></kbd></p>
      <br>

      <a id="node-673"></a>
      <p align="center"><kbd><img src="assets/2efe4e0ddcc06ad8b076f5af04fbea12028c7b9c.png" width="100%"></kbd></p>
      <p align="center"><kbd><img src="assets/2efe4e0ddcc06ad8b076f5af04fbea12028c7b9c.png" width="100%"></kbd></p>
      <p align="center"><kbd><img src="assets/4339205ee1d7b07d0ea1e0d3e11803fe1d4b2f11.png" width="100%"></kbd></p>
      <br>

  <a id="node-674"></a>
  - 6.2 - Backward Propagation with Dropout
    <br>

      <a id="node-675"></a>
      <p align="center"><kbd><img src="assets/50f53267c0f7b386da5a4c6c86830c4f85dc2919.png" width="100%"></kbd></p>
      <br>

      <a id="node-676"></a>
      <p align="center"><kbd><img src="assets/06634e5762748f4e7a7c5fb219d84c7a974d88c7.png" width="100%"></kbd></p>
      <p align="center"><kbd><img src="assets/06634e5762748f4e7a7c5fb219d84c7a974d88c7.png" width="100%"></kbd></p>
      <p align="center"><kbd><img src="assets/8f3d3d955a75e600be19b519a1a8e91a1edacbfc.png" width="100%"></kbd></p>
      <br>

      <a id="node-677"></a>
      <p align="center"><kbd><img src="assets/00fd6599bfa69734c1d24a739bfd98f18c5a7010.png" width="100%"></kbd></p>
      <br>

      <a id="node-678"></a>
      <p align="center"><kbd><img src="assets/88dc9ddb439c1b2518390660412c27b6c5436443.png" width="100%"></kbd></p>
      <br>

      <a id="node-679"></a>
      <p align="center"><kbd><img src="assets/dc43b54e57846c9359fdc9c0a2aed8c19cbf0900.png" width="100%"></kbd></p>
      <br>

<a id="node-680"></a>
- 7 - Conclusions
  <br>

    <a id="node-681"></a>
    <p align="center"><kbd><img src="assets/f7d95c2d92248f443b0875b63eb0af861ac8ece0.png" width="100%"></kbd></p>
    <br>

    <a id="node-682"></a>
    <p align="center"><kbd><img src="assets/b605f21d0dd4f2390f94508a99b7fdb8d2e9a115.png" width="100%"></kbd></p>
    <br>


<a id="node-683"></a>
### Programming Assignments: Gradient Checking

<br>

<a id="node-684"></a>
- Gradient Checking
  <br>

    <a id="node-685"></a>
    <p align="center"><kbd><img src="assets/2787577bf5e85eefb70c8a6b7f2f11ac61ef178a.png" width="100%"></kbd></p>
    <br>

    <a id="node-686"></a>
    <p align="center"><kbd><img src="assets/5eca81ee4c12e5c825f6a0272044c64101c39b8a.png" width="100%"></kbd></p>
    <br>

    <a id="node-687"></a>
    <p align="center"><kbd><img src="assets/e82596dd6ab1b20037545dfc9c1c4f03c4d27ec0.png" width="100%"></kbd></p>
    <br>

<a id="node-688"></a>
- 4 - 1-Dimensional Gradient Checking
  <br>

    <a id="node-689"></a>
    <p align="center"><kbd><img src="assets/35cad9598c1f987225df27c76b57a4b72f1c0c5e.png" width="100%"></kbd></p>
    <br>

    <a id="node-690"></a>
    <p align="center"><kbd><img src="assets/4cf33559ca0aad76f67716ff72eae3be38481c2e.png" width="100%"></kbd></p>
    <br>

    <a id="node-691"></a>
    <p align="center"><kbd><img src="assets/eec65eb45c0539c9fa8c5c9ba73a9d6cad376869.png" width="100%"></kbd></p>
    <br>

    <a id="node-692"></a>
    <p align="center"><kbd><img src="assets/928310151297a86b5886e0828c811f55e3f856c0.png" width="100%"></kbd></p>
    <br>

    <a id="node-693"></a>
    <p align="center"><kbd><img src="assets/5ab00fc74148e60957241b05e2174490ea3a896e.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/5ab00fc74148e60957241b05e2174490ea3a896e.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/48d900fa990b3fb46431653820af049e0dda24bf.png" width="100%"></kbd></p>
    <br>

<a id="node-694"></a>
- 5 - N-Dimensional Gradient Checking
  <br>

    <a id="node-695"></a>
    <p align="center"><kbd><img src="assets/c105d7e3d706a7232e3af5fee8cda6ac4daf5eb3.png" width="100%"></kbd></p>
    <br>

    <a id="node-696"></a>
    <p align="center"><kbd><img src="assets/509745c9fcc2cd33ed85326bf34b225bbac26a48.png" width="100%"></kbd></p>
    <br>

    <a id="node-697"></a>
    <p align="center"><kbd><img src="assets/a3ac19035b40bb28ac668f643bef608ad2da7bd1.png" width="100%"></kbd></p>
    > Ở đây ổng cố tình làm sai chỗ dW2 ( *2 -> Sai, ko có *2
    > làm gì) và db1 (4 ./ .. -> Sai, 1/ mới đúng).
    > Mục đích để tí nữa Gradient Check thấy sai và xem lại

    <br>

    <a id="node-698"></a>
    <p align="center"><kbd><img src="assets/b6c0b2a66249cef2bf4cbc84a5ce1f0debd62e97.png" width="100%"></kbd></p>
    <br>

    <a id="node-699"></a>
    <p align="center"><kbd><img src="assets/90623b0dde0afa7d6e4758bb6b48f9e46dea31be.png" width="100%"></kbd></p>
    <br>

    <a id="node-700"></a>
    <p align="center"><kbd><img src="assets/391aae573f47770bc95f87d3ca08de60d07e6208.png" width="100%"></kbd></p>
    <br>

    <a id="node-701"></a>
    <p align="center"><kbd><img src="assets/007dcb62eb7347155aa86b463a5fffd4f8c7b87f.png" width="100%"></kbd></p>
    <br>

    <a id="node-702"></a>
    <p align="center"><kbd><img src="assets/f69001fce67114b4b2fa4f4a94bcec3cf696256b.png" width="100%"></kbd></p>
    <br>

    <a id="node-703"></a>
    <p align="center"><kbd><img src="assets/5c27c6793d947cd0877412d1bb0925906226940d.png" width="100%"></kbd></p>
    <br>

    <a id="node-704"></a>
    <p align="center"><kbd><img src="assets/45941c7702eb2b6a69c53cbc0dc058ff149fd80c.png" width="100%"></kbd></p>
    <br>

