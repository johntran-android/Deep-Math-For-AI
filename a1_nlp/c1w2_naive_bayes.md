# C1W2 - NAIVE BAYES  Learn the theory behind Bayes' rule for conditional probabilities, then apply it  toward building a Naive Bayes tweet classifier of your own!  \\*Learning Objectives \\*  • Error analysis  • Naive Bayes inference  • Log likelihood  • Laplacian smoothing  • conditional probabilities  • Bayes rule  • Sentiment analysis  • Vocabulary creation  • Supervised learning

📊 **Progress:** `56` Notes | `119` Screenshots

---

Learn the theory behind Bayes' rule for conditional probabilities, then apply it toward building a Naive Bayes tweet classifier of your own!
**Learning Objectives**
 • Error analysis
 • Naive Bayes inference
 • Log likelihood
 • Laplacian smoothing
 • conditional probabilities
 • Bayes rule
 • Sentiment analysis
 • Vocabulary creation
 • Supervised learning

<a id="node-182"></a>
## Probability & Bayes's Rule

<br>

<a id="node-183"></a>

<p align="center"><kbd><img src="assets/e518b89ef736592dba4ad6177ed32fabbd0bca11.png" width="100%"></kbd></p>

<br>

<a id="node-184"></a>

<p align="center"><kbd><img src="assets/27aebe7cb9a294cebfd887a4b429deed7addf2cb.png" width="100%"></kbd></p>

> [!NOTE]
> Đại ý là trong corpus các tweets được label positive hay negative.
> Và trong số đó từ happy xuất hiện trong các tweet của cả 2 class

<br>

<a id="node-185"></a>

<p align="center"><kbd><img src="assets/8f67086b03e68f2cab63f0a3fba698ced02483df.png" width="100%"></kbd></p>

> [!NOTE]
> Cho A là sự kiện: "1 tweet là positive", thì Probability của A sẽ là tổng số
> sự kiện mà có A xuất hiện (13) chia tổng số sự kiện (20)
>
> Và Probability mà A ko xuất hiện sẽ là 1 - P(A) với điều kiện là
> tất cả event (tweet) đều được label là Pos hay Neg nhưng không
> được cả hai

<br>

<a id="node-186"></a>

<p align="center"><kbd><img src="assets/c93556c3925b7a6ee6db157e3a30e138133c5d0e.png" width="100%"></kbd></p>

> [!NOTE]
> Tương tự, cho sự kiện B là '1 tweet có chứa từ 'happy' thì Probability
> của B là số lần B xuất hiện (tổng các tweet chứa từ này) = 4, chia cho
> tổng số sự kiện (tổng số tweet = 20)

<br>

<a id="node-187"></a>

<p align="center"><kbd><img src="assets/80905082dfc58f7f18197e06f7b2d1c796950452.png" width="100%"></kbd></p>

> [!NOTE]
> Và Probability của cả A và B cùng
> xảy ra (intersection) sẽ kí hiệu như vầy

<br>


<a id="node-188"></a>
## Bayes's Rule

<br>

<a id="node-189"></a>

<p align="center"><kbd><img src="assets/40e4d69f8c45dfda6bfb1e6162af46dc27956e18.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là nói về khái niệm tính xác xuất (probability / likelihood) xảy ra
> A. nếu đã xảy ra B (P(A, given B)) thì ta tính **tỉ số các event có A (tweet
> là positive) = 3 \_trong các event có B\_ (tweet có chữ 'happy') = 4 = 75%**ta nói **"xác suất 1 tweet có chữ happy là một positive tweet là 75%"**

<br>

<a id="node-190"></a>

<p align="center"><kbd><img src="assets/93102b1a96eee7f8fb5a3bbd12885579f9560ead.png" width="100%"></kbd></p>

> [!NOTE]
> Tương tự, P(B, given A) là: \_**trong các event A**\_ (số Positive tweet)  =
> 13 thì **có bao nhiêu tweet mang chữ 'happy' event B** = 3.
>
> Ta nói xác suất một tweet positive có chữ happy chỉ là 23,1%

<br>

<a id="node-191"></a>

<p align="center"><kbd><img src="assets/ca3c89cec9bed604454e0486f8eadc53a767e449.png" width="100%"></kbd></p>

> [!NOTE]
> 2 cách 'nói':
> - Khả năng xảy ra B nếu A đã xảy ra
>
> - Trong các sự kiện A, có bao nhiêu cơ hội cũng xảy ra B

<br>

<a id="node-192"></a>

<p align="center"><kbd><img src="assets/7384739aee5f77c4b6f455ec58bc3a5ac0dd66c8.png" width="100%"></kbd></p>

> [!NOTE]
> Công thức khái quát
> hoá như sau: 
>
> Trong các **sự kiện/khả năng** xảy ra 'happy' = **P(happy)** thì: 
>
> có bao nhiêu **sự kiện/khả năng** vừa có happy vừa có 
> positive = **P(happy giao với positive)**

<br>

<a id="node-193"></a>

<p align="center"><kbd><img src="assets/989654c6eb7ce374e26bbcba3ceba19528281a54.png" width="100%"></kbd></p>

<br>

<a id="node-194"></a>

<p align="center"><kbd><img src="assets/7016b8fb0d07d940831a1ee24576b4f08d8dec57.png" width="100%"></kbd></p>

<br>

<a id="node-195"></a>

<p align="center"><kbd><img src="assets/840433fdfee9f1e7bb5b4b17387b37b9ef51614c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/840433fdfee9f1e7bb5b4b17387b37b9ef51614c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0cea5f5e84025af3859585ab432bdd75a16f4e84.png" width="100%"></kbd></p>

<br>

<a id="node-196"></a>

<p align="center"><kbd><img src="assets/0ec8ca022a5bcb83052fa7f9628cc9e1b9aba790.png" width="100%"></kbd></p>

> [!NOTE]
> Đại ý là chỉ cần nhớ Bayes rule được
> hình thành từ khái niệm Conditional
> probabilities và công thức

<br>

<a id="node-197"></a>

<p align="center"><kbd><img src="assets/639c8bb13cc456557e0fcd448fb678de2ffffe3f.png" width="100%"></kbd></p>

<br>


<a id="node-198"></a>
## Naive Bayes Introduction

<br>


<a id="node-199"></a>
### 1 Introduction to Naive Bayes as a method for text classification

> [!NOTE]
> 1 Introduction to Naive Bayes as a method for text classification
>
> 2 The Naive Bayes method is a simple and fast baseline for many text classification
> tasks
>
> 3 The Naive Bayes method makes the assumption that all features used for classification
> are independent
>
> 4 The first step in Naive Bayes is to extract the vocabulary and the word counts from the
> positive and negative corpora
>
> 5 The conditional probabilities of each word given the class are computed by dividing the
> frequency of each word in a class by its corresponding sum of words in the class
>
> 6 A table of conditional probabilities is created, which has the property that the sum of
> probabilities for each class is 1
>
> 7 Some words have a significant difference between probabilities, carrying more weight
> in determining tweet sentiments
>
> 8 The probability function is smoothed to avoid a situation where a word appears in only
> one corpus
>
> 9 The Naive Bayes inference condition rule for binary classification is introduced
>
> 10 The product of probabilities for each word in the tweet is calculated, and a conclusion
> is drawn regarding the sentiment of the tweet
>
> 11 Issues with the implementation are discussed, and the simplification of calculations is
> promised for the next video.

<br>

  <a id="node-200"></a>
  <p align="center"><kbd><img src="assets/7a81c40e68f2e28e6fa306151ea0106d1cd70182.png" width="100%"></kbd></p>
  > Có tên Naive là vì nó ngây thơ giả định rằng các features independent nhau
  > nhưng thự tế không phải vậy nhưng vẫn khá tốt trong việc tạo 1 model đơn
  > giản cho việc sentiment recognition
  >
  > Đại khái là có 2 corpus pos và neg sentence, ta extract tất cả các từ ra
  > thành 1 vocab list, rồi đếm số lần mỗi từ xuất hiện trong pos corpus và neg
  > corpus rồi tổng lại pos bao nhiêu neg bao nhiêu

  <br>

  <a id="node-201"></a>
  <p align="center"><kbd><img src="assets/09e923f96f842fbf0261bb99942d6e37f50aa8ac.png" width="100%"></kbd></p>
  <p align="center"><kbd><img src="assets/09e923f96f842fbf0261bb99942d6e37f50aa8ac.png" width="100%"></kbd></p>
  <p align="center"><kbd><img src="assets/ec801f1c645efbdb90971ab3617e8848d276fa6b.png" width="100%"></kbd></p>
  > Tính P(word,Pos) và P(word, Neg) của
  > từng từ để tạo 1 table mới

  <br>

  <a id="node-202"></a>
  <p align="center"><kbd><img src="assets/07834317242a6fd6d4f18a24f88bfd43924fefac.png" width="100%"></kbd></p>
  > Dễ hiểu được tính chất tổng các
  > cột đều bằng 1

  <br>

  <a id="node-203"></a>
  <p align="center"><kbd><img src="assets/744d94658206cec29f82c0479a54aae74e528235.png" width="100%"></kbd></p>
  🔗 **Related:** [1 Counting word \\*occurrence\\* for probability calculation  2 \\*Problem with probability of zero\\* for \\*unseen word\\* pairs  3 Introduction to \\*smoothing\\*  4 \\*Laplacian smoothing\\* technique to \\*avoid zero probabilities\\*  5 Formula for Laplacian smoothing  6 Calculation of probability using Laplacian smoothing  7 Importance of Laplacian smoothing  8 Introduction to log likelihood in next video.](laplacian_smoothing.md#node-212)

  > Những từ như I, am có P_pos và neg bằng nhau và ko giúp ích gì trong
  > sentiment recognition nhưng happy hay sad có 2 chỉ số này chênh lệch ->
  > Nó là những power word sẽ có sức nặng để quyết định kết quả của
  > sentiment analysis của câu

  > Còn những từ như because ko xuất hiện trong 1 cột (neg) thì ta sẽ smooth
  > cái probability function để giúp P pos hay neg không bằng 0 (để công thức
  > Naive Bayes không bị lỗi do chia 0)

  <br>

  <a id="node-204"></a>
  <p align="center"><kbd><img src="assets/21c0efe461b7251a277015c972e2d8a2c18a69db.png" width="100%"></kbd></p>
  > Phương pháp: Tính product của các tỉ số P_pos và P_neg của các từ trong
  > câu, ví dụ câu này ra 1.4 -> Khả năng câu này là positive sentiment

  <br>

  <a id="node-205"></a>
  <p align="center"><kbd><img src="assets/cc824fcf1be16bcbf529cdeb1a7089d227564020.png" width="100%"></kbd></p>
  <br>


<a id="node-206"></a>
## Laplacian Smoothing

<br>


<a id="node-207"></a>
### 1 Counting word \\*occurrence\\* for probability calculation

> [!NOTE]
> 1 Counting word \**occurrence\** for probability calculation
>  2 \**Problem with probability of zero\** for \**unseen word\** pairs
>  3 Introduction to \**smoothing\**
>  4 \**Laplacian smoothing\** technique to \**avoid zero probabilities\**
>  5 Formula for Laplacian smoothing
>  6 Calculation of probability using Laplacian smoothing
>  7 Importance of Laplacian smoothing
>  8 Introduction to log likelihood in next video.

<br>

  <a id="node-208"></a>
  <p align="center"><kbd><img src="assets/5ac697cbbe950ab84b869d820e3526b3b279b640.png" width="100%"></kbd></p>
  > "So now all the probabilities in each column will sum to one. This process is
  > called Laplacian in smoothing."
  >
  > Mình hiểu là cộng 1 trên tử để cho P không bằng 0 dù cho từ ko xuất hiện
  > trong cột neg/pos (freq (w|pos) hay freg(w|neg = 0) thì cộng thêm V (số
  > unique word) ở dưới để tổng các P theo công thức mới (Laplacian
  > smoothing) vẫn = 1
  >
  > Nếu có bối rối:
  >
  > freq(w1|Pos) +freq(w2|Pos)... = 3 + 3 + 2 +. ..= N_pos = 13
  >
  > V là số unique words = 8

  <br>

  <a id="node-209"></a>
  <p align="center"><kbd><img src="assets/d559b54fa691fb55f3bd1b83c71e3e7ebdaa54fa.png" width="100%"></kbd></p>
  <br>

  <a id="node-210"></a>
  <p align="center"><kbd><img src="assets/53772260aea11b29e11e3d2abdf111e6cd4dd2d6.png" width="100%"></kbd></p>
  <p align="center"><kbd><img src="assets/53772260aea11b29e11e3d2abdf111e6cd4dd2d6.png" width="100%"></kbd></p>
  <p align="center"><kbd><img src="assets/7d4cd72407fb8dc67ac9b268c124a25a05880411.png" width="100%"></kbd></p>
  > Tính lại Probability table với
  > Laplacian smoothing

  <br>

  <a id="node-211"></a>
  <p align="center"><kbd><img src="assets/61582d4c01e0afbebcd941c289df3b40948145d4.png" width="100%"></kbd></p>
  <br>

  <a id="node-212"></a>
  <p align="center"><kbd><img src="assets/11be03bf04d11ec6a0b257aba25df3f83bb6975a.png" width="100%"></kbd></p>
  🔗 **Related:** [1 Introduction to Naive Bayes as a method for text classification  2 The Naive Bayes method is a simple and fast baseline for many text classification tasks  3 The Naive Bayes method makes the assumption that all features used for classification are independent  4 The first step in Naive Bayes is to extract the vocabulary and the word counts from the positive and negative corpora  5 The conditional probabilities of each word given the class are computed by dividing the frequency of each word in a class by its corresponding sum of words in the class  6 A table of conditional probabilities is created, which has the property that the sum of probabilities for each class is 1  7 Some words have a significant difference between probabilities, carrying more weight in determining tweet sentiments  8 The probability function is smoothed to avoid a situation where a word appears in only one corpus  9 The Naive Bayes inference condition rule for binary classification is introduced  10 The product of probabilities for each word in the tweet is calculated, and a conclusion is drawn regarding the sentiment of the tweet  11 Issues with the implementation are discussed, and the simplification of calculations is promised for the next video.](naive_bayes_introduction.md#node-203)

  > Với Laplacian Smoothing, P ('because', neg
  > class) không còn bằng 0 nữa

  <br>

  <a id="node-213"></a>
  <p align="center"><kbd><img src="assets/f86d60eb41abfd77092e35dc24b2432f9f7d85fa.png" width="100%"></kbd></p>
  > Mục đích là để P ko bằng 0 như trường hợp từ because ở trên có
  > P(' Because'. Neg class) = 0 để khi tính công thức Naive Bayes
  > không bị lỗi chia 0

  <br>

  <a id="node-214"></a>
  <p align="center"><kbd><img src="assets/4c7ad2789c1c8d661069927f4f517835dcd4254d.png" width="100%"></kbd></p>
  <br>


<a id="node-215"></a>
## Log Likelihood P1

<br>


<a id="node-216"></a>
### 1 The video introduces the concept of\\* log likelihood\\*s, which

> [!NOTE]
> 1 The video introduces the concept of\**log likelihood\**s, which
> are l\**ogarithms of the probabilities\** used in sentiment
> classification.
>
> 2 Words are classified as \**neutral\**, \**positive\**, or \**negative\** using
> \**conditional probabilities\**, and their \**ratios\** are used for
> classification.
>
> 3 The \**ratios\** for each word are essential for \**Naive Bayes'
> binary classification\**, and a mathematical \**trick\** using
> \**logarithms\** can be used to \**prevent numerical underflow.\**
>
> 4 \**Lambda\** is introduced as the \**log of the ratio of the
> probability that a word is positive\** \**over the probability that it
> is negative\**, and it can be used to calculate the log score for
> sentiment classification.
>
> 5 The video emphasizes the \**importance\** of the \**prior ratio\** in
> \**unbalanced data-sets\** and how it affects the Naive Bayes'
> formula for binary classification.

<br>

  <a id="node-217"></a>
  <p align="center"><kbd><img src="assets/967c5a06d1b46119c82adaddb29e27681fc3923e.png" width="100%"></kbd></p>
  > Đại khái là tính thêm cột **ratios** và dùng nó để tính 'tính positive,
  > negative hay neutral' của từ. Càng **cao thì càng positive**, càng **gần 0 thì
  > càng negative**

  <br>

  <a id="node-218"></a>
  <p align="center"><kbd><img src="assets/237977c56a7ec8d23ed91b35cac3b9729ecad7f6.png" width="100%"></kbd></p>
  > Đại khái là **Full Naive Bayes** sẽ có thêm 'prior' ratios (P(pos)/P(neg))
  > sẽ tính tới sự không cân bằng của dataset, cho tới giờ do Pos
  > sentences = Neg sentences nên tỉ số này bằng 1.
  >
  > Nói chung là Naive Bayes là 1 algorithm **đơn giản và nhanh** để tạo
  > baseline (kiểu như 1 chuẩn/một model prototype để đánh giá)

  <br>

  <a id="node-219"></a>
  <p align="center"><kbd><img src="assets/f78808de0b791c0cdaca73e0ea9d35bd1d41109e.png" width="100%"></kbd></p>
  > Đại khái là do các P đều nhỏ hơn 1 nên làm việc
  > với nó dễ bị n**umberical underflow** issue - kiểu như số nó quá
  > nhỏ dẫn đến lỗi máy tính.
  >
  > Người ta dùng **log** để tính toán giúp giải quyết issue này

  <br>

  <a id="node-220"></a>
  <p align="center"><kbd><img src="assets/85bd6e650265168060f041bbf131e220590c6785.png" width="100%"></kbd></p>
  > Ví dụ với cách dùng log, thay vì ta tính**TÍCH (Product) của các
  > tỉ số** P(w|pos) / P(w|Neg) để ra số rồi xem > 1 thì suy ra Pos <
  > 1 thì suy ra Neg thì ..
  >
  > với log ta tính **TỔNG (Sum) các log của tỉ số**
  > P_pos / P_neg - gọi là lambda thì kết quả cũng như vậy

  <br>

  <a id="node-221"></a>
  <p align="center"><kbd><img src="assets/15df7f84596892ac83bdf678533993a8a8eecd14.png" width="100%"></kbd></p>
  <br>

  <a id="node-222"></a>
  <p align="center"><kbd><img src="assets/97a248ff12482d8dded2ec197946f2bc25f58082.png" width="100%"></kbd></p>
  <p align="center"><kbd><img src="assets/97a248ff12482d8dded2ec197946f2bc25f58082.png" width="100%"></kbd></p>
  <p align="center"><kbd><img src="assets/e43ac22f2af658181096874c308fd05884a9fe84.png" width="100%"></kbd></p>
  <br>


<a id="node-223"></a>
## Log Likelihood P2

<br>


<a id="node-224"></a>
### 1 Inference: Learn how to calculate the \\*log likelihood of a tweet\\*

> [!NOTE]
> 1 Inference: Learn how to calculate the \**log likelihood of a tweet\**
> based on the\**lambda dictionary\**
>
> 2 Log likelihood: \**Sum up the lambdas from each word\** in the
> tweet to calculate the l\**og likelihood\**
>
> 3 Sentiment analysis: Determine whether a\**tweet is positive or
> negative\** based on the \**log likelihood value\**
>
> 4 Power words: \**Words with positive or negative sentiment\** have
> more influence on the \**log likelihood score\**
>
> 5 Decision threshold: The \**threshold\** for the log likelihood score
> is \**0\** instead of 1
>
> 6 Training: Introduction to \**training a naive bayes model\** for
> sentiment analysis.

<br>

  <a id="node-225"></a>
  <p align="center"><kbd><img src="assets/760a25373025017e2dd76fce990ca1d9db613719.png" width="100%"></kbd></p>
  > Log likelihood  của 1 tweets là
  > tổng các lambda của các từ trong tweet

  <br>

  <a id="node-226"></a>
  <p align="center"><kbd><img src="assets/c68e1bfea9de5c33426e4cae117141cc419c910b.png" width="100%"></kbd></p>
  > Với Log (likelihood) range sẽ là (-infi infi) và decision
  > threshold là 0 không phải (0-infi) với threshold 1 nữa

  <br>

  <a id="node-227"></a>
  <p align="center"><kbd><img src="assets/7376106269da365b005392d62600b5422f40f78d.png" width="100%"></kbd></p>
  > Log likelihood của tweet dương thì
  > positive, âm thì negative

  <br>

  <a id="node-228"></a>
  <p align="center"><kbd><img src="assets/0040985442a9aced774d7d329cad66e348b9eae4.png" width="100%"></kbd></p>
  <br>


<a id="node-229"></a>
## Training Naive Bayes

<br>


<a id="node-230"></a>
### 1 Naive Bayes classifier is trained differently from logistic regression or

> [!NOTE]
> 1 Naive Bayes classifier is trained differently from logistic regression or
> deep learning.
>
> 2 The first step in any supervised machine learning project is to \**gather\** and
> \**preprocess\** data.
>
> 3 Preprocessing involves \**lowercase\** texts, \**removing\** \**punctuation\**, \**URLs\**,
> handles,\**stop words\**, \**stemming\**, and \**tokenizing\**.
>
> 4 The next step is to \**compute the vocabulary\** for each word in each class
> to produce a table of \**frequencies\** and \**conditional probabilities\**.
>
> 5 The \**Lambda\** score for each word is estimated using the \**log of the ratio\**
> of conditional probabilities.
>
> 6 The\**log prior\** is estimated by counting the number of positive and
> negative tweets and computing the log of the ratio.
>
> 7 \**Training a Naive Bayes\** model can be divided into \**six logical steps.\**
>
> 8 The final step is to \**classify sentences\** using the\**probability table \**built in
> the previous steps.

<br>

  <a id="node-231"></a>
  <p align="center"><kbd><img src="assets/32a4a5bc3e89077a44490a5a52f683d831c466d1.png" width="100%"></kbd></p>
  > Bước 0 là chuẩn bị data và bước 1 Preprocess data
  >
  > Trong thực tế bước preprocess có thể chiếm nhiều thời gian
  > hơn là trong assignment này

  <br>

  <a id="node-232"></a>
  <p align="center"><kbd><img src="assets/1275c1790c06ffeb0a096c5ae9f1c0ce84396895.png" width="100%"></kbd></p>
  > Bước 2 là đếm số lần 1 từ xuất hiện trong pos corpus và neg corpus

  <br>

  <a id="node-233"></a>
  <p align="center"><kbd><img src="assets/ece670043173430d920cfe1dc85330db7d0ee6aa.png" width="100%"></kbd></p>
  > Step 3 và 4 là tính **Conditional Probability**P(w,Pos) và
  > P(w, Neg) của mỗi từ và lambda (log của ratios Ppos/Pneg)

  <br>

  <a id="node-234"></a>
  <p align="center"><kbd><img src="assets/73944e669bc098a9ebe25bb789d91f86b283530b.png" width="100%"></kbd></p>
  > Kế là tính log prior vốn trong assignment này do
  > balanced nên = 0 nhưng trong unbalanced dataset
  > thì chỉ số này có thể quan trọng

  <br>

  <a id="node-235"></a>
  <p align="center"><kbd><img src="assets/5eda0cd3c188d5a033aeb0289a8c7ea28ed2708f.png" width="100%"></kbd></p>
  <br>


<a id="node-236"></a>
## Lab: Visualizing Likelihoods And Confidence

<br>


<a id="node-237"></a>
### In this lab, we will cover an \\*essential part of data analysis\\* that has not

> [!NOTE]
> In this lab, we will cover an \**essential part of data analysis\** that has not
> been included in the lecture videos. As we stated in the previous module,
> \**data visualization\** gives \**insight\** into the \**expected performance\** of
> any model.
>
> In the following exercise, you are going to make a \**visual inspection\** of
> the tweets dataset using the \**Naïve Bayes features\**. We will see how we
> can understand the \**log-likelihood ratio\** explained in the videos as a pair
> of numerical features that can be fed in a machine learning algorithm.
>
> At the end of this lab, we will introduce the concept of \**confidence ellipse\**
> as a tool for representing the \**Naïve Bayes\** model visually.

<br>

<a id="node-238"></a>
- Import
  <br>

    <a id="node-239"></a>
    <p align="center"><kbd><img src="assets/d5b754c2c4cd227673dbab0b83248ed47105305c.png" width="100%"></kbd></p>
    <br>

<a id="node-240"></a>
- Calculate the likelihoods for each tweet
  <br>

    <a id="node-241"></a>
    <p align="center"><kbd><img src="assets/eb6dd3415fb10225f9a98bd97fa2eb065d8d92bc.png" width="100%"></kbd></p>
    > Log likelihood của một từ w là log của
    > ratios P(w, pos) và P(w, neg)
    >
    > Thì ở đây định nghĩa thêm Log likelihood của 1 câu tweet là 
    > log của ratios giữa P(tweet, pos) và P(tweet, neg)
    >
    > P(tweet, pos) là tích các P(word, pos) trong câu
    > tương tự P(tweet, neg) cũng là tích các P(w, neg) trong câu
    >
    > Nên ta có Log (P(tweet, pos)/P(tweet, neg)) 
    >
    > = log(P(tweet, pos)) - log(P(tweet, neg)) 
    > (do Log(a/b) = log(a)-log(b)
    >
    > = log[P(w1, pos)*P(w2, pos) ...P(wn, pos)] - log[P(w1, neg)*P(w2, neg) ...P(wn, neg)]
    >
    > = [ log(P(w1, pos) + log(P(w2, pos) + ...log(P(wn, pos) ]
    > - [ log(P(w1, neg) + log(P(w2, neg) + ...log(P(wn, neg) ]

    <br>

    <a id="node-242"></a>
    <p align="center"><kbd><img src="assets/a61ba5da71fff170ebc0b23e0eb0afe53dbca6e7.png" width="100%"></kbd></p>
    <br>

    <a id="node-243"></a>
    <p align="center"><kbd><img src="assets/f1320758e86c2ac3602c885211b0bfb4df115961.png" width="100%"></kbd></p>
    <br>

<a id="node-244"></a>
- Using Confidence Ellipses to interpret Naïve Bayes
  <br>

    <a id="node-245"></a>
    <p align="center"><kbd><img src="assets/049f4f645f39dd85c5c40a5eaf843ce62cd79b1f.png" width="100%"></kbd></p>
    > Chưa hiểu lắm như đại khái là vẽ cái phân bố (distribution) của
    > data theo Confidence Ellipses sẽ giúp có cái nhìn tốt hơn là chỉ
    > vẽ khơi khơi (Cartesian plane). Tốt hơn ở đây chắc là thể hiện
    > thêm các cấp phân bố standard deviation mấy cái đường
    > ellipse chấm chấm

    <br>

    <a id="node-246"></a>
    <p align="center"><kbd><img src="assets/743478402ced6914196a8580fa5f7b4daf3ea2f6.png" width="100%"></kbd></p>
    <br>

    <a id="node-247"></a>
    <p align="center"><kbd><img src="assets/34501ee7f9672b925006cd29018eeb57642754a2.png" width="100%"></kbd></p>
    <br>

    <a id="node-248"></a>
    <p align="center"><kbd><img src="assets/a827cd37120e0aeb17d49aa3f345989645212327.png" width="100%"></kbd></p>
    <br>

    <a id="node-249"></a>
    <p align="center"><kbd><img src="assets/ba82807fb78f7f1a46251d496b408dec3fe773a9.png" width="100%"></kbd></p>
    <br>

    <a id="node-250"></a>
    <p align="center"><kbd><img src="assets/60c755556843921ba681261a57533959f59a3bb7.png" width="100%"></kbd></p>
    <br>


<a id="node-251"></a>
## Testing Naive Bayes

<br>


<a id="node-252"></a>
### 1 The main task is to apply the Naive Bayes classifier on \\*real test examples.\\*

> [!NOTE]
> 1 The main task is to apply the Naive Bayes classifier on \**real test examples.\**
>
> 2 The \**conditional probabilities\** are used to predict the sentiment of new unseen tweets.
>
> 3 The \**model performance\** is evaluated using a\**test set\** of annotated tweets.
>
> 4\**Pre-processing of text\** is necessary before applying the model to predict sentiments.
>
> 5 The model can only give a score for words \**it's seen before.\**
>
> 6 The \**score obtained\** from the model can be used to predict whether a tweet has
> positive or negative sentiment.
>
> 7 \**Validation set\** is used to measure the performance of the trained model.
>
> 8 The \**accuracy function\** is implemented to \**measure the performance of the model\**.
>
> 9 The score of each entry in the validation set is computed and evaluated to get a vector of
> zeros and ones indicating whether the predicted sentiment is negative or positive,
> respectively.
>
> 10 The \**accuracy of the model \**is computed by \**comparing the predicted labels\** with
> the\**true labels \**provided in the validation set.
>
> 11 The words that don't appear in the Lambda table are treated as \**neutral words.\**
>
> 12 The Naive Bayes method is applied to classify tweets in the coding exercise at the end
> of the week.

<br>

  <a id="node-253"></a>
  <p align="center"><kbd><img src="assets/6b3226c6c56b059c0f545490bc42e16b96ed0b7e.png" width="100%"></kbd></p>
  <br>

  <a id="node-254"></a>
  <p align="center"><kbd><img src="assets/80e8a6b06b45b3e318473ad0f609e39ede4430b9.png" width="100%"></kbd></p>
  <br>

  <a id="node-255"></a>
  <p align="center"><kbd><img src="assets/201a6f8b2bc653edb5d4b15cd9363878b6ce3da1.png" width="100%"></kbd></p>
  > Nhớ rằng cái model này không có params gì hết, cơ bản chỉ là đếm, nên predict
  > 1 tweet mới ta sẽ preprocess nó thành vector các từ, rồi tính tổng các lambda
  > của các từ đó, từ nào ko có trong table thì thôi, rồi cộng với log prior ra kết quả
  > so với 0 để kết luận

  <br>

  <a id="node-256"></a>
  <p align="center"><kbd><img src="assets/4a6f0445961dd928196746a00b679db9966b943c.png" width="100%"></kbd></p>
  > Evaluate đv CV set.

  <br>

  <a id="node-257"></a>
  <p align="center"><kbd><img src="assets/f01a3c893de819c9247cb34f7511f1b16257e8ff.png" width="100%"></kbd></p>
  <br>

  <a id="node-258"></a>
  <p align="center"><kbd><img src="assets/efd038559b727dd27d6fbc3624bb3dabd4c4c4b5.png" width="100%"></kbd></p>
  <br>


<a id="node-259"></a>
## Application Of Naive Bayes

<br>


<a id="node-260"></a>
### 1 Naive Bayes method can be used for v\\*arious classification tasks\\*, such as \\*sentiment

> [!NOTE]
> 1 Naive Bayes method can be used for v\**arious classification tasks\**, such as \**sentiment
> analysis\**, \**author identification, spam filtering, information retrieval, and word
> disambiguation.
> \**
> 2 The \**Naive Bayes formula\** calculates the \**ratio between\** the \**conditional probabilities of the
> priors\** and \**likelihoods to estimate the probability for each class\**.
>
> 3 Naive Bayes can be used for \**author identification\** by training a model to recognize
> whether a new document was written by one author or another, based on their \**unique
> writing style.\**
>
> 4 \**Spam filtering\** can be performed using Naive Bayes by \**analyzing the sender, subject,
> and content\** of an email to determine whether it is spam or not.
>
> 5 \**Information retrieval\** can be done using Naive Bayes by calculating the \**likelihood\** of
> \**documents given a query\** and storing them based on their likelihoods.
>
> 6 Naive Bayes can be used for \**word disambiguation\** by \**calculating the score of the
> documents given that a word refers to each possible meaning\**, and choosing the one with
> the highest score.
>
> 7 Naive Bayes is a \**popular method\** due to its \**simplicity\** in training, use, and interpretation.
>
> 8 The assumptions underlying the Naive Bayes method will be discussed in the upcoming
> videos.

<br>

  <a id="node-261"></a>
  <p align="center"><kbd><img src="assets/7b1eb21efb9c9de677bb18f6c8fe05aee3f15ed3.png" width="100%"></kbd></p>
  <br>

  <a id="node-262"></a>
  <p align="center"><kbd><img src="assets/9d4ff7d1dbce35d572e81cb0ee25e856c8685f3d.png" width="100%"></kbd></p>
  <br>

  <a id="node-263"></a>
  <p align="center"><kbd><img src="assets/d7af8f12553f63e4cdb56aec47616148f6b15cb1.png" width="100%"></kbd></p>
  > Chưa hiểu lắm

  <br>

  <a id="node-264"></a>
  <p align="center"><kbd><img src="assets/da926f6b0776b3f4c0ce7f964c07341ac69a2fd6.png" width="100%"></kbd></p>
  <br>

  <a id="node-265"></a>
  <p align="center"><kbd><img src="assets/aba56daec3736af8cd7a6a250db3d1668f63a8d4.png" width="100%"></kbd></p>
  <br>

  <a id="node-266"></a>
  <p align="center"><kbd><img src="assets/aca703c918d48886a1fad30e96bf867a1d270065.png" width="100%"></kbd></p>
  > Note: Bayes Rule thường dùng
  > như 1 simple baseline

  <br>


<a id="node-267"></a>
## Naive Bayes Assumptions

<br>


<a id="node-268"></a>
### 1 The main \\*assumption\\* underlying the naïve bayes method is \\*independence\\*

> [!NOTE]
> 1 The main \**assumption\** underlying the naïve bayes method is \**independence\**
> of \**words in a sentence.\**
>
> 2 Naïve bayes is a \**simple\** model that \**doesn't require setting custom
> parameter\**s.
>
> 3 Naïve bayes assumes \**independence\** between the predictors or \**features\**
> associated with each class, which may \**not always be the case.\**
>
> 4 Naïve bayes could l\**ead to under or overestimation\** of the \**conditional
> probabilities of individual words. \** 5 Naïve bayes \**relies on the distribution of the
> training data sets\**, which could result in an \**overly optimistic or pessimistic
> model\**.
>
> 6 The assumption of\**independence in naïve bayes is difficult to guarantee\**, but
> the model \**works well in certain situations.\**
>
> 7 The relative frequency of positive and negative tweets in training data sets needs
> to be balanced for accurate results.
>
> 8 If naïve bayes fails to perform well, there are solutions to improve its
> performance, which will be covered in the next video.

<br>

  <a id="node-269"></a>
  <p align="center"><kbd><img src="assets/db1d9cfb37dfb09b660bfbf7f70c601460ed9a4a.png" width="100%"></kbd></p>
  <br>

  <a id="node-270"></a>
  <p align="center"><kbd><img src="assets/26a1f76debf5824ae7f7541c43cc47eb5a2ab57d.png" width="100%"></kbd></p>
  > Đại khái là Naive Bayes assume các từ độc lập với nhau và rõ ràng là
  > không đúng (ví dụ 'hot' và 'sunny' có quan hệ rõ ràng với 'desert', do đó
  > nó không nắm bắt được các liên hệ giữa các Từ. Các course sau sẽ nói
  > đến các model làm tốt hơn việc này (RNN, Transformer).

  <br>

  <a id="node-271"></a>
  <p align="center"><kbd><img src="assets/9ceab8f145a0b457c8297769ce80f955449765ed.png" width="100%"></kbd></p>
  > Dẫn đến trong vấn đề dưới nó sẽ tính ra P
  > của các chữ đều bằng nhau.

  <br>

  <a id="node-272"></a>
  <p align="center"><kbd><img src="assets/cd03aaf06ba932c108f6056be863fe1ba1cda4a4.png" width="100%"></kbd></p>
  > Cái thứ hai đại khái là nó **phụ thuộc vào data distribution của dataset
  > mà vốn các bộ data này thường được cleaned và artificially balanced**như tweet dataset trong khi đó thường trong thực tế sẽ nhiều positive
  > tweet hơn do cái negative bị banned hoặc user muted (???) negative
  > tweet. Đại khái là do đó Naive Bayes ko thể phản ánh đúng thực tế như
  > thế nào và dẫn đến model bị **overconfidence** hay **overpessimistic**

  <br>

  <a id="node-273"></a>
  <p align="center"><kbd><img src="assets/254c937517b0e755e0c9541e62c432d2579ee5b0.png" width="100%"></kbd></p>
  > Dù vậy nó vẫn tốt trong
  > một số trường hợp

  <br>


<a id="node-274"></a>
## Error Analysis

<br>


<a id="node-275"></a>
### 1 \\*NLP errors\\* are \\*inevitable\\* no matter what method you use

> [!NOTE]
> 1 \**NLP errors\** are \**inevitable\** no matter what method you use
>
> 2 Errors in NLP can be caused by \**loss of semantic meaning\**, \**word\**
> \**order\**, and \**language quirks\** that are \**difficult for machines\** to understand
>
> 3 It's important to \**analyze processed text\** to ensure accurate results,
> including \**checking for punctuation and word removal\**
>
> 4 \**Naïve base classification\** relies on word \**frequency\** \**counts\** and can
> lead to \**errors due to its independence assumption\**
>
> 5 \**Word vectors\** can be used to improve NLP results
>
> 6 Naïve base classification may fail in cases of \**adversarial attacks,\**
> which are \**language phenomena like sarcasm, irony, and euphemism\**
> that machines have\**difficulty understanding.\**

<br>

  <a id="node-276"></a>
  <p align="center"><kbd><img src="assets/bdca8e533196c996aac95ba9f789bef862f623b1.png" width="100%"></kbd></p>
  <br>

  <a id="node-277"></a>
  <p align="center"><kbd><img src="assets/206176e5753ec78a2b44dd2ef30bc090ffe946cb.png" width="100%"></kbd></p>
  🔗 **Related:** [PREPROCESSING](preprocessing.md#node-37)

  > Đại khái là nhớ lại 1 điểm lưu ý trong Processing bữa trước khi
  > removing **Punctuation** phải cẩn thận vì đôi khi nó chứa thông tin quan
  > trọng, ví dụ bỏ cái mặt buồn ở dưới thôi là thay đổi hết ý nghĩa câu

  <br>

  <a id="node-278"></a>
  <p align="center"><kbd><img src="assets/28f2e4e21d9996002bbad882a3deac7dfe0cda13.png" width="100%"></kbd></p>
  > Tương tự với Stop Words

  <br>

  <a id="node-279"></a>
  <p align="center"><kbd><img src="assets/dda8fe5bc8a9bce5f3b9d521e2e871d8a9fd93cc.png" width="100%"></kbd></p>
  > Word order nữa, nói chung là những model sau như RNN, Attention và
  > Transformer sẽ handle dc những ca này

  <br>

  <a id="node-280"></a>
  <p align="center"><kbd><img src="assets/2a0440261c6b534a6706d76ba406012a9008fb97.png" width="100%"></kbd></p>
  > Đại khái là sao đó mà câu positive sau khi
  > preprocess thì nghe rất negative

  <br>

<a id="node-281"></a>
- An adversarial attack in the context of naïve Bayes refers to a situation where the model misclassifies a text input due to the use of language phenomena such as \\*sarcasm, irony, or euphemism.  \\*These language phenomena can be \\*easily understood by humans\\* but can be \\*challenging for machines\\* to interpret. In the given example, the text "This is a ridiculously powerful movie. The plot was gripping and I cried right through until the ending" contains \\*positive\\* language, but the \\*pre-processing step used by naïve Bayes\\* to extract features and analyze sentiment may \\*incorrectly classify it as negative\\* due to the presence of words like "\\*ridiculous\\*" or "cried."  This can \\*result in inaccurate sentiment analysis\\* and affect the overall performance of the model. To avoid such adversarial attacks, it is important to use \\*more sophisticated models\\* that can better understand the nuances of language and context. (GPT)
  > Đại khái cái sao đó chính là hiện tượng gọi là Adversarial
  > attack, model quá đơn giản như Naive Bayes ko nắm bắt
  > được sự 'lắt léo' trong ngôn ngữ khiến nó ko hiểu được ý
  > nghĩa positive của câu trên

  <br>


<a id="node-282"></a>
## Week Conclusion

<br>


<a id="node-283"></a>
## Quiz

<br>

<a id="node-284"></a>

<p align="center"><kbd><img src="assets/dccf1666f933a953c7a279338c8546b911a5a3c8.png" width="100%"></kbd></p>

<br>

<a id="node-285"></a>

<p align="center"><kbd><img src="assets/35a244169e495ddbdd96622b52c8fd0e4c735b38.png" width="100%"></kbd></p>

<br>

<a id="node-286"></a>

<p align="center"><kbd><img src="assets/fb9deed6f3b8fa2961bf78ecedbfd46577d2d49e.png" width="100%"></kbd></p>

<br>

<a id="node-287"></a>

<p align="center"><kbd><img src="assets/e09ae57f2c2614f4d8aa145b130121870d7b0201.png" width="100%"></kbd></p>

<br>

<a id="node-288"></a>

<p align="center"><kbd><img src="assets/63d2e6b0eeb453b7aab7c75a9d5df323759fe6eb.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/63d2e6b0eeb453b7aab7c75a9d5df323759fe6eb.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/169cde840dcb9fa7e7ff78a0f5458a119fb790de.png" width="100%"></kbd></p>

> [!NOTE]
> Không hiểu sao sai

<br>

<a id="node-289"></a>

<p align="center"><kbd><img src="assets/45229f46e2c1907d266abf16db7c674519a91c2d.png" width="100%"></kbd></p>

<br>

<a id="node-290"></a>

<p align="center"><kbd><img src="assets/d4f5e324ad0b2c51462ac6ee94daa5e661f32a33.png" width="100%"></kbd></p>

<br>

<a id="node-291"></a>

<p align="center"><kbd><img src="assets/3a3898618f26a59157118589ea09933a573d428a.png" width="100%"></kbd></p>

<br>

<a id="node-292"></a>

<p align="center"><kbd><img src="assets/b9e9e3996ef394f2594304f538ca34d6743f3603.png" width="100%"></kbd></p>

<br>

<a id="node-293"></a>

<p align="center"><kbd><img src="assets/fbe971082faa04f4f29fb3228ea7e56b61c3da6f.png" width="100%"></kbd></p>

<br>


<a id="node-294"></a>
## PROGRAMMING ASSIGNMENT: Naive Bayes

<br>


<a id="node-295"></a>
### Welcome to week two of this specialization. You will learn about \\*Naive

> [!NOTE]
> Welcome to week two of this specialization. You will learn about \**Naive
> Bayes\**. Concretely, you will be using Naive Bayes for \**sentiment analysis\** on
> \**tweets\**. Given a tweet, you will decide if it has a positive sentiment or a
> negative one. Specifically you will:
>
> • \**Train a naive bayes model\** on a \**sentiment analysis task\**
>
> • \**Test using your model\**
>
> • \**Compute ratios of positive words to negative words\**
>
> • Do some \**error analysis\**
>
> • Predict on your own tweet
>
> You may already be familiar with Naive Bayes and its justification in terms of
> \**conditional probabilities\** and \**independence\**.
>
> • In this week's lectures and assignments we used the \**ratio of probabilities
> between positive and negative sentiment.\**
>
> • This approach gives us simpler formulas for these 2-way classification
> tasks.

<br>

<a id="node-296"></a>
- Importing Functions and Data
  <br>

  <a id="node-297"></a>
  - from utils import process_tweet, lookup import pdb from \\*nltk.corpus\\* import \\*stopwords\\*, \\*twitter_samples\\* import numpy as np import pandas as pd import nltk import string from nltk.tokenize import \\*TweetTokenizer\\* from os import getcwd import w2_unittest  \\*nltk.download('twitter_samples') nltk.download('stopwords')\\*
    <br>

      <a id="node-298"></a>
      <p align="center"><kbd><img src="assets/7e6ed9134bc35a610b82f660be5e3bd4bf506f43.png" width="100%"></kbd></p>
      > If you are running this notebook in your local computer, don't
      > forget to download the tweeter samples and stopwords from nltk.
      >
      > nltk.download('stopwords') nltk.download('twitter_samples')

      <br>

    <a id="node-299"></a>
    - filePath = f"{getcwd()}/../tmp2/" nltk.data.path.append(filePath)  \\/# \\*get the sets of positive and negative tweets\\*\\/ all_positive_tweets = twitter_samples.strings('\\*positive_tweets.json\\*') all_negative_tweets = twitter_samples.strings('\\*negative_tweets.json\\*')  \\/# \\*split the data into two pieces\\*, one for training and one for testing (validation set) \\/test_pos = all_positive_tweets[\\*4000\\*:] train_pos = all_positive_tweets[:\\*4000\\*] test_neg = all_negative_tweets[4000:] train_neg = all_negative_tweets[:4000]  train_x = train_pos + train_neg test_x = test_pos + test_neg  \\*# avoid assumptions about the length of all_positive_tweets\\* train_y = np.append(np.ones(len(train_pos)), np.zeros(len(train_neg))) test_y = np.append(np.ones(len(test_pos)), np.zeros(len(test_neg)))
      <br>

<a id="node-300"></a>
- 1 - Process the Data
  <br>

  <a id="node-301"></a>
  - For any machine learning project, once you've gathered the data, \\*the first step is to process it \\*to make useful inputs to your model.  \\*Remove noise\\*: You will first want to remove noise from your data -- that is, \\*remove words that don't tell you much\\* about the content. These include all \\*common words like 'I, you, are, is\\*, etc...' that would not give us enough information on the sentiment.  We'll also remove \\*stock market tickers\\*, \\*retweet\\* \\*symbols\\*, \\*hyperlinks\\*, and \\*hashtags\\* because they can not tell you a lot of information on the sentiment. You also want to remove all the \\*punctuation\\* from a tweet. The reason for doing this is because we want to \\*treat words with or without the punctuation\\* as the same word, instead of treating "happy" , "happy?", " happy!", "happy," and "happy." as different words.  Finally you want to use \\*stemming\\* to only keep track of one variation of each word. In other words, we'll treat "motivation", "motivated", and " motivate" similarly by grouping them within the same stem of \\*"motiv-"\\*. We have given you the function \\/\\*process_tweet\\*\\/ that does this for you.
    <br>

    <a id="node-302"></a>
    - custom_tweet = "RT @Twitter @chapagain Hello There! Have a great day. :) #good #morning http://chapagain.com.np"  # print cleaned tweet print(process_tweet(custom_tweet)) -> ['hello', 'great', 'day', ':)', 'good', 'morn']
      <br>

  <a id="node-303"></a>
  - 1.1 - Implementing your Helper Functions
    <br>

    <a id="node-304"></a>
    - To help you train your naive bayes model, you will need to \\*compute a dictionary\\* where the \\*keys are a tuple (word, label) \\*and the values are the corresponding \\*frequency\\*. Note that the labels we'll use here are 1\\* for positive and 0 for negative\\*.  You will also implement a \\*lookup helper function\\* that takes in the \\*freqs\\* \\*dictionary\\*, a \\*word\\*, and a \\*label\\* (1 or 0) and \\*returns the number of times that word and label tuple appears in the collection of tweets.\\*  For example: given a list of tweets ["I am rather excited", "you are rather happy"] and the label 1, the function will return a dictionary that contains the following key-value pairs:  { ("rather", 1): 2, ("happi", 1) : 1, ("excit", 1) : 1 }  - Notice how for each word in the given string, the same label 1 is assigned to each word.  - Notice how the words "I" and "am" are not saved, since it was removed by \\*process_tweet\\* because it is a \\*stopword\\*.  - Notice how the word " rather" appears twice in the list of tweets, and so its count value is 2.
      <br>

  <a id="node-305"></a>
  - Exercise 1 - count_tweets
    <br>

    <a id="node-306"></a>
    - Create a function \\*count_tweets\\* that \\*takes a list of tweets\\* as input, \\*cleans\\* all of them, and \\*returns a dictionary\\*.  - The \\*key\\* in the dictionary is a \\*tuple containing the stemmed word and its class label,\\* e.g. ("happi",1).  - The \\*value\\* the \\*number of times this word appears in the given collection of tweet\\*s (an integer).  \\*Hints\\*  • Please use the `\\*process_tweet\\*` function that was imported above, and then store the words in their respective dictionaries and sets.  • You may find it useful to use the `\\*zip\\*` function to match each element in `tweets` with each element in `ys`.  • Remember to \\*check\\* if the key in the dictionary \\*exists\\* before adding that key to the dictionary, or incrementing its value.  • Assume that the `result` dictionary that is input will contain clean key-value pairs (you can assume that the values will be integers that can be incremented). It is\\* good practice to check the datatype\\* before \\*incrementing\\* the value, but it's not required here.
      <br>

        <a id="node-307"></a>
        <p align="center"><kbd><img src="assets/a48010192fd507381b3836d9e443004ee2c653d8.png" width="100%"></kbd></p>
        <br>

        <a id="node-308"></a>
        <p align="center"><kbd><img src="assets/a78dec7e25060115b81349b4678a208a18404aae.png" width="100%"></kbd></p>
        <br>

<a id="node-309"></a>
- 2 - Train your Model using Naive Bayes
  <br>

  <a id="node-310"></a>
  - Some explaination
    <br>

      <a id="node-311"></a>
      <p align="center"><kbd><img src="assets/be33a50225a9799f3f00e0f1527db9b296c182c6.png" width="100%"></kbd></p>
      <br>

      <a id="node-312"></a>
      <p align="center"><kbd><img src="assets/568c0f65b422af5f73d557cdefabc508bda43650.png" width="100%"></kbd></p>
      > Phòng khi bối rối ngu đột xuất để rồi không hiểu tại sao logprior lại bằng
      > log(Dpos/Dneg) thì P(Dpos) = Dpos/D, P(Dneg) = Dneg/D Nên chia hai thằng
      > đó cho nhau ra Dpos/Dneg

      <br>

      <a id="node-313"></a>
      <p align="center"><kbd><img src="assets/d2071f33c164957cc286056330782da22dde886b.png" width="100%"></kbd></p>
      <p align="center"><kbd><img src="assets/d2071f33c164957cc286056330782da22dde886b.png" width="100%"></kbd></p>
      <p align="center"><kbd><img src="assets/522544d33a5ec2f2b4415dde55f2799acdaae872.png" width="100%"></kbd></p>
      <br>

    <a id="node-314"></a>
    - \\/\\*Create freqs dictionary \\*\\/  • Given your \\*count_tweets\\* function, you can compute a dictionary called \\*freqs\\* that contains all the frequencies.  • In this freqs dictionary, the \\*key\\* is the tuple \\*(word, label)\\*  • The value is the \\*number of times it has appeared\\*.  We will use this dictionary in several parts of this assignment.
      <br>

      <a id="node-315"></a>
      - # Build the freqs dictionary for later uses freqs = count_tweets({}, train_x, train_y)
        <br>

  <a id="node-316"></a>
  - Exercise 2 - train_naive_bayes
    <br>

      <a id="node-317"></a>
      <p align="center"><kbd><img src="assets/9b70f80fd855f957c7b859a03f1aa3eae04d71b6.png" width="100%"></kbd></p>
      <br>

      <a id="node-318"></a>
      <p align="center"><kbd><img src="assets/18c01da4bb34cd94d3b21764e82b612fb8cc1d52.png" width="100%"></kbd></p>
      <br>

      <a id="node-319"></a>
      <p align="center"><kbd><img src="assets/9cd8e4837519d123afb446caf07b9ebf61fffabf.png" width="100%"></kbd></p>
      <p align="center"><kbd><img src="assets/9cd8e4837519d123afb446caf07b9ebf61fffabf.png" width="100%"></kbd></p>
      <p align="center"><kbd><img src="assets/ab0e7b463519b20fa4aee05409ee89d96ec7fc55.png" width="100%"></kbd></p>
      > len(y==1) là ra y xì len của y, nhớ nha vì y==1 ra 1 vector
      > dài bằng y chưa các kết quả so sánh các vị trí của y với 1.
      > giống thì bằng 1, khác thì = 0. Nên phải sum mới đúng

      > Cách làm như này rất gọn mà Python nó mạnh những cái như vậy
      > vocab = set([key[0] for key in freqs])

      <br>

      <a id="node-320"></a>
      <p align="center"><kbd><img src="assets/cfd0dc805088d7d45a8ac1c30dbfe18759ca7f63.png" width="100%"></kbd></p>
      <br>

<a id="node-321"></a>
- 3 - Test your Naive Bayes
  <br>

  <a id="node-322"></a>
  - Exercise 3 - naive_bayes_predict
    <br>

      <a id="node-323"></a>
      <p align="center"><kbd><img src="assets/31b7ebbb66d23d5c56fad667eb7e1b9f5ed1134a.png" width="100%"></kbd></p>
      <br>

    <a id="node-324"></a>
    - Note   Note we calculate the \\*prior\\* from the \\*training data\\*, and that the training data is evenly split between positive and negative labels (4000 positive and 4000 negative tweets). This means that the ratio of positive to negative 1, and the logprior is \\*0.\\*  The value of 0.0 means that when we add the logprior to the log likelihood, we're just adding zero to the log likelihood. However, please remember to include the logprior, because whenever the data is not perfectly balanced, the logprior will be a non-zero value.
      <br>

        <a id="node-325"></a>
        <p align="center"><kbd><img src="assets/8fe7a932b4618d761af00287b5b77f28028934fc.png" width="100%"></kbd></p>
        <br>

        <a id="node-326"></a>
        <p align="center"><kbd><img src="assets/2770d64fef227f40d790d92fb3e9f3f4f35c7b4a.png" width="100%"></kbd></p>
        <br>

  <a id="node-327"></a>
  - Exercise 4 - test_naive_bayes
    <br>

    <a id="node-328"></a>
    - Implement test_naive_bayes. \\*Instructions\\*:  • Implement \\*test_naive_bayes\\* to check the accuracy of your predictions.  • The function takes in your \\*test_x\\*, \\*test_y\\*, \\*log_prior\\*, and \\*loglikelihood\\*  • It returns the accuracy of your model.  • First, use \\*naive_bayes_predict\\* function to make predictions for each tweet in test_x.
      <br>

        <a id="node-329"></a>
        <p align="center"><kbd><img src="assets/75d8cf0357a25af2c5775489950ac63a30cd37c8.png" width="100%"></kbd></p>
        > Nhờ câu hint mà làm thôi
        >
        > # error is the average of the **absolute** values of the  **differences**
        > between y_hats and test_y
        >
        > differences -> Trừ nhau chứ gì**,**average -> sum./len**.**Nhớ****absolute nữa, không nó ra âm
        >
        > error = np.abs(np.sum(y_hats - test_y)/len(test_y))

        > abs(y^-y) chứ ko phải sum hết rồi mới abs

        <br>

        <a id="node-330"></a>
        <p align="center"><kbd><img src="assets/7c2a48e1caaef4e554ea54658302a2ab7288f195.png" width="100%"></kbd></p>
        <br>

      <a id="node-331"></a>
      - # UNQ_C7 (UNIQUE CELL IDENTIFIER, DO NOT EDIT) # Run this cell to test your function for tweet in ['I am happy', 'I am bad', 'this movie should have been great.', 'great', 'great great', 'great great great', 'great great great great']:     # print( '%s -> %f' % (tweet, naive_bayes_predict(tweet, logprior, loglikelihood)))     p = naive_bayes_predict(tweet, logprior, loglikelihood) #     print(f'{tweet} -> {p:.2f} ({p_category})')     print(f'{tweet} -> {p:.2f}')  -> I am happy -> 2.14 I am bad -> -1.31 this movie should have been great. -> 2.12 great -> 2.13 great great -> 4.26 great great great -> 6.39 great great great great -> 8.52 
        <br>

        <a id="node-332"></a>
        <p align="center"><kbd><img src="assets/15671033ba2a210fabde7bae17e7fcf15d91c889.png" width="100%"></kbd></p>
        <br>

<a id="node-333"></a>
- 4 - Filter words by Ratio of Positive to Negative Counts
  <br>

  <a id="node-334"></a>
  - • Some words have \\*more positive counts\\* than others, and can be considered "more positive". Likewise, some words can be considered more negative than others.  • One way for us to define the level of positiveness or negativeness, without calculating the log likelihood, is to compare the positive to negative frequency of the word.  ▪ Note that we can also use the log likelihood calculations to compare relative positivity or negativity of words.  • We can calculate the ratio of positive to negative frequencies of a word.  • Once we're able to calculate these ratios, we can also \\*filter a subset of words\\* that have a \\*minimum ratio of positivity / negativity\\* or higher.  • Similarly, we can also filter a subset of words that have a maximum ratio of positivity / negativity or lower (words that are at least as negative, or even more negative than a given threshold).
    <br>

  <a id="node-335"></a>
  - Exercise 5 - get_ratio
    <br>

      <a id="node-336"></a>
      <p align="center"><kbd><img src="assets/90cce6cacf6456c8523f5c0795f4666a3b79ce7d.png" width="100%"></kbd></p>
      <br>

      <a id="node-337"></a>
      <p align="center"><kbd><img src="assets/40aaf11fd869fa7eebcb25a0c410adf067a94ad2.png" width="100%"></kbd></p>
      <br>

  <a id="node-338"></a>
  - Exercise 6 - get_words_by_threshold
    <br>

      <a id="node-339"></a>
      <p align="center"><kbd><img src="assets/7b1a5cf76f4368bede2a2696a198fbade6433cac.png" width="100%"></kbd></p>
      <br>

      <a id="node-340"></a>
      <p align="center"><kbd><img src="assets/9d047b1ea2f069f1b200bc1c43215a967c6f341a.png" width="100%"></kbd></p>
      <br>

      <a id="node-341"></a>
      <p align="center"><kbd><img src="assets/aca666002df7d2ce2a79a326ffa73ec5ffa7df5e.png" width="100%"></kbd></p>
      > Notice the difference between the positive and negative ratios.
      > Emojis like **:(** and words like '**me**' **tend to have a negative**
      > connotation. Other words like glad, community, arrives, tend to
      > be found in the positive tweets.

      <br>

<a id="node-342"></a>
- 5 - Error Analysis¶
  <br>

  <a id="node-343"></a>
  - # Some error analysis done for you print('Truth Predicted Tweet') for x, y in zip(test_x, test_y):     y_hat = naive_bayes_predict(x, logprior, loglikelihood)     if y != (np.sign(y_hat) > 0):         print('%d\\t%0.2f\\t%s' % (y, np.sign(y_hat) > 0, ' '.join(             process_tweet(x)).encode('ascii', 'ignore')))
    > In this part you will see some tweets that your model
    > missclassified. Why do you think the missclassifications
    > happened? Were there any assumptions made by your
    > naive bayes model?

    <br>

    <a id="node-344"></a>
    - Truth Predicted Tweet 1 0.00 b'truli later move know queen bee upward bound movingonup' 1 0.00 b'new report talk burn calori cold work harder warm feel better weather :p' 1 0.00 b'harri niall 94 harri born ik stupid wanna chang :D' 1 0.00 b'park get sunlight' 1 0.00 b'uff itna miss karhi thi ap :p' 0 1.00 b'hello info possibl interest jonatha close join beti :( great' 0 1.00 b'u prob fun david' 0 1.00 b'pat jay' 0 1.00 b'sr financi analyst expedia inc bellevu wa financ expediajob job job hire'
      <br>

<a id="node-345"></a>
- 6 - Predict with your own Tweet
  <br>

  <a id="node-346"></a>
  - # Test with your own tweet - feel free to modify `my_tweet` my_tweet = 'I am happy because I am learning :)'  p = naive_bayes_predict(my_tweet, logprior, loglikelihood) print(p)  -> 9.571143871339594
    > Congratulations on completing this
    > assignment. See you next week!

    <br>

