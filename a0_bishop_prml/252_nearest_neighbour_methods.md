# 2.5.2 Nearest-neighbour methods

📊 **Progress:** `5` Notes | `10` Screenshots

---
<a id="node-314"></a>

<p align="center"><kbd><img src="assets/3eadd3d1f696e7314ed182927268ab26d0c87479.png" width="100%"></kbd></p>

> [!NOTE]
> Ta sẽ qua cách tiếp cận thứ hai sau kernel density estimation, đó là
> nearest neighbor.
>
> Đầu tiên gs nói rằng, cách làm của kernel densitiy nó có hạn chế là: h ở
> đâu cũng bằng nhau. Còn nhớ, h đại khái là phạm vi mà ta dùng để xác
> định tầm ảnh hưởng của một data point. Ví dụ như khi dùng hàm kernel
> là Parzen window, thì h là cạnh của một hyper-cube, để từ đó nếu khoảng
> cách của **x** đến data point **x**i nhỏ hơn h/2, thì pdf tại x sẽ "bị ảnh
> hưởng bởi **x**i" (hàm parzen window kernel sẽ = 1, khiến pdf của x sẽ
> tăng thêm một khoảng do ảnh hưởng của **x**i). Với kernel function khác,
> như Normal kernel thì cũng vậy.
>
> Thế thì vấn đề là, việc h như nhau ở mọi nơi khiến cho nó bị cứng nhắc.
> Vì khi xét trong **vùng có nhiều data sample, thì nên cho h nhỏ lại, và
> ngược lại trong vùng thưa data sample thì nên cho h lớn lên**. Vì nếu
> trong vùng nhiều data sample mà h lớn quá quá sẽ khiến dẫn đến
> over-smoothing effect, xóa xạch các cấu trúc có thể được nắm bắt từ
> data. Ngược lại, nơi data density thấp mà h nhỏ quá sẽ khiến noisy. Nói
> chung **chỉ cần hiểu là h như nhau ở mọi nơi thì không tối ưu.**

<br>

<a id="node-315"></a>

<p align="center"><kbd><img src="assets/4ce4ffbc74f4112a018279577742b9da892e4809.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6540cbb0a9a9098e5ac0d3c5ae488dc2f92346e8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/54b39599554d0a46b23da5706f42d2ebe527ce4f.png" width="100%"></kbd></p>

> [!NOTE]
> Để hiểu cần recall lại chút (công thức 2.246: f(**x**) ≈ K / NV)
>
> Nói chung là, công thức này cho ta một cách để estimate giá trị của hàm density
> (probability density, tức pdf) tại một điểm **x**. Với K, còn nhớ, là ∑i I_(**x**i ∈ R), là
> số data point (sample) rơi vào vùng R (lân cận **x**). V là volume của vùng R. Và N là
> kích thước sample.
>
> Thế thì dựa vào công thức này, bằng cách fixed V, và xác định K nhờ data, ta sẽ có
> cách tiếp cận non-parameteric đầu tiên của bài toán density estimation - kernel
> approach. Trong đó, ta sẽ dùng một hàm kernel để tính xem có bao nhiêu data point
> **x**i nằm trong phạm vi R của **x** (mà cũng là có x nằm trong phạm vi của bao
> nhiêu data point, và nhân với) và từ đó sẽ định ra giá trị cao hay thấp của density tại
> **x**.
>
> Qua cách thứ hai, ta sẽ fix K, và dựa vào data để tính V, thì cách làm là: tại **x** (nơi
> cần tính f(**x**)), ta sẽ mở rộng vùng R (là một sphare - khối cầu) quanh nó ra cho
> đến khi chứa đủ K data sample **x**i, hoặc cũng có thể nhìn theo cách khác, mở rộng
> R (chính là tăng, hay xác định V) sao cho **x** nằm trong vùng ảnh hưởng của K data
> sample **x**i.
>
> Dùng ví dụ trước để minh họa có thể thấy K sẽ ảnh hưởng đến độ mượt.
>
> K nhỏ sẽ khiến K-neighbor density không mượt (noisy) mà K lớn quá sẽ khiến nó quá
> mượt làm mất đi (không capture / nắm bắt được pattern) cấu trúc của hàm density
> thật (cụ thể là hai cái đỉnh (modal) của đường màu xanh lá cây)
>
> Ôn lại tí: Với kernel density, ta sẽ fixed V, và dựa vào K từ data để tính độ cao thấp
> của density. Với hàm Parzen window kernel, sự cao thấp của kernel density sẽ được
> quyết định bởi việc x nằm trong vùnh ảnh hưởng (hyper cubic) của bao nhiêu điểm
> data, và vì với Parzen window kernel là hàm binary, nên nó sẽ tạo ra hiệu ứng bậc
> thang, khiến hàm kernel density có dạng step function. Nên để làm trơn, ta có thể
> dùng Gaussian kernel, vẫn là việc x nằm trong vùng ảnh hưởng của nhiều data point
> hay không sẽ quyết định đến độ cao thấp của density, nhưng khác với Parzen
> window, nó có thêm tính chất là khi tới gần hay ra xa thì ảnh hưởng của một data
> point lên x sẽ lớn lên hay nhỏ lại. Nhưng dù vậy, cả hai đều có chung nguyên lý, nếu
> x nằm trong vùng ảnh hưởng của nhiều data point, thì density sẽ cao và ngược lại.
> Và ta sẽ cần hiểu, hàm Parzel window kernel hay Gaussian kernel đều chỉ quy định
> mức cao thấp tương đối của density, còn để có một density hợp lệ (valid) ta cần V
> đóng vai normalizing constant
>
> Vậy thì ở đây, gs nói, với K-nearest neighbor, khi ta fixed K và tính V, để từ đó tỉ số
> K/NV cao thấp tương đối so với nhau, thì vấn đề là, nó không có cái nào đóng vai
> normalizing constant cả, do đó KNN density không phải là một valid pdf.

<br>

<a id="node-316"></a>

<p align="center"><kbd><img src="assets/6ffdeb443e42cc104296027b9b0fb4c9f1b0686b.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp theo, phần này gs Bishop sẽ nói về việc dùng KNN technique này để giải bài toán
> classification:
>
> Giả sử ta có N data sample **X**1,...**X**N. Và **x** là điểm cần classify. Cũng theo
> KNN technique: fixed K, dựa vào data tính V → ta dựng một quả cầu tâm **x**, chứa đủ
> K điểm data.
>
> Chỗ này lại một điểm như ông Bishop dùng kí hiệu khiến ta rất dễ lú: ông gọi Nk là số
> data point trong sample thuộc class Ck, làm ta dễ hiểu lầm là có K class. Sự thật là
> không phải vậy, nên mình gọi các class trong bài toán là C1,C2,....CM, tức là ta có C là
> một discrete random variable có M possible values C1,...CM.
>
> Và với điểm **x** và quả cầu của nó, chứa K điểm data, thì ta gọi Kk là số điểm dữ liệu
> thuộc class Tk. Ta có Σk Kk = K.
>
> Với mỗi class Ck, ta sẽ xây dựng một K nearest neighbor (estimate) density function:
> f(**x**|Ck)
>
> Y như công thức f(**x**) = K/NV với K, dùng parzen window kernel, thì ta dùng hàm đếm
> xem có bao nhiêu điểm data **x**i nằm trong phạm vi của **x**
>
> Vậy thì ta sẽ lập luận về f(**x**|Ck) như sau
>
> Dù gs không nói, nhưng cần hiểu rằng, ta đang xét một random variable C (class), có
> các discrete possible value C1,...CK Và f(**x**|Ck) dĩ nhiên là f(**x**|C=Ck), tức, dựa
> trên event C=Ck thì pdf tại **x** là gì.
>
> Để khỏi bối rối cái này mình cần nhớ lại định nghĩa cũng như ý nghĩa của conditional
> probability: P(A|B) = P(A,B)/P(B).
>
> Event A có bản chất là tập hợp: các possible outcome trong original sample space thuộc
> event A: A = {s ∈ Ω: s ∈ A}. Nên xét xác suất của event A, thực chất là xác suất của một
> tập hợp các s này: P(A) = P({s ∈ Ω: s ∈ A}) = Σ_{s ∈ Ω: s ∈ A} P({s}). Và ta nhớ axiom 1
> của probability theory nói rằng P(Ω) = 1.
>
> Thế thì khi xét xác suất của event A conditioned on B, tức là lúc này B đã xảy ra, thì ta
> sẽ xét tập những possible outcome thuộc B và A: Tức là (A, B) = {s ∈ B: s ∈ A}. Và xác
> suất của nó là P(A,B) = P({s ∈ B: s ∈ A}).
>
> Vấn đề là, nếu chỉ tính P(A|B) = P(A ∩ B) thì sẽ không hợp lệ. Lí do vì theo axiom của lí
> thuyết xác suất: P({s ∈ Ω}) = 1, nên lúc nếu sample space bây giờ chỉ còn là B, thì P(B)
> = P({s ∈ B}) = Σ_{s ∈ B} P({s}) không bằng 1.
>
> Thành ra, để hợp lệ, P({s}) phải được scale bởi constant c để trở thành P'({s}) thỏa Σ{s
> ∈ B} P'({s}) = 1
>
> ⇔ Σ_{s ∈ B} P({s}) c = 1
>
> ⇔ c Σ_{s ∈ B} P({s}) = 1
>
> ⇔ c P(B) = 1
>
> ⇔ c = 1/P(B)
>
> Như vậy, P(A|B) = P({s ∈ B: s ∈ A}) = Σ_{s ∈ B: s ∈ A} P'({s})
>
> = Σ_{s ∈ B: s ∈ A} [P({s})/P(B)]
>
> = [1/P(B)] Σ_{s ∈ B: s ∈ A} P({s}
>
> = [1/P(B)] P(A|B)
>
> = P(A|B)/P(B)
>
> Thế thì cũng như lập luận trên khi ta đã hiểu P(A|B) mang ý nghĩa là **khi B đã xảy ra
> thì sample space thu lại chỉ còn các possible outcome của B**, thì ở đây f(**x**|C=Ck)
> cũng có ý nghĩa tương tự, do đó nếu f(**x**) là K/NV thì f(**x**|Ck) = Kk/(Nk×V) với ý
> nghĩa là ta **áp dụng công thức** K/NV **cho những data point thuộc class k thôi, bỏ hết
> các data point khác**. Nên Kk = **chỉ xét những điểm data thuộc class k, và sau đó
> trong số chúng, bao nhiêu điểm nằm trong phạm vi của** **x**. Và Nk là **số data point
> thuộc class k**
>
> (Ôn nhanh về K trong lập luận gốc, khi ta derive ra công thức f(**x**) ≈ K/VN, thì K = Σi
> {I_(**X**i ∈ R}, với I_(**X**i ∈ **R**), hay I_(**X**i ∈ R(**x**) là indicator function, gắn với
> event **X**i ∈ R(**x**), mang giá trị bằng 1 khi **X**i nằm trong region lân cận **x** và
> bằng 0 khi ngược lại. Để rồi, với việc fixed V, dùng data để tính K, ta có kernel density
> approach, trong đó ta có thể dùng hàm Parzen window k(u) = I_|u ≤ 1/2| để đếm K =
> Σi=1:N k((**x**i-**x**)/h), hoặc Gaussian kernel để K = Σi=1:N [(1/√2πh^2)
> exp{-(**x**-**x**i)^2/2h^2}]. Hoặc với việc fixed K, tính V từ data ta sẽ có KNN density
> approach)
>
> Vậy thì, tiếp theo với f(**x**) = K/VN, ta sẽ dùng Bayes theorem:
>
> f(Ck|**x**) = f(**x**|Ck)f(Ck)/f(**x**)
>
> f(Ck), tạm gọi là prior distribution của random variable C, evaluate tại Ck (là một
> discrete variable), sẽ tính bằng Nk/N tức số observed data thuộc class k / tổng số
> observed data.
>
> ⇨ f(Ck|**x**) = f(**x**|Ck)f(Ck)/f(**x**) = (Kk/VNk) (Nk/N) / (K/VN)
>
> = Kk / K → 2.256

<br>

<a id="node-317"></a>

<p align="center"><kbd><img src="assets/2d9ad5470ac083d77329cc946f06e8c8a613d8ca.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/225ec74579fc224f1f6c1bf2faac699a010ce71e.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì gs nói, với giá trị posterior f(Ck|**x**) như vừa rồi (mình hiểu nó là hàm
> conditional pmf P(C=Ck|**X**=**x**) được estimate dựa trên KNN density
> approach) thì để có được một decision rule giảm thiểu mis-classificate rate, thì
> cái rule đó sẽ là: assign class k có f(Ck|**x**) lớn nhất, tức Kk/K
>
> Dù nghe có vẻ hiển nhiên, như vì sao? → Cái này trong chap 1 đã học rồi
> (Xem link) và thực chất, hiểu sâu hơn kết nối với kiến thức Casella đây chính
> là decision rule giúp giảm thiểu Bayes risk:
>
> **CHỌN RA CÁI NÀO NHỎ NHẤT TRONG ĐÁM**: {Σk=1:K Lk1 f(x, Ck),
> Σk=1:K Lk2 f(x, Ck), ..Σk=1:K LkK f(x, Ck)} sau đó **LẤY INDEX** ĐỂ GÁN
> CLASS cho data point **x**.
>
> Và trong bài toán này, ta cho loss là như nhau (hệ số misclassification error là
> như nhau, tức coi như L = 1 hết), và f(**x**, Ck) = f(Ck|**x**)f(**x**), nên so
> f(Ck|**x**) cũng là so sánh f(Ck, **x**).
>
> Như vậy phân tích thì dài dòng chứ cuối cùng cái rule rất đơn giản: Xem trong
> K điểm data gần nhất với **x**, thì class k nào chiếm đa số thì dùng class đó
> để assign cho **x**
>
> Và khi K = 1, ta gọi nó là nearest neighbor: xem thằng gần nhất thuộc class gì
> thì kết luận class đó.

<br>

<a id="node-318"></a>

<p align="center"><kbd><img src="assets/01a08cd7b186c0b3828faf6b43bf5fc4d96f0459.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/9ea96e663e3447fd6a9a024860f7603dcb951165.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/24c62d2a8899ece3a6ccd390d69760fac11b34a0.png" width="100%"></kbd></p>

> [!NOTE]
> Một ví dụ minh họa K thay đổi làm thay đổi độ mượt của decision boudary.
>
> Cuối cùng, đại ý gs nói là, cái này, tức KNN density estimator cũng như kernel
> density estimator đều không cần phải training gì hết, nhưng ta phải lưu trữ
> toàn bộ data, khiến sẽ là một hạn chế rất đáng kể khi data lớn.
>
> Và ông nói, tuy rằng bằng các thuật toán tree-based search ta có thể giúp tìm
> kiếm nearest neighbor nhanh, nhưng bản chất, nó vẫn rất hạn chế.
>
> Bên cạnh đó, chưa kể, ta đã thấy nó có nhiều vấn đề trong việc estimate
> distribution. Thành ra trong các chapter sau, ta sẽ bàn đến các cách tiếp cận
> khác, flexible hơn, với độ phức tạp có thể được kiểm soát một cách độc lập
> với kích thước training set.

<br>

