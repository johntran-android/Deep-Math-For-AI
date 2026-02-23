# Lecture 12: Natural Language Generation

📊 **Progress:** `60` Notes | `73` Screenshots

---
<a id="node-808"></a>

<p align="center"><kbd><img src="assets/63fcdd348ffce2aa647a5a2e1f9835946757e5f3.png" width="100%"></kbd></p>

> [!NOTE]
> Đầu tiên đại khái bạn ấy nói về NLG, bài này sẽ cho ta đến gần với việc
> hiểu được các system như ChatGPT. Thế thì NLG là một mảng của NLP,
> khi NLP bao quát hơn, gồm có Natural Language Understanding quan
> tâm đến việc xây dựng các system có thể hiểu được human language
> như dependency parsing, ..còn Nature Language Generation sẽ quan
> tâm đến việc xây dựng các system có thể tạo ra language output có tính
> chất fluent, coherent, và useful (tạm hiểu là hệ thống có thể generate
> ngôn ngữ trôi chảy, đáng tin cậy và có ích cho con người)
>
> Thế thì cái này không phải mới, và có nhiều cách tiếp cận (như ruled
> based `-` ý là dựa trên việc define những rule) tuy nhiên deep learning ra
> đời cho phép tạo ra các hệ thống mạnh mẽ hơn nhiều. Nên bài này ta sẽ
> chỉ tập trung vào deep learning NLG system

<br>

<a id="node-809"></a>

<p align="center"><kbd><img src="assets/2ee15a3bb88e6b4c95d3aac8583110915cbde3ca.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì NLG xuất hiện khắp nơi trong cuộc sống, ví dụ như Assignment 4
> mình đã làm một mô hình NMT `=` Neural Machine Translation trong đó nhận
> input là source language sentence và output là target language sentence.
>
> Rồi digital assistant system, trong đó nhận input là dialog history, và output
> sẽ nối tiếp conversation đó.
>
> Hoặc summarization, input là long document, output là summarization
>
> Tất cả đều thuộc phạm vi của NLG

<br>

<a id="node-810"></a>

<p align="center"><kbd><img src="assets/6fb9b4f40ce9fbd4a20afd9450447920baf94f1e.png" width="100%"></kbd></p>

> [!NOTE]
> Những NLG system thú vị khác dc ra đời gần đây như
> Creative stories, `Data-to-text` và visual description. Có thể
> quay lại check các paper này sau

<br>

<a id="node-811"></a>

<p align="center"><kbd><img src="assets/23d005eb90dc5c12b9407b428ce877567edd643a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/23d005eb90dc5c12b9407b428ce877567edd643a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a2bb2a182ee9862bbd2037b165fb26ea1fab04ec.png" width="100%"></kbd></p>

> [!NOTE]
> rồi ChatGPT, có thể "làm"
> nhiều loại task khác nhau.

<br>

<a id="node-812"></a>

<p align="center"><kbd><img src="assets/323fcb6f5cd1f9695935ea4c2d6065379ccb2b67.png" width="100%"></kbd></p>

> [!NOTE]
> Nói qua việc làm sao để phân loại NLG task, thì người ta sẽ dựa trên mức
> độ rộng của output space. Trong đó, những tác vụ như Machine
> Translation, Summarization có output space hẹp, có thể hiểu đại khái là vì
> ví dụ như việc dịch thuật, thì tuy rằng một câu có thể được dịch theo nhiều
> cách khác nhau, có cách hay có cách dở, có dài dòng, có vắn tắt, nhưng
> chung quy lại nó cũng không thể quá đa dạng được vì dù sao vẫn phải
> bám vào nội dung cần dịch. Tương tự với summarization cũng vậy.

<br>

<a id="node-813"></a>

<p align="center"><kbd><img src="assets/b15744104293e24fcbc0b1a033986b10762b8169.png" width="100%"></kbd></p>

> [!NOTE]
> Ngược lại, với những task như ChitChat dialog, câu trả lời
> cho một prompt có thể rất phong phú, đa dạng. Ít bị ràng
> buộc hơn

<br>

<a id="node-814"></a>

<p align="center"><kbd><img src="assets/4f7c3cd1fb1b6d208870ffde359830d31ee3a551.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi tới các task như Story generation thì
> không giới hạn trí tưởng tượng

<br>

<a id="node-815"></a>

<p align="center"><kbd><img src="assets/4adfc0c2dcd83b96082744ea02cf4a198bb387f2.png" width="100%"></kbd></p>

> [!NOTE]
> Và người ta dùng chỉ số entropy để
> chính thức hóa việc phân loại.

<br>

<a id="node-816"></a>

<p align="center"><kbd><img src="assets/6b439e7b5b4beda3f6cb452626bf9f9abe7d1eb0.png" width="100%"></kbd></p>

> [!NOTE]
> Ở đây bạn ấy review một chút về lecture 5 `-` language model, ví dụ như dùng
> RNN, trong đó tại mỗi `time-step,` dựa vào input là hidden state cũng như
> prediction của `time-step` trước đó, ta sẽ tính ra một probability distribution
> over vocabulary. Mang ý nghĩa là một conditional probability distribution thể
> hiện xác suất của token tiếp theo dựa trên các token trước đó.
>
> Trong công thức đương nhiên là hàm softmax, tính toán trên vector (có
> vocab size, kí hiệu S thuộc R^V) các class score `S_w` để chuyển thành phân
> phối xác suất.

<br>

<a id="node-817"></a>

<p align="center"><kbd><img src="assets/2830fd174dcc47bb98422eb9f571c9c3a8119059.png" width="100%"></kbd></p>

> [!NOTE]
> Thế rồi với các `non-open-ended` task (những task nằm ở khúc đầu của
> thang xếp hạng hồi nãy) như machine translation, summarization,
> người ta thường dùng kiến trúc `encoder-decoder` như ta đã làm ở
> Assignment 4. còn các task `open-ended` hơn thì người ta có thể dùng
> Autogressive decoder.
>
> Tuy nhiên cũng lưu ý rằng không có ràng buộc gì, vì `decoder-only` cũng
> có thể dùng cho machine translation và ngược lại. Vấn đề chỉ là
> convention, khi thực tế cho thấy nếu dùng `decoder-only` cho machine
> translation thì performance không tốt bằng `encoder-decoder` Còn dùng
> `encoder-decoder` cho `open-ended` task thì hiệu xuất cũng không hơn gì
> `decoder-only` system. Thành ra để hiệu quả về mặt chi phí, chẳng thà
> làm một `decoder-only` bự hơn.

<br>

<a id="node-818"></a>

<p align="center"><kbd><img src="assets/84e7645ba4a8e7a730ef557080a350ee6d065458.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì review lại **cách thức chúng ta train một language model**:
>
> Đó là dùng **maximum-likelihood estimation**, với cách tiếp cận này, ta **xây
> dựng loss function** là **negative log likelihood**:
>
> **loss tại mỗi `time-step` loss_t** là **negative log của likelihood P(y*t | {y*}<t)**.
> Công thức hay kí hiệu này không có gì khó hiểu:
>
> Tại mỗi `time-step` ta sẽ **tính ra một probability distribution over vocabulary** như
> đã nói, để **mang ý nghĩa là sự dự đoán, đánh giá của model về xác suất các từ
> khác nhau trong vocab sẽ xuất hiện tại vị trí t**.
>
> Vậy thì, nếu hiểu theo maximum likelihood, thì ta **muốn tối đa likelihood**, tức
> **tối đa giá trị của hàm mật độ xác suất tại vị trí có giá trị quan sát được `-` chính là
> y*t**, vì **đây "quả thật" là từ thật sự xuất hiện sau tại `time-step` t**, nên likelihood
> của observed sample là **p(y*_t|{y*}<t)**
>
> Và trong lúc làm ta **chỉ việc lấy giá trị tương ứng với từ y*_t từ trong vector phân
> phối xác suất dự đoán** nói trên ra, lấy log, và lấy âm, thì đó là loss tại `time-step`
> t.
>
> Và vì cách tiếp cận **Maximum Likelihood Estimation** giả định các t**oken tức
> các từ hoàn toàn độc lập** (**independent identical distribution dataset**) nên
> **likelihood của toàn training set** (ví dụ toàn bộ một câu) sẽ là**tích các
> likelihood của từng token**.
>
> Để rồi **dựa vào tính chất đồng biến của hàm log**, cho phép ta dùng **log trick**
> giúp **chuyển loss function của một câu thành tổng log loss (mà không thay đổi
> giá trị params vì minimize loss cũng chính mà minimize log loss)** tại từng
> `time-step.` Để có công thức như trong slide. Và từ đó dựa vào **gradient descent
> để train model parameter giúp giảm loss**, cũng chính là **maximize likelihood
> của training set.** Còn nói theo cách nói của **cross entropy**, thì**loss tại mỗi
> `time-step` là distance giữa hai phân phối xác suất**: **phân phối dự đoán** là
> vector phân phối xác suất output bởi hàm softmax nói trên còn p**hân phối xác
> suất thực tế** là**one-hot vector** **có số 1 tại vị trí từ y*_t** mang ý nghĩa là**toàn bộ khối lượng xác suất (probability mass tập trung tại y*_t**.
>
> Và công thức của **distance giữa hai phân phối xác suất P,Q là E[-PlogQ**] Khi
> giảm loss chính là **kéo phân phối xác suất dự đoán gần lại phân phối xác suất
> thực tế.**
>
> `=====`
>
> Rồi, gọi là **teacher forcing**, bởi, lúc training, **dù tại `time-step` `t-1,` model có "dự
> đoán" từ nào sẽ xuất hiện tại `time-step` t, gọi là y^t-1** (chú ý, `y^t-1` là sự dự đoán
> của model cho từ y*_t, được lấy bằng cách lấy cái từ ứng với xác suất dự đoán
> cao nhất trong phân phối xác suất) thì để tính loss cho dự đoán tại `time-step` t,
> **ta vẫn coi như model dự đoán đúng ở `time-step` trước, tức là cho rằng `y^_t-1` `=`
> y*t** (có nghĩa là có thể `y^t-1` khác với y*t, tức model đoán sai)
>
> Còn khi testing, đương nhiên `y^t-1` thế nào thì xài thế đó, gọi là **student forcing.**

> [!NOTE]
> Q: Autoregressive là sao? A: cơ bản là việc generate từng
> token một. Mà ở dạng cơ bản nhất là việc ta predict token,
> rồi feed nó vào tính toán để generate token tiếp theo từ trái
> sang phải một cách tuần tự

<br>

<a id="node-819"></a>

<p align="center"><kbd><img src="assets/e6d528ba48091882043aedac1e4a9fc0ac6f51ca.png" width="100%"></kbd></p>

> [!NOTE]
> Như vừa nói xong, khi inference (testing), ta sẽ từ phân phối xác suất dự
> đoán cho từ tại `time-step` t P(yt|{y<t}) , ta sẽ dùng một decoding
> algorithm kí hiệu là g() để mà "lấy ra", quyết định từ được dự đoán cho vị
> trí t. Và một cách hiển nhiên rằng ta sẽ chỉ đơn giản là chọn từ có xác
> suất cao nhất. Nhưng như đã biết từ Deep Learning Specialization ta
> cũng có thể chọn random trong top các từ có xác suất cao nhất để tạo ra
> các phiên bản có tính đa dạng hơn.
>
> Thế thì bạn ấy nói rằng cái này ta đã làm ở Assignment 4, và có thể
> improve bằng cách cải tiến decoding structure hoặc training data

<br>

<a id="node-820"></a>

<p align="center"><kbd><img src="assets/c34b60287fb7e653f0167d85c2edfa165dcc10b3.png" width="100%"></kbd></p>

> [!NOTE]
> nói về việc decoding làm cái gì, thì cơ bản là như đã biết, tại mỗi
> `time-step,` model sẽ tính một vector class scores (S thuộc R^V) có V
> number.
>
> Sau đó ta mới bỏ qua softmax để normalize chuyển thành dạng
> phân phối xác suất.
>
> Và dùng decoding algorithm để lấy ra token ứng với xác suất cao nhất
> hoặc sampling từ nhóm có xác suất cao nhất.

<br>

<a id="node-821"></a>

<p align="center"><kbd><img src="assets/ecd714c18c3503529ed6d727d1a11297c5853f70.png" width="100%"></kbd></p>

> [!NOTE]
> Nhớ lại trong lecture 7 về NMT, ta có greedy decoding là lấy token có xác
> suất cao nhất hoặc dùng Beam Search.
>
> Và tựu chung lại, maximum probability decoding như cái cái trên tỏ ra tốt
> cho các task có `low-entropy` như MT và summarization

<br>

<a id="node-822"></a>

<p align="center"><kbd><img src="assets/b5aa07237ca02021c2f8c6d26650061d6129877e.png" width="100%"></kbd></p>

> [!NOTE]
> Tuy nhiên với `open-ended` generation task như hồi nãy, thì các decoding
> strategy này có vấn đề. Ví dụ khi cho model generate từ chuỗi content
> như này, thì ban đầu có vẻ ok nhưng sau đó bắt đầu có hiện tượng lặp lại
> của tên cái tổ chức

<br>

<a id="node-823"></a>

<p align="center"><kbd><img src="assets/f80a01367a7d18a107f25c0ff128503507ee421e.png" width="100%"></kbd></p>

> [!NOTE]
> đại ý là có một hiện xảy ra có tên là `self-amplification`
> effect, trong đó khiến cho model sẽ ngày càng giảm
> loss khi nó repeat một chuỗi. Mang ý nghĩa là càng lặp
> lại một chuỗi từ nào đó thì nó lại càng tự tin rằng câu
> trả lời đó là đúng.

<br>

<a id="node-824"></a>

<p align="center"><kbd><img src="assets/60007d178e9fd756268bad524def12fe185b44f7.png" width="100%"></kbd></p>

> [!NOTE]
> có thể thấy loss giảm dần khi chuỗi i don't
> know lặp lại ngày càng nhiều

<br>

<a id="node-825"></a>

<p align="center"><kbd><img src="assets/2e3c681b29614180fd877d24fa9d6286dc014d94.png" width="100%"></kbd></p>

> [!NOTE]
> Và hiện tượng này xảy ra ở cả LSTM lẫn Transformer (openai) model.
> Chứng tỏ nó không phụ thuộc bởi mô hình nào, cũng như là scale
> model (tức dùng model lớn hơn) không giúp ích gì.

<br>

<a id="node-826"></a>

<p align="center"><kbd><img src="assets/f787bc954ddec2e54aa933063b875ecb423be296.png" width="100%"></kbd></p>

> [!NOTE]
> một số giải pháp:
>
> Option đơn giản nhất đó là dùng cách tiếp cận dựa trên kinh nghiệm: kiểu
> như hardcode một rule quy định rằng bất cứ khi nào model bắt đầu generate
> lặp lại một `n-gram` thì ta sẽ set probability thành 0, "bắt" nó phải chọn từ khác
>
> Phức tạp hơn:
>
> Dùng training objective khác `-` unlikelihood objective, nôm na là mang các cách
> "ép buộc" ở trên vào quá trình training để penalize model mỗi khi nó repeat.
>
> Hoặc dùng coverage loss: hiểu sơ là tác động vào attention mechanism
>
> Và có thể dùng các decoding objective tốt hơn như contrastive decoding `-` hiểu
> đại khái là cách này sẽ tìm string sao cho maximize log prob của hai model,
> để rồi nếu hai model đều muốn tạo ra cùng một chuỗi (tức là gây ra sự lặp lại)
> thì chuỗi đó sẽ không được chọn vì xác suất bị khử nhau.

<br>

<a id="node-827"></a>

<p align="center"><kbd><img src="assets/78cc55f64e95273284fc6877484fe6c9d3e03ca6.png" width="100%"></kbd></p>

> [!NOTE]
> Nói chung là cho thấy cách thức chọn most probable text không
> phù hợp với `open-ended` generation task
>
> Cụ thể là khi so với con người, thì chúng ta không phải lúc nào
> cũng chắc chắn, hay đưa ra câu nói mà ta chắc chắn nhất.

<br>

<a id="node-828"></a>

<p align="center"><kbd><img src="assets/5ce0b54e54581c73920bbe7ca8a9888ece199bb9.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì giải pháp có thể là sampling từ một distribution tính
> toán ra, thay vì chọn cái có xác suất cao nhất.

<br>

<a id="node-829"></a>

<p align="center"><kbd><img src="assets/592aea525e023956ebf54135668eb155ee3732af.png" width="100%"></kbd></p>

> [!NOTE]
> Tuy nhiên sampling from distribution dự đoán cũng bộc lộ nhiều vấn đề. Đại
> khái là theo lí thuyết, việc sampling sẽ nên dễ chọn được các từ mà xác xuất
> tính toán cao hơn các từ mà xác suất tính toán thấp.
>
> Tuy nhiên, bởi vì bộ vocab có rất nhiều từ, nên cho du model huấn luyện tốt
> để rồi có thể đưa ra phân phối xác suất tập trung nhiều vào một số từ phù
> hợp nào đó, nhưng với quá nhiều từ có xác suất tuy rất nhỏ nhưng cộng lại
> cũng sẽ rất đáng kể `-` nôm na là, xác suất tập trung vào một số từ không đảm
> bảo rằng khi sampling, nó ưu tiên chúng hơn, vì cái đám có xác xuất thấp rất
> đông (the long tail), hợp lại cũng thành một khối lượng xác suất đáng kể.
>
> Chính vì vậy, giải pháp là `top-k,` cắt cái `long-tail` này đi, chỉ sampling trong tốp
> K từ có xác suất cao nhất thôi

<br>

<a id="node-830"></a>

<p align="center"><kbd><img src="assets/97291f1a45fff656a8e64434cb09f09a174764d7.png" width="100%"></kbd></p>

> [!NOTE]
> K sẽ là hyperparameters, khi K lớn, kiểu như số option sẽ mở rộng, 
> giúp tăng tính đa dạng nhưng cũng tăng rủi ro có thể chọn những 
> từ có xác suất thấp
>
> Ngược lại, giảm K, giả tính đa dạng như output sẽ có vẻ chắc hơn,
> ít rủi ro hơn.

<br>

<a id="node-831"></a>

<p align="center"><kbd><img src="assets/023c5b0c798c16d75b8bfaa9ba3ae57bb735d10b.png" width="100%"></kbd></p>

> [!NOTE]
> và việc chọn K như thế nào cũng chính là vấn đề. có khi K được chọn
> sẽ là quá hẹp, để rồi distribution bị cắt bớt quá nhanh, bỏ đi rất nhiều
> từ có thể đủ tốt để được chọn. Nhưng ở trường hợp khác có thể nó lại
> quá rộng, để rồi chứa nhiều từ hoàn toàn không phù hợp

<br>

<a id="node-832"></a>

<p align="center"><kbd><img src="assets/10fa6ae8a9fc0e656a77600813fe455504b70190.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì vấn đề này xảy ra có nguyên nhân là bởi nếu probability
> distribution có dạng dàn trải, hình dung một dải đất cao trải dài, nơi
> có nhiều token có xác suất xem xem như, thì khi đó ta muốn cho K
> lớn để cho phép sampling từ một khoảng rộng hơn. Ngược lại, nếu
> xác suất phân phối có dạng tập trung (peaky) vào một số ít hơn các
> từ, thì ta sẽ muốn thu hẹp K để không chứa những từ có xác suất
> thấp.
>
> Thành ra solution là không quan tâm K mà quan tâm đến xác suất, 
> Ta sẽ `top-p,` sampling trong top p khối lượng xác suất cộng dồn: nôm
> na là sampling trong một khúc chứa phần lớn xác suất.

<br>

<a id="node-833"></a>

<p align="center"><kbd><img src="assets/f868af200e375ee5711f85c2ff15a3b85436a446.png" width="100%"></kbd></p>

> [!NOTE]
> Do đó nó sẽ có hiệu ứng như việc ta có các
> K khác nhau tùy vào probability distribution
> khác nhau (adaptive k)

<br>

<a id="node-834"></a>

<p align="center"><kbd><img src="assets/dd53c7e082f8abdd18fc2ce0df02aa3a09c1a631.png" width="100%"></kbd></p>

> [!NOTE]
> ngoài ra còn có Typical Sampling trong đó đại khái là người ta sẽ
> gán lại probability weight (reweight score) dựa trên **entropy của
> distribution** `-` nôm na là tùy vào loại task là closed hay
> `opened-end` generation (nôm na là yêu cầu nghiêm chỉnh như
> summarization, machine translation, hay cho phép sáng tạo hơn
> như chitchat).
>
> Hoặc Epsilon Sampling, do anh bạn John Hewitt dạy ở bài trước
> nghiên cứu, trong đó kiểu như ta sẽ dùng threshold để loại bỏ
> những từ có xác suất thấp dưới ngưỡng nào đó

<br>

<a id="node-835"></a>

<p align="center"><kbd><img src="assets/74e1308c69c56f85867bf4229d32004b4dc81d64.png" width="100%"></kbd></p>

> [!NOTE]
> thì khái niệm **entropy của distribution, là cái Shannon Entropy mà mình đã
> được biết trong DLYo.**Trong đó, nói một cách ngắn gọn thì đại khái là giá
> trị kì vọng của lượng thông tin thu được khi xảy ra event `X=x,` kí hiệu là I(x)
> và I(x) được tính bằng công thức I(x) `=` `-log` P(x)
>
> ```text
> Nên Shannon entropy = E x~P(x) [I(x)] = E x~P(x) [- log P(x) ]. và vì trong
> ```
> hoàn  cảnh mà ai cũng hiểu x tuân theo phân phối P(x) thì có thể viết gọn là
> `E` `[-log` P(x)] như bạn giảng viên này ghi.
>
> Thế thì cái chính để nhớ về cái này đó là, information có được khi quan sát
> một event `X=x,` kí hiệu `I(X=x)` sẽ là đại lượng mà người ta muốn nó cao khi
> sự kiện khó, hiếm xảy ra và ngược lại, nếu sự kiện chắc chắn xảy ra thì ta
> muốn I(x) `=` 0
>
> Và quả thật có thể lấy ví dụ nhanh một binary distribution (hay Bernouilly
> distribution) có hai giá trị khả dĩ là `X=1` và `X=0.` Thế thì, dựa theo công thức
> ta sẽ thấy, nếu sự kiện có xác suất xảy ra cao, thì entropy sẽ thấp, và ngược
> lại như sau:
>
> ```text
> Ta có H(x) = E[I(x)] = I(X=1)*P(X=1) + I(X=0)*P(X=0)
> ```
>
> ```text
> = I(X=1)*p + I(X=0)*(1-p)
> ```
>
> ```text
> = [-log P(X=1)]*p + [-log P(X=0)]*(1-p) = -(log p)*p - [log(1-p)]*(1-p)
> ```
>
> ```text
> Khi p->1, H(x) -> - log(1) = 0
> ```
>
> ```text
> Khi p->0, H(x) -> - log(1) = 0
> ```
>
> ```text
> Khi p->0.5, H(x) -> -(log0.5)*0.5 -(log0.5)*0.5 = -log0.5 = 0.693
> ```
>
> `===`
>
> Như vậy, nếu probability distribution dàn trải, gần với uniform (nơi mà mọi
> xác suất bằng nhau hết) thì entropy của distribution sẽ lớn.
>
> Ngược lại nếu distribution tập trung, hay họ dùng từ spiky, thì entropy sẽ
> nhỏ. Đây cũng là điều bạn giảng viên nói đến ở đây

<br>

<a id="node-836"></a>

<p align="center"><kbd><img src="assets/12a54d5f0f5e9e7f9886782587a0f81a2876c079.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi, ta gặp lại một cái trong LLMSpec, đó là temperature. Đại khái là ta có
> thể dùng một hyperparameter tau để scale các scores trước khi apply softmax
>
> Bằng cách này, ta không làm thay đổi tính chất monotonic `-` ý là nếu s1 > s2,
> thì `s1/tau` vẫn sẽ lớn hơn `s2/tau` (vì tau dương), nhưng nó sẽ giúp làm thay đổi
> so sánh tương đối của chúng từ đó làm mềm đi (flatter, dàn trải bớt) distribution
> hoặc khiến cho distribution trở nên tập trung hơn, spiky hơn.
>
> Và nó có thể được tuned bằng beam search và sampling.

<br>

<a id="node-837"></a>

<p align="center"><kbd><img src="assets/b88468bc71809fe433cc996053ff50ed182403f0.png" width="100%"></kbd></p>

> [!NOTE]
> tiếp theo, đại khái là ngay cả khi ta đã có những nỗ lực để cải thiện chất
> lượng của quá trình decoding (sampling) thì vẫn có thể xuất hiện các
> sequence tệ. Do đó, người ta còn làm thêm vụ này: `re-ranking,` ngắn gọn
> là sampling ra một vài kết quả, sau đó dùng một hoặc nhiều chỉ số nào đó
> giúp đánh giá chất lượng của sequence như perplexity đã học ở bài
> trước, để "chấm điểm" và xếp hạng các sequence theo điểm từ cao tới
> thấp, rồi mới lấy  cái có điểm cao nhất.
>
> Tuy nhiên phải lưu ý là không nên chỉ dựa vào chỉ số perplexity cao nhất,
> lí do là vì như vậy ta có thể sẽ đánh giá sai khi như đã thấy một model chỉ
> chọn những sequence dựa trên probability cao nhất có thể chọn một
> chuỗi câu lặp đi lặp lại. Nên có thể dùng nhiều loại chỉ số, đánh giá các
> khía cạnh khác nhau để thành một chỉ số "combo" và dùng nó để ranking.
>
> Có câu hỏi về perplexity, thì cái này ta đã học ở mấy bài trước, về cơ bản
> Perplexity thấp thì tốt `-` nó sẽ tương đương với log probability cao

<br>

<a id="node-838"></a>

<p align="center"><kbd><img src="assets/57121cd5d52f5cd1c58c8eff765959bca606cf1b.png" width="100%"></kbd></p>

> [!NOTE]
> tóm lại, decoding vẫn đang là một thách thức của NLG đang được nghiên 
> cứu sôi nổi hiện nay
>
> Ngoài ra ta nên biết thêm có nhiều thuật toán decoding cho phép ta "đưa"
> vào, tiêm vào (Inject) một số bias nhằm khuyến khích một số tính chất nào
> đó trong generated text.
>
> Một số những nghiên cứu có ảnh hưởng quan trọng gần đây trong NLP
> chính là về decoding

<br>

<a id="node-839"></a>

<p align="center"><kbd><img src="assets/774eebc474224f1f8769208273b5890dc86b2c88.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp theo qua
> training NLG models

<br>

<a id="node-840"></a>

<p align="center"><kbd><img src="assets/29646e80e34c15c506817f1147eeee7015290c1c.png" width="100%"></kbd></p>

> [!NOTE]
> Ok, đại ý là nãy giờ ta cố gắng cải thiện cái vấn để repetition này bằng
> cách cải thiện các decoding algorithm.
>
> Tuy nhiên vấn đề gốc vẫn là **quá trình training model như thế nào đó
> khiến cho nó assign xác suất cao cho các chuỗi repetition** như vậy

<br>

<a id="node-841"></a>

<p align="center"><kbd><img src="assets/0a041d0f78037b95b59cce5ff360d2f41a34d6fd.png" width="100%"></kbd></p>

> [!NOTE]
> Vấn đề nó nằm ở chỗ: Như đã biết việc training language model dựa
> trên cách tiếp cận thông dụng của machine learning: **Maximum
> Likelihood Estimation**: (nói một cách ngắn gọn) ta sẽ thay đổi xây dựng
> o**bjective function** tạo bởi, dùng bởi **likelihood function** parameterized
> by model, cụ thể là **likelihood của observable sample (training set)**
> mang ý nghĩa là **khả năng xuất hiện của các sự kiện  quan sát được, ghi
> nhận được (observable data)**để rồi từ đó dùng **gradient ascent** để **maximize objective function**
> hay  chuyển thành loss function là negative log likelihood để dùng gradient
> descent
>
> Đối với**language model** the likelihood sẽ được xây dựng là một
> **conditional probability density function** `-` **khả năng xuất hiện của một
> từ** **dựa trên một chuỗi từ** trước đó. `P(y_t|{y}<t)`
>
> Và **mấu chốt là**, trong đây, **khi "tính" likelihood function của `time-step`
> t** (cũng là để từ đó chuyển thành **loss tại `time-step` t**, lấy bằng
> **negative log likelihood của observed token y*t**),..
>
> ..ta đã **cho nó một giả định rằng**, các **từ trước đó đã đúng** bằng cách
> **đưa vào model chuỗi {y*}<t** là chuỗi từ "target" hay ở đây biết thêm được gọi
> là "gold context".
>
> Đây là khái niệm **teacher forcing** như đã biết, và điều này có nghĩa là khi
> predict token tại t, nó **DỰA TRÊN CONTEXT CHUẨN**
>
> Trong khi đó, lúc generating, thì input vào model lại là dự đoán của model
> ở các `time-step` trước đó, thành ra likelihood tại `time-step` t sẽ là
> P(y^_t|{y^}_<t), và vì là prediction, nên có thể sai, để rồi khi dự đoán token
> tại t, nó sẽ **PHẢI DỰA TRÊN CONTEXT CÓ SAI SÓT**
>
> Thì cái **giả định nhắc đến ở trên** đã tạo ra một bias: gọi là **Exposure
> Bias**-****có cái tên như vậy ý là lúc training với teacher forcing, ta đã **TIÊM
> VÀO MỘT BIAS RẰNG MODEL LUÔN CÓ CONTEXT TỐT, KHÔNG
> PHẢI DEAL VỚI NHỮNG SAI SÓT CỦA NÓ Ở CÁC STEP TRƯỚC** 
> để rồi **thực tế khi làm việc thì không được vậy**

<br>

<a id="node-842"></a>

<p align="center"><kbd><img src="assets/80ea6805cb0c339b8fa0743818e171c15de9d47a.png" width="100%"></kbd></p>

> [!NOTE]
> Có vài giải pháp đó ví dụ như Scheduled sampling của Yoshua Bengio đại
> khái là trong lúc training, ta sẽ có thể cho model dự đoán tại step t dựa
> trên dự đoán của nó trước đó thay vì gold context theo lối teacher forcing.
> Và cụ thể hơn, ta sẽ kiểm soát "mức độ" thực hiện việc này, bằng một
> tham số xác suất p với ý nghĩa là nếu p nhỏ, thì kiểu như lâu lâu mới làm
> vậy, còn p lớn thì luôn luôn dùng prediction của model làm input.
>
> Để rồi khi training người ta sẽ cho p nhỏ, để model vẫn được predict dựa
> trên gold context như thường lệ, nhưng sau đó p sẽ được tăng dần lên để
> cuối cùng hoàn toàn là model phải predict dựa trên prediction của nó `-`
> trạng thái khi đó sẽ giống như lúc generating.
>
> Có điều nhược điểm là nó khiến mất ổn định việc training khi training
> objective kiểu như không nhất quán, model không biết phải hướng tới cái
> gì.
>
> `====`
>
> Cách thứ hai là dataset aggregation (DAgger): nôm na là người ta sẽ
> **đưa prediction của model trộn với training sample**, để dùng nó cho
> training. Giúp **kéo hai distribution của prediction data và training data lại
> gần nhau**====
>
> Cũng là và về cái này lát nữa có câu hoỉ thì bạn này giải thích thêm rằng:
> Hai cái này tương đối giống nhau, chỉ khác là Dagger kiểu như train
> model với teacher forcing xong một epoch, sau đó bỏ prediction của nó
> vào training set để train epoch tiếp theo" thì cơ bản cũng khá giống việc
> chuyển qua lại giữa teacher forcing và student forcing của Scheduled
> sampling nhưng Dagget có vẻ như flexible hơn ở khía cạnh "insert model
> prediction ở đâu"

<br>

<a id="node-843"></a>

<p align="center"><kbd><img src="assets/dfdda12cb316a0e9284927dccaaf30137dbc3571.png" width="100%"></kbd></p>

> [!NOTE]
> một số nghiên cứu tìm cách đưa ra giải pháp cho vấn đề này bao gồm
> Retrieval Augmentation `-` model sẽ được train để học cách "truy xuất,
> trích xuất" từ một bộ dữ liệu ("của" con người `-` `human-written`
> prototypes) và sau đó sẽ chế cháo từ đó.
>
> Cách này giúp giải quyết Exposure Bias bởi lẽ quá trình training và
> inference, model đều sẽ chỉ trích xuất thông tin từ con người và viết lại từ
> đó, thay vì "viết lại từ đầu" `-` vốn gây ra sự khác nhau giữa training và
> inference do teacher forcing
>
> `===`
>
> Giải pháp khác là dùng Reinforcement Learning (không nói rõ hơn)

<br>

<a id="node-844"></a>

<p align="center"><kbd><img src="assets/af2caeb878450df22dae06a081b1448ca4835930.png" width="100%"></kbd></p>

> [!NOTE]
> đại khái là khi dùng Reinforcement Learning, trong đó ta sẽ define reward
> function. Thì đại ý ở đây chú ý là, ta sẽ nhiều khả năng cũng dùng các
> metric giúp đánh giá performance của mô hình trong các nhiệm vụ cụ thể
> (như BLEU score cho Machine Translation, ROUGE score cho
> Summarization) làm reward function.
>
> Tuy nhiên phải cẩn thận, vì các metric đó đại khái đều chỉ nên coi là (ước
> lượng) cho sự đánh gía của con người, có nghĩa là, nó không hoàn toàn
> thay thế được thước đo bởi con người, hay nói cách khác BLEU score cao
> chưa chắc đã là bản dịch tốt.
>
> Do đó, cẩn thận vấn đề**reward hacking** `-` khi model tìm cách nào đó để đạt
> được điểm cao ở các metric đó nhưng chất lượng thật sự khi ta xem xét
> kết quả và đánh giá nó bởi "human metric" thì thấy nó không tốt hơn là bao
>
> (Có thể hiểu là cái lecture này đi trước lecture Reinforcement Learning from
> Human Feedback, mà mình đã học ở bài trước)

<br>

<a id="node-845"></a>

<p align="center"><kbd><img src="assets/85ab17dc6e95ba0371bdd57bfb1d3b5e19c87187.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ta có thể thiết kế reward function sao cho nó sẽ khuyến
> khích model Cho ra text có các tính chất như liệt kê ở đây. Và cũng
> nói đến technique RLHF đã học ở bài trước

<br>

<a id="node-846"></a>

<p align="center"><kbd><img src="assets/2ec29b786cb7aa957517914fccf7f9ea17b7535e.png" width="100%"></kbd></p>

> [!NOTE]
> Tóm lại cách tiếp cận chính để training text generation model vẫn là
> Teacher Forcing, tuy nhiên nó tạo ra Exposure Bias `-` do lúc inference,
> model phải "Dựa vào các prediction của chính nó trước đó để dự đoán
> token tiếp theo (Student forcing) trong khi lúc training, nó được cung cấp
> gold context khi làm  việc này `-` teacher forcing"
>
> Các giải pháp để khắc phục vấn đề có thể là Scheduled sampling `-` cho
> model "chuyển dần" từ teacher forcing sang student forcing. Hoặc Dagger
> `-` trộn dự đoán của model với human data để làm training set giúp "kéo gần
> hai data distribution"
>
> Ngoài ra còn có Retrieval generation trong đó model sẽ retrieve và edit
> một human text.
>
> Cuối cùng là dùng Reinforcement Learning, mà trong nổi bật là RLHF đã
> học ở bài trước.

<br>

<a id="node-847"></a>

<p align="center"><kbd><img src="assets/a59a721477ac2c0d983777204414bce3095ed5fb.png" width="100%"></kbd></p>

<br>

<a id="node-848"></a>

<p align="center"><kbd><img src="assets/112f7dd6f65ffc702744a132ae160c2fd966be4d.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là nói qua việc đánh giá text generation system, thì cách thứ nhất đó là
> dùng các chỉ số trong đó nó tính toán sự giống nhau về từ vựng, từ nguyên
> (lexical) giữa generated và `gold-standard` text.
>
> Cách này nhanh và hiệu quả nên được dùng phổ biến. Ví dụ như BLEU score
> đối với bài toán MT, ROUGE score với Summarization

<br>

<a id="node-849"></a>

<p align="center"><kbd><img src="assets/9b3c4cd852a6773893c79b1e3eefbbfb2474b717.png" width="100%"></kbd></p>

> [!NOTE]
> Tuy nhiên cách này (nói chung là `content-overlap` metric, và nói riêng là
> `n-gram` overlap là các BLEU score, ROUGE score...) chỉ tỏ ra hiệu quả
> với các `closed=ended` task `-` ý là những tác vụ mà kiểu như có target, có "
> như thế nào là tốt nhất" , còn khi mức `open-ended` ngày càng lớn thì cách
> làm này tỏ ra không chính xác. Do đó với Machine Translation, dùng
> BLEU score vẫn đánh giá tốt được chất lượng nhưng với Summarization,
> Chat, Story telling thì dần dần không hiệu quả.

<br>

<a id="node-850"></a>

<p align="center"><kbd><img src="assets/54e6f20d24569225fece89e7925693bb05f9285c.png" width="100%"></kbd></p>

> [!NOTE]
> đại khái là một ví dụ đơn giản để cho thấy ở đây dùng các
> `n-gram` overlap metric sẽ không đánh giá đúng.
>
> Khi đánh giá câu trả lời cho câu hỏi này thì, dù câu cuối hoàn
> toàn sai, nhưng score của nó vẫn cao vì vẫn có lexical overlap
> với câu mẫu.

<br>

<a id="node-851"></a>

<p align="center"><kbd><img src="assets/1a02008b3e6d02bfd8d715231b4348468391d67e.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì cái failure case vừa rồi gợi cho mình đến những bài giảng đầu tiên
> của quá trình xây dựng một bài toán sentiment analysis, trong đó người ta
> cũng bắt đầu với các phương pháp đơn giản như đếm tần suất xuất hiện
> của các positive, negative word (các từ trong positive `/` negative corpus)
> và khi đó cũng dễ thấy hạn chế của nó giống như cái này.
>
> Nên một cách tự nhiên ta sẽ muốn dùng embedding để mà đánh giá
> sự giống nhau giữa generated text và reference text.

<br>

<a id="node-852"></a>

<p align="center"><kbd><img src="assets/fed013024bc8d10c3159101eab2161387cca51db.png" width="100%"></kbd></p>

> [!NOTE]
> thế thì có nhiều cách làm:
>
> Với vector similarity, ta sẽ tạo embedding của hai sentence và so sánh, đo
> độ gần, giống giữa chúng bằng các similarity metric như cosine similarity,
> l2 distance...
>
> Word Mover's distance thì kiểu như cũng tính "distance" giữa hai câu nhưng
> đo bằng tổng distance giữa các cặp từ tương ứng.
>
> BERT Score: Đại khái là pass mỗi câu qua BERT để lấy "BERT embedding"
> rồi dùng distance metric để tính khoảng cách.
>
> Nói chung chi tiết có thể tìm hiểu sau, nhưng ý chính là dùng embedding
> để so sánh.

<br>

<a id="node-853"></a>

<p align="center"><kbd><img src="assets/647382bd7585d56c33666225d28f59ce297ef74e.png" width="100%"></kbd></p>

> [!NOTE]
> một số cách khác, again, có thể tìm hiểu chi tiết sau. Cái BLEURT ở
> dưới kiểu như một regression model dựa trên BERT, dự đoán một
> con số chất lượng của sentence

<br>

<a id="node-854"></a>

<p align="center"><kbd><img src="assets/2c9206dfc55f71996a937e1c7453e7d326873b79.png" width="100%"></kbd></p>

> [!NOTE]
> Qua các metric để đánh giá. `Open-ended` text generation, là những
> task mà ta biết dùng các cách thức lexical overlap hay embedding
> similarity cũng không hiệu qủa

<br>

<a id="node-855"></a>

<p align="center"><kbd><img src="assets/3a0b338941f235712c4c9ec90483f78c906d36ea.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3a0b338941f235712c4c9ec90483f78c906d36ea.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b0e259b548342c2d67404fd55963347b5298d9c0.png" width="100%"></kbd></p>

<br>

<a id="node-856"></a>

<p align="center"><kbd><img src="assets/55481dd2c1df3ee0ec1e4a0dc5a84178f9e0dcc9.png" width="100%"></kbd></p>

> [!NOTE]
> đại khái là thế nào là một metric tốt, hay, làm sao để đánh giá
> metric: Dễ hiểu là đương nhiên ta dùng metric để đánh giá
> model là dựa trên việc muốn model làm được những gì con
> người muốn nó làm. Vậy metric đương nhiên phải phản ánh
> việc "như thế nào thì con người cho là tốt" `-` Do đó, metric tốt
> là khi nó correlate với "human score".
>
> Biểu đồ cho thấy, với BLEU score, nó không correlate với
> human score (đánh giá các `open-ended` text generation), điều
> đó thể hiện trong các task này, BLEU score không phải là
> metric phù hợp.

<br>

<a id="node-857"></a>

<p align="center"><kbd><img src="assets/623e3167039630f73796ff511de64d4b236627c8.png" width="100%"></kbd></p>

> [!NOTE]
> Do đó yêu cầu khi thiết kế một "automatic metric" là nó phải correlate
> với human evaluation

<br>

<a id="node-858"></a>

<p align="center"><kbd><img src="assets/86d9b5b110ed44d6986c2aad9a604718355e62e0.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì human evaluation là sao, hay triển khai như thế nào để có
> human  evaluation?
>
> Đó là hỏi `/` nhờ con người (human annotator) đánh giá chất lượng của
> generated text thôi.
>
> Tuy nhiên phải cụ thể dựa theo các tiêu chí như fluency (tạm gọi là tính
> chất trôi chảy), coherence `/` consistency (tính chất nhất quán), factuality
> and correctness (tính đúng, tính chính xác), common sense....
>
> Thì mỗi task có thể ta ưu tiên tính chất `/` khía cạnh nào hơn. Ví dụ như
> với summarization ta cần tính factuality & correctness, hay style và
> common sense với story generating.
>
> Cuối cùng họ chú ý ta không nên so sánh human evaluation score ở các
> study khác nhau vì human evaluation có xu hướng có tính chất không
> không nhất quán, và `non-reproductible` (ý là mỗi lần kết quả đánh gía có thể 
> ra mỗi khác)

<br>

<a id="node-859"></a>

<p align="center"><kbd><img src="assets/d0d39c6419b72793a7336edaa2bbc5b8c67ce98f.png" width="100%"></kbd></p>

> [!NOTE]
> Ngay cả khi ta cho rằng human judgement là gold standard thì nó vẫn rất đắt và
> chậm. Cũng như là có nhiều nhược điểm như :
>
> `-` không nhất quán (mỗi lẫn mỗi khác, mỗi người đánh giá mỗi khác)....
>
> `-` human annotator có thể hiểu sai về tiêu chí mình mong muốn họ đánh giá
>
> `-` human evaluation chỉ đánh gía precision chứ không đánh giá được recall:
>
> precision, như trong context của classification mà ta đã học nó là `TP/TP` `+` FP:
> để đánh giá**: trong các dự đoán là positive**, **thì bao nhiêu phần trăm là đúng
> `-` true positive**.
>
> Thì ở đây ý là **trong các text được generated bởi model (có thể hiểu các
> generated text là những text mà nó dự đoán là tốt, positive)** thì**có bao nhiêu
> phần trăm là tốt thật.** Thì cái này human evaluation có thể giúp để xác định
> kiểu như à trong 10 bản summarization mà nó cho ra, thì có 3 trong số đó là
> good.
>
> Còn với **recall** (hay **sensitivity**) hay dịch là**độ nhạy**, sẽ đo bằng
> `TP/TP+FN` với ý nghĩa là**trong mọi case là positive,** thì **dự đoán đúng, phát
> hiện ra được bao nhiêu phần trăm**.
>
> Thế thì với human evaluation, đương nhiên là không thể đánh giá được kiểu
> như là **trong mọi bản summarization tốt có thể có trên đời** thì **model có khả
> năng cho ra bao nhiêu cái.**Bởi lẽ với các task opened như này, làm sao ta
> biết có bao nhiêu bản tóm tắt tốt có thể có, hay dễ hình dung hơn là với model
> với nhiệm vụ tạo ra story thì làm sao biết được có bao nhiêu good story có thể
> có để mà đánh giá khả năng cho ra bao nhiêu phần trăm trong đó của model.
>
> Do đó, dù là human evaluation, thì cũng chỉ đánh giá được precision, chứ
> không đánh giá được recall

<br>

<a id="node-860"></a>

<p align="center"><kbd><img src="assets/98e761be38e26c6cd277842a7cd25044bff141ea.png" width="100%"></kbd></p>

> [!NOTE]
> đại khái là người ta phát triển một số cách để tích hợp
> human judgement vào

<br>

<a id="node-861"></a>

<p align="center"><kbd><img src="assets/0b6a15810e11b86d6e922b65f3623c984ec35305.png" width="100%"></kbd></p>

> [!NOTE]
> không nói rõ, chỉ lướt qua,
> nên sẽ tìm hiểu sau

<br>

<a id="node-862"></a>

<p align="center"><kbd><img src="assets/1c74f95cdf3b97254be8aa161be11ba91563314d.png" width="100%"></kbd></p>

<br>

<a id="node-863"></a>

<p align="center"><kbd><img src="assets/e97be18aaeea7f215d61702ebf52da4bd4a951d3.png" width="100%"></kbd></p>

> [!NOTE]
> Tóm lại, các thước đo dựa trên `content-overlap` có thể cung cấp một khởi
> đầu nào đó để đánh giá generated text, nhưng nó bộc lộ nhiều hạn chế khi
> task có tính chất mở `(open-ended)`
>
> Kế tới ta có thể dùng các `model-based` metric, `-` có thể giúp đánh giá tốt hơn
> nhưng cũng khó interpretable hơn.
>
> Còn `human-judgement` thì tốt nhất nhưng nó cũng chưa hoàn hảo, ví dụ như
> nó có thể không nhất quán.
>
> Cuối cùng, họ cho rằng người đánh giá tốt nhất chính là bản thân mình. Nên
> nếu final project có làm về Text generation model thì nên tự xem xét chất
> lượng của các generated text chứ không nên dựa dẫm vào các automatic
> metric

<br>

<a id="node-864"></a>

<p align="center"><kbd><img src="assets/e328d16ad28f0b0aabf953ac6ca9905dd68d6b06.png" width="100%"></kbd></p>

<br>

<a id="node-865"></a>

<p align="center"><kbd><img src="assets/5f9e2618eb54db110b85a36e8a0ca1d1c54beccf.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/5f9e2618eb54db110b85a36e8a0ca1d1c54beccf.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/83043d4053db3eb70ac301041f0ce0f4d497980c.png" width="100%"></kbd></p>

> [!NOTE]
> đại khái là phần cuối sẽ nói đến khía cạnh đạo đức (ethical). Ví dụ khi ta hỏi
> ChatGPT bảo nó tạo toxic content thì nó sẽ không trả lời. Do OpenAI đã huấn
> luyện nó để tuân theo các tiêu chuẩn đạo đức của con người (thông qua RLHF)
>
> Tuy nhiên vẫn có thể có cách để jailbreak

<br>

<a id="node-866"></a>

<p align="center"><kbd><img src="assets/3ff4f8260678c7d87d3b305b2606a9fb1b890222.png" width="100%"></kbd></p>

> [!NOTE]
> Hoặc vẫn còn tồn tại factual errors `-` model vẫn có thể đưa ra câu trả lời sai

<br>

<a id="node-867"></a>

<p align="center"><kbd><img src="assets/b1692901ee8ef2b7ef9f84260b69f265e9d239cb.png" width="100%"></kbd></p>

> [!NOTE]
> Đại ý là những bias vốn xuất phát từ quá trình model được
> `pre-train` với data trôi nổi trên internet, do đó solution có thể
> là clean data tốt hơn. Dù vậy, rất khó để clean một lượng
> data quá lớn vì quá tốn kém

<br>

<a id="node-868"></a>

<p align="center"><kbd><img src="assets/103232a1545349ea23e2a1ba6c38895afb7fd61f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/103232a1545349ea23e2a1ba6c38895afb7fd61f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6725e27d469618bf9fd603d6d09d61e289e559e7.png" width="100%"></kbd></p>

> [!NOTE]
> rồi, có một vấn đề nữa kiểu như một số kiểu input có thể trigger model
> generate content rất toxic. Và nó có thể bị khai thác với ý đồ xấu.
>
> Nên ý chính là phải rất cẩn thận trước khi deploy model

<br>

<a id="node-869"></a>

<p align="center"><kbd><img src="assets/3f24ca5cba7c8c050e2006f5611dcb3bd449f8bd.png" width="100%"></kbd></p>

> [!NOTE]
> Tóm lại là lời kêu gọi phải suy nghĩ kĩ
> về những gì mình đang cố gắng tạo ra
> ở khía cạnh đạo đức

<br>

<a id="node-870"></a>

<p align="center"><kbd><img src="assets/b75318bbe3c26834bcc996d0b8b4dec40b8a9d85.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b75318bbe3c26834bcc996d0b8b4dec40b8a9d85.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/45fad9abd9a1bf9c005b06abc6154e0e690e1366.png" width="100%"></kbd></p>

> [!NOTE]
> Một số concluding thoughts bao gồm đại ý là 
>
> i) thật ra nếu xem xét kĩ, ta sẽ thấy các hệ thống như ChatGPT còn rất
> nhiều hạn chế, do đó với vai trò là người "trong nghành AI" ta còn rất nhiều
> cơ hội hay thứ có thể làm.
>
> ii) Các thước đo để đánh giá mô hình AI còn rất nhiều thách thức phải giải
> quyết.
>
> iii) Đây là thời điểm tốt để tham gia lĩnh vực AI vì những bước tiến của
> lĩnh vực này đã giúp mọi chuyện trở nên dễ hơn so với trước đây.
>
> iv) Cuối cùng là NLG là một trong những phân vùng thú vị nhất của NLP

<br>

