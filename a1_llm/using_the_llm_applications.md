# Using The LLM Applications

📊 **Progress:** `8` Notes | `12` Screenshots

---

<a id="node-576"></a>
## 1. **Challenges with LLMs:**

> [!NOTE]
> 1. **Challenges with LLMs:**
>
> - **LLMs have a knowledge cutoff,** and they **can't provide information beyond their training
> data**.
> - They can struggle with **complex math problems** as they **predict tokens based on
> training, not perform calculations**.
> - LLMs tend to**generate text even when they don't know the answer**, leading to "
> hallucination."
>
> 2. ****Connecting to External Data Sources**:**
>
> - To overcome these challenges, you can **connect LLMs to external data sources and
> applications**.
> - This connection is facilitated through an**orchestration library**.
> - Access to external data sources **enhances LLM performance** at runtime.
>
> 3. ****Retrieval Augmented Generation (RAG)**:**
>
> - **RAG** is a framework that **allows LLMs to utilize external data sources**.
> - It helps **overcome knowledge cutoff issues by providing access to additional data during
> inference**.
> - RAG can be used to**access new information documents** or **proprietary knowledge**.
> - It **improves the relevance and accuracy of LLM completions**.
>
> 4. **RAG Implementation:**
>
> - RAG involves a "**Retriever**" component consisting of a **query encoder and an external
> data source**.
> - The encoder **encodes user input for querying the data source**.
> - The **Retriever** finds **relevant documents and combines them with the user query**.
> - The **expanded prompt** is then used by the LLM to generate completions.
>
> 5. **Benefits of RAG:**
>
> - RAG helps **prevent model hallucination and enhances LLM utility**.
> - It can **integrate various external information sources**, including **local documents, the
> internet, and databases**.
> - Vector Stores, containing **vector representations of text**, are particularly useful for LLMs in
> RAG.
>
> 6. **Considerations for RAG:**
>
> - External data **must be chunked to fit the LLM's context window**.
> - **Data retrieval** relies on **vector representations** and similarity measures.
> - **Vector stores and databases** allow for **efficient searching and citation tracking.**
>
> By connecting LLMs to **external data sources** using RAG, you can **address their
> limitations, improve their performance, and provide more accurate and relevant information to
> users.**

<br>

<a id="node-577"></a>

<p align="center"><kbd><img src="assets/480031dd633ed65d82400062467679ccc19aaed3.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là LLM có những nhược điểm như bị outdate
> thông tin, không tính toán được và bịa chuyện

<br>

<a id="node-578"></a>

<p align="center"><kbd><img src="assets/a24bf7a70c351bb448b015d00a5e5804611eaa9c.png" width="100%"></kbd></p>

<br>

<a id="node-579"></a>

<p align="center"><kbd><img src="assets/26810b6358eeb8c8156a460b105ef2eb4a8a33f9.png" width="100%"></kbd></p>

> [!NOTE]
> Những điều này có thể khắc phục bằng cách dùng một cơ
> chế như sau Orchestration library để kết nối LLM với
> Database hoặc External applications,

<br>

<a id="node-580"></a>

<p align="center"><kbd><img src="assets/60da38146ba135878c3c56ecbd07441c2079253c.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là có nhiều lib support việc này, ở đây nói về cái đầu tiên (của
> Facebook) trong đó đại khái là nó giúp từ initial prompt, nó lấy thông tin từ
> external information sources và rồi combine với initial prompt để được
> prompt mới (chứa những kiến thức được cập nhật) sẽ bỏ vào model

<br>

<a id="node-581"></a>

<p align="center"><kbd><img src="assets/5778c59e0a483d0ef2cbe898dffac404ff7add39.png" width="100%"></kbd></p>

> [!NOTE]
> Lấy ví dụ hỏi model về một vấn đề liên quan đến một vụ án
> trong lịch sử. Query encoder sẽ trích xuất thông tin của vụ án ra
> để kết hợp với initial prompt trước  khi bỏ vào model

<br>

<a id="node-582"></a>

<p align="center"><kbd><img src="assets/e68f34c9099551bf45d092338f697e75a1cb8114.png" width="100%"></kbd></p>

> [!NOTE]
> Với **thông tin đúng được trích xuất** đi kèm với**initial prompt**, đưa
> vào model sẽ **giúp model cho ra câu trả lời với thông tin được cập
> nhật chính xác**
>
> Thật ra quá trình này cũng y như mình tìm thông tin rồi instructed
> prompting vậy

<br>

<a id="node-583"></a>

<p align="center"><kbd><img src="assets/20df200a22dd6865f96bf589a96f33fd3de31e54.png" width="100%"></kbd></p>

<br>

<a id="node-584"></a>

<p align="center"><kbd><img src="assets/f84d5529a7d633722a3e570c7f79b1f177118710.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là vì limit của context window nên thông tin trích xuất thực tế
> sẽ phải được split ra thành nhiều mảnh. Thì những cái như
> LangChain sẽ giúp làm việc này

<br>

<a id="node-585"></a>

<p align="center"><kbd><img src="assets/237e495a2c72e956553d8745fa018503038bee18.png" width="100%"></kbd></p>

> [!NOTE]
> Điều consideration thứ 2 đó là
> data phải ở format phù hợp: Embedding vectors

<br>

<a id="node-586"></a>

<p align="center"><kbd><img src="assets/2514f004b42f5f4823edeb172b89f088b3c602f7.png" width="100%"></kbd></p>

<br>

<a id="node-587"></a>

<p align="center"><kbd><img src="assets/d099c48ea0b674e1b04113770cf1a13a73d0e310.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là kiểu như có vector
> database mapping key = word
> với embedding vector.

<br>

<a id="node-588"></a>

<p align="center"><kbd><img src="assets/a536300d69978309b13e42aaa1627505010a376f.png" width="100%"></kbd></p>

<br>

