# Reward Hacking

📊 **Progress:** `6` Notes | `10` Screenshots

---

<a id="node-477"></a>
## Certainly, here's the content reorganized into indexed paragraphs without using titles:

> [!NOTE]
> Certainly, here's the content reorganized into indexed paragraphs without using titles:
>
> 1. **RLHF Fine-Tuning Process:**: RLHF **aligns LLMs with human preference**s through a **reward
> model**. LLM completions are assessed against human preference metrics. Reinforcement learning
> **(PPO) updates LLM weights based on rewards**. **Multiple iterations** with**various prompt**s **lead to
> desired alignment.**
>
> 2. ****Reward Hacking in RL**:** Reward hacking occurs when the **agent maximizes reward at the
> expense of original objectives**. In LLMs, it can **involve generating phrases to boost scores but
> reduce language quality**.
>
> 3. ****Reward Model Example**:** Using RLHF to detoxify model. A reward model rates toxic vs.
> non-toxic completions. Given a prompt, an LLM generates completions like "complete garbage"
> which gets a high toxic rating.
>
> 4. ****Preventing Reward Hacking**:** RLHF can **diverge from initial LLM**. Use an **unfrozen reference
> LLM (reference model) to prevent divergence**. **Compare completions from reference LLM and
> updated LLM using KL divergence**. **Penalize updated LLM if it diverges too much**.
>
> 5. ****KL Divergence Calculation**:** KL divergence **measures distribution differences**. Use it to **assess
> the divergence between LLM completions**. It's **computationally demanding** but **standard libraries**
> offer algorithms.
>
> 6. ****Applying KL Divergence**:** **Calculate KL divergence for each token**. **Add the term to reward
> calculation** to **penalize divergence from the reference model**.
>
> 7. **PEFT Adapter with RLHF and PEFT:** Use PEFT adapter for RLHF with PEFT. **Update PEFT adapter's
> weights, not full LLM**. Same underlying LLM for reference and PPO models, **reducing memory
> usage**.
>
> 8. ****Assessing Model Performance**:** After RLHF,**evaluate model's performance**. **Use
> summarization dataset for toxicity reduction assessment**. Baseline **toxicity score** from original LLM.
> **Compare scores after RLHF for improved alignment.**
>
> 9. **Conclusion:** **RLHF refines LLMs using reward models** and **reinforcement learning**. It tackles
> **reward hacking** through **reference models and KL divergence**. **Assessing alignment**using **toxicity
> scores** demonstrates success.
>
> Feel free to ask if you need further clarification or assistance!

<br>

<a id="node-478"></a>

<p align="center"><kbd><img src="assets/59b574fd2903b700d0384278c0666386dd3312a5.png" width="100%"></kbd></p>

<br>

<a id="node-479"></a>

<p align="center"><kbd><img src="assets/24da458cadedc7c8ff9d99b3289bb1fa93be6708.png" width="100%"></kbd></p>

<br>

<a id="node-480"></a>

<p align="center"><kbd><img src="assets/ea5131bcdf864a266a9a224888bb8fb694f4701b.png" width="100%"></kbd></p>

<br>

<a id="node-481"></a>

<p align="center"><kbd><img src="assets/60dc03bc6fb9070b5e4488534bf4db0a85559489.png" width="100%"></kbd></p>

> [!NOTE]
> **Reward hacking**xảy ra khi **LLM output ra sentence
> theo hướng nhằm mục đích nhận được điểm
> cao** **bất kể có đúng hay không**

<br>

<a id="node-482"></a>

<p align="center"><kbd><img src="assets/514432fe0bc52b2321de9019463744c9b7d12563.png" width="100%"></kbd></p>

> [!NOTE]
> Bằng những cách ví dụ**như cố nhét các chữ như này
> vào để có điểm cao, nhưng nội dung thì sai bét**

<br>

<a id="node-483"></a>

<p align="center"><kbd><img src="assets/70b750192d349116fd2169a6b34984bcfae1178b.png" width="100%"></kbd></p>

> [!NOTE]
> Khắc phục hiện tượng này bằng cách **dùng bản gốc của LLM** như một
> **reference model**, trong đó ta sẽ **đưa prompt vào cả Reference model và RL
> updated model** để **lấy completion của cả hai** để tính **KL Divergence Shift
> Penalty**

<br>

<a id="node-484"></a>

<p align="center"><kbd><img src="assets/141eaaa7891215d58c37b886b63ec3c64006b18b.png" width="100%"></kbd></p>

> [!NOTE]
> **Add KL Divergence Shift Penalty vào Reward**. Ý tưởng này nên hiểu đại
> khái là **khiến / giữ (penalize) cho distribution của output của RL updated
> LLM không đi xa khỏi distribution của output của model gốc** từ đó **ngăn
> việc Updated LLM tạo ra những câu trả lời quá không thực tế nhằm mục
> đích chỉ đạt Reward cao.**

<br>

<a id="node-485"></a>

<p align="center"><kbd><img src="assets/8c91dc24efadb7650bdd62da10eacde209e004df.png" width="100%"></kbd></p>

> [!NOTE]
> Quá trình này còn có thể kết hợp với nguyên lý của PEFT, tức là k**hông thay
> đổi model weight** mà chỉ **update một Low Rank weight matrix (như phương
> pháp của LoRA)** hay nói chung là **một 'lớp' weight "thêm vào" thôi**

<br>

<a id="node-486"></a>

<p align="center"><kbd><img src="assets/b6e1c52d02bb59b42d2bf4e93bcc7e226935ceb9.png" width="100%"></kbd></p>

> [!NOTE]
> Và ta sẽ có cách để**evaluate kết quả của quá trình**, bằng cách
> **đo chỉ số ví dụ 'toxicity' của model mới so sánh với model cũ**

<br>

<a id="node-487"></a>

<p align="center"><kbd><img src="assets/cb08eebf29e4738583f4ad46df7db5fda25e0f88.png" width="100%"></kbd></p>

<br>

