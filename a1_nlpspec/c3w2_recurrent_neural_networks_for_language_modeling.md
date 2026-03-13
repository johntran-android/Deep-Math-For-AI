# C3w2_recurrent Neural Networks For Language Modeling

📊 **Progress:** `67` Notes | `146` Screenshots

---

Learn about the limitations of traditional language models and see how RNNs and GRUs 
use sequential data for text prediction. Then build your own next-word generator using a 
simple RNN on Shakespeare text data!

Learning Objectives

 • N-grams
 • Gated recurrent units
 • Recurrent neural networks

<a id="node-2152"></a>
## Traditional Languages Models

<br>


<a id="node-2153"></a>
### 1 N-gram language models have **limitations** in terms of **space** and **memory requirements.**

> [!NOTE]
> 1 N-gram language models have **limitations** in terms of **space** and **memory requirements.**
>
> 2 To compute the **probability of a sequence of word**s,**N-gram models require computing conditional
> probabilities for bigrams** or higher-order N-grams.
>
> 3 The p**robability of a sentence** in an N-gram model is obtained by **multiplying the probabilities of each
> word using its previous (N-1) words**.
>
> 4 N-gram models **struggle to capture dependencies between words that are far apart**, as they would
> **require accounting for conditional probabilities in very long word sequences.**
>
> 5 **Estimating** these probabilities **becomes challenging** with **large corpora**, and **storing all possible
> combinations of probabilities** would **require significant space and memory**.
>
> 6 **Recurrent Neural Networks (RNNs)** and **Gated Recurrent Units (GRUs)** are **more efficient models**
> for **natural language processing (NLP)** tasks like **machine translation.**
>
> 7 **RNNs and GRUs** are **more suitable for scenarios with limited space**, such as **mobile applications**,
> as they do**not require storing the entire probability distribution** like N-gram models.
>
> 8 **RNNs** are introduced as an alternative to traditional N-gram language models in this video, offering
> more efficient approaches for NLP tasks.

<br>

<a id="node-2154"></a>

<p align="center"><kbd><img src="assets/a210392f2c31afd45c562f4435e5eca831776a6e.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là với N-Gram model ra được câu này là có P(sen) cao nhất.

  <br>

<a id="node-2155"></a>

<p align="center"><kbd><img src="assets/95b804b56fd5ca8f9b21feb6ba18a64ccd9a6ddb.png" width="100%"></kbd></p>

> [!NOTE]
> Xác suất của từ tiếp theo sẽ phụ thuộc vào n-1 từ trước đó (N-gram). Hạn
> chế của phương pháp này là nó khó nắm bắt được dependencies của
> những từ ở xa và nếu có làm được cũng cần rất nhiều space và RAM

  <br>


<a id="node-2156"></a>
## RNN

<br>


<a id="node-2157"></a>
### 1 **Recurrent Neural Networks (RNNs)** have **advantages** over \\*traditional N-gram language

> [!NOTE]
> 1 **Recurrent Neural Networks (RNNs)** have **advantages** over **traditional N-gram language
> models** in **capturing dependencies** that **N-grams cannot capture**.
>
> 2 **RNNs** can **propagate information** **from the beginning to the end of a sequence**, allowing for
> **better predictions**.
>
> 3 Traditional language models, like **trigrams**, may **select the most probable word based on the
> previous context**, but it **may not make sense in the context of the sentence.**
>
> 4 RNNs are **not limited to considering only the previous n words** and **can use information from the
> entire sequence.**
>
> 5 To capture dependencies for sentence completion using an N-gram model, one would need to
> account for impractical and lengthy sequences of words.
>
> 6 RNNs propagate information through a sequence by computing values at each step, **using
> information from previous computations** and the **current word**.
>
> 7 The computations in an RNN are **repeated for each word in the sequence**, with the **same
> weights**multiplied to propagate information.
>
> 8 RNNs are called **recurrent** because they \\_**repeatedly feed the computed values to
> themselves**\\_ **until** a **prediction is made**.
>
> 9 The main advantage of RNNs is **their ability to propagate information within sequences**, **sharing
> most of the parameters in the computations**.
>
> 10 **Different types of RNN architectures** will be explored in the next video, along with guidelines on
> when to use each type.

<br>

<a id="node-2158"></a>

<p align="center"><kbd><img src="assets/298e1152b6034f1c8e33e5bb1fc7e683aa59f981.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là nếu dùng **N-gram ví dụ 3-gram** trong bài toán này nó
> sẽ chọn từ have vì "did not have" có **xác suất cao trong corpus**
> nhưng **rõ ràng là sai bét.**

  <br>

<a id="node-2159"></a>

<p align="center"><kbd><img src="assets/ff13d1e3a59a84d8e5d9fc73f488c77e9590e6e2.png" width="100%"></kbd></p>

> [!NOTE]
> Ý nói **để làm đúng được** nó phải **dựa trên context là cả
> câu chứ không thể chỉ dựa vào vài từ trước đó**.

  <br>

<a id="node-2160"></a>

<p align="center"><kbd><img src="assets/a6d62c7c147a2146d830ed514f4431cd003c2680.png" width="100%"></kbd></p>

> [!NOTE]
> **Mỗi lần tính toán (cho một từ, một time step)** nó sẽ lấy thông
> tin từ trước đó và hiện tại do đó kết quả của từ cần tìm sẽ được
> dựa trên thông tin từ tất cả các từ trong câu giúp tạo ra kết quả
> chính xác hơn N-gram

  <br>

<a id="node-2161"></a>

<p align="center"><kbd><img src="assets/b5db699251d040f9e0e2642ee1bc4aead6e4af48.png" width="100%"></kbd></p>

> [!NOTE]
> Chữ recurrent là vì các **time-step** đều được **share cùng một
> Wh**, kiểu như tính toán lặp đi lặp lại với input từ time-step trước và
> current word cho đến khi hoàn thành (tìm được từ, hay hoàn thành
> câu)

  <br>

<a id="node-2162"></a>

<p align="center"><kbd><img src="assets/59c70c6259af4623c2ce03bb8e224b8264191a56.png" width="100%"></kbd></p>

  <br>

<a id="node-2163"></a>

<p align="center"><kbd><img src="assets/d8652619717f4fc859cb2ccc4d8ccf3486f00b7a.png" width="100%"></kbd></p>

  <br>


<a id="node-2164"></a>
## Applications Of RNN

<br>


<a id="node-2165"></a>
### 1 **Different tasks in A**I can be **categorized** based on their **input and output nature.**

> [!NOTE]
> 1 **Different tasks in A**I can be **categorized** based on their **input and output nature.**
>
> 2 **One-to-One task**s involve taking a **set of input features** and **returning a single output**.
>
> 3 Fo**r tasks like predicting a team's position on a leaderboard** using **input scores**, a recurrent neural
> network (RNN) isn't significantly different from a conventional neural network.
>
> 4**One-to-Many** tasks involve **taking a single input (e.g., an image)** and **generating multiple outputs (e.g.,
> a caption describing the image).**
>
> 5 **Sentiment analysis** is an example of a**Many-to-One task**, where a **sequence of words is inputted**, and
> the **RNN outputs the sentiment (positive or negative).**
>
> 6**Many-to-Many tasks** involve **multiple inputs and multiple outputs**, such as **machine translation**, where a
> **sequence of words in one language is translated to another language**.
>
> 7 The **encoder-decoder architecture** is commonly **used in machine translation**, with the**encoder capturing
> the overall meaning of the input sentenc**e and the **decoder generating the translated sequence.**
>
> 8 **RNNs** are **powerful architectures** that can be **used to solve various problems in natural language
> processing (NLP)**, including **machine translation and caption generation.**
>
> 9 **RNNs** are **versatile tools**that can be **shaped according to the specific task requirements.**
>
> 10 Choosing the appropriate RNN architecture depends on the task at hand.
>
> 11 The next video will cover a simple recurrent neural network, which can be applied to the different
> architectures discussed.

<br>

<a id="node-2166"></a>

<p align="center"><kbd><img src="assets/1d7f29343ebc1464915fed1863e5879b2a55b329.png" width="100%"></kbd></p>

  <br>

<a id="node-2167"></a>

<p align="center"><kbd><img src="assets/033d1985aadf6faf27730740258d933ed4a50d74.png" width="100%"></kbd></p>

  <br>

<a id="node-2168"></a>

<p align="center"><kbd><img src="assets/27cd731f8c91d03a239e409a726de9dff2e2deed.png" width="100%"></kbd></p>

  <br>

<a id="node-2169"></a>

<p align="center"><kbd><img src="assets/b73dccae22b198f7133f38b66d1ab99ce4272b7e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b73dccae22b198f7133f38b66d1ab99ce4272b7e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/90aec5fb963c0fedd78b8dc28419c6fd7cbc65f0.png" width="100%"></kbd></p>

  <br>

<a id="node-2170"></a>

<p align="center"><kbd><img src="assets/d0f53ae2db1bacf8ca764a08fc374e7dca3073e9.png" width="100%"></kbd></p>

  <br>

<a id="node-2171"></a>

<p align="center"><kbd><img src="assets/7b1c57077c59878274caa788d228b633685bdabe.png" width="100%"></kbd></p>

  <br>


<a id="node-2172"></a>
## Math In RNN

<br>


<a id="node-2173"></a>
### 1 **Recurrent Neural Networks**(RNNs) are **powerful models** for **processing sequential data** and \\*making sequential

> [!NOTE]
> 1 **Recurrent Neural Networks**(RNNs) are **powerful models** for **processing sequential data** and **making sequential
> predictions**.
>
> 2 The computation in a **plain or vanilla RNN** involves taking an **input x**, a**hidden state h**, and producing a
> p**rediction y^** at each**time step <t>**
> 3 The hidden state at each time step is computed using an **activation function g**, which takes the **product of a
> weight matrix Wh** and the previous **hidden state h<t-1>, concatenated with the input
> variable x<t>** and **a bias term bh**
>
> 4 The **prediction y^** is obtained by using an **activation function g** with the **product** of the **hidden state h<t>** and
> another set of parameters **Wy** plus a **bias term by.**
>
> 5 These equations represent the **mathematical operations** performed in a simple RNN.
>
> 7 The hidden states in RNNs enable the **propagation of information through time**, allowing the network to
> **capture dependencies across different positions** **within a sequence.**
>
> 8 Diagrams similar to the one presented in the video are often used in RNN literature to illustrate the
> **computation flow** and **information propagation** within a recurrent unit.
>
> 9 **Hidden states** serve as the **variables that facilitate information propagation in RNNs.**
>
> 10 The video provides an introduction to the forward propagation equations and the concept of hidden states in
> RNNs, with the promise of explaining the cost function in the next video.

<br>

<a id="node-2174"></a>

<p align="center"><kbd><img src="assets/926f962ff1091093922ff08ce06c798d64da65a0.png" width="100%"></kbd></p>

  <br>

<a id="node-2175"></a>

<p align="center"><kbd><img src="assets/b785522c5ad4e81f600f75041b4f6cf9baac5b4c.png" width="100%"></kbd></p>

> [!NOTE]
> [h<t-1>, x<t>] tức là h<t-1> sẽ được concatenate với x<t> hoặc cũng
> có thể được triển khai ở dạng riêng biệt Whh và Whx mà trong
> DLSpec mr Andrew ghi là Waa và Wax.
>
> Wh chính là Whh (hay Waa) stack theo phương horizontally với Whx
> (hay Wax).
>
> Activation function là tanh hay reLU (DLSpec).
>
> h<t0) hay a<0> theo DLSpec được initialize là Zeros vector

  <br>

<a id="node-2176"></a>

<p align="center"><kbd><img src="assets/3f21ad24651e7cadd544c72d799d0134cb18b3f0.png" width="100%"></kbd></p>

  <br>

<a id="node-2177"></a>

<p align="center"><kbd><img src="assets/517b3033b925878ba1d15d85eed4a2ab8a5b217f.png" width="100%"></kbd></p>

> [!NOTE]
> Sơ đồ thể hiện các bước tính
> toán của một RNN unit

  <br>

<a id="node-2178"></a>

<p align="center"><kbd><img src="assets/2340aad096ee2d9701c79ffcc58aad45a58fe674.png" width="100%"></kbd></p>

  <br>

<a id="node-2179"></a>

<p align="center"><kbd><img src="assets/c997c89a2a40918b30edc7f3259bdcd4139076dd.png" width="100%"></kbd></p>

> [!NOTE]
> Hidden state h<t> sẽ có vai trò trong việc mang / lưu thông
> tin through time giúp model nắm bắt được các quan hệ của
> các unit / time-step ở xa nhau

  <br>

<a id="node-2180"></a>

<p align="center"><kbd><img src="assets/b09f7ea6adff0c20151f205d44f75410daf60b29.png" width="100%"></kbd></p>

> [!NOTE]
> Theo DLSpec ta đã biết h<t-1> sẽ stack theo vertically với
> x<t> nên kết quả là 4+10 x 1 = 14x1. Nên để nhân matrix
> được thì Wh phải là 4x14 hoặc 14x14.

  <br>


<a id="node-2181"></a>
## Lab: Hidden State Activation

<br>

<a id="node-2182"></a>

<p align="center"><kbd><img src="assets/21c8ff5dbcc723a21c6303121f4989a7df326a80.png" width="100%"></kbd></p>

<br>

<a id="node-2183"></a>

<p align="center"><kbd><img src="assets/305f22f26d649d57f5b8773ab544733f187b877f.png" width="100%"></kbd></p>

> [!NOTE]
> Wh là horizontally stack của Whh và Whx.
> Còn [ h<t-1>, x<t>] là vertically stack của
> h<t-1> và x<t>

<br>

<a id="node-2184"></a>

<p align="center"><kbd><img src="assets/3a7af6cf672f094e59dbbeca168aec295db03f77.png" width="100%"></kbd></p>

<br>

<a id="node-2185"></a>

<p align="center"><kbd><img src="assets/4088fd46b809b91ef990d01e81b737be0ca28ae2.png" width="100%"></kbd></p>

> [!NOTE]
> Để horizontally stack ta dùng concatenate ((matrix 1, matrix 2), axis=)
> axis = 1 tức là "concate theo cột" tức là horizontally ||| + || -> |||||
>
> Cách khác là hstack (horizontally stack)

<br>

<a id="node-2186"></a>

<p align="center"><kbd><img src="assets/9388175c815b03689dd22ba8838dcc3abcc76a3e.png" width="100%"></kbd></p>

<br>

<a id="node-2187"></a>

<p align="center"><kbd><img src="assets/a32272f642cac7f6554105fefd79635825c032e5.png" width="100%"></kbd></p>

> [!NOTE]
> [ h<t-1>, x<t>] là vertically stack của h<t-1> và x<t>

<br>

<a id="node-2188"></a>

<p align="center"><kbd><img src="assets/7d2c9ad959844e732177cfcc1e13c70e52ffb47b.png" width="100%"></kbd></p>

> [!NOTE]
> Để vertical stack ta dùng
> concatenate (axis = 0) hoặc vstack()

<br>

<a id="node-2189"></a>

<p align="center"><kbd><img src="assets/33bccfb3200cda81116b112073b37a93f37855ac.png" width="100%"></kbd></p>

<br>

<a id="node-2190"></a>

<p align="center"><kbd><img src="assets/dddec18ccfd7f9fa51046f9b620741f284ee80b8.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là so sánh thử xem có đúng là hai công thức nhân (nhân
> matrix) Wh là horizontlly stack của Whh và Whx với vertically stack của
> h<t-1> và x<t> có chính là tổng của Whh.h<t-1> và Whx.x<t> hay
> không.

<br>

<a id="node-2191"></a>

<p align="center"><kbd><img src="assets/a9dcd97150259d51c936d7ae84e6ce95854c6948.png" width="100%"></kbd></p>

<br>

<a id="node-2192"></a>

<p align="center"><kbd><img src="assets/7312ac22f5239c428898aca41682f2732e5f4040.png" width="100%"></kbd></p>

> [!NOTE]
> Kết qủa đúng là
> giống nhau

<br>


<a id="node-2193"></a>
### Summary That's it! We've verified that the \\*two formulas

> [!NOTE]
> Summary That's it! We've verified that the **two formulas
> produce the same results**, and seen how to combine
> matrices vertically and horizontally to make that happen.
> We now have all the intuition needed to understand the
> math notation of RNNs.

<br>


<a id="node-2194"></a>
## Cost Function For RNN

<br>

<a id="node-2195"></a>

<p align="center"><kbd><img src="assets/e854853bde170ddb9905b9ae11abb154231140dd.png" width="100%"></kbd></p>

> [!NOTE]
> Cross entropy loss là loss function cho bài toán **multi-class classification**
> Ví dụ **y = [1, 0, 0]** - thể hiện **ground-truth label** là con **mèo** trong bộ 3
> class [mèo gà, chó] và **y^ = [y^_1 y^_2 y^_3]**.
>
> Thì loss (cho training example này) sẽ là **- (1*y^_1 + 0*y^_2 + 0*y^3)** = **- y^1**.
>
> Vậy **muốn giảm loss** thì model phải làm sao cho (**- y^_1)** càng nhỏ càng tốt,
> đồng nghĩa **y^_1** **phải** **càng lớn càng tốt.**
>
> Dẫn tới là nó sẽ adjust weight sao cho nó ra **y^ ví dụ = [0.99, 0.005, 0. 005]** để
> predict image là con mèo.
>
> Trong bài toán này, **nếu nó là mèo thì không thể là gà hay chó**, nên label y là
> **[1 0 0] hoặc [0 1 0]** chứ không thể **[1 1 0]** được.
>
> Và**tổng ba giá trị y^_1, y^_2, y^_3 phải = 1** nên layer cuối sẽ chọn **Softmax**
> activation function và cross function sẽ là **Categorical Cross Entropy**
>
> ===Tuy nhiên nếu là bài toán khác, **multi-label classification** === label cho 1
> example y(i) viết gọn là y sẽ là [1 1 1] thì y^ sẽ có thể là [0.99 0.98 0.98] thì
> activation function sẽ là: **Sigmoid** và loss function tương ứng sẽ là **Binary Cross
> Entropy**

<br>


<a id="node-2196"></a>
### So sánh, ôn lại hai bài toán

> [!NOTE]
> So sánh, ôn lại hai bài toán
> Multi-class và Multi-label

<br>

<a id="node-2197"></a>

<p align="center"><kbd><img src="assets/78c1eec6f2d7db0115d51d0f7eb3f5d89c633e67.png" width="100%"></kbd></p>

  <br>

<a id="node-2198"></a>

<p align="center"><kbd><img src="assets/3deea2a978ee57af449f63c567adedd1058117bc.png" width="100%"></kbd></p>

  <br>

<a id="node-2199"></a>

<p align="center"><kbd><img src="assets/4002537a06cad469bb267b9bac6676f5774a8e43.png" width="100%"></kbd></p>

  <br>

<a id="node-2200"></a>

<p align="center"><kbd><img src="assets/a42169407415bf2d6e589e1607bc9b5a5c740582.png" width="100%"></kbd></p>

  <br>

<a id="node-2201"></a>

<p align="center"><kbd><img src="assets/e21cc06264af64833733357130718c6789615480.png" width="100%"></kbd></p>

  <br>

<a id="node-2202"></a>

<p align="center"><kbd><img src="assets/d75a45a02a0ab8c31557d0500c11db2fa9a833d4.png" width="100%"></kbd></p>

  <br>

<a id="node-2203"></a>

<p align="center"><kbd><img src="assets/f6a2576e57c195e8a9246ebfde09aa9c65699459.png" width="100%"></kbd></p>

> [!NOTE]
> Đối với RNN ta tính trung bình
> loss của các time-step

<br>


<a id="node-2204"></a>
## Implementation Note

<br>

<a id="node-2205"></a>

<p align="center"><kbd><img src="assets/9bf213ba33a7d471210be0b97f3e820a3e8886a6.png" width="100%"></kbd></p>

<br>

<a id="node-2206"></a>

<p align="center"><kbd><img src="assets/0d75ddce52cd702308f3fb29dc4496dd9349e53b.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là nó như một function bình thường làm cái việc là **loop
> trong tất cả các time-step của sequence** (**elements**, **chính là x**
> tensor) để **tính toán các bước của một RNN unit / time-step** dùng
> function **fn** với input là **x** và **previous hidden state là cur_value** để
> được **y<t> = y và h<t> = cur_value** (hay a<t> trong DLSpec).
>
> **Append** y vào ys là một list chứa các y<t>.
>
> Ổng nói sở dĩ phải có cái scan function như này là kiểu như tạo
> một **abstraction function để TF nó tối ưu bằng cách run trên GPU**

<br>

<a id="node-2207"></a>

<p align="center"><kbd><img src="assets/84c899239c8b446aad31ddfcc887aeaff7f0485b.png" width="100%"></kbd></p>

<br>

<a id="node-2208"></a>

<p align="center"><kbd><img src="assets/84c4c2a1119ef859281e75fee867e7ae610ccf99.png" width="100%"></kbd></p>

<br>

<a id="node-2209"></a>

<p align="center"><kbd><img src="assets/c7c690743bd5469a4615effa7adad34544b354b5.png" width="100%"></kbd></p>

<br>


<a id="node-2210"></a>
## Lab: Vanilla RNN, Gru And The Scan

> [!NOTE]
> LAB: VANILLA RNN, GRU AND THE SCAN
> FUNCTION

<br>

<a id="node-2211"></a>

<p align="center"><kbd><img src="assets/4b46447080633743ce9938014e4b1f8c507b4630.png" width="100%"></kbd></p>

<br>


<a id="node-2212"></a>
### Part 1: Forward method for

> [!NOTE]
> Part 1: Forward method for
> vanilla RNNs and GRUs

<br>

<a id="node-2213"></a>

<p align="center"><kbd><img src="assets/b4c2b54b9bd4c689ec51502420db139650558b10.png" width="100%"></kbd></p>

> [!NOTE]
> Embedding size (emb) 128 là**size của embedding vector x<t>**
> (Tất nhiên **nếu xử lý một batch** thì x<t> sẽ là (**batch_size, emb**).
> Hidden state size **h_dim** hoặc **(batch_size, h_dim**) là size của
> **h<t> (hay a<t>** theo DLSpec)

  <br>

<a id="node-2214"></a>

<p align="center"><kbd><img src="assets/860e45c80769a6c870bd52293bffb235572994f9.png" width="100%"></kbd></p>

> [!NOTE]
> Nhận xét, họ không define axis cho np.
> concatenate như trong DLSpec

  <br>

<a id="node-2215"></a>

<p align="center"><kbd><img src="assets/980311e75d69732c5e426c49a4715e8a87e4c2bc.png" width="100%"></kbd></p>

> [!NOTE]
> **Reset gate** thì kiểu như cho**phép model quyết định** thông tin của **c<t>**
>  **có cần phải lấy từ previous hidden state h<t-1> hay không**.
> Ta thấy nếu value (của element trong Reset gate tensor) **gần 1**
> tức là **model nhận thấy h<t-1> quan trọng** cần (cùng với x<t>)
> để tính toán c<t>.
> Còn ngược lại, nó sẽ adjust weight để **Reset gate value ~=0**và
> **c<t> sẽ chỉ ảnh hưởng bởi x<t>**
> Có thể thấy **Update gate** trong GRU với sigmoid function sẽ
> khiến **h<t>** **một là giữ bằng hidden state trước h<t-1>** hoặc **bỏ đi
> thay mới bằng c<t>**. Tất nhiên sigmoid cho ra trong khoảng 0,1
> nhưng như Mr Andrew có nói thực tế nó sẽ ~=0 hoặc ~=1 để
> control việc dùng c<t> hay h<t-1>

  <br>

<a id="node-2216"></a>

<p align="center"><kbd><img src="assets/dca356940b3183d7e19d32e59a4fde468e5d5219.png" width="100%"></kbd></p>

> [!NOTE]
> Update gate của RNN

  <br>

<a id="node-2217"></a>

<p align="center"><kbd><img src="assets/2fc0003b3f5d0d49d958db5194fa9b65c1080794.png" width="100%"></kbd></p>

> [!NOTE]
> Reset gate

  <br>

<a id="node-2218"></a>

<p align="center"><kbd><img src="assets/9ff763a9f4d0991087126f7518137a13b5c74bdf.png" width="100%"></kbd></p>

  <br>


<a id="node-2219"></a>
### Part 2: Implementation of

> [!NOTE]
> Part 2: Implementation of
> the scan function

<br>

<a id="node-2220"></a>

<p align="center"><kbd><img src="assets/2c4b5b9e7932ec4d4443b324388d01e397b6a9cf.png" width="100%"></kbd></p>

  <br>


<a id="node-2221"></a>
### Part 3: Comparison between

> [!NOTE]
> Part 3: Comparison between
> vanilla RNNs and GRUs

<br>

<a id="node-2222"></a>

<p align="center"><kbd><img src="assets/a4a5fcd365d4982e9015a27670707eaa0bc0bce3.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là cho thấy **GRU chậm hơn RNN tuy
> nhiên nó cho phép giữ thông tin liên quan cần
> thiết cho long sequence**s.

  <br>


<a id="node-2223"></a>
## Lab: Working With Jax Numpy And

> [!NOTE]
> LAB: WORKING WITH JAX NUMPY AND
> CALCULATING PERPLEXITY

<br>


<a id="node-2224"></a>
### Jax numpy

<br>

<a id="node-2225"></a>

<p align="center"><kbd><img src="assets/5e3d4a9bb41b65c4563954b6222c37acad22983e.png" width="100%"></kbd></p>

  <br>

<a id="node-2226"></a>

<p align="center"><kbd><img src="assets/f9e9051402511e2a6f19926e040b534e0d25df3c.png" width="100%"></kbd></p>

  <br>


<a id="node-2227"></a>
### Calculating Perplexity

<br>

<a id="node-2228"></a>

<p align="center"><kbd><img src="assets/cc92cf12720f389cf4d5e2d171f7f918867758fe.png" width="100%"></kbd></p>

> [!NOTE]
> Ôn lại perplexity là metric giúp đánh giá một language model xem khả
> năng nó tạo ra một sample (ví dụ như một câu) có giống thật hay
> không. Ta đã học qua, đại khái là nó tính chỉ số này dựa trên xác suất
> của cái câu mà nó tạo có cao hay không. Công thức của nó như vầy.
> Và để tránh "**underflow problems**" - khi số quá nhỏ, thì người ta
> **thường tính log của Perplexity** thay vì Perplexity.
>
> Theo sự hiểu, language model sau khi đ**ược huấn luyện từ một
> corpus** sẽ học được ... kiểu như **"xác suất của các từ trong corpus"**. Do đó **để test 'năng lực' của model**, người ta sẽ **đưa cho model
> xem một sequence các từ và bảo nó dự đoán từ tiếp theo, rồi so sánh
> nó với kết quả thực.**

  <br>

<a id="node-2229"></a>

<p align="center"><kbd><img src="assets/729c2f6f9e56198a8aa4d22bfdc22739bae8c50a.png" width="100%"></kbd></p>

> [!NOTE]
> Các biến đổi dưới dựa vào các công thức sau:
>
> 1. căn bậc N của a là a^(1/N)
>
> 2. 1/a là a^-1
>
> 3. (a^(-1))^(1/N) = a^(-1/N) vì (a^b)^c) = a^(b*c).
>
> 4. Log(a^b) = (1/b)*Log(a)
>
> 5. Log(a*b*c) = Log(a) + Log(b) + Log(c)

  <br>

<a id="node-2230"></a>

<p align="center"><kbd><img src="assets/b9b6f8b7ab2a5b14a0b4b3b58fd86579ee51b69e.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là bài toán của mình sắp tới sẽ là **dùng RNN hay GRU để build một
> language model**, trong đó model sẽ **predict một sequence** (hoặc chính xác
> hơn là **một** **batch các sequence**).
>
> Tất nhiên **ground truth label cũng là môt sequence hay batch các sequence**.
> Ở đây là một kiểu như **cho ví dụ một "bộ" predictions và label**. **Batch size là
> 32**, chiều dài **sequence là 64**. Tuy nhiên để ý predictions có shape là (32 x
> 64 x **256)**
>
> Cái dimension cuối là bởi vì, model không **"một phát" cho ra luôn "từ thứ nhất
> là 5 (**ứng với từ thứ 5 trong vocab là "I" ví dụ vậy), **từ thứ hai là 7**, **từ thứ
> ba là 11**... để rồi một prediction **y^(i)** của nó có dạng **[5 7 11 ...**]
>
> Mà thay vào đó, **tại mỗi vị trí,** nó sẽ cho ra**một array/vector các giá trị xác
> suất** của **các từ trong vocab**, t**ổng các giá trị p này sẽ bằng 1** và để kết
> luận ta sẽ **lấy từ tương ứng với vị trí có p lớn nhất.**
>
> Và ở đây ví dụ vocab có **256 từ. Đó là lí do predictions có shape như vậy**Nói thêm chút xíu không ảnh hưởng đó là, ở ví dụ này, **predictions chứa log
> probabilities** chứ **không phải thuần tuý probabilities**.  Do đó các giá trị của
> y^(i)<1> prediction của example i, tại time-step (từ) thứ 1 sẽ là **một array có tổng
> không bằng 1 (vì là log của prob) chứ không phải prob**

  <br>

<a id="node-2231"></a>

<p align="center"><kbd><img src="assets/51b6746eeb901a8b5b80dc0dd9422b1d5b61fe0d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/51b6746eeb901a8b5b80dc0dd9422b1d5b61fe0d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d88aa660f2f7aeb8408aaee544a13eb515fb5f37.png" width="100%"></kbd></p>

> [!NOTE]
> Vậy thì, nói về **y**, có dạng một **tensor shape:** **m example x số từ
> trong sequence** ví dụ **y(1) có thể là [5 120 4 ...]** thể hiện **câu đúng
> của training example x(1) là [Anh muốn ăn cơm]** trong đó **'Anh' là từ
> thứ 5 trong vocab**, **'muốn' là từ thứ 120**...
>
> Muốn đưa vào model **để tính loss thì cũng phải biến ' Anh', 'muốn',...
> thành one-hot vector** có **độ dài bằng vocab size = 256,** như ta đã biết
> số 1 trong vector sẽ nằm tại index của từ 'Anh' trong vocab.
>
> Do đó ở đây giới thiệu function **tl.one_hot** để **thực hiện việc one-hot
> encoding này**. Người ta dùng **predictions.shape[-1]** để **lấy giá trị của
> last dimension** của predictions chính là **256**. Có thể cho tiện, **thay vì
> phải hard code là 256, hay một variable vocab size nào đó**

  <br>

<a id="node-2232"></a>

<p align="center"><kbd><img src="assets/10904717a47452dad8f2fab3d540160b0b8bd629.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/10904717a47452dad8f2fab3d540160b0b8bd629.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0662a20519ca0b927bb9f5c8eac4bc84eb305c27.png" width="100%"></kbd></p>

> [!NOTE]
> Khúc này là nói về việc **tính log perplexity** theo công thức đây **rất giống
> cách tính loss function**. Hình vẽ lý giải tại sao axis = -1 và log_p sẽ là
> tensor batch_size (32) x Ty (64)

  <br>

<a id="node-2233"></a>

<p align="center"><kbd><img src="assets/1e4edf4420a6beb6e1eba803e65402a3be2a5728.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là **target** như ta nói ở trên **batch (32) x sequence_len
> (64)** khi chưa sử lý one-hot sẽ **có giá trị là index của từ đúng trong
> vocab**. Và **chỗ nào = 0 tức là padding** bởi **zeros padding**.
>
> Ví dụ câu **"I love you"** sẽ thành **[159 23 241 0 0 0 ...0]**với **3 vị
> trí đầu tiên** là **index của từ I, love, you trong vocab**, còn lại **fill 0
> vào cho đủ sequence_len**.
>
> Hiểu vậy rồi thì dễ hiểu tại sao nó tính cái **non_pad** như bên dưới.
> Mục đích của **non_pad có shape là (32x64)** sẽ là cái **filter để nhân
> nó với matrix log sẽ bỏ đi những log của padding**

  <br>

<a id="node-2234"></a>

<p align="center"><kbd><img src="assets/fbb8c0ebc7ddda8f43db6b720c17b821393b5321.png" width="100%"></kbd></p>

  <br>

<a id="node-2235"></a>

<p align="center"><kbd><img src="assets/45222098756ddb33d970241c47aee62383eafb91.png" width="100%"></kbd></p>

> [!NOTE]
> Nhân với log_p để bỏ đi các effect của padding

  <br>

<a id="node-2236"></a>

<p align="center"><kbd><img src="assets/25b1191aa974dc8647d9baff9aba94aafc4d9dc8.png" width="100%"></kbd></p>

> [!NOTE]
> Chỗ này lạ nè, tính perplexity nhìn giống như tính loss
> vậy. Chưa hiểu lắm. Nhưng cứ theo đó mà tính

  <br>

<a id="node-2237"></a>

<p align="center"><kbd><img src="assets/b99c1735f2e3dc3c15b9eac1a16e1bb307529701.png" width="100%"></kbd></p>

  <br>

<a id="node-2238"></a>

<p align="center"><kbd><img src="assets/779482dd4f5a2ce6577a87eacc53d726554e13c7.png" width="100%"></kbd></p>

> [!NOTE]
> Chưa hiểu những mang máng hiểu (tại sao tính perplexity lại như vậy) .
> Giả sử tại một từ có G.T là [0 1 0 0] model predict ra là [a b c d] thì để P
> cao thì b phải cao, không việc nhân với y sẽ khiến trong loss function chỉ
> quan tâm đến b, và muốn giảm loss thì b phải cao lên = tăng khả năng
> đoán đúng. Và ở khía cạnh đánh giá bằng Perplexity, model có muốn có
> Perplexity cao thì cũng phải cho ra con số b cao. Ý nói logic giống nhau,
> khi dùng ylogy^ để xây dựng loss function cũng như là perplexity score.

  <br>

<a id="node-2239"></a>

<p align="center"><kbd><img src="assets/eff54c0c96062bdcfad3cf3c4bb06ced25e2a9e7.png" width="100%"></kbd></p>

  <br>


<a id="node-2240"></a>
## Gru - Gated Recurrent Units

<br>

<a id="node-2241"></a>

<p align="center"><kbd><img src="assets/1baec91eea914f42b6d614c649ee5d725c203472.png" width="100%"></kbd></p>

<br>

<a id="node-2242"></a>

<p align="center"><kbd><img src="assets/193b85fcfdf906ac2b5e76fcd0338d1beaabeb31.png" width="100%"></kbd></p>

> [!NOTE]
> 1 Vanilla RNNs are powerful but suffer from the **vanishing information problem** for
> **long sequences.**
>
> 2 Gated Recurrent Units (GRUs) are **more complex models** that can **handle long
> sequences effectively.**
>
> 3 GRUs **allow relevant information to be preserved** in the**hidden state** over **long
> sequences.**
>
> 4 GRUs can be used for tasks such as predicting missing words in a sentence
> based on context.
>
> 5 GRUs use **relevance** and**update gates** to **control the flow of information in the
> hidden state**.
>
> 6 GRUs are an extension of vanilla RNNs with additional computations.
>
> 7 GRUs take inputs of the current variable (X) and the previous hidden state (h)
> at each time step.
>
> 8 **Relevance gates (Gamma subscript r)** and **update gates (Gamma subscript u)**
> are computed using **sigmoid activation functions**.
>
> 9 **Relevance gates** determine **which information from previous hidden states is
> relevant**.
>
> 10 A **candidate hidden state (h prime)** is computed based on the**previous hidden
> state and the relevance gates.**
>
> 11 A n**ew hidden state** is calculated using the **previous hidden stat**e, **candidate
> hidden state, and update gates.**
>
> 12 **Update gate**s determine h**ow much information from the  previous hidden state
> will be overwritten.**
> 13 A prediction (y hat) is computed using the current hidden state.
>
> 14 GRUs overcome the vanishing information problem and allow for better
> long-term dependency modeling compared to vanilla RNNs.

> [!NOTE]
> Có nói trong DLSpec, nói lại cho nhớ rõ không thừa. Điểm quan trọng
> thứ nhất chính là **Relevant gate** (trong DLSpec mình note là
> **Reset gate**, cũng không sai) cho phép model **đánh giá sự "
> relevant" của các thông tin trước đó h<t0> với thông tin đưa vào hiện
> tại x<t1>** để quyết định sẽ **có hay không nhiều hay ít phần thông tin
> trước đó để kết hợp với thông tin hiện tại để tính ra h'<t1>** tạm gọi là
> **candidate cho hidden state** ở time-step hiện tại.
>
> Và **Update gate** sẽ q**uyết định phần thông tin nào là lấy từ
> candidate này hay từ previous hidden state.** Tức ở đây nó sẽ **dùng
> cả relevant gate và update gate** để **cân nhắc kết hợp thông tin cũ
> và mới dựa theo sự liên quan**.

<br>

<a id="node-2243"></a>

<p align="center"><kbd><img src="assets/56037290360fb8f22cbba61a92906c1fa4919a1b.png" width="100%"></kbd></p>

> [!NOTE]
> Remember that a **vanilla RNN** such as this one computes an activation function
> with the previous hidden states and currents variable X's parameters to get the
> current hidden state. With the current hidden state, another activation function
> is computed to get the current prediction y hat. **This architecture is updating the
> hidden state at every time step, for long sequences, the information tends to
> vanish**. This is one cause of the so-called vanishing gradients problem.

<br>

<a id="node-2244"></a>

<p align="center"><kbd><img src="assets/ea206eb57c6a92e6f7d80fb5a11fe184c250e3ca.png" width="100%"></kbd></p>

<br>

<a id="node-2245"></a>

<p align="center"><kbd><img src="assets/f53abc39355356499c438768e96cfe2ee6d26b20.png" width="100%"></kbd></p>

<br>


<a id="node-2246"></a>
## Lab: Creating A Gru Model Using Trax

<br>

<a id="node-2247"></a>

<p align="center"><kbd><img src="assets/5a0bc51b5934188262c27fdcffd72257856f803a.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái ngắn gọn là minh hoạ **một simple Vanilla neural network
> define với Trax dùng Serial layers combinator**. Trong Trax thì
> **activation function cũng là một layer riêng biệt**. Và cuối cùng nói
> **Trax rất dễ hiểu**, lệnh **print model** sẽ **cho ra ngay cấu trúc
> của model define thế nào thì thấy thế đó** không lòng vòng giấu
> diếm

<br>

<a id="node-2248"></a>

<p align="center"><kbd><img src="assets/c7761dda28448639a6bd82306e3e559fb0c95719.png" width="100%"></kbd></p>

<br>

<a id="node-2249"></a>

<p align="center"><kbd><img src="assets/33a5da9dae6e80db2f8900da5ad87a458abf41f3.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/33a5da9dae6e80db2f8900da5ad87a458abf41f3.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3bad460a726d4104b6c9b3ada5a2d4e9b28e036a.png" width="100%"></kbd></p>

> [!NOTE]
> Giải thích ShiftRight: Tương tự bài toán tạo ra tên khủng long ở DLSpec.
> Nhưng ở đây ta không tự làm quá trình loop (forward) nên không làm như
> trong bài toán đó trong đó define **y<t> = x<t+1>** mà ta sẽ dùng **ShiftRight
> layer n_shifts = 1**. Nói **ngắn gọn lại** cho mục đích của việc này là **để
> model predict một time-step y^<t>** dựa vào **những từ / kí tự trước đó**. Do
> đó ban đầu (time-step 1, chưa có gì), thì đương nhiên phải input vào model
> (x<1>) để predict phải là "chưa có gì", tức x<t> phải = 0. Và ta làm vậy bằng
> cách insert một số 0 vào vị trí đầu của tensor x. Chứ nếu không ShiftRight
> hoá ra model predict lại nhận / dựa vào chữ đầu tiên để predict ra chữ đầu
> tiên à? (Như trong tên khủng long, nhận chữ d rồi predict chữ d thì rõ ràng là
> không đúng)

<br>

<a id="node-2250"></a>

<p align="center"><kbd><img src="assets/96adbf9a5a96954dfb839da3bba2222c0c247937.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/96adbf9a5a96954dfb839da3bba2222c0c247937.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/2ac18e55b23eca3560d3ecf46803b32abbd5f922.png" width="100%"></kbd></p>

> [!NOTE]
> Define một GRU network, lí do **Dense layer có n_units = vocab_size**
> là vì cái này là họ kiểu như nói trước (hướng dẫn) về bài toán dự đoán kí
> tự / generate chuỗi kí tự trong P.A. tương tự như trong bài toán generate
> tên khủng long của DLSpec, trong đó ta tạo một RNN học các pattern
> trong tên khủng long bằng một bộ data tên khủng long. để khi training
> xong, sampling từ model để có tên khủng long mới để mà đặt cho một
> loại khủng long mới phát hiện.
>
> Và **activation z<t> của mỗi time-step tính từ hidden state là một vector
> có size bằng vocab size** (cho dù là bài toán ở cấp kí tự, cũng gọi là
> vocab size),**gọi là logit.**
>
> Và **cái softmax tính với z<t> sẽ cho ra output y<t>**, đương nhiên là
> một **vector dài vocab size, chứa các chỉ số probability score của các kí
> tự**, để rồi cái nào có**p cao nhất sẽ là cái được chọn.** Thì ở đây, **họ còn
> cho z<t> qua một Fully Connected layer trước khi qua softmax** nên có
> thể hiển**độ dài của output từ F.C layer cũng phải bằng vocab size,** do đó
> **số hidden unit của F.C (hay Dense) layer cũng bằng vocab size là
> vậy**.

<br>

<a id="node-2251"></a>

<p align="center"><kbd><img src="assets/9cc172439930d473d5cf7a0ee62a3d69ee237044.png" width="100%"></kbd></p>

> [!NOTE]
> một helper function giúp print
> các layer của model (access
> bằng model.sublayers)

<br>


<a id="node-2252"></a>
## Deep And Bi-directional Rnns

<br>


<a id="node-2253"></a>
### 1 **Deep recurrent neural networks (RNNs)** are useful for \\*capturing dependencies that shallow

> [!NOTE]
> 1 **Deep recurrent neural networks (RNNs)** are useful for **capturing dependencies that shallow
> RNNs cannot capture.**
>
> 2 Equations used in implementing deep RNNs and their relation to the cost function are explained.
>
> 3 Bidirectional neural networks and their importance are introduced.
>
> 4 **Bidirectional RNNs** **propagate information both from the beginning to the end of a sequence** and
> f**rom the end to the beginning**, allowing predictions to be made for missing information.
>
> 5 Bidirectional RNNs are r**epresented as acyclic graphs**where information**flows independently in
> both directions.**
>
> 6 Computation of **hidden states** and **predictions** in a bidirectional RNN involves **propagating
> information from both direction**s.
>
> 7 **Deep RNNs**consist of **multiple hidden layers,** similar to **regular deep neural networks**.
>
> 8 Information**flows through time in deep RNNs**, followed by **propagation through the layers** to
> obtain predictions.
>
> 9 Bidirectional RNNs and deep RNNs are **variations** of the **vanilla RNN model**, offering **more
> complex capabilities.**
>
> 10 The passage concludes by summarizing the topics covered: RNNs, gated recurrent units,
> bidirectional RNNs, and deep RNNs. It mentions that in the assignments, learners will have the
> opportunity to work with RNNs and understand their implementation.

<br>

<a id="node-2254"></a>

<p align="center"><kbd><img src="assets/c130cf58abedf7a0c9f63ca566680ec86f32cc2d.png" width="100%"></kbd></p>

  <br>

<a id="node-2255"></a>

<p align="center"><kbd><img src="assets/c099e7318e6d2365f27e536e486b33d12ed926eb.png" width="100%"></kbd></p>

> [!NOTE]
> An RNN that's **propagates information**from the **beginning to the end**of sequences, would be able to make a prediction tool. It would **take
> the words before the blank as inputs** and **do its best to predict the
> missing word**. However, because **Louise** **doesn't appear until the
> beginning of the next sentenc**e, it would have to guess between **her,
> him and them**

> [!NOTE]
> Như đã biết từ DLSpec, bài toán như thế này sẽ không
> giải quyết được bằng uni-directional RNN vì thông tin
> quan trọng cần thiết lại nằm ở sau.

  <br>

<a id="node-2256"></a>

<p align="center"><kbd><img src="assets/28c619663aaf4d17a5a29401ad7489a02e53e987.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/28c619663aaf4d17a5a29401ad7489a02e53e987.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7f170439cc33a60264f278312857a381fbedbf55.png" width="100%"></kbd></p>

> [!NOTE]
> Thì nếu 'làm' ở chiều ngược lại bắt đầu với
> zeros và tính với các time-step từ T đến t1.
> Hoàn toàn tương tự.

  <br>

<a id="node-2257"></a>

<p align="center"><kbd><img src="assets/4d43fb1384835a43830e423e5fbea7af267428df.png" width="100%"></kbd></p>

> [!NOTE]
> Và bi-directional RNNs sẽ combine
> cả hai chiều đi và về lại.

  <br>

<a id="node-2258"></a>

<p align="center"><kbd><img src="assets/6513074be9300b372b5f11494b9891ce1d843b67.png" width="100%"></kbd></p>

> [!NOTE]
> và prediction y^<t> sẽ được tính
> từ combination cả hidden state
> <t> ở cả hai chiều.

  <br>

<a id="node-2259"></a>

<p align="center"><kbd><img src="assets/d7aab7aecfacc3a7ad7a80e554ab671ad3f626e2.png" width="100%"></kbd></p>

> [!NOTE]
> Deep RNNs sẽ stack các RNNs lại với nhau, thay vì dùng
> Wy tính y^ từ hidden state h<t>, nó sẽ có Wa để tính a<t>
> từ h<t> và dùng a<t> bỏ vào thay cho x của RNNs layer tiếp
> theo.

  <br>

<a id="node-2260"></a>

<p align="center"><kbd><img src="assets/b7502536c17aedf2e48dd3e437fb337dd7275080.png" width="100%"></kbd></p>

  <br>

<a id="node-2261"></a>

<p align="center"><kbd><img src="assets/62799c1d300ddb410b22949c475cb1455aad3ed8.png" width="100%"></kbd></p>

  <br>

<a id="node-2262"></a>

<p align="center"><kbd><img src="assets/86a78af0fb0e8a5949be6bcfc31aa82e3b191ff2.png" width="100%"></kbd></p>

  <br>


<a id="node-2263"></a>
## Week Conclusion

<br>


<a id="node-2264"></a>
## Quiz

<br>

<a id="node-2265"></a>

<p align="center"><kbd><img src="assets/370eef86ac88170a46c24817b309aaaa4da89913.png" width="100%"></kbd></p>

<br>

<a id="node-2266"></a>

<p align="center"><kbd><img src="assets/bde7f8dc483110a8ecd48987ecc037037b1aa834.png" width="100%"></kbd></p>

<br>

<a id="node-2267"></a>

<p align="center"><kbd><img src="assets/73730dad53e3ed8f45ccc303eb50796df980e2d6.png" width="100%"></kbd></p>

<br>

<a id="node-2268"></a>

<p align="center"><kbd><img src="assets/2f2c6fed1a9291d8e65ef7a8fab1ba671386b216.png" width="100%"></kbd></p>

<br>

<a id="node-2269"></a>

<p align="center"><kbd><img src="assets/f6fa4cf07744798bac83b73a9a8be588c1b25eec.png" width="100%"></kbd></p>

> [!NOTE]
> Ý là mỗi từ cần dự đoán tại một time-step chỉ có 1 đáp án đúng chứ
> không phải nhiều đáp án đúng. Nếu nhiều đáp án đúng, hay y<t> là
> multi-hot vector, thì phải tính loss trung bình của nhiều class tại time-step
> đó. Còn phải chia T là vì để tính trung bình loss trên tất cả các time-step
> mới có thể coi là loss của model trên training example x(i). Mỗi time-step
> predict ra một từ, nó cho ra y^(i)<t> là một probability scores vector, để
> so vối y(i)<t> được loss trên time-step <t>. Và loss tính trung trên toàn
> time-step là loss trên training example đó

<br>

<a id="node-2270"></a>

<p align="center"><kbd><img src="assets/c00dbed260daccaf6a40b3edf2ba411acff3915e.png" width="100%"></kbd></p>

<br>

<a id="node-2271"></a>

<p align="center"><kbd><img src="assets/21dea7eb325f0d3d0fa511368d642ee07441211e.png" width="100%"></kbd></p>

<br>

<a id="node-2272"></a>

<p align="center"><kbd><img src="assets/370f6447c0c70f5293005f2552d4ded7ef53f25c.png" width="100%"></kbd></p>

<br>

<a id="node-2273"></a>

<p align="center"><kbd><img src="assets/ece51d2b3962e4eb9428da2a4ab559c9bb9080b7.png" width="100%"></kbd></p>

<br>

<a id="node-2274"></a>

<p align="center"><kbd><img src="assets/af772f8681c548453666d7654b07bcb88e468c6e.png" width="100%"></kbd></p>

<br>


<a id="node-2275"></a>
## P.a Deep N-grams

<br>


<a id="node-2276"></a>
### Welcome to the second assignment of course 3. In this assignment you will explore

> [!NOTE]
> Welcome to the second assignment of course 3. In this assignment you will explore 
> **Recurrent Neural Networks RNN**.
>
>  • You will be using the fundamentals of google's \\_**trax**\\_ package to implement any 
> kind of deeplearning model.
>
> By completing this assignment, you will learn how to implement models from scratch:
>  • How to **convert a line of text** into a **tensor**
>  • **Create an iterator** to **feed data to the model**
>  • Define a **GRU** **model** using **trax**
>  • **Train the model** using **trax**
>  • **Compute the accuracy** of your model using the **perplexity**
>  • **Predict** using your own model

<br>

<a id="node-2277"></a>
- Overview
  <br>

  <a id="node-2278"></a>
  - Your task will be to **predict the next set of characters** using the **previous characters.**  • Although this task **sounds simple**, it is **pretty useful.**  • You will start by **converting a line of text** into a **tensor**  • Then you will **create a generator** to **feed data into the model**  • You will **train a neural network** in order to **predict the new set of characters** of  defined length.  • You will **use embeddings** for each character and **feed them as inputs** to your  model.  ▪ Many **natural language task**s rely on **using embeddings for predictions.**  • Your model will **convert each character to its embedding**, run the embeddings  through a **Gated Recurrent Unit GRU**, and **run it through a linear layer** to predict the next  set of characters.
    > [!NOTE]
    > Đại khái là bài toán **predict một chuỗi kí tự** dựa trên **những kí tự
    > trước đó,** qua đó học được **cách "chuẩn bị" chuỗi kí tự thành một
    > tensor**, tạo một **generator để feed data vào model,** **xây dựng
    > và train một GRU neural network** dùng **trax** cũng như là làm việc
    > với **embedding**.

    <br>

      <a id="node-2279"></a>
      <p align="center"><kbd><img src="assets/daccccf219538f5badbea098cffa6542ce8cf9ae.png" width="100%"></kbd></p>
      <br>

    <a id="node-2280"></a>
    - The figure above gives you a summary of what you are about to implement.  • You will **get the embeddings**;  • **Stack the embeddings on top of each other**;  • Run them through **two layers** with a **relu activation** in the middle;  • Finally, you will **compute the softmax**.  To predict the next character:   • **Use the softmax output**and **identify the word** with the**highest probability.** • The word with the highest probability is the prediction for the next word.
      <br>

        <a id="node-2281"></a>
        <p align="center"><kbd><img src="assets/9ef0d9161ddb19238b20c9e9c750bbebae70070d.png" width="100%"></kbd></p>
        <br>

<a id="node-2282"></a>
- 1 - Importing the Data
  <br>

<a id="node-2283"></a>
- 1.1 - Loading in the Data
  <br>

  <a id="node-2284"></a>
  - Now **import the dataset** and do some **processing**.  • The dataset has **one sentence per line.**  • You will be **doing character generation**, so you have to process each sentence  by **converting each character (and not word) to a number.**  • You will use the **ord** function to c**onvert a unique character** to a**unique integer  ID.**  • **Store** **each line** in a **list**.  • Create a **data generator** that takes in the **batch_size** and the **max_length**.  ▪ The **max_length** corresponds to the **maximum length of the sentence**.
    <br>

      <a id="node-2285"></a>
      <p align="center"><kbd><img src="assets/6bd3ddec9e45902b4f958f25c9df6e690bb9bc17.png" width="100%"></kbd></p>
      > [!NOTE]
      > **Define path** và **filename** để**open file, load data** bỏ
      > đi khoảng trống đầu cuối câu và **add vào lines -
      > dạng một list các sentence.**

      <br>

      <a id="node-2286"></a>
      <p align="center"><kbd><img src="assets/681bea9b71a67c36a4b625928676d9e20098ad4e.png" width="100%"></kbd></p>
      > [!NOTE]
      > **lowercase hết**, và chia ra thành **hai bộ**: **training**
      > set và **validation** set. Validation set lấy **1000 item
      > (sentence | text) cuối cùng** (**[-1000:]**) còn lại là training set.

      <br>

<a id="node-2287"></a>
- 1.2 - Convert a Line to Tensor
  <br>

    <a id="node-2288"></a>
    <p align="center"><kbd><img src="assets/d528c35af1e8b2717d7aaaf8244da0f372d2a4bf.png" width="100%"></kbd></p>
    > [!NOTE]
    > Đại khái là ta sẽ **convert từng character thành
    > number** dùng function **ord**() của Python
    > giúp làm việc này. Nó sẽ **biến kí tự** thành
    > **unicode integer tương ứng.**

    <br>

<a id="node-2289"></a>
- Exercise 1 - line_to_tensor (UNQ_C1)
  <br>

  <a id="node-2290"></a>
  - **Instructions:** **Write a function** that **takes in a single line** and **transforms each character**  into **its unicode integer.** This returns **a list of integers**, which we'll refer to as a **tensor**.  • Use a **special integer** to represent the **end of the sentence** (the end of the line).  • This will be the **EOS_int** (end of sentence integer) parameter of the function.  • Include the **EOS_int**as the **last integer** of the  • For this exercise, you will **use the number 1** to **represent the end of a  sentence.**
    > [!NOTE]
    > Đại khái là **viết một function** nhận một **single line of text** và "
    > chuyển" **character của nó** thành **unicode** integer và **thêm một
    > con số đặc biệt**đóng vai trò đại diện cho **End of Sentence**,
    > mà ở đây sẽ dùng số **1**.

    <br>

      <a id="node-2291"></a>
      <p align="center"><kbd><img src="assets/2b63aeb838844a60abe03f5bc316920b7bafbc60.png" width="100%"></kbd></p>
      <br>

<a id="node-2292"></a>
- 1.3 - Batch Generator
  <br>

  <a id="node-2293"></a>
  - Most of the time in **Natural Language Processing**, and **AI** in general we use **batches** when  training our data sets. Here, you will **build a data generator** that **takes in a text** and  r**eturns a batch of text lines** (lines are **sentences**).   • The **generator** converts **text lines** (sentences) into n**umpy arrays of integers**  **padded by zeros** so that **all arrays have the same length**, which is the **length of the  longest sentence** in the entire data set.  Once you create the generator, you can**iterate on it**like this: **next(data_generator)**  This generator r**eturns the data** in a **format** that you could **directly use in your model** when  computing the **feed-forward of your algorithm**. This iterator returns a **batch of lines** and  **per token mask**. The batch is a tuple of three parts: **inputs**, **targets**, **mask**. The **inputs** and  **targets** are **identical**. The **second column** will be u**sed to evaluate your predictions**. **Mask  is 1 for non-padding tokens.**
    > [!NOTE]
    > Đại khái là thường trong ML và NLP model sẽ "xử lý" từng batch nhiều training
    > sample thay vì chỉ một mỗi lần. Mình sẽ viết một function đóng vai trò là một
    > generator nhận một đoạn text và xử lý sao cho trả về nhiều list (arrays) các tensor,
    > mỗi tensor như nói ở trên là một list các integer đại diện cho character mà bên trên ta
    > đã làm. Function này sẽ dùng một keyword đặc biệt là yield thay vì return mà ta đã
    > biết để có thể giống như trả kết quả về từng batch theo yêu cầu - cho phép có thể "
    > iterate" trong function.
    >
    > Trong function, ta sẽ phải làm sao đó để các tensor có cùng chiều dài lấy bằng chiều
    > dài của tensor dài nhất (câu dài nhất) trong dataset chính là input text (tức là function
    > generator này sẽ nhận nguyên một bộ training dataset mà ta đã chuẩn bị ở trên ~
    > sương sương hơn 100k lines). Các câu sẽ được padding (fill) với số 0 để đạt đủ
    > chiều dài. Và tương ứng ta cũng sẽ trả về một cái mask - kiểu như một cái matrix
    > bằng shape với batch of tensor mà ta trả ra nhưng chỗ nào là padding sẽ là 0, còn
    > không phải padding sẽ là 1.

    <br>

    <a id="node-2294"></a>
    - **Instructions:** Implement the data generator below. Here are some things you will need.  • **While True loop**: this will **yield one batch** at a time.  • **if index >= num_lines**, **set index to 0**.  • The generator should return **shuffled** batches of data. To achieve this **without  modifying the actual lines** a **list containing the indexes of data_lines** is created. This list  can be **shuffled** and **used to get random batches** everytime the index is reset.  • **if len(line) < max_length** **append line to cur_batch**.  ▪ Note that a line that has **length equal** to **max_length** should **not be appended**  to the batch.  ▪ This is because **when converting the characters into a tensor of integers**, an  **additional end of sentence token id will be added**.  ▪ So if max_length is 5, and a line has 4 characters, the tensor representing  those 4 characters plus the end of sentence character will be of length 5, which is the  max length.  • if **len(cur_batch) == batch_size**, go over every line, convert it to an int and  store it. **Remember that when calling np you are really calling trax.fastmath.numpy which is  trax’s version of numpy that is compatible with JAX. As a result of this, where you  used to encounter the type numpy.ndarray now you will find the type  jax.interpreters.xla.DeviceArray.**
      <br>

<a id="node-2295"></a>
- Exercise 2 - data_generator (UNQ_C2)
  <br>

    <a id="node-2296"></a>
    <p align="center"><kbd><img src="assets/b945e27d4dfb0f96a267bdc9f0262d3f3943b858.png" width="100%"></kbd></p>
    <br>

    <a id="node-2297"></a>
    <p align="center"><kbd><img src="assets/f4b29b23e744c2a8d444c1ebc63f7e7940f0b882.png" width="100%"></kbd></p>
    <br>

    <a id="node-2298"></a>
    <p align="center"><kbd><img src="assets/4b5d91d5facc60e998611d223933bce713022c4f.png" width="100%"></kbd></p>
    <br>

    <a id="node-2299"></a>
    <p align="center"><kbd><img src="assets/55e146eb00585987907cb1c6fbeb0f3b54e83a61.png" width="100%"></kbd></p>
    <br>

  <a id="node-2300"></a>
  - Now that you have your generator, you can just call them and they will return tensors which correspond to your lines in Shakespeare. The**first column and the second column are identical**. Now you can go ahead and start building your neural network
    <br>

<a id="node-2301"></a>
- 1.4 - Repeating Batch Generator
  <br>

  <a id="node-2302"></a>
  - The way the iterator is currently defined, it will **keep providing batches forever.**  Although it is not needed, we want to show you the**itertools.cycle function** which is really  **useful when the generator eventually stops**  Notice that **it is expected to use this function within the training function** further below  Usually we want to**cycle over the dataset multiple times during training** (i.e. train for  **multiple \\/epochs**\\/).  For small datasets we can use \\_**itertools.cycle**\\_ to achieve this easily.
    > [!NOTE]
    > Chưa hiểu lắm đại khái là giới thiệu một cách tiện lợi để
    > chạy qua / lướt qua dataset nhiều lần kiểu như nhiều
    > epoches

    <br>

      <a id="node-2303"></a>
      <p align="center"><kbd><img src="assets/d25a07a23b0c27458f7216b48f1a6db322f44fca.png" width="100%"></kbd></p>
      > [!NOTE]
      > Đại khái hiểu là giúp khi cycle
      > qua dataset nhiều lần

      <br>

    <a id="node-2304"></a>
    - The purpose of using itertools.cycle in this context is to create an iterator that can provide  an infinite sequence of batches of data. The iterator keeps cycling through the provided data repeatedly, allowing for easy repetition of the dataset during training.  In the given code, the infinite_data_generator is created using itertools.cycle. It takes the output of the data_generator function, which likely generates batches of data for training a machine learning model. By using itertools.cycle, the data generator is transformed into an infinite iterator.  This is particularly useful when training a model for multiple epochs or repeatedly cycling over the dataset. During each iteration, the next function is called on the infinite_data_generator to retrieve the next batch of data. Since itertools.cycle ensures that the iterator keeps cycling indefinitely, it allows for seamless access to the dataset without explicitly handling the end of the data.  The use of itertools.cycle **simplifies** the **process of iterating over the dataset** **multiple times**, especially when dealing with small datasets. It **eliminates t**he need to **manually reset or handle the end of the dataset**, making it **convenient**for**training functions**that **require repeated access to the data.**
      <br>

<a id="node-2305"></a>
- 2 - Defining the GRU Model
  <br>

  <a id="node-2306"></a>
  - Now that you have the input and output tensors, you will go ahead and **initialize your  model**. You will be implementing the **GRULM**, **gated recurrent unit**model. To implement  this model, you will be using **google's trax package**. Instead of making you implement the GRU from scratch, we will give you the **necessary method**s from a build in package.  You can use the following packages when constructing the model:
    > [!NOTE]
    > Rồi bây giờ đến build
    > GRU model với trax

    <br>

      <a id="node-2307"></a>
      <p align="center"><kbd><img src="assets/ab5fa4de1964aa393a417028cc997a8136b7eda2.png" width="100%"></kbd></p>
      > [!NOTE]
      > Thì đại khái là ta sẽ dùng những cái này, đầu tiên là Serial layer giúp combine các layer serially
      > (tuần tự) chỉ việc bỏ các layer vào, cách nhau bởi dấu phẩy. Còn ShiftRight thì man mán hiểu là
      > giúp shift "chuyển dịch" input sentence qua bên phải 1 vị trí (default n_shifts = 1) bằng cách chèn
      > số 0 vào trước, nhằm mục đích gì chưa hiểu lắm

      <br>

      <a id="node-2308"></a>
      <p align="center"><kbd><img src="assets/33a5da9dae6e80db2f8900da5ad87a458abf41f3.png" width="100%"></kbd></p>
      <p align="center"><kbd><img src="assets/33a5da9dae6e80db2f8900da5ad87a458abf41f3.png" width="100%"></kbd></p>
      <p align="center"><kbd><img src="assets/3bad460a726d4104b6c9b3ada5a2d4e9b28e036a.png" width="100%"></kbd></p>
      > [!NOTE]
      > Tương tự bài toán tạo ra tên khủng long ở DLSpec. Nhưng ở đây ta
      > không tự làm quá trình loop (forward) nên không làm như trong bài toán
      > đó trong đó define **y<t> = x<t+1>** mà ta sẽ dùng **ShiftRight layer
      > n_shifts = 1**. Nói **ngắn gọn lại** cho mục đích của việc này là **để
      > model predict một time-step y^<t>** dựa vào **những từ / kí tự trước
      > đó**. Do đó ban đầu (time-step 1, chưa có gì), thì đương nhiên phải input
      > vào model (x<1>) để predict phải là "chưa có gì", tức x<t> phải = 0. Và ta
      > làm vậy bằng cách insert một số 0 vào vị trí đầu của tensor x. Chứ nếu
      > không ShiftRight hoá ra model predict lại nhận / dựa vào chữ đầu tiên để
      > predict ra chữ đầu tiên à? (Như trong tên khủng long, nhận chữ d rồi
      > predict chữ d thì rõ ràng là không đúng)

      <br>

      <a id="node-2309"></a>
      <p align="center"><kbd><img src="assets/dc704b586df8393a0b0ea013121846b8fac2182a.png" width="100%"></kbd></p>
      <br>

<a id="node-2310"></a>
- Exercise 3 - GRULM (UNQ_C3)
  <br>

    <a id="node-2311"></a>
    <p align="center"><kbd><img src="assets/96adbf9a5a96954dfb839da3bba2222c0c247937.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/96adbf9a5a96954dfb839da3bba2222c0c247937.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/61fc1c27327bf23bf025251dadfdcbc7a61dad76.png" width="100%"></kbd></p>
    > [!NOTE]
    > Define một GRU network, lí do **Dense layer có n_units = vocab_size**
    > là vì cái này là họ kiểu như nói trước (hướng dẫn) về bài toán dự đoán kí
    > tự / generate chuỗi kí tự trong P.A. tương tự như trong bài toán generate
    > tên khủng long của DLSpec, trong đó ta tạo một RNN học các pattern
    > trong tên khủng long bằng một bộ data tên khủng long. để khi training
    > xong, sampling từ model để có tên khủng long mới để mà đặt cho một
    > loại khủng long mới phát hiện.
    >
    > Và **activation z<t> của mỗi time-step tính từ hidden state là một vector
    > có size bằng vocab size** (cho dù là bài toán ở cấp kí tự, cũng gọi là
    > vocab size),**gọi là logit.**
    >
    > Và **cái softmax tính với z<t> sẽ cho ra output y<t>**, đương nhiên là
    > một **vector dài vocab size, chứa các chỉ số probability score của các kí
    > tự**, để rồi cái nào có**p cao nhất sẽ là cái được chọn.** Thì ở đây, **họ
    > còn cho z<t> qua một Fully Connected layer trước khi qua softmax** nên
    > có thể hiển**độ dài của output từ F.C layer cũng phải bằng vocab size,**
    > do đó **số hidden unit của F.C (hay Dense) layer cũng bằng vocab size
    > là vậy**.

    <br>

    <a id="node-2312"></a>
    <p align="center"><kbd><img src="assets/093dbfe46263c3b27c0ccdadbd231d1cbd88a006.png" width="100%"></kbd></p>
    <br>

<a id="node-2313"></a>
- 3 - Training
  <br>

  <a id="node-2314"></a>
  - Now you are **going to train your model**. As usual, you have to **define the cost function**, the **optimizer**, and **decide whether you will be training it** on a **gpu** or **cpu**. You also have to**feed in a built model**. Before, going into the training, we re-introduce the **TrainTask** and **EvalTask** **abstractions** from the**last week's assignment.**  To train a model on a task, Trax defines an **abstraction** t**rax.supervised.training**.**TrainTask** which **packages the train data, loss and optimizer (among other things) together into an object.**  Similarly to evaluate a model, Trax defines an abstraction **trax.supervised.training.EvalTask** which **packages the eval data and metrics** (among other things) into another object.  The final piece tying things together is the **trax.supervised.training.Loop abstraction** that is a very **simple and flexible** way to **put** **everything together** and train the model, all the while **evaluating it and saving checkpoint**s. Using **training.Loop** will **save you a lot of code** compared to always **writing the training loop by hand**, like you did in **courses 1 and 2.** More importantly, you are**less likely to have a bug** in that code that would **ruin your training**
    > [!NOTE]
    > Đại khái là nhắc lại những **cái abstraction TrainTask, EvalTask** giúp **đóng gói
    > training/evaluation data, optimizer và loss** lại thành một **object**, và **Loop giúp
    > handle phần training loop, save checkpoint..**. t**hay vì phải tự viết giúp giảm
    > nguy cơ bug.**

    <br>

    <a id="node-2315"></a>
    - An **epoch** is traditionally defined as **one pass through the dataset.**  Since the **dataset was divided in batches** you need **several steps (gradient evaluations)** in order to complete an epoch. So, one epoch corresponds to the **number of examples in a batch** times the **number of steps**. In short, in **each epoch** you **go over all the dataset.**  The **max_length** variable defines the **maximum length of lines** to be used in training our data, **lines longer than that** length **are discarded.**  Below is a function and results that indicate **how many lines conform to our criteria of maximum length** of a sentence **in the entire dataset** and **how many steps are required in order to cover the entire dataset** which in turn corresponds to an **epoch**..
      > [!NOTE]
      > Đại khái là nói lại về **định nghĩa của một epoch** là sao, nó là **một lần loop qua
      > hết toàn bộ training** data. Vì **bộ data chia thành nhiều batch**, trong đó **model
      > sẽ xử lý từng batch và gradient descent update**, nên **một epoch là bằng số step
      > (tức là số batch) nhân với số training data trong batch**. Ở đây đại khái là **viết
      > function tính thử xem sẽ có bao nhiêu batch / hay bao nhiêu step trong toàn bộ
      > dataset**, vì ta không dùng toàn bộ dataset mà **bỏ đi những câu dài hơn
      > max_len** (phần tạo generator có làm) khi tính function này phải trừ đi những câu
      > dài hơn max_lenght

      <br>

        <a id="node-2316"></a>
        <p align="center"><kbd><img src="assets/dcb42c8bab61d39c6a883603a3d098396a2e700d.png" width="100%"></kbd></p>
        > [!NOTE]
        > Ví dụ batch_size = 4.

        <br>

        <a id="node-2317"></a>
        <p align="center"><kbd><img src="assets/4f9a30aab8905959643b810a9ef27d9f17a24360.png" width="100%"></kbd></p>
        <br>

<a id="node-2318"></a>
- 3.1 - Training the Model
  <br>

    <a id="node-2319"></a>
    <p align="center"><kbd><img src="assets/70fffd1f0cb3d95065769ddf07fd85385aa3e233.png" width="100%"></kbd></p>
    <br>

<a id="node-2320"></a>
- Exercise 4 - train_model (UNQ_C4)
  <br>

    <a id="node-2321"></a>
    <p align="center"><kbd><img src="assets/1bab6ee9a614ba43da2ebc0558953bb673f47ef5.png" width="100%"></kbd></p>
    <br>

    <a id="node-2322"></a>
    <p align="center"><kbd><img src="assets/103fd15bcd3b29d50b97520511a7f7cb95810b62.png" width="100%"></kbd></p>
    <br>

    <a id="node-2323"></a>
    <p align="center"><kbd><img src="assets/ad46a24a4df9c9a66fbef32aeb701e3a8e6e896d.png" width="100%"></kbd></p>
    <br>

<a id="node-2324"></a>
- 4 - Evaluation
  <br>

    <a id="node-2325"></a>
    <p align="center"><kbd><img src="assets/44bf2efb5d6c71309527abe6aaa4095e7db0e861.png" width="100%"></kbd></p>
    <br>

<a id="node-2326"></a>
- 4.1 - Evaluating using the Deep Nets
  <br>

<a id="node-2327"></a>
- Exercise 5 - test_model (UNQ_C5)
  <br>

    <a id="node-2328"></a>
    <p align="center"><kbd><img src="assets/3627f4de4968f55c7674afcab58ce7d411fb9631.png" width="100%"></kbd></p>
    > [!NOTE]
    > Nếu thấy khó hiểu, xem lại Lab
    > trước, đã giải thích rất rõ

    <br>

    <a id="node-2329"></a>
    <p align="center"><kbd><img src="assets/b8f45d7f6059f21a54c01d02bf152314ca2bed73.png" width="100%"></kbd></p>
    <br>

<a id="node-2330"></a>
- 5 - Generating the Language with your Own Model
  <br>

    <a id="node-2331"></a>
    <p align="center"><kbd><img src="assets/ba0b1e5e172c98ba1f872fb5493f055ca536472b.png" width="100%"></kbd></p>
    <br>

    <a id="node-2332"></a>
    <p align="center"><kbd><img src="assets/ce2a52ae2d2f3826cade5294078f775b65f4bce2.png" width="100%"></kbd></p>
    > [!NOTE]
    > In the generated text above, you can see that the model
    > generates text that **makes sense capturing dependencies
    > between words and without any input.** A**simple n-gram
    > model would have not been able to capture all of that in
    > one sentence.**

    <br>

    <a id="node-2333"></a>
    <p align="center"><kbd><img src="assets/12ad0179250efc969a53ca7ec90a1026b2b3b172.png" width="100%"></kbd></p>
    <br>

    <a id="node-2334"></a>
    <p align="center"><kbd><img src="assets/36832ec0102f688254a535f2b78cfdac655a4461.png" width="100%"></kbd></p>
    <br>

    <a id="node-2335"></a>
    <p align="center"><kbd><img src="assets/58f6315675735354c4e927485e803757b784ee91.png" width="100%"></kbd></p>
    <br>

    <a id="node-2336"></a>
    <p align="center"><kbd><img src="assets/436b529dd19a7b2b7b7af303d8a2867b9c4abd07.png" width="100%"></kbd></p>
    <br>

    <a id="node-2337"></a>
    <p align="center"><kbd><img src="assets/4ca0e0ec74df816e86ac3e0462dce2743ff2ade3.png" width="100%"></kbd></p>
    <br>

    <a id="node-2338"></a>
    <p align="center"><kbd><img src="assets/9a3541b200ecaaab1212f547628a8dc07a007f08.png" width="100%"></kbd></p>
    <br>

  <a id="node-2339"></a>
  - in the predict() function above, why don't we use the max probability to get the next character?  ChatGPT  In the predict() function, the max probability is not used directly to select the next character because the goal is to introduce randomness and diversity in the generated text. By using Gumbel sampling instead of directly choosing the maximum probability, the generated text becomes less deterministic and more varied.  If the maximum probability were always chosen, the generated text would be more predictable and repetitive. The Gumbel sampling process adds randomness by considering the probabilities along with the Gumbel noise, controlled by the temperature parameter. This randomness allows the model to explore different possibilities and generate more diverse text.  In essence, Gumbel sampling with the temperature parameter provides a way to balance between exploration and exploitation. Higher temperatures result in more exploration and randomness, while lower temperatures make the sampling process more focused on exploiting the highest probabilities.  By using Gumbel sampling instead of relying solely on the maximum probability, the generated text becomes more interesting and less predictable, capturing a broader range of possibilities and allowing for more creative outputs.
    <br>

    <a id="node-2340"></a>
    - is is  the similar 'random sampling with distribution" technique?  ChatGPT  Yes, Gumbel sampling with temperature can be considered a form of random sampling with a specific distribution. In this case, the Gumbel distribution is used as the underlying distribution for sampling. Random sampling with distribution involves drawing samples from a given probability distribution. In the case of Gumbel sampling, the goal is to sample from a categorical distribution. The Gumbel distribution is utilized to introduce randomness and exploration in the sampling process. The Gumbel distribution is often used to model extreme values and is defined by its shape and location parameters. By transforming uniform random numbers through the Gumbel distribution, Gumbel sampling allows us to select a category or item from a categorical distribution in a probabilistic manner. The temperature parameter in Gumbel sampling controls the level of randomness in the sampling process. Higher temperatures lead to more diverse and random samples, while lower temperatures make the sampling process more focused and deterministic. Therefore, Gumbel sampling with temperature can be seen as a form of random sampling with the Gumbel distribution, where the temperature parameter determines the level of exploration and randomness in the generated samples.
      <br>

<a id="node-2341"></a>
- Summary
  <br>

  <a id="node-2342"></a>
  - **On statistical methods** Using a **statistical method** like the one you implemented in **course 2** will **not give you  results that are as good.** Your model will **not be able to encode information seen  previously in the data set** and as a result, the **perplexity will increase**. Remember from  course 2 that the**higher the perplexity, the worse your model** is. Furthermore, **statistical  ngram models** take up t**oo much space and memory**. As a result, it will be **inefficient** and  too **slow**. Conversely, with **deepnets, you can get a better perplexity**. Note, l**earning about  n-gram language models is still important** and allows you to better understand deepnets.
    > [!NOTE]
    > Đại khái là những**statistical method như N-gram ở course 2** **không đạt kết quả
    > tốt**được như này. Vì nó **không nắm bắt và "nhớ" được thông tin mà nó gặp ở
    > trước đó**, dẫn tới **perplexity cao**, đồng nghĩa **model tệ**. Ngoài ra nó còn **đòi hỏi
    > nhiều memory** nên **không hiệu quả** và chạy **chậm**. Còn với **Deep Net**, những
    > **vấn đề này được cải thiện đáng kể**. Tuy vậy ổng nói **việc hiểu về các statistical
    > model** đóng vai trò **quan trọng** trong việc **giúp ta hiểu hơn về Deepnet**

    <br>

