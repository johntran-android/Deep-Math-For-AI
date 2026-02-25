# C2w3_hyperparamter Tuning, Batch Normalization & Programming Frameworks

📊 **Progress:** `56` Notes | `89` Screenshots

---

Explore TensorFlow, a deep learning framework that allows you to build neural networks quickly and easily, then train a neural network on a TensorFlow dataset.
**Learning Objectives**
 • Master the process of hyperparameter tuning
 • Describe softmax classification for multiple classes
 • Apply batch normalization to make your neural network more robust
 • Build a neural network in TensorFlow and train it on a TensorFlow dataset
 • Describe the purpose and operation of GradientTape
 • Use tf.Variable to modify the state of a variable
 • Apply TensorFlow decorators to speed up code
 • Explain the difference between a variable and a constant

<a id="node-861"></a>
## Hyperparams Tuning

> [!NOTE]
> 1ST REVIEWED

<br>


<a id="node-862"></a>
### Tuning Process

<br>

<a id="node-863"></a>
- 1 There are a lot of hyperparameters that need to be set when training deep neural networks, such as \\*learning rate\\*, \\*momentum term\\*,\\* number of layers,\\* number of hidden units, mini-batch size, and learning rate decay.  2 Some of these hyperparameters are \\*more important than others\\*. \\*Learning rate\\* is the\\* most important,\\* followed by \\*momentum term\\*, \\*mini-batch size\\*, and number of \\*hidden units.\\*  3 It's difficult to know in advance which hyperparameters will be the most important, so it's important to\\* try out a wide range of values\\*.  4 \\*Sampling at random\\* is a \\*better approach\\* than systematically exploring values in a \\*grid\\* because it allows for a \\*more rich exploration\\* of the hyperparameter space.  5\\* Coarse to fine sampling\\* is a \\*common practice\\* that involves \\*zooming\\* \\*in\\* on \\*promising areas\\* of the \\*hyperparameter space\\* and exploring more densely within that area.
  > 1 Hyperparameters in neural networks: Neural networks involve setting a lot of different hyperparameters, ranging from the learning rate alpha to the momentum term beta, the hyperparameters for the Adam Optimization Algorithm (beta one, beta two, and epsilon), the number of layers, the number of hidden units for the different layers, and the mini-batch size.
>  2 Importance of hyperparameters: Some of these hyperparameters are more important than others. The most important hyperparameter to tune is usually the learning rate alpha. Other hyperparameters that should be considered next include the momentum term (0.9 is a good default), the mini-batch size (to ensure the optimization algorithm is running efficiently), and the hidden units.
>  3 Tuning hyperparameters: How do you go about finding a good setting for these hyperparameters? It's important to systematically organize your hyperparameter tuning process to make it more efficient for you to converge on a good setting of the hyperparameters.
>  4 Sampling hyperparameters: In earlier generations of machine learning algorithms, if you had two hyperparameters, it was common practice to sample the points in a grid and systematically explore these values. However, in deep learning, it's better to choose the points at random to try out on a randomly chosen set of points. This is because it's difficult to know in advance which hyperparameters are going to be the most important for your problem.
>  5 Importance of sampling at random: Some hyperparameters are much more important than others. If you sample in a grid, you might find that you've only tried out a few values of the most important hyperparameter, while having tried out many different values of a less important hyperparameter. Sampling at random helps to explore a more diverse set of possible values for the most important hyperparameters, whatever they turn out to be.
>  6 Coarse to fine sampling scheme: Another common practice when sampling hyperparameters is to use a coarse to fine sampling scheme. This involves starting with a larger set of hyperparameters and then zooming in to a smaller region of the hyperparameters to sample more densely within this space. This can help to focus more resources on searching within the most promising regions of hyperparameters.

  <br>

    <a id="node-864"></a>
    <p align="center"><kbd><img src="assets/47811c5e1387a09f2298898766370864e9a8c705.png" width="100%"></kbd></p>
    <br>

    <a id="node-865"></a>
    <p align="center"><kbd><img src="assets/a8099fdc6562a3d92a6b5bf8e6323e63d26e7ff1.png" width="100%"></kbd></p>
    > Khó biết được hyperparam nào là quan trọng (khiến Model tốt)
>
> Nên thay vì làm theo kiểu Grid như hồi đầu của ML, bây giờ
> nên chọn **Random** .

    <br>

    <a id="node-866"></a>
    <p align="center"><kbd><img src="assets/82f64d433fab854493d95e09600fd8151ebdb65d.png" width="100%"></kbd></p>
    > Khi thấy 'vị trí' nào cho kết qua tốt -> Zoom vào khu
> vực đó **(Coarse to fine)**

    <br>

  <a id="node-867"></a>
  - 1 Hyperparameters in neural networks: Neural networks involve setting a lot of different hyperparameters, ranging from the learning rate alpha to the momentum term beta, the hyperparameters for the Adam Optimization Algorithm (beta one, beta two, and epsilon), the number of layers, the number of hidden units for the different layers, and the mini-batch size.  2 Importance of hyperparameters: Some of these hyperparameters are more important than others. The most important hyperparameter to tune is usually the learning rate alpha. Other hyperparameters that should be considered next include the momentum term (0.9 is a good default), the \\*mini-batch size\\* (to ensure the optimization algorithm is running efficiently), and the hidden units.  3 \\*Tuning\\* \\*hyperparameters\\*: How do you go about finding a good setting for these hyperparameters? It's important to \\*systematically organize your hyperparameter\\* tuning process to make it more efficient for you to converge on a good setting of the hyperparameters.  4 \\*Sampling\\* hyperparameters: In earlier generations of machine learning algorithms, if you had two hyperparameters, it was common practice to sample the points in a grid and systematically explore these values. However, in deep learning, it's better to choose the\\* points at random\\* to try \\*out on a randomly chosen set of points\\*. This is because it's difficult to know in advance which hyperparameters are going to be the most important for your problem.  5 Importance of sampling at random: Some hyperparameters are \\*much more important than other\\*s. If you sample in a grid, you might find that you' ve only tried out a few values of the most important hyperparameter, while having tried out many different values of a less important hyperparameter. Sampling at random helps to explore a \\*more diverse set of possible values for the most important hyperparameters\\*, whatever they turn out to be.  6 \\*Coarse to fine sampling\\* scheme: Another common practice when sampling hyperparameters is to use a \\*coarse to fine sampling scheme\\*. This involves \\*starting with a larger set of hyperparameters\\* and then \\*zooming in to a smaller region\\* of the hyperparameters to sample m\\*ore densely within this space.\\* This can help to\\* focus more resources on searching within the most promising regions\\* of hyperparameters.
    <br>


<a id="node-868"></a>
### Using An Appropriate Scale To Pick Hyperparameters

<br>

<a id="node-869"></a>
- 1\\* Random sampling\\* over hyperparameters allows \\*efficient search\\* over their space.  2 It is \\*important\\* to pick the \\*appropriate scale\\* on which to explore the hyperparameters.  3 \\*Sampling uniformly at random \\*over the range of hyperparameters might be \\*reasonable for certain hyperparameters,\\* such as the \\*number of hidden units\\* and \\*layers\\* in a neural network.  4 It is\\* not reasonable\\* to sample uniformly at random over the range of all hyperparameters.  5 Searching for hyperparameters on a\\* log scale\\* is \\*more reasonable\\*, especially for hyperparameters such as the \\*learning rate.\\*  6 To sample on a log scale, you need to take the \\*low\\* and \\*high values\\*, take \\*logs\\* to figure out what \\*a\\* and\\* b\\* are, sample \\*r\\* \\*uniformly between a and b\\*, and set the \\*hyperparameter to be 10 to the power of r.\\*  7 Sampling for the hyperparameter \\*beta\\* used for computing exponentially weighted averages is \\*tricky\\* and \\*should not be\\* \\*sampled on a linear scale. \\* 8 To explore the r\\*ange of values for beta\\*, it is important to \\*consider the range of values for the corresponding exponentially weighted average\\*s.
  > 1 Sampling hyperparameters at random can be an efficient way to search over their space, but it's important to pick the appropriate scale to explore them.
>  2 Uniformly sampling hyperparameters may not be appropriate for all ranges of values. For example, when searching for the learning rate alpha, using a linear scale from 0.0001 to 1 would result in sampling mostly from the range of 0.1 to 1. Instead, it's better to use a logarithmic scale where values are spaced equally on the log scale.
>  3 To sample on a logarithmic scale in Python, you can use the following code:
>  • Let r = -4 * np.random.rand()
>  • A randomly chosen value of alpha would then be alpha = 10 to the power of r
>  • This results in alpha being sampled between 10 to the -4 and 10 to the 0
>  4 In a more general case, if you want to sample between 10 to the a and 10 to the b on a log scale, you can use the following steps:
>  • Take the log base 10 of the low value to find a
>  • Take the log base 10 of the high value to find b
>  • Sample r uniformly at random between a and b
>  • Set the hyperparameter to be 10 to the r
>  5 Another tricky case is sampling the hyperparameter beta used for computing exponentially weighted averages. In this case, it's important to understand the effect of changing the value of beta on the average. Using a linear scale to sample beta between 0.9 and 0.999 may not be effective since the values are spaced closely together near 0.999. Instead, a good way to sample beta is to use the formula beta = 1 - 10 to the power of -x, where x is sampled uniformly at random between 1 and 4.
>  6 Overall, it's important to understand the range of values that each hyperparameter can take and to choose an appropriate scale for sampling in order to efficiently explore their space.

  <br>

    <a id="node-870"></a>
    <p align="center"><kbd><img src="assets/cb0c8c68caabb2d08b4ea4cc636d0e6c8f231fae.png" width="100%"></kbd></p>
    > Ví dụ như ta đang chọn random số hidden unit cho layer mà
> Ta nhắm chừng trong khoảng 50 - 100, thế là lẽ dĩ nhiên ta
> lấy random vài giá trị trong khoảng này.
>
> Hoặc số layer nhắm chừng trong khoảng 2,3,4, ta cứ thử từng 
> cái 2,3,4..
> Thì đại khái là cái hyperparam kiểu này ta làm vâỵ được, nhưng đối 
> với cái khác thì không....

    <br>

    <a id="node-871"></a>
    <p align="center"><kbd><img src="assets/b21e8c6f165f8bf5bfb8485312e4353e9d6a4500.png" width="100%"></kbd></p>
    > Ví dụ như alpha nhắm trong khoảng từ 0.001 tới 1
> Nếu ta cũng làm như cách làm ở thằng hidden unit
> thì đại khái là ta sẽ 90% là chọn alpha từ 0.1-1. chỉ còn 10%
> từ 0.001-0.1
> 90 hay 10 là đại ý nói do cái **scale nó ko bằng nhau** nên 
> không làm vậy được.
>
> Thay vào đó phải làm theo kiểu lấy **log**.
>
> Ví dụ muốn lấy từ 0.0001 - 1. Thừ xem **0.0001** là log(a) **a bao nhiêu**.
> **1** là log(b) ->**b bao nhiêu.**
> -> Dẫn tới bài toán chọn **r random trong đoạn [a,b]** ->**alpha = 10^r**

    <br>

    <a id="node-872"></a>
    <p align="center"><kbd><img src="assets/3476f0f823557357f53fa4b6dce8cd8e73cb9804.png" width="100%"></kbd></p>
    > Tương tự như vậy với beta.
>
> Nhớ lại (1-epsilon)^(1/epsilon)
>
> 0.9000 -> 0.9005: Tăng 0.0005
> Beta = 0.9 -> epsilon = 0.1 -> 1/epsilon = 10 thì hiểu đại khái là nó lấy 
> Trung bình của 10 ngày trước đó.
> Beta = 0.9005 -> Epsilon = 0.095 -> 1/epsilon cũng cỡ 10 (10,05)
>
> 0.9990 -> 0.9995: Cũng tăng 0.0005
> Beta = 0.9990 -> epsilon = 0.001 -> 1/epsilon = 1000
> Beta = 0.9995 -> epsilon = 0.0005 -> 1/epsilon = 2000
>
> Có nghĩa là trong đoạn cùng là 0.0005 mà mức ảnh hưởng của nó
> hoàn toàn khác nhau

    <br>

    <a id="node-873"></a>
    <p align="center"><kbd><img src="assets/0c144922aad53bb89b3f7e006c7f51fcd778dac9.png" width="100%"></kbd></p>
    <br>

  <a id="node-874"></a>
  - 1 Sampling hyperparameters at random can be an efficient way to search over their space, but it's important to pick the appropriate scale to explore them.  2 Uniformly sampling hyperparameters may not be appropriate for all ranges of values. For example, when searching for the learning rate alpha, using a linear scale from 0.0001 to 1 would result in sampling mostly from the range of 0.1 to 1. Instead, it's better to use a logarithmic scale where values are spaced equally on the log scale.  3 To sample on a logarithmic scale in Python, you can use the following code:  • Let r = -4 * np.random.rand()  • A randomly chosen value of alpha would then be alpha = 10 to the power of r  • This results in alpha being sampled between 10 to the -4 and 10 to the 0  4 In a more general case, if you want to sample between 10 to the a and 10 to the b on a log scale, you can use the following steps:  • Take the log base 10 of the low value to find a  • Take the log base 10 of the high value to find b  • Sample r uniformly at random between a and b  • Set the hyperparameter to be 10 to the r  5 Another tricky case is sampling the hyperparameter beta used for computing exponentially weighted averages. In this case, it's important to understand the effect of changing the value of beta on the average. Using a linear scale to sample beta between 0.9 and 0.999 may not be effective since the values are spaced closely together near 0. 999. Instead, a good way to sample beta is to use the formula beta = 1 - 10 to the power of -x, where x is sampled uniformly at random between 1 and 4.  6 Overall, it's important to understand the range of values that each hyperparameter can take and to choose an appropriate scale for sampling in order to efficiently explore their space.
    <br>


<a id="node-875"></a>
### Hyperparams Tuning In Practice: Pandas Vs. Caviar

<br>

<a id="node-876"></a>
- 1 Intuitions about hyperparameter settings from one application area may or may not transfer to a different one, but \\*cross-fertilization among different domains\\* is \\*increasingly common\\*.  2 \\*Hyperparameter settings\\* can get \\*stale\\* due to \\*changes\\* in \\*data\\* or \\*computational resources,\\* so it's recommended to \\*retest\\* or \\*reevaluate hyperparameters\\* at least once \\*every several months.\\*  3 Two \\*major ways\\* of searching for hyperparameters are the \\*panda approac\\*h, where \\*one model\\* is \\*gradually tweaked\\*, and the \\*caviar approach\\*, where \\*many mode\\*ls are trained \\*in parallel \\*and the b\\*est one is chosen.\\*  4 The choice between the two approaches \\*depends on the amount of computational resources\\* available.
  > 1 Importance of cross-fertilization in deep learning:
>  2 Deep learning is applied in various application areas, and intuitions about hyperparameter settings from one area may or may not transfer to a different one. However, there is a lot of cross-fertilization among different application domains, with researchers reading increasingly from other domains to look for inspiration for cross-fertilization. For example, ideas developed in computer vision, such as Confonets or ResNets, have been successfully applied to speech, and vice versa.
>  3 The risk of stale hyperparameter settings:
>  4 Intuitions about the best hyperparameter settings can get stale over time, even when working on the same problem. For instance, a good setting that was once found may no longer work due to changes in data or hardware. Therefore, it is recommended to retest or reevaluate hyperparameters periodically, maybe at least once every several months, to ensure that the current hyperparameter values are still suitable.
>  5 Two major schools of thought in hyperparameter search:
>  6 There are two major ways in which people go about searching for hyperparameters: babysitting one model and training many models in parallel.
>  7 Babysitting one model:
>  8 If computational resources are limited, then one approach is to babysit one model by gradually nudging up and down the parameters. For example, one might initialize the parameters randomly and start training, then gradually watch the learning curve, maybe the cost function or dataset error, gradually decrease over the first day. At the end of the day, one might try increasing the learning rate a little bit and see how it performs, and then adjust the parameters again the following day, and so on. The approach is called the panda approach, as it is similar to how pandas have few children and put a lot of effort into ensuring their survival.
>  9 Training many models in parallel:
>  10 If there are enough computational resources, then one can train many models in parallel with different hyperparameters. Each model generates its own learning curve, and the best hyperparameter setting is selected based on which model performs the best. This approach is called the caviar strategy, as it is similar to how fish reproduce by laying many eggs and not paying too much attention to any one of them.
>  11 Choosing between the two approaches:
>  12 The choice between the two approaches is mainly a function of how much computational resources are available. If there are enough resources, then the caviar strategy can be used to try a lot of different hyperparameter settings and select the best one quickly. However, if resources are limited, then the panda approach can be used to gradually adjust the hyperparameters of one model over time.

  <br>

    <a id="node-877"></a>
    <p align="center"><kbd><img src="assets/8f2566d8c964e56892ed982c2193f519ee2f82c6.png" width="100%"></kbd></p>
    > Đại khái là nên **retest hyperparams vài tháng một lần** vì
> những **sự thay đổ**i có thể khiến cái mình đã tune ngon 
> hết ngon
> Ví dụ: Data thay đổi, server khác, 
>
> Còn chuyển từ domain này qua domain khác thì đại ý là 
> Deep learning nó có ưu điểm là kế thừa được những cái từ
> domain khác, nhưng hyperparam thì không, phải tune lại.

    <br>

    <a id="node-878"></a>
    <p align="center"><kbd><img src="assets/3232bc09d92cce411d497da01ac2019f069a0a89.png" width="100%"></kbd></p>
    > Đại khái là máy mạnh thì **chạy nhiều model cùng lúc** rồi **xem
> cái nào ngon nhất**.-> Như cá hồi đẻ trứng
>
> Còn không thì c**hăm như chăm con**, từng ngày từng ngày 
> theo dõi và điều chỉnh. Ví dụ ngày thứ 2 thử giảm alpha xuống 
> Qua thứ 3 thấy ok, thử cái khác qua thứ 4 thấy nó không ổn,
> liền quay lại setting của ngày thứ 3, thử setting khác -> Chăm 
> như chăm con

    <br>

  <a id="node-879"></a>
  - 1 Importance of \\*cross-fertilization\\* in deep learning:  2 Deep learning is applied in various application areas, and\\* intuitions about hyperparameter settings\\* from one area \\*may or may not transfer\\* to a different one. However, there is a lot of \\*cross-fertilization among different application domains\\*, with researchers reading increasingly from other domains to look for inspiration for cross-fertilization. For example, ideas developed in \\*computer vision\\*, such as \\*ConVnets\\* or \\*ResNets\\*, have been successfully applied to \\*speech\\*, and vice versa.  3 The risk of \\*stale hyperparameter settings:\\*  4 Intuitions about the \\*best hyperparameter settings can get stale over time,\\* even when working on the same problem. For instance, a good setting that was once found may \\*no longer work\\* due to c\\*hanges in data or hardware\\*. Therefore, it is recommended to \\*retest\\* or \\*reevaluate\\* \\*hyperparameters\\* \\*periodically\\*, maybe at least\\* once every several months\\*, to ensure that the current hyperparameter values are\\* still suitable.\\*  5 Two major \\*schools of thought \\*in \\*hyperparameter search\\*:  6 There are two major ways in which people go about searching for hyperparameters: \\*babysitting\\* one model and \\*training\\* many models in \\*parallel\\*.  7 \\*Babysitting\\* one model:  8 If c\\*omputational resources are limited\\*, then one approach is to \\*babysit\\* one model by \\*gradually nudging up\\* and \\*down the parameters\\*. For example, one might initialize the parameters randomly and start training, then gradually watch the learning curve, maybe the cost function or dataset error, gradually decrease over the first day. At the end of the day, one might try increasing the learning rate a little bit and see how it performs, and then adjust the parameters again the following day, and so on. The approach is called the p\\*anda approach\\*, as it is similar to how pandas have few children and \\*put a lot of effort into ensuring their survival\\*.  9 Training\\* many models in parallel:\\*  10 If there are \\*enough computational resources\\*, then one can train \\*many models\\* in \\*parallel\\* with \\*different hyperparameters\\*. Each model generates its \\*own learning curve\\*, and the \\*best hyperparameter setting\\* is selected based on\\* which model performs the best\\*. This approach is called the \\*caviar strategy\\*, as it is similar to how fish reproduce by laying many eggs and not paying too much attention to any one of them.  11 Choosing between the two approaches:  12 The choice between the two approaches is mainly a function of how \\*much computational resources are available\\*. If there are enough resources, then the caviar strategy can be used to try a lot of different hyperparameter settings and select the best one \\*quickly\\*. However, if \\*resources are limited\\*, then the panda approach can be used to gradually adjust the hyperparameters of one model over time.
    <br>


<a id="node-880"></a>
## Batch Normalization

> [!NOTE]
> 1ST REVIEWED

<br>


<a id="node-881"></a>
### Clarification About Upcoming

> [!NOTE]
> CLARIFICATION ABOUT UPCOMING
> NORMALIZATION ACTIVATIONS IN A NETWORK

<br>

<a id="node-882"></a>
- ...
  <br>

    <a id="node-883"></a>
    <p align="center"><kbd><img src="assets/3612b55d81f41d7991f391b8002656d2038efb81.png" width="100%"></kbd></p>
    <br>


<a id="node-884"></a>
### Normalization Activations In A Network

<br>

<a id="node-885"></a>
- 1 Batch normalization is a deep learning algorithm that was created by Sergey Ioffe and Christian Szegedy.  2 Batch normalization can make the hyperparameter search problem much easier, make neural networks more robust, and enable easy training of very deep networks.  3 Normalizing input feature values can speed up learning in models such as logistic regression.  4 Batch normalization can be used to normalize the mean and variance of activations in hidden layers.  5 Batch normalization normalizes the values of z before the activation function is applied, and this is done much more often in practice.  6 To implement batch norm, you compute the mean and variance of intermediate values, normalize the values using mean and variance, and use learnable parameters gamma and beta to set the mean and variance of the normalized values to desired values.  7 Gamma and beta parameters can be updated using gradient descent or other algorithms, just like the weights of a neural network.
  > 1 Algorithm: Batch Normalization
>  • Batch normalization is an algorithm developed by Sergey Ioffe and Christian Szegedy.
>  • It is one of the most important ideas in the rise of deep learning.
>  • Batch normalization makes hyperparameter search easier and makes neural networks more robust.
>  • It enables a much bigger range of hyperparameters that work well and allows for easier training of even very deep networks.
>  2 Normalizing Input Features
>  • When training a model, such as logistic regression, normalizing input features can speed up learning.
>  • To normalize input features, compute the means and subtract them from the training sets.
>  • Then compute the variances and normalize the dataset according to the variances.
>  • This can turn the contours of the learning problem from elongated to round, making it easier for algorithms like gradient descent to optimize.
>  3 Normalizing Hidden Layer Activations
>  • For deeper models, not only do you have input features x, but also activations a1 in one layer, a2 in the next layer, and so on.
>  • Batch normalization normalizes the mean and variance of the activations a2 to make training of parameters w3 and b3 more efficient.
>  • By normalizing hidden layer activations, you can train w3 and b3 faster, as a2 is the input to the next layer, and therefore affects the training of w3 and b3.
>  4 Batch Normalization Implementation
>  • Given some intermediate values in your neural network, compute the mean and variance.
>  • Then normalize each value by subtracting the mean and dividing by the standard deviation.
>  • For numerical stability, add epsilon to the denominator in case sigma squared turns out to be zero in some estimate.
>  • Compute z tilde = gamma * zi_norm + beta, where gamma and beta are learnable parameters of your model.
>  • Gamma and beta allow you to set the mean of z tilde to be whatever you want it to be.
>  • By appropriately setting gamma and beta, you can make hidden unit values have other means and variances as well.
>  • Gamma and beta are updated using gradient descent or some other algorithm, just like the weights of your neural network.

  <br>

    <a id="node-886"></a>
    <p align="center"><kbd><img src="assets/99964d8b9c701b61f063b47d371f90b2aca415a1.png" width="100%"></kbd></p>
    > Đại khái là cũng như normalization đ.v X giúp ích cho việc training
> thì normalize các hidden unit output cũng vậy.

    <br>

    <a id="node-887"></a>
    <p align="center"><kbd><img src="assets/71025f672f9dab667d2fc8c9054ad533b14ade29.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/71025f672f9dab667d2fc8c9054ad533b14ade29.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/48faef0a34c25a3a392d9f78ca46cf00dfad3a1b.png" width="100%"></kbd></p>
    > Ở đây nó cũng normalize Theo kiểu tương tự 
> feature scaling (-mu) + mean normalization (/sigma)
>
> Nhưng có cái là 'không muốn cho mean = 0 để tận dụng khả
> năng của hàm sigmoid gì gì đó nên thay vì dùng
> z_norm, dùng z~ (Đọc là z tilde) = Gamma*z_norm + beta và Train
> Gamma và Beta như W, b.
>
> Chưa hiểu thì từ từ sẽ hiểu

    > Đại khái là nếu data chỉ loanh quanh quanh
> mốc z = 0 thì sigmoid(z) chỉ loanh quanh mốc 0.
> 5 và đoạn này nó khá tuyến tính nên nó sẽ
> không tận dụng được khả năng phi tuyến tính
> của hàm sigmoid

    <br>


<a id="node-888"></a>
### Fitting Batch Norm Into A Neural Network

<br>

<a id="node-889"></a>
- 1 Introduction to deep neural networks as a series of computations with multiple layers, each layer computing two things: Z and A.  2 Traditional process of computing Z and A without Batch Normalization.  3 Batch Normalization explained as a new layer that normalizes the Z values using Beta and Gamma parameters, computed for each layer.  4 The intuition behind using normalized values instead of un-normalized ones in computing the activations.  5 The new parameters added to the network for each layer where Batch Normalization is applied.  6 Optimization methods such as gradient descent, RMSprop, and Adam used for updating Beta and Gamma parameters.  7 Implementation of Batch Normalization in deep learning frameworks.  8 Mini-batch processing used in applying Batch Normalization during training.
  > Sure, here's a more detailed answer with indexed main ideas:
>  1 The equations for Batch Norm were previously introduced for a single hidden layer. In this context, Batch Norm takes the value Z1 and applies normalization to it using the Batch Norm parameters Beta 1 and Gamma 1 to get the normalized value Z tilde 1. This normalized value is then fed into the activation function to get A1.
>  2 In the case of a deep neural network, each unit can be viewed as performing a two-step computation, where Z is computed first and then fed into the activation function to get A. This process is repeated for each layer of the network.
>  3 When applying Batch Norm to a deep network, the normalized value Z tilde is used instead of the un-normalized value Z. For example, in the first layer, Z tilde 1 is computed and fed into the activation function to get A1. In the second layer, Z tilde 2 is computed using Z2 and Batch Norm parameters Beta 2 and Gamma 2.
>  4 The parameters of the network now include not only the usual W and B parameters for each layer, but also additional parameters Beta and Gamma for each layer where Batch Norm is applied.
>  5 The optimization method used to train the network can be any method of choice, such as gradient descent or Adam. The Batch Norm parameters can be updated using the chosen optimization method.
>  6 Batch Norm is typically applied using mini-batches of the training set. For each mini-batch, Z and A are computed for each layer using the parameters specific to that mini-batch. Mean and variance are computed for Z in that mini-batch, and Batch Norm is applied to the normalized Z value using the parameters Beta and Gamma for that layer. This process is repeated for each mini-batch in order to perform one step of gradient descent.
>  7 In most deep learning frameworks, Batch Norm is implemented as a built-in function that can be called with a single line of code. However, understanding how Batch Norm works can provide a better understanding of the training process and help with debugging.

  <br>

    <a id="node-890"></a>
    <p align="center"><kbd><img src="assets/5150f81ab76d2282da140e1623139c916f7dbc5a.png" width="100%"></kbd></p>
    > Thêm bước tính từ z -> z ~ (z tilde) nữa
>
> Và training thêm d_beta và d_gamma nữa
> (update beta, gamma như W, b bằng G.D vậy
>
> Nếu dùng Framework như TensorFlow thì không
> cần làm chỉ cần khai báo nó tự làm. Nói chung là
> chỉ cần hiểu nó làm gì là được.

    <br>

    <a id="node-891"></a>
    <p align="center"><kbd><img src="assets/74be861f64734a7acbb060eb8ef9170fef010447.png" width="100%"></kbd></p>
    > 1. Thường là làm việc với Mini-batch, thì nó sẽ như vầy, như vầy..
> Các step normalize (Batch norm) sẽ chỉ đ.v từng mini. batch 
>
> 2. Với Batch-norm thì param b trở nên vô nghĩa, nên có thể bỏ.
>
> 3.Beta[l] Gamma[l] sẽ cùng size / shape (n[l], 1) với b[l]

    <br>

    <a id="node-892"></a>
    <p align="center"><kbd><img src="assets/863787336bd00d22fcfa205470f19d199b3a8b73.png" width="100%"></kbd></p>
    > Put them together

    <br>


<a id="node-893"></a>
### Why Does Batch Norm Work

<br>

<a id="node-894"></a>
- 1 Batch normalization speeds up learning by normalizing all input features to take on a similar range of values.  2 Batch normalization makes weights deeper in a network more robust to changes to weights in earlier layers by addressing the problem of covariate shift.  3 Covariate shift occurs when the distribution of X changes, and it becomes necessary to retrain a learning algorithm even if the ground truth function mapping from X to Y remains unchanged.  4 From the perspective of a certain layer in a deep network, it gets some values from the earlier layers and has to map them to Y-hat, but these values change as the parameters in earlier layers change, causing the problem of covariate shift.  5 Batch normalization reduces the amount that the distribution of hidden unit values shifts around, ensuring that their mean and variance remain the same, making the network more robust to the problem of covariate shift.
  > 1 One reason why batch normalization works is that it normalizes the input features (X) to have a similar range of values, which can speed up learning. Instead of having some features that range from zero to one and others from one to a thousand, normalizing all features to have mean zero and variance one can make learning faster.
>  2 Batch normalization also makes weights deeper in the network more robust to changes in earlier layers. This is because of the problem of covariate shift, which occurs when the distribution of input data changes. If a network is trained on black cats and then tested on colored cats, for example, the network might not perform well. Even if the ground truth function mapping from inputs to outputs remains the same, the network might need to be retrained. Batch normalization helps reduce the amount that the distribution of hidden unit values shifts around, ensuring that the mean and variance remain the same. This makes the network more robust to changes in the input distribution.
>  3 Batch normalization works by normalizing the values in each batch, meaning that each batch has its own mean and variance. This reduces the effects of batch-to-batch variation in the network's performance. By normalizing the values, batch normalization also makes it easier for the network to learn the weights, which can improve generalization.
>  4 Batch normalization also introduces two additional parameters per activation unit, gamma and beta. These parameters can be used to shift and scale the normalized values, giving the network more flexibility to learn a wider range of functions. By controlling the means and variances of the activations, gamma and beta can help the network learn more quickly and generalize better.
>  5 There are some potential drawbacks to batch normalization, including increased computational cost and the possibility of overfitting if not used carefully. However, overall, batch normalization is a powerful technique for improving the performance and generalization of neural networks, and it is widely used in practice.

  <br>

    <a id="node-895"></a>
    <p align="center"><kbd><img src="assets/f25620b54372c5a86a8ec204dbe3dee759520bfd.png" width="100%"></kbd></p>
    > **Covariate shift.**And the idea is that, if you've learned some X to Y mapping, 
> if the distribution of X changes, then you might need to retrain 
> your learning algorithm.

    <br>

    <a id="node-896"></a>
    <p align="center"><kbd><img src="assets/60e5295aca78b17a148bd12afd441e064bd7ce9e.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/60e5295aca78b17a148bd12afd441e064bd7ce9e.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/5ff4284d724dfaee79c230e67a92c6838bbad308.png" width="100%"></kbd></p>
    > "So from the perspective of the third hidden layer, these hidden unit
> values are changing all the time, and so it's suffering from  the problem
> of covariate shift" 
> Đại khái là params được update liên tục dẫn đến cái **"DISTRIBUTION
> CỦA INPUT CỦA HIDDEN LAYER"** thay đổi liên tục nên gây khó khăn
> cho quá trình training. -> Batch Norm giúp fix vấn đề này

    <br>

    <a id="node-897"></a>
    <p align="center"><kbd><img src="assets/8d2b5a4f9c2c3c49956f5f070a81539e68988fb7.png" width="100%"></kbd></p>
    <br>

    <a id="node-898"></a>
    <p align="center"><kbd><img src="assets/0385a4bb4fb4d5a98fdf43c9b96db9ddd5410b42.png" width="100%"></kbd></p>
    > **Covariate shift:**This is the phenomenon where the
> **distribution of the inputs to a layer changes during training**,
> which makes it difficult for the network to learn. By normalizing the
> inputs to each layer, batch normalization reduces the internal
> covariate shift, which can make it easier for the network to learn.

    <br>


<a id="node-899"></a>
### Batch Norm At Test Time

<br>

<a id="node-900"></a>
- 1 Batch normalization processes data in mini batches during training.  2 During training, mean and variance are computed on the entire mini batch.  3 During test time, processing a single example at a time, you need to estimate mean and variance from training data.  4 Exponentially weighted averages are used to estimate mean and variance from training data.  5 At test time, use the estimated mean and variance to scale the test example.  6 Deep learning frameworks usually have default ways to estimate mean and variance.  7 Using batch normalization can help train deeper networks and improve learning algorithm efficiency.
  > Sure, here's a more detailed summary of the video:
>  1 Batch normalization at test time:
>  1 During training, batch normalization is done one mini-batch at a time. The mean and variance are computed on each mini-batch, and used to normalize the data.
>  2 At test time, you may not have a mini-batch of data to process, so you need to come up with a separate estimate of the mean and variance.
>  3 In typical implementations, an exponentially weighted moving average is used to estimate the mean and variance across mini-batches during training. This running average is then used at test time to normalize the data.
>  2 The benefits of using deep learning frameworks:
>  1 Deep learning frameworks provide high-level APIs that make it easier to write and train deep neural networks.
>  2 They often provide pre-trained models that you can use out-of-the-box or fine-tune for your specific use case.
>  3 They can handle low-level details like GPU optimization, distributed training, and automatic differentiation, which would be difficult and time-consuming to implement from scratch.
>  3 How to choose a deep learning framework:
>  1 Look for a framework that has good documentation and an active community.
>  2 Consider the programming language you're comfortable with, as many frameworks support multiple languages.
>  3 Look for a framework that has the features you need for your specific use case, such as support for specific types of layers or optimization algorithms.
>  4 Common deep learning frameworks:
>  1 TensorFlow: A popular framework developed by Google that is known for its scalability and support for distributed training.
>  2 PyTorch: Another popular framework that is known for its ease of use and flexibility. It is often preferred by researchers and academics.
>  3 Keras: A high-level API that can run on top of TensorFlow or other backends. It is known for its simplicity and ease of use.
>  4 Caffe: A framework developed by Berkeley that is known for its speed and efficiency on image-based tasks.

  <br>

    <a id="node-901"></a>
    <p align="center"><kbd><img src="assets/cc25442e818add2c24b37fb5d3dee6dbf37d2e8a.png" width="100%"></kbd></p>
    > But that test time, you might need to process a single example at
> a time. So, the way to do that is to estimate mu and sigma
> squared from your training set and there are many ways to do
> that. You could **in theory run your whole training set through
> your final  network to get mu and sigma squared**. But in
> practice, what people  usually do is implement and exponentially
> weighted average where  you **just keep track of the mu and
> sigma squared values you're  seeing during training** and use
> and exponentially the weighted  average, also sometimes called
> the running average, to just get a  rough estimate of mu and
> sigma squared and then you use those  values of mu and sigma
> squared that test time to do the scale and  you need the head
> and unit values Z

    <br>


<a id="node-902"></a>
## Multiclass Classification

<br>


<a id="node-903"></a>
### Clarification About Upcoming Softmax

<br>

<a id="node-904"></a>
- ...
  <br>

    <a id="node-905"></a>
    <p align="center"><kbd><img src="assets/1db5e507f513fcfaefc7d52ed274c068d31a233b.png" width="100%"></kbd></p>
    <br>


<a id="node-906"></a>
### Softmax Regression

<br>

<a id="node-907"></a>
- 1 \\*Binary\\* \\*classification\\* involves two possible labels, \\*0\\* or \\*1\\*.  2 \\*Softmax\\* \\*regression\\* is a \\*generalization\\* of \\*logistic regression\\* used for recognizing \\*multiple classes\\*.  3 Softmax regression uses a \\*Softmax\\* \\*layer\\* to generate the \\*probabilities\\* for \\*each of the classes\\*.  4 The number of \\*units\\* in the \\*Softmax\\* layer is \\*equal to the number of classes\\*.  5 The \\*Softmax\\* \\*activation\\* \\*function\\* computes a temporary variable, t, which is e to the power of the output of the final layer.  6 The output of the Softmax activation function, aL, is the vector t normalized to sum to 1.  7 The i-th element of the output vector aL represents the p\\*robability of the input belonging to the i-th class\\*.  8 The \\*probabilities\\* generated by the Softmax layer should \\*sum to 1.\\*
  > 1 Softmax regression is a generalization of logistic regression for multiple classes. Instead of just recognizing two classes, Softmax regression allows you to recognize one of C possible classes, where C is the number of classes you're trying to categorize your inputs into.
>  2 To use Softmax regression, you need to build a new neural network where the upper layer has C units. The goal is for each unit to output the probability of its corresponding class, given the input x.
>  3 The output labels y hat in Softmax regression are a C by 1 dimensional vector, where each element represents the probability of its corresponding class.
>  4 Because probabilities should sum to one, the elements in y hat should also sum to one.
>  5 The standard model for Softmax regression uses a Softmax layer in the output layer to generate these probabilities. The Softmax activation function is used to compute the output of the final layer.
>  6 The Softmax activation function takes the linear part of the layer (zL) and computes a temporary variable (t), which is e to the zL (element-wise). Then, the output aL is computed by normalizing t to sum to one. This ensures that the elements in aL represent probabilities that sum to one.
>  7 In the Softmax layer, the output aL is a C by 1 dimensional vector, where each element represents the probability of its corresponding class. The i-th element of aL is computed as ti divided by the sum of all the ti's, where ti is the i-th element of the vector t.
>  8 An example is given to illustrate how the Softmax activation function works. In the example, zL is a four-dimensional vector: 5, 2, -1, 3. Using the Softmax activation function, we compute t, which is e to the 5, e to the 2, e to the -1, e to the 3. We then normalize t to sum to one, which gives us the output aL, where each element represents the probability of its corresponding class.

  <br>

    <a id="node-908"></a>
    <p align="center"><kbd><img src="assets/c12aef050ebe1d2bb471a8f655e95ab5e629fb47.png" width="100%"></kbd></p>
    <br>

    <a id="node-909"></a>
    <p align="center"><kbd><img src="assets/363986a61a44690f28159a8b3998aede4fb49d2b.png" width="100%"></kbd></p>
    <br>

    <a id="node-910"></a>
    <p align="center"><kbd><img src="assets/21328144842995694b151f69eb6ff53a5be09250.png" width="100%"></kbd></p>
    <br>

  <a id="node-911"></a>
  - 1 Softmax regression is a generalization of logistic regression for multiple classes. Instead of just recognizing two classes, Softmax regression allows you to recognize \\*one of C possible classes,\\* where C is the number of classes you're trying to categorize your inputs into.  2 To use Softmax regression, you need to build a new neural network where the upper layer has C units. The goal is for each unit to output the probability of its corresponding class, given the input x.  3 The output labels y hat in Softmax regression are a C by 1 dimensional vector, where each element represents the \\*probability of its corresponding class.\\*  4 Because \\*probabilities should sum to one\\*, the \\*elements in y hat should also sum to one.\\*  5 The standard model for Softmax regression uses a \\*Softmax layer\\* in the output layer to generate these probabilities. The Softmax activation function is used to compute the output of the final layer.  6 The \\*Softmax\\* activation function takes the\\* linear part\\* of the layer (\\*zL\\*) and computes a temporary variable (t), which is e to the zL (element-wise). Then, the output aL is computed by normalizing t to sum to one. This ensures that the elements in aL \\*represent probabilities that sum to one.\\*  7 In the Softmax layer, the output aL is a C by 1 dimensional vector, where each element represents the probability of its corresponding class. The i-th element of aL is computed as ti divided by the sum of all the ti's, where ti is the i-th element of the vector t.  8 An example is given to illustrate how the Softmax activation function works. In the example, zL is a four-dimensional vector: 5, 2, -1, 3. Using the Softmax activation function, we compute t, which is e to the 5, e to the 2, e to the -1, e to the 3. We then normalize t to sum to one, which gives us the output aL, where each element represents the probability of its corresponding class.
    <br>


<a id="node-912"></a>
### Training A Softmax Classifier

<br>

<a id="node-913"></a>
- 1 Softmax activation function was introduced in the previous video and in this video, we will deepen our understanding of softmax classification and learn about the training model that uses a softmax layer.  2 Softmax classification generalizes the logistic activation function to C classes and if C=2, then softmax with C=2 essentially reduces to logistic regression.  3 The loss function used in softmax classification is the negative sum of j=1 through C of yj log yhat j, where yj is the true label and yhat j is the predicted probability of the class j.  4 The loss function tries to make the corresponding probability of the true class as high as possible, which is a form of \\*maximum likelihood estimation.\\*  5 To reduce the loss on the training set, the neural network adjusts the predicted probability of the true class.
  > 1 Softmax activation function: In the previous video, you learned about the softmax activation function, which is used in the output layer of neural networks to classify data into multiple classes. It takes in a vector of inputs and outputs a vector of probabilities that sum up to 1.
>  2 Softmax classification: In this video, you deepen your understanding of softmax classification, which is a way to classify data using the softmax activation function. Softmax regression or the softmax identification function generalizes the logistic activation function to C classes rather than just two classes.
>  3 Softmax vs. hard max: The name softmax comes from contrasting it to what's called a hard max which would have taken the vector Z and matched it to a vector of zeros and ones. A hard max function will look at the elements of Z and just put a 1 in the position of the biggest element of Z and then 0s everywhere else. In contrast, a softmax is a more gentle mapping from Z to probabilities.
>  4 Training a neural network with softmax output layer: To train a neural network with a softmax output layer, you need to define a loss function that measures the difference between the predicted probabilities and the ground truth labels. The loss function used in softmax classification is the negative sum of the products of the ground truth labels and the logarithm of the predicted probabilities.
>  5 Loss function example: Let's take an example of an image of a cat that falls into Class 1, and the ground truth label is 0 1 0 0. Let's say that the neural network is currently outputting a vector of probabilities of 0.1, 0.4, 0.2, and 0.3. The loss function for this example would be -log(0.4), which is the negative logarithm of the predicted probability of Class 2, the ground truth class.
>  6 Maximizing probability of ground truth class: To minimize the loss function, the neural network needs to maximize the probability of the ground truth class. This is achieved by adjusting the weights and biases in the network using backpropagation and gradient descent. If the learning algorithm is trying to make the loss function small, then the only way to do that is to make the probability of the ground truth class as high as possible.

  <br>

    <a id="node-914"></a>
    <p align="center"><kbd><img src="assets/04af685d99db92bab7fddbc4e8aba423bfc0d86a.png" width="100%"></kbd></p>
    <br>

    <a id="node-915"></a>
    <p align="center"><kbd><img src="assets/ed039abb8d7b695ac51fbec1e90557d99f11291b.png" width="100%"></kbd></p>
    > Hiểu đại khái Machine nó sẽ muốn làm gì:
> Muốn min L thì phải min Sum y_iLog(y^_i), mà y_1, y_3, y_4 = 0 
> -> Phải min y_2log(y^_2) mà y_2 = 1 
> -> Phải min log(y^_2)
> -> Phải max y^_2
>
> Softmax thật ra là mở rộng khái quát hoá của Logistic Regression

    <br>

    <a id="node-916"></a>
    <p align="center"><kbd><img src="assets/84e4d61c75aaddae0c91d28bfea655738953392d.png" width="100%"></kbd></p>
    > Programming assignment này sẽ bắt đầu dùng Framework 
> (TensorFlow) nên chỉ cần ForProp, BackProp nó sẽ làm giùm
> mình nhưng đại khái cũng giống cách tính BackProp bữa trước
> làm thôi, chỉ có cái là h y nó có C hàng chứ 1 ko phải 1 hàng

    <br>


<a id="node-917"></a>
## Introduction To Programming Frameworks

<br>


<a id="node-918"></a>
### Deep Learning Frameworks

<br>

<a id="node-919"></a>
- 1 Deep learning algorithms can be implemented from scratch using Python and NumPY, but more complex models may require the use of deep learning software frameworks.  2 Implementing everything yourself from scratch becomes increasingly impractical as models get larger and more complex.  3 There are now many good deep learning software frameworks available to help implement complex models, such as convolutional neural networks and recurring neural networks.  4 Choosing a framework depends on several factors, including ease of programming, running speeds, and whether or not the framework is truly open.  5 Some popular deep learning frameworks include TensorFlow, PyTorch, Keras, and Caffe.  6 Each of these frameworks has a dedicated user and developer community, and each is a credible choice for some subset of applications.  7 The criteria recommended for choosing a framework include ease of programming, running speeds, and whether or not the framework is truly open.  8 Truly open frameworks are those that are not only open source but also have good governance and are not under the control of a single company.  9 Multiple frameworks could be a good choice depending on the user's preferences and the application they are working on.  10 Using a deep learning software framework can make development of machine learning applications more efficient by providing a higher level of abstraction than just a numerical linear algebra library.
  <br>

    <a id="node-920"></a>
    <p align="center"><kbd><img src="assets/40121657e9cd545242c30ffc1046290ebfaaaf46.png" width="100%"></kbd></p>
    > Đại khái là khi làm các bài toán lớn thì sử dụng các lib sẽ giúp 
> ta tiện hơn

    <br>

    <a id="node-921"></a>
    <p align="center"><kbd><img src="assets/061fb0179eeb6b83843fe1efeec50696c5bf5612.png" width="100%"></kbd></p>
    > Các Framework này improve liên tục và đây là 1 số tiêu chí để chọn F.W

    <br>


<a id="node-922"></a>
### Tensorflow

<br>

  <a id="node-923"></a>
  <p align="center"><kbd><img src="assets/a3205cc52dfabc3f229ff70f8c0e2c64c0d6dc64.png" width="100%"></kbd></p>
  <br>

  <a id="node-924"></a>
  <p align="center"><kbd><img src="assets/83d6874166906fe82e975959254bccf0b625f0b6.png" width="100%"></kbd></p>
  <br>

  <a id="node-925"></a>
  <p align="center"><kbd><img src="assets/aca3baee5eb4dc673d48741183f4c8505e219160.png" width="100%"></kbd></p>
  > Đại khái là T.S nó sẽ tự tính BackProp

  <br>


<a id="node-926"></a>
### Learn About Gradient Tape And More

<br>

  <a id="node-927"></a>
  <p align="center"><kbd><img src="assets/96abb2e33fc8883d599c592e335174490cdffa22.png" width="100%"></kbd></p>
  <br>


<a id="node-928"></a>
## Quiz

<br>

<a id="node-929"></a>

<p align="center"><kbd><img src="assets/bfe87b33fda9737ef130d858bf8843471e67e300.png" width="100%"></kbd></p>

<br>

<a id="node-930"></a>

<p align="center"><kbd><img src="assets/4bff75269233d9cbb62993876bb718ecd7617ac3.png" width="100%"></kbd></p>

> [!NOTE]
> Không 'equally' vì rõ ràng Alpha quan trọng hơn Epsilon nhiều

<br>

<a id="node-931"></a>

<p align="center"><kbd><img src="assets/537f41235c7fa79ad0e62568b412479b3d70681c.png" width="100%"></kbd></p>

> [!NOTE]
> Này quá rõ, nếu máy mạnh thì chạy nhiều cái cùng lúc

<br>

<a id="node-932"></a>

<p align="center"><kbd><img src="assets/10aab4ec6f5014c901d5e19b27d18338109cfdcc.png" width="100%"></kbd></p>

<br>

<a id="node-933"></a>

<p align="center"><kbd><img src="assets/7ee889085db41133efb9b84fd7e861ed6ee18982.png" width="100%"></kbd></p>

<br>

<a id="node-934"></a>

<p align="center"><kbd><img src="assets/39a9070dd5f63dfab40669c0705b2d821f8b2b9d.png" width="100%"></kbd></p>

<br>

<a id="node-935"></a>

<p align="center"><kbd><img src="assets/ac7815a56df0178dc9d4c8ec9a9fa3abc5883610.png" width="100%"></kbd></p>

<br>

<a id="node-936"></a>

<p align="center"><kbd><img src="assets/e0d88890e714c865212f263c5226e81f4f71851c.png" width="100%"></kbd></p>

> [!NOTE]
> Beta gammar được train như Web bằng G.D ...nên câu
> đầu sai, câu 2 đúng.
>
> Beta[l], gammae[l] cũng như, b[l] là. vector mỗi unit 1 cái
> nên không phải là 1 R cho cả layer -> Câu 3 sai
>
> Câu 4 sai vì ko phải là Optimal value, mà đó là value khiến
> cho  Gamma và Beta vô nghĩa (Khiến Z~ bằng Z)
>
> Câu 5 đúng

<br>

<a id="node-937"></a>

<p align="center"><kbd><img src="assets/ac0ca4cda7a8f47c813dba37ba13d8ec65a98d28.png" width="100%"></kbd></p>

> [!NOTE]
> Sai vì vẫn có tính Batch Norm

<br>

<a id="node-938"></a>

<p align="center"><kbd><img src="assets/d97ecc61091735e60c834c68cb32c64fc5e702ff.png" width="100%"></kbd></p>

<br>


<a id="node-939"></a>
## Programming Assignment

<br>


<a id="node-940"></a>
### Introduction to TensorFlow

<br>

<a id="node-941"></a>
- .
  <br>

    <a id="node-942"></a>
    <p align="center"><kbd><img src="assets/9f6d06116bd9eebe99d66b86f80af3f6ae3254ce.png" width="100%"></kbd></p>
    <br>

    <a id="node-943"></a>
    <p align="center"><kbd><img src="assets/f82f309fbb8b5fb55aebc584fc211abb3e0b7a81.png" width="100%"></kbd></p>
    <br>

<a id="node-944"></a>
- Checking TensorFlow Version
  <br>


<a id="node-945"></a>
### 2 - Basic Optimization with GradientTape

<br>


<a id="node-946"></a>
### Basic Optimization with GradientTape

<br>

  <a id="node-947"></a>
  <p align="center"><kbd><img src="assets/3ff430888f386d6acceddf8ba33d4180806db6d1.png" width="100%"></kbd></p>
  <p align="center"><kbd><img src="assets/3ff430888f386d6acceddf8ba33d4180806db6d1.png" width="100%"></kbd></p>
  <p align="center"><kbd><img src="assets/a5969ed2b9543280c485e7ddbcd1a64608118075.png" width="100%"></kbd></p>
  <br>

  <a id="node-948"></a>
  <p align="center"><kbd><img src="assets/ebf721009f53405f9f7fb86b83164e13abdb45ac.png" width="100%"></kbd></p>
  <br>

  <a id="node-949"></a>
  <p align="center"><kbd><img src="assets/608a1e1fdd7f413fb14207979c9049677c579faf.png" width="100%"></kbd></p>
  <br>


<a id="node-950"></a>
### 2.1 - Linear Function

> [!NOTE]
> Làm quen với TF Khai báo
> Constant với tf.constant() .
> tf.matmul(), tf.add() Tính
> thử Y = WX + b bằng T.F

<br>

  <a id="node-951"></a>
  <p align="center"><kbd><img src="assets/2a565b792af3d3048ee9c3e4823e0b6ef0472a3c.png" width="100%"></kbd></p>
  <br>

<a id="node-952"></a>
- Exercise 1 - linear_function
  <br>

    <a id="node-953"></a>
    <p align="center"><kbd><img src="assets/6cf0c7b9a668e47e4fd105cde816260de6902a1d.png" width="100%"></kbd></p>
    <br>

    <a id="node-954"></a>
    <p align="center"><kbd><img src="assets/70b72bada95c1e78f9ebc668460878535a390e0e.png" width="100%"></kbd></p>
    <br>


<a id="node-955"></a>
### 2.2 - Computing the Sigmoid

> [!NOTE]
> Làm quen với TF
> tf.keras.activation.sigmoid()
> tf.cast(.., tf.float32)

<br>

  <a id="node-956"></a>
  <p align="center"><kbd><img src="assets/c11c349a66027cd38cee7ef974c43f6b0d23d1ce.png" width="100%"></kbd></p>
  <br>

<a id="node-957"></a>
- Exercise 2 - sigmoid
  <br>

    <a id="node-958"></a>
    <p align="center"><kbd><img src="assets/ce245fbc898bd82898517a45002ad7150323c3e1.png" width="100%"></kbd></p>
    <br>

    <a id="node-959"></a>
    <p align="center"><kbd><img src="assets/40b2cdaea766709a6180819dda5b87b588d20b31.png" width="100%"></kbd></p>
    <br>


<a id="node-960"></a>
### 2.3 - Using One Hot Encodings

> [!NOTE]
> One hot encoding with TF
> Dùng tf.one_hot(labels, depth)
> và tf.reshape(.., [-1, ]) để

<br>

  <a id="node-961"></a>
  <p align="center"><kbd><img src="assets/7e0a7a7ade524978c6baf9a954b98e7806b202af.png" width="100%"></kbd></p>
  <br>

<a id="node-962"></a>
- Exercise 3 - one_hot_matrix
  <br>

    <a id="node-963"></a>
    <p align="center"><kbd><img src="assets/fb919ac8238a9c43d17af8d8d7cfc0bdb1903eda.png" width="100%"></kbd></p>
    <br>

    <a id="node-964"></a>
    <p align="center"><kbd><img src="assets/5927bb05c449dc6bc7d97e789747c66ea4097bd1.png" width="100%"></kbd></p>
    <br>

    <a id="node-965"></a>
    <p align="center"><kbd><img src="assets/7abc8f6d18432a302d897d436721b8978f817a24.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/7abc8f6d18432a302d897d436721b8978f817a24.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/ae154354de5e7d3bc324dabcb53ca385addcc360.png" width="100%"></kbd></p>
    > Argument -1 có nghĩa là để nó tự chuyển thành 1D vector size bằng
> mấy cái kia nhân lại (dồn lại hết thành 1 row)

    <br>


<a id="node-966"></a>
### 2.4 - Initialize the Parameters

> [!NOTE]
> Initialize bằng GlorotNormal.

<br>

  <a id="node-967"></a>
  <p align="center"><kbd><img src="assets/a1083478ffb25c518635d0618720e7280005fdf6.png" width="100%"></kbd></p>
  <br>

<a id="node-968"></a>
- Exercise 4 - initialize_parameters
  <br>

    <a id="node-969"></a>
    <p align="center"><kbd><img src="assets/c26a481dcaf20c8290bba848e9692f053b3f6004.png" width="100%"></kbd></p>
    <br>

    <a id="node-970"></a>
    <p align="center"><kbd><img src="assets/206cdcc3584383a94dc0737513ff6c711b2a72f1.png" width="100%"></kbd></p>
    <br>


<a id="node-971"></a>
### 3 - Building Your First Neural Network in TensorFlow

<br>


<a id="node-972"></a>
### 3.2 Compute the Total Loss

> [!NOTE]
> Viết hàm tính loss function dùng TF's 
> categorical_crossentropy(logits, labels)
>
> Cứ tưởng kẹt ở Excersie này, người ta đã gợi ý là phải đảm
> bảo argument's shape đúng mà. Có điều không có nói vụ 
> **from_logits** khiến mò mãi mới đúng
>
> 1. Chú ý thứ tự argument, **(labels, logits)**
>
> 2. Vì yêu cầu shape = (no. examples - m, no. features - n) nên
> phải **transpose**. Với TF, dùng **tf.transpose()**
> 3.Phải thêm**from_logits = True**mới đúng

> [!NOTE]
> **from_logits = True** có nghĩa là Y^ (output của last layer
> trong n.n) vẫn ở dạng 'raw output', không phải dạng '
> Probability'.
>
> Layer cuối cùng nó để Linear (tức là tính tính Z3 = Z[L] =
> W[L]. A[L-1] + b[L] và không tính A[L] hay nói cách khác g[L] =
> L (không áp dụng hàm rêu hay sigmoid gì cả)  Để rồi mới bỏ
> Z[L] đó vào Softmax để tính ra Probability
>
> Thì đây cũng vậy, cái mà mình bỏ vào cùng với y là Z, là **raw
> output** chứ không phải là **Probability** nên phải ghi rõ
> **from_logit = True**Nếu không ghi, hoặc để = false, hàm categorical_crossentropy
> sẽ apply **Softmax** (tính ra Probability) rồi mới tính Loss

<br>

  <a id="node-973"></a>
  <p align="center"><kbd><img src="assets/b2fa02fe317ca7a45ecd5876e3ab2ec7acb40397.png" width="100%"></kbd></p>
  <br>

<a id="node-974"></a>
- Exercise 6 - compute_total_loss
  <br>

    <a id="node-975"></a>
    <p align="center"><kbd><img src="assets/07f8a8e5f9085d43bf29abaf1366c181d36174f9.png" width="100%"></kbd></p>
    <br>

    <a id="node-976"></a>
    <p align="center"><kbd><img src="assets/42221c6f2dfb16883c1333a378ddaefb46e3863d.png" width="100%"></kbd></p>
    <br>

    <a id="node-977"></a>
    <p align="center"><kbd><img src="assets/e82454c69961df5dbbca765f8ca92baebe19ff00.png" width="100%"></kbd></p>
    > **from_logits = True** có nghĩa là Y^ (output của last layer
> trong n.n) vẫn ở dạng 'raw output', không phải dạng '
> Probability'.
>
> Nhớ lại, layer cuối cùng nó để Linear (tức là tính tính Z[L] =
> W[L]. A[L-1] + b[L] và không tính A[L] hay nói cách khác g[L] =
> L (không áp dụng hàm rêu hay sigmoid gì cả)  Để rồi mới bỏ
> Z[L] đó vào Softmax để tính ra Probability
>
> Thì đây cũng vậy, cái mà mình bỏ vào cùng với y là Z, là **raw
> output** chứ không phải là **Probability** nên phải ghi rõ
> **from_logit = True**Nếu không ghi, hoặc để = false, hàm categorical_crossentropy
> sẽ apply **Softmax** (tính ra Probability) rồi mới tính Loss

    <br>

    <a id="node-978"></a>
    <p align="center"><kbd><img src="assets/4c99bf9b6280fa9b93cce49eebb329ee8f9fd0fa.png" width="100%"></kbd></p>
    <br>


<a id="node-979"></a>
### 3.1 - Implement Forward Propagation

> [!NOTE]
> Forward Prop với tf
> Thay vì dùng np.dot(), relu() thì dùng 
> tf.matmul(), tf.add() và 
> tf.keras.activations.relu()

<br>

  <a id="node-980"></a>
  <p align="center"><kbd><img src="assets/7fdc18d5ab6fb62eedaa5cec11cb30ee9f3dba88.png" width="100%"></kbd></p>
  <br>

<a id="node-981"></a>
- Exercise 5 - forward_propagation
  <br>

    <a id="node-982"></a>
    <p align="center"><kbd><img src="assets/18279cc5ab18d5a83acb775b1ded2d3b4841b337.png" width="100%"></kbd></p>
    <br>

    <a id="node-983"></a>
    <p align="center"><kbd><img src="assets/7952b6db7c378a6f57261289e05da544d1f1c5ae.png" width="100%"></kbd></p>
    <br>


<a id="node-984"></a>
### 3.3 - Train the Model

> [!NOTE]
> Build modal để train dùng TF

<br>

  <a id="node-985"></a>
  <p align="center"><kbd><img src="assets/424571c4fe314777b969317dbac13bf5c07374fd.png" width="100%"></kbd></p>
  <br>

  <a id="node-986"></a>
  <p align="center"><kbd><img src="assets/cfaf94165721a923b8b06e4f44ff06d435a75328.png" width="100%"></kbd></p>
  <br>

  <a id="node-987"></a>
  <p align="center"><kbd><img src="assets/74e55811fff02c6b2da8c2c827b48fb7288b3e16.png" width="100%"></kbd></p>
  <br>

  <a id="node-988"></a>
  <p align="center"><kbd><img src="assets/d2052cd995dd9b75cd70127acd6b7aa94f6fc86e.png" width="100%"></kbd></p>
  <br>

  <a id="node-989"></a>
  <p align="center"><kbd><img src="assets/c146253b79f3a44c6850dfc41b5fc6462044e845.png" width="100%"></kbd></p>
  <br>

  <a id="node-990"></a>
  <p align="center"><kbd><img src="assets/86ffc53d0838469fcc007b029a66ff3ff8a3e8a4.png" width="100%"></kbd></p>
  <br>

<a id="node-991"></a>
- optimizer = tf.keras.optimizers. Adam(learning_rate)
  > Dùng optimizer Adam

  <br>

<a id="node-992"></a>
- dataset = tf.data.Dataset. zip((X_train, Y_train))
  > Đại khái là nó giúp tạo 1 Dataset modal
> để dùng cho  training bằng TF

  <br>

    <a id="node-993"></a>
    <p align="center"><kbd><img src="assets/fdfc99b3f71375fb0902827c3e9008bff5ae7751.png" width="100%"></kbd></p>
    <br>

<a id="node-994"></a>
- grads = tape. gradient(minibatch_total_loss, trainable_variables)
  > Notice the tape.gradient function: this allows you to
> retrieve the operations recorded for **automatic
> differentiation** inside the GradientTape block.
>
> Đây chính là bước T.F giúp mình tính Gradient dW1, db1, dW2, db2..

  <br>

    <a id="node-995"></a>
    <p align="center"><kbd><img src="assets/fcb5c2a2e9a545f77f148a15d499f2336333d5b8.png" width="100%"></kbd></p>
    <br>

<a id="node-996"></a>
- optimizer. apply_gradients(zip(grads, trainable_variables))
  > Then, calling the optimizer method
> **apply_gradients**, will apply the optimizer's
> update rules to each trainable parameter.
>
> Đây chính là bước mà T.F nó update W1, b1,
> W2, b2... với dW1, db1, dW2, db2...
>
> Và với optimizer là Adam thì nó sẽ update theo 
> kiểu Adam: Momentum + RMSProp

  <br>

    <a id="node-997"></a>
    <p align="center"><kbd><img src="assets/66684d089354ed031ecf80e43860ac7b150aadfe.png" width="100%"></kbd></p>
    <br>

<a id="node-998"></a>
- minibatches = dataset. batch(minibatch_size).prefetch(8)
  > Đại khái là bước này giúp chuẩn bị mini-batch 
> - **Chia data thành từng Mini-batch**, và **load trước 
> 8 cái (prefetch(8))** để khi chạy cái này thì luôn có 
> sẵn 8 cái giúp nhanh hơn

  <br>

    <a id="node-999"></a>
    <p align="center"><kbd><img src="assets/8d6de4d722c5e812f53f6dec04b779166086ae6d.png" width="100%"></kbd></p>
    <br>

<a id="node-1000"></a>
- #We need to reset object to start measuring from 0 the accuracy each epoch train_accuracy.reset_states()  # We accumulate the accuracy of all the batches train_accuracy.update_state(minibatch_Y, tf.transpose(Z3))
  > CategoricalAccuracy của TF này giúp tính độ ' accuracy'
> của Z3 và Y. Mỗi iteration/epoch reset lại để train xong thì
> update

  <br>

    <a id="node-1001"></a>
    <p align="center"><kbd><img src="assets/718c388365dcb62d73edb639b0f74f1717120155.png" width="100%"></kbd></p>
    <br>

<a id="node-1002"></a>
- costs.append(epoch_total_loss)             train_acc.append(train_accuracy.result())             test_acc.append(test_accuracy.result())
  > Sau mỗi lần train-update params (mỗi
> iteration). cứ 100 lần thì ghi lại cót,
> accuracy để tí nữa plot ra

  <br>


<a id="node-1003"></a>
### 4 - Bibliography

<br>


<a id="node-1004"></a>
## References

> [!NOTE]
> In this assignment, you were introducted to tf.GradientTape, which records operations for differentation. Here are a couple of resources for diving deeper into what it does and why:
> Introduction to Gradients and Automatic Differentiation: \_https://www.tensorflow.org/guide/autodiff\_
> GradientTape documentation: \_https://www.tensorflow.org/api_docs/python/tf/GradientTape\_

<br>

<a id="node-1005"></a>

<p align="center"><kbd><img src="assets/c5fdfce22077619f92cd9a2eaeb1267fa8326708.png" width="100%"></kbd></p>

<br>

