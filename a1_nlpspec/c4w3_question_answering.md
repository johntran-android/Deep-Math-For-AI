# C4w3 - Question Answering

📊 **Progress:** `119` Notes | `197` Screenshots

---

Explore transfer learning with state-of-the-art models like T5 and BERT, then build a 
model that can answer questions.

Learning Objectives

 • Gain intuition for how transfer learning works in the context of NLP
 • Identify two approaches to transfer learning
 • Discuss the evolution of language models from CBOW to T5 and Bert
 • Fine-tune BERT on a dataset
 • Implement context-based question answering with T5
 • Interpret the GLUE benchmark

<a id="node-3166"></a>
## Week 3 Overview

<br>


<a id="node-3167"></a>
### Here are the main ideas extracted from the lecture text in numerical order:

> [!NOTE]
> Here are the main ideas extracted from the lecture text in numerical order:
>
> 1. Introduction to**transfer learning** as a **new concept** in the course, which **improves results**
> and**speeds up training**.
>
> 2. Discussion of q**uestion answering**, both **context-based** and **closed book question
> answering**.
>
> 3. Highlighting the importance of **innovations in training methods**for improving
> performance.
>
> 4. Comparison of**classical training to transfer learning**, emphasizing **the use of pre-trained
> model weights.**
>
> 5. Demonstrating the **application of transfer learning to various tasks**, such as **sentiment
> classification** and **question answering**.
>
> 6. Explanation of **BERT** and its use of **bi-directional context.**
>
> 7. Comparison of **single task models to multi-task models using T5**.
>
> 8. Emphasis on **the importance of data size in transfer learning**, with examples of dataset
> sizes.
>
> 9. **Desirable goals for transfer learning**, including **reducing training time**, **improving
> predictions, and needing less data.**
>
> 10. Excitement for the upcoming exploration of transfer learning in the next video.

<br>

<a id="node-3168"></a>

<p align="center"><kbd><img src="assets/97902bfc8185097fd557abe7d1c2972de4458b64.png" width="100%"></kbd></p>

  <br>

<a id="node-3169"></a>

<p align="center"><kbd><img src="assets/f8848108e4a6263f2bba0f59cc031ad9a9892c28.png" width="100%"></kbd></p>

  <br>

<a id="node-3170"></a>

<p align="center"><kbd><img src="assets/12c8d8c9fc0e271ee8a2c9a1b6f5d3705432d9dd.png" width="100%"></kbd></p>

  <br>

<a id="node-3171"></a>

<p align="center"><kbd><img src="assets/d1e3b8c1f2c67288aaac43a7ca48c7f7c4e855a9.png" width="100%"></kbd></p>

  <br>

<a id="node-3172"></a>

<p align="center"><kbd><img src="assets/001cd961870babd222e5df699906a3140130c693.png" width="100%"></kbd></p>

  <br>

<a id="node-3173"></a>

<p align="center"><kbd><img src="assets/370342d4b8b953ab6ce4901bdd57015828211770.png" width="100%"></kbd></p>

  <br>

<a id="node-3174"></a>

<p align="center"><kbd><img src="assets/79ea358ee708b30c3245ef060d279e1c3062952a.png" width="100%"></kbd></p>

  <br>

<a id="node-3175"></a>

<p align="center"><kbd><img src="assets/44ca071e40844886e980b4e825ad59c31132daed.png" width="100%"></kbd></p>

  <br>

<a id="node-3176"></a>

<p align="center"><kbd><img src="assets/4fea813ac7509cd8a49faa4658bde835469bba59.png" width="100%"></kbd></p>

  <br>

<a id="node-3177"></a>

<p align="center"><kbd><img src="assets/717aa73fe2247e5ba02d679d54c65bfe6374b74a.png" width="100%"></kbd></p>

  <br>

<a id="node-3178"></a>

<p align="center"><kbd><img src="assets/9b64c3032197fd1b5e7c1c17780a0529c85458a6.png" width="100%"></kbd></p>

  <br>


<a id="node-3179"></a>
## Transfer Learning In NLP

<br>


<a id="node-3180"></a>
### Here are the main ideas extracted from the lecture text in numerical order:

> [!NOTE]
> Here are the main ideas extracted from the lecture text in numerical order:
>
> 1. Introduction to the lecture topics, including transfer learning with the full transformer, 
> **BERT** (Bidirectional Encoder Representation for Transformers), and the **T5** model.
>
> 2. Explanation of what**transfer learni**ng is and its relevance to NLP tasks.
>
> 3. Overview of **two basic forms**of transfer learning: **feature-based learning** and **fine-
> tuning.**
>
> 4. Discussion of **pre-trained data** and **pre-training tasks**, such as language modeling.
>
> 5. Exploration of**general-purpose learning**, including **word embeddings** and their 
> application to translation tasks.
>
> 6. Comparison between**feature-based** and **fine-tuning approaches**with visual examples.
>
> 7. Detailed explanation of**fine-tuning**, including how it can be added to a model and its 
> role in downstream tasks.
>
> 8. Emphasis on the significant **impact of data on model performance**, with examples 
> showing the relationship between data size and outcomes.
>
> 9. Explanation of the **availability of labeled and unlabeled data** and **their relevance in self-
> supervised tasks**.
>
> 10. Illustration of **self-supervised learning through language modeling**, using **unlabeled 
> data** to create **input features and targets.**
>
> 11. Discussion of fine-tuning a pre-trained model for various downstream tasks like 
> **translation, summarization, and question answering**.
>
> 12. Summary of key points, including the use of transfer learning for feature-based or 
> fine-tuning approaches, the importance of data, and the role of pre-training tasks.
>
> 13. Mention of the advantages of transfer learning.
>
> These points provide an overview of the lecture's main concepts and topics related to 
> transfer learning in NLP.

<br>

<a id="node-3181"></a>

<p align="center"><kbd><img src="assets/019140e046190ba7748c59bc9bcf000466fafa66.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là **Transfer learning** có 2 dạng: **Feature-bases** ví dụ
> word embedding được tạo ra từ việc training model ví dụ
> như CBOW. **Fine-tuning** thì là dùng pre-trained model và
> thay đổi (tweak) weights của nó một chút để dùng nó cho
> bài toán của mình.

  <br>

<a id="node-3182"></a>

<p align="center"><kbd><img src="assets/26b26f99a27540c2a95a9f4932c67d57e3d6f478.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là nói về cái 'kiểu' Transfer learning thứ nhất
> khi dùng ví dụ như CBOW model để training Word
> Embeddings. Rồi dùng word embedding đó để
> training Translation model.

  <br>

<a id="node-3183"></a>

<p align="center"><kbd><img src="assets/b681a5592ab8a0f9c87c37901718662fe491d11b.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là với **feature-based** transferred
> learning thì ta sẽ sử dụng features của pre-trained
> model. Còn với **Fine-tuning**, thì ta sử dụng bản
> thân model cho một task khác.

  <br>

<a id="node-3184"></a>

<p align="center"><kbd><img src="assets/d5171711295cf318967ed47c49a861f72f6904de.png" width="100%"></kbd></p>

> [!NOTE]
> Ví dụ, pre-train model dự đoán movies reviews sau đó
> freeze mọi weights layer của nó, và thêm FF layer ở cuối và
> train nó cho bài toán Course reviews.

  <br>

<a id="node-3185"></a>

<p align="center"><kbd><img src="assets/22a77d49d0d8e49cd34efd9ee9dd347a1ac6cbc4.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là với pre-train model, thì
> càng được train trên bộ data lớn
> thì model càng tốt.

  <br>

<a id="node-3186"></a>

<p align="center"><kbd><img src="assets/e75121fa24ed0099a50e72ee7989406eebc5fbca.png" width="100%"></kbd></p>

> [!NOTE]
> Ý nói thường ta có nhiều
> unlabeled data hơn labeled data

  <br>

<a id="node-3187"></a>

<p align="center"><kbd><img src="assets/f8cb03113c21ef24bf581dc778ac96b97a94a91f.png" width="100%"></kbd></p>

> [!NOTE]
> Đây ý nói pre-trained model có thể được train theo kiểu
> un-supervised learning hay self-supervised learning. Rồi
> dùng nó để train tiếp downstream task với labeled data
> supervised learning.

  <br>

<a id="node-3188"></a>

<p align="center"><kbd><img src="assets/380ed6345d873cea04510dfae9f58054f7bf2e4e.png" width="100%"></kbd></p>

> [!NOTE]
> Ví dụ về self-supervised tasks, ta dùng tuy là
> unlabeled data nhưng thực chất là
> self-labeled (che chữ đi, predict)

  <br>

<a id="node-3189"></a>

<p align="center"><kbd><img src="assets/04a5b15ce2c08092532ad9065150fae46634254b.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là dùng một model được pre-trained với task
> khác, train nó với các downstream task khác như
> translation, summarization, Q&A.

  <br>

<a id="node-3190"></a>

<p align="center"><kbd><img src="assets/fda07179c6b93c2227ae52cc3525cc2a0118dcd1.png" width="100%"></kbd></p>

  <br>


<a id="node-3191"></a>
## (reading) Transfer Learning

<br>


<a id="node-3192"></a>
## Elmo, Gpt, Bertm T5

<br>

<a id="node-3193"></a>

<p align="center"><kbd><img src="assets/afdc78401a4cce62bc24de5d97ed697a4764bbd5.png" width="100%"></kbd></p>

<br>

<a id="node-3194"></a>

<p align="center"><kbd><img src="assets/1532e4d2e9d15aab92c8bd13a40aed6b8cb6119d.png" width="100%"></kbd></p>

> [!NOTE]
> Ý là hạn chế của CBOW là **đóng khung context
> của một từ trong phạm vi của một context window**

<br>

<a id="node-3195"></a>

<p align="center"><kbd><img src="assets/478b02db45215e7fb7fac05bac6e8546d8ec6ba9.png" width="100%"></kbd></p>

> [!NOTE]
> Người ta khắc phục việc hạn chế context trong context
> window của CBOW bằng cách dùng **bidirectional
> RNN/LSTM**

<br>

<a id="node-3196"></a>

<p align="center"><kbd><img src="assets/0e73ccc9ab3ba2be1d608eaab58d636a842f7765.png" width="100%"></kbd></p>

> [!NOTE]
> Nhưng với **ELMO** thì nó
> chỉ có **1 direction**

<br>

<a id="node-3197"></a>

<p align="center"><kbd><img src="assets/5028f5805a347e9742169874c25e95346c092128.png" width="100%"></kbd></p>

> [!NOTE]
> Với GPT thì cũng ch**ỉ Uni-directional**- trong **Causal attention**

<br>

<a id="node-3198"></a>

<p align="center"><kbd><img src="assets/31f64ff193146abd735dabee1205b71f0dac241c.png" width="100%"></kbd></p>

> [!NOTE]
> BERT thì nó là
> **Bi-directional**

<br>

<a id="node-3199"></a>

<p align="center"><kbd><img src="assets/c891295d29d48542bb427e7814b3264c1325cc7b.png" width="100%"></kbd></p>

<br>

<a id="node-3200"></a>

<p align="center"><kbd><img src="assets/9bfc1505c51cf4ea67e5d7151b0d20d35f23eff3.png" width="100%"></kbd></p>

<br>

<a id="node-3201"></a>

<p align="center"><kbd><img src="assets/208da97efb36df93345bf4ab3a764998a07fae85.png" width="100%"></kbd></p>

<br>

<a id="node-3202"></a>

<p align="center"><kbd><img src="assets/7084321fc076114b55e8df58bd1abce276c922b8.png" width="100%"></kbd></p>

<br>

<a id="node-3203"></a>

<p align="center"><kbd><img src="assets/ee83d2f48860c2c258f0f8f356c2a92a6bd36eb5.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là với T5 ta có thể multi-task, với các task type
> (ideas của prompt trong LLM) khác nhau, model sẽ
> generate prediction tương ứng

<br>

<a id="node-3204"></a>

<p align="center"><kbd><img src="assets/6841e0321df270e7ccfbcd636dc2a1261f36bd2c.png" width="100%"></kbd></p>

<br>


<a id="node-3205"></a>
## Bidirectional Encoder

> [!NOTE]
> BIDIRECTIONAL ENCODER
> REPRESENTATIONS FROM
> TRANSFORMERS (BERT)

<br>


<a id="node-3206"></a>
### 1. **Introduction to BERT**: **Bidirectional Encoder Representations for Transformers**.

> [!NOTE]
> 1. **Introduction to BERT**: **Bidirectional Encoder Representations for Transformers**.
>
> 2. **Directionality**: BERT p**rocesses inputs from two directions**.
>
> 3. **Architecture**: BERT is a **multi-layer bidirectional transformer** utilizing **positional embeddings**. 
>
> 4. **BERT's Base**: Has 1**2 transformer blocks, 12 attention heads, and 110 million parameters**.
>
> 5. **Framework**: Comprises two main steps: 
>    -**Pre-training**: Training on **unlabeled data**.
>    - **Fine-tuning**: Uses p**re-trained parameters** and **fine-tunes with labeled data**.
>
> 6. **Input and Output**: Starts with**input embeddings** (E_1 to E_n), **goes through transformer 
> blocks**, and **results in outputs (T_1 to T_n).**
>
> 7. ****Pre-training Tasks****:
>    - ****Masked Language Mode**l**: **15% of words are masked**. These masked words are:
>      -**Replaced by a [MASK] token 80%** of the time.
>      -**Replaced by a random token 10%** of the time.
>      - **Left unchanged 10%** of the time.
>    - Objective is to **predict the original token**.
>    - Example given: "After school, Lucas does his [blank] in the library."
>
> 8. ****Prediction Mechanism****: Add a **dense layer** post the **token** and**classify after encoder outputs**. 
> **Multiplication by embedding matrix** transforms them into vocabulary dimension, ending with **softmax**.
>
> 9. ****Next Sentence Prediction****: Determines if two given sentences follow one another in a sequence or not.
>
> 10. **End Note**: The next video will formalize and explain BERT's loss function.

<br>

<a id="node-3207"></a>

<p align="center"><kbd><img src="assets/7b53696affdf64fd486719f73ec60fb4ab40fe37.png" width="100%"></kbd></p>

  <br>

<a id="node-3208"></a>

<p align="center"><kbd><img src="assets/511c81b539036c2c14a37166cfabd01aa18a1c70.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là BERT stand for **Bidirectional Encoder Representation from
> Transformer**.
>
> Kiến trúc của nó bao gồm **Embedding** theo sau bởi **nhiều tầng transformer
> thì cũng chính là nhiều Encoder tạo thành Encoder stack**như trong article
> Series của Ketan có nói.
>
> Người ta gọi transformer block chính là Encoder một bộ gồm các component sau: 
> Embedding + Positional Encoding, Multi-head attention, Skip connection,
> Feed forward và Normalization.
>
> ====
>
> Hai giai đoạn chính của nó là**pre-train với unlabeled data và fine-tuning với 
> specific task**
>
> Theo GPT nói thì nó task thứ nhất là **predict từ được che 'masked' dựa trên
> context** (những từ xung quanh) **ở cả 2 chiều** (nhờ vào **Transformer**
> architecture như đã biết).
>
> Task thứ 2 là n**ó predict next sentence**đại khái là nó sẽ được đưa vào các
> cặp câu sao cho 50% trường hợp là các câu liền kề nhau, và 50%  là các câu ở
> đâu đâu (không liền kề). Mục đích là để model predict liệu  chúng có phải là 2
> câu kế tiếp nhau hay không, giúp model nắm bắt được context - liên quan giữa
> các câu
>
> Sau đó, qua giai đoạn **fine-tuning với specific task nào đó.**

  <br>

<a id="node-3209"></a>

<p align="center"><kbd><img src="assets/01de49055049102c145ff41d863ad7ca4af7e5a9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/01de49055049102c145ff41d863ad7ca4af7e5a9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/be317c9deffac98662ccebcb283baf5c65ffa6b0.png" width="100%"></kbd></p>

  <br>

<a id="node-3210"></a>

<p align="center"><kbd><img src="assets/c42f504018fa1fd0da470464e5dcbf2d223ca65d.png" width="100%"></kbd></p>

> [!NOTE]
> Kiến trúc của BERT thật ra **y như ta đã học với
> Transformer** thì **BERT_base** có **12 transformer blocks**,
> **12 attention heads và 110 triệu params**.
>
> Các LLM sau này như GPT-3 cũng được xây dựng dựa trên
> kiến trúc tương tự nhưng có nhiều params hơn

  <br>

<a id="node-3211"></a>

<p align="center"><kbd><img src="assets/698e7f8789db174830db26466ce0fb5222c4883c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/698e7f8789db174830db26466ce0fb5222c4883c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/aed90459707a48a606dc9d15ddacb501d56e516b.png" width="100%"></kbd></p>

> [!NOTE]
> Ổng nói gì đó đại khái liên quan đến **cách triển khai việc
> pre-train BERT model với unlabeled data**. Bằng cách **chọn một tỉ
> lệ những từ được 'masked' (randomly) để model predict.**
>
> Cụ thể là**15%** tokens được chọn randoms, trong đó sẽ có **80%
> được mask**. **10% được replace với token khác** randomly và
> **10% giữ nguyên.**

  <br>

<a id="node-3212"></a>

<p align="center"><kbd><img src="assets/599ea71cb4d7201f5fe8984d3fae230cdaa4d7b9.png" width="100%"></kbd></p>

> [!NOTE]
> Certainly! BERT (Bidirectional Encoder Representations from Transformers) is a transformative
> approach in the realm of natural language processing (NLP), and it's fundamentally based on the
> Transformer architecture. Let's delve into its architecture and pre-training process:
>
> ### BERT Architecture:
>
> 1. **Transformer Architecture**: BERT's architecture is built upon the Transformer model,
> specifically the encoder part of the Transformer. The Transformer model, originally introduced in the
> "Attention is All You Need" paper, uses attention mechanisms to draw global dependencies between
> input and output.
>
> 2. **Bidirectional Context**: Unlike traditional language models that predict the next word in a
> sequence (unidirectional), BERT is designed to consider both left and right contexts in all layers,
> making it bidirectional.
>
> 3. **Multiple Layers**: BERT comes in two sizes - **BERT-Base and BERT-Large.** BERT-Base has 12
> layers (**transformer blocks**), 768 hidden units, and 1**2 attention heads**, summing to 110M
> parameters. BERT-Large has 24 layers, 1024 hidden units, and **16 attention heads**, amounting to
> 340M parameters.
>
> 4. ****Positional Encoding****: Since the Transformer doesn't have a sense of order of words, positional
> encodings are added to the embeddings at the bottom of the model to give it some information
> about the relative positions of words.
>
> ### BERT Pre-training Process:
>
> BERT's pre-training is performed on a large corpus of text. The model is trained on a combined
> dataset of BooksCorpus (800M words) and English Wikipedia (2,500M words). Two main tasks are
> used for this:
>
> 1. ****Masked Language Model (MLM)****:
>
> - **Randomly masking out words from a sentence and asking the model to predict the masked word**.
>
> - For example, for the sentence "I love to read books", a possible masking might be "I love to
> [MASK] books", and BERT tries to predict "read" for the [MASK] token.
>
> - Around 15% of the words in each sequence are chosen to be masked.
>
> 2. ****Next Sentence Prediction (NSP)****:
>
> - Given two sentences, **A and B, the model is trained to predict if B comes after A in the corpus**.
>
> - This helps BERT **understand relationships between sentences and tackle tasks like
> question-answering** where understanding the context across sentences is vital.
>
> - For training, **50%**of the inputs are a **pair in which the second sentence is the subsequent
> sentence in the original document**, while in the other **50%, it's a random sentence**from the corpus.
>
> After the pre-training phase, BERT can be**fine-tuned on a specific task using a modest amount of
> labeled data** by adding an additional output layer and training on the downstream task.
>
> In summary, BERT's architecture and pre-training strategy have been pivotal in its ability to achieve
> state-of-the-art performance on numerous NLP benchmarks. Its bidirectional context and
> Transformer-based design, combined with the comprehensive pre-training tasks, enable it to
> capture intricate language patterns and relationships.

> [!NOTE]
> Certainly! The term "transformer blocks" refers to the repeated layers/modules in the
> Transformer architecture. To grasp the concept of transformer blocks, we need to delve
> into the inner workings of the Transformer model, particularly the encoder segment.
>
> Each transformer block in BERT (which uses only the encoder part of the original
> Transformer model) consists of the following components:
>
> 1. **Multi-Head Self-Attention Mechanism**:
>
> - **Attention Mechanism**: At its core, the attention mechanism allows the model to focus
> on different parts of the input text, to varying degrees, based on the given context.
>
> - **Self-Attention**: In self-attention, the model computes the attention scores using the
> same input sequence for keys, values, and queries. It helps the model to focus on
> different words within the same input.
>
> - **Multi-Head Attention**: Instead of having a single set of attention weights, the
> multi-head mechanism has multiple sets, allowing the model to focus on different parts of
> the input for different tasks or reasons. The outputs of these multiple heads are
> concatenated and linearly transformed.
>
> 2. **Position-wise Feed-Forward Networks**:
>
> - After the multi-head attention layer, the transformer block contains feed-forward neural
> networks that are applied position-wise, i.e., independently to each position.
>
> - These networks consist of two linear transformations with a ReLU activation in between.
>
> 3. **Residual Connection**:
>
> - Each sub-layer (like multi-head attention or feed-forward neural network) in the
> transformer block has a residual connection around it followed by layer normalization.
>
> - This means the output of the sub-layer is added to its input, which helps in avoiding the
> vanishing gradient problem and allows for deeper models.
>
> 4. **Layer Normalization**:
>
> - After the residual connection, layer normalization is applied. It's a normalization method
> where the mean and variance are computed across the features, and it helps stabilize
> and speed up the training.
>
> 5. **Positional Encoding**:
>
> - Since the Transformer model doesn't inherently understand the sequential order of input
> tokens (because it processes all tokens in parallel), positional encodings are added to the
> embeddings at the start to provide the model with positional context. This isn't unique to
> each transformer block but is crucial to the model's architecture.
>
> In BERT and other transformer-based architectures, these blocks are stacked on top of
> one another multiple times. For instance, BERT-Base uses 12 such transformer blocks,
> while BERT-Large uses 24.
>
> To understand transformer blocks deeply, visual diagrams and hands-on experimentation
> can be immensely helpful. They provide an intuitive sense of data flow and the
> transformations happening within the block.

  <br>


<a id="node-3213"></a>
## Bert Objective

<br>

<a id="node-3214"></a>

<p align="center"><kbd><img src="assets/4aa3f68aa35684202d49eb06c4f51820e2b24106.png" width="100%"></kbd></p>

<br>

<a id="node-3215"></a>

<p align="center"><kbd><img src="assets/e3e887d9031fc0283ba6c766c6bde3b4adf0148d.png" width="100%"></kbd></p>

> [!NOTE]
> Như vậy đại khái là bên cạnh **Token embedding** (semantic embedding),
> và **Positional embedding**. Ta còn có **Segment embedding** để chứa
> thông tin cho biết từ nào là của câu nào.
>
> **Combine cả 3 lại để thành input của BERT**

<br>

<a id="node-3216"></a>

<p align="center"><kbd><img src="assets/b7eb68c6cb91df15d6852cd875933b7fafde29d8.png" width="100%"></kbd></p>

> [!NOTE]
> Cùng với **[CLS] token** được add vào trước mọi input và **[SEP]**
> token để separate hai câu. Hình thành nên **input**.
>
> Qua model để **predict ra các vị trí bị masked**Hoặc **predict xem 2 câu đưa vào có phải là kế tiếp nhau**trong 
> corpus không

<br>

<a id="node-3217"></a>

<p align="center"><kbd><img src="assets/bcd041cf86a8a449f5c3eaab3747c4a4eefea050.png" width="100%"></kbd></p>

> [!NOTE]
> BERT có 2 objective đó là reduce **Cross Entropy Loss** - bằng
> cách cố predict đúng từ được mask và reduce**Binary Loss**
> bằng cách predict hai câu là kế tiếp nhau trong corpus ban đầu  là
> đúng hay sai (nên mới dùng binary loss)
>
> Theo GPT cái việc train để predict hai câu có kế tiếp nhau hay
> không giúp nó học được kiểu như **hiểu được hai câu có phải là
> dạng hỏi - trả lời hay không**Còn predict masked word đương nhiên là để nó hiểu được yếu tố
> ngữ nghĩa language nói chung

<br>

<a id="node-3218"></a>

<p align="center"><kbd><img src="assets/3b7b64cc38311dad8185fb4e4bdc5a11872614fa.png" width="100%"></kbd></p>

> [!NOTE]
> Alright, let's dive deep into the input representation for BERT and its training process:
> **### Input Representation:**
>
> 1. ****Token Embeddings****: The input text is first tokenized. BERT uses **WordPiece tokenization**, which breaks words
> into commonly occurring subwords or characters. For example, "unaffordable" might be tokenized into ["un", "##aff", "
> ##ord", "##able"]. Each token is then mapped to a vector using an embedding lookup.
>
> 2. ****Segment Embeddings****: Since BERT can take two sentences as input for tasks like Next Sentence Prediction
> (NSP), segment embeddings are used to differentiate between the two sentences. If a token belongs to the first
> sentence, it gets a segment embedding `A`, and if it belongs to the second sentence, it gets segment embedding `B`.
>
> 3. ****Positional Embeddings****: Transformers do not have a built-in sense of order for sequences. To counter this,
> positional embeddings are added to provide information about a token's position in a sequence. BERT uses fixed
> positional embeddings to handle sequences up to a certain length (e.g., 512 tokens).
>
> The final input representation for each token is the sum of its token embedding, segment embedding, and positional
> embedding. This combined embedding is fed into the BERT architecture.
>
> **### Training Process:**
>
> BERT's training process comprises two main phases: pre-training and fine-tuning.
>
> **#### 1. Pre-training:**
>
> This phase involves training on a massive amount of unlabeled data over the following tasks:
>
> - **Masked Language Model (MLM)**:   - Randomly 15% of the tokens in the input are masked.   - BERT then tries to
> predict the original identity of the masked words, based on the context provided by the non-masked words.
>
> - **Next Sentence Prediction (NSP)**:   - BERT is provided pairs of sentences and must predict if the second
> sentence in the pair is the subsequent sentence from the original text.   - This task enables BERT to learn
> relationships between sentences.
>
> BERT is pre-trained on a combination of BooksCorpus (800M words) and English Wikipedia (2,500M words).
> **#### 2. Fine-tuning:**
>
> Once pre-training is complete, BERT can be fine-tuned on a specific task with a relatively small amount of labeled
> data.
>
> - A task-specific layer is added on top of the pre-trained BERT model.
> - The entire model (BERT + task-specific layer) is trained on the downstream task.
> - Examples of downstream tasks include text classification, named entity recognition, question-answering, etc.
>
> For fine-tuning, the general process is:
>
> 1. Load the pre-trained BERT model.
> 2. Add an additional output layer specific to the task (e.g., a dense layer for classification).
> 3. Train the entire model on the downstream task's data.
>
> During fine-tuning, all layers are slightly adjusted to better suit the specific task, leveraging the knowledge BERT
> gained during its pre-training phase.
>
> This two-step process—pre-training on a large corpus and then fine-tuning on a specific task—allows BERT to
> generalize well across a range of tasks by first learning a broad understanding of language and then adapting that
> knowledge to specific tasks.

<br>


<a id="node-3219"></a>
## Bert Objective (reading)

<br>

<a id="node-3220"></a>

<p align="center"><kbd><img src="assets/98cc80a9413ed57831440c1b0ccbb19aecfec93d.png" width="100%"></kbd></p>

<br>

<a id="node-3221"></a>

<p align="center"><kbd><img src="assets/74d3e3a25c4f2bade232d8da93dbdc761664c5c8.png" width="100%"></kbd></p>

> [!NOTE]
> Hiểu đại khái là nó bố trí như này để**train nhiều loại task khác nhau** từ
> question answering đến sentiment analysis.
>
> Ví dụ nếu là **sentiment analysis** thì **câu sau để trống**. Chưa hiểu rõ lắm
> nhưng đại khái là vậy

<br>

<a id="node-3222"></a>

<p align="center"><kbd><img src="assets/0b0a4d1c0886ba03e4743fd3f9e8fe88f86740b4.png" width="100%"></kbd></p>

<br>


<a id="node-3223"></a>
## Fine Tuning Bert

<br>

<a id="node-3224"></a>

<p align="center"><kbd><img src="assets/0ef5567eb7dacf32afe1555eab436a19fed8f6f7.png" width="100%"></kbd></p>

> [!NOTE]
> Thì như nói ở bài trước,**tuỳ specific task được fine-tune** mà
> sentence #1 và sentence #2 sẽ khác nhau. Nếu là NER -
> **Name Entity Recognition** thì là **Sentences và Tags**,...

<br>

<a id="node-3225"></a>

<p align="center"><kbd><img src="assets/1d848f576888447f056dcf05a3f17e8fce7f4828.png" width="100%"></kbd></p>

<br>

<a id="node-3226"></a>

<p align="center"><kbd><img src="assets/aadaf53f03084dfbd3780dd7a8b5471272333096.png" width="100%"></kbd></p>

<br>

<a id="node-3227"></a>

<p align="center"><kbd><img src="assets/7d6ffc1f140e6c349daaa772e74635a259a870b1.png" width="100%"></kbd></p>

> [!NOTE]
> That's it. Đại khái là **quá trình fine-tuning** với các **specific task
> khác nhau** thì **input vào sentence 1 và 2 sẽ khác nhau tương
> ứng**

<br>


<a id="node-3228"></a>
## (reading) Fine Tuning Bert

<br>


<a id="node-3229"></a>
## Transformer: T5

<br>

<a id="node-3230"></a>

<p align="center"><kbd><img src="assets/75853aa1ae7d56880d46865abc968a35a8d383a9.png" width="100%"></kbd></p>

<br>

<a id="node-3231"></a>

<p align="center"><kbd><img src="assets/02b0f9362144d08627e83e146c951377f9c8d05e.png" width="100%"></kbd></p>

> [!NOTE]
> One of the major techniques that allowed the T5 model to reach state of the art is the
> concept of masking:
>
> For example, you represent the “for inviting” with <X> and last with <Y> then the model
> predicts what the X should be and what the Y should be. This is exactly what we saw in
> the BERT loss. You can also mask out a few positions, not just one. The loss is only on
> the mask for BERT, for T5 it is on the target.

> [!NOTE]
> Đại khái là mấy cái LLM này đều được pre-train
> kiểu self-supervised với unlabeled data.

<br>

<a id="node-3232"></a>

<p align="center"><kbd><img src="assets/e2379b4e9ec9a81ed0d0ad194063f2b4ad56f0a8.png" width="100%"></kbd></p>

> [!NOTE]
> So we start with the basic encoder-decoder representation.There you have a fully visible
> attention in the encoder and then causal attention in the decoder.  So light gray lines
> correspond to causal masking. And dark gray lines correspond to the fully visible masking.In
> the middle we have the language model which consists of a single transformer layer stack.
> And it's being fed the concatenation of the inputs and the target. So it uses causal masking
> throughout as you can see because they're all gray lines. And you have X1 going inside, you
> get X2, X2 goes into the model and you get X3 and so forth.To the right, we have prefix
> language model which corresponds to allowing fully visible masking over the inputs as you
> can see with the dark arrows. And then causal masking in the rest.

> [!NOTE]
> Kiến trúc chúng nó có thể khác nhau ở chỗ Encoder-Decoder
> hay chỉ Encoder / chỉ Decoder. Còn cơ bản vẫn là cấu thành
> bởi Transformer block unit.

<br>

<a id="node-3233"></a>

<p align="center"><kbd><img src="assets/dfa5c44cbdc4b6f1b126d7a17889f1ebb9156ece.png" width="100%"></kbd></p>

<br>

<a id="node-3234"></a>

<p align="center"><kbd><img src="assets/bbd2fc41d1993a7a739792168bfc7e0918b1f583.png" width="100%"></kbd></p>

<br>


<a id="node-3235"></a>
## (reading) Transformer T5

<br>


<a id="node-3236"></a>
## Multi-task Training Strategy

<br>

<a id="node-3237"></a>

<p align="center"><kbd><img src="assets/ac294ffcfdf316661fbbad502e339758d3cc2925.png" width="100%"></kbd></p>

> [!NOTE]
> Có nhiều cái mai
> phải search

<br>

<a id="node-3238"></a>

<p align="center"><kbd><img src="assets/faec5cf6dd16ce425cb1970bac63a0865f952e48.png" width="100%"></kbd></p>

<br>

<a id="node-3239"></a>

<p align="center"><kbd><img src="assets/6b04c932f3518031cb4ffa5e717895a139b8aaf8.png" width="100%"></kbd></p>

<br>

<a id="node-3240"></a>

<p align="center"><kbd><img src="assets/ecb1881495e1ba341e9c755a1e2df784c45d60a6.png" width="100%"></kbd></p>

<br>

<a id="node-3241"></a>

<p align="center"><kbd><img src="assets/dff044b06b9d9a74c5429c6b5b0be6c35716053e.png" width="100%"></kbd></p>

<br>

<a id="node-3242"></a>

<p align="center"><kbd><img src="assets/4eb9b53745c3e8cf3c1cf3452750d4bc5fe4e776.png" width="100%"></kbd></p>

<br>

<a id="node-3243"></a>

<p align="center"><kbd><img src="assets/6f83cff5ed70657ebe3c411d831fa4a4896b5b05.png" width="100%"></kbd></p>

<br>


<a id="node-3244"></a>
## (reading) Multi-task Training

> [!NOTE]
> (READING) MULTI-TASK TRAINING
> STRATEGY

<br>


<a id="node-3245"></a>
## Glue Bench-mark

<br>

<a id="node-3246"></a>

<p align="center"><kbd><img src="assets/d8b4b6ba108647a962ff7a6479559d6aa938c78e.png" width="100%"></kbd></p>

> [!NOTE]
> GLUE scores là chỉ số đánh giá mức độ hiểu
> ngôn ngữ của model, bao gồm nhiều dataset
> trên nhiều vấn đề khác nhau.

<br>

<a id="node-3247"></a>

<p align="center"><kbd><img src="assets/5f7aa746c7fafaddf4735950be6ec71964348863.png" width="100%"></kbd></p>

<br>

<a id="node-3248"></a>

<p align="center"><kbd><img src="assets/f7d5170f6b7cc6b06c51520c75e15f4668289908.png" width="100%"></kbd></p>

> [!NOTE]
> GLUE dùng để đánh giá model trong quá trình research, nó có tính
> agnostic khi không care model cụ thể là gì. Và nó giúp transfer
> learning khi model evaluate bởi GLUE có thể giúp dẫn dắt việc tìm
> based model (pretrained) phù hợp

<br>


<a id="node-3249"></a>
## (reading) Glue Benchmark

<br>

<a id="node-3250"></a>

<p align="center"><kbd><img src="assets/2dc9637c412ddbc9dac0a9396f60ecde8bb5e098.png" width="100%"></kbd></p>

<br>


<a id="node-3251"></a>
## Question Answering

<br>

<a id="node-3252"></a>

<p align="center"><kbd><img src="assets/a22aadf6b2f2f6bbc302afde3ec5b23a4f13b0da.png" width="100%"></kbd></p>

<br>

<a id="node-3253"></a>

<p align="center"><kbd><img src="assets/6ce997f13227c85b7b3b153d343d1663dd04f149.png" width="100%"></kbd></p>

<br>

<a id="node-3254"></a>

<p align="center"><kbd><img src="assets/1956eda90a38175c545c13d57737c210e97e0efc.png" width="100%"></kbd></p>

> [!NOTE]
> Nói sơ về dataset
> sẽ làm trong PA

<br>

<a id="node-3255"></a>

<p align="center"><kbd><img src="assets/c8d507257f23945ac5656bbeec6ff30af4badc3b.png" width="100%"></kbd></p>

> [!NOTE]
> Các bước sẽ làm trong PA. Cơ
> bản là ta dùng pre-trained T5
> model để fine-tuning

<br>


<a id="node-3256"></a>
## Lab: **sentencepiece** And **bpe**

<br>


<a id="node-3257"></a>
### Introduction to

> [!NOTE]
> Introduction to
> Tokenization

<br>

<a id="node-3258"></a>

<p align="center"><kbd><img src="assets/547c04f3c138aff0d3dbdc65b8b2b54f12c0cc4f.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là nói về **tokenization** - quá trình c**huyển input text thành
> các token là các index number** trước khi đưa vào model.
>
> Cũng như là **de-tokenize** - chuyển index numbers thành text lại. Có
> nhiều thử nghiệm để tìm**cách làm hiệu quả nhất, như word,
> characters, phonemes...**

  <br>

<a id="node-3259"></a>

<p align="center"><kbd><img src="assets/c55162592c280a2c85c3f110d1370e0163572d13.png" width="100%"></kbd></p>

> [!NOTE]
> Tuy nhiên các **ngôn ngữ khác nhau lại có quy luật khác nhau**,
> như **tiếng anh có thể dùng khoảng trống** **để split** thành từng
> từ n**hưng tiếng Trung thì không được.**

  <br>

<a id="node-3260"></a>

<p align="center"><kbd><img src="assets/f419a30efa0d6f4de67f2204c3c2ff1a4fe13757.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ngoài vấn đề các ngôn ngữ khác nhau cho những cách tokenize
> khác nhau chứ không thống nhất được, thì còn vấn đề đặt ra đối với việc
> **bộ vocab size nên có kích thước bao nhiêu**.
>
> **Nhiều quá thì tất nhiên là tốt** cho kết quả của model hơn nhưng **lại gây
> vấn đề memory.**
>
> Thì ở đây ta sẽ khám phá **SentencePiece** với **BPE**, một **tokenization
> technique** được sử dụng trong **BERT.**Và **giải thuật pseudocode của
> nó cũng dễ hiểu và dễ làm**

  <br>


<a id="node-3261"></a>
### SentencePiece

> [!NOTE]
> SentencePiece
> Preprocessing

<br>

<a id="node-3262"></a>

<p align="center"><kbd><img src="assets/9591991fb0cabf8a1b27d569e947dfe25c3bc483.png" width="100%"></kbd></p>

> [!NOTE]
> Ngay cả khi dùng unicode để tokenize text cũng gây **vấn đề** **ambiguous**, ở
> đây ta thấy**hai chữ 'é' trông y hệt nhau, nhưng thật ra lại khác nhau**.
>
> Thì việc này được giải quyết bởi **normalization**.

  <br>

<a id="node-3263"></a>

<p align="center"><kbd><img src="assets/05b4a07e775c3a433b381df4d5401427fbfc4503.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là normalization thật sự đã thay đổi "**unicode point**" của 1
> trong hai "é" (cụ thể là cái thứ 2 từ 0x65 0x31 thành 0xe9) từ đó
> đồng nhất hai cái "é" đều cùng một unicode point là "0xe9"
>
> Nói thêm là cái normalization này nó có nhiều side effect hữu ích 
> ví dụ như chuyển kí tự ngoặc kép sang dạng tương đương của ASCII
> tuy có thể làm mất dạng nghiêng

  <br>

<a id="node-3264"></a>

<p align="center"><kbd><img src="assets/4c78a538a6abfdf40f7f77fdaeab6df7e304eec1.png" width="100%"></kbd></p>

> [!NOTE]
> Về cách SentencePiece xử lý vấn đề khoảng trắng bằng cách
> nó replace khoảng trắng bằng "_" để khi "khôi phục" khoảng
> trắng lại thì nó sẽ replace "_" lại thành khoảng trắng, với cách
> này thì những khoảng trắng liên tục nhau sẽ không  bị mất.

  <br>

<a id="node-3265"></a>

<p align="center"><kbd><img src="assets/f6dbc3b6bd4096d77e30b3c01b2b22a01f0d4d43.png" width="100%"></kbd></p>

  <br>

<a id="node-3266"></a>

<p align="center"><kbd><img src="assets/7547797f48c9f5bdb0031ecd2e8978f3dbc13394.png" width="100%"></kbd></p>

  <br>


<a id="node-3267"></a>
### BPE Algorithm

<br>

<a id="node-3268"></a>

<p align="center"><kbd><img src="assets/111cb798fd30d1922ab8d5f26dbd6fc1f614052f.png" width="100%"></kbd></p>

> [!NOTE]
> Nãy giờ kiểu như nói về **cách mà SentencePiece hoạt động khi thực
> hiện việc tokenization**. Bây giờ mình sẽ lấy data, preprocess nó và
> **apply BPE algorithm** - tokenization.
>
> Function dưới đại khái là nhận filepath của file data chứa data json,
> Đầu tiên nó **mở file được chỉ định** bởi filepath với **open(filepath)**và đọc nội dung của file dưới dạng một list các **json-likes strings**.
>
> Sau đó nhờ thư viện **ast = Abstract Syntax Trees**import ở trên để
> dùng function .**literal_eval() của nó giúp convert Json-like string thành
> dạng Python dictionary.**Thì GPT nó nói là cái function này giúp
> convert an toàn hơn, tránh vấn đề "**code injection attacks**"
>
> Tiếp theo, **tạo một list** (texts variable) bằng cách **extracting 'text'
> fields từ mỗi bộ dictionary**, rồi **từ bytes decoding thành dạng UTF-8
> string**.  Để ý ở đây dùng Python **list comprehension**.
>
> Kế tiếp, function**"\ \ ".join(texts)** kiểu như sẽ join mọi text trong
> list lại, nối nhau bởi "\\n\\n" thành ra kết quả có dạng các articles
> separating nhau bởi "\\n\\n"
>
> Cuối cùng nói được **normalize**() bởi **Unicode normalization**
> (NFKC) như đã  thấy ở trên, giúp **ensure consistent character
> representation**. (Không bị tình trạng **mặt chữ in ra thì giống nhau
> nhưng representation thì khác nhau**)
>
> Cuối cùng, normalized text được **ghi vào file có tên 'example.txt'**

> [!NOTE]
> Đại khái là ta sẽ "bắt chước" BPE
> algorithm mà SentencePiece nó
> dùng để tokenize data.

  <br>

<a id="node-3269"></a>

<p align="center"><kbd><img src="assets/88fc59dde676cb0849eb72e1a5a21ddfde22be23.png" width="100%"></kbd></p>

  <br>

<a id="node-3270"></a>

<p align="center"><kbd><img src="assets/eca04e56aa0dfdd9fff0894965de62038ca274c1.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/eca04e56aa0dfdd9fff0894965de62038ca274c1.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/49fc5e3b3118eeaef2db19afd87674bea98cf40a.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là bên trong cái tokenization algorithm, thực chất nó sẽ **tạo một
> dictionary map** **từ - tần suất xuất hiện** của nó. 
>
> Ngoài ra, **mỗi character được
> prepend với một kí tự '_'** để **indicate rằng đó là bắt đầu của một từ**. 
>
> Cuối cùng,
> **các characters được tách ra bởi space** để **BPE algorithm có thể nhóm các
> characters phổ biến nhất** trong dictionary theo một **'greedy fashion'.**
>
> Trong đoạn code dưới, ta thấy họ **tạo Counter**, bỏ vào đó một**list các word**: tạo
> bởi **text.split()** sau đó add **thêm underscore character ('\\u2581' = '_') ở đầu**
>
> Cái Counter sẽ **đếm xem mỗi word xuất hiện bao nhiêu lần.**
>
> Dòng thứ 2, **dùng Python list comprehension** tạo dictionary, map giữa **key-value,**
> Trong đó key là: **Từng kí tự trong word**, **joint với nhau** và **xen ' ' vào giữa**. Ví dụ
> **word = '_want' -> '_ w a n t', '_get' -> '_ g e t'**
>
> Còn value là: **freq = frequency = số lần xuất hiện của từ mà Counter nó đếm
> được.**

  <br>

<a id="node-3271"></a>

<p align="center"><kbd><img src="assets/43388aa9df5176dceb7f780901cf87f717249c12.png" width="100%"></kbd></p>

> [!NOTE]
> CHƯA HIỂU LẮM, liên quan đến vocab size
> là một hyperparam quan trọng ảnh hưởng
> đến chất lượng của quá trình tokenization.

> [!NOTE]
> The provided text is explaining the importance of checking the size of the vocabulary (frequency
> dictionary) when using Byte Pair Encoding (BPE) for text tokenization. Here's a breakdown of the
> explanation:
>
> 1. **BPE and Tokenization**: BPE is a subword tokenization technique used in natural language
> processing (NLP) to **break down words** into **smaller units**, such as **subword pieces**. It's a popular
> approach for **handling out-of-vocabulary words** and **reducing the size of the vocabulary**, which can be
> helpful for NLP models. Tokenization refers to the process of **splitting text into smaller units**, like **words** or
> **subword pieces**.
>
> 2. **Vocabulary Size Matters**: The**size of the vocabulary**(the **number of unique tokens** or **subword
> pieces**) is a **crucial hyperparameter** when using BPE. The vocabulary size determines**how finely
> BPE will break down words into subword pieces**. A**larger vocabulary size**results in **smaller
> subword pieces**, while a s**maller vocabulary size leads to larger subword pieces**.
>
> 3. **Dependence on Vocabulary Size**: The explanation states that BPE depends crucially on the size of
> the vocabulary. In other words, the vocabulary size has a significant impact on how BPE operates.
>
> 4. **Specific Example**: In the specific case mentioned in the explanation, the author is working with a
> trained model and a small dataset. They have observed that to achieve a target vocabulary size of 32,
> 000 (vocab_size), approximately 60% of the 455 most frequent characters need to be merged or
> combined into subword pieces using BPE.
>
> 5. **Reproducing the Vocabulary Size**: The statement "need to be done to reproduce the upper limit of a
> 32K vocab_size" means that, in their experiments, they found that they had to perform a certain number
> of merges (breaking down words into subword pieces) to reach a vocabulary size of 32,000. This allows
> them to control the size of the vocabulary by adjusting the number of merges.
>
> 6. **Corpus-Wide Consideration**: The explanation also emphasizes that this observation applies " over
> the entire corpus of examples." This means that the choice of how many merges to perform is not made
> on a per-word basis but considers the entire dataset. The goal is to find a balance where the vocabulary
> size is manageable while still representing the data effectively.
>
> In summary, the explanation highlights that the vocabulary size is a critical factor in BPE tokenization, and
> it provides specific information about how the author determined the number of merges needed to
> achieve a target vocabulary size in their particular NLP task. Adjusting this hyperparameter can have a
> significant impact on the effectiveness of the tokenization process.

> [!NOTE]
> Vocab size lớn thì subword piece nhỏ và ngược lại vocab size càng nhỏ thì subword
> piece càng lớn
>
> Để hiểu cái này ta lấy phương pháp 1 là cách tokenize theo cấp word, tức 
> là mỗi từ là một token để làm mốc. Theo cách này thì "**in**depen**dent**, depend**ent**,
> depend, insuffici**ent**" thì mỗi từ đều phải có một token 
>
> Thì cách 2 - dùng sub-word ví dụ 'depend', 'in', 'ent' thì vì nó chung cho rất rất
> nhiều từ kiểu vậy cho nên số lượng token cần thiết, hay vocab size sẽ ít hơn so với
> cách 1. 
>
> Cách 3 là dùng sub-word theo kiểu tối đa là thu về cấp kí tự thì ta thấy vocab size 
> chỉ còn có mấy chục.
>
> Thì ý nói là vocab size nó sẽ có một mối liên quan nào đó khiến cách thức bẻ từ tạo 
> subword thay đổi. Hiểu đại khái tới đây thôi

  <br>

<a id="node-3272"></a>

<p align="center"><kbd><img src="assets/13a442ce93d22bf89d6f12875900a9fd944cc614.png" width="100%"></kbd></p>

> [!NOTE]
> Function **get_stats** đại khái là nó**tạo dict để đếm tần suất của các cặp
> symbols liền kề**
>
> Ta thấy nó nhận vocab, như đã biết ở trên là dict giữa key = '_ a p p l e' và số
> lần xuất hiện của nó. Ví dụ:  **{'_ a p p l e' : 5}**
>
> Nó loop trong các tuple (word, freq) đó, **split word ra thành các subword** 
> ví dụ '_ a p p l e' -> '_', 'a', 'p', 'l', 'e'.
>
> Rồi dùng một loop để update vào **pairs dict**cặp **symbols liền kề** - **số lần xuất
> hiện**. Ví dụ: { '_ a': 7,  'a p': 5, 'p p': 4, }
>
> Ở đây symbol đang ở cấp kí tự, nhưng nó có thể là bi-gram, tri-gram.
> Nên pair có thể là {'ap pl' : 3, 'jui ce': 5}
>
> ====
>
> Đại khái về function **get_sentence_piece_vocab()**: Đầu tiên, **dựa vào 'tỉ lệ
> merge' argument,** và **vocab's size** nó tính ra **số  'hành động merge' sẽ diễn ra**.
>
> Bắt đầu **thực hiện các 'hành động merge'** cho đến khi đủ **num_merges**, trong
> đó:
>
> Nó dùng function **get_stats**() ở trên để **tính ra pairs** là bộ dict map các cặp
> subword liền kề với tần suất của nó.
>
> Dòng tiếp theo **max(...)** kiểu như nó **lấy cái có tần suất cao nhất**.
>
> Rồi bỏ vào function **merge_vocab**, trong đây nôm na đại khái là nó sẽ **thay hai
> kí tự liền kề thành 1 subword**.  
>
> Ví dụ:  { '_ **a p** p l e': 5, '_ **a p** p l e j u i c e': 10 }
>
> ->  { '_ **ap** p l e': 5  '_ **ap** p l e j u i c e': 10 }

  <br>

<a id="node-3273"></a>

<p align="center"><kbd><img src="assets/274c36d07ba877631158e42bc9ec8d04413b5b1b.png" width="100%"></kbd></p>

  <br>

<a id="node-3274"></a>

<p align="center"><kbd><img src="assets/0cc9abe7917b35111642440c58237117bc3e7f92.png" width="100%"></kbd></p>

  <br>

<a id="node-3275"></a>

<p align="center"><kbd><img src="assets/a2d8ee448b95c3c79cfc2f8c38ce14502cdc3205.png" width="100%"></kbd></p>

> [!NOTE]
> Kết quả kiểu như các cặp subword
> liền kề mà xuất hiện nhiều sẽ được
> 'gom lại' dần dần.

  <br>


<a id="node-3276"></a>
### Train SentencePiece BPE

> [!NOTE]
> Train SentencePiece BPE
> Tokenizer on Example Data

<br>

<a id="node-3277"></a>

<p align="center"><kbd><img src="assets/880edbe7bc7c210f4e8607dfe3dc41b763ef51f0.png" width="100%"></kbd></p>

> [!NOTE]
> Một ví dụ về **SentencePiece** lib sẽ dùng để tokenize trong P.A tuần này.
> Import và khởi tạo nó với path dẫn đến model (tức là model đã fit với
> bộ dataset, liên hệ như TensorFlow's tokenizer **fit_on_texts**(dataset))
>
> Sử dụng **encode_as_pieces** và **encode_as_ids** để encode/tokenize
> và **decode_pieces** / **decode_ids** để detokenize

  <br>

<a id="node-3278"></a>

<p align="center"><kbd><img src="assets/aaf996ed42adb62449b1a0df38151ed2aca1d8f7.png" width="100%"></kbd></p>

  <br>

<a id="node-3279"></a>

<p align="center"><kbd><img src="assets/7a600b40328e068843efc2e3b29f7402714cb1e0.png" width="100%"></kbd></p>

> [!NOTE]
> Xem một số token đặc biệt của SentencePieces như
> BOS (Beginning of sentence) là -1, Pad là 0 như
> thường lệ, EOS là 1, UNK là 2

  <br>

<a id="node-3280"></a>

<p align="center"><kbd><img src="assets/02c2c2b773d8480761ddb19ede08c95c7bde8a18.png" width="100%"></kbd></p>

> [!NOTE]
> Biết thêm về kí tự \t giúp separate thành khi print.

  <br>

<a id="node-3281"></a>

<p align="center"><kbd><img src="assets/7a5a46eb1f4c91326da174d223f04fde9af40f8e.png" width="100%"></kbd></p>

> [!NOTE]
> Train BPE model trực tiếp từ SentencePiece lib" - Cái này khó hiểu, nhưng nôm
> na là so sánh cái BPE của cái library và cái "sự bắt chước BPE algorithm" mà ta
> làm ở trên.
>
> Kết quả thấy cũng tương đối giống nhau. Nếu có khác là do BPE của
> SentencePiece lib nó còn thực hiện thêm một cái vụ gọi là "priority queue" gì đó
> nữa giúp **"keep track of best pairs".**Và Python nó cũng có cái này, - **heapq** mà ta có thể thử

  <br>


<a id="node-3282"></a>
### Optionally try to implement BPE

> [!NOTE]
> Optionally try to implement BPE
> using a priority queue below

<br>

<a id="node-3283"></a>

<p align="center"><kbd><img src="assets/6fc2474ffad029a2136627530b77164387fc7f16.png" width="100%"></kbd></p>

  <br>


<a id="node-3284"></a>
## (reading) Welcome To Hugging Face

<br>


<a id="node-3285"></a>
## Hugging Face Introduction

<br>


<a id="node-3286"></a>
## Hugging Face I

<br>


<a id="node-3287"></a>
## Hugging Face Ii

<br>


<a id="node-3288"></a>
## Hugging Face Iii

<br>


<a id="node-3289"></a>
## Lab: Question

> [!NOTE]
> LAB: QUESTION
> ANSWERING WITH HF 1

<br>


<a id="node-3290"></a>
### You've seen how to use **BERT**, and other **transformer models** for a wide range of \\*natural

> [!NOTE]
> You've seen how to use **BERT**, and other **transformer models** for a wide range of **natural
> language tasks**, including machine translation, summarization, and question answering.
> **Transformers** have become the **standard model for NLP,** similar to **convolutional models in
> computer vision**. And all started with **Attention**!
>
> In practice, you'll **rarely train a transformer model from scratch**. Transformers tend to be
> very **large**, so they take **time, money, and lots of data** to train fully. Instead, you'll want to
> **start with a pre-trained model and fine-tune it**with your dataset if you need to.
>
> \\_Hugging Face\\_ (🤗) is the best resource for pre-trained transformers. Their **open-source
> libraries** simplify **downloading** and **using transformer models** like**BERT, T5, and GPT-2**.
> And the best part, you can**use them alongside either TensorFlow, PyTorch and Flax**. In this
> notebook, you'll use 🤗 transformers to download and use the **DistilBERT** model for
> question answering.
>
> First, let's install some packages that we will use during the lab.

> [!NOTE]
> Đại khái là ta đã biết BERT và các model dựa trên Transformer. Và vai trò của Transformer
> với NLP giống như Convolutional model với Computer vision vậy
>
> Tuy nhiên việc train một Transformer từ đầu rất tốn kém, thời gian, chi phí và data.
>
> Do đó thường người ta sẽ dùng một base - pretrained model và fine-tune nó với dataset của
> họ.
>
> Thì HuggingFace là một platform rất hữu ích cho việc này khi nó cung cấp các công cụ để
> download các pre-trained model.

<br>

<a id="node-3291"></a>

<p align="center"><kbd><img src="assets/e2879e66125707b8c2db028af6d48bfd485353f8.png" width="100%"></kbd></p>

  <br>

<a id="node-3292"></a>
- **Before fine-tuning a model**, you will look to the **pipelines** from Hugging Face to **use pre-trained transformer models** for **specific tasks**. The transformers library**provides pipelines for popular tasks** like sentiment analysis, summarization, and text generation. A pipeline consists of a **tokenizer**, a **model**, and the **model configuration**. All these are packaged together into an easy-to-use object. Hugging Face makes life easier.  Pipelines are intended **to be used without fine-tuning** and will **often be immediately helpful** in your projects. For example, transformers provides a pipeline for question answering that you can directly use to answer your questions if you give some context. Let's see how to do just that.  You will import pipeline from transformers for creating pipelines.
> [!NOTE]
> Một điểm hay đầu tiên của HuggingFace là chỉ việc search pipeline
> phù hợp với nhu cầu là có thể dùng được ngày (dạng task cần làm
> như sentiment analysis, question answering..)

  <br>

    <a id="node-3293"></a>
    <p align="center"><kbd><img src="assets/c2277d85a83e23fd9827efc60e1d8f8357e09ca5.png" width="100%"></kbd></p>
    > [!NOTE]
    > Ví dụ, import **pipeline**, và dùng nó để load cái pipeline với
    > model**distilBert - base** (như ta đã biết nó là bản distilled của
    > BERT) và dùng với **task question-answering.**

    <br>

    <a id="node-3294"></a>
    <p align="center"><kbd><img src="assets/82a61c432be04ad007ef23b44578eff62264fc7e.png" width="100%"></kbd></p>
    > [!NOTE]
    > Và với pipeline đã load, ta**chỉ việc inference nó với "câu
    > hỏi" mà ta cần hỏi ở dạng text**. **Pipeline** bên trong sẽ có **tokenizer phù
    > hợp để tokenize input** và**inference với model**, cũng như
    > **detokenize model's output**

    <br>

    <a id="node-3295"></a>
    <p align="center"><kbd><img src="assets/099aaa20428087f651d7043fb7763ce5a1c2732e.png" width="100%"></kbd></p>
    > [!NOTE]
    > Ví dụ hỏi nó extract thông tin
    > từ provided content

    <br>

    <a id="node-3296"></a>
    <p align="center"><kbd><img src="assets/19c18482b006cd5c7f9f1213e1c28f0f6f2267ad.png" width="100%"></kbd></p>
    > [!NOTE]
    > Thậm chí có thể hỏi
    > nhiều câu cùng lúc

    <br>

    <a id="node-3297"></a>
    <p align="center"><kbd><img src="assets/8ba0c1939038226cc5705bba4aea3e03a2776fc5.png" width="100%"></kbd></p>
    <br>

    <a id="node-3298"></a>
    <p align="center"><kbd><img src="assets/6196d55046c842315d40fbf58829f36ead479fb0.png" width="100%"></kbd></p>
    > [!NOTE]
    > Cái này ý nói là không phải model luôn
    > trả lời tốt cho mọi câu hỏi.

    <br>

    <a id="node-3299"></a>
    <p align="center"><kbd><img src="assets/55555e148d4826e1107b94e26ce0ab36e0ec2408.png" width="100%"></kbd></p>
    <br>

  <a id="node-3300"></a>
  - It seems like this model is a huge fan of Archie Andrews. It even considers him a superhero!  The example that fooled your question_answerer belongs to the TyDi QA dataset, a dataset from Google for question/answering in diverse languages. To achieve better results when you know that the pipeline isn't working as it should, you need to consider fine-tuning your model.  In the next ungraded lab, you will get the chance to fine-tune the DistilBert model using the TyDi QA dataset.
    > [!NOTE]
    > Do đó, có thể ta cần
    > Fine-tune model

    <br>


<a id="node-3301"></a>
## Lab: Question

> [!NOTE]
> LAB: QUESTION
> ANSWERING WITH HF 2

<br>


<a id="node-3302"></a>
### In the previous Hugging Face ungraded lab, you saw how to **use the pipeline objects** to

> [!NOTE]
> In the previous Hugging Face ungraded lab, you saw how to **use the pipeline objects** to 
> use **transformer models** for NLP tasks. I showed you that the **model didn't output the 
> desired answers** to a series of precise questions for a context related to the history of 
> comic books.
>
> In this lab, you will **fine-tune the model** from that lab to**give better answers** for that type of 
> context. To do that, you'll be using the \\_**TyDi QA dataset**\\_ but on a filtered version with only 
> English examples. Additionally, you will use a lot of the tools that Hugging Face has to 
> offer.
>
> You have to note that, in general, you will**fine-tune general-purpose transformer models** 
> to work for specific tasks. However, **fine-tuning a general-purpose** model can **take a lot of 
> time**. That's why you will be**using the model from the question answering pipeline** in this 
> lab.
>
> First, let's install some packages that you will use during the lab.

> [!NOTE]
> https://colab.research.google.com/drive/1P8COnbYLphJNaW3v8wS1AwpahnV-653A#scrollTo=u2UXutvEvpUj:~:text=In%20the%20previous,during%20the%20lab.

> [!NOTE]
> Đại khái là tiếp tục fine-tune với TyDi QA dataset để cải thiện khả năng
> thực hiện tác Question Answering

<br>

<a id="node-3303"></a>
- Dataset
  <br>

    <a id="node-3304"></a>
    <p align="center"><kbd><img src="assets/2fde6cdc12c51e37eb8dd64ba6169eb1f6bf9ab4.png" width="100%"></kbd></p>
    <br>

    <a id="node-3305"></a>
    <p align="center"><kbd><img src="assets/e5842f445301364327b5aeb17c3fb238ef06877b.png" width="100%"></kbd></p>
    > [!NOTE]
    > Như đã nói, ta sẽ fine-tuning pre-trained distilled BERT model
    >
    > Trong quá trình đó ta sẽ sử dụng 3 lib của HuggingFace là Datasets
    > - giúp load  và access các bộ dataset cũng như là metrics. Tokenizer
    > chịu trách nhiệm preprocessing dataset và transformer cho ta tiếp
    > cận nhiều pre-trained model

    <br>

    <a id="node-3306"></a>
    <p align="center"><kbd><img src="assets/39b1e2dc187e5072a69658901c230ff66483eded.png" width="100%"></kbd></p>
    > [!NOTE]
    > Đại khái là có thể dùng **load_dataset**() để download dataset. Nó
    > support nhiều format như CSV, JSON, text.
    >
    > Ở đây thì người ta **chuẩn bị sẵn bộ dataset bằng cách filter  bộ gốc để
    > chỉ lấy tiếng Anh thôi**. Nên ta sẽ download và dùng **load_from_disk**
    > (thay vì bộ gốc từ**HuggingFace Dataset** với **load_dataset**())

    <br>

    <a id="node-3307"></a>
    <p align="center"><kbd><img src="assets/3dc83235eacc6254b8fe434fd844f1f88a0477cb.png" width="100%"></kbd></p>
    > [!NOTE]
    > Download bộ filtered dataset người ta chuẫn bị sẵn, để trên Google Cloud

    <br>

    <a id="node-3308"></a>
    <p align="center"><kbd><img src="assets/705d0e856a744487b69bc985f79e92741ca7cc24.png" width="100%"></kbd></p>
    <br>

    <a id="node-3309"></a>
    <p align="center"><kbd><img src="assets/f9cef54370962db32331d771e5bea163b237700e.png" width="100%"></kbd></p>
    > [!NOTE]
    > Load data from disk

    <br>

    <a id="node-3310"></a>
    <p align="center"><kbd><img src="assets/4297d65aba3ba51dec17bbffd6a81abd9640da34.png" width="100%"></kbd></p>
    > [!NOTE]
    > Apache Arrow Table, là một loại dataset hiệu
    > quả hơn (efficient) khi làm việc với lots of data

    <br>

  <a id="node-3311"></a>
  - You can see that **each example** is like a**dictionary object.** This dataset consists of **questions**, **contexts**, and **indices** that **point to the start and end position** of the answer**inside the context**. You can**access the index using the annotations key**, which is a kind of dictionary.
    <br>

      <a id="node-3312"></a>
      <p align="center"><kbd><img src="assets/d29cc6a85c44ce3bbb9af78ad76659799431194a.png" width="100%"></kbd></p>
      > [!NOTE]
      > Đại khái là **question** và **context** (inference vào pipeline) sẽ là **question_text,
      > document_plaintext**
      >
      > Và **thông tin về correct answer** (correct answer) sẽ kiểu như được đánh
      > dấu  **bằng start index và end index** trong document_text cụ thể là  **field
      > annotation - minimal_answers_start_byte và minimal_answer_end_byte**

      <br>

    <a id="node-3313"></a>
    - The **question answering model** predicts **a start and endpoint in the context to extract as the answer**. That's why **this NLP task is known as extractive question answering.**  To train your model, you need to **pass start and endpoints as labels**. So, you need to**implement a function that extracts the start and end positions** from the dataset.  The dataset contains **unanswerable questions**. For these, the **start and end indices for the answer are equal to -1**
      > [!NOTE]
      > Đại khái là với dạng task này, model được train để extract
      > thông tin từ context ra bằng cách predict start và end point
      > trong context.
      >
      > Nên để train nó, ground truth label là start / end position
      > của câu trả lời đúng nằm trong context.
      >
      > Trong dataset có thể có câu hỏi không có câu trả lời, thì 
      > g.t. label của nó sẽ là start / end point đều là -1.

      <br>

        <a id="node-3314"></a>
        <p align="center"><kbd><img src="assets/b09c23ae66cc92efff063c1f4762baf85b6ea0fc.png" width="100%"></kbd></p>
        <br>

        <a id="node-3315"></a>
        <p align="center"><kbd><img src="assets/554457f77205eaad4248ae8eb40366f0f47ea102.png" width="100%"></kbd></p>
        > [!NOTE]
        > Tiếp Theo là flatten the dataset để nó trở thành object có table
        > structure thay vì dictionary structure. Chưa hiểu lắm
        >
        > Đại khái là để giảm thời gian chờ đợi training, ta sẽ chỉ train trên
        > subset 3000 data samples.

        <br>

<a id="node-3316"></a>
- Tokenizer
  <br>

  <a id="node-3317"></a>
  - Now, you will use the \\_**tokenizer**\\_ object from Hugging Face. You can **load a tokenizer** using  different methods. Here, you will **retrieve it from the pipeline object** you created in the  previous Hugging Face lab. With this tokenizer, you can **ensure that the tokens you get  for the dataset** will **match the tokens used in the original DistilBERT** implementation.  When **loading a tokenizer** with any method, you must **pass the model checkpoint** that you  want to fine-tune. Here, you are using the **'distilbert-base-cased-distilled- squad'** checkpoint.
    > [!NOTE]
    > Có nhiều cách để load tokenizer, ở đây ta load từ pipeline define ở
    > trên, việc này sẽ đảm bảo cái tokenizer là đúng cái được dùng trong
    > DistilBERT model. Và phải pass model check point vào.

    <br>

    <a id="node-3318"></a>
    - # Import the AutoTokenizer from the transformers library from transformers import **AutoTokenizer** tokenizer = **AutoTokenizer**.**from_pretrained**("distilbert-base-cased-distilled-squad")
      > [!NOTE]
      > Có thể dùng AutoTokenizer để load tokenizer tương thích với model
      > distilBERT bằng cách gọi **from_pretrained**(tên model)

      <br>

      <a id="node-3319"></a>
      - Given the**characteristics of the dataset** and the **question-answering task**, you will need to **add some steps to pre-process the data** after the tokenization:  When **there is no answer to a question** given a context, you will use the **CLS token**, a unique token used to represent the **start of the sequence.**  **Tokenizers** can **split a given string into substrings**, resulting in a subtoken for each substring, **creating misalignment between the list of dataset tags and the labels generated by the tokenizer**. Therefore, you will need to**align the start and end indices with the tokens associated with the target answer word.**  Finally, a tokenizer can **truncate a very long sequence**. So, if the **start/end position of an answer is None**, you will **assume that it was truncated** and **assign the maximum length of the tokenizer to those positions.**
        <br>

        <a id="node-3320"></a>
        - # Processing samples using the 3 steps described. def **process_samples**(sample):     tokenized_data = tokenizer(sample['document_plaintext'], sample['question_text'], truncation="only_first", padding="max_length")      input_ids = tokenized_data["input_ids"]      # We will label impossible answers with the index of the CLS token.     cls_index = input_ids.index(tokenizer.cls_token_id)      # If no answers are given, set the cls_index as answer.     if sample["annotations.minimal_answers_start_byte"][0] == -1:         start_position = cls_index         end_position = cls_index     else:         # Start/end character index of the answer in the text.         gold_text = sample["document_plaintext"][sample['annotations.minimal_answers_start_byte'][0]:sample['annotations.minimal_answers_end_byte'][0]]         start_char = sample["annotations.minimal_answers_start_byte"][0]         end_char = sample['annotations.minimal_answers_end_byte'][0] #start_char + len(gold_text)          # sometimes answers are off by a character or two – fix this         if sample['document_plaintext'][start_char-1:end_char-1] == gold_text:             start_char = start_char - 1             end_char = end_char - 1     # When the gold label is off by one character         elif sample['document_plaintext'][start_char-2:end_char-2] == gold_text:             start_char = start_char - 2             end_char = end_char - 2     # When the gold label is off by two characters          start_token = tokenized_data.char_to_token(start_char)         end_token = tokenized_data.char_to_token(end_char - 1)          # if start position is None, the answer passage has been truncated         if start_token is None:             start_token = tokenizer.model_max_length         if end_token is None:             end_token = tokenizer.model_max_length          start_position = start_token         end_position = end_token      return {'input_ids': tokenized_data['input_ids'],           'attention_mask': tokenized_data['attention_mask'],           'start_positions': start_position,           'end_positions': end_position} 
          <br>

            <a id="node-3321"></a>
            <p align="center"><kbd><img src="assets/cc06218ff9b4bf370f26d8e9d23198401d8a5d38.png" width="100%"></kbd></p>
            <br>

<a id="node-3322"></a>
- Transformer
  <br>

    <a id="node-3323"></a>
    <p align="center"><kbd><img src="assets/8c74f5094bd278567afabe03d3414171ea1432fb.png" width="100%"></kbd></p>
    > [!NOTE]
    > Dùng **AutoModelForQuestionAnswering**.
    > **from_pretrained**(tên model  = distilBERT
    > model name) để **load model**

    <br>

    <a id="node-3324"></a>
    <p align="center"><kbd><img src="assets/f09e574f3d433892c28acc6e23dfc3270c7933f3.png" width="100%"></kbd></p>
    > [!NOTE]
    > Cơ bản là **sét định dạng của train/test dataset cụ thể là
    > các feature được define** thành **Pytorch Tensor.**

    <br>

  <a id="node-3325"></a>
  - Here, we give you the **F1 score** as a **metric to evaluate** your model's performance. We will use this metric for simplicity, although it is based on the start and end values predicted by the model. If you want to dig deeper on other metrics that can be used for a question and answering task, you can also check this**colab notebook resource from the Hugging Face team.**
    > [!NOTE]
    > Đại khái là ở đây **chỉ dùng F1 score để evaluate cho nhanh**, nghiên cứu thêm **cách
    > khác evaluate 'Question Answering' model** bằng Notebook này:
    >
    > https://colab.research.google.
    > com/github/huggingface/notebooks/blob/master/examples/question_answering. ipynb

    <br>

      <a id="node-3326"></a>
      <p align="center"><kbd><img src="assets/7d94ec50caa7477369af56bd58121e4bddd35b5c.png" width="100%"></kbd></p>
      > [!NOTE]
      > Viết function tính F1 score, cơ bản là dùng f1_score của
      > Scikit Learn. Chưa hiểu lắm nó tính như thế nào

      <br>

      <a id="node-3327"></a>
      <p align="center"><kbd><img src="assets/ac8e620b5a94765f4828cc86c479e5bf6f668b78.png" width="100%"></kbd></p>
      <p align="center"><kbd><img src="assets/0d5288a346779c620d26d18cdffb648939444c56.png" width="100%"></kbd></p>
      <p align="center"><kbd><img src="assets/ac8e620b5a94765f4828cc86c479e5bf6f668b78.png" width="100%"></kbd></p>
      <p align="center"><kbd><img src="assets/0d5288a346779c620d26d18cdffb648939444c56.png" width="100%"></kbd></p>
      <p align="center"><kbd><img src="assets/5277b6ac8f5b3c18dbe735054435c3c4c585143f.png" width="100%"></kbd></p>
      > [!NOTE]
      > Start Fine-tuning model, sử dụng **Trainer**. Take input là **model**, **training
      > argument**- define **output directory để save fine-tuned model**, số **epoch**, **batch
      > size**, l**earning rate decay**..
      >
      > Và **training/evaluation dataset** cũng như là **metric**, ở đây metric đưa vào là
      > một **function tính f1 score define ở trên** thay vì chỉ là một default metric nào
      > đó như Accuracy

      <br>

      <a id="node-3328"></a>
      <p align="center"><kbd><img src="assets/d5cf7e4b599aca615bd912e460865f38f7222102.png" width="100%"></kbd></p>
      > [!NOTE]
      > Evaluate trên test set

      <br>

<a id="node-3329"></a>
- Using Your Fine-tunied Model
  <br>

  <a id="node-3330"></a>
  - After **training and evaluating** your**fine-tuned model**, you can **check its results** for the same questions from the previous lab.  For that, you will tell **Pytorch** to use your **GPU or your CPU** to run the model. Additionally, you will need to t**okenize your input context and questions**.  Finally, you need to **post-process the output results to transform them from tokens to human-readable strings using the tokenizer.**
    <br>

      <a id="node-3331"></a>
      <p align="center"><kbd><img src="assets/9dd6d25257fca2c4bdc9aed04ac99980a5626204.png" width="100%"></kbd></p>
      <br>

    <a id="node-3332"></a>
    - questions = ["What superheroes were introduced between 1939 and 1941 by Detective Comics and its sister company?",              "What comic book characters were created between 1939 and 1941?",              "What well-known characters were created between 1939 and 1941?",              "What well-known superheroes were introduced between 1939 and 1941 by Detective Comics?"]  for question in questions:     inputs = tokenizer**.encode_plus**(question, text, **return_tensors="pt"**)     #print("inputs", inputs)     #print("inputs", type(inputs))     **input_ids** =**inputs["input_ids"].tolist()[0]**     **inputs.to("cuda")**      text_tokens = tokenizer.**convert_ids_to_tokens**(input_ids)     **answer_model** = **model(**inputs)**     # **Get the most likely beginning of answer** with the argmax of the score     answer_start = **torch.argmax(**         **answer_model['start_logits']**     )        # Get the most likely end of answer with the argmax of the score     answer_end = **torch.argmax**(answer_model['end_logits']) + 1        answer =****tokenizer.**convert_tokens_to_string**(                                          tokenizer.**convert_ids_to_tokens**(                                                             input_ids[answer_start:answer_end]))      print(f"Question: {question}")     print(f"Answer: {answer}\\\ ") 
      > [!NOTE]
      > Với mỗi câu hỏi, làm các bước sau:
      >
      > Dùng tokenizer để preprocess kiểu như tokenize question và context lại thành dạng Pytorch
      > Tensor
      >
      > Sau đó bảo Pytorch dùng GPU (inputs.to('cuda'))
      >
      > Rồi inference vào model,
      >
      > Lấy kết qủa và làm vài bước detokenize

      <br>

      <a id="node-3333"></a>
      - Question: What superheroes were introduced between 1939 and 1941 by Detective Comics and its sister company? Answer: Superman, Batman, Captain Marvel ( later known as SHAZAM! ), Captain America, and Wonder Woman  Question: What comic book characters were created between 1939 and 1941? Answer: Superman, Batman, Captain Marvel ( later known as SHAZAM! ), Captain America, and Wonder Woman  Question: What well-known characters were created between 1939 and 1941? Answer: Superman, Batman, Captain Marvel ( later known as SHAZAM! ), Captain America, and Wonder Woman  Question: What well-known superheroes were introduced between 1939 and 1941 by Detective Comics? Answer: Superman, Batman, Captain Marvel ( later known as SHAZAM! ), Captain America, and Wonder Woman
        <br>

          <a id="node-3334"></a>
          <p align="center"><kbd><img src="assets/d504d3d37760348280b6951613d9330077c88fbb.png" width="100%"></kbd></p>
          > [!NOTE]
          > So với những câu trả lời trước khi
          > fine-tune thì tốt hơn nhiều

          <br>


<a id="node-3335"></a>
## Week Conclusion

<br>


<a id="node-3336"></a>
## Reference

<br>


<a id="node-3337"></a>
### This course drew from the following resources:

> [!NOTE]
> This course drew from the following resources:
>
> - Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer
>  (Raffel et al, 2019)
> https://arxiv.org/abs/1910.10683
>
> - Reformer: The Efficient Transformer (Kitaev et al, 2020)
> https://arxiv.org/abs/2001.04451
>
> - Attention Is All You Need (Vaswani et al, 2017)
> https://arxiv.org/abs/1706.03762
>
> - Deep contextualized word representations
> https://arxiv.org/pdf/1802.05365.pdf 
>
> - The Illustrated Transformer (Alammar, 2018)
> http://jalammar.github.io/illustrated-transformer/
>
> - The Illustrated GPT-2 (Visualizing Transformer Language Models)
>  http://jalammar.github.io/illustrated-gpt2/
>
> - BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
>  https://arxiv.org/abs/1810.04805
>
> - How GPT3 Works - Visualizations and Animations
>  http://jalammar.github.io/how-gpt3-works-visualizations-animations/

<br>


<a id="node-3338"></a>
## Quiz

<br>


<a id="node-3339"></a>
## P.a: Question Answering

<br>


<a id="node-3340"></a>
### Welcome to this week's assignment of course 4. In this you will

> [!NOTE]
> Welcome to this week's assignment of course 4. In this you will
> explore **question answering**. You will implement the **"Text to Text
> Transfer from Transformers"** (better known as **T5**). Since you
> implemented **transformers** from scratch last week you will now be
> able to **use them.**

<br>

<a id="node-3341"></a>
- Overview
  <br>

  <a id="node-3342"></a>
  - This assignment will be different from the two previous ones. Due to **memory and time constraints** of this environment you will not be **able to train a model and use it for inference**. Instead you will **create the necessary building blocks** for the **transformer encoder model** and will use a **pretrained version of the same model** in two ungraded labs after this assignment.  After **completing these 3** (1 graded and 2 ungraded) labs you will:  • Implement the **code necessary** for **Bidirectional Encoder Representation from Transformer (BERT).**  • **Understand how the C4 dataset is structured**.  • **Use a pre-trained model**for **inference**.  • Understand how the **"Text to Text Transfer from Transformers"** or T5 model works.
    > [!NOTE]
    > Đại khái là vì giới hạn bộ nhớ và thời gian ở đây nên ta sẽ **không thể train một
    > cái model cỡ T5, hay BERT được**. Thay vào đó ta sẽ thực hành việc **tạo những
    > building blocks** cho Transformer encoder model. Sau đó **sử dụng pre-trained
    > version** của cùng model đó **để inference trong 2 cái lab cuối.**
    >
    > Từ đó, ta sẽ hiểu những **component** (code để tạo ra) của **BERT**, hiểu về bộ
    > dataset **C4**, và hiểu về **T5 model**

    <br>

<a id="node-3343"></a>
- Importing the Packages
  <br>

    <a id="node-3344"></a>
    <p align="center"><kbd><img src="assets/80b4fa8ba932ef9767bdfedd1fa6bfe3195ab090.png" width="100%"></kbd></p>
    <br>

<a id="node-3345"></a>
- 1 - C4 Dataset
  <br>

    <a id="node-3346"></a>
    <p align="center"><kbd><img src="assets/eeabda31d5c70f45ad3f597b27aa5e7e653c9b86.png" width="100%"></kbd></p>
    > [!NOTE]
    > Đại khái **C4 là một bộ dữ liệu khổng lồ** được thu thập từ **internet**.
    > Nó chính là b**ộ dữ liệu cơ bản để training ra các LLM như BERT,
    > GPT.**..
    >
    > Ở đây ta sẽ chỉ **sử dụng một vài example của nó** (trong file **data.
    > txt**)
    >
    > **Open file và tạo list**

    <br>

    <a id="node-3347"></a>
    <p align="center"><kbd><img src="assets/eaba5168c1f328db59eeecb2785d18411cb82431.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/eaba5168c1f328db59eeecb2785d18411cb82431.png" width="100%"></kbd></p>
    <p align="center"><kbd><img src="assets/fb4c0a1caf8b3a8073ea491cdd65e36b41414db5.png" width="100%"></kbd></p>
    <br>

    <a id="node-3348"></a>
    <p align="center"><kbd><img src="assets/93291bdef3b12978017274100a037a8ba15330f6.png" width="100%"></kbd></p>
    > [!NOTE]
    > Có thể thấy mỗi data sample là map với các key
    > **content-length, content-type, text, timestamp, url**

    <br>

    <a id="node-3349"></a>
    <p align="center"><kbd><img src="assets/06dfe4cfcc0da441595a7fe338d18030c70d77a5.png" width="100%"></kbd></p>
    > [!NOTE]
    > Họ nói để ý sẽ thấy**kí tự 'b'** ở trước mỗi string ví dụ b'
    > 1970', b'text/plain'....Đó là vì thật ra nó là **dạng bytes**
    > (nhớ lại CS50 - byte=8 bit nhị phân)

    <br>

  <a id="node-3350"></a>
  - 1.1 - Pre-Training Objective
    <br>

      <a id="node-3351"></a>
      <p align="center"><kbd><img src="assets/3eb9324acb3582a1e3ecf6aad8903ce4814c3dce.png" width="100%"></kbd></p>
      > [!NOTE]
      > Đại khái là để**tạo training data** sample, ta **lấy một câu** rồi
      > **mask** một hay vài phần (cụm từ) đi, để làm input, và
      > **dùng các cụm từ được mask đó để làm output**

      <br>

  <a id="node-3352"></a>
  - 1.2 - Process C4
    <br>

      <a id="node-3353"></a>
      <p align="center"><kbd><img src="assets/f53c39f0c612392b1efe3afc54150d3eec8ab549.png" width="100%"></kbd></p>
      > [!NOTE]
      > Rất dễ hiểu, như đã thấy, một data sample của C4 chỉ có**content type,
      > content length, và text** - chứa nội dung của một web page hay bài báo gì
      > đó
      >
      > Có nghĩa là không có gì khác hết. Và ta sẽ **dùng phương thức nói ở trên**
      > (**che từ đi, và dùng nó làm label**) để train model predict. Cách này gọi là
      > **self-supervised learning** và thật ra ta đã dùng nó ở **CBOW** - Continuous
      > Bowl Of Words
      >
      > Đoạn code dưới **loop trong data và lấy content (text) ra bỏ vào thành một
      > list**

      <br>

  <a id="node-3354"></a>
  - 1.2.1 - Decode to Natural Language
    <br>

    <a id="node-3355"></a>
    - The following functions will help you **detokenize** and **tokenize** the text data.  The **sentencepiece** vocabulary was used to **convert from text to ids**. This vocabulary file  is **loaded and used in these helper functions**.  **natural_language_texts** has the **text from the examples we gave you.**  Run the cells below to see what is going on.
      > [!NOTE]
      > Đại khái nói là **họ chuẩn bị hai function** giúp **tokenize** và
      > **detokenize** data. Trong đó dùng **sentencepiece** vocabulary
      > được**fit từ bộ dataset C4.**
      >
      > Trong function nó sẽ load bộ vocab này (**vocab_file='
      > sentencepiece.model**' để dùng

      <br>

        <a id="node-3356"></a>
        <p align="center"><kbd><img src="assets/dd0143f45576f2c1ff0527182c10513672d2d41c.png" width="100%"></kbd></p>
        <br>

        <a id="node-3357"></a>
        <p align="center"><kbd><img src="assets/cbd9c9448c780a72ff7d1d6d66da795f898bd73f.png" width="100%"></kbd></p>
        > [!NOTE]
        > Lấy cái data sample thứ 1st (trong list **natural_language_texts** đã chuẩn bị
        > ở trên), **split()** để thành **words list**.
        >
        > Rồi dùng **tokenize()** để thành **token**, ta thấy có **vụ tokenize(word).tolist()**
        > để rồi ví dụ từ **"Beginners" trở thành [12847, 277]** có nghĩa là như đã
        > biết trong cái **lab BPE, nó token theo kiểu subword.**
        >
        > Thành ra từ "**Beginners**" nó thành **2 tokens**
        >
        > Và **detokenize** ngược ra**[12847, 277] thành "Beginners"**

        <br>

        <a id="node-3358"></a>
        <p align="center"><kbd><img src="assets/37c004ca0f30e86711d9bde87f257047af7585d1.png" width="100%"></kbd></p>
        <br>

        <a id="node-3359"></a>
        <p align="center"><kbd><img src="assets/de57994376cb86983b181c1612d29e459ffa9b77.png" width="100%"></kbd></p>
        > [!NOTE]
        > Đại khái phần trên là mô phỏng một cách để 'masking'.
        >
        > string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        >
        > iterate chuỗi string.ascii_letters ở trên, theo chiều từ cuối lên đầu, ví dụ (1,'Z') (2,'Y') (3,'X') ...
        >
        > decoded_text sẽ lần lượt là: 
        >
        > detokenize([32000 - 1]) = 'International' 
        > detokenize([32000 - 2]) = 'erwachsene'
        > ...

        > [!NOTE]
        > Function get_sentinels này làm gì:
        >
        > Nó nhận vocab_size number, sử dụng chuỗi ascii_letters như sau: loop trong
        > các kí tự theo chiều ngược lại (Z -> Y -> X...).
        >
        > Với mỗi char = character trong chuỗi ASCII (Z -> Y -> X...), và i = 1, 2, 3...
        >
        > lấy cái index = vocab_size - i sẽ là **index và cũng là token** của các từ  ở
        > cuối vocab dict đi ngược dần lên: vocab_size -1, vocab_size -2...
        >
        > Nhắc lại khỏi bối rối, vocab_dict được tạo sẽ có dạng (ví dụ vocab_size =
        > 32000) "word a" - 1, "word b" - 2,....."word gì đó 1" - 31199, "word gì đó 2" -
        > 32000 Thì index 32000, 31199 cũng là token của các từ áp chót trong vocab
        > dict.
        >
        > Bỏ vào detokenize() để lấy ra từ (decoded_text)
        >
        > Kế tiếp sentinels[decoded_text] = f'<{char}>': Tạo cặp key=decoded_text,
        > value là kí tự trong chuỗi ASCII ở trên
        >
        > Tóm lại function này mục đích là tạo bộ dictionary, key là các từ trong vocab
        > size từ dưới lên, value là các kí tự trong ASCII cũng từ dưới lên.
        >
        > "Internațional" - "<Z>" 
        > "erwachsene" - "<Y>"

        <br>

      <a id="node-3360"></a>
      - i: 1, char: **Z**[vocab_size - i] = [**31999**] -> decoded_text = **Internațional** The sentinel is <Z> and the decoded token is: Internațional i: 2, char: Y [vocab_size - i] = [31998] -> decoded_text = erwachsene The sentinel is <Y> and the decoded token is: erwachsene i: 3, char: X [vocab_size - i] = [31997] -> decoded_text = Cushion The sentinel is <X> and the decoded token is: Cushion i: 4, char: W [vocab_size - i] = [31996] -> decoded_text = imunitar The sentinel is <W> and the decoded token is: imunitar i: 5, char: V [vocab_size - i] = [31995] -> decoded_text = Intellectual The sentinel is <V> and the decoded token is: Intellectual i: 6, char: U [vocab_size - i] = [31994] -> decoded_text = traditi The sentinel is <U> and the decoded token is: traditi i: 7, char: T [vocab_size - i] = [31993] -> decoded_text = disguise The sentinel is <T> and the decoded token is: disguise i: 8, char: S [vocab_size - i] = [31992] -> decoded_text = exerce The sentinel is <S> and the decoded token is: exerce i: 9, char: R [vocab_size - i] = [31991] -> decoded_text = nourishe The sentinel is <R> and the decoded token is: nourishe i: 10, char: Q [vocab_size - i] = [31990] -> decoded_text = predominant The sentinel is <Q> and the decoded token is: predominant i: 11, char: P [vocab_size - i] = [31989] -> decoded_text = amitié The sentinel is <P> and the decoded token is: amitié i: 12, char: O [vocab_size - i] = [31988] -> decoded_text = erkennt The sentinel is <O> and the decoded token is: erkennt i: 13, char: N [vocab_size - i] = [31987] -> decoded_text = dimension The sentinel is <N> and the decoded token is: dimension i: 14, char: M [vocab_size - i] = [31986] -> decoded_text = inférieur The sentinel is <M> and the decoded token is: inférieur
        <br>

          <a id="node-3361"></a>
          <p align="center"><kbd><img src="assets/be6f71b847498b343b230c7f5269ccb819636e78.png" width="100%"></kbd></p>
          > [!NOTE]
          > Như vậy function này chỉ là nhận **một câu** và một **list các sentinels** chứa các
          > cặp **'từ' - sentinels,** ví dụ **'Intellectual' - '<V>'**
          >
          > Nó sẽ đơn giản là **loop trong sentinels list**, ví dụ: 
          >
          > token (= 'Intellectual') - (char = '<V>'), 
          > token (= 'halloween') - (char = '<b>'), 
          >
          > thực hiện **replace (token, char)** thì có nghĩa là**trong câu input mà có
          > từ 'Intellectual' thì từ đó sẽ bị replace bởi '<V>'**Thành ra câu "I want to dress up as an **Intellectual** this **halloween**" trở thành
          > "I want to dress up as an **<V>** this **<b>**"
          >
          > ====
          >
          > Ở trên nói T5 dùng các ids ở cuối vocab size làm sentinels, có thể bởi lập luận 
          > sau: Vì ta đã biết vocab dict sẽ được tạo theo kiểu - những từ xuất hiện nhiều
          > sẽ nằm ở trên (với id thấp) và cứ thế.
          >
          > Thì kiểu làm ở đây có thể là, họ sẽ chọn 1 con số (hyper-parameter) các sentinels
          > ví dụ 100, lấy từ dưới của vocab dict lên để dùng trong quá trình training sẽ che và 
          > đoán. Thì để thấy cách làm này có hiệu quả gì thì trước tiên xem thử có cách 
          > khác không.
          >
          > Thì một cách khác là, lấy từ trên xuống, (ngược lại với cách này). Ngay lập tức cách
          > này không ổn đó là nó sẽ chọn những từ thông dụng nhất, xuất hiện nhiều và khả năng
          > cao là những từ chung chung vô nghiã như may, can, ....
          >
          > Cách khác đó là lấy random, thì cũng có thể được nhưng cũng khó khống chế khả năng
          > vấp phải những từ chung chung vô nghĩa nhưng xuất hiện nhiều.
          >
          > Cơ bản là cách đầu là ổn nhất theo lập luận này

          <br>

          <a id="node-3362"></a>
          <p align="center"><kbd><img src="assets/2ac0afce50e429fc445de9f20414e8cd77176f99.png" width="100%"></kbd></p>
          <p align="center"><kbd><img src="assets/2ac0afce50e429fc445de9f20414e8cd77176f99.png" width="100%"></kbd></p>
          <p align="center"><kbd><img src="assets/8db2f088d1ddb94d47f48dd88eaae9e0476b2bca.png" width="100%"></kbd></p>
          > [!NOTE]
          > Như ở câu này, có 2 từ xuất hiện trong sentinels là '
          > Intellectual' và 'halloween' đã bị replace bởi '<V>' và '<b>'

          <br>

  <a id="node-3363"></a>
  - 1.3 - Tokenizing and Masking
    <br>

    <a id="node-3364"></a>
    - Exercise 1 - tokenize_and_mask
      <br>

        <a id="node-3365"></a>
        <p align="center"><kbd><img src="assets/35c5970ab9a62522f9e97f321a00ea205f728ebf.png" width="100%"></kbd></p>
        <br>

        <a id="node-3366"></a>
        <p align="center"><kbd><img src="assets/5ab83ab9dd50fc3904735e6dfca37665ac156225.png" width="100%"></kbd></p>
        > [!NOTE]
        > Input sentence: Younes and Lukasz \_were\_ working together in the \_lab\_ yesterday after lunch.
        > Input:                Younes and Lukasz **Z** together in the **Y** yesterday after lunch.
        > Target:              **Z** \_were\_ working **Y** \_lab\_.
        >
        > Nhận đoạn text, vocab_size, noise vai trò như threshold để kiểm soát mức % từ được che,
        > randomizer dùng để tạo một random number từ 0-1 và theo default lấy từ Uniform
        > distribution, và tokenizer
        >
        > Đầu tiên chuẩn bị inps = list chứa các inputs - tức là inputs đưa vào model, đóng vai trò là
        > X đó. Và chuẩn bị targs = list chứa các targets, đóng vai trò ground truth label (Y).
        >
        > Bắt đầu với việc dùng tokenizer object để tokenize text thành các token , sau đó bắt đầu
        > loop trong các token đó.
        >
        > Tạo một random value bằng randomizer(), và so nó với noise = 0.15 Mục đích là với
        > default của randomizer là Uniform distribution (như đã biết sẽ có P(x) bằng nhau hết trên
        > các gía trị khả dĩ của x) thì giả sử gọi rất nhiều lần thì các giá trị của x sẽ xuất hiện chia
        > đều trong khoảng [0:1]. Đồng nghĩa là sẽ có 15% trong số đó mang  giá trị < 0.15.
        >
        > Nôm na là cho 100 số 1-100. với xác suất các số xuất hiện như nhau thì nếu bốc rất nhiều
        > lần ví dụ m lần thì sẽ có m/100 số lần bốc trúng số 1, m/100 lần bốc trúng số 2,..... m/100
        > lần bốc trúng số 15. Như vậy có (m+m+..m)/100 = 15m/100 lần bốc trúng số nhỏ hơn hoặc
        > bằng 15 Như vậy là trong m lần bốc, có 15/100 = 15% số lần bốc trúng số nhỏ hơn hoặc
        > bằng 15.

        > [!NOTE]
        > Check từ trước đó không có mask để đảm bảo không có vị 2 từ mask kế tiếp
        >
        > Nếu pass, tăng số sentinel_num lên 1, lấy end_id = vocab_size - cur_sentinel_num (với
        > cur_sentinel_num tăng lên dần từ 1, 2...thì end_id sẽ lần lượt là vocab_size -1,
        > vocab_size- 2...)
        >
        > và add end_id vào inputs, targets list : tức là đó là từ được chọn để mask
        >
        > ====
        >
        > Nói chung là mục đích là, với đoạn text đưa vào, biến thành list tokens, loop trong đó.
        >
        > Check điều kiện random < 0.15, và trước đó không có mask. 
        > ========
        >
        > Ví dụ tới chữ **"\_were\_"** trong ví dụ ở trên, random check passed -> ta sẽ bỏ **end_id** (ở đây sẽ 
        > là vocab_size - cur_sentinel_num = vocab_size - 1 = **31999**) vào**inputs, và targets**
        >
        > Inputs: ["Younese"(t) "and"(t) "Lukasz"(t) **31999**] ~> [Younese and Lokasz **Z**]
        >
        > Targets: [**31999**] ~> [**Z**]
        >
        > Ra ngoài, bỏ **token** vào targets, targets lúc này:
        > Targets:  [**31999** **"were"(t)**] ~> [Z were]
        >
        > ====
        >
        > Chạy tiếp qua từ **"working"**, 
        > + Ở đây pass random check, nhưng prev_no_mask đang là **False**, nên không pass điều kiện 
        > prev_no_mask, nó sẽ đi xuống add token = "working"(t) vào targets
        >
        > Inputs: ["Younese"(t) "and"(t) "Lukasz"(t) **31999**] ~> [Younese and Lokasz **Z**]
        > Targets: [**31999 "were"(t) "working"(t)**] ~>  [Z were working]
        >
        > (Ở đây nếu không pass random check) thì đơn giản là add "working" vào inputs)
        >
        > ====
        >
        > Chạy tiếp qua từ **"together", "in", "the"** đều không pass random check, nên chỉ add vào inputs 
        > (Ở đây nếu pass random check thì vì vẫn đang có prev_no_mask False nên nó sẽ tiếp tục nối vào chuỗi target [31999 "were"(t) "working"(t) "together"(t), "in"(t), "the"(t)])
        >
        > Inputs:  ["Younese"(t) "and"(t) "Lukasz"(t) 31999 "together"(t) "in"(t) "the"(t)] ~> [Younese and Lokasz Z together in the]
        > Targets: [31999 "were"(t) "working"(t)] ~>  [Z were working]
        >
        > ====
        >
        > Chạy tiếp qua từ "**lab**". Ở đây pass random check, và vì nãy giờ luôn ở nhánh không pass random check nên 
        > prev_no_mask là True, tiến hành update end_id = vocab_size - 2 = 31998, add vào inputs, targets:
        >
        > Inputs:  ["Younese"(t) "and"(t) "Lukasz"(t) 31999 "together"(t) "in"(t) "the"(t) 31998] ~> [Younese and Lokasz Z together in the Y]
        > Targets: [31999 "were"(t) "working"(t) 31998] ~>  [Z were working Y]
        >
        > Ra ngoài, bỏ token vào targets, targets lúc này:
        > [31999 "were"(t) "working"(t) 31998 "lab"(t)] ~>  [Z were working Y lab]
        >
        > ====
        >
        > Chạy tiếp qua từ "**yesterday**", không pass random check, nên chỉ add vào inputs
        >
        > Inputs:  ["Younese"(t) "and"(t) "Lukasz"(t) 31999 "together"(t) "in"(t) "the"(t) 31998 "yesterday"(t)] ~> [Younese and Lokasz Z together in the Y yesterday]
        > Targets: [31999 "were"(t) "working"(t) 31998 "yesterday"(t)] ~>  [Z were working Y yesterday] 
        >
        > Cứ thế tiếp tục. 
        > Kết luận có 2 tính chất quan trọng sau: 
        > Nếu pass random check, nhưng trước đó có mask, thì nó vẫn add vào targets để thành ra mask là 1 cụm nhiều từ ví dụ Z were working 
        > Nếu pass random check nhưng trước đó không có mask thì mới tạo mask mới.
        > Còn nếu không pass random check thì đưa từ vào input nhưng không vào target.

        <br>

        <a id="node-3367"></a>
        <p align="center"><kbd><img src="assets/0455408a95d89a403fef6f2d8608e441bef532b4.png" width="100%"></kbd></p>
        <br>

        <a id="node-3368"></a>
        <p align="center"><kbd><img src="assets/43915b1a3f6ae8b286778f27dd08799f0374c56e.png" width="100%"></kbd></p>
        <br>

        <a id="node-3369"></a>
        <p align="center"><kbd><img src="assets/abc05834dca5ddb91a7003962b38a21a24676035.png" width="100%"></kbd></p>
        <br>

        <a id="node-3370"></a>
        <p align="center"><kbd><img src="assets/6d71340b66b329f3800532ae516913b0e107134d.png" width="100%"></kbd></p>
        > [!NOTE]
        > input string:
        >
        > **b'Beginners** BBQ Class Taking Place in Missoul**a!**\\nDo you want
        > to get  better at making **delicious** BBQ? You will have the
        > opportunity, put **this  on** your calendar now. Thursday, September
        > 22**nd** **join** World Class  BBQ Champion, Tony Balay **from
        > L**onestar Smoke Rangers. **He will**be  teaching a beginner level
        > class for everyone who wants to get better  with their culinary skills.
        > \\nHe will teach you everything you need to  know to **compete in** a
        > KCBS BBQ competition, **including techniques**,  recipes, timelines,
        > meat selection **and trimming**, plus smoker and fire  information.
        > \\nThe **cost to** be in the class is $35 per person**, and** for
        > spectators it is free. Included **in** the cost **will be** either a t-shirt or
        > apron  and you will be tasting samples of each meat that is prepared.'
        >
        > Targets:
        >
        > <Z> Beginners <Y>a! <X> delicious BBQ <W> this on <V>nd join <U>
        > from L  <T> will be<S> who wants<R> He will <Q> compete in<P>
        > including techniques <O> and trimming <N> cost to <M>, and <L>d in
        > <K>t- <J> will be <I>.

        > [!NOTE]
        > token: 12847 - "Beginners"(t)
        >
        > ===random passed!
        >
        > ==prev_no_mask: True
        > end_id = 32000 - 1 = 31999
        > inps: [31999]  
        > targs: [31999]
        >
        > inps: [31999] ~= ['Z']
        > targs: [31999, 12847] ~= ['Z', "Beginners"]
        >
        >
        > token: 277 
        >
        > ===random passed!
        >
        > ==prev_no_mask: False -> Reject, không cho 2 mask liên tục
        >
        > inps: [31999]
        > targs: [31999, 12847, 277] ~= ['Z', "Beginners"]
        >
        >
        >
        > token: 15068
        >
        > ===random not passed!
        >
        > inps: [31999, 15068]
        > targs: [31999, 12847, 277]
        >
        >
        >
        > token: 4501
        >
        > ===random not passed!
        >
        > inps: [31999, 15068, 4501]
        > targs: [31999, 12847, 277]

        > [!NOTE]
        > token: 3
        >
        > ===random not passed!
        >
        > inps: [31999, 15068, 4501, 3]
        > targs: [31999, 12847, 277]
        >
        >
        >
        > token: 12297
        >
        > ===random not passed!
        >
        > inps: [31999, 15068, 4501, 3, 12297]
        > targs: [31999, 12847, 277]
        >
        >
        >
        > token: 3399
        >
        > ===random not passed!
        >
        > inps: [31999, 15068, 4501, 3, 12297, 3399]
        > targs: [31999, 12847, 277]
        >
        >
        >
        > token: 16
        >
        > ===random not passed!
        >
        > inps: [31999, 15068, 4501, 3, 12297, 3399, 16]
        > targs: [31999, 12847, 277]
        >
        >
        >
        > token: 5964
        >
        > ===random not passed!
        >
        > inps: [31999, 15068, 4501, 3, 12297, 3399, 16, 5964]
        > targs: [31999, 12847, 277]
        >
        >
        >
        > token: 7115
        >
        > ===random not passed!
        >
        > inps: [31999, 15068, 4501, 3, 12297, 3399, 16, 5964, 7115]
        > targs: [31999, 12847, 277]

        <br>

  <a id="node-3371"></a>
  - 1.4 - Creating the Pairs
    <br>

      <a id="node-3372"></a>
      <p align="center"><kbd><img src="assets/ffb210cd47d0f9b7a882c24e7492b60131a41058.png" width="100%"></kbd></p>
      <br>

    <a id="node-3373"></a>
    - token: **Internațional**, char **<Z>**  after replacing: Beginners BBQ Class Taking Place in Missoula! Do you **<Z>** to get better at making delicious BBQ? You will have the opportunity, put this on your calendar now. Thursday, September 22nd join World Class erwachsene Champion, Tony Ba Cushion from Lone imunitare Rangers. He will be teaching  Intellectual beginner level class for everyone who wants traditi get better with their culinary disguise. Heexerce teach you everything younourishe to know to compete in a KCBS BBQ competition, including techniques, predominant, timelines, amitié selection and erkennt, plus smoker and fire information. The cost to be in the class is $35 perdimension and for inférieurs it refugi free. cheddard in unterlieg will be either a t-shirt or  garanteazpron and you will be tasting samples of each meat that is prepared.  token: **erwachsene**, char **<Y>**  after replacing: Beginners BBQ Class Taking Place in Missoula! Do you **<Z>** to get better at making delicious BBQ? You will have the opportunity, put this on your calendar now. Thursday, September 22nd join World Class **<Y>** Champion, Tony Ba Cushion from Lone imunitare Rangers. He will be teaching  Intellectual beginner level class for everyone who wants traditi get better with their culinary disguise. Heexerce teach you everything younourishe to know to compete in a KCBS BBQ competition, including techniques, predominant, timelines,amitié selection and erkennt, plus smoker and fire information. The cost to be in the class is $35 perdimension and for inférieurs it refugi free. cheddard in unterlieg will be either a t-shirt or  garanteazpron and you will be tasting samples of each meat that is prepared.
      <br>

<a id="node-3374"></a>
- 2 - Transformer
  <br>

    <a id="node-3375"></a>
    <p align="center"><kbd><img src="assets/01cd7be8ffb2212393b6786f02e4f27767764db2.png" width="100%"></kbd></p>
    <br>

    <a id="node-3376"></a>
    <p align="center"><kbd><img src="assets/0c28221276d7af975a8a6e26e8c6df42fc6ad334.png" width="100%"></kbd></p>
    <br>

  <a id="node-3377"></a>
  - 2.1 - Transformer Encoder
    <br>

      <a id="node-3378"></a>
      <p align="center"><kbd><img src="assets/abd0a27669a061ac850b4fa19a8348f5ae965923.png" width="100%"></kbd></p>
      <br>

  <a id="node-3379"></a>
  - 2.1.1 - The Feedforward Block
    <br>

    <a id="node-3380"></a>
    - Exercise 2 - FeedForwardBlock
      <br>

        <a id="node-3381"></a>
        <p align="center"><kbd><img src="assets/b0d3d57b53e786c93084f14908146fa2821b47b0.png" width="100%"></kbd></p>
        <br>

        <a id="node-3382"></a>
        <p align="center"><kbd><img src="assets/2dcc760d1269a56aa7bfc1705497d8aafba27399.png" width="100%"></kbd></p>
        <br>

  <a id="node-3383"></a>
  - 2.1.2 - The Encoder Block
    <br>

      <a id="node-3384"></a>
      <p align="center"><kbd><img src="assets/5053b0c03b0004b7dcfd65cb178122f75ad56746.png" width="100%"></kbd></p>
      <br>

    <a id="node-3385"></a>
    - Exercise 3 - EncoderBlock
      <br>

        <a id="node-3386"></a>
        <p align="center"><kbd><img src="assets/4f00bee824f1e7ffb82264f2bce2ebdb519d0063.png" width="100%"></kbd></p>
        <p align="center"><kbd><img src="assets/4f00bee824f1e7ffb82264f2bce2ebdb519d0063.png" width="100%"></kbd></p>
        <p align="center"><kbd><img src="assets/418ff92a609a100455e93f533b6e76408c2c7c77.png" width="100%"></kbd></p>
        <br>

        <a id="node-3387"></a>
        <p align="center"><kbd><img src="assets/4e30943eb213977e5944d89dfabf3cb22d734473.png" width="100%"></kbd></p>
        <br>

        <a id="node-3388"></a>
        <p align="center"><kbd><img src="assets/a67040cc225a23e3ae15764348782d746f0492c0.png" width="100%"></kbd></p>
        <br>

  <a id="node-3389"></a>
  - 2.1.3 - The Transformer Encoder
    <br>

    <a id="node-3390"></a>
    - Exercise 4 - TransformerEncoder
      <br>

        <a id="node-3391"></a>
        <p align="center"><kbd><img src="assets/0235493889c5f66473d2e615a81f3aacb7d2cfba.png" width="100%"></kbd></p>
        <br>

        <a id="node-3392"></a>
        <p align="center"><kbd><img src="assets/5fb8ba937473ffa7b56982684468429e6ce34e87.png" width="100%"></kbd></p>
        <p align="center"><kbd><img src="assets/5fb8ba937473ffa7b56982684468429e6ce34e87.png" width="100%"></kbd></p>
        <p align="center"><kbd><img src="assets/2f8b849cf46a021a4a19bfad873e746f3b5485b6.png" width="100%"></kbd></p>
        <br>

        <a id="node-3393"></a>
        <p align="center"><kbd><img src="assets/722bac6e54c85b124794847e942de8a95b452352.png" width="100%"></kbd></p>
        <p align="center"><kbd><img src="assets/722bac6e54c85b124794847e942de8a95b452352.png" width="100%"></kbd></p>
        <p align="center"><kbd><img src="assets/0cb84b450c07a1b61552056a983fd1045e209fda.png" width="100%"></kbd></p>
        <br>


<a id="node-3394"></a>
## Lab: Bert Loss

<br>

<a id="node-3395"></a>

<p align="center"><kbd><img src="assets/c4b16a39787fde717c224540788957049c167593.png" width="100%"></kbd></p>

<br>

<a id="node-3396"></a>

<p align="center"><kbd><img src="assets/aa6e53078551e78856faf23fc6fbc7d3feaf399d.png" width="100%"></kbd></p>

<br>

<a id="node-3397"></a>

<p align="center"><kbd><img src="assets/0760014e2ec8e422e406b1a5e81a3df84f036aed.png" width="100%"></kbd></p>

<br>

<a id="node-3398"></a>

<p align="center"><kbd><img src="assets/5d2400a67c2e6d4e789bd3711a09974ee6a8f874.png" width="100%"></kbd></p>

> [!NOTE]
> Các bước đã làm trong PA: Load bộ dataset (C4), tạo list chỉ chứa
> các content (field text của json file)
>
> Chuẩn bị một số function: tokenize() và detokenize(), dùng tokenizer
> đã fit với  dataset để tokenize và detokenize

<br>

<a id="node-3399"></a>

<p align="center"><kbd><img src="assets/78f22adb1bef8eb7d0ece1424cca546559adff4d.png" width="100%"></kbd></p>

> [!NOTE]
> Function get_sentinels này làm gì:
>
> Nó nhận vocab_size number, sử dụng chuỗi ascii_letters như sau: loop trong
> các kí tự theo chiều ngược lại (Z -> Y -> X...).
>
> Với mỗi char = character trong chuỗi ASCII (Z -> Y -> X...), và i = 1, 2, 3...
>
> lấy cái index = vocab_size - i sẽ là **index và cũng là token** của các từ  ở
> cuối vocab dict đi ngược dần lên: vocab_size -1, vocab_size -2...
>
> Nhắc lại khỏi bối rối, vocab_dict được tạo sẽ có dạng (ví dụ vocab_size =
> 32000) "word a" - 1, "word b" - 2,....."word gì đó 1" - 31199, "word gì đó 2" -
> 32000 Thì index 32000, 31199 cũng là token của các từ áp chót trong vocab
> dict.
>
> Bỏ vào detokenize() để lấy ra từ (decoded_text)
>
> Kế tiếp sentinels[decoded_text] = f'<{char}>': Tạo cặp key=decoded_text,
> value là kí tự trong chuỗi ASCII ở trên
>
> Tóm lại function này mục đích là tạo bộ dictionary, key là các từ trong vocab
> size từ dưới lên, value là các kí tự trong ASCII cũng từ dưới lên.

<br>

<a id="node-3400"></a>

<p align="center"><kbd><img src="assets/4aeaf3ffc35b02d1a86b4a196aacdec0dbf89836.png" width="100%"></kbd></p>

> [!NOTE]
> Như vậy function này chỉ là nhận **một câu** và một **list các sentinels** chứa các
> cặp **'từ' - sentinels,** ví dụ **'Intellectual' - '<V>'**
>
> Nó sẽ đơn giản là **loop trong sentinels list**, ví dụ: 
>
> token (= 'Intellectual') - (char = '<V>'), 
> token (= 'halloween') - (char = '<b>'), 
>
> thực hiện **replace (token, char)** thì có nghĩa là**trong câu input mà có
> từ 'Intellectual' thì từ đó sẽ bị replace bởi '<V>'**Thành ra câu "I want to dress up as an **Intellectual** this **halloween**" trở thành
> "I want to dress up as an **<V>** this **<b>**"
>
> ====
>
> Ở trên nói T5 dùng các ids ở cuối vocab size làm sentinels, có thể bởi lập luận 
> sau: Vì ta đã biết vocab dict sẽ được tạo theo kiểu - những từ xuất hiện nhiều
> sẽ nằm ở trên (với id thấp) và cứ thế.
>
> Thì kiểu làm ở đây có thể là, họ sẽ chọn 1 con số (hyper-parameter) các sentinels
> ví dụ 100, lấy từ dưới của vocab dict lên để dùng trong quá trình training sẽ che và 
> đoán. Thì để thấy cách làm này có hiệu quả gì thì trước tiên xem thử có cách 
> khác không.
>
> Thì một cách khác là, lấy từ trên xuống, (ngược lại với cách này). Ngay lập tức cách
> này không ổn đó là nó sẽ chọn những từ thông dụng nhất, xuất hiện nhiều và khả năng
> cao là những từ chung chung vô nghiã như may, can, ....
>
> Cách khác đó là lấy random, thì cũng có thể được nhưng cũng khó khống chế khả năng
> vấp phải những từ chung chung vô nghĩa nhưng xuất hiện nhiều.
>
> Cơ bản là cách đầu là ổn nhất theo lập luận này

<br>

<a id="node-3401"></a>

<p align="center"><kbd><img src="assets/2211f6678488b6493d52b18e07632d93e46f98f5.png" width="100%"></kbd></p>

<br>

<a id="node-3402"></a>

<p align="center"><kbd><img src="assets/82292111e2ca319039b248088ef62f27bb74f1a5.png" width="100%"></kbd></p>

<br>

<a id="node-3403"></a>

<p align="center"><kbd><img src="assets/a7c50a3dee8b38a0ca1305c7bd4684449226a1cf.png" width="100%"></kbd></p>

<br>

<a id="node-3404"></a>

<p align="center"><kbd><img src="assets/0adcbe036952918da06d140a488aadc1f83ccf06.png" width="100%"></kbd></p>

<br>

<a id="node-3405"></a>

<p align="center"><kbd><img src="assets/78863be059c0959d4c99e5d9ce0f33af19415dda.png" width="100%"></kbd></p>

> [!NOTE]
> Không ai train Transformer from scratch, vì tốn rất nhiều thời gian.
> Thường người ta download pre-trained model và fine-tune với
> specific task
>
> Ở đây trước tiên là khởi tạo Transformer model của Trax với các
> hyper-params  nà ta đã "dùng" khi build component cho model
> (Encoder block) như một cách để biết thật sự bên trong Trax's
> Transformer có gì.
>
> **d_ff** là **số unit của Feed Forward layers**,
>
> **d_model** là **kích thước embedding vector**,
>
> **max_len** là h.p quy định **max length** để giúp quá trình **padding và
> batching.**
>
> **n_heads** là **number of heads trong Multi-head attentions layers**.
>
> **dropout** đương nhiên là **dropout rate,**
> input vocab size là **vocab size,**
>
> **n_encoder_layers** = 24 tức có tới 24 Encoder kế tiếp nhau trong
> Encoder stacks,
>
> tương tự với **n_decoder_layers**

<br>


<a id="node-3406"></a>
### Sure, here's an explanation for each of the hyper-parameters in the Transformer initialization using the Trax

> [!NOTE]
> Sure, here's an explanation for each of the hyper-parameters in the Transformer initialization using the Trax
> library:
>
> 1. **d_ff (Feedforward dimensionality)**: This represents the number of units in the feed-forward neural
> network that exists in each transformer block. It essentially denotes the inner hidden size of the pointwise
> feedforward networks. In the provided initialization, it is set to 4096.
>
> 2. **d_model (Model Dimensionality)**: This is the depth size or the number of units in the embeddings and
> also in the transformer blocks. In this model, the embeddings and outputs for each transformer block will
> have a size of 1024.
>
> 3. **max_len**: This represents the maximum sequence length that the model can handle. It's essentially
> the maximum number of tokens a sequence can have for processing by the transformer. In this instance, it's
> set to 2048 tokens.
>
> 4. **n_heads (Number of Heads)**: In the multi-head attention mechanism of the transformer, `n_heads`
> denotes the number of parallel sets of linear projections used for the attention computations. Here, 16
> heads means that the multi-head attention mechanism will process the input in parallel 16 times with
> different learned linear projections.
>
> 5. **dropout**: Dropout is a regularization technique where randomly selected neurons are ignored or "
> dropped out" during training. This helps in preventing overfitting. The value `0.1` indicates a 10% dropout
> rate.
>
> 6. **input_vocab_size**: This denotes the size of the vocabulary for the input sequences. Here, the model
> can handle input sequences with a vocabulary size of up to 32000 unique tokens.
>
> 7. **n_encoder_layers**: This indicates the number of transformer blocks in the encoder part of the
> transformer model. In this instance, there are 24 encoder layers.
>
> 8. **n_decoder_layers**: This specifies the number of transformer blocks in the decoder part of the
> transformer model. Like the encoder, there are 24 decoder layers here.
>
> 9. **mode**: This parameter determines how the model will be used. The modes can typically be:    - `'train'
> `: For training the model.    - `'eval'`: For evaluating the model. When set to 'eval', some functionalities like
> dropout will be turned off.    - `'predict'`: For generating predictions from the model. In the provided
> initialization, the mode is set to 'predict'. The comment also mentions that you can change it to `'eval'` for
> slow decoding.
>
> Each of these hyper-parameters plays a vital role in the functioning, capacity, and performance of the
> Transformer model. Adjusting them can have significant impacts on how the model learns and makes
> predictions.

<br>

<a id="node-3407"></a>

<p align="center"><kbd><img src="assets/3a241026c50e79e49d788a88fbbaacab060c7627.png" width="100%"></kbd></p>

> [!NOTE]
> Load pre-trained
> model từ filepath

  <br>

<a id="node-3408"></a>

<p align="center"><kbd><img src="assets/f647230a9fb2ead33c536ed7cb4866c26686339a.png" width="100%"></kbd></p>

> [!NOTE]
> Dùng function **inputs_targets_pairs**() để **tạo và lấy** một "bộ"
> input - target. Lấy text content ra, dùng cơ chế masking đã làm để
> thay từ trong text bằng sentinel,..để tạo ra input và targets
>
> Lấy lại ví dụ :
> Input sentence: Younes and Lukasz were working together in the **lab** yesterday after lunch.
> Input:                Younes and Lukasz **Z**                     together in the **Y**    yesterday after lunch.
> Target:               **Z were working** **Y lab**.
> (Ghi cách vậy cho dễ hiểu thôi chứ không phải nó có khoảng cách như vậy đâu)
>
> Và dùng pretty_decoded để decode ra xem

  <br>

<a id="node-3409"></a>
- **pretty_decoded input:**  Fo **<Z>** plaid ly **<Y>** and **<X>**dex shortall with metallic slinky insets. Attached metallic elastic **<W>** with O-ring. **<V>**band **<U>**. Great hip hop **<T>** dance costume. Made in the USA.  **pretty_decoded target:**  **<Z>il <Y>cra <X> span <W> belt <V> Head <U> included <T> or jazz**  c4_input:  [4452, 31999, 30772, 3, 120, 31998, 11, 31997, 26, 994, 710, 1748, 28, 18813, 3, 7, 4907, 63, 16, 2244, 7, 5, 28416, 15, 26, 18813, 15855, 31996, 28, 411, 18, 1007, 5, 31995, 3348, 31994, 5, 1651, 5436, 13652, 31993, 2595, 11594, 5, 6465, 16, 8, 2312, 5]  c4_target:  [31999, 173, 31998, 2935, 31997, 8438, 31996, 6782, 31995, 3642, 31994, 1285, 31993, 42, 9948] 15 64
  <br>

    <a id="node-3410"></a>
    <p align="center"><kbd><img src="assets/5052a3820f24bd139a54f98dfa8bb48ec440da1b.png" width="100%"></kbd></p>
    > [!NOTE]
    > Chưa hiểu lắm, họ dùng **trax.supervise.decoding**, gọi function
    > **autoregressive_sample** take input:
    >
    > - **pre-trained model** load ở trên,
    >
    > - **c4_input** là cái**token sequence của masked text**
    >
    > - Tham số **temperature** = 0 (để chỉ định dùng **most probable tokens**)
    >
    > Kết quả có được bỏ vào wrapper.fill() có tác dụng gì chưa rõ
    > So sánh với Target chưa hiểu sao lại có các sentinel khác như <S>, <R>..
    >
    > Target: <Z>il **<Y>cra** <**X> span** <W> belt <V> Head <U> included <T> or jazz
    >
    > Prediction: <Z>o **<Y>cra** **<X> span** <W> waistband <V> Attached metallic elastic
    > waist <U> with O-ring <T> and<S>o<R>cra <Q>,<P> span <O> and<N>o
    > <M>cra <L> span <K> waistband. A rhy <J>o

    <br>


<a id="node-3411"></a>
## Lab: T5

<br>


<a id="node-3412"></a>
### Welcome to the part 2 of testing the models for this week's

> [!NOTE]
> Welcome to the part 2 of testing the models for this week's
> assignment. This time we will perform **decoding using the T5
> SQuAD model**. In this notebook we'll **perform Question
> Answering** by **providing a "Question", its "Context"** and **see how
> well we get the "Target" answer.**

> [!NOTE]
> Thử **dùng** T5 đã **fine-tuned trên SqaAD dataset**. Đưa vào model
> **question + context** và xem thử answer của nó ra sao

<br>

<a id="node-3413"></a>

<p align="center"><kbd><img src="assets/9d496378778488fcf5c70dcd4cd639ba0172ea81.png" width="100%"></kbd></p>

> [!NOTE]
> Install Trax và t5

  <br>

<a id="node-3414"></a>

<p align="center"><kbd><img src="assets/ab54434e975458e22a14f85e4c53c8afb66c0a03.png" width="100%"></kbd></p>

  <br>

<a id="node-3415"></a>

<p align="center"><kbd><img src="assets/f8f2d961fabb3a50a74ee4332ff48b2c3a6d8f96.png" width="100%"></kbd></p>

  <br>

<a id="node-3416"></a>

<p align="center"><kbd><img src="assets/f7bf53350f960bd7e85935548908efceb9855c59.png" width="100%"></kbd></p>

> [!NOTE]
> Chuẩn bị mấy function như lab trước

  <br>

<a id="node-3417"></a>

<p align="center"><kbd><img src="assets/057ed9dc59c8701ba836cbe1c8637338774e9ba9.png" width="100%"></kbd></p>

  <br>

<a id="node-3418"></a>
- Now let's try to **fine tune on SQuAD** and see what becomes of the model. For this, we need to **write a function** that will **create and process the SQuAD tf.data.Dataset**. Below is how **T5 pre-processes SQuAD dataset** as a **text2text example**. Before we jump in, we will have to **first load in the data.**
> [!NOTE]
> Đại khái là lab này mình sẽ dùng **T5 model** đã được
> **fine-tuned với bộ dataset tên là SQuAD**.

  <br>

    <a id="node-3419"></a>
    <p align="center"><kbd><img src="assets/81a26b009cc3d8405841b3aa616f5940f7f79fb3.png" width="100%"></kbd></p>
    > [!NOTE]
    > Đại khái nó nói là mỗi text2text example của SQuAD dataset có dạng
    >
    > inputs: 'question: <question> context: <article>'
    > target: '<answer'
    >
    > Function squa_preprocess_fn() ở dưới nhận bộ dataset và xử lí nó 
    > sử dụng sentencePiece vocabulary như đã biết
    >
    > Chưa hiểu lắm nó preprocess kiểu gì

    <br>

    <a id="node-3420"></a>
    <p align="center"><kbd><img src="assets/2e7f349168dbe0563efbd474dc21ad08faa88f3f.png" width="100%"></kbd></p>
    > [!NOTE]
    > Tạo train_generator_fn, và eval_generator_fn là **data_streams**define
    > data directory, **preprocess functions**, tên của feature làm inputs, tên của
    > feature làm targets. 
    >
    > Nói chung như đã gặp, nó sẽ dùng load data trong data directory, dùng 
    > pre_process_function để thực hiện preprocess

    <br>

    <a id="node-3421"></a>
    <p align="center"><kbd><img src="assets/e7163ccc259926b3f022ef04c52e0f7bf60ab828.png" width="100%"></kbd></p>
    > [!NOTE]
    > In ra một example xem thử

    <br>

  <a id="node-3422"></a>
  - **question**: What is the use of a transistor ?  **context**:  A transistor is a semiconductor device used to amplify or switch electronic signals and electrical power . It is composed of semiconductor material with at least three terminals for connection to an external circuit . A voltage or current applied to one pair of the transistor ' s terminals changes the current through another pair of terminals . Because the controlled ( output ) power can be higher than the controlling ( input ) power , a transistor can amplify a signal . Today , some transistors are packaged individually , but many more are found embedded in integrated circuits .  **target**: to amplify or switch electronic signals and electrical power
    <br>

      <a id="node-3423"></a>
      <p align="center"><kbd><img src="assets/8e49666b833fecc3719db1d3f6437e194adec1b6.png" width="100%"></kbd></p>
      > [!NOTE]
      > Tạo Transformer model với các
      > hyper params như lab trước

      <br>

      <a id="node-3424"></a>
      <p align="center"><kbd><img src="assets/5a876dc5966f1ec0ed007928fb163e1f116f3e8e.png" width="100%"></kbd></p>
      > [!NOTE]
      > Load pretrained-weight

      <br>

      <a id="node-3425"></a>
      <p align="center"><kbd><img src="assets/29e47f238a3b5430da35adbaaccdadaba02f876c.png" width="100%"></kbd></p>
      > [!NOTE]
      > **inputs** = '**question**: What are some of the colours of a rose? **context**: A rose is
      > a woody perennial flowering plant of the genus Rosa, in the family Rosaceae,
      > or the flower it bears.There are over three hundred species and tens of
      > thousands of cultivars. They form a group of plants that can be erect shrubs,
      > climbing, or trailing, with stems that are often armed with sharp prickles.
      > Flowers vary in size and shape and are usually large and showy, in colours
      > ranging from white through yellows and reds. Most species are native to Asia,
      > with smaller numbers native to Europe, North America, and northwestern
      > Africa. Species, cultivars and hybrids are all widely grown for their beauty and
      > often are fragrant.'

      > [!NOTE]
      > Tạo một input là question: ...context:....
      > Dùng tokenize() để tokenize nó

      <br>

      <a id="node-3426"></a>
      <p align="center"><kbd><img src="assets/199cd03506783eabfa01553d282f1765445a5b6c.png" width="100%"></kbd></p>
      > [!NOTE]
      > Dùng decoding.autoregressive_sample như ở lab trước, bỏ vào
      > đó model, inputs (đã được chuyển thành np.array),
      > temperature, max_length) và dùng wrapper.fill, pretty_decode
      > để decode model's output
      >
      > Nói chung cái lab này giống như lab trên chẳng làm gì ngoài
      > việc load pre-trained model và thử inference nó để xem kết qủa
      > ra sao

      <br>

