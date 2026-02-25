# C3W3_LSTMs AND NAMED ENTITY REGCONITION:  Learn about how long short-term memory units (\\*LSTMs\\*) solve the \\*vanishing gradient \\* problem, and how \\*Named Entity Recognition\\* systems quickly \\*extract important  information from text\\*. Then build your own Named Entity Recognition system using an  \\*LSTM and data from Kaggle!\\*  Learning Objectives   • \\*Vanishing gradients\\*  • \\*Named entity recognition\\*  • \\*LSTMs\\*  • \\*Feature extraction\\*  • \\*Part-of-speech tagging\\*  • \\*Data generators\\* 

📊 **Progress:** `63` Notes | `115` Screenshots

---

<a id="node-2344"></a>
## Welcom

<br>


<a id="node-2345"></a>
### This week explores named entity recognition or NAR for short, which is a sap task of

> [!NOTE]
> This week explores named entity recognition or NAR for short, which is a sap task of
> information extraction that locates and classifies named entities and text. The named
> entities could be organizations, persons, locations, times. For example, if you look at
> the sentence, the French people are visiting Morocco for Christmas, you will see that
> the word French is a geopolitical entity. Morocco is a geographic entity and Christmas
> is a time indicator. \**When you can recognize named entities and text then given an
> article, you can find the people, countries, organizations that are mentioned, and you
> can quickly pass and gather information about\**. \**You can use this information, for
> example, to do market research about certain topics by scraping the internet\**. When
> implementing NAR for this week, you will be using a \**long short-term memory unit\** or
> \**LSTM\**. LSTM's are \**similar to RNNs and GRUs\** except they have \**other gates that make
> them more powerful\**. Jonas will show you more about it. &gt;&gt; Yeah, let's get started.

<br>


<a id="node-2346"></a>
## Rnns And Vanishing Gradients

<br>


<a id="node-2347"></a>
### 1 Introduction to LSTM: The text introduces \\*long short-term memory (LSTM) cells\\* as a solution to

> [!NOTE]
> 1 Introduction to LSTM: The text introduces \**long short-term memory (LSTM) cells\** as a solution to
> the \**problems faced by conventional RNNs\**, namely the \**vanishing and exploding gradients\**.
>
> 2 Pros and cons of RNNs: \**RNNs\** are discussed in terms of their ability to \**model sequences\**,
> \**capture dependencies\**, and their \**relatively lightweight nature\**. However, they \**struggle with
> long-term dependencies\** and are \**prone to vanishing and exploding gradients\**.
>
> 3 Description of \**information propagation in RNN\**s: The \**process of propagating information\** from
> the beginning to the end of the sequence is explained, where computed values for each word are
> used to compute values for subsequent words.
>
> 4 \**Vanishing\** and \**exploding gradients\**: The consequences of vanishing gradients, where \**gradients
> exponentially decay\** as they \**propagate backward through time\**, and \**exploding gradients\**, where
> \**gradients grow uncontrollably,\** are described. These problems result in the\**loss of information from
> early steps\** or \**convergence issues\** during training.
>
> 5 \**Solutions for vanishing and exploding gradients\**: Some techniques to address these issues are
> briefly mentioned, including \**weight initialization\**, \**ReLU activation\**, \**gradient clipping\**, and \**skip
> connections.\**
>
> 6 \**Introduction to LSTM\** as a solution: The text concludes by mentioning that the next video will
> discuss LSTM as a \**solution to the problems of vanishing and exploding gradient\**s in RNNs.

<br>

  <a id="node-2348"></a>
  <p align="center"><kbd><img src="assets/537634864e0e36fff7008b32f63ed19c7f66eb82.png" width="100%"></kbd></p>
  > Ưu điểm là captures được **short range dependencies** -
  > nôm na là n**hớ được, nắm bắt được quan hệ ngữ nghĩa
  > của các từ trong chuỗi** nhưng không quá xa. Và cũng **nhẹ
  > RAM hơn các N-gram model**

  <br>

  <a id="node-2349"></a>
  <p align="center"><kbd><img src="assets/7ebeaece65e4d2031f5097bf6422c0ad09c31a3e.png" width="100%"></kbd></p>
  > Nhưng nhược điểm là **không nhớ tốt
  > được long term dependencies** và bị
  > **vanishing / exploding gradient**

  <br>

  <a id="node-2350"></a>
  <p align="center"><kbd><img src="assets/b3629cb2a5f6d15bde24102060fe5bdf6583efb1.png" width="100%"></kbd></p>
  > 1 **Vanishing** and **exploding** **gradients**: These are problems that can occur in**recurrent neural
  > networks (RNNs)** when **propagating information** from the **beginning** to the **end** of a sequence.
  >
  > 2 Information propagation in **RNNs**: RNNs start by **computing values for the first word** in the
  > sequence and then **propagate those values to compute new values for the second word**, using
  > the previously computed values. This process continues for subsequent words in the sequence.
  >
  > 3 Illustration of information propagation: The text describes a visual representation where the
  > **orange area represents the first computed values**, and the **green area represents the second
  > word**. The process of computing new values for each word using the previous values is
  > depicted.
  >
  > 4 **Accumulation of information**: As the RNN progresses through the sequence, it **incorporates
  > information from all the previous words**. This accumulation **allows the RNN to predict the next
  > word based on the information contained in the entire sequence.**
  >
  > 5 Influence of **early steps**: The**information from the first step** in the sequence has **less impact
  > on the final outputs of the RNN**. This is evident from the decreasing influence of the orange
  > portion (representing the first step) with each subsequent step in the computation.

  > Đại khái**thông tin từ những step đầu** **ảnh hưởng rất nhỏ tới output
  > của những step cuối** lí do là **hiện tượng gradient vanishing** mà theo
  > GPT là do **eigenvalue của weight matrix nhỏ hơn 1 sẽ khiến
  > gradient tính ra nhỏ đi nhanh chóng (exponential decay)**  (Từ
  > DLSpec ta hiểu Vanishing Gradient nhưng cụ thể cái gì gây ra hiện
  > tượng này?) dẫn đến là **những tính toán từ step đầu ảnh hưởng
  > nhỏ đến cost function**

  <br>

  <a id="node-2351"></a>
  <p align="center"><kbd><img src="assets/57051b0dcc050fa9471c7ccace7753d2c628c0f0.png" width="100%"></kbd></p>
  > The gradients are calculated using **backpropagation through time**, which sounds way
  > more **scary** than what it really is. As it would **simple backpropagation**. You just have to
  > apply the**chain rule multiple times**. Recall that the weights **W_h** and **W_x** are **the same
  > for each step**. Let's focus on the weights W_h. Noting that everything that I'll present to
  > you also applies to W_x, with the loss being computed at the T step sequence. The
  > **gradient with respect to W_h** would depend on the computations that are made this
  > every step. In fact, it is proportional to the s**um of products** of **hidden states, partial
  > derivatives**. This relationship can be found by **applying the chain rule** and the use of a
  > couple of tricks. But you **don't need to worry about the derivation** as much as the
  > implications behind this formula

  > Nói chung là đầu tiên cứ biết rằng **d Loss w.r.t W_h** sẽ
  > proportional với **sum của product của partial derivative của
  > hidden state w.r.t hidden state time step trước đó dh<t>/dh<t-1>**

  <br>

  <a id="node-2352"></a>
  <p align="center"><kbd><img src="assets/073465b9b2c9897ab39cde2e222307facb9a8560.png" width="100%"></kbd></p>
  > Và product của chuỗi các partial derivative của
  > hidden state time-step hiện tại w.r.t hidden
  > state của time-step trước đó.

  <br>

  <a id="node-2353"></a>
  <p align="center"><kbd><img src="assets/049b4276f6175ff7738e5f2bf16687bcf95146da.png" width="100%"></kbd></p>
  > Thì ý nói nếu P.d mà nhỏ hơn 1, nó sẽ nhân nhiều lần nhỏ hơn
  > 1 thì **dần dần thu nhỏ về 0** gây ra**Vanishing Gradient** còn
  > ngược lại nếu **P.d mà lớn hơn 1** thì nó được **khuếch đại
  > nhanh chóng** trở thành rất lớn gây ra **Exploding Gradient**

  <br>

  <a id="node-2354"></a>
  <p align="center"><kbd><img src="assets/93ec2af9997dcb62efac6f6b1da0f6559fc748ab.png" width="100%"></kbd></p>
  > You can deal with vanishing gradients by **initializing your weights to the identity matrix**,
  > which carries values of **one along the main diagonal** and **zero everywhere else**. Using a
  > **ReLU activation**. What this essentially does is **copy the previous hidden states** and
  > **information** from the current inputs and **replace any negative values with zero**. This has
  > the effect of **encouraging your network to stay close to the values of the identity
  > matrix**, which act like ones during matrix multiplication. This method is referred to
  > unsurprisingly as an **identity RNN**. The identity RNN approach **only works for vanishing
  > gradients** though, as a derivative of ReLU is equal to 1 for all values greater than zero.
  > To account for **values growing exponentially** you can perform**gradients clipping**. To clip
  > your gradient,**simply choose a relevant value** that you would **clip the gradient**to, say
  > 25. Using this technique, **any value greater than 25 will be clipped to 25**. This serves to
  > **limit the magnitude of the gradient**. Finally **skip connections**provide a **direct connection
  > to the earlier layers**. This effectively skips over the activation functions and adds the
  > value from your initial inputs x to you're outputs or f of x plus x. This way, activations
  > from early layers have more influence over the costs

  > **Một số giải pháp khắc phục** (trước khi có LSTM
  > là) **Identity RNN** để **giảm Vanishing gradient**,
  > **Gradient clipping** để **fix vấn đề exploding**
  > gradient và **Skip Connection.**

  <br>

  <a id="node-2355"></a>
  <p align="center"><kbd><img src="assets/54262ea1b65da02a273676caa27e7157e0f05a0b.png" width="100%"></kbd></p>
  <br>


<a id="node-2356"></a>
## Rnns And Vanishing

> [!NOTE]
> RNNS AND VANISHING
> GRADIENTS (READING)

<br>

<a id="node-2357"></a>

<p align="center"><kbd><img src="assets/5cc4a5ebcf983debd164e58bce44cd2ca47bd597.png" width="100%"></kbd></p>

<br>

<a id="node-2358"></a>

<p align="center"><kbd><img src="assets/fd40680aacad00f838cbaee517bdb90a19b9a6e2.png" width="100%"></kbd></p>

> [!NOTE]
> Note that the **sigmoid** and **tanh functions** are bounded by **0 and
> 1** and **-1 and 1** respectively. This eventually leads us to a problem.
> If you have **many numbers that are  less than |1|**, then as you **go
> through many layers**, and **you take the product of those  numbers**,
> you **eventually end up getting a gradient that is very close to 0**. This
> introduces  the problem of **vanishing gradients.**

<br>

<a id="node-2359"></a>

<p align="center"><kbd><img src="assets/021ae1ef8d733010aade6cccebc7e14f0fbe449d.png" width="100%"></kbd></p>

<br>


<a id="node-2360"></a>
## (optional) Reading Intro To

> [!NOTE]
> (OPTIONAL) READING INTRO TO
> OPTIMIZATION IN DEEP LEARNING:
> GRADIENT DESCENT

<br>


<a id="node-2361"></a>
### https://blog.paperspace.com/intro-to-optimization-in-deep-learning-gradient-descent/

> [!NOTE]
> Bài viết rất hay về Gradient
> Descent. Quay lại sau

<br>

  <a id="node-2362"></a>
  <p align="center"><kbd><img src="assets/69ea8fcccf0c5de1a3ca96a5c13dee3c6f7fbbb6.png" width="100%"></kbd></p>
  <br>

  <a id="node-2363"></a>
  <p align="center"><kbd><img src="assets/b20366397299066fca57af3f9168c07ba8d63228.png" width="100%"></kbd></p>
  <br>

  <a id="node-2364"></a>
  <p align="center"><kbd><img src="assets/4a44f5e18549cb7868c6d7dd7134fea472904059.png" width="100%"></kbd></p>
  <br>

  <a id="node-2365"></a>
  <p align="center"><kbd><img src="assets/4122ef04b4ab28f06bdaabd74cff592bee1110c8.png" width="100%"></kbd></p>
  <br>

  <a id="node-2366"></a>
  <p align="center"><kbd><img src="assets/148935ea4658c146b3b514153c655a482943819c.png" width="100%"></kbd></p>
  <br>

  <a id="node-2367"></a>
  <p align="center"><kbd><img src="assets/b72d43aaf1e138f9b8f4bb5ae4ac0a7ecdd546bf.png" width="100%"></kbd></p>
  <br>


<a id="node-2368"></a>
## Lab: Exploding & Vanishing Gradients

<br>

<a id="node-2369"></a>

<p align="center"><kbd><img src="assets/14566055909d951e04579d4eb24c2c0cc75b4460.png" width="100%"></kbd></p>

> [!NOTE]
> **Partial derivative (P.D) of loss function w.r.t weight matrix Wh** - **dL/dWh** sẽ **tỉ lệ
> thuận** (proportional) với **tổng các product** của các **P.D** of **hidden state sau w.r.
> t hidden state trước** - **dh_i/dh_i-1**. Và ở đây người ta sẽ cho mình thấy **với k
> lớn** (tức cái chuỗi dài) thì cái **"tổng các product..."** này sẽ **trở nên vô cùng bé
> hoặc vô cùng lớn** gây ra hiện tượng **vanishing gradient hoặc exploding
> gradient.**

<br>

<a id="node-2370"></a>

<p align="center"><kbd><img src="assets/e358c8874db34c1be112ee27d221d6f62995d3c4.png" width="100%"></kbd></p>

<br>

<a id="node-2371"></a>

<p align="center"><kbd><img src="assets/482d0506e71a5a19b3e93d7b92097fd10577729a.png" width="100%"></kbd></p>

> [!NOTE]
> Công thức của hidden state
> trong RNN, và partial derivative
> của h_i w.r.t h_i-1.

<br>

<a id="node-2372"></a>

<p align="center"><kbd><img src="assets/02243e343af6be2c0dab70ae068042672b27c556.png" width="100%"></kbd></p>

> [!NOTE]
> Điều kiện để gây ra V.G hoặc E.G:
>
> 1. Đạo hàm của activation function bị rằng buộc bởi một giá trị
> alpha nào đó
>
> 2. Giá trị tuyệt đối của cái eigenvalue lớn nhất của matrix Whh
> mà nhỏ hơn 1/alpha, thì gây vanishing gradient, lớn hơn
> 1/alpha thì gây exploding gradient

<br>

<a id="node-2373"></a>

<p align="center"><kbd><img src="assets/05a73a6fe96359c1ef9ca0954a19bbe5ae76f578.png" width="100%"></kbd></p>

> [!NOTE]
> Với x = -6, sigma(x) ~=0, và
> dsigma(x)/d(x) ~= 0.0025

<br>

<a id="node-2374"></a>

<p align="center"><kbd><img src="assets/2b3238fd0853f5afed671e33934bc18b73229728.png" width="100%"></kbd></p>

> [!NOTE]
> Với x = 2, sigma(x) = đâu đó 0.1, và
> dsigma(x)/d(x) ~= 0.1050

<br>

<a id="node-2375"></a>

<p align="center"><kbd><img src="assets/6af10f343af12d4e704da9a9ac20aeefea01d255.png" width="100%"></kbd></p>

> [!NOTE]
> Với x = 6, sigma(x) ~=1, và dsigma(x)/d(x) ~= 0.0025
>
> Ta thấy, khi x<-6 và x>6, sigma(x) ~= 0 và ~=1,  giá trị của
> dsigma(x)/d(x) không bao giờ vượt con số 0.0025.
>
> Chưa hiểu sao người ta lại nói sigmoid function is bounded by
> alpha = 1/4 nhưng chắc cũng liên quan.
>
> Vậy thì nếu thoả mãn điều kiện eigenvalue lớn nhất của Whh mà
> nhỏ hơn 1/alpha  = 4 thì sẽ gây V.G. Còn ngược lại sẽ gây E.G

> [!NOTE]
> As you checked, the derivative of the sigmoid function is bounded by  𝛼=14  . So
> vanishing gradient problems will arise for long-term components if the largest
> eigenvalue of  𝑊ℎℎ   is lower than 4, and exploding gradient problems will happen if
> the largest eigenvalue is larger than 4.

<br>

<a id="node-2376"></a>

<p align="center"><kbd><img src="assets/1d833aa2d3ce1262560827d9ff9999116a0e1e41.png" width="100%"></kbd></p>

> [!NOTE]
> Đoạn này ý là giả bộ có một RNN model, và sequence len = 20: có
> 20 time-step
>
> Giả bộ giá trị của x(i) - là tensor 20x5 - 20 time-step, mỗi input tại
> mỗi time-step x(i)<t> là một vector có len = 5
>
> Và hidden state cũng vậy, cũng là vector len 5 tại mỗi timestep h<t>
>
> Và dĩ nhiên Whx phải là 5x5 matrix, bh 5x1.

<br>

<a id="node-2377"></a>

<p align="center"><kbd><img src="assets/5040ace25a23d57ca3d746dd843af35be12ba703.png" width="100%"></kbd></p>

> [!NOTE]
> 1 Random Eigenvalues: The line "eig = np.random.rand(5)*4" **generates an array of 5
> random numbers between 0 and 1** using **np.random.rand(5)**. These numbers are then
> **multiplied by 4**, resulting in **random eigenvalues that are lower than 4**. The array eig
> represents the eigenvalues.
>
> 2 Random Eigenvectors: The line "Q = np.random.randn(5,5)" creates a 5x5 matrix Q with
> random values drawn from a standard normal distribution using np.random.randn(5,5).
> These values represent the random eigenvectors.
>
> 3 Computation of W_hh: The next line of code "W_hh = \_Q@np.diag\_(eig)@np.linalg.
> inv(Q)" computes the matrix product of three matrices: Q, a diagonal matrix formed from the
> eigenvalues eig using np.diag(eig), and the inverse of Q calculated using np.linalg.inv(Q).
> This multiplication results in the matrix W_hh.

<br>

<a id="node-2378"></a>

<p align="center"><kbd><img src="assets/b3ed1afedb90bc778598587565561a7ac94c7f3f.png" width="100%"></kbd></p>

> [!NOTE]
> Tạo một matrix Whh sao cho nó có wigenvalue < 4 (max eigenvalue < 4
> để mô phỏng điều kiện Vanishing Gradient).
>
> Đầu tiên là np.random.rand(5) sẽ tạo vector chứa 5 số trong khoảng 0,
> 1. Đem nhân 4 thì được một vector mà các giá trị không lơn hơn 4. 5
> con số này đóng vai trò là 5 eigenvalues và nhắc lại max của chúng
> không quá 4.
>
> Dòng thứ 2 tạo ra matrix 5x5 random từ normal distribution - đóng vai
> trò random eigenvectors.
>
> Dòng thứ 3, np.diag(eig) sẽ tạo ra diagonal matrix - tạo matrix 5x5 mà
> số 0 hết, chỉ có đường chéo tạo bởi các giá trị của eig. Cuối cùng nó
> tính Whh.

<br>

<a id="node-2379"></a>

<p align="center"><kbd><img src="assets/7efc27ff3cb90e46d27eb91b515a3d872ad84099.png" width="100%"></kbd></p>

> [!NOTE]
> Kế tới là define một function để tính
> product của công thức trên

<br>

<a id="node-2380"></a>

<p align="center"><kbd><img src="assets/8f16cfc809291b7d835c3fb7dd4110be6a25449a.png" width="100%"></kbd></p>

> [!NOTE]
> With the l**argest eigenvalue of the weight matrix**𝑊**ℎℎ   being lower than 4** --with a **sigmoid
> activation function**, the **contribution of the early items in the sequence to the gradient go to
> zero**. In practice, this will **make your RNN rely only upon the most recent items** in the series.

> [!NOTE]
> Thì đại khái đồ thị cho ta thấy **contribution của các time-step khác
> nhau từ 1 tới k đối với gradient cũng là contribution với loss function**
> cho thấy: **contribution của những time-step từ 16 trở về trước hầu
> như bằng 0**, hệ quả nôm na là :
>
> **khi model tính loss và dùng gradient để điều chỉnh weight** **để có
> thể predict đúng hơn ở một time step k** thì **hầu như gradient chỉ bị
> ảnh hưởng bởi những time-step gần đó**, **còn ở xa xa hầu như
> không có**.
>
> Cho nên, **ý nghĩa của nó đó là:** **từ được dự đoán ở timestep k**
> **chỉ phụ thuộc hay dựa trên một số từ gần gần đó thôi**, **không thể
> có long-range dependency** hay **ảnh hưởng bởi những từ ở đầu câu
> ở xa**

<br>

<a id="node-2381"></a>

<p align="center"><kbd><img src="assets/87d8653354b8e0697321861705de42b65fae770f.png" width="100%"></kbd></p>

> [!NOTE]
> Ý ổng nói với Exploding gradient thì điều kiện 2 (max value of
> eigenvalue >4) là điều kiện cần chứ không phải điều kiện đủ, nên hiện
> tượng V. G dễ xẩy ra hơn E.G. Tương tự, cũng giả bộ một RNN có
> trạng thái gây ra E.G

<br>

<a id="node-2382"></a>

<p align="center"><kbd><img src="assets/449305bf2e5a10ebe062dfbf3159530dd47c5e00.png" width="100%"></kbd></p>

> [!NOTE]
> With the **largest eigenvalue of the weight matrix**𝑊**ℎℎ being greater than 4**
> --with a sigmoid activation function, the **contribution of the early items in the
> sequence to the gradient goes to infinity**. In practice, this will **make you face
> convergence problems during training.**

> [!NOTE]
> Thì hình vẽ cho thấy , contribution của các time-step ở
> xa đối với gradient lớn vô cùng, gây ra các vấn đề
> converge. Đó chính là Exploding Gradient

<br>


<a id="node-2383"></a>
### Now you are more familiar with the \\*conditions for vanishing and exploding

> [!NOTE]
> Now you are more familiar with the \**conditions for vanishing and exploding
> gradient problems\**. You should take away that for \**vanishing gradient it is
> sufficient to satisfy\** an \**eigenvalue condition\**, while for the \**exploding gradient
> problem it is neccesary but not enough\**. I used the weight matrix  𝑊ℎℎ   in this
> discussion, but everything exposed here\**also applies\** for  𝑊ℎ𝑥  .
>
> Solution One solution is to use RNN architectures \**specially designed\** to avoid
> these problems (like GRUs and LSTMs). Other solutions involve
> \**skip-connections or gradient clipping\**. But those are both discussions for another
> time.

<br>


<a id="node-2384"></a>
## Introduction To Lstms

<br>


<a id="node-2385"></a>
### 1 \\*LSTMs\\* are the \\*best-known solution\\* to the \\*vanishing gradients problem\\* in \\*recurrent neural

> [!NOTE]
> 1 \**LSTMs\** are the \**best-known solution\** to the \**vanishing gradients problem\** in \**recurrent neural
> networks (RNNs)\**.
>
> 2 LSTMs are a \**special variety of RNNs \**designed to \**handle entire sequences of  data\** by \**learning
> when to remember and forget information.
> \**
> 3 LSTMs consist of a \**cell\** \**state\** (\**memory\**) and a \**hidden state\** where  computations are performed
> during training to decide on changes to make.
>
> 4 LSTMs have\**multiple gates\** (\**forget\** gate, \**input\** gate, \**output\** gate) that \**allow  information to flow
> through the network\**, \**avoiding vanishing or exploding gradients\**.
>
> 5 The \**concept of LSTMs\** can be related to how \**humans handle conversations  and retain relevant
> information while discarding irrelevant details\**.
>
> 6 Applications of LSTMs include \**language models, chatbots, music composition,  automatic image
> captioning, and speech recognition.\**
>
> 7 LSTMs have \**revolutionized natural language processing (NLP) \**and are \**widely  used\** for various
> tasks in this domain.
>
> 8 The LSTM architecture involves computations through three gates:\**forget gate,  input gate, and
> output gate.
> \**
> 9 LSTMs have become popular due to their ability to\**overcome the limitations of  traditional RNNs.\**
>
> Overall, LSTMs are powerful tools that have significantly advanced the field of natural language
> processing and other related tasks by efficiently processing sequential data while avoiding
> gradient-related issues.

<br>

  <a id="node-2386"></a>
  <p align="center"><kbd><img src="assets/7b1d989a5a4ddaafe888559c5096ad8f777c7b2b.png" width="100%"></kbd></p>
  <br>

  <a id="node-2387"></a>
  <p align="center"><kbd><img src="assets/079291d292b1f9b86b0faa7e3a1689c79d4f8a78.png" width="100%"></kbd></p>
  > So sánh với việc con người handle một conversation:
  >
  > Bỏ thông tin không còn quan trọng (irrelevant) - Forget gate.
  >
  > Thêm thông tin mới quan trọng (Input gate).
  >
  > Product output (output gate)

  <br>

  <a id="node-2388"></a>
  <p align="center"><kbd><img src="assets/9091cf83d632f6e0e1bcfb0564ed3a0b06df9951.png" width="100%"></kbd></p>
  > Thông tin đi từ time-step trước sẽ bị chặn bởi Forget gate (số 1), gate
  > này (cũng như các gate khác) sẽ được model dựa trên thông tin từ
  > current input và hidden state trước để quyết định nên giữ hay bỏ, giữ
  > nhiều hay ít thông tin từ time-step trước c<t0> trong cell state này
  > c<t>.
  >
  > Input và hidden state trước sẽ được kết hợp để tính c~<t> và cho
  > qua Input gate để quyết định sẽ sử dụng hay không, nhiều hay ít
  > trong cell state.
  >
  > Như vậy thông qua Forget gate, input gate, thông tin cell state sẽ có
  > chứa thông tin nào được giữ lại từ previous time-step , và thông tin
  > mới ở time-step <t> nào được cho vào.
  >
  > Cuối cùng, output gate sẽ quyết định thông tin nào của cell state sẽ
  > được dùng để output và save vào hidden state để pass qua next time-step

  <br>

  <a id="node-2389"></a>
  <p align="center"><kbd><img src="assets/9b2e9a792b144f58a98bee89a58ec6304cf4d318.png" width="100%"></kbd></p>
  <br>

  <a id="node-2390"></a>
  <p align="center"><kbd><img src="assets/1776c8640de0e0c08d83e492740c77534c3f4a0a.png" width="100%"></kbd></p>
  <br>


<a id="node-2391"></a>
## Lstm Architecture

<br>


<a id="node-2392"></a>
### 1 The architecture of an LSTM involves a cell state, a hidden state, input (x), and output (y).

> [!NOTE]
> 1 The architecture of an LSTM involves a cell state, a hidden state, input (x), and output (y).
>
> 2 The \**cell state\** functions as the \**memory of the network\** and gets modified using information from
> the input and previous hidden state.
>
> 3 LSTMs use three gates to control the flow of information: \**forget gate, input gate, and output gate.\**
>
> 4 \**Sigmoid\** activation functions are applied to the input and previous states for the gates, ensuring
> values are \**between 0 and 1.\**
>
> 5 The \**forget gate \**decides \**what information to keep or discard\** from the \**previous cell state.\**
>
> 6 The \**input gate\** selects \**relevant information\** from the \**input and previous hidden state.\**
>
> 7 The \**candidate cell state\** is computed by transforming information from the \**previous hidden states\**
> and \**current inputs\** using a \**hyperbolic tangent activation function\**.
>
> 8 The \**new cell state\** is \**updated\** by \**adding the candidate cell state information\** that \**passes
> through the input gates\** to the cell state information that passes through the forget gate.
>
> 9 The \**new hidden state\** is \**computed\** by p\**assing transformed information\** from the \**new cell state
> through the output gate.\**
>
> 10 Some LSTM architectures \**directly pass the new cell state\** through the output gate \**without applying
> the hyperbolic tangent activation.\**
>
> 11 LSTMs are powerful tools for handling sequential data, and the understanding of their architecture and
> computations is essential for implementing them.
>
> The text provides a detailed explanation of the LSTM architecture, describing the functions of different
> components (cell state, gates, candidate cell state, hidden state) and their interactions. It emphasizes the
> importance of LSTMs in handling sequential data and their practical applications in solving NLP tasks.

<br>

  <a id="node-2393"></a>
  <p align="center"><kbd><img src="assets/feaf142dfa42092117a8266d08f8dd57252798e1.png" width="100%"></kbd></p>
  <br>

  <a id="node-2394"></a>
  <p align="center"><kbd><img src="assets/20a5d20ef7ef92aa3269b1c378913804496900d4.png" width="100%"></kbd></p>
  > **Input** và **hidden state trước** sẽ được kết hợp để tính **c~<t>** và
  > cho qua **Input gate** để quyết định sẽ **sử dụng hay không, nhiều
  > hay ít** trong **cell state.**Và tanh giúp ổn định, kiểm soát giá trị
  > không cho quá cao hay quá thấp, khắc phục tình trạng vanishing &
  > exploding gradient.

  <br>

  <a id="node-2395"></a>
  <p align="center"><kbd><img src="assets/b791408db024d80cc345781ce2a060493c6da2e1.png" width="100%"></kbd></p>
  > Như vậy thông qua **Forget gate**, **Input gate**, thông tin **cell state sẽ
  > có chứa thông tin nào được giữ lại từ previous time-step**, và**thông
  > tin mới ở time-step <t> nào được cho vào**

  <br>

  <a id="node-2396"></a>
  <p align="center"><kbd><img src="assets/302e539431ad7439a5dc4f9afd1633b99e7b0bd2.png" width="100%"></kbd></p>
  > Cuối cùng, **output gate** sẽ quyết định thông tin nào của
  > cell state sẽ được dùng để **output** và save vào **hidden
  > state** để **pass qua next time-step**

  <br>

  <a id="node-2397"></a>
  <p align="center"><kbd><img src="assets/f6765508d78958c18a40425ec38f92fc5bee5039.png" width="100%"></kbd></p>
  <br>


<a id="node-2398"></a>
## Introduction To Named

> [!NOTE]
> INTRODUCTION TO NAMED
> ENTITY RECOGNITION

<br>


<a id="node-2399"></a>
### 1 Named Entity Recognition (NER) is an \\*essential problem in natural language processing (NLP)\\*, and many

> [!NOTE]
> 1 Named Entity Recognition (NER) is an \**essential problem in natural language processing (NLP)\**, and many
> NLP systems use \**NER components\**.
>
> 2 NER systems \**locate and extract named entities from text,\** which can be anything from \**places\**,
> \**organizations\**, and \**people's names\** to times and dates.
>
> 3\**NER systems\** use \**labels\** to \**classify entities\**. Some common classes include \**geographical entities,\**
> \**organizations, geopolitical entities, time indicators, artifacts, and person names.\**
>
> 4 \**NER\** is useful for \**content classification\** and o\**ptimizing search engine efficiency\** by \**quickly scanning large
> amounts of text\** for specific words or entities.
>
> 5 Real-world applications of NER systems include \**optimizing search engine efficiency\**, making
> \**recommendations\** based on user history, \**matching customers\** to appropriate service agents, and even
> \**automatic trading\** using sentiment analysis on news articles.
>
> 6 NER systems have \**numerous applications in the field of deep learning\**, and \**their ability to extract and
> identify entities\** plays a \**vital role in various NLP tasks.\**
>
> The text provides an overview of what NER is, its \**significance\** in NLP, and its \**practical applications\** in
> various domains. It highlights the \**versatility of NER systems \**in \**extracting relevant information from text\** and
> how they can be \**employed to improve efficiency in different tasks\**, from search engines to customer service
> and trading applications.

<br>

  <a id="node-2400"></a>
  <p align="center"><kbd><img src="assets/ce46d26d5345d6c3d56fabf79c6c6f5024ba43e6.png" width="100%"></kbd></p>
  <br>

  <a id="node-2401"></a>
  <p align="center"><kbd><img src="assets/1bb98e0e5ce70c090153c48234c6247f31f86c6d.png" width="100%"></kbd></p>
  <br>

  <a id="node-2402"></a>
  <p align="center"><kbd><img src="assets/f7a5073e66117a9482b516fefbeb8fca7d3debe3.png" width="100%"></kbd></p>
  <br>

  <a id="node-2403"></a>
  <p align="center"><kbd><img src="assets/b358bce7dad7e98878911d17e5ec5f5b87231d96.png" width="100%"></kbd></p>
  <br>

  <a id="node-2404"></a>
  <p align="center"><kbd><img src="assets/05645b567e2c2f230d571d1cffb1c6f0c2859a53.png" width="100%"></kbd></p>
  <br>


<a id="node-2405"></a>
## Lstm Equations

<br>

<a id="node-2406"></a>

<p align="center"><kbd><img src="assets/ca64efdc5c0a7b66cd10751a4bfd158ad2771921.png" width="100%"></kbd></p>

<br>


<a id="node-2407"></a>
## Training Ners: Data Preprocessing

<br>


<a id="node-2408"></a>
### 1 To train a \\*Named Entity Recognition (NER) system\\*, the first step involves \\*converting entity classes\\* and

> [!NOTE]
> 1 To train a \**Named Entity Recognition (NER) system\**, the first step involves \**converting entity classes\** and
> \**labeled data\** into \**arrays of numbers\** that correspond to each other.
>
> 2 \**Each entity class \**is assigned a\**unique number\**, and \**each word in the sentence\** is \**assigned a number
> corresponding to its entity class\**.
>
> 3 The s\**equences of numbers\** are transformed\**\**into\**numerical arrays\**, and to handle \**different sequence
> lengths,\** a \**padding token is added to fill empty spaces.\**
>
> 4 Data is processed in \**batches\** using a \**data generator\** to \**speed up processing time.\**
>
> 5 The \**NER\** \**system\** architecture includes\**feeding the input data through an LSTM layer,\** followed by a \**fully
> connected (dense) layer\** and using \**log softmax for prediction\**.
>
> 6 \**Log softmax\** is preferred over softmax for \**better numerical performance\** during optimization.
>
> 7 The layers in the NER system include the\**LSTM layer, a dense layer, and a log softmax activation\**
> function.
>
> 8 After implementing these steps, the NER system is \**ready for training and evaluation.\**
>
> The text outlines the \**steps involved in training a NER system\**, including \**data preprocessing\**, \**batch
> processing\**, and\**building the NER model architecture\**. It also emphasizes the progress made throughout
> the course in understanding and implementing these concepts. The next step is to evaluate the trained
> NER system, completing the process of \**building a fully functional NER model from scratch\**.

<br>

  <a id="node-2409"></a>
  <p align="center"><kbd><img src="assets/fd2ece235602da93f27b3f9a348277fe28ed0806.png" width="100%"></kbd></p>
  > Assign mỗi class 1 number ví
  > dụ "Tên riêng" = 45

  <br>

  <a id="node-2410"></a>
  <p align="center"><kbd><img src="assets/df0cf369ebf564c927f5cc7807cfb7ffb4e2fd36.png" width="100%"></kbd></p>
  > Chỗ này chưa hiểu lắm là assign mỗi từ một number là
  > number gì, là index trong vocab hay class number?

  <br>

  <a id="node-2411"></a>
  <p align="center"><kbd><img src="assets/98b352de74c28d9587a19017b374467275448cfc.png" width="100%"></kbd></p>
  > Không có gì mới, các câu phải được padding để bằng size
  > nhau hết thường size câu dài nhất. Cái này cũng tương tự
  > các image trong 1 batch phải cùng size vậy

  <br>

  <a id="node-2412"></a>
  <p align="center"><kbd><img src="assets/c02d0dd281c6d68905dbb9ec151388b342b6b0ad.png" width="100%"></kbd></p>
  > Quá trình training

  <br>

  <a id="node-2413"></a>
  <p align="center"><kbd><img src="assets/264bdc2af28248fafec7fcf9b11833eadf0dda6a.png" width="100%"></kbd></p>
  > Output dùng log-softmax . Tức là lấy
  > log trên kết quả của softmax.

  <br>

<a id="node-2414"></a>
- We use Log Softmax instead of Softmax in training the Named Entity Recognition (NER) neural network model mainly for \\*numerical stability\\* and \\*computational efficiency\\* during optimization.  The \\*Softmax\\* function is used to convert the \\*raw scores (logits)\\* produced by the last layer of the neural network \\*into probabilities\\*. However, \\*exponentiating large logits\\* in Softmax can \\*lead to numerical instability\\*, as exponential values can grow very quickly, potentially \\*causing overflow\\* or \\*loss of precision in floating-point representations\\*.  On the other hand, \\*Log Softmax\\* is a \\*more numerically stable\\* alternative. \\*Instead of exponentiating the logits\\*, Log Softmax computes the \\*logarithm of the Softmax probabilities\\*. This \\*avoids the issues of exponential growth\\* and helps \\*maintain numerical stability\\* during training.  Using Log Softmax also provides \\*computational advantages\\* during \\*optimization\\*, especially in deep neural networks like NER models. When computing gradients during backpropagation, \\*taking the logarithm of the Softmax probabilities allows for simpler and more efficient computations\\*. It \\*simplifies the calculations\\* when performing the chain rule to compute gradients, \\*reducing computational complexity\\* and \\*speeding up the training process.\\*  In summary, using Log Softmax in training NER neural network models ensures numerical stability and enhances computational efficiency during optimization, making the training process more reliable and faster.
  > Đại khái là quá trình tính **Softmax** khiến **giá trị có thể rất
  > lớn do tính e^**, dẫn đến tiềm ẩn **nguy cơ bị numerical
  > instability như overflow** hoặc**loss precision** trong floating
  > point representation. Một cái nữa là khi **backprob, tính
  > derivative của log softmax đơn giản hơn** cho việc tính
  > toán dẫn đến**training nhanh hơn**

  <br>

    <a id="node-2415"></a>
    <p align="center"><kbd><img src="assets/4416ae271543e04222fa93aab21d9d8af41d1668.png" width="100%"></kbd></p>
    > Define LSTM neural network nhờ
    > Trax trở nên rất đơn giản

    <br>

    <a id="node-2416"></a>
    <p align="center"><kbd><img src="assets/c092baa328c5a0597539fb2d9fca802326b23fae.png" width="100%"></kbd></p>
    <br>

    <a id="node-2417"></a>
    <p align="center"><kbd><img src="assets/21af1575d35dde5e9ba2e48aaca80a324988b7a5.png" width="100%"></kbd></p>
    <br>


<a id="node-2418"></a>
## Reading: Lstm (dlspec C5)

<br>


<a id="node-2419"></a>
## Compute Accuracy

<br>

<a id="node-2420"></a>

<p align="center"><kbd><img src="assets/dd85873dfea2a348df2a2a98a5a7600d8b4fd12b.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là evaluate model bằng cách **tính accuracy của model trên test
> set**. thì đây là bài toàn **NER - Named Entity Recognition** nên cơ bản
> nó là **multi-class classification** - **predict label của một từ trong số
> nhiều label có thể có**.
>
> Thì khi model nó **predict một từ (tại một time-step)** thì nó có dạng
> **vector các probability** có độ dài là **số label (Entity class)**, thì **thằng
> nào có P lớn nhất sẽ được chọn**, và**index** của nó chính là "kết luận"
> sẽ  đem so với **g.t.label (label của mỗi từ cũng chính là index của một
> Entity class nào đó)**
>
> Thì việc ta **xác định thằng có P lớn nhất đó rồi lấy index của nó** chính
> là "**arg max across prediction array".**Ý thứ 3 đại khái là đối với token đóng vai trò là padding thì tất nhiên ta
> không tính đúng sai gì đối với nó, cho đó mới nói là **Mask padded
> token** ý nói **khi tính accuracy thì che padded token lại, không tính nó.**
> Cuối cùng với các **" kết luận" về entity class của các từ trong sequence
> mà model predict, ta đem so với labe**l. Xem phần trăm đúng là bao
> nhiêu.

<br>

<a id="node-2421"></a>

<p align="center"><kbd><img src="assets/1bd01083943b5d169b6a5962ef2c86ee4afd474b.png" width="100%"></kbd></p>

> [!NOTE]
> 1. Như đã phân tích, ta **cần lấy index của vị trí có giá trị cao nhất trong  probability
> vector.**
>
> Nhưng không chỉ có 1 vector mà là một list Tx từ nên có Tx vector vector. Và lại có
> batch câu.
>
> Nên **prediction output tensor y^**sẽ có shape là  batch x Tx (chiều dài sequence) x
> n_classes.
>
> Do đó **trục thứ nhất axis = 0** là **batch size** lấy trong trục này là **lấy một câu nào
> đó trong batch.**
>
> **Trục thứ hai axis = 1** là **số từ Tx** hay đúng hơn là token trong sequence. Loop
> trong đây là **loop trong các từ | time-step trong câu.**
>
> **Trục thứ ba, axis = 2** mới là **probability vector**. Vậy để lấy index mà có giá trị p
> max trong từng vector thì phải để axis = 2
>
> 2. Cái mask sẽ làm như thế nào cụ thể trong Assignment sẽ note
>
> 3.Cái cuối chính là **so sánh output** với **ground-truth label**, mà y sẽ có shape là:
> **Batch x Tx**: Có batch câu, mỗi câu có Tx từ (có thể sẽ lấy Tx là câu dài  nhất trong
> batch) Mỗi từ gắn với index của Entity class
>
> -> shape y: **batch_size x Tx**
>
> Kết quả của output sau khi lấy argmax của y^ cũng là **batch_size x Tx.** **So sánh
> hai thằng đó sẽ ra một tensor mà chỗ nào chúng nó bằng  nhau thì là True, ngược lại
> thì False**. Do đó **sum hết lại chính là những từ được predict Named Entity đúng.**
>
> Sau đó chia cho sum(mask). **Khả năng cao mask ta sẽ tạo một tensor số 1 hết, trừ
> chỗ nào là padded token sẽ là 0**. Nên sum **mask tính là tất cả các từ trong tensor.**

<br>

<a id="node-2422"></a>

<p align="center"><kbd><img src="assets/d87c7c04d993ce8533f24ddaaca467c753f537b6.png" width="100%"></kbd></p>

<br>


<a id="node-2423"></a>
## Week Conclusion

<br>


<a id="node-2424"></a>
## Quiz

<br>

<a id="node-2425"></a>

<p align="center"><kbd><img src="assets/af89f9c389ac5c7851a24f8403b7a701232cbc4d.png" width="100%"></kbd></p>

<br>

<a id="node-2426"></a>

<p align="center"><kbd><img src="assets/1aaf343a1239fb0193c1bbe5458adbcdf0add1c1.png" width="100%"></kbd></p>

> [!NOTE]
> Hoá ra image captioning
> cũng dùng LSTM

<br>

<a id="node-2427"></a>

<p align="center"><kbd><img src="assets/88cd79df6d6afe17bee0c760fd9663153aea42e7.png" width="100%"></kbd></p>

<br>

<a id="node-2428"></a>

<p align="center"><kbd><img src="assets/f68492aa627bfee98ac2a3dc97cc9fcb1be2a941.png" width="100%"></kbd></p>

<br>

<a id="node-2429"></a>

<p align="center"><kbd><img src="assets/db10015cf77fbffae85c102cb100ea82806e0576.png" width="100%"></kbd></p>

<br>

<a id="node-2430"></a>

<p align="center"><kbd><img src="assets/5d13c0e199ad559b2fcd39e6b72356f95a939e9d.png" width="100%"></kbd></p>

<br>

<a id="node-2431"></a>

<p align="center"><kbd><img src="assets/edc547eb70ccfed9daa229e6b101c4c229bcd746.png" width="100%"></kbd></p>

<br>

<a id="node-2432"></a>

<p align="center"><kbd><img src="assets/b080cc05a9232312fdf13d68b38e267c68690cfe.png" width="100%"></kbd></p>

<br>

<a id="node-2433"></a>

<p align="center"><kbd><img src="assets/82dd4a5b042860bead023cc2db134bedb81f04d9.png" width="100%"></kbd></p>

<br>


<a id="node-2434"></a>
## P.A: Named  Entity Recognition

<br>


<a id="node-2435"></a>
### Welcome to the third programming assignment of Course 3. In this assignment,

> [!NOTE]
> Welcome to the third programming assignment of Course 3. In this assignment, 
> you will  learn to \**build more complicated models\** with \**Trax\**. By completing this
>  assignment, you will be able to:
>  • \**Design the architecture of a neural network\**, \**train it, and test it.
> \** • \**Process features\** and \**represents\** them
>  • Understand \**word padding\**
>  • Implement \**LSTMs\**
>  • \**Test\** with your own sentence

<br>

<a id="node-2436"></a>
- Introduction
  <br>

    <a id="node-2437"></a>
    <p align="center"><kbd><img src="assets/140efef332273e4c4b529e574acb53ef38f05e13.png" width="100%"></kbd></p>
    > NER là một subtask của **Information extraction**. Ở đây ta sẽ build một cái model
    > làm nhiệm vụ này và train nó để đạt **75% accuracy** trong vài giây. Rồi lại **load một
    > cái y vậy những được đã được train lâu hơn** và evaluate nó sẽ thấy nó đạt tới **96%
    > accuracy**.

    <br>

    <a id="node-2438"></a>
    <p align="center"><kbd><img src="assets/a7f7605a20000c9f45a99f2d6a06d4898db630a8.png" width="100%"></kbd></p>
    <br>

<a id="node-2439"></a>
- 1 - Exploring the Data
  <br>

  <a id="node-2440"></a>
  - We will be using a dataset from \\*Kaggle\\*, which we will \\*preprocess\\* for you.  The \\*original data\\* consists of \\*four columns\\*: the \\*sentence number\\*, the \\*word\\*,  the \\*part of speech of the word\\*, and the \\*tags\\*. A few tags you might expect to see are:  \\*geo\\*: \\*geographical\\* entity \\*org\\*: \\*organization\\* \\*per\\*: \\*person\\* \\*gpe\\*: \\*geopolitical\\* entity \\*tim\\*: \\*time\\* indicator \\*art\\*: \\*artifact\\* \\*eve\\*: \\*event\\* \\*nat\\*: \\*natural phenomenon\\* O: \\*filler word\\*
    <br>

      <a id="node-2441"></a>
      <p align="center"><kbd><img src="assets/1ffeed554ecb49a55fe124edd9ca4aa283a829d2.png" width="100%"></kbd></p>
      > Dataset này sẽ lấy từ **Kaggle**, được **preprocess giùm** để có dạng như sau:
      > **Mỗi data sample** **x sẽ là một sentence**. **Label sẽ là một chuỗi**, **tương
      > ứng mỗi vị trí của từ trong câu là một tag** ví dụ như **B-geo (geographical
      > entity), B_gpe (geopolitical entity), O (filler word)**.
      >
      > Original (Chưa preprocess data) thì có dạng 4 columns như bên dưới tất nhiên ta
      > sẽ làm việc với bộ data đã preprocessed sẵn

      <br>

<a id="node-2442"></a>
- 1.1 - Importing the Data
  <br>

    <a id="node-2443"></a>
    <p align="center"><kbd><img src="assets/591e56959682b4075fc06ae7436d10b13278548f.png" width="100%"></kbd></p>
    > Sử dụng utils function get_vocab(với path dẫn
    > đến hai file words.txt và tags.txt) nó sẽ giúp
    > chuẩn bị hai bộ dictionary. Một cái map từ - index, và một cái
    > map tag - index.

    <br>

    <a id="node-2444"></a>
    <p align="center"><kbd><img src="assets/dc8a1d7fb9e2187df3490df2eb6371cfffe75e40.png" width="100%"></kbd></p>
    > Open file define bởi input path (vocab_path), đọc file và split ra bởi "
    > xuống dòng" để có list các từ và loop trong đó map từ với index. Cuối
    > cùng thêm một từ đặc sắc gọi là '<PAD>'. Làm tương tự với tags. Nói
    > chung nó sẽ trả ra hai cái dictionary. Một cái map từ - index, và một cái
    > map tag - index.

    <br>

    <a id="node-2445"></a>
    <p align="center"><kbd><img src="assets/4fc9970856348d79112553f7b1822adabc0522a9.png" width="100%"></kbd></p>
    > File words.txt trong
    > folder data/large:

    <br>

    <a id="node-2446"></a>
    <p align="center"><kbd><img src="assets/235e6b504cd7b41dbf59b0db136498ba945ff00a.png" width="100%"></kbd></p>
    > File tags.txt trong
    > folder data/large:

    <br>

    <a id="node-2447"></a>
    <p align="center"><kbd><img src="assets/353d2b6184e8be60997e449b7c944030a0288609.png" width="100%"></kbd></p>
    > Thì ý nói với hai cái dictionary này. Ta sẽ "transform" training
    > sample từ câu text thành list (hoặc batch of list) các index number
    > (của từ đó trong vocab). Đồng thời bù vào cuối một số lượng các
    > các index của Padded token để cho đủ một số lượng nào đó mà ta
    > chọn (Tx) mục đích để tất cả các sequence trong batch đều dài
    > bằng nhau.

    <br>

    <a id="node-2448"></a>
    <p align="center"><kbd><img src="assets/4c9914778c7ab2c6a65f14cf071dac873a7dc6d8.png" width="100%"></kbd></p>
    > tag_map dictionary map tag với index. Chỉ có cái đặc biệt là I- hay B-.
    > Thì đại khái là nếu có cái tên Anh Tran is learning.. thì Anh là B-name (ví
    > dụ vậy, là Entity class "Name", nhưng Trần sẽ là I-name thể hiện nó
    > cũng là "Name" nhưng không đứng trước như "Anh" mà đứng "trong"
    > - trong ở đây hiểu là trong một "Name" lớn hơn là "Anh Tran".

    <br>

    <a id="node-2449"></a>
    <p align="center"><kbd><img src="assets/4304e5e6b6ffb9f14486c892889579b929d6725c.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/4304e5e6b6ffb9f14486c892889579b929d6725c.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/d481884d97ac55e3ad866a7b2c036eb83e466adf.png" width="100%"></kbd></p>
    > Thì đại khái cái câu lệnh dưới sử dụng utils function get_params đã giúp ta load hai cái
    > file sentences.txt chứa các câu, và labels.txt chứa các tags mà các labeler đã miệt mài
    > gán nhãn cho các từ của các câu trong file sentences.txt.
    >
    > Từ đó ta có dataset dành cho training, validating và testing (mỗi cái load file sentence.
    > txt và labels.txt từ folder tương ứng (data/large/train/, data/large/val, data/large/text)

    <br>

    <a id="node-2450"></a>
    <p align="center"><kbd><img src="assets/7427f92a43c90a05fc9c87292f91efc6fc5b8998.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/6281b9fcefb476749b952499e23c82bbcf7e16cb.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/7427f92a43c90a05fc9c87292f91efc6fc5b8998.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/6281b9fcefb476749b952499e23c82bbcf7e16cb.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/561d3301703eb9f6a6604eba6bcb8acba89b306f.png" width="100%"></kbd></p>
    <br>

<a id="node-2451"></a>
- 1.2 - Data Generator
  <br>

    <a id="node-2452"></a>
    <p align="center"><kbd><img src="assets/237b66d9a02f32bb9cd6f525d96d6d5b2f441c5d.png" width="100%"></kbd></p>
    > Viết function làm nhiệm vụ data generator, nhận input là batch_size,
    > bộ data "full" x, y, pad - là padded token hoặc index của nó, shuffle
    > là boolean ý muốn có shuffle không. Làm sao đó để trả về từng
    > batch data dạng tuple (X,Y) sao cho chứa số sample bằng
    > batch_size. Phải được 'pad' cho đủ max_length là chiều dài của
    > câu dài nhất trong batch đó - không phải trong toàn bộ data. Rồi
    > phải có cơ chế shuffle để dùng nếu cần.

    <br>

  <a id="node-2453"></a>
  - Details:  Use this code as an outer loop  \\*while True:   ...   yield((X,Y))\\*    so your data generator runs continuously. Within that loop, \\*define 2\\* \\/\\*for loops\\*\\/:  The first stores \\*temporal lists\\* of the \\*data samples\\* \\*to be included\\* in the batch, and \\*finds  the maximum length\\* of the sentences contained in it.  The second one \\*moves the elements\\* from the \\*temporal list\\* into \\*NumPy arrays pre-filled  with pad values\\*.  There are three features useful for defining this generator:  The NumPy \\*full()\\* function to \\*fill the NumPy arrays\\* with a \\*pad value\\*. See full function  documentation.  \\*Tracking the current location\\* in the incoming lists of sentences. \\*Generators\\* \\*variables hold  their values between invocations\\*, so we\\* create an index variable\\*, \\*initialize to zero\\*, and  \\*increment by one for each sample included\\* in a batch. However, we \\*do not use the index\\*  to access the positions of the list of sentences \\*directly\\*. Instead, we \\*use it to select one  index\\* from \\*a list of indexes\\*. In this way, we can \\*change the order\\* in which we \\*traverse\\*  our original list, keeping untouched our original list.  Since \\*batch_size\\* and \\*the length of the input lists\\* are \\*not aligned\\*, gathering a batch_size  group of inputs may involve \\*wrapping back to the beginning of the input loop\\*. In our  approach, it is \\*just enough to reset the index to 0\\*. We can \\*re-shuffle the list of indexes\\* to  produce different batches each time.
    > Đã quen quen với cái này - Data Generator. Nói chung sẽ là như vầy:
    >
    > Cái Generator có đặc điểm là nó sẽ GIỮ giá trị variable của nó giữa những lần yêu
    > cầu nó để lấy batch data cho việc training (invocation) nên cách làm là mình sẽ có
    > một cái variable ví dụ "index". Mỗi khi add một sample vào batch ta sẽ tăng index
    > lên 1. Nhưng ta không dùng nó để lấy data item ra mà là lấy một cái index thứ 2 từ
    > list các index ra rồi mới dùng cái index 2 này để lấy data. Mục đích chính là để
    > shuffle nếu cần, vì chỉ cần thay vì ta shuffle cái bộ data gốc đưa vào thì ta chỉ
    > shuffle cái index list.
    >
    > Cái cuối ý muốn nói nếu khi index (index 1) đã vượt quá số lượng của  bộ data "full"
    > mà chưa đủ số cho batch (kiểu như lần training ở cuối  khi đã loop qua hết số
    > sample) thì ta sẽ reset index về 0 để lấy tiếp, lúc đó có thể shuffle lại nữa (nếu yêu
    > cầu shuffle).
    >
    > Cuối cùng quay lại khúc đầu đại khái cách làm cho vụ padding là mình  cứ lấy một
    > list chứa batch_size các sample ra (bằng cách đã nói ở  trên), sau đó tìm lengh của
    > câu dài nhất. Rồi dùng nó cùng với batch_size để tạo một matrix hay tensor chứa
    > toàn index của padded  token. Xong mới loop trong cái temporal list để lấy các giá
    > trị trong đó  và update vào cái tensor "pad"

    > lines_index = [*range(num_lines)]: Chính là tạo ra một list chứa
    > index của các câu.

    <br>

      <a id="node-2454"></a>
      <p align="center"><kbd><img src="assets/701dda6cde5038fd2a5bcf863ed6f98ca18d4723.png" width="100%"></kbd></p>
      <p align="center"><kbd><img src="assets/701dda6cde5038fd2a5bcf863ed6f98ca18d4723.png" width="100%"></kbd></p>
      <p align="center"><kbd><img src="assets/432ed14dcfbbd9340fda2e007bc6de42992c300e.png" width="100%"></kbd></p>
      <br>

<a id="node-2455"></a>
- Exercise 1 - data_generator (UNQ_C1)
  <br>

    <a id="node-2456"></a>
    <p align="center"><kbd><img src="assets/b8a64fdc3cea309ea902f5111bf248c916d15bd0.png" width="100%"></kbd></p>
    <br>

    <a id="node-2457"></a>
    <p align="center"><kbd><img src="assets/6b04060b425f74723c10a251383faecb2eb7bd71.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/6b04060b425f74723c10a251383faecb2eb7bd71.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/c3640145d4b25d550f18604e0b93f3fc660ee073.png" width="100%"></kbd></p>
    <br>

    <a id="node-2458"></a>
    <p align="center"><kbd><img src="assets/0f1ec9b14851032c4514b971a36d6a463a8e511b.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/0f1ec9b14851032c4514b971a36d6a463a8e511b.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/54ec2b8d6c682cfa3f73fc7a047350e60a1b538e.png" width="100%"></kbd></p>
    <br>

    <a id="node-2459"></a>
    <p align="center"><kbd><img src="assets/6018d60ce931391c76e446fe723337a510eca50e.png" width="100%"></kbd></p>
    <br>

<a id="node-2460"></a>
- 2 - Building the Model
  <br>

    <a id="node-2461"></a>
    <p align="center"><kbd><img src="assets/e2d7f9bfecec178b5e15a1c105aac72a298df7eb.png" width="100%"></kbd></p>
    <br>

<a id="node-2462"></a>
- Exercise 2 - NER (UNQ_C2)
  <br>

    <a id="node-2463"></a>
    <p align="center"><kbd><img src="assets/7500d5da6e40047027beedf1d860c3b50a043c2c.png" width="100%"></kbd></p>
    <br>

    <a id="node-2464"></a>
    <p align="center"><kbd><img src="assets/bbcb9bbd64506a7658ab1cd987e9bae3c2c0fd76.png" width="100%"></kbd></p>
    > Trong Trax, đại khái có điểm chú ý là trong Trax số lượng unit của hidden
    > state nên bằng với embedding vector input x. Có nghĩa là x<t> và c<t> (tất
    > nhiên bằng luôn là a<t> hay h<t>) có length bằng nhau

    <br>

    <a id="node-2465"></a>
    <p align="center"><kbd><img src="assets/ab9a6dde15c4e5db29b0f9a8216e76c8bcb3ba80.png" width="100%"></kbd></p>
    <br>

<a id="node-2466"></a>
- 3 - Train the Model
  <br>

    <a id="node-2467"></a>
    <p align="center"><kbd><img src="assets/9cffa17db6dc5c08c328b97e93d336811c94ac7c.png" width="100%"></kbd></p>
    > Đại khái là dùng function của trax add_loss_weighs(nhận generator
    > khởi tạo bởi data_generator() function mình làm ở trên, với một
    > id_to_mask argument). Mục đích là add padding in the loss weight.
    > Kiểu như data nó có có loss weight để nhấn mạnh một số chỗ này
    > thì quan trọng hơn những chỗ khác, hoặc là nếu có pad token để
    > khi tính loss nó sẽ bỏ qua loss đối với pad token. Function này nó
    > cũng chỉ giống như chỉnh sửa và trả lại một cái Generator mới mà
    > đã có add loss weight ở dạng một tensor chứa weight tương ứng
    > của các vị trí trong index. Nếu chưa generator gốc chưa trả về
    > weight, nó tự tạo weight là một ones-tensor, còn nếu có rồi thì
    > check thêm nếu id_to_mask khác None thì nó sẽ update cái weight
    > sao cho chỗ nào mà là pad (quy định bởi id_to_mask) sẽ bị gán =
    > 0.

    <br>

    <a id="node-2468"></a>
    <p align="center"><kbd><img src="assets/b8b14e105e7ad86c12f03bf3815b8b9fd6a08d82.png" width="100%"></kbd></p>
    > Theo GPT và doc thì hiểu đại khái rằng nếu original generator có trả
    > về weight tensor (bên cạnh data + label tensor) thì nó dùng cái đó,
    > còn không thì nó tạo cái mới "tensor of ones of same shape as
    > target". Sau đó nếu có id_to_mask, nó sẽ căn cứ vào đó mà update
    > weight chỗ nào bị masked trở thành 0.

    <br>

<a id="node-2469"></a>
- Exercise 3 - train_model (UNQ_C3)
  <br>

    <a id="node-2470"></a>
    <p align="center"><kbd><img src="assets/6b077cbfc42126f7c4c203e34efdc0cbb578cd28.png" width="100%"></kbd></p>
    <br>

    <a id="node-2471"></a>
    <p align="center"><kbd><img src="assets/a2e06d405a6c08e9e1685b077d2f13445bb5e78a.png" width="100%"></kbd></p>
    > Chỉ lắp các mảnh
    > ghép lại thôi

    <br>

    <a id="node-2472"></a>
    <p align="center"><kbd><img src="assets/b5ee94cccf034e927dfcdb19e95e8c31a17c14b1.png" width="100%"></kbd></p>
    > Bắt đầu train với
    > 100 train_steps cho thấy accuracy đạt 93%

    <br>

    <a id="node-2473"></a>
    <p align="center"><kbd><img src="assets/9923739d7a05456a2d6eae0ace5c8f7c5e583ba5.png" width="100%"></kbd></p>
    > Load cái model y vậy nhưng được
    > pre-trained lâu hơn tăng performance lên

    <br>

<a id="node-2474"></a>
- 4 - Compute Accuracy
  <br>

    <a id="node-2475"></a>
    <p align="center"><kbd><img src="assets/36f6e6650f0a4c9c8e87ae489b39de8faf476312.png" width="100%"></kbd></p>
    <br>

    <a id="node-2476"></a>
    <p align="center"><kbd><img src="assets/452cdeb05dfc9724d4ff33014f3b148e1a7c389b.png" width="100%"></kbd></p>
    > Một ví dụ cho thấy với x là (batch, max_len) ví dụ (7194, 70) thì sau model cho ra
    > batch, max_len, num_class ví dụ (7194, 70, 17). Vì ứng với mỗi từ (đúng hơn là
    > index của từ) nó sẽ cho ra probability vector chứa 17 p value. Và mình sẽ lấy index
    > (trong vector đó) của thằng có p cao nhất. Sẽ cho ra lại tensor (batch, max_len) và
    > dùng nó để so sánh với y cũng có shape (batch, max_len)

    <br>

<a id="node-2477"></a>
- Exercise 4 - evaluate_prediction (UNQ_C4)
  <br>

    <a id="node-2478"></a>
    <p align="center"><kbd><img src="assets/ef8483464fbebbb1472d5d600247cfd730a55c6d.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/ef8483464fbebbb1472d5d600247cfd730a55c6d.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/191fa1fb3f45cf7c22a7c81255ca49e80527f7d3.png" width="100%"></kbd></p>
    > 1. Như đã phân tích, ta **cần lấy index của vị trí có giá trị cao nhất trong  probability vector.**
    >
    > Nhưng không chỉ có 1 vector mà là một list Tx từ nên có Tx vector vector. Và lại có batch câu.
    >
    > Nên **prediction output tensor y^**sẽ có shape là  batch x Tx (chiều dài sequence) x n_classes.
    >
    > Do đó **trục thứ nhất axis = 0** là **batch size** lấy trong trục này là **lấy một câu nào đó trong batch.**
    >
    > **Trục thứ hai axis = 1** là **số từ Tx** hay đúng hơn là token trong sequence. Loop trong đây là **loop
    > trong các từ | time-step trong câu.**
    >
    > **Trục thứ ba, axis = 2** mới là **probability vector**. Vậy để lấy index mà có giá trị p max trong từng
    > vector thì phải để axis = 2
    >
    > 2. Cái mask: Vì labels (b,max_len) là tensor chứa g.t. label đã được padded. Nên chỉ việc so sánh (!=)
    > nó với pad index sẽ cho ra tensor cùng shape mà chỗ nào trong labels bằng với pad index thì chỗ đó =
    > 0, chỗ nào không phải pad thì chỗ đó = 1. Thì sum của mask tensor này chính là tổng số từ không phải
    > pad.
    >
    > 3.Cái cuối chính là **so sánh output** với **ground-truth label**, mà y sẽ có shape là: **Batch x Tx**: Có
    > batch câu, mỗi câu có Tx từ (có thể sẽ lấy Tx là câu dài  nhất trong batch) Mỗi từ gắn với index của
    > Entity class
    >
    > -> shape y: **batch_size x Tx**
    >
    > Kết quả của output sau khi lấy argmax của y^ cũng là **batch_size x Tx.** **So sánh hai thằng đó sẽ ra
    > một tensor mà chỗ nào chúng nó bằng  nhau thì là True, ngược lại thì False**. Do đó **sum hết lại
    > chính là những từ được predict Named Entity đúng.**
    >
    > Sau đó chia cho sum(mask). **Khả năng cao mask ta sẽ tạo một tensor số 1 hết, trừ chỗ nào là padded
    > token sẽ là 0**. Nên sum **mask tính là tất cả các từ trong tensor.**

    <br>

    <a id="node-2479"></a>
    <p align="center"><kbd><img src="assets/f9da1843f96ffd9ec481578e6c285a5dd2fadb69.png" width="100%"></kbd></p>
    <br>

    <a id="node-2480"></a>
    <p align="center"><kbd><img src="assets/7560ac2a718850a4567e041ae2bfc7ff2642d451.png" width="100%"></kbd></p>
    <br>

<a id="node-2481"></a>
- 5 - Testing with your Own Sentence
  <br>

    <a id="node-2482"></a>
    <p align="center"><kbd><img src="assets/803c648f7fa7495fb6745cee78ba6994ac353849.png" width="100%"></kbd></p>
    <br>

    <a id="node-2483"></a>
    <p align="center"><kbd><img src="assets/79ac41c4b6cbb0e7e1e3bfd7e94bc3f33a7cc316.png" width="100%"></kbd></p>
    <br>

