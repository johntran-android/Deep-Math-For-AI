# C2w2_optimization Algorithms

📊 **Progress:** `49` Notes | `102` Screenshots

---

<a id="node-706"></a>
## Mini-batch Gradient Descent

<br>


<a id="node-707"></a>
### 1 Introduction to **optimization algorithms** for **faster neural network training**.

> [!NOTE]
> 1 Introduction to **optimization algorithms** for **faster neural network training**.
>
> 2 **Vectorization** allows for **processing large training sets** without an explicit For
> loop.
>
> 3 Gradient descent algorithm requires **processing the entire training set** before
> taking one step.
>
> 4 Mini-batch gradient descent algorithm involves dividing training sets into
> **mini-batches** and **processing them iteratively** for faster training.
>
> 5 Mini-batches consist of a **subset of the training set** and are processed in a
> For loop using one step of gradient descent.
>
> 6 The dimensions of XT and YT for mini-batches are MX by 1,000 and 1 by 1,
> 000, respectively.
>
> 7 The mini-batch gradient descent algorithm is **more efficient** than the batch
> gradient descent algorithm for large training sets.

> [!NOTE]
> Sure, I'd be happy to provide more detail on the main ideas presented in the text.
>  1 Optimization algorithms for faster training: The text introduces the concept of optimization algorithms, which can enable faster training of neural networks. As machine learning is an iterative and empirical process, it often involves training a large number of models to find one that performs well. However, training on large datasets can be slow, so having efficient optimization algorithms can speed up the process and improve efficiency for teams.
>  2 Mini-batch gradient descent: The text goes on to explain mini-batch gradient descent, which is an optimization algorithm that enables faster training of neural networks. Instead of processing the entire training set at once, mini-batch gradient descent splits the data into smaller subsets called mini-batches. These mini-batches typically contain around 1,000 examples each.
>  3 Notation for mini-batches: The text introduces new notation to represent mini-batches. X superscript curly braces 1 through 5,000 represents the input data for each mini-batch, while Y superscript curly braces 1 through 5,000 represents the corresponding output data.
>  4 Implementation of mini-batch gradient descent: To run mini-batch gradient descent, the text explains that you would run a For loop for T equals 1 to 5,000, representing the 5,000 mini-batches. Inside the loop, one step of gradient descent is implemented using the mini-batch XT, YT. This allows progress to be made even before the entire training set has been processed, resulting in faster training times.
>  5 Vectorization for processing large datasets: The text also mentions that vectorization can be used to process all m examples in a training set relatively quickly. However, when m is very large (e.g., 5 million or 50 million), even vectorization can be slow. Mini-batch gradient descent allows progress to be made with smaller subsets of the data, enabling faster training times overall.
>  6 Comparison to batch gradient descent: The text notes that mini-batch gradient descent is different from batch gradient descent, which processes the entire training set at once. While batch gradient descent is sometimes referred to as "batch" because it processes the entire set at once, mini-batch gradient descent is so-named because it processes smaller subsets (i.e., mini-batches) of the data.
> Overall, the text provides an overview of mini-batch gradient descent as an optimization algorithm for faster training of neural networks. It introduces new notation for mini-batches and explains how the algorithm is implemented. It also highlights the importance of optimization algorithms in improving efficiency for machine learning teams.

<br>

<a id="node-708"></a>

<p align="center"><kbd><img src="assets/d1bfe1d08634dc8ca5ed2b5ec0ff2abd58be510d.png" width="100%"></kbd></p>

  <br>

<a id="node-709"></a>

<p align="center"><kbd><img src="assets/9dc85a029e744bde8e41a702905e57df2a3239b0.png" width="100%"></kbd></p>

  <br>

<a id="node-710"></a>

<p align="center"><kbd><img src="assets/12130e9b94754d445b8cffb54244f644700d7fc8.png" width="100%"></kbd></p>

> [!NOTE]
> **Epoc chính là số Iteration** thôi 
> Trong mỗi epoch/Iteration:
>
> Đ/v **mini batch**: nó sẽ chạy lần lượt tất
> cả các mini-batch ví dụ có 10 mini-batch thì nó update w,b **10 lần.**
>
> Còn đ/v **batch**: thì mỗi epoch nó chạy hết toàn bộ m data rồi update
> w,b **1 lần**
>
> Còn đ/v **Stochastic** thì để mỗi epoc / iteration nó chạy từng dataset
> và mỗi lần chạy nó update w,b 1 lần -> mỗi epoch/iteration nó update
> W,b **1000 lần. -> Câu dưới ChatGPT nó trả lời sai ở chỗ Stochastic**

  <br>

<a id="node-711"></a>

<p align="center"><kbd><img src="assets/b02775b6d8015ba06d8f9c96fa8646b0430736c2.png" width="100%"></kbd></p>

  <br>

<a id="node-712"></a>

<p align="center"><kbd><img src="assets/5cde8c6e894016f86510a25d1fff4631cdd7bb31.png" width="100%"></kbd></p>

  <br>

<a id="node-713"></a>
- Sure, I'd be happy to provide more detail on the main ideas presented in the text.  1 **Optimization algorithms** for **faster** training: The text introduces the concept of **optimization algorithms**, which can **enable faster training** of neural networks. As machine learning is an iterative and empirical process, it often involves training a large number of models to find one that performs well. However, training on large datasets can be slow, so having efficient optimization algorithms can speed up the process and improve efficiency for teams.  2 **Mini-batch gradient** **descent**: The text goes on to explain mini-batch gradient descent, which is an optimization algorithm that enables **faster training** of neural networks. Instead of processing the entire training set at once, mini-batch gradient descent **splits the data into smaller subsets** called **mini-batches**. These mini-batches typically contain around **1,000** **examples** each.  3 Notation for mini-batches: The text introduces new notation to represent mini-batches. X superscript curly braces 1 through 5,000 represents the input data for each mini-batch, while Y superscript curly braces 1 through 5,000 represents the corresponding output data.  4 Implementation of mini-batch gradient descent: To run mini-batch gradient descent, the text explains that you would run a **For loop** for T equals 1 to 5,000, representing the 5,000 mini-batches. Inside the loop, **one step of gradient descent is implemented using the mini-batch** XT, YT. This **allows progress to be made even before the entire training set has been processed**, resulting in **faster training times.**  5 **Vectorization** for processing large datasets: The text also mentions that vectorization can be used to process all m examples in a training set relatively quickly. **However, when m is very large** (e.g., 5 million or 50 million),**even vectorization can be slow**. Mini-batch gradient descent allows progress to be made with smaller subsets of the data, enabling faster training times overall.  6 **Comparison** to batch gradient descent: The text notes that mini-batch gradient descent is different from batch gradient descent, which **processes the entire training set at once**. While batch gradient descent is sometimes referred to as "**batch**" because it processes the entire set at once, mini-batch gradient descent is so-named because it processes smaller subsets (i.e., mini-batches) of the data.  Overall, the text provides an overview of mini-batch gradient descent as an **optimization algorithm** for faster training of neural networks. It introduces new notation for mini-batches and explains how the algorithm is implemented. It also highlights the importance of optimization algorithms in improving efficiency for machine learning teams.
  <br>


<a id="node-714"></a>
## Understanding Mini-batch Gradient Descent

<br>


<a id="node-715"></a>
### 1 The **cost function should decrease on every iteration** of batch

> [!NOTE]
> 1 The **cost function should decrease on every iteration** of batch
> gradient descent.
>
> 2 Mini-batch gradient descent **may not decrease the cost function
> on every iteration** due to training on different mini-batches.
>
> 3 **The size of the mini-batch** used in gradient descent is a
> **parameter that needs to be chosen**.
>
> 4 A **mini-batch size** of **m** results in **batch** gradient descent, while a
> mini-batch size of **1** results in **stochastic** gradient descent.
>
> 5 **Batch** gradient descent takes **too much time per iteration** for a
> large training set, while **stochastic** gradient descent can be
> **extremely noisy**.
>
> 6 The mini-batch size used in practice is usually somewhere in
> between **1 and m**, as these values are respectively too small and
> too large.

> [!NOTE]
> 1 Mini-batch gradient descent allows for progress to be made even when the entire training set has not been processed yet. The cost function J(t) may not decrease on every iteration due to processing different mini-batches X(t), Y(t), resulting in a noisier trend downwards.
>  2 The size of the mini-batch is a parameter that needs to be chosen. The two extremes are:
>  • Batch gradient descent, where the mini-batch size is equal to the training set size m. In this case, the entire training set is processed on every iteration.
>  • Stochastic gradient descent, where the mini-batch size is equal to 1. In this case, each example is its own mini-batch, and the gradient descent step is taken with just a single training example at a time.
>  3 Batch gradient descent can take relatively large steps with low noise, but takes too long per iteration when processing a large training set. Stochastic gradient descent can be extremely noisy and won't ever converge, but is faster per iteration when processing a small training set.
>  4 In practice, the mini-batch size used will be somewhere between 1 and m. If the mini-batch size is too small, then the noise from processing individual examples will be too high. If the mini-batch size is too large, then the time per iteration will be too long. A good mini-batch size allows for a balance between the two.

<br>

<a id="node-716"></a>

<p align="center"><kbd><img src="assets/9a45cafdc9f5a762b4473f849c8a22c6524174e9.png" width="100%"></kbd></p>

  <br>

<a id="node-717"></a>

<p align="center"><kbd><img src="assets/13268cd70749a55cd0f790f8af66bd39d04b7da2.png" width="100%"></kbd></p>

> [!NOTE]
> Mini batch size = m thì chính là \/**Batch:**\/Với data lớn thì nó 
> rất lâu vì mỗi lần 'chạy' g.d là nó phải tính toàn bộ data 
>
> Mini batch size = 1 thì ta có \/**Stochastic**\/
> Ưu điểm của nó là **cho ra 'progress' ngay chỉ với 1 training sample.**
> Và cái vấn đề 'zig zac / noisy' của nó có thể cải thiện bằng
> cách chọn learning rate nhỏ hơn.
> Tuy nhiên Stochastic có nhược điểm là coi như vứt bỏ sức 
> mạnh của **vectorization**

> [!NOTE]
> Chỉ với **mini batch** thì có được cả 2 ưu điểm:
> - **Progress mà không phải đợi tính hết cả bộ data**
> - Vẫn tận dụng được sức mạnh của **vectorization**

  <br>

<a id="node-718"></a>

<p align="center"><kbd><img src="assets/5ca5355b972e2e7a880710675b829b82cb7ca028.png" width="100%"></kbd></p>

> [!NOTE]
> - Nếu training size nhỏ thì không cần mini-batch làm gì ví dụ 
> <**2000**. Còn lớn hơn thì nên dùng mini batch.
>
> - **Thử nhiều giá trị** **mini-batch size 2^6, 2^7**... Typical use là 
> 64-512. 
>
> - Đảm bảo mini batch data **fit CPU/GPU memory** -> Cái này 
> phải thì  tuỳ vào application và data gì nhưng đại khái phải 
> check, nếu không nó sẽ fail

  <br>

<a id="node-719"></a>
- 1 Mini-batch gradient descent **allows for progress** to be made even w**hen the entire training set has not been processed yet**. The cost function J(t) may **not decrease on every iteration** due to processing different mini-batches X(t), Y(t), resulting in a **noisier trend downwards.**  2 The **size** of the mini-batch is a **parameter that needs to be chosen**. The two extremes are:  • **Batch** gradient descent, where the mini-batch size is equal to the training set size **m**. In this case, the entire training set is processed on every iteration.  • **Stochastic** gradient descent, where the mini-batch size is equal to **1**. In this case, **each example is its own mini-batch**, and the gradient descent step is taken with just a single training example at a time.  3 **Batch** gradient descent can take relatively **large steps** with **low noise**, but takes **too long per iteration** when processing a**large training set**. **Stochastic** gradient descent can be **extremely noisy** and **won't ever converg**e, but is **faster** per iteration when processing a **small** training set.  4 In practice, the **mini-batch size** used will be s**omewhere between 1 and m**. If the mini-batch size is **too small**, then the **noise** from processing individual examples will be too high. If the mini-batch size is **too large**, then the time per iteration will be **too long**. A good mini-batch size allows for a **balance** between the two.
  <br>


<a id="node-720"></a>
## Exponentially Weighted Averages

<br>


<a id="node-721"></a>
### 1 The speaker wants to show some **optimization algorithms** that are

> [!NOTE]
> 1 The speaker wants to show some **optimization algorithms** that are
> **faster than gradient descent.**
>
> 2 To understand these algorithms, it is necessary to understand
> **exponentially weighted averages**, also known as **exponentially
> weighted moving averages.**
>
> 3 The speaker provides an example of **how to compute** exponentially
> weighted averages using the d**aily temperature data from London**.
>
> 4 The formula for computing exponentially weighted averages is
> given, and its general formula is presented.
>
> 5 The speaker explains how to **vary the parameter beta** to obtain
> **different effect**s, such as a **smoother** or **noisier** curve, or **faster** or
> **slower adaptation** to temperature changes.
>
> 6 Varying **beta** is a **hyperparameter** that can be tuned to optimize
> learning algorithms.

> [!NOTE]
> 1 Introduction: The speaker wants to introduce a few optimization algorithms that are faster than gradient descent.
>  2 Exponentially Weighted Averages: To understand these algorithms, it is important to understand exponentially weighted averages, also known as exponentially weighted moving averages in statistics.
>  3 Temperature Data Example: The speaker provides an example of daily temperature data from London over the course of a year.
>  4 Computation of Moving Average: In order to compute the trends or moving average of the temperature, the speaker proposes a formula using an exponentially weighted average. The formula initializes V0 to zero and then averages it with a weight of 0.9 times the previous value plus 0.1 times the temperature of that day. The more general formula is V on a given day is 0.9 times V from the previous day plus 0.1 times the temperature of that day.
>  5 Plotting the Moving Average: The computed moving average is plotted in red and shows a smoother curve than the original data.
>  6 Varying the Beta Parameter: The speaker then discusses how varying the beta parameter in the formula can lead to different effects. A high beta value results in a smoother curve but more latency in adapting to temperature changes, while a low beta value results in a noisier curve but quicker adaptation to temperature changes.
>  7 Importance of Choosing the Right Beta Value: The speaker notes that the choice of beta value is a hyperparameter that can affect the performance of a learning algorithm and that there is usually some value in between that works best.

<br>

<a id="node-722"></a>

<p align="center"><kbd><img src="assets/2ddb8333ed4d05695476d4d2dabea05e440eef96.png" width="100%"></kbd></p>

  <br>

<a id="node-723"></a>

<p align="center"><kbd><img src="assets/8c66e6213809b415393a3b0e5b0f08ccf9ac5375.png" width="100%"></kbd></p>

> [!NOTE]
> Beta lớn -> **Lấy nhiều ảnh hưởng của quá khứ**, 
> **giảm ảnh hưởng của hiện tại** 
> -> **Trễ nhận ra sự thay đổi hơn**
> -> **Đường cong smooth hơn** do nó thay đổi 
> chậm hơn
>
> Ngược lại nó **nhạy hơn,** đường cong nó **wiggly hơn**.

  <br>

<a id="node-724"></a>

<p align="center"><kbd><img src="assets/b0154b8afd16f112f4770242f0dfc0f8a32089c7.png" width="100%"></kbd></p>

> [!NOTE]
> Ngược lại beta nhỏ -> nó nhạy hơn, đường cong nó wigly hơn.

  <br>

<a id="node-725"></a>
- 1 Introduction: The speaker wants to introduce a few optimization algorithms that are f**aster** than g**radient descent.**  2 **Exponentially Weighted Averages**: To understand these algorithms, it is important to understand exponentially weighted averages, also known as **exponentially weighted moving averages** in statistics.  3 **Temperature** Data Example: The speaker provides an example of **daily temperature data**from London over the course of a year.  4 **Computation** of Moving Average: In order to compute the trends or moving average of the temperature, the speaker proposes a formula using an **exponentially weighted average**. The formula initializes **V0** to zero and then averages it with a **weight of 0.9 times** the**previous value** plus**0.1 times** the temperature **of that day**. The more general formula is V on a given day is 0.9 times V from the previous day plus 0.1 times the temperature of that day.  5 Plotting the Moving Average: The computed moving average is plotted in red and shows a **smoother** curve than the original data.  6 Varying the **Beta** Parameter: The speaker then discusses how**varying the beta paramete**r in the formula can **lead to different effects**. A **high beta** value results in a **smoother curve** but more **latency in adapting to temperature changes**, while a l**ow beta** value results in a **noisier curve** but **quicker adaptation** to temperature changes.  7 Importance of **Choosing the Right Beta** **Value**: The speaker notes that the choice of beta value is a **hyperparameter** that can affect the performance of a learning algorithm and that there is usually some value in between that works best.
  <br>


<a id="node-726"></a>
## Understand Exponentially Weighted Averages

<br>


<a id="node-727"></a>
### 1 **Exponentially weighted averages**is a **key** **component** of several optimization

> [!NOTE]
> 1 **Exponentially weighted averages**is a **key** **component** of several optimization
> algorithms used to train neural networks.
>
> 2 The video delves deeper into intuitions for understanding the algorithm.
>
> 3 The **key equation** for implementing exponentially weighted averages is
> presented.
>
> 4 **Different values of beta** result in different **exponentially decaying functions**.
>
> 5 The algorithm computes averages of daily temperatures.
>
> 6 The equation for computing V100 is derived.
>
> 7 **V100** is a **weighted average of theta values**, where the **weight decays
> exponentially over time**.
>
> 8 The daily temperature is multiplied by an **exponentially decaying function** and
> then **summed up to compute V100**.
>
> 9 All **coefficients** add up to one, or very close to one, up to a detail called **bias
> correction.**
>
> 10 It takes about **10 days** for the height of the **exponentially decaying function** to
> **decay** to around **1/3** or one over **e** of the peak.
>
> 11 When **beta equals 0.9,** the algorithm is as if computing an **exponentially
> weighted average** that focuses on the **last 10 days' temperature.**

> [!NOTE]
> 1 In the last video, we learned about exponentially weighted averages (EWAs), which are a key component of several optimization algorithms used to train neural networks.
>  2 In this video, the focus is on understanding the intuition behind EWAs and how they compute averages of daily temperature.
>  3 The key equation for implementing EWAs is presented, which includes a parameter called beta that determines the weight given to past values.
>  4 Different values of beta result in different weights for past values, and the resulting graph shows an exponentially decaying function.
>  5 To understand how this function is computing averages of daily temperature, the equation is rearranged with decreasing values of T.
>  6 This rearranged equation is then used to calculate V100, which is the average of theta values from day 100 to day 1.
>  7 The coefficients of the theta values in the equation can be expanded out and simplified, showing that V100 is a weighted sum of theta values.
>  8 This sum of theta values is weighted by an exponentially decaying function, which results in a graph that decays exponentially from theta 100 to theta 1.
>  9 The value of beta determines how quickly the weight given to past values decays, with larger values resulting in slower decay.
>  10 The number of days that the EWA averages over can be calculated based on the value of beta, with beta equal to 0.9 resulting in an average over the last 10 days.
>  11 More generally, if beta is 1-epsilon, where epsilon is small, then the EWA averages over approximately 1/epsilon days.
>  12 This video provides a detailed understanding of the intuition behind EWAs and how they work to compute averages of daily temperature.

<br>

<a id="node-728"></a>

<p align="center"><kbd><img src="assets/236b9fa43885d4eada6ac024710499e47a0fe893.png" width="100%"></kbd></p>

  <br>

<a id="node-729"></a>

<p align="center"><kbd><img src="assets/02e7f3bd055681f89844577ded38950d5470c436.png" width="100%"></kbd></p>

  <br>

<a id="node-730"></a>

<p align="center"><kbd><img src="assets/74f2c2f79364d99c8c46ec0dd002a0e565040313.png" width="100%"></kbd></p>

  <br>

<a id="node-731"></a>

<p align="center"><kbd><img src="assets/ba5384901ab58e67fa283fe80d48e5a56ca6e0ed.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ..V100 sau khi triển khai thành ra:
>
> = 0.1*θ_100 + 0.1*0.9^1*θ_99 + 0.1*0.9^2*θ_98 +...
>
> thì đại khái là 2 cái này element-wised nhân nhau rồi sum up
>
> [θ_1,...θ_99, θ_100]
>
> và
>
> [... 0,1*0.9^2, 0,1*0.9, 0.1] = là hàm gọi là **exponentially decaying function**2. Cái nữa mà ổng sẽ nói thêm sau là các coefficient 
> 0.1 + 0,1*0.9^1 + 0.1*0.9^2 ...~= 1 mà gọi là **correctness bias** gì đó

> [!NOTE]
> Thì điều này đại khái đồng nghĩa là nếu **beta = 0,9** tương đương **eps = 0.1** thì
> kiểu như vt sẽ là average của 10 ngày trước đó cái này chưa hiểu lắm

  <br>

<a id="node-732"></a>

<p align="center"><kbd><img src="assets/04b111df0774085cf8cd70fdf8bb96d9854a042c.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là **exponentially decaying function** có quy luật là
>
> (1-eps)**(1/eps) = 1/e ~= 0.3
>
> là sau 1/eps ngày thì value **giảm còn** ~= 1/3 ban đầu
> Ví dụ eps = 0.1 thì mất 10 ngày
> Ví dụ eps = 0.02 thì mất 50 ngày

  <br>

<a id="node-733"></a>

<p align="center"><kbd><img src="assets/5b5898e939915580668fd07cc29d911653965cb5.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là implement như thế nào thì
> trong code không có v1,v2,...mà là
> repeatedly assigning

  <br>

<a id="node-734"></a>
- 1 In the last video, we learned about **exponentially weighted averages** (EWAs), which are a **key component** of several optimization algorithms used to train neural networks.  2 In this video, the focus is on understanding the intuition behind EWAs and how they compute averages of daily temperature.  3 The**key equation** for implementing EWAs is presented, which includes a parameter called **beta** that determines the **weight given to past values**.  4 **Different** **values** of **beta** result in **different weights for past values**, and the resulting graph shows an exponentially decaying function.  5 To understand how this function is computing averages of daily temperature, the equation is **rearranged** with decreasing values of T.  6 This **rearranged** **equation** is then used to **calculate V100**, which is the average of theta values from day 100 to day 1.  7 The **coefficients** of the **theta** **values** in the equation can be expanded out and simplified, showing that V100 is a weighted sum of theta values.  8 This sum of theta values is weighted by an **exponentially decaying function**, which results in a graph that **decays exponentially from theta 100 to theta 1.**  9 The value of **beta** determines **how quickly the weight given to past values decays**, with **larger values resulting in slower decay.** 10 The number of days that the **EWA** averages over can be calculated based on the value of **beta**, with beta equal to 0.9 resulting in an average over the last 10 days.  11 More generally, if beta is **1-epsilon**, where **epsilon is small,** then the **EWA** averages over **approximately 1/epsilon days.**  12 This video provides a **detailed understanding** of the intuition behind EWAs and how they work to compute averages of daily temperature.
  <br>


<a id="node-735"></a>
## Bias Correction In Exponentially Weighted Averages

<br>


<a id="node-736"></a>
### 1 **Exponentially weighted moving averages** can be used to \\*smooth out

> [!NOTE]
> 1 **Exponentially weighted moving averages** can be used to **smooth out
> noisy data** and **capture trends** over time.
>
> 2 When implementing **exponential moving averages,** **bias correction** can
> **improve accuracy**, especially during the**initial phas**e of the estimate.
>
> 3 Without bias correction, the e**stimate may start off much lower than
> expected**, leading to a **biased assessment.**
>
> 4 To correct this bias, instead of using **V_t** as the estimate, we use **V_t
> divided by 1-Beta^t**, where t is the current day.
>
> 5 As **t becomes large**, **Beta to the t approaches 0**, so **bias correction
> becomes less important**.
>
> 6 Implementing bias correction can help obtain a **better estimate of the
> data** during the **initial phase of learning**.
>
> 7 While most implementations of exponentially weighted moving averages
> **do not include bias correction**, it can be **useful in certain situations**.
>
> 8 With these concepts, we can build **better optimization algorithm**s using
> **exponential moving averages.**

<br>

<a id="node-737"></a>

<p align="center"><kbd><img src="assets/afcdc0b8c89c9d05b68f8b7a8f1d86098535cf06.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là với cách tính 'Exponentially weighted average'
> thì những lúc đầu t nhỏ, bởi vì initialize v_0 = 0 nên đại khái là
> giá trị tính ra sai lệch rất lớn so với giá trị thực tế.
>
> Cách khắc phục là 'Bias correction', sau khi tính vt thì chia cho 
> (1-beta^t)
>
> Thì giai đoạn đầu với t nhỏ, -> việc điều chỉnh v_t = v_t/(1-beta^t)
> sẽ giúp **fix sự sai lệch trên.** 
>
> Ví dụ trong hình ổng nói nếu không có B.C, thì v_1 chỉ bằng 0.02 theta_1,
> v_2 chỉ bằng 0,0196 theta_1 + 0,02 theta_2 đại khái là nhỏ hơn rất nhiều theta_2 
> -> Dẫn đến sai lệch ở khúc đầu
>
> Còn khi chia cho 1 - beta**t thì :
>
> v_1 = v_1/(1-0.98**1) = 0.02theta_1/0.02 = bằng ra lại theta_2 -> Hết lệch
>
> v_2 = v_2/(0.0396) = ..nói chung là việc chia cho term này giúp 'khôi
> phục' - có thể không nguyên vẹn nhưng khắc phục tình trạng cách biệt lớn ban đầu.
>
> Giai đoạn sau, t lớn, beta^t tiến về 0 -> 1-beta^1 tiến về 1 
> -> **hiệu ứng của Bias correction mất dần.**

  <br>


<a id="node-738"></a>
## Gradient Descent With Momentum

<br>


<a id="node-739"></a>
### 1 The Momentum algorithm or **Gradient Descent with Momentum** is an

> [!NOTE]
> 1 The Momentum algorithm or **Gradient Descent with Momentum** is an
> **optimization algorithm** that works **faster** than **standard Gradient Descent.**
>
> 2 The basic idea is to compute an **exponentially weighted average** of the
> **gradients** and use that to update weights instead of using the gradients
> themselves.
>
> 3 Gradient Descent often **oscillates** and takes many steps to reach the
> minimum, **preventing** the use of **larger learning rates.**
>
> 4 **Momentum** **smooths out** the steps of Gradient Descent by taking a **more
> straightforward path** and **damping out the oscillations to the minimum.**
>
> 5 Momentum can be **viewed as** providing **acceleration** to a **ball rolling down a
> bowl-shaped function** and **momentum terms** **represent velocity**.
>
> 6 The algorithm involves**computing the derivatives**, computing **vdW** and **vdb**,
> and updating the **weights** using vdW and vdb.
>
> 7 Momentum works for some people as an **analogy** of a ball rolling down a
> bowl but may not work for everyone.

> [!NOTE]
> 1 The video discusses the algorithm called momentum, or gradient descent with momentum, which almost always works faster than the standard gradient descent algorithm.
>  2 The basic idea of the momentum algorithm is to compute an exponentially weighted average of the gradients and use that gradient to update the weights instead of using the usual gradient.
>  3 The standard gradient descent algorithm often takes many steps and oscillates towards the minimum because it cannot use a large learning rate due to the oscillations.
>  4 The momentum algorithm smooths out the steps of gradient descent by computing a moving average of the derivatives for w. It averages out the oscillations in the vertical direction, where slowing things down is desired, and takes steps that are much smaller in the vertical direction but are more directed to moving quickly in the horizontal direction.
>  5 The momentum algorithm works by computing vdW to be Beta vdw plus 1 minus Beta dW, where Beta is a hyperparameter between 0 and 1, and similarly computing vdb.
>  6 The weights are updated using W gets updated as W minus the learning rate times vdW, and similarly, b gets updated as b minus alpha times vdb.
>  7 An analogy to understand the momentum algorithm is to think of the derivatives providing acceleration to a ball that is rolling down a hill, while the momentum terms represent velocity.
>  8 The momentum algorithm prevents the ball from speeding up without limit by applying a row of friction, which is similar to how the momentum algorithm applies the Beta hyperparameter.
>  9 Finally, the video presents the algorithm and its implementation details.

<br>

<a id="node-740"></a>

<p align="center"><kbd><img src="assets/730440d486c3f9cba543b27be6093ed6a767263c.png" width="100%"></kbd></p>

> [!NOTE]
> Vấn đề của G.D là nó sẽ bị **zic zac** ở 1 phương không mong muốn
> (một feature nào đó, hiểu đại khái thôi). Nên ta phải khắc phục bằng
> cách **khống chế learning rate alpha**. Nhưng điều này lài làm chậm
> quá trình G.D. Đại khái là chúng ta bị một mâu thuẫn là **muốn 
> G.D đi mạnh ở cái hướng mà nó sẽ tới minimum** (muốn vậy phải để
> Alpha lớn) nhưng lại phải **khống chế cái phương tán loạn kia** để nó
> không bị 'Diverge') (muốn vậy phải để alpha nhỏ.) Do đó 
> G.D không thể nhanh được.
>
>
> Đại khái thay vì update W, b bởi dW, db
> thì nay ta update bởi **vdW**, **vdb**
> trong đó vdW, vcb tính bằng phương pháp **'Exponentially weighted 
> average'**
>
> Đại khái hệ quả là làm cho 'đường đi' của Gradient Descent nó
> **bớt zic zac/ tán loạn** về phương ngang (đang lấy ví dụ như trong 
> hình) mà **bước dài hơn về phương dọc** (là phương sẽ đến minimum)

> [!NOTE]
> Advantages of gradient descent with momentum over traditional 
> gradient descent include:
>  1 Faster Convergence: Momentum helps **accelerate 
> gradient descent in the right direction**, thus speeding up 
> convergence. It helps to **overcome the problems of oscillations
>  or getting stuck in local minima**, which are commonly faced in 
> traditional gradient descent.
>  2 Stabilization: Gradient descent with momentum tends to 
> **dampen oscillations and moves more smoothly towards the 
> minimum**. This can lead to faster convergence and better results.
>
>  3 Handling of sparse gradients: **Sparse gradients** occur 
> when the gradient vector has **mostly zero entrie**s. Momentum helps 
> to overcome this problem by **accumulating the gradient information**
> over multiple iterations, providing a **more robust update**.
>
> Overall, gradient descent with momentum provides a better 
> optimization experience compared to traditional gradient descent. 
> However, **it is important to note that the choice of optimization 
> algorithm depends on the specific problem, and it is always a good 
> idea to experiment with different optimization algorithms**to 
> determine which one works best for a given problem.

> [!NOTE]
> Cũng chưa hiểu tại sao lại tương đương việc vận tốc với gia
> tốc momentum gì đó trong bài toán ball roll down the hill

  <br>

<a id="node-741"></a>

<p align="center"><kbd><img src="assets/b4529500452976ddf20d8d4abbc6bfd3099fc935.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là có 2 phiên bản, cái nào cũng được.
> 1 cái là vdw = beta*vdw + (1-beta)*dw 
> 1 cái bỏ cái 1-beta đi mà tính vdw = beta*vdw + dw luôn
>
> Riêng mr Andrew prefer cái đầu hơn. 
>
> Beta thường chọn là 0.9 còn alpha phải tune riêng
>
> Và trong thực tế người ta cũng không bias correction vì sau chừng
> 10 iteration là hiện tượng (sai lệch ban đầu này) cũng không còn

> [!NOTE]
> Finally, I just want to mention that if you read the literature on gradient descent with
> momentum often you see it with this term omitted, with this 1 minus Beta term
> omitted. So you end up with vdW equals Beta vdw plus dW. And the net effect of
> using this version in purple is that vdW ends up being scaled by a factor of 1 minus
> Beta, or really 1 over 1 minus Beta.
>
> And so when you're performing these gradient descent updates, alpha just
> needs to change by a corresponding value of 1 over 1 minus Beta. In practice,
> both of these will work just fine, it just affects what's the best value of the learning
> rate alpha.
>
> But I find that this particular formulation is a little less intuitive. Because one impact
> of this is that if you end up tuning the hyperparameter Beta, then this affects the
> scaling of vdW and vdb as well. And so you end up needing to retune the learning
> rate, alpha, as well, maybe.
>
> Chưa hiểu khúc này lắm nhưng chắc cũng không quan trọng mấy mà đại khái là
> nó chỉ ảnh hưởng chút đến best value của alpha

  <br>

<a id="node-742"></a>
- 1 The video discusses the **algorithm** called **momentum**, or **gradient descent with momentum**, which almost always works **faster** than the **standard gradient descent algorithm.**  2 The basic idea of the momentum algorithm is to compute an **exponentially weighted average of the gradients** and **use that gradient to update the weights instead of using the usual gradient.**  3 The standard gradient descent algorithm often takes many steps and **oscillates** towards the minimum because it cannot use a l**arge learning rate** due to the **oscillations**.  4 The momentum algorithm **smooths out the steps** of gradient descent by **computing a moving average of the derivatives for w**. It **averages out the oscillations** in the **vertical direction**, **where** **slowing things down is desired**, and **takes steps that are much smaller in the vertical direction** but are **more directed to moving quickly in the horizontal direction.**  5 The momentum algorithm works by computing **vdW** to be **Beta vdw plus 1 minus Beta dW**, where Beta is a **hyperparameter** between 0 and 1, and similarly computing **vdb**.  6 The weights are updated using **W gets updated as W minus the learning rate times vdW**, and similarly, b gets updated as b minus alpha times vdb.  7 An analogy to understand the momentum algorithm is to think of the **derivatives** providing **acceleration** to a ball that is **rolling down a hill**, while the **momentum terms represent velocity.** 8 The **momentum** algorithm **prevents the ball from speeding up without limit by applying a row of friction**, which is similar to how the momentum algorithm applies the Beta hyperparameter.  9 Finally, the video presents the algorithm and its implementation details.
  <br>


<a id="node-743"></a>
## Rmsprop

<br>


<a id="node-744"></a>
### 1 RMSprop is another algorithm that can**speed up gradient descent,** and it aims to

> [!NOTE]
> 1 RMSprop is another algorithm that can**speed up gradient descent,** and it aims to
> **slow down learning in the vertical direction** and **speed up learning in the horizontal
> direction**.
>
> 2 On each iteration, RMSprop computes the**derivative of the parameters on the
> current mini-batch**, then keeps an **exponentially weighted average** of the **squares of
> these derivatives.**
>
> 3 **RMSprop** updates the parameters by dividing the **derivative** of each **parameter** by
> the **square root** of the**exponentially weighted average** of the **squares of the
> derivatives of that parameter.**
>
> 4 The effect of this is that the **updates in the vertical direction** **are divided by a much
> larger number**, which helps **damp out oscillations**, whereas the **updates in the
> horizontal direction are divided by a smaller number.**
>
> 5 In practice, **RMSprop** is used in a **high-dimensional space of parameters**, and it can
> **damp out oscillations** in a **subset of parameters.**
>
> 6 RMSprop stands for **Root Mean Squared Prop** because it **squares** the derivatives and
> then takes the**square root at the end.**
>
> 7 To avoid division by zero, RMSprop adds a s**mall epsilon to the denominator.**
>
> 8 In the next video, RMSprop will be combined with momentum.

> [!NOTE]
> 1 What is RMSprop and how does it work?
>  2 RMSprop is another algorithm, in addition to momentum, that can speed up gradient descent. It stands for root mean square prop and it is designed to slow down the learning in the vertical direction and speed up learning in the horizontal direction. To accomplish this, on each iteration, RMSprop computes the derivative of the current mini-batch as usual, then it keeps an exponentially weighted average of the squares of the derivatives, which is denoted as SdW and Sdb. These terms are updated as follows: SdW = beta * SdW + (1 - beta) * dW^2 and Sdb = beta * Sdb + (1 - beta) * db^2, where beta is a hyperparameter and the squaring operation is an element-wise operation. Next, RMSprop updates the parameters as follows: W = W - learning_rate * dW / sqrt(SdW) and b = b - learning_rate * db / sqrt(Sdb), where learning_rate is the hyperparameter that controls how big of a step is taken during each iteration.
>  3 How does RMSprop help with oscillations in the vertical direction?
>  4 RMSprop helps with oscillations in the vertical direction by slowing down the learning rate in that direction. This is achieved by keeping a larger value of Sdb, which is the exponentially weighted average of the squares of the derivatives in the vertical direction. The derivatives in the vertical direction tend to be much larger than those in the horizontal direction, due to the steep slope of the function in the vertical direction. As a result, Sdb will be relatively large, and when db is divided by sqrt(Sdb) in the update equation for b, the resulting update will be much smaller than in the horizontal direction, effectively damping out the oscillations in the vertical direction.
>  5 How does RMSprop help with faster learning in the horizontal direction?
>  6 RMSprop helps with faster learning in the horizontal direction by speeding up the learning rate in that direction. This is achieved by keeping a smaller value of SdW, which is the exponentially weighted average of the squares of the derivatives in the horizontal direction. The derivatives in the horizontal direction tend to be much smaller than those in the vertical direction, due to the gentle slope of the function in the horizontal direction. As a result, SdW will be relatively small, and when dW is divided by sqrt(SdW) in the update equation for W, the resulting update will be much larger than in the vertical direction, effectively allowing for faster learning in the horizontal direction.
>  7 How is RMSprop applied in practice?
>  8 In practice, RMSprop is applied by computing the derivatives of the current mini-batch as usual, then keeping an exponentially weighted average of the squares of the derivatives in each dimension of the parameter vector. The resulting terms SdW and Sdb are used to update the parameters in each dimension, with a learning rate that is scaled by the inverse square root of SdW or Sdb, respectively. To prevent division by zero, a small constant is added to SdW and Sdb before taking the square root. Additionally, a hyperparameter beta is used to control the weighting of the current and previous values in the exponential moving averages of SdW and Sdb, respectively. In practice, beta is typically set to a value between 0.9 and 0.99.

<br>

<a id="node-745"></a>

<p align="center"><kbd><img src="assets/7b3984bbfe124eb1a1b8e17e87ad91a7bbce2138.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là với **param nào mà khiến G.D đi sai hướng - oscillate**,
> ví dụ ở đây cho dễ hình dung là b, thì **average weight của nó
> sẽ lớn** -> việc **chia db cho sqrt(sdb)** sẽ làm **b nhỏ lại** -> **Giảm bớt 
> ảnh hường của b, giảm bớt oscillation**
>
> Ngược lại với weight/param nào khiến G.D đi đúng hướng, 
> ở đây ví dụ là w, thì nó ít oscillation -> sdw nhỏ -> dw chia 
> cho sqrt(sdw) không ảnh hưởng mấy đến w -> giữ hướng 
> đi đúng đó.

> [!NOTE]
> Bài sau sẽ kết hợp momentum và
> RMSProp nên đánh beta2 để phân biệt.
>
> Thêm epsilon để không bị chia cho 0

  <br>

<a id="node-746"></a>
- 1 What is RMSprop and how does it work?  - RMSprop is **another algorithm**, in addition to momentum, that can **speed up gradient descen**t. It stands for **root** **mean** **square** **prop** and it is designed to**slow down the learning in the vertical direction** and **speed up learning in the horizontal direction**. To accomplish this, on each iteration, RMSprop **computes the derivative of the current mini-batch** as usual, then it keeps an **exponentially weighted average** **of the squares of the derivatives**, which is denoted as **SdW** and **Sdb**. These terms are updated as follows: SdW = beta * SdW + (1 - beta) * dW^2 and Sdb = beta * Sdb + (1 - beta) * db^2, where beta is a hyperparameter and the squaring operation is an element-wise operation. Next, RMSprop updates the parameters as follows: **W = W - learning_rate * dW / sqrt(SdW)** and b = b - learning_rate * db / sqrt(Sdb), where learning_rate is the hyperparameter that controls how big of a step is taken during each iteration.  2 How does RMSprop help with oscillations in the vertical direction?  - RMSprop helps with oscillations in the vertical direction by slowing down the learning rate in that direction. This is achieved by keeping a larger value of Sdb, which is the exponentially weighted average of the squares of the derivatives in the vertical direction. The derivatives in the vertical direction tend to be much larger than those in the horizontal direction, due to the steep slope of the function in the vertical direction. As a result, Sdb will be relatively large, and when db is divided by sqrt(Sdb) in the update equation for b, the resulting update will be much smaller than in the horizontal direction, effectively damping out the oscillations in the vertical direction.  3 How does RMSprop help with faster learning in the horizontal direction?  - RMSprop helps with faster learning in the horizontal direction by speeding up the learning rate in that direction. This is achieved by keeping a smaller value of SdW, which is the exponentially weighted average of the squares of the derivatives in the horizontal direction. The derivatives in the horizontal direction tend to be much smaller than those in the vertical direction, due to the gentle slope of the function in the horizontal direction. As a result, SdW will be relatively small, and when dW is divided by sqrt(SdW) in the update equation for W, the resulting update will be much larger than in the vertical direction, effectively allowing for faster learning in the horizontal direction.  4 How is RMSprop applied in practice?  - In practice, RMSprop is applied by computing the derivatives of the current mini-batch as usual, then keeping an exponentially weighted average of the squares of the derivatives in each dimension of the parameter vector. The resulting terms SdW and Sdb are used to update the parameters in each dimension, with a learning rate that is scaled by the inverse square root of SdW or Sdb, respectively. To prevent division by zero, a small constant is added to SdW and Sdb before taking the square root. Additionally, a hyperparameter beta is used to control the weighting of the current and previous values in the exponential moving averages of SdW and Sdb, respectively. In practice, beta is typically set to a value between 0.9 and 0.99.
  <br>


<a id="node-747"></a>
## Clarification About Upcoming Adam Optimization Video

<br>


<a id="node-748"></a>
### ...

<br>

<a id="node-749"></a>

<p align="center"><kbd><img src="assets/b4ab7ac8d93def7617818b836074cf4daf6bc573.png" width="100%"></kbd></p>

  <br>


<a id="node-750"></a>
## Adam Optimization Algorithm

<br>


<a id="node-751"></a>
### 1 Introduction:  2 During the history of deep learning, many optimization algorithms were

> [!NOTE]
> 1 Introduction:  2 During the history of deep learning, many optimization algorithms were
> proposed by researchers, but few generalize well across a wide range of neural networks.
> The deep learning community developed **skepticism** about new optimization algorithms,
> preferring to **use gradient descent with momentum** as a **reliable approach**.
>
> 3 **RMSprop** and **Adam Optimization Algorithm:**  4 RMSprop and the Adam optimization
> algorithm are two algorithms that have been shown to **work well across a wide range of
> deep learning architectures**. The Adam optimization algorithm is a **combination** of
> **momentum** and **RMSprop**. It uses hyperparameters **Beta_1** and **Beta_2** to calculate the
> **moving** **weighted** **average** **of the derivatives and their squares**.
>
> 5 Implementation of Adam:  6 To implement Adam, we first initialize **V_dw**, **V_db**, **S_dw**,
> and **S_db** to zero. We then compute the derivatives, dw, and db, using mini-batch gradient
> descent, and calculate the momentum and RMSprop updates using **Beta_1** and **Beta_2**.
> **Bias correction** is implemented **to correct** V_dw, V_db, S_dw, and S_db. Finally, the
> weights are updated using the learning rate hyperparameter **Alpha** and the **RMSprop-like**
> update.
>
> 7 Hyper-parameters and Tuning:  8 The Adam optimization algorithm has several
> **hyper-parameters** that need to be tuned, including **Alpha**, **Beta_1**, **Beta_2**, and **Epsilon**.
> Alpha is the learning rate and needs to be tuned, while default values of Beta_1, Beta_2,
> and Epsilon are often used. Beta_1 computes the mean of the derivatives, and Beta_2 is
> used to compute the exponentially weighted average of the squares. The term Adam
> stands for **Adaptive** **Moment** **Estimation**.
>
> 9 Conclusion and Further Discussion:  10 The Adam optimization algorithm is an **effective
> learning algorithm** that allows for quicker training of neural networks. However, tuning the
> hyperparameters is necessary for optimal performance.

<br>

<a id="node-752"></a>

<p align="center"><kbd><img src="assets/67ccd6413397727de339740a25ca88bde752e7b6.png" width="100%"></kbd></p>

> [!NOTE]
> Adam algorithm kết hợp giữa momentum g.d và RMSprop

  <br>

<a id="node-753"></a>

<p align="center"><kbd><img src="assets/656a4ace380abf0d456d9a1b4cdf65ad40b31353.png" width="100%"></kbd></p>

> [!NOTE]
> Các hyperparam beta1, beta2, epsilon thường dùng và chỉ cần
> tune Alpha. và Adam không liên quan gì ông này Adam Coat

  <br>


<a id="node-754"></a>
## Clarification About Learning Rate Decay Video

<br>


<a id="node-755"></a>
### ...

<br>

<a id="node-756"></a>

<p align="center"><kbd><img src="assets/fdd601f0c1ac106cf08503190240ae4b288e57c8.png" width="100%"></kbd></p>

  <br>


<a id="node-757"></a>
## Learning Rate Decay

<br>


<a id="node-758"></a>
### 1 **Learning rate** **decay** is a technique that can help **speed up** the learning algorithm by

> [!NOTE]
> 1 **Learning rate** **decay** is a technique that can help **speed up** the learning algorithm by
> **gradually reducing** the **learning rate over time**.
>
> 2 By using a **smaller** learning rate, the algorithm can **oscillate** in a **tighter region** **around
> the minimum** instead of **wandering far away** as training goes on and on.
>
> 3 One way to implement **learning rate decay** is to set the **learning rate Alpha** to be equal
> to **1 over 1 plus a paramete**r (decay rate times epoch num) times some**initial learning
> rate Alpha 0.**
>
> 4 Other than this formula for learning rate decay, there are other ways people use to
> decay the learning rate **manually**, using **exponential decay**, learning rate that decreases
> and discretizes, etc.
>
> 5 **Manual decay** is sometimes used when **training only a small number of models** and
> the **learning rate is controlled by hand**, **hour-by-hour**, **day-by-day**.
>
> 6 Next week, when we talk about **hyperparameter tuning**, there will be more **systematic
> ways** to organize all the **hyperparameters** and **efficiently search amongst them.**
>
> 7 **Learning rate decay** is usually **lower** down on the **list of things to try**, compared to
> **setting a fixed value of Alph**a and **getting it to be well-tuned**, which has a huge impact on
> training.
>
> 8 Lastly, the concept of **local optima** and **saddle points** in **neural network**s are briefly
> mentioned as a topic for future discussion.

> [!NOTE]
> 1 Learning rate decay can help speed up learning algorithms:
>  2 One way to improve learning algorithms is to implement learning rate decay, which involves slowly reducing the learning rate over time. This can help the algorithm converge more effectively and avoid getting stuck in a noisy region. The intuition behind this approach is that during the initial steps of learning, larger steps can be taken, but as learning approaches convergence, smaller steps become necessary.
>  3 Implementation of learning rate decay:
>  4 To implement learning rate decay, you can set the learning rate Alpha to be equal to 1 over 1 plus a parameter (decay rate) times the epoch num, times an initial learning rate Alpha 0. One epoch is one pass through the data, and as you iterate through the data, the learning rate gradually decreases according to this formula.
>  5 Other ways to implement learning rate decay:
>  6 In addition to the formula for learning rate decay described above, there are other ways to implement it, such as exponential decay, where Alpha is equal to some number less than 1 times epoch num times Alpha 0. There are also other formulas that people use, including a learning rate that decreases discretely over time.
>  7 Manual decay:
>  8 In some cases, people may opt for manual decay, which involves watching the model as it trains and manually adjusting the learning rate as needed. However, this method is only feasible for training a small number of models.
>  9 Choosing hyperparameters:
>  10 With the various options available for implementing learning rate decay, it can be overwhelming to select the best hyperparameters. However, systematic methods for choosing hyperparameters will be discussed in the next week's lecture.
>  11 Importance of fixed learning rate:
>  12 While learning rate decay can be helpful, setting a fixed learning rate that is well-tuned can have a huge impact on the effectiveness of learning algorithms. Learning rate decay may be a lower priority on the list of things to try when optimizing the model.
>  13 Local optima and saddle points:
>  14 In addition to discussing learning rate decay, the lecture also briefly touches on local optima and saddle points in neural networks. These concepts relate to the challenge of avoiding getting stuck in suboptimal solutions during training.

<br>

<a id="node-759"></a>

<p align="center"><kbd><img src="assets/fe9674a934de3004762263d9eab9ef4b31424253.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là với mini-bactch gradient descent với **Fixed alpha** thì 
> **J sẽ không converge chính xác về Minimum** mà sẽ **loanh quanh** khu
> vực đó. Vấn đề này có thể **tạm chấp nhận** vì dù sao mini-batch 
> giúp G.D nhanh hơn và kết quả cũng không qúa tệ.
>
> Tuy nhiên có thể improve vấn đề này bằng cách cho alpha **giảm 
> dần - Decay**

  <br>

<a id="node-760"></a>

<p align="center"><kbd><img src="assets/1d6e08abe89bd4b0583707382166e7ed098accf2.png" width="100%"></kbd></p>

  <br>

<a id="node-761"></a>

<p align="center"><kbd><img src="assets/c77a8167d090ae0cba235daeebc920e6ec69c2ed.png" width="100%"></kbd></p>

> [!NOTE]
> **Manually decay:**Đại khái là tự adjust alpha thủ công
> chỉ dc khi training vài model hàng giờ, hàng ngày liền
> thì cách này đại khái là theo dõi model và tự điều chỉnh
> alpha****If you're **training just one model at a time**, and if your
> model takes **many hours** or even many **days to train**,
> what some people would do is **just watch your model**
> as it's training over a large number of days, and then
> now you say, **oh, it looks like the learning rate slowed
> down, I'm going to decrease Alpha a little bit**.Of course,
> this works, this **manually controlling Alpha**, really **tuning
> Alpha by hand, hour-by-hour, day-by-day**. This works
> only if you're training **only a small number of model**s, but
> **sometimes people do that as well**

> [!NOTE]
> Một số cách thức decay alpha hay dùng

  <br>


<a id="node-762"></a>
## The Problem Of Local Optima

<br>


<a id="node-763"></a>
### 1 In the early days of deep learning, people were concerned about

> [!NOTE]
> 1 In the early days of deep learning, people were concerned about
> optimization algorithms getting stuck in **bad local optima**.
>
> 2 As our understanding of deep learning has advanced, **our understanding
> of local optima is changing**.
>
> 3 Most points of zero gradient in a cost function are actually **saddle points
> rather than local optima**, especially in **high-dimensional spaces**.
>
> 4 **Plateaus** can**slow down learning** and are a **problem for optimization
> algorithms**.
>
> 5 **Sophisticated** **optimization** algorithms, such as **momentum**, **RmsProp**,
> and **Adam**, can help **overcome the problem of plateaus**.
>
> 6 Our understanding of high-dimensional optimization problems is still
> evolving.

> [!NOTE]
> 1 In the early days of deep learning, people used to worry about the optimization algorithm getting stuck in bad local optima. They used to think that there were a lot of local optima in the cost function surface and that it would be easy for the optimization algorithm to get stuck in one of them.
>  2 However, as the theory of deep learning has advanced, our understanding of local optima has also changed. Most points of zero gradient in a cost function are actually saddle points rather than local optima. In a high-dimensional space, it's much more likely to run into a saddle point than a local optimum.
>  3 Plateaus can slow down learning because they are regions where the derivative is close to zero for a long time. Gradient descent will move down the surface, but because the gradient is near zero, the surface is quite flat, and it can take a long time to reach the bottom of the plateau. This is where more sophisticated optimization algorithms like momentum, RmsProp, or Adam can help speed up learning.
>  4 Algorithms like Adam can help speed up the rate at which the optimization algorithm moves down the plateau and then gets off it.
>  5 Our understanding of high-dimensional spaces is still evolving, and it's hard to have good intuitions about what these spaces really look like. However, one takeaway from this video is that we're unlikely to get stuck in bad local optima as long as we're training a reasonably large neural network with many parameters and the cost function is defined over a high-dimensional space.
>  6 The main problem in optimization is plateaus, and algorithms like momentum and Adam can help overcome this problem.

<br>

<a id="node-764"></a>

<p align="center"><kbd><img src="assets/42e631d94bfa99c4c51727fbad15ee76bed1ba79.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là trong thực tế khó gặp l**ocal optima - Stuck /
> không có đường xuống nữa** ( - vấn đề mà ML lúc trước hay
> nói đến) mà là thường là dạng **Saddle - nơi luôn có đường
> để xuống.**

  <br>

<a id="node-765"></a>

<p align="center"><kbd><img src="assets/f20d7aa1d52412c656a1f20457a5fba9ebbbf2f9.png" width="100%"></kbd></p>

> [!NOTE]
> Nên vấn đề là **không phải ta sẽ bị stuck ko xuống được
> nữa** mà là khi gặp mấy cái saddle này ta sẽ **xuống rất rất chậm**
>
> *Ta ở đây ý nói J trong quá trình training, xuống ở đây ý nói 
> việc giảm J trong quá trình G.D
>
> Và vấn đề trên đ**ã được giải quyết** bằng nhưng **Algorithm** cải tiến
> như **momentum**, **Adam**

  <br>


<a id="node-766"></a>
## Quiz

<br>

<a id="node-767"></a>

<p align="center"><kbd><img src="assets/69b9c16e95e2d4824e5071ff812db8f636b7a7f2.png" width="100%"></kbd></p>

<br>

<a id="node-768"></a>

<p align="center"><kbd><img src="assets/30db9cfbb00aeb1026268c74267f7dc31ba8c5ab.png" width="100%"></kbd></p>

<br>

<a id="node-769"></a>

<p align="center"><kbd><img src="assets/3954241927292f555c41679c65f420c38d51a52e.png" width="100%"></kbd></p>

<br>

<a id="node-770"></a>

<p align="center"><kbd><img src="assets/8cc63137f6a774917bcfaca9a44daa4181a7c78d.png" width="100%"></kbd></p>

<br>

<a id="node-771"></a>

<p align="center"><kbd><img src="assets/1bffe60c7ad2c9128de6c157391fa368e204a879.png" width="100%"></kbd></p>

<br>

<a id="node-772"></a>

<p align="center"><kbd><img src="assets/a85e643d8dcdcb5b6eed99f68db9741b6f144657.png" width="100%"></kbd></p>

<br>

<a id="node-773"></a>

<p align="center"><kbd><img src="assets/f6b7fe0cc93d663f88787be66dfec07194d6a842.png" width="100%"></kbd></p>

<br>

<a id="node-774"></a>

<p align="center"><kbd><img src="assets/3bdac62c28dcb574042f63184b6a3be15ce11e44.png" width="100%"></kbd></p>

<br>

<a id="node-775"></a>

<p align="center"><kbd><img src="assets/98e87bd0008248d9e188875f19e819fe23855e97.png" width="100%"></kbd></p>

<br>

<a id="node-776"></a>

<p align="center"><kbd><img src="assets/6b7468267f33c1d4ee40d7281a873e137e2c0c52.png" width="100%"></kbd></p>

<br>

<a id="node-777"></a>

<p align="center"><kbd><img src="assets/32ba84e77a19d0a1b5e01b655fd5638b97d8db3b.png" width="100%"></kbd></p>

<br>

<a id="node-778"></a>

<p align="center"><kbd><img src="assets/3967e66a6c6706acb209167c53aac5fa9767d019.png" width="100%"></kbd></p>

<br>


<a id="node-779"></a>
## Programming Assignment

<br>


<a id="node-780"></a>
### Optimization Methods

<br>

<a id="node-781"></a>

<p align="center"><kbd><img src="assets/bb4dce7b5b5985cd39b68e7f0d5f070ee08df792.png" width="100%"></kbd></p>

  <br>


<a id="node-782"></a>
### 1- Packages

<br>

<a id="node-783"></a>

<p align="center"><kbd><img src="assets/0ed0bd52c17b4172626a744987afee035af20dae.png" width="100%"></kbd></p>

  <br>


<a id="node-784"></a>
### 2 - Gradient Descent

<br>

<a id="node-785"></a>
- Exercise 1 - update_parameters_with_gd
> [!NOTE]
> Update params như thông thường

  <br>

    <a id="node-786"></a>
    <p align="center"><kbd><img src="assets/245526b309183749bcad6381f89825127286f246.png" width="100%"></kbd></p>
    <br>

    <a id="node-787"></a>
    <p align="center"><kbd><img src="assets/ceaa17e9864dd7c164ce796d6894f05431f86c66.png" width="100%"></kbd></p>
    <br>

    <a id="node-788"></a>
    <p align="center"><kbd><img src="assets/fe4e103226d98421479d599a93167638e90a4408.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/fe4e103226d98421479d599a93167638e90a4408.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/60966f80dd04dc88521becd32cf4c601071940ab.png" width="100%"></kbd></p>
    <br>

    <a id="node-789"></a>
    <p align="center"><kbd><img src="assets/309f2c696ae99834be6bd7ba8fdd42f1883bb017.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/309f2c696ae99834be6bd7ba8fdd42f1883bb017.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/65da6f9aef9bf3509e4cbdfc3daf12f40847f603.png" width="100%"></kbd></p>
    <br>


<a id="node-790"></a>
### 3 - Mini-Batch Gradient Descent

<br>

<a id="node-791"></a>
- 2 steps: Shuffle & Partition
  <br>

    <a id="node-792"></a>
    <p align="center"><kbd><img src="assets/10f95ebc7837854f7e1a62e0919efd6ce363267f.png" width="100%"></kbd></p>
    <br>

    <a id="node-793"></a>
    <p align="center"><kbd><img src="assets/11e6ca05e6d419798524e9d1103f310549d9441b.png" width="100%"></kbd></p>
    <br>

<a id="node-794"></a>
- Exercise 2 - random_mini_batches
> [!NOTE]
> Chia bộ data thành các mini batch,
> Số mini_batch = K  + 1 bộ lẻ 
> (nếu có thì size = m - K*mini_batch_size)
> K = np.roundoff(m/mini_batch_size).

  <br>

    <a id="node-795"></a>
    <p align="center"><kbd><img src="assets/abdb0347f6b5f528bfffb1274705e62c77e8fd76.png" width="100%"></kbd></p>
    <br>

    <a id="node-796"></a>
    <p align="center"><kbd><img src="assets/26e9cf80f31efc54c40541bb54736913cbfabe26.png" width="100%"></kbd></p>
    <br>

    <a id="node-797"></a>
    <p align="center"><kbd><img src="assets/ef74bd59e2a16b199fdfda98253a21d5b2b0966b.png" width="100%"></kbd></p>
    <br>

    <a id="node-798"></a>
    <p align="center"><kbd><img src="assets/8713ee7b3f8ee3f3075ae48364552beb050fe49e.png" width="100%"></kbd></p>
    <br>

    <a id="node-799"></a>
    <p align="center"><kbd><img src="assets/e0fd82b415573237ef30fb2430396f4283db4ee9.png" width="100%"></kbd></p>
    <br>

    <a id="node-800"></a>
    <p align="center"><kbd><img src="assets/7037b19a78a8cdc72f0bbdabd9e6765f07fe5eec.png" width="100%"></kbd></p>
    <br>

<a id="node-801"></a>
- Note
> [!NOTE]
> *NOTE

  <br>

    <a id="node-802"></a>
    <p align="center"><kbd><img src="assets/7037b19a78a8cdc72f0bbdabd9e6765f07fe5eec.png" width="100%"></kbd></p>
    > [!NOTE]
    > *NOTE

    <br>


<a id="node-803"></a>
### 4 - Momentum

<br>

<a id="node-804"></a>
- Exercise 3 - initialize_velocity
> [!NOTE]
> Chỉ ini vdW1, vdb1, ...vdWL, vdbL bởi 
> np.zeros(shape)
> Với shape tương ứng của W1, b1,..WL, bL
> Bỏ vào trong dictionary v luôn
> Ex. v[dw1=...], v[db1=...]

  <br>

    <a id="node-805"></a>
    <p align="center"><kbd><img src="assets/b9171bf5e320b96da095140b0064da7feb5a3dc1.png" width="100%"></kbd></p>
    <br>

    <a id="node-806"></a>
    <p align="center"><kbd><img src="assets/73d9aa7291d651e2fc1da1e95cb6ef0919925ffe.png" width="100%"></kbd></p>
    <br>

    <a id="node-807"></a>
    <p align="center"><kbd><img src="assets/5cfe628dd3d90f443fa08d4b74237eaaba67840a.png" width="100%"></kbd></p>
    <br>

<a id="node-808"></a>
- Exercise 4 - update_parameters_with_momentum
> [!NOTE]
> Update params with MOMENTUM
> Thay vì update W,b với dW, db thông thường thì
> Nay update W với vdW, vdb
> Với vdW, vdb Tính theo công thức **Exponentially 
> Weight Average**
>
> vdW = beta*vdW + (1-beta)*dW 
> vdb = beta*vdb + (1-beta)*db

  <br>

    <a id="node-809"></a>
    <p align="center"><kbd><img src="assets/52d6047b8deea502d9198de1f2faa6f5a4e5b79e.png" width="100%"></kbd></p>
    <br>

    <a id="node-810"></a>
    <p align="center"><kbd><img src="assets/c761d4444ada4e94b62dc7e464639a261a509628.png" width="100%"></kbd></p>
    <br>

<a id="node-811"></a>
- Note
> [!NOTE]
> *NOTE

  <br>

    <a id="node-812"></a>
    <p align="center"><kbd><img src="assets/f5a55a39c805c56f876c405d122077ccf740dad5.png" width="100%"></kbd></p>
    > [!NOTE]
    > *NOTE

    <br>


<a id="node-813"></a>
### 5 - Adam

<br>

<a id="node-814"></a>
- Exercise 5 - initialize_adam
> [!NOTE]
> Chỉ ini vdW1, vdb1, ...vdWL, vdbL 
> sdW1, sdb1, ...sdWL, sdbL
> bởi np.zeros(shape)
> Với shape tương ứng của W1, b1,..WL, bL
> Bỏ vào trong dictionary v luôn
> Ex. v[dw1=...], v[db1=...]

  <br>

    <a id="node-815"></a>
    <p align="center"><kbd><img src="assets/f8769e19f2949106183048548f77c6cee2aac2b6.png" width="100%"></kbd></p>
    <br>

    <a id="node-816"></a>
    <p align="center"><kbd><img src="assets/835303c56d1e551a623ba9506b9ca7c4ea7613d1.png" width="100%"></kbd></p>
    <br>

    <a id="node-817"></a>
    <p align="center"><kbd><img src="assets/f8c44c2d2d28a4fb5898067eb1892f0313f2b2d6.png" width="100%"></kbd></p>
    <br>

<a id="node-818"></a>
- Exercise 6 - update_parameters_with_adam
> [!NOTE]
> Update params with ADAM

  <br>

    <a id="node-819"></a>
    <p align="center"><kbd><img src="assets/4a4b46e5147423c81093c082eb06de09202abc65.png" width="100%"></kbd></p>
    <br>

    <a id="node-820"></a>
    <p align="center"><kbd><img src="assets/5263a4e8f2e3c97b7572cb15b5d6eb389026f0f4.png" width="100%"></kbd></p>
    <br>

    <a id="node-821"></a>
    <p align="center"><kbd><img src="assets/5e3a5539dec533a91a7b3a0256a77fb3c09dfa91.png" width="100%"></kbd></p>
    <br>


<a id="node-822"></a>
### 6 - Model with different Optimization algorithms

> [!NOTE]
> Lần lượt thử train model với 3 loaị để coi cái 
> nào tốt hơn: G.D, Momentum, Adam

<br>

<a id="node-823"></a>
- 'Moons' dataset
  <br>

    <a id="node-824"></a>
    <p align="center"><kbd><img src="assets/30b81dc95b8b79c66a5ead95fa64ee4def69a5a8.png" width="100%"></kbd></p>
    <br>

    <a id="node-825"></a>
    <p align="center"><kbd><img src="assets/29df00d7afe9fbd50c32eb04b174664092714b1b.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/29df00d7afe9fbd50c32eb04b174664092714b1b.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/37c546c469233dd151acee955203f3098ecc5549.png" width="100%"></kbd></p>
    <br>

<a id="node-826"></a>
- 6.1 - Mini-Batch Gradient Descent
  <br>

    <a id="node-827"></a>
    <p align="center"><kbd><img src="assets/998c866090e1b91d6eaa21be67cafdfbd0bbca1a.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/998c866090e1b91d6eaa21be67cafdfbd0bbca1a.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/cd8046cd7c7f294e2020ed00240b1cd36c68b49d.png" width="100%"></kbd></p>
    <br>

<a id="node-828"></a>
- 6.2 - Mini-Batch Gradient Descent with Momentum
  <br>

    <a id="node-829"></a>
    <p align="center"><kbd><img src="assets/b302364b245218619881b7f36bd00a6462f4f0aa.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/b302364b245218619881b7f36bd00a6462f4f0aa.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/11f366cee77a06794199e6ac2ac7d1a882c0e378.png" width="100%"></kbd></p>
    <br>

<a id="node-830"></a>
- 6.3 - Mini-Batch with Adam
  <br>

    <a id="node-831"></a>
    <p align="center"><kbd><img src="assets/87bf69c06c6a3762889125899b5ba831f469b167.png" width="100%"></kbd></p>
    <br>

    <a id="node-832"></a>
    <p align="center"><kbd><img src="assets/4a1a77766eb5ba26b71a418d81275a5905b9cd60.png" width="100%"></kbd></p>
    <br>

<a id="node-833"></a>
- 6.4 - Summary
> [!NOTE]
> *NOTE

  <br>

    <a id="node-834"></a>
    <p align="center"><kbd><img src="assets/3c8b849a58c7682fb6293b47c3e48e35da8386cb.png" width="100%"></kbd></p>
    > [!NOTE]
    > *NOTE

    <br>


<a id="node-835"></a>
### 7 - Learning Rate Decay and Scheduling

<br>

<a id="node-836"></a>
- Thêm 'Learning decay' element
  <br>

    <a id="node-837"></a>
    <p align="center"><kbd><img src="assets/87a9bd704c2ac8e601475c9b0b43ec64157f2744.png" width="100%"></kbd></p>
    <br>

    <a id="node-838"></a>
    <p align="center"><kbd><img src="assets/4d94269c21747ead80335a83fb1fdd923140dd7a.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/4d94269c21747ead80335a83fb1fdd923140dd7a.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/4bc06a6abbfe0ff01f0bf6de1ce2aacfbb566069.png" width="100%"></kbd></p>
    <br>

<a id="node-839"></a>
- 7.1 - Decay on every iteration
  <br>

  <a id="node-840"></a>
  - Exercise 7 - update_lr
    <br>

      <a id="node-841"></a>
      <p align="center"><kbd><img src="assets/95b2b5c7fe2e0ffc2e88e1facb8252a434a36093.png" width="100%"></kbd></p>
      <br>

      <a id="node-842"></a>
      <p align="center"><kbd><img src="assets/c30544d1bd7af54446dfa07c9305e6574c25c78a.png" width="100%"></kbd></p>
      <br>

      <a id="node-843"></a>
      <p align="center"><kbd><img src="assets/5b8cc8227164b61f5434cd4a55d628632bb9b38e.png" width="100%"></kbd></p>
      > [!NOTE]
      > *NOTE

      <br>

<a id="node-844"></a>
- 7.2 - Fixed Interval Scheduling
  <br>

  <a id="node-845"></a>
  - Exercise 8 - schedule_lr_decay
    <br>

      <a id="node-846"></a>
      <p align="center"><kbd><img src="assets/dd01b2dc98c80f49cbb0be6e50ef4415b1eb4993.png" width="100%"></kbd></p>
      <br>

      <a id="node-847"></a>
      <p align="center"><kbd><img src="assets/2df0c3e8211eebfcd6724e5fffeabac3306d1329.png" width="100%"></kbd></p>
      <br>

<a id="node-848"></a>
- 7.3 - Using Learning Rate Decay for each Optimization Method
  <br>

  <a id="node-849"></a>
  - 7.3.1 - Gradient Descent with Learning Rate Decay
    <br>

      <a id="node-850"></a>
      <p align="center"><kbd><img src="assets/f29860cde9c5c8654ac2670b635c335e5e3d3631.png" width="100%"></kbd></p>
      <br>

      <a id="node-851"></a>
      <p align="center"><kbd><img src="assets/be4ea083ba4095687b37d77992a929b4dde82e8b.png" width="100%"></kbd></p>
      <br>

  <a id="node-852"></a>
  - 7.3.2 - Gradient Descent with Momentum and Learning Rate Decay
    <br>

      <a id="node-853"></a>
      <p align="center"><kbd><img src="assets/7ba7b90cde07810a87ba0cdc8d65000a0c096db9.png" width="100%"></kbd></p>
      <br>

      <a id="node-854"></a>
      <p align="center"><kbd><img src="assets/150c1a2d29315df8cf5716a22cf651c2c09883ef.png" width="100%"></kbd></p>
      <br>

  <a id="node-855"></a>
  - 7.3.3 - Adam with Learning Rate Decay
    <br>

      <a id="node-856"></a>
      <p align="center"><kbd><img src="assets/57d2496d923f78ca29aba923e4a6c04208dfd2a0.png" width="100%"></kbd></p>
      <br>

      <a id="node-857"></a>
      <p align="center"><kbd><img src="assets/4ebd16b8d3235618970855c5b7b26bd798f5495a.png" width="100%"></kbd></p>
      <br>

<a id="node-858"></a>
- 7.4 - Achieving similar performance with different methods
> [!NOTE]
> *NOTE

  <br>

    <a id="node-859"></a>
    <p align="center"><kbd><img src="assets/ca327c1b0f55ea43fb38dbfdcd66942611b0a59f.png" width="100%"></kbd></p>
    > [!NOTE]
    > *NOTE

    <br>

