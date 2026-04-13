# Lab 1 - Generative Ai Use Case: Summarize Dialogue

📊 **Progress:** `24` Notes | `29` Screenshots

---

<a id="node-104"></a>
## In this lab, you will do the **dialogue summarization task using generative AI**. You will

> [!NOTE]
> In this lab, you will do the **dialogue summarization task using generative AI**. You will 
> **explore how the input text affects the output of the model**, and **perform prompt 
> engineering** to **direct it towards the task you need**. By comparing **zero shot, one shot, and 
> few shot inferences**, you will t**ake the first step towards prompt engineering** and see how 
> it can enhance the generative output of Large Language Models.  
> **The labs are accessible to learners who purchased the course. If you have not yet 
> purchased access, you can do so through the "Upgrade to Submit" button below.**
> **If you have already paid for the course, start the lab by first ticking the checkbox 
> below indicating you will adhere to the Coursera Honor Code, then click the 
> "Launch App"\\/ \\/button.**
>
> The lab is formally ungraded, but you will need to click on the **Submit** button to complete 
> the lab. This button is on the top right of the Vocareum page and **not** on the AWS 
> console.

<br>


<a id="node-105"></a>
### 1 - Set up Kernel and

> [!NOTE]
> 1 - Set up Kernel and
> Required Dependencies

<br>

<a id="node-106"></a>

<p align="center"><kbd><img src="assets/fae79fd3a751a0d2a2d390a727af7c0065f2b006.png" width="100%"></kbd></p>

> [!NOTE]
> Check Kernel

<br>

<a id="node-107"></a>

<p align="center"><kbd><img src="assets/27b46df80a14bb7150ef82b89b0c61d44e52dacd.png" width="100%"></kbd></p>

> [!NOTE]
> Install transformer,
> dataset và pytorch

<br>

<a id="node-108"></a>

<p align="center"><kbd><img src="assets/2a6d9e39624b984bf97209b25710fa1ec59280e3.png" width="100%"></kbd></p>

> [!NOTE]
> Import load_dataset,
> Tokenizer, LLM model...

<br>


<a id="node-109"></a>
### 2 - Summarize Dialogue

> [!NOTE]
> 2 - Summarize Dialogue
> without Prompt Engineering

<br>

<a id="node-110"></a>

<p align="center"><kbd><img src="assets/2b37ec8b4fe90f134b92c34c13b610eeb10b3ba8.png" width="100%"></kbd></p>

> [!NOTE]
> https://huggingface.co/docs/transformers/index

> [!NOTE]
> Ta sẽ dùng pre-trained LLM model của HuggingFace là FLAN-T5 để
> làm thử nhiệm vụ summary dialog. Trước hết ta sẽ load một dialog
> từ DialogSum dataset (cũng của HuggingFace). Mỗi dialog được
> label để có summary và topic.

<br>

<a id="node-111"></a>

<p align="center"><kbd><img src="assets/af60a5edf2da9b4d0b38aab1a7b46c1763c42bdb.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/af60a5edf2da9b4d0b38aab1a7b46c1763c42bdb.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6b0102d2a5170aba73d05c609609b718a8fb7391.png" width="100%"></kbd></p>

> [!NOTE]
> Ta thấy nó ghi "
> expert-generated", size 10k -
> 100k

<br>

<a id="node-112"></a>

<p align="center"><kbd><img src="assets/f25f050b04b33d78ad8181f7c4b73540c1191a99.png" width="100%"></kbd></p>

> [!NOTE]
> Dùng function load_dataset với
> input là tên của dataset.

<br>

<a id="node-113"></a>

<p align="center"><kbd><img src="assets/4e4989281c280d862a9f6baf442d93e08e730bbd.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái chỉ định 2 index để lấy 2 dialog trong test set của dataset. In ra
> dialogue và summary (label) để so sánh với summary của model (prediction)

<br>

<a id="node-114"></a>

<p align="center"><kbd><img src="assets/b581f862927fb0c258577a0007b9623f96118ab7.png" width="100%"></kbd></p>

> [!NOTE]
> Kế tiếp là load cái pretrained LLM model, define cái tên để bỏ vào
> AutoModelForSeq2SeqLM. from_pretrained()

<br>

<a id="node-115"></a>

<p align="center"><kbd><img src="assets/57c8807aa11dd1dc8dd7de3ccb30086a42f17513.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái dùng cái tên model đó, để load cái tokenizer cho
> nó. Có thể hiểu là mỗi model có thể có cách tokenize khác
> nhau, nên phải load cái tokenizer phù hợp. Thì tương tự,
> AutoTokenizer.from_pretrained() giúp load cái tokenizer
> tương thích với model

<br>

<a id="node-116"></a>

<p align="center"><kbd><img src="assets/eb09e1d03f01f522ffbbdcc1bdda111b51301a63.png" width="100%"></kbd></p>

> [!NOTE]
> Test thử cái tokenizer, cho một câu nào đó,
> tokenizer sẽ tokenize thành 1 tensor mỗi từ được
> đại diện bởi 1 index (trong vocab)

<br>

<a id="node-117"></a>

<p align="center"><kbd><img src="assets/77ab7a8eef78020ee8a584f4e5856c8bbc074b59.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi, cho model predict thử - generate summary mà không có cái prompt
> nào hết. Loop lần lượt trong example_indices (chứa hai cái index của 2
> data sample), dùng index, lấy data sample từ test sét (dataset['test']), và tạo
> var chứa dialogue content và label (summary). Kế tối, bỏ dialog vào
> tokenizer để tokenize. Sau đó bỏ vào model.generate() để model predict,
> để ý không có prompt gì đi kèm, và max_new_tokens = 50 để giới hạn độ
> dài. Sau đó kết quả của nó được đưa vào tokenizer.decode để in ra.

<br>

<a id="node-118"></a>

<p align="center"><kbd><img src="assets/c6efb9e54672f130c54c833e785352dd071fa9fe.png" width="100%"></kbd></p>

<br>

<a id="node-119"></a>

<p align="center"><kbd><img src="assets/2c5092539f2b58922be209318bdb09dbfd18e0a2.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là model nó không biết
> mình muốn nó làm gì, thành ra
> câu trả lời rất ất ơ.

<br>


<a id="node-120"></a>
### 3 - Summarize Dialogue with

> [!NOTE]
> 3 - Summarize Dialogue with
> an Instruction Prompt

<br>


<a id="node-121"></a>
### 3.1 - Zero Shot Inference with

> [!NOTE]
> 3.1 - Zero Shot Inference with
> an Instruction Prompt

<br>


<a id="node-122"></a>
#### In order to instruct the model to perform a task - summarize a dialogue - you can take the  dialogue and convert it into an instruction prompt. This is often called **zero shot  inference**. You can check out this blog from AWS for a quick description of what zero  shot learning is and why it is an important concept to the LLM model.  Wrap the dialogue in a descriptive instruction and see how the generated text will  change:

<br>

<a id="node-123"></a>

<p align="center"><kbd><img src="assets/ea41ec9abd4e698fa10500a834c4ab8b5d36428d.png" width="100%"></kbd></p>

> [!NOTE]
> Ok, đại khái là có thêm cái prompt, tức là không phải khơi khơi đưa dialogue vào
> model (sau khi tokenize) mà ghi thêm yêu cầu ("Summarize the ..."). Tất nhiên ta
> vẫn sẽ tokenize cái text - chứa cả promt và dialog content, trước khi đưa vào
> model

<br>

<a id="node-124"></a>

<p align="center"><kbd><img src="assets/799b2675f375a251728027aba9a33cefb7e5a3e0.png" width="100%"></kbd></p>

> [!NOTE]
> Câu trả lời đã tốt hơn.

<br>


<a id="node-125"></a>
#### This is **much better**! But the model **still does not pick up on the nuance of the conversations** though.   **Exercise:**   • **Experiment with the prompt text** and**see how the inferences will be changed.** Will the inferences change if you end the prompt with just empty string vs. Summary: ?   • Try to **rephrase the beginning of the prompt text** from Summarize the following  conversation. to something different - and see how it will influence the generated output. 

<br>


<a id="node-126"></a>
### 3.2 - Zero Shot Inference with the

> [!NOTE]
> 3.2 - Zero Shot Inference with the
> Prompt Template from FLAN-T5

<br>

<a id="node-127"></a>

<p align="center"><kbd><img src="assets/cfc03d051ff65eda5f4805e3b053993edc490210.png" width="100%"></kbd></p>

> [!NOTE]
> https://github.com/google-research/FLAN/blob/main/flan/v2/templates.py

<br>

<a id="node-128"></a>

<p align="center"><kbd><img src="assets/df7f7e7185f015151522a152613f1eee6781d409.png" width="100%"></kbd></p>

<br>


<a id="node-129"></a>
#### Notice that this prompt from FLAN-T5 did **help a bit**, but still **struggles to pick up on the nuance** of the conversation. This is what you will try to solve with the few shot inferencing

<br>


<a id="node-130"></a>
### 4 - Summarize Dialogue with One

> [!NOTE]
> 4 - Summarize Dialogue with One
> Shot and Few Shot Inference

<br>


<a id="node-131"></a>
#### One shot and few shot inference are the practices of **providing an LLM with either one or more full examples of prompt-response pairs** that match your task - **before your actual prompt**that you want completed. This is called "**in-context learning**" and **puts your model into a state that understands your specific task**. You can read more about it in this blog from HuggingFace.

> [!NOTE]
> Đại khái là cung cấp thêm ví dụ về một prompt-response pairs - kiểu
> như yêu cầu và câu trả lời mong muốn. Trước khi đưa ra prompt thật
> sự được yêu cầu. Cái này gọi là In-context learning, nếu là 1 ví dụ thì
> gọi là one-shot, nhiều thì few-shot

<br>


<a id="node-132"></a>
### 4.1 - One Shot Inference

<br>

<a id="node-133"></a>

<p align="center"><kbd><img src="assets/119d1095f53702519cc6e9f21c935f2fa879f425.png" width="100%"></kbd></p>

> [!NOTE]
> Tạo function để 'tạo prompt, để chứa 1 hoặc vài
> example (lấy từ một dialog và label khác) trước khi
> add với dialog mình muốn nó làm

<br>

<a id="node-134"></a>

<p align="center"><kbd><img src="assets/23ebb72c21bcc489dacfec9403ca7e37f22ce55c.png" width="100%"></kbd></p>

> [!NOTE]
> Tạo prompt chứa 1 shot (lấy ví dụ là
> dialog và label index 40)

<br>

<a id="node-135"></a>

<p align="center"><kbd><img src="assets/922cf0603e91012982a7f6eb43fb832e852f9d94.png" width="100%"></kbd></p>

<br>


<a id="node-136"></a>
### 4.2 - Few Shot Inference

<br>

<a id="node-137"></a>

<p align="center"><kbd><img src="assets/5974129f9e00b48ccd01d17e14460c3a3a90609e.png" width="100%"></kbd></p>

> [!NOTE]
> Lần này tạo prompt
> chứa hẳn 3 shot.

<br>

<a id="node-138"></a>

<p align="center"><kbd><img src="assets/b1f4649a872830bf5d933f16825aca322ed5b486.png" width="100%"></kbd></p>

<br>


<a id="node-139"></a>
#### In this case, **few shot** **did not provide much of an improvement** over one shot inference. And, **anything above 5 or 6 shot will typically not help much**, either. Also, you need to **make sure that you do not exceed the model's input-context length which**, in our case, if **512** tokens. Anything above the context length will be ignored.  However, you can see that **feeding in at least one full example (one shot) provides the model with more information** and **qualitatively improves** the summary overall.

> [!NOTE]
> Đại khái là cho thấy trong trường hợp này few
> shot có vẻ không giúp ích gì thêm, tuy nhiên rõ
> ràng là so với zero shot, one shot giúp model
> output tốt hơn thấy rõ.

<br>


<a id="node-140"></a>
### 5 - Generative Configuration

> [!NOTE]
> 5 - Generative Configuration
> Parameters for Inference

<br>


<a id="node-141"></a>
#### You can **change the configuration parameters** of the generate() method to**see a different  output** from the LLM. So far the only parameter that you have been setting  was **max_new_tokens**=50, which **defines the maximum number of tokens** to generate. A  **full list of available parameters** can be found in the Hugging Face Generation  documentation.   (https://huggingface.co/docs/transformers/v4.29.1/en/main_classes/ text_generation#**transformers.GenerationConfig**)  A convenient way of organizing the configuration parameters is to  use **GenerationConfig class.**

<br>


<a id="node-142"></a>
#### Change the **configuration parameters** to investigate their influence on the output.  Putting the parameter **do_sample** = **True**, you **activate various decoding strategies** which  **influence the next token** from the **probability distribution**over the**entire vocabulary**. You  can then a**djust the outputs changing temperature** and other parameters (such  as **top_k** and **top_p**).  Uncomment the lines in the cell below and rerun the code. **Try to analyze the results**. You  can read some comments below.

<br>


<a id="node-143"></a>
#### Comments related to the choice of the parameters in the code cell above:  Choosing max_new_tokens=10 will make the output text too short, so the dialogue summary will be cut.  Putting do_sample = True and changing the temperature value you get more flexibility in the output.

<br>

<a id="node-144"></a>

<p align="center"><kbd><img src="assets/0ed91d44e88c69f54de0304c16ac577bebf0f8ca.png" width="100%"></kbd></p>

<br>

<a id="node-145"></a>

<p align="center"><kbd><img src="assets/037e1b1a9447d2ed31df90310e681ee7500312eb.png" width="100%"></kbd></p>

> [!NOTE]
> max_neew_token = 10 khiến quá giới hạn, nội dụng sẽ bị cắt ngắn nhiều

<br>

<a id="node-146"></a>

<p align="center"><kbd><img src="assets/ed7ff561e63e13f242f4bd6da018e46882a53486.png" width="100%"></kbd></p>

> [!NOTE]
> với do_sample, và temperature tăng thì câu
> trả lời flexible hơn đa dạng hơn

<br>

<a id="node-147"></a>

<p align="center"><kbd><img src="assets/94c462d6074501b776c60ff80a5c77e6efca97ad.png" width="100%"></kbd></p>

<br>

<a id="node-148"></a>

<p align="center"><kbd><img src="assets/6f361301457d2eb29cbd609d306737d6fb430517.png" width="100%"></kbd></p>

<br>


<a id="node-149"></a>
### Conclusion

<br>


<a id="node-150"></a>
#### As you can see, **prompt engineering** can take you a long way for this use case, but there are some **limitations**. Next, you will start to explore how you can use **fine-tuning** to help your LLM to understand a particular use case in better depth!

> [!NOTE]
> Prompt engineering có những hạn chế, do
> đó cần phải fine-tuning model

<br>

