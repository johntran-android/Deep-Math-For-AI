# C1w1_logistic Regression

📊 **Progress:** `46` Notes | `121` Screenshots

---

Learn to extract features from text into numerical vectors, then build a binary 
classifier for tweets using a logistic regression!

Learning Objectives

 • Sentiment analysis
 • Logistic regression
 • Data pre-processing
 • Calculating word frequencies
 • Feature extraction
 • Vocabulary creation
 • Supervised learning

Learn to extract features from text into numerical vectors, then build a binary classifier for tweets using a logistic regression!
**Learning Objectives**
 • Sentiment analysis
 • Logistic regression
 • Data pre-processing
 • Calculating word frequencies
 • Feature extraction
 • Vocabulary creation
 • Supervised learning

<a id="node-3"></a>
## Welcome To NLP Spec

<br>


<a id="node-4"></a>
### 1 Introduction of Younes and Lukasz as instructors of the

> [!NOTE]
> 1 Introduction of Younes and Lukasz as instructors of the
> specialization.
>
> 2 Overview of the development of NLP from rule-based systems to
> deep learning-based systems.
>
> 3 The rise of end-to-end systems and attention models in NLP.
>
> 4 Overview of the four courses in the specialization, starting with
> classification and vector spaces in the first course.
>
> 5 The second course focuses on probabilistic models in NLP.
>
> 6 The third course teaches sequence models.
>
> 7 The fourth course focuses on attention models and their applications
> in chatbots, question answering, and text summarization.
>
> 8 The potential impact of these models in industry, including call
> centers and data analysis.
>
> 9 Excitement about learning and building NLP systems.

<br>


<a id="node-5"></a>
## Welcome To Course 1

<br>


<a id="node-6"></a>
### 1 Introduction to NLP course

> [!NOTE]
> 1 Introduction to NLP course
>
> 2 Topics covered: classification and vector spaces
>
> 3 Applications of NLP to sentiment analysis and word translation
>
> 4 Example problem of building a system to classify positive and negative
> product reviews
>
> 5 Week 1: **Representing text as a vector** and using**logistic regression** to
> classify sentiment
>
> 6 Week 2: Using the **Naive Bayes classifier** for sentiment classification
>
> 7 Week 3: Learning about **vector space models** and their applications in
> **information retrieval, indexing, relevancy ranking, and information
> filtering**
>
> 8 Week 4: Building a simple **machine translation** system and using
> **locality sensitive hashing** to improve **nearest neighbor search**
>
> 9 Importance of NLP concepts in search engine algorithms

<br>


<a id="node-7"></a>
## Acknowledgement - Ken Church

<br>

<a id="node-8"></a>

<p align="center"><kbd><img src="assets/ac974b41d5ec7801897a4b467325200831430e30.png" width="100%"></kbd></p>

<br>


<a id="node-9"></a>
## Week Introduction

<br>


<a id="node-10"></a>
### Welcome to the first week of Course 1.

> [!NOTE]
> Welcome to the first week of Course 1.
>
> This week is all about **logistic regression**, which is a very
> important tool used in many applications in NLP.
>
> Logistic regression algorithms are **particularly useful** because
> they are **easy to train** and provide you with a **good baseline
> result**.
>
> This week you'll use logistic regression for **sentiment analysis of
> tweets**.
>
> You will first **process your data**, then you **train your model** and
> finally, you will **test the accuracy**of your model.

<br>


<a id="node-11"></a>
## Supervised Ml & Sentiment Analysis

<br>


<a id="node-12"></a>
### 1 The **goal** of supervised machine learning is to **minimize error rates or cost**

> [!NOTE]
> 1 The **goal** of supervised machine learning is to **minimize error rates or cost**
> by **mapping input features X to output labels Y hat.**
>
> 2 **Logistic regression** is a **classification** algorithm used to assign
> observations to two distinct classes.
>
> 3 In the context of **sentiment analysis**, logistic regression can be used to
> predict whether a tweet has a positive or negative sentiment.
>
> 4 The steps for building a logistic regression classifier for sentiment analysis
> include: p**rocessing raw tweets to extract useful features**, **training** the
> **classifier** to**minimize the cost,** and **making predictions** based on the trained
> model.
>
> 5 The next video will cover how to extract features from tweets for sentiment
> analysis.

<br>

<a id="node-13"></a>

<p align="center"><kbd><img src="assets/3f2438c7fc532682af150cdff2ecf4b26dd6b473.png" width="100%"></kbd></p>

<br>

<a id="node-14"></a>

<p align="center"><kbd><img src="assets/2bc29e6e546e3df7c73abf11f2e1a6e86feb0dbb.png" width="100%"></kbd></p>

<br>

<a id="node-15"></a>

<p align="center"><kbd><img src="assets/743fc8a632cfa8135c4521e9f3f52690b4abb403.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là: Preprocess để **extract feature** from text rồi
> bỏ vào Lo.Re model để **train** và **classify**

<br>


<a id="node-16"></a>
## Vocabulary & Feature Extraction

<br>


<a id="node-17"></a>
### 1 Introduction: Learning to **represent text as a vector**

> [!NOTE]
> 1 Introduction: Learning to **represent text as a vector**
>
> 2 Building a vocabulary: Creating a **list of unique words**
>
> 3 Extracting features: Assigning values to features in a tweet
> based on the vocabulary
>
> 4 **Sparse** **representation**: Representation with a small relative
> number of non-zero values
>
> 5 Problems with large vocabularies: Model training takes
> **excessive time**
>
> 6 Conclusion: Recap of representing text as a vector and
> introduction to identifying problems with large vocabularies in
> the next video.

<br>

<a id="node-18"></a>

<p align="center"><kbd><img src="assets/748ac088fc043220a4024be577d0e120f8f215b5.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là tạo bộ dictionary/ list các unique words

<br>

<a id="node-19"></a>

<p align="center"><kbd><img src="assets/0f416e2a99d96d16f821185dc5b97441056a6a1f.png" width="100%"></kbd></p>

> [!NOTE]
> Một cách để 'extract feature' - tức là tạo feature vector gọi là **sparse**
> **representation** (từ nào có trong dic thì gán 1, không có thì gán 0
>
> Cách xây dựng vector kiểu này khiến số 0 nhiều nên gọi là "sparse"
> tạm dịch là "trống trải" / "thưa thớt"

<br>

<a id="node-20"></a>

<p align="center"><kbd><img src="assets/21510d8c74ac0ba47a2f48317ab42ce565bca438.png" width="100%"></kbd></p>

> [!NOTE]
> Vấn đề đ.v làm kiểu này là số params phải learn là rất lớn - độ
> dài của feature vector = V và V thường rất lớn do bộ vocab
> size lớn

<br>

<a id="node-21"></a>

<p align="center"><kbd><img src="assets/0984d76efdc980f581aed9486827ac473c84dcb9.png" width="100%"></kbd></p>

<br>

<a id="node-22"></a>

<p align="center"><kbd><img src="assets/c2fb0b807731ee81382055ad83bbee4c4de9772b.png" width="100%"></kbd></p>

> [!NOTE]
> 13 từ - the0-theta13 = 14

<br>


<a id="node-23"></a>
## Negative & Positive Frequencies

<br>

<a id="node-24"></a>

<p align="center"><kbd><img src="assets/6fa0bf43438cb1407c8f59dab35cd283bca4f70a.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái cách feature extraction này, đối với từng từ trong
> vocabulary list, ta đếm số lần nó xuất hiện trong positive và
> negative câu

<br>

<a id="node-25"></a>

<p align="center"><kbd><img src="assets/cf060eb8a785905030bd9d36c0d334524d4cf42c.png" width="100%"></kbd></p>

> [!NOTE]
> Các câu trong corpus dc gắn label
> positive / negative

<br>

<a id="node-26"></a>

<p align="center"><kbd><img src="assets/731f7b92601db48472612cd08f448980fba99589.png" width="100%"></kbd></p>

> [!NOTE]
> Thì happy xuất hiện 2 lần trong các
> câu positive -> posFreq = 2

<br>

<a id="node-27"></a>

<p align="center"><kbd><img src="assets/31b0ee10bae0de81c184d88390d5b298f5aa3fb8.png" width="100%"></kbd></p>

> [!NOTE]
> "sad" xuất hiện 2 lần trong
> negative câu -> negFreq = 2

<br>

<a id="node-28"></a>

<p align="center"><kbd><img src="assets/319f9d8c6bbfae9a660205b7b68c2642ae664666.png" width="100%"></kbd></p>

<br>


<a id="node-29"></a>
## Feature Extraction With Frequencies

<br>

<a id="node-30"></a>

<p align="center"><kbd><img src="assets/a9a4690cf3b11c64e946032d38b2d55457bdbca2.png" width="100%"></kbd></p>

<br>

<a id="node-31"></a>

<p align="center"><kbd><img src="assets/693e0493199299553eefe868f1523bbf7a95fd6d.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là encode feature theo 3 dimension thay
> vì V dimension như cách làm trước

<br>

<a id="node-32"></a>

<p align="center"><kbd><img src="assets/c62e733125ee5c98e6718dfc7d3297ab7b2e9ee2.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là tổng các PosFreq của
> các từ trong câu này là 8

<br>

<a id="node-33"></a>

<p align="center"><kbd><img src="assets/bae188507dc51b52d076cdfd2daed82cf2c04bf5.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là tổng các NegFreq của
> các từ trong câu này là 11

<br>

<a id="node-34"></a>

<p align="center"><kbd><img src="assets/b011b0152be8fbeaa21ab55f4594912cdae10a10.png" width="100%"></kbd></p>

> [!NOTE]
> Nên feature representation (encode) của câu này là [1,8,11]

<br>


<a id="node-35"></a>
## Preprocessing

<br>

<a id="node-36"></a>

<p align="center"><kbd><img src="assets/b6d3de19c0b90e8c8522241f3efb604407da146a.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái preprocess đầu tiên là bỏ đi 'stop word' vốn
> không thay đổi lắm thông tin

<br>

<a id="node-37"></a>

<p align="center"><kbd><img src="assets/b55f7fbb4e5f82f2e56622b768527de0df34015a.png" width="100%"></kbd></p>

🔗 **Related:** [1 \\*NLP errors\\* are \\*inevitable\\* no matter what method you use  2 Errors in NLP can be caused by \\*loss of semantic meaning\\*, \\*word\\* \\*order\\*, and \\*language quirks\\* that are \\*difficult for machines\\* to understand  3 It's important to \\*analyze processed text\\* to ensure accurate results, including \\*checking for punctuation and word removal\\*  4 \\*Naïve base classification\\* relies on word \\*frequency\\* \\*counts\\* and can lead to \\*errors due to its independence assumption\\*  5 \\*Word vectors\\* can be used to improve NLP results  6 Naïve base classification may fail in cases of \\*adversarial attacks,\\* which are \\*language phenomena like sarcasm, irony, and euphemism\\* that machines have\\* difficulty understanding.\\*](error_analysis.md#node-277)

> [!NOTE]
> Sau đó là punctuation tuy nhiên
>
> Đôi khi phải cân nhắc giữ lại punctuation nếu
> nó thể hiện thông tin cần thiết cho nlp task cụ thể đang làm

<br>

<a id="node-38"></a>

<p align="center"><kbd><img src="assets/b0e5cdbba2151814937de91d9983af778f4f50aa.png" width="100%"></kbd></p>

> [!NOTE]
> Bỏ luôn handles và URLS, còn lại câu này mang ý nghĩa positive, thì
> một ML model tốt sẽ detect dc là positive

<br>

<a id="node-39"></a>

<p align="center"><kbd><img src="assets/3a5a9a9b9e697b82d2f1aa3d16a8e550b7692060.png" width="100%"></kbd></p>

> [!NOTE]
> Cuối cùng là 'Stemming' - bỏ đi mấy cái hậu tố (suffix) chỉ giữ
> lại cái từ gốc và giúp giảm bớt vocab list
>
> Và lowercase hết

<br>

<a id="node-40"></a>

<p align="center"><kbd><img src="assets/79026f5c72a140e4ef8d1a530d40af3d56a1a774.png" width="100%"></kbd></p>

> [!NOTE]
> Kết quả sau khi
> preprocessed

<br>


<a id="node-41"></a>
## Preprocessing Reading

<br>


<a id="node-42"></a>
### When preprocessing, you have to perform the following:

> [!NOTE]
> When preprocessing, you have to perform the following:
>
> 1 Eliminate handles and URLs
>
> 2 Tokenize the string into words.
>
> 3 Remove stop words like "and, is, a, on, etc."
>
> 4 Stemming- or convert every word to its stem. Like dancer, dancing, danced,
> becomes 'danc'. You can use porter stemmer to take care of this.
>
> 5 Convert all your words to lower case.
>
> For example the following tweet "@YMourri and @AndrewYNg are tuning a GREAT AI
> model at https://deeplearning.ai!!!" after preprocessing becomes
>
> [\\/tun\\/,\\/great\\/,\\/ai\\/,\\/model\\/]. Hence you can see how we eliminated handles,
> tokenized it into words, removed stop words, performed stemming, and converted
> everything to lower case.

<br>


<a id="node-43"></a>
## Lab: Nl Preprocessing

<br>


<a id="node-44"></a>
### In this lab, we will be exploring how to preprocess tweets for

> [!NOTE]
> In this lab, we will be exploring how to preprocess tweets for
> sentiment analysis. We will **provide a function for
> preprocessing tweets** during this week's assignment, but it is
> **still good to know what is going on** under the hood.
>
> By the end of this lecture, you will see **how to use the NLTK
> package to perform a preprocessing** pipeline for Twitter
> datasets.

<br>


<a id="node-45"></a>
#### Setup  Đại khái là sẽ dùng thư viện Python NLTK dùng để natural language preprocessing, có các modules để collect, handling và processing Twitter data

<br>

<a id="node-46"></a>

<p align="center"><kbd><img src="assets/c73c2a70c1cf0a3834dfe9b463a7b0d1d8ea9dd9.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là sẽ dùng thư viện Python NLTK dùng để natural
> language preprocessing, có các modules để collect,
> handling và processing Twitter data

<br>


<a id="node-47"></a>
#### About the Twitter dataset

<br>

<a id="node-48"></a>

<p align="center"><kbd><img src="assets/d0d16f557bf82e09dbc5e21dd65380bf65db88bb.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là 5000 positive 5000 negative, chia đều vậy là để
> tạo một dataset cân bằng chứ nhớ là nó không phản ánh
> distribution trong thực tế (dĩ nhiên)
>
> Đại khái là có 2 list, mỗi entry là string

<br>

<a id="node-49"></a>

<p align="center"><kbd><img src="assets/9f8fcd774544ed0559caa20e7c0b7ae246b88729.png" width="100%"></kbd></p>

<br>


<a id="node-50"></a>
#### Looking at raw texts

<br>

<a id="node-51"></a>

<p align="center"><kbd><img src="assets/57f91aa5974d22a3a7ef5492d1d6c9e0e1b111df.png" width="100%"></kbd></p>

> [!NOTE]
> Xem để có cái hiểu data chiếm 80% thành công của một data science
> project. Đại khái nhận thấy tweet hay chứa url và emoticon ví dụ :)

<br>


<a id="node-52"></a>
#### Preprocess raw text for Sentiment analysis

<br>


<a id="node-54"></a>
#### Remove hyperlinks, Twitter marks and styles

<br>

<a id="node-55"></a>

<p align="center"><kbd><img src="assets/d1871a6965128d532d8b0ac2090ee1eb642ec0c1.png" width="100%"></kbd></p>

<br>


<a id="node-56"></a>
#### Tokenize the string

<br>

<a id="node-57"></a>

<p align="center"><kbd><img src="assets/04e68ff3ac30049610fcfb8f6e62fd7d7a0f6606.png" width="100%"></kbd></p>

<br>


<a id="node-58"></a>
#### Remove stop words and punctuations

<br>

<a id="node-59"></a>

<p align="center"><kbd><img src="assets/6fa5b3f8c743ac39e08ef9f7e72314e1e3b5a792.png" width="100%"></kbd></p>

> [!NOTE]
> Xem những stop word và punctuation có gì

<br>

<a id="node-60"></a>

<p align="center"><kbd><img src="assets/8ce4af17de75237e8ef762d5657aa5aff003fa68.png" width="100%"></kbd></p>

> [!NOTE]
> Một số trường hợp stop word cần phải được customize
> lại vì mang thông tin quan trọng, còn ở đây ổng bỏ hết,
> emoticon cũng vậy

<br>


<a id="node-61"></a>
#### Stemming

<br>

<a id="node-62"></a>

<p align="center"><kbd><img src="assets/569961d0a42e468a80c43794bb8181c5c1260af8.png" width="100%"></kbd></p>

> [!NOTE]
> Stemming như trong bài giảng đã hiểu là convert về cái từ gốc mà nếu add
> mấy cái suffix râu ria sẽ ra nhiều từ khác nhau như ed, ing thì stemming sẽ
> **giúp giảm vocab size rất nhiều**, mà vẫn **giữ phần lớn ý nghĩa của từ vựng**
>
> Có nhiều module để **stemming** nhưng ở đây ổng chọn **Porter**

<br>

<a id="node-63"></a>

<p align="center"><kbd><img src="assets/068b698234d151a644738fe5fc15d6bfeed1b898.png" width="100%"></kbd></p>

<br>


<a id="node-64"></a>
#### process_tweet()

<br>

<a id="node-65"></a>

<p align="center"><kbd><img src="assets/b1b8387d2ee866608106c83d95a1dc7dffe11fe1.png" width="100%"></kbd></p>

> [!NOTE]
> Đai khái là mấy step trên sẽ làm sẵn trong funciton **process_tweet**()
> **khi làm assignment chỉ việc gọi function** này thôi nhưng **quan trọng là
> đã hiểu nó làm cái gì**

<br>

<a id="node-53"></a>

<p align="center"><kbd><img src="assets/3f8aaf6f6c2180347588e13e4a8839802731f25e.png" width="100%"></kbd></p>

> [!NOTE]
> Chọn một câu mà ta thấy complex. Download một số tool
> preprocessing từ NLTK để làm

<br>


<a id="node-66"></a>
## Putting It All Together

<br>

<a id="node-67"></a>

<p align="center"><kbd><img src="assets/5614c8d4217c2a99085e6eab3f2cfd639fdae3d6.png" width="100%"></kbd></p>

> [!NOTE]
> Mỗi 1 câu sẽ được represented/encoded
> bởi một 3 dimensions vector

<br>

<a id="node-68"></a>

<p align="center"><kbd><img src="assets/b7cc1233914ad41610aeca9fc8710700d18d28fc.png" width="100%"></kbd></p>

<br>

<a id="node-69"></a>

<p align="center"><kbd><img src="assets/72a6bcb1f1ea5720a1d915435fcfd3f7d4339968.png" width="100%"></kbd></p>

> [!NOTE]
> Và làm vậy với 1 một bộ m
> câu, ta được 1 matrix

<br>

<a id="node-70"></a>

<p align="center"><kbd><img src="assets/0bff38c962b34541c656c0795133a337b5543332.png" width="100%"></kbd></p>

> [!NOTE]
> - Bước build_freqs:
>
> Với tất cả các tweets và label tương ứng (positive hay negative), nó tạo
> 1 bộ vocab và tương ưng mỗi vocab là chỉ số positive và negative
> frequency ví dụ ' happy' pos = 200, neg = 50 tức là nó xuất hiện 200 lần
> trong các câu có label positive và 50 lần trong các câu gắn label
> negative
>
> Ini matrix X  = shape (m,3) tức là có m row, 3 columns
>
> - Bước process_tweet như đã xem ở lab trước nó sẽ xử lý các bước
> như loại bỏ stop word, punctuation, stemming,,
>
> - Bước extract_features sẽ là cái mình sẽ làm trong programming
> assignment : Dựa vào frequency dictionary, mình sẽ tạo representative
> vector cho mỗi tweet đã được preprocessed.
>
> Thì đại khái là tính tổng positive count và negative của các từ trong câu

<br>


<a id="node-71"></a>
## Visualization Word Frequencies

<br>


<a id="node-72"></a>
### Building and Visualizing word frequencies

> [!NOTE]
> Building and Visualizing word frequencies
>
> In this lab, we will focus on the **build_freqs**() helper
> function and visualizing a dataset fed into it. In our goal of
> tweet sentiment analysis, this function will **build a
> dictionary where we can lookup how many times a word
> appears in the lists of positive or negative** tweets. This
> will be very helpful when extracting the features of the
> dataset in the week's programming assignment. Let's see
> how this function is implemented under the hood in this
> notebook.

<br>


<a id="node-73"></a>
#### Setup

<br>

<a id="node-74"></a>

<p align="center"><kbd><img src="assets/2061659f879b78452a7f7390576b6c1cd2ee2be9.png" width="100%"></kbd></p>

<br>


<a id="node-75"></a>
#### Load the NLTK sample dataset

<br>

<a id="node-76"></a>

<p align="center"><kbd><img src="assets/f97bd98fa623736294c64391a50424ba026f5f3f.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ổng load bộ twitter dataset from NLTK, rồi lấy ra các
> positive tweets và negative tweets rồi concat lại thì 5000 câu đầu
> là positive, 5000 câu sau là negative. Xong tạo 2 array 5000 số 1
> và 5000 số 0 rồi concat lại để thành cái vector label

<br>


<a id="node-77"></a>
#### Dictionaries

<br>

<a id="node-78"></a>

<p align="center"><kbd><img src="assets/475c9cb3e4aaf394586418615d2c0ccdb5975997.png" width="100%"></kbd></p>

<br>

<a id="node-79"></a>

<p align="center"><kbd><img src="assets/a4b717212026e0af925a7f216f40503bb54f253b.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là một số tính chất của Python dictionary có thể
> get() để có default value nếu ko có key trong dic còn
> dùng [] thì ko có nó báo lỗi.

<br>


<a id="node-80"></a>
#### Word frequency dictionary

<br>

<a id="node-81"></a>

<p align="center"><kbd><img src="assets/f8acb4b38e8dc3eb82326cade6ec1cd03a8be989.png" width="100%"></kbd></p>

> [!NOTE]
> Cũng dễ hiểu chỉ lưu ý chỗ này là có cái vụ 2 element key, tức là ví dụ
> (word, y) là key freqs[('happy',1)] = 10 tức là từ 'happy', cột positive thì
> bằng 10.

<br>

<a id="node-82"></a>

<p align="center"><kbd><img src="assets/ebf65735107785473cad77defaa61770641d84de.png" width="100%"></kbd></p>

<br>

<a id="node-83"></a>

<p align="center"><kbd><img src="assets/ea558b4e16d104670885ecc12b0dc40be5a741f7.png" width="100%"></kbd></p>

<br>


<a id="node-84"></a>
#### Table of word counts

<br>

<a id="node-85"></a>

<p align="center"><kbd><img src="assets/f73147e4855050cb45a7a5ade4fecb0522a2a259.png" width="100%"></kbd></p>

<br>

<a id="node-86"></a>

<p align="center"><kbd><img src="assets/67c4fdb50418f7d0f096ccebd0c685ba5e11bb81.png" width="100%"></kbd></p>

<br>

<a id="node-87"></a>

<p align="center"><kbd><img src="assets/80dc910a1d964d957deca7210242cea125f18d64.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là:
>
> Plot một số từ theo 2 thông số log của positive count và log
> của negative count
>
> Cho ta cái nhìn trực quan (visualizing) về 'mức độ' positive
> và  negative của chúng  ('\/scatter plot to inspect this table
> visually')
>
> \/Và dùng hàm log '\/take into account the wide discrepancies
> between the raw counts' \/hiểu đại khái là để cho giảm bớt
> sự quá chênh lệch giữa các giá trị pos và neg sẽ khiến plot
> bị stretch

<br>


<a id="node-88"></a>
## Logistic Regression Overview

<br>

<a id="node-89"></a>

<p align="center"><kbd><img src="assets/eac56b7bd177c2099222fb59213bfc2c28d5268f.png" width="100%"></kbd></p>

<br>

<a id="node-90"></a>

<p align="center"><kbd><img src="assets/0b4ff86ad66d7d273fecea8f80e224d85cd93282.png" width="100%"></kbd></p>

<br>

<a id="node-91"></a>

<p align="center"><kbd><img src="assets/f216eb5aca77580dbe5d9d48e70493b4eef3d36c.png" width="100%"></kbd></p>

> [!NOTE]
> Có vector representation x, nhân với theta transpose rồi
> bỏ vào sigmoid tính ra probability x là positive bằng bao
> nhiêu đem so với threshold = 0.5

<br>


<a id="node-92"></a>
## Lo.re Training

<br>

<a id="node-93"></a>

<p align="center"><kbd><img src="assets/6f2333069d091627e4432deabfe9d8a3f7cc9153.png" width="100%"></kbd></p>

<br>

<a id="node-94"></a>

<p align="center"><kbd><img src="assets/86a49069f341d7810a296cfc9d23ae11e2a7e2e0.png" width="100%"></kbd></p>

> [!NOTE]
> Gradient descent

<br>


<a id="node-95"></a>
## Lab: Visualizing Tweets And Lo.re Models

<br>


<a id="node-96"></a>
### **Objectives:** Visualize and interpret the logistic

> [!NOTE]
> **Objectives:** Visualize and interpret the logistic
> regression model
>
> **Steps:**  • Plot tweets in a scatter plot using their
> positive and negative sums.
>
> • Plot the output of the logistic regression model in the
> same plot as a solid line

<br>


<a id="node-97"></a>
#### Import the required libraries

<br>

<a id="node-98"></a>

<p align="center"><kbd><img src="assets/cf3b2f90fd3abc04b08d56ea4619d49053260a08.png" width="100%"></kbd></p>

<br>


<a id="node-99"></a>
#### Load the NLTK sample dataset

<br>

<a id="node-100"></a>

<p align="center"><kbd><img src="assets/c76ce63e7e3a7c34dc92f9caf5f25cd5c8b84a85.png" width="100%"></kbd></p>

<br>


<a id="node-101"></a>
#### Load the extracted features

<br>

<a id="node-102"></a>

<p align="center"><kbd><img src="assets/762092588c90c136f5e374a6e58a3d913c269154.png" width="100%"></kbd></p>

> [!NOTE]
> Ý là do cuối tuần sẽ làm function extract feature này nên để khỏi ' lộ đáp án' ổng
> load sẵn các prep vector từ CSV file

<br>

<a id="node-103"></a>

<p align="center"><kbd><img src="assets/63bc3e51f7682370dac687f2027a6ee1d1bd65f7.png" width="100%"></kbd></p>

<br>


<a id="node-104"></a>
#### Load a pretrained Logistic Regression model

<br>


<a id="node-105"></a>
#### In the same way, as part of this week's assignment, a Logistic regression model must be trained. The next cell contains the resulting model from such training. Notice that a list of 3 numeric values represents the whole model, that we have called theta  𝜃  theta = [6.03518871e-08, 5.38184972e-04, -5.58300168e-04]

<br>


<a id="node-106"></a>
#### Plot the samples in a scatter plot

<br>

<a id="node-107"></a>

<p align="center"><kbd><img src="assets/b3522bda58890d389619b6ae9c58c940aad440f3.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là plot các data instance ra dù là 3D đáng lẽ phải vẽ trong
> không gian 3 chiều thì ổng nói khi đó 3 giá trị của theta (đã trained) sẽ
> cho ra 1 plane phân tách các instance thành 2 class, nhưng ở đây do
> cái feature đầu là bias đều bằng 1 nên vẽ mỗi instance bằng 2 feature
> sau lên Cartesian (2D)

<br>

<a id="node-108"></a>

<p align="center"><kbd><img src="assets/f2b32b9725ca35c103f767b541ada647b3392c03.png" width="100%"></kbd></p>

<br>


<a id="node-109"></a>
#### Plot the model alongside the data

<br>

<a id="node-110"></a>

<p align="center"><kbd><img src="assets/40331d42805e2ec87be728f5f0949d0f1dc67ebf.png" width="100%"></kbd></p>

> [!NOTE]
> Nói chung là nhừ theta vẽ ra cái đường phân chia (Decision Boundary?) rồi 2 cái
> arrow vuông góc với nó. Chưa hiểu cụ thể lắm nhưng chắc cũng ko quan trọng.

<br>

<a id="node-111"></a>

<p align="center"><kbd><img src="assets/9c4fd5b0810946383354966a4b76e5761e4a7da6.png" width="100%"></kbd></p>

<br>

<a id="node-112"></a>

<p align="center"><kbd><img src="assets/f5d73dd9c8fd11fb1ae9e62b30bac2677f2c11c7.png" width="100%"></kbd></p>

<br>


<a id="node-113"></a>
## Log.re: Testing

<br>


<a id="node-114"></a>
### 1 Using data to predict new data points

> [!NOTE]
> 1 Using data to predict new data points
>
> 2 Analyzing model generalization
>
> 3 Computing accuracy of a model
>
> 4 Process of computing sigmoid function for X_val with parameters
> Theta
>
> 5 Evaluating whether each value of h of Theta is greater than or
> equal to a threshold value
>
> 6 Building a predictions vector with zeros and ones
>
> 7 Computing accuracy by comparing predictions with true values
>
> 8 Dividing number of correct predictions by the total number of
> observations to estimate model's performance on unseen data
>
> 9 Summary of concepts learned in the first week of specialization
>
> 10 Implementation of concepts in programming exercise

<br>

<a id="node-115"></a>

<p align="center"><kbd><img src="assets/8167d7664300a428c40878b157851d9a53713afd.png" width="100%"></kbd></p>

<br>

<a id="node-116"></a>

<p align="center"><kbd><img src="assets/2ccde7f361027e1ce7a865c2325691e569739f28.png" width="100%"></kbd></p>

<br>

<a id="node-117"></a>

<p align="center"><kbd><img src="assets/18370db3b5f1417ecd7e92624108e218c5c1e5e0.png" width="100%"></kbd></p>

<br>

<a id="node-118"></a>

<p align="center"><kbd><img src="assets/d9b7f19d970e1eb5722a9bc07dafb5f2ca6c7386.png" width="100%"></kbd></p>

<br>

<a id="node-119"></a>

<p align="center"><kbd><img src="assets/06098ff57163f6d139b12cb5e11768a91c6f0992.png" width="100%"></kbd></p>

<br>


<a id="node-120"></a>
## Lo.re Cost Function

<br>


<a id="node-121"></a>
### 1 Introduction to logistic regression cost function and its

> [!NOTE]
> 1 Introduction to logistic regression cost function and its
> intuition
>
> 2 Components of the logistic regression cost function
> equation
>
> 3 Explanation of the two terms in the cost function equation
> and their relevance to label values of 0 and 1
>
> 4 Visualization of the cost function for label values of 0 and 1
>
> 5 Understanding the impact of prediction accuracy on overall
> cost
>
> 6 Mention of Naive Bayes as a different classification
> algorithm for predicting sentiment in tweets

<br>

<a id="node-122"></a>

<p align="center"><kbd><img src="assets/12c025cafbc14a6d685a57ac20d874b412e2dee0.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a80e8286474baff835fec4192b8762c03ed8802c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1da12dd202b18d37c71e792dbc3fb94e4f3236ea.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/12c025cafbc14a6d685a57ac20d874b412e2dee0.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a80e8286474baff835fec4192b8762c03ed8802c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1da12dd202b18d37c71e792dbc3fb94e4f3236ea.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/01ceefd7ec679c103b16c74754905f3a32198640.png" width="100%"></kbd></p>

> [!NOTE]
> Trung bình cộng của loss cho từng data sample
>
> Và vì loss này tính bởi hàm log nên luôn âm nên thêm dấu trừ ở phía trước để
> chuyển cost function thành dương

<br>

<a id="node-123"></a>

<p align="center"><kbd><img src="assets/243dda1cbe883a7cb0fccdc30c57e056f8ccfc46.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/243dda1cbe883a7cb0fccdc30c57e056f8ccfc46.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3ecdea347b00addffb969747d3c74a65ee2b7615.png" width="100%"></kbd></p>

> [!NOTE]
> Ôn lại thôi chứ biết rồi, 2 vế kiểu như sẽ phụ trách cho 2
> trường hợp y = 1 hay = 0. 
> Nếu y = 1 (thì vế 2 = 0, bỏ): 
> Nếu y^ cũng càng gần 1 thì log của (y^) sẽ càng gần bằng 0
> -> Loss gần 0. 
> Nếu y^ càng gần 0, log (0) sẽ về vô cùng -> Loss về vô cùng

<br>

<a id="node-124"></a>

<p align="center"><kbd><img src="assets/9d539e66c0f461fa3e4e73722ba25f3306a396cc.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/9d539e66c0f461fa3e4e73722ba25f3306a396cc.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c0b3ed45c24b880b2bb4112fa129b878ee03371e.png" width="100%"></kbd></p>

> [!NOTE]
> Tương tự khi y = 0

<br>


<a id="node-125"></a>
## Optional Logistic Regression: Cost Function

<br>


<a id="node-126"></a>
### 1. Đại khái xây dựng function P(y(i)) cho 1 instance như này sẽ đảm bảo

> [!NOTE]
> 1. Đại khái xây dựng function P(y(i)) cho 1 instance như này sẽ đảm bảo
> nếu tối đa được P sẽ cho ra predict chính xác
>
> 2. Xây dựng objective như này (tối đa tích của các P(i)) - PI sẽ  đảm bảo
> muốn PI lớn thì tất cả (P(y(i)) phải lớn = phải 'ráng' mà predict đúng cho mọi
> instance mới được.
>
> 3. Và để cho PI lớn nhất thì cũng tương đương làm log(PI) của nó lớn  nhất
>
> 4. Và dựa vào phép tính lôgarit, có thể chuyển nó thành dạng tổng log
>
> 5. Và Làm nó nó lớn nhất cũng chính là làm cho (Trừ của nó) nhỏ nhất ->
> Hoá ra hàm J

> [!NOTE]
> Hiểu được cái này rồi, rất hay

<br>

<a id="node-127"></a>

<p align="center"><kbd><img src="assets/7bd085a30f5e839fad9c152f585e75c02b823263.png" width="100%"></kbd></p>

<br>

<a id="node-128"></a>

<p align="center"><kbd><img src="assets/6ec2d8a75d0bd6a4ba4363476804bfb21612fcae.png" width="100%"></kbd></p>

<br>

<a id="node-129"></a>

<p align="center"><kbd><img src="assets/bc0af5ca28026ee354e1ed9b479fc5c30ec7babf.png" width="100%"></kbd></p>

<br>

<a id="node-130"></a>

<p align="center"><kbd><img src="assets/b1d58efd6b344e5a34ccbfc1bf7e67f7f66796fa.png" width="100%"></kbd></p>

<br>


<a id="node-131"></a>
## Week Conclusion

<br>


<a id="node-132"></a>
## Lo.re: Gradient

<br>

<a id="node-133"></a>

<p align="center"><kbd><img src="assets/45cf04b389a6be9db29ad9b2c785423ff0ae731e.png" width="100%"></kbd></p>

<br>

<a id="node-134"></a>

<p align="center"><kbd><img src="assets/1dc40e926f793e6aaf15c86999de198dda7b0703.png" width="100%"></kbd></p>

<br>

<a id="node-135"></a>

<p align="center"><kbd><img src="assets/fc04b43fe8824cc190a28bcfe020110a9a4d6f99.png" width="100%"></kbd></p>

<br>

<a id="node-136"></a>

<p align="center"><kbd><img src="assets/7e2015a95fd40b2f42f9927ea098012bd03b6896.png" width="100%"></kbd></p>

<br>

<a id="node-137"></a>

<p align="center"><kbd><img src="assets/04077da779de7301a2058030b235fc6e88a74bbd.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/fe798005ecbb4182fa259e0ac1724e3b40107987.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ff06551d97d3feb314181c2a5739b4187a801851.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/04077da779de7301a2058030b235fc6e88a74bbd.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/fe798005ecbb4182fa259e0ac1724e3b40107987.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ff06551d97d3feb314181c2a5739b4187a801851.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7a5d4fc94a3d85f56c14f2c1dd5e7554d2670acf.png" width="100%"></kbd></p>

> [!NOTE]
> Tự triển khai

<br>


<a id="node-138"></a>
## Quiz: Log.re

<br>


<a id="node-139"></a>
## Programming Assignment: Log.re

<br>


<a id="node-140"></a>
### Welcome to week one of this specialization. You will learn about

> [!NOTE]
> Welcome to week one of this specialization. You will learn about
> logistic regression. Concretely, you will be implementing logistic
> regression for sentiment analysis on tweets. Given a tweet, you
> will decide if it has a positive sentiment or a negative one.
> Specifically you will:
>
> • Learn how to \\/extract features\\/ for logistic regression given
> some text
>
> • Implement \\/**logistic regression from scratch**\\/
>
> • Apply logistic regression on a \\/**natural language processing
> task**\\/
>
> • \\/**Test**\\/ using your logistic regression
>
> • Perform \\/**error analysis**\\/

<br>


<a id="node-141"></a>
#### Import Functions and Data

<br>

<a id="node-142"></a>

<p align="center"><kbd><img src="assets/080480968103e246f524586e197bd141f89c0003.png" width="100%"></kbd></p>

<br>

<a id="node-143"></a>

<p align="center"><kbd><img src="assets/c90d160639383be8a12fd877276dd5fa97480b3a.png" width="100%"></kbd></p>

<br>

<a id="node-144"></a>

<p align="center"><kbd><img src="assets/1a662400151b5565ca3aa961f87db2985cedad96.png" width="100%"></kbd></p>

<br>

<a id="node-145"></a>

<p align="center"><kbd><img src="assets/83e619c76088a15ad21dd42e0e9c0444cc3ac6c5.png" width="100%"></kbd></p>

<br>

<a id="node-146"></a>

<p align="center"><kbd><img src="assets/2858a9d02592bbfdb292731e4735e4fb6de15209.png" width="100%"></kbd></p>

<br>


<a id="node-147"></a>
#### 1 - Logistic Regression

<br>


<a id="node-148"></a>
#### 1.1 - Sigmoid

<br>

<a id="node-149"></a>

<p align="center"><kbd><img src="assets/ba3b3f90b099ad6b62ea9ded8fd1ad294dee0ae9.png" width="100%"></kbd></p>

<br>


<a id="node-150"></a>
#### Exercise 1 - sigmoid (UNQ_C1)

<br>

<a id="node-151"></a>

<p align="center"><kbd><img src="assets/2dbf0c3e80b5dd66c700a0536d8527c1844533be.png" width="100%"></kbd></p>

<br>

<a id="node-152"></a>

<p align="center"><kbd><img src="assets/c593a90135907fa0af6a3185e440730d7902eb24.png" width="100%"></kbd></p>

<br>


<a id="node-153"></a>
#### 1.2 - Cost function and Gradient

<br>

<a id="node-154"></a>

<p align="center"><kbd><img src="assets/601d383e30ba7dc6463059f1dccf6d7769213f6a.png" width="100%"></kbd></p>

<br>

<a id="node-155"></a>

<p align="center"><kbd><img src="assets/41cf0109bd3657a393f5d58a6f5368cd94fb8a9d.png" width="100%"></kbd></p>

<br>


<a id="node-156"></a>
#### Exercise 2 - gradientDescent (UNQ_C2)

<br>

<a id="node-157"></a>

<p align="center"><kbd><img src="assets/51d5f7bebe27c793a45fe54526f4f88e18491494.png" width="100%"></kbd></p>

<br>

<a id="node-158"></a>

<p align="center"><kbd><img src="assets/5ee7d7d0e6511c4f7dd0b1ff1d00a8b51c60666c.png" width="100%"></kbd></p>

<br>

<a id="node-159"></a>

<p align="center"><kbd><img src="assets/a0de94da1645ab913ea03b1ad0bb27edf3c1ead5.png" width="100%"></kbd></p>

<br>


<a id="node-160"></a>
#### 2 - Extracting the Features

<br>


<a id="node-161"></a>
#### Exercise 3 - extract_features (UNQ_C3)

<br>

<a id="node-162"></a>

<p align="center"><kbd><img src="assets/3154472180f5116c1ebcd6b2431fdbda0098ad43.png" width="100%"></kbd></p>

<br>

<a id="node-163"></a>

<p align="center"><kbd><img src="assets/e115bbb1aabe865810118600f853468a83a5c685.png" width="100%"></kbd></p>

> [!NOTE]
> Phải dùng get để còn handle case nếu
> word ko có trong dictionary

<br>

<a id="node-164"></a>

<p align="center"><kbd><img src="assets/a76149d7c24e4949555d0b279c15bb5ac2efd918.png" width="100%"></kbd></p>

<br>


<a id="node-165"></a>
#### 3 - Training Your Model

<br>

<a id="node-166"></a>

<p align="center"><kbd><img src="assets/ab87155700ef6cc4886ed4edbffe297ad3d9f3cc.png" width="100%"></kbd></p>

<br>


<a id="node-167"></a>
#### 4 - Test your Logistic Regression

<br>


<a id="node-168"></a>
#### Exercise 4 - predict_tweet (UNQ_C4)

<br>

<a id="node-169"></a>

<p align="center"><kbd><img src="assets/39ef9d4ea499a1307010f7baa07e049439875b60.png" width="100%"></kbd></p>

<br>

<a id="node-170"></a>

<p align="center"><kbd><img src="assets/12af81fcc5a3f113b4f2aa576eb6a5831119af27.png" width="100%"></kbd></p>

<br>


<a id="node-171"></a>
#### 4.1 - Check the Performance using the Test Set

<br>

<a id="node-172"></a>

<p align="center"><kbd><img src="assets/b12cfd51014fc62f517785528ecca645b7704490.png" width="100%"></kbd></p>

<br>


<a id="node-173"></a>
#### Exercise 5 - test_logistic_regression (UNQ_C5)

<br>

<a id="node-174"></a>

<p align="center"><kbd><img src="assets/048bdf7d484637dcf92e4c80f805eba9b2891145.png" width="100%"></kbd></p>

<br>


<a id="node-175"></a>
#### 5 - Error Analysis

<br>

<a id="node-176"></a>

<p align="center"><kbd><img src="assets/e15b4e024495463759612d8fa69913524929f4a3.png" width="100%"></kbd></p>

<br>

<a id="node-177"></a>

<p align="center"><kbd><img src="assets/9ba65d155751bb713015ddef128ac277542d312f.png" width="100%"></kbd></p>

<br>


<a id="node-178"></a>
#### 6 - Predict with your own Tweet

<br>

<a id="node-179"></a>

<p align="center"><kbd><img src="assets/e97a84d156ed8636a75c0f400aad3eaa1ef4db28.png" width="100%"></kbd></p>

<br>


<a id="node-180"></a>
## Andrew Ng & Chris Manning

<br>

