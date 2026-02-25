# Lecture 2: Neural Classifiers

📊 **Progress:** `31` Notes | `39` Screenshots

---
<a id="node-101"></a>

<p align="center"><kbd><img src="assets/3793fc5e1425c21a180f561173eb874fd655c7f1.png" width="100%"></kbd></p>

> [!NOTE]
> "Mục tiêu là sau lecture này các bạn sẽ tự tin mà
> đọc các paper như word2vec, glovec...." Chris Manning

<br>

<a id="node-102"></a>

<p align="center"><kbd><img src="assets/6b66da36f4a434f9bc794abcc7ca97ffb5772da2.png" width="100%"></kbd></p>

> [!NOTE]
> Như bài trước đã học, bằng cách cho máy tính **dự đoán từ context** **dựa
> trên từ center word**, và quá trình training nó tìm cách **giảm loss**define
> bằng**log likelihood** nó sẽ**"learn" bộ word embedding** sao cho**các từ
> vựng nằm gần nhau** sẽ có ý nghĩa giống nhau mà hơn nữa còn **nắm bắt
> được các yếu tố ngữ nghĩa** cũng như các hướng vector có ý nghĩa (ví dụ
> man - woman sẽ mang ý nghĩa giới tính)

<br>

<a id="node-103"></a>

<p align="center"><kbd><img src="assets/c78d8cb1ff15989339fee548e0c99cd3fb3938dc.png" width="100%"></kbd></p>

> [!NOTE]
> Đại ý là những phương pháp này gọi là **bag of words models**. Nôm
> na là nó **không quan tâm nhiều lắm đến vị trí của các context word là
> trước  hay sau**...Nó c**hỉ quan tâm các từ có xuất hiện gần nhau hay
> không**
>
> Và một điều là ta sẽ không nói đến các giá trị p 0.3, 0.5 mà sẽ là những
> giá trị nhỏ như 0.01, vì có rất nhiều từ có thể xuất hiện cùng nhau (nôm na
> là**cho một center word thì sẽ có rất nhiều từ có thể xuất hiện trong
> context của nó**) nên**chia ra thì  P rất nhỏ** (dù là so sánh tương đối với
> các từ ít xuất hiện quanh từ center  word đó là cao)

<br>

<a id="node-104"></a>

<p align="center"><kbd><img src="assets/81355e15355fd9b5e20a286985c6f730af2dc06f.png" width="100%"></kbd></p>

> [!NOTE]
> Đại ý là Word2Vec algorithm trong quá trình training sẽ tìm cách**tweak các params (mà ở đây chỉ là các word embedding)** sao cho
> **những từ gần nghĩa nhau** sẽ **nằm gần nhau trong vector space** thì
> sẽ khiến giảm loss và đạt objective function.
>
> Và thầy Manning lưu ý ta rằng ở đây mình đang xem là dùng **PCA** để
> giảm chiều xuống 2D, tuy nhiên**trong không gian high dimension của
> word embedding thì có thể nó sẽ khác** - 2 từ gần nhau ở 2D có thể thật
> ra là cách rất xa nhau trong không gian gốc

<br>

<a id="node-105"></a>

<p align="center"><kbd><img src="assets/831bccb17f56a4e9e0bad68ec57349d122bd09ed.png" width="100%"></kbd></p>

> [!NOTE]
> Về G.D đã biết rồi khỏi nói lại

<br>

<a id="node-106"></a>

<p align="center"><kbd><img src="assets/170d599fe9d1f38ee674bcbdd197acde97776c05.png" width="100%"></kbd></p>

<br>

<a id="node-107"></a>

<p align="center"><kbd><img src="assets/6a94eb36e3effaa928450260a73a5574d107e5cd.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là như ta đã biết bên **MLSpec** đó là **gradient descent** nếu nói
> chính xác thì đó **batch gradient descent** - tức là ta sẽ **tính gradient**  =
> **derivative của loss** w.r.t **params** với l**oss tính trên toàn bộ data
> sample** mà ở đây là **toàn bộ center words**, và cũng đồng nghĩa là
> **toàn bộ training corpus** và có thể lên tới hàng trăm nghìn từ.
>
> Thì làm vậy như ta cũng đã biết là sẽ khiến **một lần tính để update params
> sẽ mất rất nhiều thời gian**. Tuy là kiểu như ta **sẽ đi theo hướng đúng
> nhất** về đáy thung lũng n**hưng mỗi bước sẽ phải tính rất lâu**.
>
> Thì do vậy mà thay vào đó nên dùng **stochastic G.D** hoặc **mini-batch
> G.D** trong đó ta tính gradient (derivative của loss function w.r.t params)
> **dựa trên một hoặc vài data sample thôi, và gọi nó là ước lượng của
> gradient (chính xác)**
>
> Và vì **chỉ là ước lượng** của gradient chính xác (mà muốn tính phải tính
> trên toàn bộ training set) nên **nó sẽ không chính xác**,**có lúc rất sai**,
> nhưng cũng có lúc đúng và dẫn đến **nó khiến ra đi xuống đồi theo nhiều
> hướng khác nhau mỗi lần**, mà trong đó có thể có những lúc đi rất sai (so
> với hướng đúng phải đi).
>
> Nhưng **được cái là ta sẽ tốn rất ít thời gian cho một lần "đi"**. Và vì **dù đi
> rất nhiều bước chệch choạc nhưng đi nhiều lần nhìn chung vẫn giúp ta
> xuống đồi nhanh hơn là "suy nghĩ một hồi lâu thiệt lâu chọn ra hướng đi
> đúng nhất" rồi mới bước.**

<br>

<a id="node-108"></a>

<p align="center"><kbd><img src="assets/ea98ab38ad95c0ebaf2bb53808d70a8818add16d.png" width="100%"></kbd></p>

> [!NOTE]
> Và thêm một ý là mr Chris nói dù SGD có vẻ như là
> hack/trick nhưng thật ra không phải vậy, sự noisy của
> nó thật sự có thể giúp model học tốt hơn chứ không
> chỉ là converge nhanh hơn

<br>

<a id="node-109"></a>

<p align="center"><kbd><img src="assets/94ba51750139ffde6371c82dcd4f3a088f078e92.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là với SGD vì **mỗi lần ta chỉ "tính trên 1 sample = 1
> center words"** để ra gradient (partial derivative) của loss đối với
> params = word embedding của vài từ context của center word
> đó. Nên**vector derivative vốn sẽ chứa tất cả params = tất 
> cả các word embedding của các words sẽ phần lớn là 0.**
> Nên rất **sparse** = trống trải.

<br>

<a id="node-110"></a>

<p align="center"><kbd><img src="assets/1ed4a0bc272bd7407eabd23d909f84dd7ac141ea.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là thầy nói nếu chỉ **nghĩ theo phương diện toán học** thì **cứ
> việc thực hiện phép tính cộng trừ vector hay matrix** trên matrix (V,
> d) mỗi row là một word embedding vector.
>
> Nhưng **để tối ưu tính toá**n thì ta phải **nghĩ đến việc làm sao chỉ
> thực hiện việc update trên vài row mà đang "tính" thôi.**
>
> Và một chi tiết nữa là trong **Pytorch mỗi word embedding là một
> row**Và một điểm đáng chú ý nữa đó là thầy nói nếu các bạn biết về 
> memory thì sẽ hiểu tại sao người ta làm vậy vì khi đó **mỗi row chứa
> một vector của data sample sẽ nằm trên các byte kế tiếp nhau** trên
>  memory máy tính giúp **hiệu quả hơn**

<br>

<a id="node-111"></a>

<p align="center"><kbd><img src="assets/cb4a5ae8cf2f2801b3fc7faef3144550b32739a7.png" width="100%"></kbd></p>

> [!NOTE]
> Đầu tiên đại khái là ta cuối cùng ta sẽ **average hai vector của mỗi từ** một
> cái khi từ đó đóng vai center word, một cái khi nó đóng vai context word, để**trở thành một vector duy nhất cho từ đó.**
>
> Thứ hai, thày nói là**thật ra có thể dùng chỉ một vector cho một từ và thật
> sự làm vậy hiệu quả hơn** nhưng có cái là khiến quá trình thực hiện t**rở
> nên rối khi ta tính đạo hàm.**Rồi tiếp theo thì đại khái là không chỉ có một algorithm duy nhất mà thật ra
> **có nhiều cách làm**, trong số đó là **skip gram** như thầy vừa nói mấy bữa
> nay và **CBOW** là cái mình đã học trong NLPSpec trong đó thay vì cho
> trước center  word bắt đoán outer context word thì ta sẽ cho model đoán
> center word dựa trên bag of context words. Cả hai **đều cho cùng kết quả.**
>
> Cuối cùng đó là tuy lí thuyết là vậy nhưng thực tế khi tính với softmax như
> trên thì sẽ **không hiệu quả (tính toán)**. Do đó thực tế người ta dùng **"
> negative sampling"**

<br>

<a id="node-112"></a>

<p align="center"><kbd><img src="assets/b1c52d3eb47b2b8bbc1835ed1762fd47f01644d2.png" width="100%"></kbd></p>

> [!NOTE]
> Thì đại khái là vầy, ta **vẫn muốn maximize độ giống nhau giữa hai word 
> vector của center word và context word**, bằng cách **maximize
> dot product giữa chúng**. Tuy nhiên **thay vì xây dựng objective function
> là maximize P(o|c) bằng softmax** trong đó ta **phải tính dot product của 
> center word với mọi từ khác trong vocab**, **rất tốn kém**, thì ở đây ta sẽ
> xây objective function **với hàm sigmoid** như vầy.
>
> Trong đó việc maximize function này sẽ **encourage model maximize
> uoTvc bởi vế đầu giúp khiến context word và center word vector
> giống nhau**. Còn vế sau ta hiểu là ta sẽ**lấy random k từ NOT context
> word**, và model sẽ **minimize độ giống nhau của center word và các từ
> "sai" này.**
>
> Chú ý ở đây là objective function **Jt(theta) với mỗi center word t** , 
> và objective function (cho mọi word) sẽ là**average của mọi Jt(theta)**====
>
> Nói thêm rằng dù khi chọn k random words có thể ta vẫn đôi khi chọn được
> từ vốn là cũng nên similar với context word (vì có thể nó cùng xuất hiện với
> trong bối cảnh center-context khác) nhưng 99% là ta sẽ chọn những từ "không
> context" nên mọi việc vẫn ok.

<br>

<a id="node-113"></a>

<p align="center"><kbd><img src="assets/b142e41e0ecd8dc14594b4b91bed81a57e5bf5b5.png" width="100%"></kbd></p>

> [!NOTE]
> Và c**huyển objective function thành cost function**
>
> Có **một vài trick** mà trong DLSpec ông Andrew cũng có nói đó là người
> ta sẽ **dùng cách sample sao cho giảm việc các từ quá thông dùng được
> chọn và tăng khả năng chọn của các từ hiếm**. Thầy Cris cũng chỉ nói
> lướt qua sơ sơ là bằng cách dùng **unigram distribution** = tính toán
> bằng**tần suất xuất hiện của từ**. Và **lũy thừa 3/4 như vậy để thu hẹp
> khoảng cách giữa các từ hiếm và thông dụng** giúp khi random sampling
> không bị chỉ chọn toàn từ thông dụng.

<br>

<a id="node-114"></a>

<p align="center"><kbd><img src="assets/d5e80b42d567156c4fb15eba441f671d512c46d4.png" width="100%"></kbd></p>

> [!NOTE]
> Xong mới đặt câu hỏi là sao không làm đơn giản là t**hống kê
> các lần các từ xuất hiện cùng nhau** để tạo thành co-occurrence
> table

<br>

<a id="node-115"></a>

<p align="center"><kbd><img src="assets/746f2967bd8c8a34a2f0642d166e7acb645032ce.png" width="100%"></kbd></p>

> [!NOTE]
> Ví dụ như cái**co-occurrence table** như này. đơn giản chỉ là đếm số lần các
> từ xuất hiện cùng nhau, có thể trong context window là vài từ hoặc cả
> document
>
> Thì đại khái là nếu dùng dạng window, tức chỉ "tính" phạm vi hẹp vài từ thì ta
> có thể có được "**syntactic & semantic information**" - tức là nó cũng có thể
> giúp ta nắm bắt được ít nhiều thông tin về ngữ nghĩa, cú pháp của từ vựng
>
> Còn nếu dùng ở "**cấp document**" thì nôm na là ta sẽ có thông tin về sự gần
> gũi của các từ ở cấp "topic", tức là các từ nào cũng trong một phạm vi một
> chủ đề nào đó. Dẫn đến một lĩnh vực gọi là Latent Semantic Analysis

<br>

<a id="node-116"></a>

<p align="center"><kbd><img src="assets/9f02b52f474f1b4394f4dacdac73fb2f81b5518f.png" width="100%"></kbd></p>

> [!NOTE]
> Tuy nhiên nếu dùng vector bằng cách này (ví dụ như bảng trên, mỗi hàng
> là  vector của một từ) thì sẽ **rất "sparse"** = trống khi ta thấy nó sẽ**rất nhiều
> số 0 và nó rất dài** (bằng số lượng vocab) = **số dimension rất lớn**.
>
> Hệ quả là như ta cũng đã nghe nói (dù chưa hiểu rõ lắm) đó là **một số
> model làm việc không tốt với sparse vector.**
>
> Từ đó ta quay lại khẳng định rằng thực tế chứng minh rằng**dùng "dense"
> vector thấp chiều hơn, "dense" hơn (mà được tạo bằng các phương pháp
> như word2vec) sẽ mang lại hiệu quả hơn.**

<br>

<a id="node-117"></a>

<p align="center"><kbd><img src="assets/12f7565ee06fb827af069ed1d5aa9f75e05b9d00.png" width="100%"></kbd></p>

> [!NOTE]
> Nói về phương pháp dùng SVD để giảm chiều vector
> (dimensionality reduction)

<br>

<a id="node-118"></a>

<p align="center"><kbd><img src="assets/ea0b1a74b5ff774d83e1704cbb7ceea20bc0053b.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là nếu dùng**raw-counts** tức là bảng thống kê co-occurrence 
> nguyên gốc thì sẽ không work tốt, lí do là có quá nhiều từ mang ý nghĩa 
> **"chung chung"** như the, he, has sẽ có tần suất xuất hiện cao, khiến gây
> nhiễu thông tin. Do đó mới nói là **sẽ tốt hơn nếu scale các chỉ số lại
> ví dụ như dùng log**, dùng cách giới hạn hạn mức hoặc là bỏ luôn các từ
> chung chung như vậy (function words) 
>
> Một số cách khác nữa là dùng window nhỏ, và use **Pearson correlation**

<br>

<a id="node-119"></a>

<p align="center"><kbd><img src="assets/e2d4068c36a4e7b9c38a07ee207e886061d96c30.png" width="100%"></kbd></p>

> [!NOTE]
> Thì đại khái là cũng cho thấy một số kết qủa mang hơi
> hướng giống như king-queen-man-woman

<br>

<a id="node-120"></a>

<p align="center"><kbd><img src="assets/3642c3ba3fc648c4ff2aa75f6dfab631172c0731.png" width="100%"></kbd></p>

<br>

<a id="node-121"></a>

<p align="center"><kbd><img src="assets/7b9948705583e1946cefd2f6e5904d821af1631a.png" width="100%"></kbd></p>

<br>

<a id="node-122"></a>

<p align="center"><kbd><img src="assets/9be7dafca0041f99067b998a06cd53fe4f181e5e.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là nói về một nhận định quan trọng trong nỗ lực tìm cách "**thể hiện các
> khái niệm trừu tượng**" gọi là "meaning component" ví dụ như**hướng thay đổi từ
> man sang woman** (mang ý niệm giới tính), hay **solid sang gas**, mang **ý niệm trạng
> thái vật lí.**
>
> Thì đại khái là nếu ta chỉ dùng (cách tính) xác suất một từ xuất hiện gần từ "ice" là
> một từ mang thể rắn trong vậy lí- P(solid | ice) và lập luận rằng vì solid mang giá
> trị cao để thể  hiện rằng nó**mang ý nghĩa của thể rắn** thì sẽ không ổn. Vì như đây
> ta thấy với "water" thì nó cũng hay xuất hiện bên cạnh "ice" nên P(water|ice) cũng
> cao trong khi đó water có thể là dạng hơi hoặc dạng lỏng nữa.
>
> Tương tự, nếu chỉ dựa vào P(gas|steam) cao thì nôm na là **chưa đủ để biểu thị  ý
> nghĩa gas là thể hơi**. Vì P(water|steam) cũng cao.
>
> Tuy nhiên người ta nhận thấy **nếu dựa vào tỉ lệ của P(x|ice)/P(x|steam)** thì ta sẽ
> thấy rõ ràng rằng với solid, nó có tỉ lệ cao, với gas nó có tỉ lệ rất nhỏ. Còn water và
> fashion thì đều ~= 1
>
> Từ đó cho thấy rằng dùng tỉ lệ, sẽ làm rõ thông tin rằng **từ solid là từ mang ý nghĩa
> rắn rất cao**, và **gas là từ mang ý nghĩa hơi** (như steam) rất cao còn **water thì
> fashion là trung tính**, không thiên hẵn về bên nào.
>
> Và tóm lại ta có thể**dựa vào tỉ lệ này để xem thử 1 từ thiên về hướng nào trong
> spectrum từ solid -> gas**

<br>

<a id="node-123"></a>

<p align="center"><kbd><img src="assets/58aeccf3fc3be5317b89bb662ccf65947fa96349.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là vì ta đã biết dot product của hai vector uo, vc sẽ thể hiện**xác suất của
> việc chúng xuất hiện cùng nhau**, đúng hơn là log của xác suất vì khi ta tính xác
> suất, p(o|c) ta dùng softmax, trong đó ta exp(uoTvc). Mà nói lại cho nhớ thêm đó
> là bởi ta xuất phát từ một nhận định quan trọng đó là **ý nghĩa của một từ sẽ được
> định nghĩa bằng các từ gần nó**, từ đó **nếu hai từ hay xuất hiện gần nhau thì ý
> nghĩa của chúng cũng gần gũi nhau, giống nhau**. Nên từ đó ta xây dựng
> objective function sao cho nếu xác xuất chúng xuất hiện cùng nhau cao thì **hai
> vector của chúng phải trở nên giống nhau**,  gần gũi nhau trong không gian
> embedding vector. Thì hai vector gần nhau thì dot product của chúng sẽ lớn
> (cũng như khi tính Cosine similarity trong đó có dot product)
>
> Do đó để tính P(x|a)/P(x|b) sẽ bằng **wx.(wa-wb)**
>
> Thì đại khái là GloVec muốn **kết hợp cái gọi là Co-occurrence matrix** trong các
> phương pháp xây dựng word vector theo thống kê (statistic) như mấy cái bên trái
> của cái bảng trước. **Và phương pháp xác suất như CBOW,  Word2Vec** ở bên
> phải bảng trước. Do đó học xây dựng objective function như vầy.
>
> Cái f(Xij) từ từ nói, nói cái Xij trước, nó là chỉ số co-occurrence của từ w_i và từ
> w_j trong co-occurrence matrix. Thì đương nhiên nếu hai từ hay xuất hiện cùng
> nhau thì chỉ số này cao.
>
> Thì vế bên phải mang ý định nôm na là: À, hay tweak word embedding vector
> của w_i và w_j sao cho **nếu hay từ này xuất hiện cùng nhau nhiều** thì **dot
> product của chúng phải cao tương ứng** (để rồi trừ nhau mới nhỏ lại). Bình
> phương lên để kiểu **khuếch đại error lên như trong MSE**. Hai cái **b là bias term**
> không  có gì, đương nhiên model cũng sẽ tìm ra hai chỉ số này.
>
> Cuối cùng quay lại f**(Xij)**đại khái chỉ là một function để ta **khống chế các từ thông
> dụn**g, bên DLSpec có nói đó là để g**iảm chênh lệch giữa các từ thông dụng và
> các từ ít thông dụn**g.Theo GPT thì người ta hay dùng **sigmoid**, trong đây Crist có
> nói**f(Xij)**dùng để **"cap" mức ảnh hưởng của các từ thông dụng**. Nhìn công thức
> mình hiểu rằng, **nếu (những từ wi và wj mà có Xij lớn thì phải cho model tập
> trung vào nó, tức là dùng Xịj như trọng số để ưu tiên hơn / nhấn mạnh hơn các
> cặp từ hay xuất hiện cùng nhau)**. Nhưng **phải hạn chế nó, bằng cách dùng f(Xij)
> để cho nó (Xij) có lớn mấy thì mức ảnh hưởng vào objective function cũng chỉ =
> 1 thôi**
>
> Và một cái ở đây Crish không nói nhưng Andrew có nói đó là tránh việc X**ij = 0
> sẽ khiến logXij = log0 bị lỗi**

<br>

<a id="node-124"></a>

<p align="center"><kbd><img src="assets/b171b92f68707602f436a643febf6535262d57a3.png" width="100%"></kbd></p>

> [!NOTE]
> Và kết quả là nó cho word vector rất tốt khi những từ
> này (gần nhau trong không gian) thì đúng đều là những
> loài ếch khác nhau

<br>


<a id="node-125"></a>
## Ở đây có người hỏi đại khái là tại sao việc dùng các chỉ số statistic

> [!NOTE]
> Ở đây có người hỏi đại khái là tại sao việc dùng các chỉ số statistic
> (co-occurrence matrix) lại là cons là ưu điểm hỗ trợ cho Skip-gram
>
> Thì đại khái đó là vì, trong skipgram như ta đã thấy, quá trình sẽ là ta
> di chuyển các window qua hết corpus, để tại mỗi window ta có center
> word và context words. Để rồi nôm na là tại mỗi window ta mới biết từ
> nào là hay xuất hiện với từ nào.
>
> Còn bằng cách sử dụng co-occurrence matrix, ta đã có sẵn à là từ
> này hay xuất hiện nhiều với từ kia, nên sẽ kiểu như "trực tiếp hơn", ta
> khỏi phải đi từng window mà có thể làm "at once" dẫn đến hiệu quả
> hơn trong training

<br>

<a id="node-126"></a>

<p align="center"><kbd><img src="assets/0aca7ea783e1ccf75491690850e1918412b9e3ed.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là nói về các cách để đánh giá word vector mà cũng là các khía
> cạnh khác trong ML.
>
> Cái này cũng đã biết qua bên MLOpsSpec, thì đại khái là intrinsic nôm na
> là ta đánh giá bằng các task cụ thể (specific) được thiết kế riêng cho việc
> đánh giá word vector. Ưu điểm là nhanh, nhưng nhược điểm là nó mang
> tính cục bộ, ta không biết được kiểu như là à, word vector đánh giá bằng
> cách này ok rồi, nhưng liệu khi mang nó vào các ứng dụng ngoài đời
> thực thì nó có giúp cải thiện performance của chúng không.
>
> Còn extrinsic thì ngược lại, đó là đánh giá chất lượng của word vector
> thông qua việc xem nó có giúp cải thiện các ứng dụng cụ thể thực tế
> (như dịch thuật, semantic search) Nhược điểm là phải xâu dựng ứng
> dụng cuối thì mới đánh giá được, nên lâu. Và nếu performance có tốt lên
> hay dở đi thì cũng không chắc là do word vector tốt lên hay đơn giản chỉ
> vì những cái component khác làm việc tốt hơn so với cái cũ

<br>

<a id="node-127"></a>

<p align="center"><kbd><img src="assets/15f8c2e5c1deb5fee08e5207e94f704228fc5c02.png" width="100%"></kbd></p>

> [!NOTE]
> Ví dụ điển hình của intrinsic evaluation là có có man to woman thì từ
> king tìm ra cái gì, và ta expect sẽ ra queen.
>
> Ở đây mr Chris nói một cái trick đó là,  khi các bạn tính wMan -
> wWoman + wKing rồi tìm nearest neighbor của kết quả đó thì khả
> năng đó là bạn sẽ lại thấy từ King, nên cái trick là là đừng có include
> từ king khi search.

<br>

<a id="node-128"></a>

<p align="center"><kbd><img src="assets/fe6228fe1e0df25ac03ec7ce1f4f1ee269951aad.png" width="100%"></kbd></p>

<br>

<a id="node-129"></a>

<p align="center"><kbd><img src="assets/a5bbf24390426e070208d0f17aa58f2f89094fb6.png" width="100%"></kbd></p>

<br>

<a id="node-130"></a>

<p align="center"><kbd><img src="assets/1f187da2bc66ca8f77a35e40ae53c5dbca345afd.png" width="100%"></kbd></p>

<br>

<a id="node-131"></a>

<p align="center"><kbd><img src="assets/964cc08cd1252b0ed6ef105bf5563d02a77aafc4.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là bảng tính các chỉ số đánh giá word vector ở khía
> cạnh Semantic và Syntatic. Cho thấy GloVe đạt performance
> cao nhất, sau đó là SkipGram và CBOW
>
> Ở khúc trên SVD (bài trước đã nói, là dùng phương pháp 
> dựa trên co-occurence table, cho thấy nếu không scale, tức
> giảm ảnh hưởng của các từ thông dụng xuống thì performance
> rất tệ, nhưng khi scale thì cải thiện hơn hẳn

<br>

<a id="node-132"></a>

<p align="center"><kbd><img src="assets/abf189ae77e121b2973b84c690943d14632e07e9.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là nói về ảnh hưởng của**data lên performance**. Khi model
> train trên**Wiki data** có **semantic scores cao hơn** còn model train trên
> **google news** thì có**syntactic score cao hơn**. Và model train bằng web
> crawl (lấy hết data trên internet) thì tốt hơn cả ở hai khía cạnh.

<br>

<a id="node-133"></a>

<p align="center"><kbd><img src="assets/25bdff86d67829b2354180d9e373674d51bbf6eb.png" width="100%"></kbd></p>

> [!NOTE]
> Còn cái biểu đồ này cho thấy tại sao ta hay thấy người
> ta dùng dimension 300. Vì nhiều hơn thì  nó không hẳn
> là tốt hơn nữa

<br>

<a id="node-134"></a>

<p align="center"><kbd><img src="assets/c7cce4c81e0181c5f8ba591d377dd9eff95b6b3b.png" width="100%"></kbd></p>

> [!NOTE]
> Một cách intrinsic word vector evaluation nữa đó là dựa trên
> các đánh gía (do con người làm) về độ tương đồng của các từ

<br>

<a id="node-135"></a>

<p align="center"><kbd><img src="assets/a844efb61edf4a2d70a70f28a0bc65ffd55a9da8.png" width="100%"></kbd></p>

<br>

<a id="node-136"></a>

<p align="center"><kbd><img src="assets/bca90d74c855add3da44d4c02aa38806dfc4d445.png" width="100%"></kbd></p>

<br>

<a id="node-137"></a>

<p align="center"><kbd><img src="assets/b9f4378374a2fe04001e09235b2cc19be02bf7c5.png" width="100%"></kbd></p>

> [!NOTE]
> Nói đến vấn đề đặt ra là **từ vựng thường có nhiều nghĩa khác nhau** khi
> ở các n**gữ cảnh khác nhau** thì làm sao 1 vector có thể capture mọi ý
> nghĩa đó

<br>

<a id="node-138"></a>

<p align="center"><kbd><img src="assets/375d4115c67b8fd27d3f7b801dcc719d265ef7a9.png" width="100%"></kbd></p>

> [!NOTE]
> Ví dụ như từ pike có nhiều nghĩa khi ở các
> ngữ cảnh, lĩnh vực khác nhau

<br>

<a id="node-139"></a>

<p align="center"><kbd><img src="assets/3932464d4341944ac568b92e3add77d18c564197.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là nói đến việc dùng mỗi word vector cho
> mỗi khía cạnh / trường nghĩa / lĩnh vực khác nhau
> của từ

<br>

<a id="node-140"></a>

<p align="center"><kbd><img src="assets/e4e6078849bf2d2e04cee05a8bba2f12815e52a8.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là một cách đó là weighted sum tụi nó lại theo weight tính bởi
> frequency
>
> Và sparse coding đại khái nói là trong vector space thật sự ra hóa ra là
> Ta có thể phân tách từ vector spice chung chung (weighted sum) thành
> các component cho các nghĩa của nó. Kiểu như nếu nói 17 là sum của 3
> số thì trong không gian 1D ta không thể biết 17 là tổng của 3 số nào
> nhưng trong không gian cao chiều hơn thì hóa ra có thể làm cái việc
> phân tách này.
>
> Ví dụ tie có thể được phân tách ra thành các sub vector mà trong đó
> người ta thấy nó gần gủi với các vector của các từ trong các cột từ đó
> cho thấy các nghĩa khác nhau của từ tie

<br>

