# Generating Text With Transformers

📊 **Progress:** `7` Notes | `7` Screenshots

---

<a id="node-55"></a>
## 1 Transformer Architecture: The passage provides a high-level overview of the **major components** inside

> [!NOTE]
> 1 Transformer Architecture: The passage provides a high-level overview of the **major components** inside
> the**transformer architecture**.
>
> 2 Translation Task: The example focuses on a translation task, where a transformer model is used to
> translate a French phrase into English.
>
> 3 **Tokenization** and **Encoding**: The input words are **tokenized** using a **tokenizer**, **added to the
> encoder side of the network**, **passed through the embedding layer**, and then **fed into the multi-headed
> attention layers**.
>
> 4 **Encoder**: The **input sequence** **goes through the encoder**, which **generates a deep representation
> of the input sequence's structure and meaning**.
>
> 5 **Decoder**: The **deep representation from the encoder** is **inserted into the decoder** to influence its
> **self-attention mechanisms**. A **start of sequence token** is **added to the decoder's input**, and **it
> predicts the next token** based on the**contextual understanding from the encoder**.
>
> 6**Looping and Generation**: The **output token** from the **decoder** is p**assed back as input to generate
> the next token**. This **loop** continues **until an end-of-sequence token is predicted**, generating the**final
> sequence of tokens.**
>
> 7 **Detokenization**: The**final sequence of tokens** can be **detokenized into words**, resulting in the
> **translated output.** 8 Types of **Transformer Models:**
>
> a.**Encoder-Only Models**: They work as **sequence-to-sequence models** and can be used for**classification tasks** with additional layers. **BERT** is an example.
>
> b. **Encoder-Decoder Model**s: They excel at**sequence-to-sequence** tasks like **translation**. They can
> also be trained for **general text generation task**s. Examples include **BART** and **T5**.
>
> c. **Decoder-Only Models**: Widely used models like **GPT**, **BLOOM**, **Jurassic**, **LLaMA**, etc., that
> can **generalize to most tasks.**
>
> 9 **Prompt Engineerin**g: Understanding the details of the underlying architecture is not necessary for
> interacting with transformer models through natural language. **Prompt engineering, using written words as
> prompts,** is the **key to working with transformer model**s.
>
> The passage emphasizes that the goal is to provide **enough background information** to understand the
> **differences between various transformer models** and read their documentation, without needing to
> remember all the details. The next part of the course will focus on prompt engineering.

<br>

<a id="node-56"></a>

<p align="center"><kbd><img src="assets/c6fc8988f72eb2554a4a93834b3b537837c0e423.png" width="100%"></kbd></p>

> [!NOTE]
> Như đã nói ở bài trước, qua các bước **tokenization**, **embedding**,
> **multi-head attention**, **fully connected layers**, **output** của encoder sẽ được
> **insert** vào **khúc giữa của decoder**cung cấp các **thông tin về ngữ cảnh**
> cho **decoder** để nó **dùng khi generating text.**

<br>

<a id="node-57"></a>

<p align="center"><kbd><img src="assets/892e53f1fc70b86add23885683d8a2fc2061f083.png" width="100%"></kbd></p>

> [!NOTE]
> Decoder cũng **nhận input bắt đầu từ start of sentence token**, cũng **tokenization**, **embedding**, và
> **multi-head attention**. Sau đó nó **kết hợp với output của encoder** và qua một số**FC layer**
> và **softmax** để p**redict ra từ tiếp theo**. Tiếp tục, **bỏ từ mới generate này** vào **input** của
> decoder để **tiếp tục vòng lặp cho đến khi generate EOS token**.

<br>

<a id="node-58"></a>

<p align="center"><kbd><img src="assets/546ec0c45aa80a132beaa36c4a9e2e26d1760e65.png" width="100%"></kbd></p>

<br>

<a id="node-59"></a>

<p align="center"><kbd><img src="assets/0d4d34af18d0053e203ca6145db8217c7d3c29d5.png" width="100%"></kbd></p>

> [!NOTE]
> Xong hết, các token được
> **detokenize** để **tạo ra câu tiếng Anh**

<br>

<a id="node-60"></a>

<p align="center"><kbd><img src="assets/63e65b7ab1980a88d28e0443a3f6c266d07c3e3d.png" width="100%"></kbd></p>

<br>

<a id="node-61"></a>

<p align="center"><kbd><img src="assets/3aeda8919cc4b06ce24f22cfcc0122d0c6e8ec49.png" width="100%"></kbd></p>

> [!NOTE]
> Let's summarize what you've seen so far. The **complete transformer
> architecture** consists of an **encoder** and **decoder** components. The
> **encoder** encodes **input sequences**into a **deep representation** of the
> structure and meaning of the input. The **decoder**, working from **input
> token triggers**, uses the **encoder's contextual understanding** to **generate
> new tokens**. It does this in a **loop until some stop condition has been
> reached**

<br>

<a id="node-62"></a>

<p align="center"><kbd><img src="assets/088aeb66f7fd8c1d00be9e428d204c61e2d600bb.png" width="100%"></kbd></p>

> [!NOTE]
> **Encoder-only models** also work as**sequence-to-sequence models**, but **without
> further modification**, the input sequence and the output sequence or the **same
> length.** Their use is**less common these days**, but by **adding additional layers
> to the architecture**, you can **train encoder-only model**s to perform **classification
> tasks**such as **sentiment analysis**, **BERT** is an example of an encoder-only
> model

> [!NOTE]
> Encoder-decoder models, as you've seen, perform well on
> **sequence-to-sequence tasks** such as **translation**, where the **input
> sequence** and the **output sequence** can be **different lengths**. You can
> also **scale and train this type of model to perform general text
> generation tasks**. Examples of encoder-decoder models include
> BART as opposed to **BERT** and **T5**, the model that you'll use in the
> labs in this course.

> [!NOTE]
> Finally, **decoder-only models** are some of the **most commonly used**today. Again, as they have scaled, their capabilities have grown.
> These models can now generalize to most tasks. Popular
> decoder-only models include the **GPT** family of models, **BLOOM**,
> **Jurassic**, **LLaMA**, and many more

<br>

