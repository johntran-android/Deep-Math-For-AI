# Lab3 Walkthrough

📊 **Progress:** `14` Notes | `16` Screenshots

---

<a id="node-501"></a>
## In the described lecture, the process of detoxifying a language model using

> [!NOTE]
> In the described lecture, the process of detoxifying a language model using 
> Reinforcement Learning from Human Feedback (RLHF) is summarized in the following 
> steps:
>
> 1. **Introduction and Purpose:**
>    - The purpose of the lab is to**lower the toxicity of an instruction fine-tuned model** from 
> a **previous lab (Lab 2)** using**RLHF.**   - The goal is to **optimize for "not hate" using a hate speech reward model.**
>    - **Proximal Policy Optimization (PPO)** will be employed for the **RLHF process.**
>
> 2. ****Library Installation:****
>    - Required Python libraries are imported, including**PyTorch, transformers, datasets, 
> and more.**
>    - A new library called **"trl"** is introduced, which **provides access to PPO functionality.**
>
> 3. ****Model and Data Setup**:**
>    - Loading of the **pre-trained models from Lab 2 (Peft model)** and a**Facebook binary 
> classifier for hate speech detection.**
>    - Creating a **sentiment pipeline for sentiment analysis** using **hugging face's inference 
> pipelines.**
>
> 4. ****Toxicity Evaluation**:**
>    - **Setting up a toxicity evaluation mechanism** using the**Facebook RoBERTa hate speech 
> model.**
>    - **Determining** the**toxicity score for sample nontoxic and toxic texts**.
>
> 5. **Initializing **PPO Trainer**:**
>    - **Initializing a PPOTrainer** with specific configurations (e.g., **learning rates, batch size**).
>    - Setting up a **reference model for KL divergence comparison** to **prevent reward hacking** 
> during training.
>
> 6. ****Fine-tuning with RLHF**:**
>    - Utilizing the **PPOTrainer** to **fine-tune the model using RLHF**.
>    - **Passing prompt-response pairs**and**their associated not_hate scores** to the **PPOTrainer.**
>    - **Minimizing KL divergence** and **maximizing advantage** during PPO training.
>
> 7. ****Quantitative and Qualitative Comparison**:**
>    - **Comparing the model's response quality** before and after**fine-tuning using toxicity evaluation**.
>    - Using **sentiment pipeline to classify prompt-response pairs** and **measuring not_hate scores.**
>    - **Showing qualitative comparisons of model responses before and after detoxification**.
>
> 8. **Results and Conclusion:**
>    - Observing that, after PPO fine-tuning with the hate speech reward model, the**overall 
> toxicity of model responses is reduced.**
>    - Acknowledging that **for greater differences**, starting with a**relatively toxic dataset is beneficial.**
>
> Overall, the process involves**fine-tuning the model using Proximal Policy Optimization** and 
> the**feedback from the hate speech reward model** to **minimize toxicity**and **optimize for generating 
> responses that are less likely to contain hate speech**. The result is a model that **produces less 
> toxic outputs based on quantitative and qualitative evaluations.**

<br>

<a id="node-502"></a>

<p align="center"><kbd><img src="assets/9818666e368389ef2b043ed085be13bdf49ef84c.png" width="100%"></kbd></p>

> [!NOTE]
> Mục tiêu của lab 3 là 'detoxify' model đã train ở lab 2 -
> tức làm cho nó tuân thủ nguyên tắc không tạo ra những
> câu trả lời toxic - bằng RLHF

<br>

<a id="node-503"></a>

<p align="center"><kbd><img src="assets/77f2fb14c3819ec0cb35aae5df7224dec4e4f408.png" width="100%"></kbd></p>

> [!NOTE]
> Import một số lib như bữa trước như transformer,
> dataset, evaluate, rouge_score để evaluate model,
> peft để " Parameterized Efficient Fine Tuning', đặc
> biệt có thêm trl giúp Reinforcement Learning

<br>

<a id="node-504"></a>

<p align="center"><kbd><img src="assets/d6eb65734c132a82e983952aec5d5f17496b8c8c.png" width="100%"></kbd></p>

> [!NOTE]
> Một số component đặc biệt có cái mới là AutoModelForSequenceClassification giúp nhận
> một string of text và predict cho ta biết có chứa hated speech hay không. Rồi thì
> load_dataset, PeftModel, PeftConfig, LoraConfig từ peft. Rồi từ trl thì PPOTrainer,.... Đặc
> biệt có cái LengthSampler giúp kiểu như giúp tự động lấy ra một đoạn sampling không
> quá 512
>
> Rồi những component quen thuộc như evaluate, np, pandas, tqdm - cái này ổng nói giúp
> tạo cái progress bar.

<br>

<a id="node-505"></a>

<p align="center"><kbd><img src="assets/53fa716e41737ff5990de37337c7bbf072f2a6df.png" width="100%"></kbd></p>

> [!NOTE]
> Load dataset

<br>

<a id="node-506"></a>

<p align="center"><kbd><img src="assets/e23e8a0ff8cf9d0ccf0980c60619ecbb211885e2.png" width="100%"></kbd></p>

> [!NOTE]
> Download pre-trained model

<br>

<a id="node-507"></a>

<p align="center"><kbd><img src="assets/1675e8837d32f6e3b2c36eea47944856f33c6ab6.png" width="100%"></kbd></p>

<br>

<a id="node-508"></a>

<p align="center"><kbd><img src="assets/59ae50ca1e5633e37bd125334a0241cfcf2fd014.png" width="100%"></kbd></p>

> [!NOTE]
> Reference model để prevent reward hacking

<br>

<a id="node-509"></a>

<p align="center"><kbd><img src="assets/1ecb824aebadf27bdf7dac21b50c3fa3f345112b.png" width="100%"></kbd></p>

> [!NOTE]
> Load pre-trained 'ROBERTA-based hate
> speech model' của Facebook sẽ dùng làm reward model

<br>

<a id="node-510"></a>

<p align="center"><kbd><img src="assets/fa3dad18a65ee3267dce046aef870c3d9aab3cb3.png" width="100%"></kbd></p>

> [!NOTE]
> Cái này là cái model nói ở trên giúp đánh giá độ toxicity (ví dụ ở đây là
> sự thù ghé) của input text. Ổng lưu ý nhấn mạnh rằng chỉ số positive -
> không toxic nằm ở vị trí thứ 0. Đại khái là vì ta sẽ lấy output (ở dạng
> logits) để làm reward nên nếu lấy sai sẽ khiến RLHF ra một model còn
> toxic bạo nữa.
>
> Thì cái này sẽ chính là Reward model

<br>

<a id="node-511"></a>

<p align="center"><kbd><img src="assets/1ff7ab0e590c5fc01d39a516a24974bb9fac6086.png" width="100%"></kbd></p>

> [!NOTE]
> Đoạn này nói về cái gọi là 'Inference Pipeline' kiểu như là một cái rất tiện lợi từ
> HuggingFace's transformer. Ta chỉ cần define 'loại' task mà ta muốn cùng với tên model,
> thì từ đó chỉ việc 'dùng' - như gọi và bỏ vào đó input text không cần phải lo về việc
> tokenize, ....rồi gọi các function của model như generate hay predict gì cả rất handy

<br>

<a id="node-512"></a>

<p align="center"><kbd><img src="assets/eedb90104cb8ef99a5f75a7555e6ee92787f1717.png" width="100%"></kbd></p>

> [!NOTE]
> Đây là dùng lib evaluate để đánh
> giá tính toxicity của model

<br>

<a id="node-513"></a>

<p align="center"><kbd><img src="assets/ba86bb5ccf7840ad8547f154fd88ca5aee265851.png" width="100%"></kbd></p>

> [!NOTE]
> Đây là cái sẽ update LLM model
> bằng RL algorithm đây.

<br>

<a id="node-514"></a>

<p align="center"><kbd><img src="assets/86d6dc28812630bb2252d21c4851894be36a2eaa.png" width="100%"></kbd></p>

> [!NOTE]
> Ref_model để làm cái
> vụ 'KLDivergence'

<br>

<a id="node-515"></a>

<p align="center"><kbd><img src="assets/b61cf2f20e29515d620dbbbd0e3e981793f56973.png" width="100%"></kbd></p>

> [!NOTE]
> Quá trình RLHF

<br>

<a id="node-516"></a>

<p align="center"><kbd><img src="assets/c98c59f3a429b59f23ca6741182567ec539a9cfa.png" width="100%"></kbd></p>

<br>

<a id="node-517"></a>

<p align="center"><kbd><img src="assets/a7d10ad0833c40cf207686fa302d3641dceabf04.png" width="100%"></kbd></p>

> [!NOTE]
> Đánh giá kết quả

<br>

