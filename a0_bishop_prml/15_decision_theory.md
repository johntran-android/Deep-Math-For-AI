# 1.5 Decision Theory

📊 **Progress:** `28` Notes | `36` Screenshots

---
<a id="node-111"></a>

<p align="center"><kbd><img src="assets/42263ad5f84bedf3ca4859eb9fcf20b7d4536659.png" width="100%"></kbd></p>

> [!NOTE]
> Mở đầu gs cho biết ta đã thấy trong những phần trước lí thuyết xác suất đã
> cung cấp cho ta một framework để định lượng và thao tác với tính
> uncertainty. Thì nay, kết hợp với decision theory, sẽ cho ta một công cụ để
> giúp đưa ra  những quyết định hợp lí trong bối cảnh uncertainty

<br>

<a id="node-112"></a>

<p align="center"><kbd><img src="assets/e17d3122dfe78cfac7371dc57e42341aea4231fd.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là, giả sử ta có input vector **x**, tương ứng là vector **t**, và mục
> đích là dự đoán t từ new value x. Thì với bài toán regression, t sẽ là biến
> liên tục. còn classification, t sẽ là class label.
>
> Khi đó joint probability của **X**,**T** (ở đây mình cứ theo quy tắc Casella,
> biến thì viết hoa, cũng như xài chữ f cho quen thuộc) f(**x**,**t**) sẽ phản
> ánh toàn diện mọi tính uncertainty gắn với các random variables này. Và
> bài toán đi xác định phân phối xác suất của **X**,**T** được gọi là **INFERENCE**.
>
> Có thể hiểu ý này, vì xuyên suốt cuốn Statistical Inference của Casella,
> mình chính là deal với bài toán này: cho random sample X = (X1,...Xn) ~
> f(**x**|θ) thì mục tiêu của ta là suy đoán giá trị của θ, tham số chi phối phân
> phối xác suất của **X**, và 3 bài toán lớn là
>
> i) point estimation - tìm cách đưa ra một function của sample W(**X**) sao
> cho với giá trị quan sát **X** = **x** thì ta có một estimate W(**x**) cho θ.
>
> ii) hypothesis testing - tìm cách đưa ra một nhận định rằng θ ∈ Θ0 hoặc θ ∈
> Θ0c, và cụ thể là đi xây dựng một rejection region R = {**x**: reject H0}
> cũng  chính là một hypothesis test, có bản chất là một decision rule: nhận
> vào **x**, tính toán giá trị của test statistic và dùng nó để quyết định xem
> nên tuyên bố θ ∈ Θ0 hay Θ0c.
>
> iii) interval estimator - tìm cách xây dựng một random interval hay khái quát
> hơn là random set C(**X**) để khi quan sát **X** = **x** ta sẽ đưa ra một
> nhận định là θ ∈ C(**X**)
>
> Quay lại đây, gs Bishop cho rằng đây vốn là bài toán rất khó, và sẽ là chủ
> đề xuyên suốt của cuốn sách này. Tuy nhiên, trong những bài toán thực tế,
> ta thường muốn dự đoán t dựa trên giá trị của x hoặc rộng hơn, mục đích
> của ta thường là đưa ra một hành động tốt nhất dựa trên giá trị mà t có khả
> năng cao nhất dựa trên input x

<br>

<a id="node-113"></a>

<p align="center"><kbd><img src="assets/1806c579b842c21c38f3f56e57a4da202ae4495d.png" width="100%"></kbd></p>

> [!NOTE]
> Lấy ví dụ bài toán y khoa, ta muốn dựa trên input x là vector các giá trị điểm
> ảnh của ảnh chụp x quang, để dự đoán t mang một trong hai giá trị 0 hoặc 1
> để đại diện là C1 và C2 là tên hai class: có bị ung thư hay không bị. Thì ở
> đây nếu ta tìm được phân phối xác suất f(**x**, t) hay f(**x**, Ck)
>
> (chỗ này mình nghĩ ông gs Bishop làm cho rách việc ra thêm bằng cách
> dùng kí hiệu Ck, mình cho là cứ dùng t cũng được, chỉ cần biết nó là
> discrete mang hai  possible value 0 hoặc 1 thôi. Vốn dĩ việc ổng thoát li khỏi
> quy ước kí hiệu bên toán như xài chữ p thay cho f, viết thường cho tên biến
> thay vì viết hoa vốn đã gây dễ lú rồi. Nên ở đây mình sẽ cứ dùng t, f, và tuân
> theo quy ước viết hoa cho tên biến)
>
> thì đó chính là bài toán inference, tuy nhiên sau hết, mục đích vẫn là đưa ra
> quyết định là làm gì tiếp theo, thì đây chính là địa hạt của decision theory, nó
> sẽ giúp ta đưa ra quyết định tối ưu dựa trên xác suất tính toán được.
>
> Và gs cho biết thường thì bước make decision sẽ tương đối đơn giản một
> khi ta đã giải được bài toán inference.

<br>

<a id="node-114"></a>

<p align="center"><kbd><img src="assets/27282d92b172c007966374349361c82a4db14bbe.png" width="100%"></kbd></p>

> [!NOTE]
> Trước đi đi vào phân tích chi tiết, ta sẽ xem xét một cách không chính thức
> làm cách nào để ta thấy rằng xác suất sẽ đóng vai trò giúp ta quyết định
> thông qua ví dụ dễ hiểu.
>
> Như nãy đã nói, trong bối cảnh bài toán ta muốn dựa trên tấm ảnh chụp 
> x quang để đưa ra dự đoán bệnh hay không bệnh. Thì ta sẽ muốn xem
> xét f(t|**x**) 
>
> Theo Bayes theorem: f(t|**x**) = f(**x**|t) f(t) / f(**x**)
>
> Y như trong Bayesian approach ta coi θ là random variable để gán cho nó
> prior distribution π(θ), và dựa vào Bayes theorem để cập nhật xác suất
> của θ dựa trên **X** = **x**, để có posterior distribution π(θ|**x**). Thì ở đây, f(t)
> (trong sách là p(Ck) cũng sẽ là prior distribution của T, và f(t|**x**) là posterior
> distribution, với ý nghĩa là:
>
> Khi chưa biết kết quả x-ray thì xác suất một người mắc bệnh (T mang giá
> trị gì) sẽ được quy định bởi prior distribution f(t).
>
> Nhưng sau khi có x-ray thì xác suất của T sẽ do f(t|**x**) quyết định.
>
> Như vậy, để giảm thiểu khả năng phán bệnh sai, lẽ thường ta sẽ dùng
> kết quả của posterior distribution, là trong hai giá trị khả dĩ của T, thì cái
> nào có posterior probability cao hơn.
>
> Vậy thì ở đây, tính được f(t, **x**) coi như là bài toán inference, khi đó, ta
> sẽ tính được f(t|**x**) và việc lấy giá trị nào có posterior cao hơn để gán / báo 
> cho bệnh nhân chính là bước dựa vào decision theory để take action

<br>

<a id="node-115"></a>

<p align="center"><kbd><img src="assets/44a744c064d80aaa0be07268a91e3428cac5cb32.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì đại ý là nếu như mục tiêu của ta là giảm thiểu tỉ lệ phân loại nhầm
> (misclassification rate) thì ta sẽ cần một bộ quy tắc để gán giá trị cho của **x** cho
> một trong các class đang xét.
>
> Trước khi nói tiếp, mình tranh thủ recall lại kiến thức trong Casella: Hypo thesis
> testing:
>
> Như lúc nãy cũng đã review lại sơ sơ: Bài toán hypothesis testing là bài toán suy
> luận thống kê mà trong đó ta muốn xây dựng một cái hypothesis test - có bản
> chất chỉ là một decision rule: dựa vào gía trị quan sát của **X**, tính toán ra test
> stastisic λ(**X**) và theo một cái rule nào đó để đưa ra kết luận rằng H0: θ ∈ Θ0,
> gọi là accept null hypothesis, hay kết luận H1: θ ∈ Θ0c gọi là reject null
> hypothesis.
>
> Thế thì, như vậy việc định ra một cái test, cũng chính là định ra cái rule, để rồi áp
> dụng cái rule này với mọi **x** ∈ range **X**, nó sẽ chia range **X** thành hai
> phần, Rejection region R = {**x** ∈ range **X**: reject H0} và Rc = {**x** ∈ range
> **X**: accept H0}, gọi là Acceptance region.
>
> Để rồi, khi đó, khi bàn tới việc đánh giá một hypothesis test, ta sẽ muốn giảm
> thiểu hai loại sai sót: Type I error, là khi θ ∈ Θ0 nhưng lại reject H0 (**X** ∈ R), và
> Type II error, là khi θ ∈ Θ0c nhưng lại accept H0 (**X** ∈ Rc).
>
> Để rồi từ đó ta có các khái niệm như power function: β(θ) = P_θ(**X** ∈ R), với
> định nghĩa này, ta sẽ muốn một cái test có Type I error thấp thì có nghĩa là với θ ∈
> Θ0 β(θ) nên thấp, từ đó ta có định nghĩa level α test là test mà:
>
> sup_θ∈Θ0 P_θ(**X** ∈ R) ≤ α.
>
> Và định nghĩa size α test, là test có sup_θ∈Θ0 P_θ(**X** ∈ R) = α.
>
> Và khi đã xét một đám có xác suất Type I error thấp, ví dụ leve α test.
>
> Ta sẽ muốn tìm thằng có xác suất mắc Type II error thấp nhất trong đó, cũng là
> thằng mà khi θ ∈ Θ0c thì xác suất reject H0 là cao nhất mọi thằng khác, đó chính
> là most power level α test, với power function chính là định nghĩa bởi β(θ) =
> P_θ(**X** ∈ R): một test gọi là most power trong các test level α là khi với mọi θ ∈
> Θ0c, thì β(θ) của nó luôn ≥ β'(θ) của mọi test khác trong đám đó.
>
> Review chút xíu cho nhớ, giờ quay lại bài toán này.
>
> \------
>
> Để thực hiện bước phân loại, ta cũng sẽ muốn một cái decision rule, cũng  giống
> như hypothesis test, ta cũng sẽ cần một cái function, để nhận vào x, và trả ra kết
> quả là predict là class nào. Khi đó nó cũng sẽ chia range X thành các vùng, gọi là
> DECISION REGIONS
>
> (không nhất thiết phải là 2 vùng rejection region R và decision region R, mà tùy
> vào số possible class / cũng là số possible values của T, nhưng ở đây thì đúng là
> có 2 vùng, vì T có 2 possible values, gọi là R1, và R2)
>
> Và biên giới phân tách các decision regions gọi là DECISION BOUNDARY.
>
> Thế thì khi nói về event "mắc sai lầm / phân loại sai", nếu trong bối cảnh bài toán
> Hypothesis testing, thì nó sẽ là:
>
> (θ ∈ Θ0, reject H0) hoặc (θ ∈ Θ0c, accept H0)
>
> cũng là (θ ∈ Θ0, **X** ∈ R) hoặc (θ ∈ Θ0c, **X** ∈ Rc)
>
> Tương tự, ở đây, một event "phân loại sai" sẽ là:
>
> (T = C1, phân loại C2) hoặc (t = C2, phân loại C1)
>
> cũng là (T = C1, **X** ∈ R2) hoặc T = C2, **X** ∈ R1)
>
> Thế thì xét xác suất của event "mắc sai lầm" này, ta sẽ thấy.
>
> Với bài toán hypothesis testing, phải chú ý rằng, vì theo Frequentist approach, ta
> không coi θ như random variable, cho nên xác suất mắc Type 1 Error không phải
> là P_θ(θ ∈ Θ0, **X** ∈ R) mà phải define là P_θ(**X** ∈ R) khi θ ∈ Θ0, mang ý
> nghĩa: Khi giá trị của θ, vốn là fixed và unknown, thật sự là ∈ Θ0 thì P_θ(**X** ∈ R)
> chính là xác suất mắc Type I error. (vì sao có chữ θ ở dưới P: P_θ(...) thì là vì
> **X** ~ f(**x**|θ) nên dĩ nhiên xác suất này phụ thuộc θ)
>
> Tương tự, xác suất mắc Type II error sẽ được định nghĩa là:
>
> P_θ(**X** ∈ Rc) khi θ ∈ Θ0c.
>
> Nhưng với bài toán này, vì **X** và T đều là random variable / random vectors,
>
> (Chú ý, **X** là random vectors, nên trong sách gs Bishop dùng bold font, nhưng
> như đã nói ông ko theo convention nữa, nên viết chữ thường (vẫn in đậm, nhưng
> chữ thường **x**) còn mình thì theo convention của Casella, nên in đậm, chữ hoa
> **X**)
>
> nên xác suất của event mắc sai lầm sẽ là:
>
> P[(T = C1, **X** ∈ R2) or (T = C2, **X** ∈ R1)]
>
> = P[(T = C1, **X** ∈ R2) U (T = C2, **X** ∈ R1)]
>
> Đây là union của hai disjoint event, nên theo axiom 2 của lí thuyết xác suất, ta
> tách nó thành tổng của:
>
> = P(T = C1, **X** ∈ R2) + P(T = C2, **X** ∈ R1)
>
> Và đây là xác suất của joint event liên quan đến T, và **X**, nên ta sẽ dùng thể
> hiện nó / tính toán nó bởi joint distribution của T và **X**:
>
> f(t,**x**) | t=C1, **x**∈R2 + f(t,**x**) | t=C2, **x**∈R1
>
> Để thấy bước tiếp theo quen thuộc ta nhớ trong Casella hay Stat110, khi xét joint
> distribution của X,Y f(x,y), và xét xác suát của event X ∈ A, Y ∈ B, ta sẽ lấy tích
> phân ∫A∫B f(x,y)dxdy.
>
> Ở đây nó hơi lạ là đây là joint distribution của một biến discrete và một biến liên
> tục nhưng nguyên lí cũng  vậy thôi, có thể coi cái ta cần tính ở đây là xác suất của
> event T ∈ {C1}, **X** ∈ R2 **⇨** ∫{C1}∫R2 f(t, **x**)d**x** dt = ∫R2 f(C1, **x**)d**x**
>
> nên ta có:
>
> ∫R2 f(C1,**x**)d**x** + ∫R1 f(C2,**x**)d**x**

<br>

<a id="node-116"></a>

<p align="center"><kbd><img src="assets/51d1bb21d9e200f13d92f4183ff21f9b8f692526.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/5ce8cf390b2d4eb7ed721733558bf7efe42cd2c2.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp, cùng tìm hiểu sao ông Bishop nói dễ thấy là cái rule mà sẽ giúp ta giảm thiểu
> xác suất mistake này sẽ là cái rule sau đây: gán cho **x** cái class nào mà f(**x**,
> Ck) nhỏ hơn. Ví dụ nếu f(**x**, C1) < f(**x**, C2) thì kết luận C2, ngược lại thì kết luận C1.
>
> Mình sẽ nhìn bài toán này theo góc nhìn bài toán tối ưu hóa:
>
> nói bằng lời là:
>
> tìm cái decision rule sao cho dưới cái rule đó, xác suất sai lầm là nhỏ nhất.
>
> Vấn đề là,  với bài toán tối ưu, thì phải xác định biến tối ưu (optimization variable)  là
> gì. Thế thì ở đây, cái cần tìm là một decision rule, ko phải tìm x, y gì cả.
>
> Vậy thì cái biến tối ưu ở đây, là decision rule. Mà decision rule thì làm sao mà thể
> hiện theo toán học đây.
>
> À, như đã biết trong bài toán Hypothesis testing, nói về một cái test, hay test rule,
> thì bản chất cũng chính là nói về cái rejection region hay acceptance region. Vì một
> cái rule, sẽ gắn với cái rejection region có được khi áp cái rule đó để mà chia range
> **X** thành R và Rc.
>
> Nên ở đây cũng vậy, bản chất một cái decision rule, chính là thể hiện qua  các
> decision region R1, R2. Vì tương tự như trên, mỗi một cái decision rule khác nhau
> sẽ tạo ra một bộ decision region khác nhau.
>
> Do đó bài toán tối ưu sẽ được thể hiện như sau:
>
> minimize_R1,R2 {∫R2 f(C1,**x**)d**x** + ∫R1 f(C2,**x**)d**x**}
>
> (chỗ này vì X là vector nên ta phải hiểu đây là tích phân đa biến ∫...∫ nếu ghi
> chặt chẽ theo toán học, chỉ là ghi ∫ cho gọn, cũng như range **X** đây là subset của R^n
> chứ ko phải R)
>
> Tuy nhiên, R1,R2 sẽ có ràng buộc: R1 U R2 = range **X**, và R1, R2 disjoint:  R1 ∩
> R2 = ∅
>
> Nhưng tích phân trên miền R2, có thể được tách thành tích phân trên toàn miền trừ
> tích phân trên miền R1: ∫R2 f(C1,**x**)d**x** = ∫{Range **X**} f(C1,**x**)d**x** - ∫R1
> f(C1,**x**)d**x**
>
> Và xét cái này ∫{Range **X**} f(C1,**x**)d**x**, Ta biết là marginalizing joint pdf/pmf
> của **X**, T trên toàn miền xác định của **X** ta sẽ được marginal pdf/pmf của T.
>
> Do đó ∫{Range **X**} f(C1,**x**)d**x** chính là f(t)|t=C1, tức prior distribution của T,
> evaluate tại t = C1
>
> Vậy bài toán tối ưu lúc này là:
>
> minimize_R1 {f(C1) - ∫R1 f(C1,**x**)d**x** + ∫R1 f(C2,**x**)d**x**} = {f(C1) + ∫R1 [f(C2,
> **x**) - f(C1,**x**)]d**x** }
>
> Và f(C1) thì ko phụ thuộc R1, nên ta chuyển thành bài toán tương đương:
>
> minimize_R1 { ∫R1 [f(C2,**x**) - f(C1,**x**)]d**x** }
>
> Đến đây, nói bằng lời, ta muốn tìm R1, sao cho minimize cái tích phân này
>
> Nếu là bối cảnh bài toán tối ưu với biến **x** thông thường, có lẽ tới đây mình sẽ dùng
> first order necessary condition để tìm **x** khiến gradient = 0, để ra critical point rồi xét
> phép thử bậc hai các kiểu.
>
> Còn ở đây, biến tối ưu lại là một cái region, vậy phải làm sao?
>
> Ta sẽ dựa vào lập luận: mục đích là tìm vùng R1 sao cho minimize tích phân này.
> Mà bản chất tích phân này là tổng: tổng các giá trị [f(C2,**x**) - f(C1,**x**)] trên miền
> R1 ∈ range **X**
>
> Nên có thể diễn dịch yêu cầu là tìm trong miền **X**, để nhặt ra, gom lại những
> giá trị **x** nào đó sao cho tổng [f(C2,**x**) - f(C1,**x**)] trên tập đó là nhỏ nhất.
>
> Để làm được điều này, về trực giác, ta sẽ chọn các **x** khiến cái cụm này âm, thì
> khi đó, tổng của một đám mang giá trị âm mới khiến đẩy giá trị ngày càng nhỏ
> lại.
>
> Và ta cũng chỉ có thể lập luận như vậy, để kết luận R1 tối ưu nên là tập các **x** ∈ range **X**
> sao cho [f(C2,**x**) - f(C1,**x**)] < 0 ⇔ f(C2,**x**) < f(C1,**x**).
>
> Nhờ vậy giúp ta hiểu vì sao gs Bishop nói vậy trong đoạn này. (ông nói clearly
> nhưng mình thấy chả clearly chút nào nếu ko phân tích như trên).
>
> Vậy optimal decision rule (theo tiêu chí minimize misclassification rate) là:
>
> Assign class C1 nếu f(C2,**x**) < f(C1,**x**) và ngược lại.
>
> Và cũng dễ hiểu rằng vì f(t,**x**) = f(t|**x**)f(**x**) **⇨** f(C2,**x**) = f(C2|**x**)f(**x**)
>
> và f(C1,**x**) = f(C1|**x**)f(**x**)
>
> nên decision rule tối ưu cũng là: Assign class C1 nếu f(C2|**x**) (tức posterior pdf
> tại C2) < f(C1|**x**)

<br>

<a id="node-117"></a>

<p align="center"><kbd><img src="assets/bc07aaa6f292a17dc0fcd19bb4f103c2b407b240.png" width="100%"></kbd></p>

> [!NOTE]
> Minh họa bằng hình ảnh này. Vẽ đồ thị của hàm f(C1, **x**) và f(C2, **x**) theo **x**.
>
> Mình phải nói trước: hình ảnh chỉ nên hiểu mang tính minh họa, vì **x** vốn
> đang là vector, ko thể thể hiện nó trên 1 trục như vậy được, hay nói cách
> khác, ở đây coi như **x** chỉ là vector 1-D, do nên ta thấy gs Bishop dùng
> kí hiệu x thường (ko phải x bold: **x** như trong phần trước)
>
> Xác suất của event "phân loại" sai, như vừa phân tích được tính bởi
>
> P(Mistake) = ∫R1 f(C2,x) dx + ∫R2 f(C1,x)dx
>
> Và dĩ nhiên như đã học trong MIT 1801, ý nghĩa của tích phần ∫a:b f(t)dt là
> diện tích của phần đồ thị bên dưới hàm f(t) từ a đến b.
>
> Nên (Mistake) là tổng diện tích của phần đồ thị hàm f(C2,x) với x ∈ R1 và
> diện tích của phần đồ thị hàm f(C1,x) với x trong R2. chính là phần xanh
> đỏ và xanh  lá
>
> Và bài toán đặt ra là tìm R1, R2 giúp minimize cái tổng diện tích này, và
> điều này đồng nghĩa nhích cái decision boundary tại x^ qua lại.
>
> Thế thì đại ý rất dễ thấy đó là, khi dịch chuyển cái x^, thì tổng diện tích
> vùng  xanh lá, xanh dương ko đổi. Nó chỉ thay đổi diện tích vùng đỏ. Và tại
> x^ = x0 thì diện tích vùng đỏ là nhỏ nhất (= 0), đó chính là nơi mà từ tại đó,
> ta có optimal decision rule:
>
> Assign C1 nếu f(C2|x) < f(C1|x) và ngược lại.
>
> Có nghĩa là cái optimal rule sẽ là: Assign C1 nếu x < x0 và ngược lại.

<br>

<a id="node-118"></a>

<p align="center"><kbd><img src="assets/8dc26ad22dd0a74e8edf737a8eab06468b506443.png" width="100%"></kbd></p>

> [!NOTE]
> Nói qua khái quát bài toán lên K classes thay vì 2 classes, ông cho rằng sẽ
> dễ hơn nếu ta đặt objective cho việc tìm rule tối ưu là maximize xác suất
> phân loại đúng thay vì minimize xác suất phân loại sai.
>
> Là sao? À đơn giản là vì đây là hai event disjoint và bù nhau, nên P("mistake"
> ) = 1 - P(" correct"). Mà với bài toán tối ưu thì ta biết rồi, minimize hàm f(x) thì
> cũng là maximize hàm -f(x). Đo đó, minimize P("mistake") tương đương
> maximize
> \- P("mistake"), và cũng tương đương maximize 1 - P("mistake") (cộng hằng
> số vào objective thì cũng được bài toán tương đương), và đây chính là
> maximize P("correct")
>
> Như vậy minimize P("mistake") cũng chính là maximize P("correct")
>
> Nhưng vì sao maximize P("correct") lại dễ hơn.
>
> Là vì, event "correct" dễ định nghĩa hơn event "mistake" trong trường hợp có
> nhiều classes.
>
> Ví dụ có K classes, dĩ nhiên event correct sẽ là:
>
> ([T = C1, decision rule phán là C1] hoặc [T = C2, decision rule phán là C2] ..
>
> hoặc [T = CK, decision rule phán là CK])
>
> viết theo toán học gọn hơn thì sẽ là:
>
> "Correct" = (T = C1, **X** ∈ R1) hoặc (T = C2, **X** ∈ R2) ,...(T = CK, **X** ∈
> Rk)
>
> ⇨ P("Correct") = P[(T = C1, **X** ∈ R1) U (T = C2, **X** ∈ R2) U...U( T = CK,
> **X** ∈ Rk)]
>
> tương tự, đây là union của các disjoint events nên theo axiom 2 (hay 3 nếu
> theo sách Casella)
>
> .. = P[(T = C1, **X** ∈ R1) + P(T = C2, **X** ∈ R2) +...+ P(T = CK, **X** ∈ Rk)]
>
> và tương tự như hồi nãy, nó chính là ∫R1 f(C1,**x**)d**x** + ...∫RK f(CK,
> **x**)d**x**
>
> = Σk=1:K ∫Rk f(Ck,**x**)d**x** Và tương tự như khi K = 2, cái decision rule khiến maximize P("correct") có
> thể đoán được cũng sẽ chính là cái rule này: Assign class Ck nếu joint  pdf
> f(Ck, **x**) và cũng là posterior pdf f(Ck|**x**) là cao nhất trong các k = 1,..K
>
> =====
>
> Vậy ở đây giúp ta hiểu sâu hơn như sau: Nếu tiêu chí của ta, mục tiêu của
> ta là giảm thiểu tỉ lệ sai xót tổng thể, thì cách phân loại tốt nhất chính là
> dựa trên posterior probability

<br>

<a id="node-119"></a>

<p align="center"><kbd><img src="assets/2f5a777bb2a9fd00996eeddac1880f5a69c9cb37.png" width="100%"></kbd></p>

> [!NOTE]
> Qua đây, đại ý là, trong nhiều trường hợp, mục tiêu không đơn giản chỉ là
> giảm tỉ lệ sai sót nói chung.
>
> Quay lại ví dụ việc xác định bệnh nhân có bệnh hay không, đôi khi hai
> loại lỗi nó có mức độ hậu qủa khác nhau. Ví dụ như không có ung thư mà
> phán là có, thì có thể cùng lắm là khiến bệnh nhân lo lắng và xét nghiệm
> thêm các kiểu tốn tìền. Nhưng nếu có ung thư mà chẩn đoán là không thì
> người ta có thể sẽ chết vì không được chữa trị.
>
> Lúc này, mục tiêu của ta có thể là ưu tiên loại error thứ hai, chấp nhận
> error thứ nhất (ý là nếu so sánh performance của các quy trình chẩn đoán
> thì có thể ưu tiện chọn cái có tỉ lệ error thứ hai nhỏ nhất, dù error thứ nhất
> nó ko phải là nhỏ nhất)
>
> Lại liên hệ nó với hypothesis testing cho vui. Mình đã review lại một ít
> trong các note trước, rằng trong bài toán này, ta cũng sẽ có hai loại error:
> Type I error, là khi θ thật sự thuộc Θ0, nhưng lại kết luận là reject H0, hay
> **X** ∈ R và Type II error là khi θ ∈ Θ0c mà lại kết luận là accept H0: **X**
> ∈ Rc.
>
> Thì còn nhớ, trong sách Casella, ta đã nghe là, trong thực tế, người ta sẽ
> dành Type I error để chỉ lại sai lầm mà ta muốn  tránh bằng mọi giá, ưu
> tiên tránh, vì mang lại hậu quả lớn. Ví dụ như trong nghiên cứu thuốc
> mới, nếu thuốc gây tác dụng phụ nguy hiểm mà kết quả test lại kết luận
> thuốc không có tác dụng phụ gì, thì hậu quả sẽ rất lớn. Do đó, ta sẽ đặt
> H0: θ ∈ Θ0 ứng với: Thuốc có tác dụng phụ. Để rồi Type I error sẽ là:
> thuốc có tác dụng phụ mà lại công bố là không.
>
> Khi đó, bằng cách định nghĩa như vầy, ta sẽ tập trung xây dựng level α
> test, ví dụ level 0.001 test, theo định nghĩa, là các test có xác suất mắc lỗi
> loại I cao nhất cũng không bao giờ vượt quá 0.001.
>
> Sau đó, ta mới đi tìm trong các level 0.001 test, cái nào có xác suất mắc
> Type II error thấp nhất.
>
> Đây là một cách tiếp cận của việc đánh giá (evaluating) hypothesis test

> [!NOTE]
> Thế thì vừa rồi mình đã ôn lại cách tiếp cận vấn đề đánh giá một hypothesis testing trong
> Casella, dĩ nhiên còn vài vấn đề khác, ví dụ như khi không tồn tại Uniformly Most Powerful
> test, rồi p-values.
>
> Recall thêm chút nữa:
>
> Trong thống kê cổ điển như cuốn Casella, mình nhớ là với Point estimator, Hypothesis
> testing, Interval estimator đều nói đến cách tiếp cận của decision theory để đánh giá (7.3.
> 4, 8.3.5, 9.3.4)
>
> Ôn lại vài khái niệm liên quan đến decision theory đã học trong phần Point estimation và
> Interval estimation Casella: Đầu tiên, đối với point estimator thì khi dẫn dắt ta về cái này,
> gs Casella nói rằng, trong decision theory, action space là không gian những action, mà áp
> vào bối cảnh point estimation thì action đó là "(đưa ra) một estimation của θ", để rồi action
> space, là tập hợp mọi estimation của θ. Thế thì, theo decision theory, một action sẽ tạo ra
> một loss, và hàm loss sẽ là hàm được định nghĩa để phản ánh mức độ nghiêm trọng của
> action. Với bài toán estimation, thì loss có thể dùng **squared error loss** L(θ, δ(**x**)) =
> (δ(**x**)-θ)^2 hoặc **absolute error loss** L(θ,δ(**x**)) = |δ(**x**) - θ|
>
> Và như vậy thì, với loss function, ta sẽ có một hàm số phụ thuộc θ phản ánh chất lượng
> của estimator δ(**X**) ứng với θ cụ thể nào đó.
>
> Và để có một con số duy nhất, không phụ thuộc **X**, phản ánh chất lượng của estimator
> δ(**X**) nói chung, ta sẽ định nghĩa cái gọi là risk function:
>
> R(δ(**X**), θ) = E_θ[L(δ(**X**), θ)], với phân tích ý nghĩa như sau:
>
> L(δ(**X**), θ) sẽ là một random variable, vì nó là kết quả do áp một function lên δ(**X**)
> nên phụ thuộc δ(**X**), nên phụ thuộc **X**.
>
> Lấy kì vọng cái random variable này, thì tính cái này, thì ta sẽ dùng distribution của
> L(δ(**X**),θ), mang ý nghĩa là marginalizing mọi giá trị khả dĩ của L, nên kết quả sẽ là fix,
> không còn là random variable nữa, không phụ thuộc **X** nữa. nhưng nó vẫn là hàm theo
> θ.
>
> Và bằng cách tìm cái δ(**X**) có risk nhỏ nhất với mọi θ thì ta sẽ có cái estimator tốt nhất,
> tức là minimum risk estimator.
>
> Và có thể thấy, nếu loss là squared error loss thì:
>
> R(δ(**X**), θ) = E_θ[(δ(**X**) - θ)^2] thì đây chính là định nghĩa của hàm MSE:
>
> MSE củan estimator W(**X**), define bởi: MSE(W(**X**),θ) = E_θ[(W(**X**) - θ)^2].
>
> Từ đó, ta mới liên hệ với việc tìm estimator **minimize MSE cũng chính là tìm estimator
> minimize square error loss risk function**.
>
> Và triển khai thêm tí nữa:
>
> Dùng VarX = EX^2 - (EX)^2 ⇨ Var[W(**X**) - θ] = E[(W(**X**) - θ)^2] - E[W(**X**) - θ])^2
>
> Do đó MSE(W(**X**), θ) = R(W(**X**), θ)_squared error loss = E_θ[(W(**X**) - θ)^2]
>
> = Var[Var(**X**) - θ] + (E[W(**X**) - θ])^2
>
> = Var[Var(**X**)] + (E[W(X) - θ])^2
>
> Và E[W(**X**) - θ] lại chính là definition của Bias(W(X), θ)
>
> ⇨ MSE(W(**X**), θ) = Var[W(**X**)] + [Bias(W(**X**), θ)]^2
>
> \-----
>
> Sang tới interval estimator, thì lúc này loss function cần phản ánh hai thứ: độ chính xác
> (C(**X**) chứa θ và kích thước C(**X**). Do đó, loss sẽ là kết hợp  của một indicator
> function I_{C(**X**) chứa θ} (= 0 khi C(**X**) chứa và bằng 1 khi  C(X) không chứa θ) và
> Size(C(**X**)) với một tham số b giúp điều chỉnh tương quan giữa hai sub-objective này:
>
> L(C(**X**), θ) = I_{θ ∈ C(**X**)} + b Size(C(**X**)), thể hiện: nếu C(**X**) chứa θ và có size
> nhỏ thì loss sẽ nhỏ.
>
> Và ta cũng sẽ đặt ra risk function của interval estimator là kì vọng của loss này. Để rồi tìm
> cách tìm estimator mà giảm thiểu risk:
>
> R(C(**X**), θ) = E_θ[L(C(**X**), θ)].
>
> \-----
>
> Còn với bài toán Hypothesis testing, trong 8.3.5 Casella ta được biết rằng, với bài toán
> này, action sẽ chỉ là một trong hai: a0, a1 biểu diễn kết luận của test rule là accept H0 hay
> reject H0. Và ta cũng sẽ define loss function, gọi là 1-0 loss để phản ảnh hậu quả:
>
> L(θ, a0) = 0 nếu θ ∈ Θ0, = 1 nếu θ ∈ Θ0c
>
> L(θ, a1) = 0 nếu θ ∈ Θ0c, = 1 nếu θ ∈ Θ0,
>
> Và risk cũng sẽ là function lấy trung bình loss:
>
> Chỗ này cần nói rõ cho dễ hiểu: Định nghĩa của loss, luôn gắn với một action. Với point
> estimator, loss kí hiệu là L(δ(**X**), θ), để rồi nó là một random variable, mà khi nhận giá trị
> **X** = **x**, kéo theo δ(**X**) mang giá trị estimate cho θ: δ(**x**) (là một action), kéo theo
> phát sinh loss L(δ(**x**), **θ**) từ action này. Và vì L(δ(**X**), θ) là random variable, nên
> risk = lấy kì vọng, chính là dựa trên distribution của cái thằng L này, và truy nguyên nguòn
> gốc thì c**ũng chỉ là xuất phát từ distribution của X**: f(**x**|θ), do đó risk mới là hàm phụ
> thuộc θ.
>
> Tương tự, với interval estimator, thì action là một interval C(**x**), loss L(C(**X**), θ) cũng
> là random variable, mà yếu tố random của nó đến từ C(**X**). Khi quan sát **X** = **x**,
> C(**X**) mang giá trị C(**x**), thì nó mang ý nghĩa là một action được đưa ra: một interval
> được dự đoán sẽ chứa θ, và với action đó, phát sinh loss: L(C(**x**), θ). Nên lấy kì vọng
> cái này để có risk, thì ta sẽ dựa trên **distribution của C(X)**, tất nhiên, C(**X**), nếu là
> random interval, thì cũng sẽ được cấu thành bởi hai random variable L(**X**), U(**X**), nên
> tương tự, cũng chỉ là xuất phát từ distribution của **X**
>
> Còn trong hypothesis testing, action là một kết luận mang một trong hai giá trị a0 hoặc a1,
> nên ta có thể thể hiện nó bởi λ(**X**) nào đó, là một Bernoulli random variable, để rồi khi
> quan sát **X** = **x**, λ(**X**) ghi nhận giá trị cụ thể λ(**x**) (= a0 hoặc a1), loss ghi nhận
> giá trị cụ thể L(θ, λ(**x**)) (là L(θ, a0) hoặc L(θ, a1)).
>
> Nhờ vậy, ta hiểu trong hypothesis testing, loss L(θ, λ(**X**)) là một Bernoulli random
> variable
>
> nên khi lấy trung bình, dĩ nhiên ta sẽ dựa trên distribution của Bernoulli:
>
> R(θ, λ(**X**)) = E_θ[L(θ, λ(**X**)]
>
> = L(θ, a0) * P_θ[L(θ, λ(**X**)) = L(θ, a0)] + L_θ(θ, a1) * P[L(θ, λ(**X**) = L(θ, a1)]
>
> = L(θ, a0) * P_θ(λ(**X**) = a0) + L_θ(θ, a1) * P(λ(**X**) =  a1)
>
> = L(θ, a0) * P_θ(**X** ∈ Acceptance region Rc) + L(θ, a1) * P_θ(**X** ∈ Rejection region R)
>
> Và tùy vào θ ở đâu:
>
> θ ∈ Θ0 ⇨ R = 0 * P_θ(**X** ∈ Rc) + 1 * P_θ(**X** ∈ R) = β(θ)
>
> θ ∈ Θ0c = R = 1 * P_θ(**X** ∈ Rc) + 0 * P_θ(**X** ∈ R) = P_θ(**X** ∈ Rc) = 1 - β(θ)
>
> Cuối cùng, nếu muốn thay đổi tương quan giữa hậu quả của hai loại Type I và II error, ta
> có thể thay đổi định nghĩa của loss, gọi là generalized 1-0 loss
>
> L(θ, a0) = 0 nếu θ ∈ Θ0, = cII nếu θ ∈ Θ0c
>
> L(θ, a1) = 0 nếu θ ∈ Θ0c, = cI nếu θ ∈ Θ0,
>
> Khi đó R(θ, λ(**X**)):
>
> Khi θ ∈ Θ0: R = cI * P_θ(**X** ∈ R) + 0 * P_θ(X ∈ Rc) = cI * β(θ)
>
> Khi θ ∈ Θ0c: R = cII * P_θ(**X** ∈ R) + 0 * P_θ(X ∈ Rc) = cII * (1 - β(θ))

<br>

<a id="node-120"></a>

<p align="center"><kbd><img src="assets/716d3c525b029fbeba6014906a56caf2c42c33ce.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6042c9481eddc6670360912cb3f54e07fad6180a.png" width="100%"></kbd></p>

> [!NOTE]
> Quay lại đây, trong bối cảnh machine learning, gs Bishop giới thiệu về cách tiếp
> cận decision theory: Ta sẽ dùng loss function (hay cost function) để phản ánh
> những hậu quả do các quyết định tạo ra. Thì có thể thấy nó y chang những gì đã
> học trong Casella. Chỉ khác là ta mở rộng lên K class, tức là decision rule không
> còn chỉ đưa ra một trong hai action a0 a1 nữa. Mà là a1,...aK, hay như trong
> sách, là C1,...Ck
>
> Và định nghĩa của loss, phải thể hiện bằng môt loss matrix:
>
> phần từ Lkj sẽ mang ý nghĩa là: [sự thật: T = k, decision rule gán cho class j],
> nên:
>
> khi k = j, tức là phần từ Lkk trên đường chéo, thì ta cho giá trị bằng 0: vì lúc này
> decision rule đoán đúng.
>
> còn k khác j, thì ta cho nó một giá trị dương ckj phản ảnh mức độ nghiêm trong
> của việc "đoán sai là class j trong khi thật sự là class k" này.
>
> Tất nhiên với K = 2, thì cái matrix loss này cũng chỉ cách thể hiện matrix cái hàm
> generalized loss mà ta vừa ôn trong Casella, đây nhé:
>
> Vừa nãy mới nói, ta define generalized loss:
>
> L(θ, a0) = 0 khi θ ∈ Θ0 và = cII khi θ ∈ Θ0c
>
> L(θ, a1) = 0 nếu θ ∈ Θ0c, = cI nếu θ ∈ Θ0,
>
> Thì loss matrix sẽ là:
>
> L11 = 0: phân loại đúng: θ ∈ Θ0, dự đoán a0: θ ∈ Θ0
>
> L12 = cI, thể hiện loss khi θ ∈ Θ0 và dự đoán lại là a1: θ ∈ Θ0c, đây là Type I
> error
>
> L22 = 0: phân loại đúng: θ ∈ Θ0c, dự đoán a1: θ ∈ Θ0c
>
> L21 = cII, thể hiện loss khi θ ∈ Θ0c mà dự đoán là a0: θ ∈ Θ0, đây là Type II error
>
> Nhưng lưu ý, θ **tuy đóng vai trò của** T **ở đây** nhưng **trong bối cảnh
> Casella, nó là fixed but unknown**. Do đó mới có vụ phải chia công thức của Risk
> function ra làm hai trường hợp ứng với θ nằm ở đâu.
>
> Còn **trong bối cảnh Bishop**, T **cũng là random variable**. Nên **ứng với mỗi ô
> trong loss matrix, là một joint event** của T và **X**.
>
> Ví dụ, ô Lkj sẽ là loss của event: T = k (class thật là j) và "mô hình phân lại là
> class j" , cũng là **X** ∈ Rj
>
> Để rồi ta sẽ thấy gs Bishop cũng là tính risk function (ông gọi là loss bằng cách
> **tổng lại hết rồi lấy kì vọng** nhưng mình hiểu **nó chính xác là risk function**
> trong Casella), và lúc này, thì chỉ việc dùng joint distribution của T, và **X**

<br>

<a id="node-121"></a>

<p align="center"><kbd><img src="assets/489bdf4fd51779463f4990296598fb1f13378372.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi, như vừa nói nó note trước, đây chính xác là việc mr Bishop làm ở đây: Tính risk function, là kì vọng của loss, với loss là
> tổng mọi loss ở các case khác nhau, define bởi loss matrix.
>
> Và như vừa nói, điểm khác biệt mấu chốt của risk function trong Casella là trong đó vẫn đang tiếp cận theo Classical, nên θ là
> fixed và unknown. Do đó khi lấy kì vọng của Loss, thì là lấy theo distribution của L(δ(**X**), θ), có tính ngẫu nhiên xuất nguồn
> từ tính ngẫu nhiên của **X**.
>
> Còn ở bối cảnh Bishop, T là random variable luôn, nên khi lấy kì vọng,  nên tại mỗi event ứng với mỗi ô trong loss matrix ứng
> với một joint event của hai biến ngẫu nhiên T và **X**, do đó khi lấy kì vọng**,** ta **dùng joint distribution** T và **X**: f(t, **x**)
> (trong sách là p(**x**, Ck)
>
> Từ đó giúp ta hiểu bản chất của cái công thức 1.80: chỉ là risk function trong Casella mà thôi, có điều đang theo Bayesian. Và
> trong Casella, khi dùng risk, nhưng đang theo trường phái Bayesian (ví dụ như khi tính risk của Bayes estimator δB(**X**) của
> θ), ta gọi nó là Bayes risk. **Tóm lại, cái 1. 80 trong sách Bishop** **chính là Bayes risk**.
>
> Còn cụ thể **vì sao dạng công thức của 1.80 là như vậy?**
>
> Phải hiểu thế này: Ta đang tính kì vọng của Loss, hàm nghĩa Loss là một random variable.
>
> Mà giá trị khả dĩ (possible value) của nó, sẽ phụ thuộc T và decision rule, và ta dùng cái loss matrix để liệt kê các possible
> value này. Ví dụ,
>
> Loss = L12 khi "class thật là 1, phân loại của decision rule là 2", thể hiện toán học của event này: (T = 1, **X** ∈ R2).
>
> Tượng tự,
>
> Loss = Lkj khi (T = k, **X** ∈ Rj)
>
> Nên Loss, là một **DISCRETE** random variable mà được **tạo ra bởi việc áp một hàm số sau đây** lên T, và **X**:
>
> g(t,**x**) = Lkj (giá trị của matrix loss tại hàng k, cột j) khi T = t, **X** = **x**.
>
> Nói cách khác, ta hãy nhìn loss matrix chính là định nghĩa một hàm số g(t,**x**):
>
> i) nhận vào input là t, và **x**, nó sẽ hỏi xem:
>
> t bằng mấy (C1 hay ...CK), ví dụ là Ck đi)
>
> **x** thuộc R mấy (R1, R2 hay RK), ví dụ bằng Rj
>
> ii) output ra giá trị hàng Lkj
>
> Nên hiểu g(t,**x**) = Lkj là như vậy.
>
> Hay g(t,**x**) = Lkj với k là index từ 1,..K sao cho t = Ck, j là index từ 1,..K sao cho **x** ∈ Rj
>
> Thể hiện theo toán học dùng **indicator function:** 
>
> I_(t = Ck), có giá trị = 1 khi t = Ck, = 0 kh t ≠ Ck
>
> I_(**x** ∈ Rj), có giá trị = 1 khi **x** ∈ Rj, = 0 khi x không thuộc Rj
>
> g(t, **x**) = Σk=1:K Σj=1:K Lkj I_(t = Ck) I_(**x** ∈ Rj)
>
> Từ đó giúp ta thấy rõ, việc tính cái kì vọng của cái biến ngẫu nhiên Loss này, đơn giản là dùng LOTUS:
>
> Nhớ lại LOTUS, nó nói rằng, khi ta có biến ngẫu nhiên Y được tạo thành bằng cách áp hàm g(x) lên biến ngẫu nhiên X, thì ta
> có thể tính EY bằng cách dùng pmf/pdf của X: EY = Σ{possible  x của X} g(x)P(X=x) hoặc ∫_{range X} g(x)f(x)dx
>
> Mà dù là tích phân hay sum thì đều có nghĩa là: marginalizing over mọi possible value của X đối với cụm g(x)f(x)
>
> Vậy thì đây, ta có LOSS, là **biến ngẫu nhiên có được bằng cách áp hàm** g(t,**x**) lên hai biến ngẫu nhiên T, **X**, thì việc
> tính E[LOSS] **cũng theo LOTUS**:
>
> E[LOSS] = marginalizing mọi possible value của T và **X** đối với g(t,**x**)f(t,**x**).
>
> Và để thực hiện cái việc marginalizing, vì ở đây T là biến rời rạc, nhận các giá trị possible value C1, C2,... CK. Còn **X** là biến
> liên tục. nên công thức sẽ là:
>
> Σ_{mọi possible value Cm của T} ∫_range_**X** g(t, **x**) f(t, **x**) d**x** = Σ_{mọi possible value Cm của T} ∫_range_**X** [Σk=1:K Σj=1:K Lkj I_(t = Ck) I_(**x** ∈ Rj)] f(t, **x**) d**x** = Σ_{mọi possible value Cm của T} ∫_range_**X** [Σk=1:K Σj=1:K Lkj I_(t = Ck) I_(**x** ∈ Rj)] | t=Cm f(Cm, **x**) d**x**
>
> Với t = Cm, [Σk=1:K Σj=1:K Lkj I_(t = Ck) I_(**x** ∈ Rj)] | t=Cm = [Σj=1:K Lkj I_(**x** ∈ Rj)]
>
> = Σ_{mọi possible value Cm của T} ∫_range_**X** [Σj=1:K Lmj I_(**x** ∈ Rj)] f(Cm, **x**) d**x** = Σ_m=1:K ∫_range_**X** [Σj=1:K Lmj I_(**x** ∈ Rj)] f(Cm, **x**) d**x**
>
> Tách cái tích phân trên toàn range **X** thành tổng tích phân các vùng R1,... RK
>
> = Σ_m=1:K Σn=1,..K ∫_Rn [ Σj=1:K Lmj I(**x** ∈ Rj) ] f(Cm,**x**) d**x**
>
> với việc đã xét n=1,...K ở miền ngoài tích phân thì cái tổng [ Σj=1:K Lmj I_(t = Ck) I(**x** ∈ Rj) ] bên trong vòng
> lặp này chỉ còn [ Σj=1:K Lmj I_(t = Ck) I(**x** ∈ Rj) ] | j=n ] chỉ còn là [ Lmn ]
>
> = Σ_m=1:K Σn=1,..K ∫_Rn [  Lmn ] f(Cm,**x**) d**x**
>
> Và và vì m, n chỉ là dummy name, đặt lại tên biến là k, j ta có
>
> Σ_k=1:K Σj=1,..K ∫_Rj Lkj f(Ck,**x**) d**x** Đây chính là 1.80
>
> Nhờ việc hiểu bản chất Loss là biến ngẫu nhiên define bởi hàm g, thì áp dụng kiến thức LOTUS, giúp ta hiểu vì sao công thức
> E[Loss] lại là như vậy.
>
> Còn nhờ học Casella, ta hiểu thấu bản chất đây chỉ là Bayes risk mà thôi.

<br>

<a id="node-122"></a>

<p align="center"><kbd><img src="assets/23e8a37e2e2251737671d6e0f9fac6fe9351677c.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi, thế thì, tiếp theo, mục tiêu sẽ làm giảm cái E[L] này, mà vừa rồi ta đã hiểu bản chất của nó chính là Bayes risks, cũng như vì sao nó có công thức như
> vậy.
>
> Lại recall liên kết với Casella chút xíu:
>
> Trong Casella, mình được nghe về khái niệm Bayes risk khi nói về việc đánh giá (evaluate) Bayes estimator của θ: δ^B(**X**). Như đã ôn lại ở các note
> trước, risk function là function được định nghĩa bằng trung bình của loss function. R(δ(**X**), θ) = E_θ[L(δ(**X**), θ], nên với risk function, trước tiên ta cần
> biết đang dùng loss gì (ví dụ squared error hay absolute error). Thế thì, ta cũng nhớ, khi nói về Bayes estimator, điểm quan trọng là hiểu rằng ta đang theo
> trường phái Bayesian, nên coi θ như biến ngẫu nhiên và từ đó đi xây dựng posterior distribution của θ. Và với distribution này, khi cần một point estimator
> cho θ, ta có thể nghĩ đến mean của nó: E[θ|**X**] Tuy nhiên, chưa chắc nó luôn là mean của posterior. Mà sự thật là: E[θ|**X**] chỉ là Bayes estimator khiến
> minimize risk function E_θ[L(δ(**X**), θ)] với L(δ(**X**), θ) đang dùng là squared error loss. Còn nếu loss là absolute error thì Bayes estimator khiến minimize
> risk function sẽ hóa ra chính là median của posterior.
>
> Vậy thì ở đây, việc ta đi minimize cái Bayes risk này, hoàn toàn tương ứng với việc ta đi tìm Bayes estimator giúp minimize risk function trong bối cảnh
> Casella. Nói vậy để thấy có sự liên kết giữa Casella và Bishop.
>
> Rồi, vậy thì như đã nói, khi đặt vấn đề minimize E[L] với công thức 1.80, biến số tối ưu ở đây là: **Cách chia range** **X** ra **thành một phân hoạch**
> (partition): R1,....RK.
>
> Có nghĩa là, không giống như trong bài toán tối ưu quen thuộc, trong đó ta đi tìm trong các giá trị cho phép của x để có được giá trị x* khiến hàm f(x*) là nhỏ
> nhất
>
> Thì ở đây ta lại đi tìm trong số các phân hoạch [R1,...RK] (định nghĩa phân hoạch: R1 U R2 U ...Rk = range X và intersection của chúng là tập rỗng) sao cho
> E[L] có giá trị nhỏ nhất
>
> Mà điều này cũng là vì bản chất là cũng vì, ta đang làm việc với bài toán classification, nơi mà mục tiêu của nó, là tìm được một quy tắc phân loại sao cho
> chính xác nhất, gỉam thiểu được sai lầm phân loại sai. Để rồi cũng y như trong bài toán Hypothesis testing, nơi mà thứ chúng ta tìm kiếm, cũng là một cái
> rule - giúp đưa ra quyết định rằng nên reject hay accept H0 tốt nhất, và cái rule này, cũng được thể hiện bởi việc nó sẽ phân chia range X thành rejection
> region R và acceptance region Rc.
>
> Nói vậy để thấy, việc ta đụng bài toán tối ưu mà trong đó thứ cần tìm (biến số tối ưu) là một phân hoạch không phải nay mới gặp.
>
> Quay lại đây ta có bài toán:
>
> minimize_{phân hoạch R1,...RK} Σk=1:K Σj=1,..K ∫_Rj Lkj f(Ck,**x**) d**x**
>
> Biến đổi objective chút xíu:
>
> Σk=1:K Σj=1,..K ∫_Rj Lkj f(Ck,**x**) d**x**
>
> Tích phân của tổng = tổng tích phân, bản chất tích phân chỉ là cái tổng, và  với các kí hiệu các tổng của tổng thì cứ thay đổi vị trí thoải mái:
>
> = Σj=1,..K ∫_Rj Σk=1:K Lkj f(Ck,**x**) d**x**
>
> = Σj=1,..K ∫_Rj  [Σk=1:K Lkj f(Ck,**x**)] d**x**
>
> Đặt hàm gj(**x**) = Σk=1:K Lkj f(Ck,**x**), ta sẽ xem xét ý nghĩa của cái cụm này sau.
>
> = Σj=1,..K ∫_Rj  gj(**x**) d**x**
>
> Dùng **indicator** **function** để chuyển tổng tích phân trên các vùng Rj thành tích phân trên toàn range **X**: Ij(**x**) = I_(**x** ∈ Rj), mang giá trị 1 hoặc 0
> tùy vào **x** ∈ Rj hay không
>
> ⇨..= Σj=1,..K ∫_range_**X**  Ij(**x**) gj(**x**) d**x**  Đưa nốt tổng j vào tích phân: =  ∫_range_**X** Σj=1,..K Ij(x) gj(x) dx   Đến đây viết lại bài toán: Tìm kiếm bộ phân hoạch R1,..RK / cũng là cái decision rule để gán class cho các data point **x** ∈ range **X**  sao cho minimize ∫_range_**X** Σj=1,..K
> Ij(**x**) gj(**x**) d**x**
>
> Để dễ hiểu, ta sẽ xem xét ý nghĩa của từng thành phần trong cái objective này:
>
> i) gj(**x**) = Σk=1:K Lkj f(**x**, Ck) là cái gì, ý nghĩa là gì?
>
> Để thấy cái này là gì, hãy nhớ về định nghĩa của kì vọng, trong Stat110, gs Joe Blizstein dạy ta rằng, bản chất của kì vọng của random variable X, chỉ là GIÁ
> TRỊ TRUNG BÌNH của nó. Ví dụ như nó là một biến rời rạc, có các giá trị khả dĩ x1,x2,...xn với xác suất mà nó (X) mang các giá trị đó quy định bởi P(X=x1),
> P(X=x),...Thì EX chỉ là weighted average - trung bình của X có gắn trọng số bởi xác suất tương ứng: Σi xi P(X=xi)
>
> Vậy thì ở đây trong công thức trên Lkj là mức phạt quy định khi gán **x** có T = k vào class j
>
> Và f(**x**, Ck) về cơ bản cũng có thể tương đương với xác suất mà T = Ck xảy ra.
>
> Nên Σk=1:K Lkj f(**x**, Ck) = Σk=1:K [mức phạt khi gán một data point thuộc class Ck vào class j] * [Xác xuất data point thuộc class Ck]
>
> và nó mang ý nghĩa là **Trung bình mức phạt khi gán data point x vào class Cj**
>
> Vậy gj(**x**): mức phạt trung bình khi gán data point x vào class Cj
>
> \-------
>
> ii) Σj=1:K Ij(**x**)gj(**x**) là cái gì:
>
> triển khai ra, = I1(**x**)g1(**x**) + I2(**x**)g2(**x**) + ..IK(**x**)gK(**x**)
>
> và nó sẽ có kết quả chỉ là một hạng tử trong đám này. Cái nào thì tùy vào **CÁCH PHÂN LOẠI ĐANG GÁN** **x** **CHO RỔ NÀO TRONG R1,..RK**, ví dụ
> gán x cho R2, thì I2(x) = 1, mấy cái khác = 0 ⇨ tổng này = 1*g2(**x**) = g2(**x**)
>
> Như vậy, nếu gj(**x**) là **mức phạt trung bình khi gán x vào class Cj**, mang ý nghĩa là: Mức phạt được **QUY ĐỊNH TRONG LUẬT**
>
> thì Σj=1:K Ij(**x**) gj(**x**) là **mức phạt THỰC TẾ, ghi nhận được khi mô hình THỰC HIỆN PHÂN LOẠI MỘT DATA POINT x.** iii) Vậy ∫_range_**X** Σj=1:K Ij(**x**)gj(**x**) là gì?
>
> Nó CHÍNH LÀ **TỔNG MỨC PHẠT THỰC TẾ**, ghi nhận được khi mô hình **THỰC HIỆN PHÂN LOẠI TOÀN BỘ x TRONG RANGE X**
>
> VẬY THÌ TỪ ĐÓ DỄ HIỂU RẰNG, **CÁI TỔNG MỨC PHẠT THỰC TẾ TRÊN TOÀN BỘ DỮ LIỆU SẼ NHỎ NHẤT** NẾU **MỨC PHẠT THỰC TẾ TRÊN
> TỪNG ÔNG x LÀ NHỎ NHẤT.**
>
> Ví dụ tổng mức phạt trên tập range X = {x1, x2, x3} sẽ dĩ nhiên là nhỏ nhất khi mức phạt trên từng ông là nhỏ nhất. Vì mấy ông này đâu có liên quan mẹ gì
> nhau. Nó sẽ chỉ không đúng nếu như: giảm mức phạt của ông x1 lại khiến tăng mức phạt của ông x2 chẳng hạn, thì khi đó, việc giảm mức phạt của từng
> ông mới khiến chưa chắc tổng mức phạt cả đám giảm. Nhưng ở đây thì chúng không liên quan gì nhau.
>
> Đó là lí do mà ta có thể chuyển bài toán tối ưu minimize ∫rangeX Σj=1:K Ij(**x**)gj(**x**) thành minimize Σj=1:K Ij(**x**)gj(**x**)
>
> Và như vậy, kiểu như ta sẽ có vô số bài toán tối ưu, mỗi cái ứng với với mỗi **x**:
>
> minimize Σj=1:K Ij(**x**)gj(**x**)
>
> ⇔ minimize Σj=1:K Ij(**x**)gj(**x**)
>
> = I1(**x**) g1(**x**) + ... + IK(**x**) gK(**x**)
>
> Và nên nhớ biến tối ưu là phân hoạch R1,...RK, hay cũng là bộ các hàm I1(**x**), I2(**x**),...Ik(**x**),
>
> Vì là một phân hoạch nên ràng buộc của chúng là: Chỉ một trong số các indicator function được  phép bằng 1. Ví dụ I1(**x**) = 1, thì I2(**x**) = ...IK(**x**) = 0,
> thể hiện rằng decision rule assign data point x cho class 1.
>
> Như vậy, đến đây **bài toán trở thành y như đặt vấn đề là**: 
>
> **TRONG SỐ CÁC HÀM INDICATOR** Ij(**x**) j = 1...K thì **CHO CÁI NÀO BẰNG 1 ĐỂ RA KẾT QUẢ NHỎ NHẤT**.
>
> Thì cũng chính là đồng nghĩa với: **CHỌN CÁI NÀO ĐỂ CÓ KẾT QUẢ NHỎ NHẤT TRONG ĐÁM {g1(x),...gK(x)**
>
> cũng là **CHỌN RA CÁI NÀO NHỎ NHẤT TRONG ĐÁM:** **{Σk=1:K Lk1 f(x, Ck), Σk=1:K Lk2 f(x, Ck), ..Σk=1:K LkK f(x, Ck)}**
>
> **VÀ ĐÓ CHÍNH LÀ Ý CỦA GS BISHOP KHI NÓI WE SHOULD MINIMIZE Σk Lkj p(x, Ck)**
>
> **trong câu nói "...which implies that for each x we should minimize Σk Lkj p(x, Ck)"**

<br>

<a id="node-123"></a>

<p align="center"><kbd><img src="assets/2bbe0abe4d9b56da91cf525031096b51d8c79a0f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a1e3712d245508f45be86a726cfccc200225786e.png" width="100%"></kbd></p>

> [!NOTE]
> Như vậy đến đây ta đã hiểu là cái optimal decision rule đó là:
>
> **CHỌN RA CÁI NÀO NHỎ NHẤT TRONG ĐÁM**: {Σk=1:K Lk1 f(x, Ck), Σk=1:K
> Lk2 f(x, Ck), ..Σk=1:K LkK f(x, Ck)} sau đó **LẤY INDEX** ĐỂ GÁN CLASS cho
> data point **x**.
>
> Gọi là j = argmin_{Σk=1:K Lkj f(**x**, Ck)}, mang ý nghĩa là **trong K cục** Σk=1:K
> Lkj f(x, Ck) j = 1,2..K thì **cục nhỏ nhất ứng với j bằng mấy**
>
> **Gán data point x cho Cj**, và **làm vậyvới mọi x**.
>
> (ví dụ trong K cục trên, cái thứ 2 là nhỏ nhất, thì j = 2, decision rule tối ưu sẽ
> gán data point vào class 2)
>
> Thì đó **chính là một phân hoạch / decision rule tạo ra Bayes risk nhỏ nhất**.
>
> Và vì f(**x**, Ck) = f(Ck|**x**)f(**x**) nên f(x) là như nhau và không âm
>
> xem trong đám {Σk=1:K Lkj f(**x**, Ck)} j =1,...K cái nào nhỏ nhất
>
> thì cũng là xem trong đám {Σk=1:K Lkj f(Ck|**x**)} j =1,...K cái nào nhỏ nhất
>
> Tóm lại cái optimal (minimize Bayes risk) decision rule là:
>
> Với mỗi **x**, gán cho nó class Cj với j = argmin Σk=1:K Lkj f(Ck|**x**)

<br>

<a id="node-124"></a>

<p align="center"><kbd><img src="assets/d9def9387d98a616750a6b298afbe623a6b03818.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/544c304360ad25a9e3f3da3689ccb1c517fcfcfa.png" width="100%"></kbd></p>

> [!NOTE]
> Đại ý là, như ta đã thấy vừa rồi, cái decision rule / hay classifier tối ưu xét theo
> tiêu chí giảm thiểu Bayes risk là cái mà ta assign class Ck cho data point **x**
> với k = argmin_j [trung bình loss khi assign class j cho **x,** = Σk Lkj f(Ck|**x**)]
>
> Nếu các mức penalty cho các loại error đều cho bằng nhau = 1 Lkj = 1 với mọi k
> khác j và bằng 0 khi k = j thì decision rule nói trên trở thành:
>
> Khi đó, gj(x) = Σk=1:K Lkj f(Ck|**x**) = Σk≠j f(Ck|**x**) = 1 - f(Cj|**x**) (do Σk
> f(Ck|**x**) = 1)
>
> ⇨ rule trở thành:
>
> Assign Ck cho **x**, với k = argmin_j [1 - f(Cj|**x**)]
>
> cũng là k = argmax_j [f(Cj|**x**) - 1]
>
> = argmax_j f(Cj|**x**)
>
> có ngghĩa là trở thành cái rule mà giúp giảm misclassification error (không coi
> trọng loại error nào hơn cái nào): gán class nào thì dựa vào posterior f(t|x) nào
> lớn nhất
>
> Tuy vậy, không có gì chắc đây là rule tuyệt đối đúng.
>
> Có nghĩa là, cái Ck với k = argmax_j f(Cj|**x**) không có gì đảm bảo chính là
> class thật sự của **x**.
>
> Do đó, vẫn có thể có misclassification error.
>
> Và nó xảy ra khi: ví dụ với **x1,** posterior f(C2|**x**) là cao nhất, nhưng nó
> không vượt trội, để rồi, f(C1|**x**) cũng ko nhỏ. Và sự thật thì C1 mới là class
> đúng.
>
> Nên lúc này, khi f(C2|**x**) và f(C1|**x**) xem xem nhau, tuy f(C2|**x**) là lớn nhất. Và
> cũng đồng nghĩa là f(C2|**x**) cách khá xa mức tuyệt đối (=1, gs Bishop gọi là
> unity).
>
> Và đây là khi misclassification error có thể xảy ra.
>
> Nói chung là, ta chỉ có thể đảm bảo misclassification error không xảy ra khi
> f(C2|**x**) = 1, để rồi assign class C2 cho data point x thì sẽ đảm bảo chính xác.
> Tuy nhiên chỉ cần f(C2|**x**) < 1, thì đồng nghĩa vẫn có xác suất class đúng là class
> khác chứ ko phải C2.
>
> Thành ra, ta có thể đưa ra option thứ 3: (giả sử đang dự đoán giữa hai class C1
> vs C2) là: Không biết - Từ chối đoán - bằng cách sau khi tính posterior của các
> class thì không dựa vào việc cái nào có lớn nhất để đưa ra phân loại ngay lập
> tức, mà xem posterior có lớn hơn một cái threshold (α, hay trong sách là θ) hay
> không, ví dụ, chỉ kết luận nếu posterior lớn nhất lớn hơn 80%. Còn không thì
> đưa ra option: Từ chối phân loại, ko biết, mời bạn đoán.
>
> Tương tự, ta cũng có thể làm vậy bài toán có loss matrix (ý là có ưu tiên loại
> error này hơn error kia)

<br>

<a id="node-125"></a>

<p align="center"><kbd><img src="assets/b8489be132887ff1b2c26e8d99d5f4d1e93ff2e0.png" width="100%"></kbd></p>

> [!NOTE]
> HÌnh minh họa cho thấy vùng giữa hai đường xanh lá, nơi đó posterior tại  hai class
> (ý là f(t|x)|t=C1 và f(t|x)|t=C2)  có giá trị khác biệt không lớn. Và ta sẽ từ chối đưa ra
> quyết định phân loại

<br>

<a id="node-126"></a>

<p align="center"><kbd><img src="assets/b78606c3dd716321513e8385bfdb6e2c48cdd2a6.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/48d2b2fb3bdafb9fe8292971a60e154db46f19b1.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái gs nói là bữa giờ ta đang tiếp cận bài toán classification theo hai
> bước: bước một là dựa trên data, đi xây dựng posterior distribution f(t|**x**)
> (trong sách là p(Ck|**x**)), đây chính là bước gọi là inference state
>
> (liên hệ với Statistical Inference - Casella,  bài toán inference là bài toán đi
> xây dựng một suy đoán về tham số của population distribution, có thể là một
> point estimator W(**X**) để estimate giá trị của θ, hypothesis test  để đưa ra
> suy đoán về θ nằm ở Θ0 hay Θ0c, hoặc một interval estimator C(**X**) để
> estimate một khoảng / một set mà có thể chứa θ, thì nói chung, ta hiểu
> inference là việc ta muốn suy đoán về sự thật của phân phối xác suất chi
> phối dữ liệu quan sát thấy)
>
> Sau đó, ta mới dựa trên posterior để thông qua decision theory giúp đưa ra
> prediction, đây gọi là decision stage.
>
> Thế thì, ông cho biết, có một cách làm khác, không cần chia ra hai bước,
> mà làm luôn trong một lần: vừa "học" ra / suy luận / inference posterior
> và vừa đưa ra dự đoán luôn, thông qua hình thức là học một function map
> giữa input và decision, gọi là DISCRIMINANT function**.** Dừng lại chút, mình vừa hiểu ra một việc: Lấy ví dụ một neural network,
> hay deep learning model, thì bằng cách training một mapping function
> giữa ảnh đầu vào và phân loại ảnh đầu ra, mình có thể hiểu bên trong nó
> đang làm hai việc cùng lúc: học ra posterior distribution và thực hiện
> decision. Nhưng có những loại khác, nó ko tìm cách học posterior, mà
> chỉ học luôn cái mapping function, gọi là discriminant function nói trên.
>  Hay, ví dụ như mình đã từng học về VAE trong cs231n cũng vậy, encoder
> là cái khúc nó sẽ học ra posterior distribution, và decoder là một mô hình
> đóng vai trò sampling từ posterior distribution đó.

<br>

<a id="node-127"></a>

<p align="center"><kbd><img src="assets/9d1b8106122b27e1686ac14b352221e1486756f5.png" width="100%"></kbd></p>

> [!NOTE]
> Có ba cách tiếp cận cho bài toán decision (tạm hiểu là classification). 
>
> Loại thứ nhất: Đầu tiên, ta giải bài toán inference: 
>
> Học / xây dựng f(**x**|t) với từng possible value của t: C1,...CK. (tức là
> theo kí hiệu của gs Bishop: p(**x**|Ck).
>
> Học / xây dựng f(**t**).
>
> Dùng Bayes theorem, chuyển nó thành posterior của T:
>
> f(t|**x**) = f(**x**|t) f(t) / f(**x**).
>
> Với f(**x**) có thể dùng LOTP để tách thành:
>
> Σ{mọi possible value của t} f(**x**, t)
>
> = Σ{mọi possible value của t} f(**x**|t)f(t)
>
> Từ đó, ta có giá trị của f(t|x) với mỗi giá trị của {C1,...CK} của t
>
> Và cho phép ta dùng decision theory như đã biết để make decision.
>
> Mình có thể nhận ra đây chính là Naive Bayes
>
> Gs cho biết những cách tiếp cận mà trong đó ta thực hiện bước suy luận về
> **distribution của input và** output, tức là học ra f(t, **x**) thì gọi là **generative** model.
> Vì, nếu ta có distribution của input, ta có thể thực hiện sampling từ đó,
> để có thể có một dạng dữ liệu synthetic (ý là ví dụ như ảnh do ta tạo ra, 
> không phải ảnh chụp ở ngoài đời thật, ví dụ mấy mô hình tảo ảnh hiện nay
> như diffusion model)

<br>

<a id="node-128"></a>

<p align="center"><kbd><img src="assets/d77ddcee5c7624b12a07f377f532c34bc1c48067.png" width="100%"></kbd></p>

> [!NOTE]
> Cách tiếp cận thứ hai, là inference ra trực tiếp posterior f(t|**x**) và sau đó thì
> dùng nó để make decision. 
>
> Nó khác cái trước ở chỗ, ta không cần học ra f(**x**|t) f(t). Mà chỉ học thẳng
> ra f(t|**x**) thôi.
>
> Cái này như bữa giờ đang làm, gọi là discriminative models

<br>

<a id="node-129"></a>

<p align="center"><kbd><img src="assets/4986c8283d8861b668bfead102d0fc4b60efc51c.png" width="100%"></kbd></p>

> [!NOTE]
> Và cuốn cùng là discriminant function như nãy nói. Cái này nó ko cần học
> phân phối xác suất gì hết, nó chỉ là tìm ra cái mapping function giữa t và x.
> t = f(x). Xác suất ko có vai trò gì hết

<br>

<a id="node-130"></a>

<p align="center"><kbd><img src="assets/fbee5581e24dbbe6a2c0b611821153cd55983710.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0e5e5ef8b66da5fe05798a7bdc7df75b7a9e2857.png" width="100%"></kbd></p>

> [!NOTE]
> Bàn một chút về ưu nhược diểm của 3 cách làm này.
>
> Cách đầu tiên, đại khái là vì ta dù implicitly hay explicitly (tường minh hoặc
> ngầm định) xây dựng joint distribution f(t,**x**) (vì infer f(**x**|t), f(t) thì cũng là
> xây f(**x**,t)) thì đều cần nhiều data.
>
> Ưu điểm là, ta có thể có f(**x**) (bằng cách marginalizing f(**x**, t) over range T
> và cái này, là prior distribution của x. Do đó có thể dùng nó để tính  xác suất
> của một input. Và áp dụng vào bài toán phát hiện bất thường.
>
> Nói rõ hơn tí, thì đại ý là: ví dụ trong bài toán phân loại ảnh, thì input x, là
> ảnh, t là phân loại (class), thì ý nghĩa của f(**x**) là hàm xác suất của ảnh,
> công dụng là, bỏ vào một **x** - vector đại diện của một ảnh, nó sẽ cho biết xác
> suất là cao hay thấp. Vậy ta có thể dùng nó như một hàm check để phát
> hiện khi nào thì ta có một x có xác suất thấp → thì đó chính là một tấm ảnh
> có sự bất thường gọi là outlier

<br>

<a id="node-131"></a>

<p align="center"><kbd><img src="assets/6770520e6b9d5eea53f5ea36f8ca1f37780827d8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d595eacbaf31b8aa53c97d350f4f9f383e5a05ee.png" width="100%"></kbd></p>

> [!NOTE]
> Tuy nhiên, nếu như ta chỉ muốn làm bài toán classification thì việc học ra joint 
> distribution f(**x**, t) là quá lãng phí. Vì như đã biết, cũng như trong cách b, 
> để phân loại, ta chỉ cần dựa trên posterior f(t|**x**). 
>
> Nên sẽ ít tốn kém hơn nếu ta học trực tiếp hàm posterior thay vì đi tìm f(**x**, t)
> rồi mới dùng để có posterior.
>
> Ông nó nói cái ý, f(**x**|t) với t = C1,...CK có những cấu trúc ít ảnh hưởng đến 
> posterior, thì ý là do đó việc làm theo cách a) để tiếp cận bài toán classification
> là không mang lại lợi ích gì cả.
>
> Ví dụ như trong minh họa bài toán có 2 class C1, C2 và input 1D x này.
>
> Đồ thị của f(x|C1) và f(x|C2) ở bên trái cho thấy có các đỉnh.
>
> Nhưng đồ thị của posterior f(C1|x), f(C2|x) thì lại chẳng phản ánh gì tương
> ứng tại các đỉnh này. Đó là ý gs Bishop nói những structure của class
> conditional density chả có đóng góp gì cho posterior cả.
>
> Còn cái cách (c), thì chả cần posterior gì, chỉ là học cái mapping function
> nhận vào x, nhả ra C1 hay C2...
>
> MInh họa trong hình gs nói, nó sẽ tương ứng với việc ta tìm cách học ra
> function: f(x) sau đây: f(x) = C1 nếu x < c, và C2 nếu x > c với c là cái điểm
> ứng với đường màu xanh lá, chính là nơi mà nếu dùng nó để assign class,
> ta sẽ minimize misclassification rate

<br>

<a id="node-132"></a>

<p align="center"><kbd><img src="assets/1098de16646aa71a6a777b54d6033cb0e4d0985a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/840de2f3b8d4eb446e9abaafd4add8cc29a1c76a.png" width="100%"></kbd></p>

> [!NOTE]
> Với c, tuy vậy, ta sẽ ko có posterior,  mà cái này thì rất hữu dụng.
>
> Ví dụ, ví dụ như bài toán mấy bữa nay làm, khi ta define ra cái loss matrix
> quy định mức phạt khác nhau cho các loại error khác nhau. Nếu ta làm
> theo cách làm bữa trước, thì khi muốn thay đổi loss matrix, thì chỉ việc thay
> đổi, cái posterior sẽ được cập nhật theo rất đơn giản (trivially). Còn nếu ta
> làm theo cách c, ta phải train lại từ đầu (afresh)
>
> Hơn nữa, posterior sẽ giúp ta có thể reject, ko đưa ra quyết định khi cảm
> thấy ko chắc

<br>

<a id="node-133"></a>

<p align="center"><kbd><img src="assets/dbe58a3b19e9ba425e5bac5fa026380eb9493ec4.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi đoạn này nói về một ý nữa mà việc dùng posterior sẽ mang lại lợi ích
> mà  cách làm (c) ko có:
>
> Ví dụ như trong bài toán phân loại cancer hay ko cancer từ ảnh chụp X
> quang mà ta đang làm bữa giờ. thì có có vấn đề này (là cái mà mr Andrew
> Ng đã nói trong MLSpec: **Skewed dataset**). Trong thực tế, số ca cancer là ít
> hơn nhiều so với không cancer (này nói ở đâu chứ ko phải Việt Nam). Nên
> dễ hiểu là giả sử tỉ lệ cancel trong dân số chỉ là 0.1%, thì một cái mô hình
> tào lao nhận vào input x và luôn trả ra là ko cancer, sẽ vẫn có thể có kết
> quả chính xác rất cao.
>
> Rồi, và vì số ca cancer ít, nên x-ray cancer cũng ít hơn x-ray ko cancer,
> nên nếu dùng chúng để training mô hình thì có thể sẽ không hiệu quả. Khi
> đó ta có thể tạo một dataset cân bằng hơn giữa có và không cancer.
>
> Nhưng vấn đề là, posterior, f(t|**x**) theo bayes rule = f(**x**|t)f(t)/f(**x**), nên dễ thấy
> nó sẽ tỉ lệ thuận với f(t) - tức priori.
>
> Thành ra, một khi mà ta đã "chỉnh sửa": bằng cách tạo dataset cân bằng
> hơn, ta đã thay đởi prior distribution.
>
> Do đó, cách làm là, sau khi dùng data cân bằng để học ra posterior, ta  sẽ
> lấy cái posterior scale lại với tỉ lệ của prior, và normalizing lại. Vầy nè:
>
> Giải sử có C1, C2, Trong đó f(C1) = 0.9 f(C2) = 0.1 (tức hàm ý, 10 người
> thì 9 ca ko cancer, 1 người có cancer)
>
> sau khi dùng một dataset cân bằng (50% là hình có cancer, 50% là hình
> không cancer) để train ra posterior f(t|**x**)
>
> Ta sẽ điều chỉnh lại:
>
> f^(C1|**x**) = f(C1|**x**) * 0.9/c
>
> và
>
> f^(C2|**x**) =  f(C2|**x**) * 0.1/c
>
> với c là normalizing constant giúp f^(C1|**x**) + f^(C2|**x**) = 1
>
> như vậy lúc này posterior sau điều chỉnh đã phản ánh lại được tỉ lệ mắc
> bệnh / không mắc bệnh của prior.
>
> Nên cái này gọi là Đền bù (compensate) lại class prior
>
> Mấu chốt là, nếu làm theo (c) ta sẽ ko làm vậy được

<br>

<a id="node-134"></a>

<p align="center"><kbd><img src="assets/af092b7e2174655d56fcf9ada3b7803c15b07ff8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/55244556e3f8a4e4ca310fc1b7657e979564c425.png" width="100%"></kbd></p>

> [!NOTE]
> Đại ý là, một công dụng nữa của cách tiếp cận posterior là ta giải quyết một bài
> toán phức tạp bằng cách tách nó ra thành các bài toán đơn  gỉan hơn.
>
> Ví dụ: Dự đoán bệnh cancer hay không dựa trên ảnh X-quang và kết  quả xét
> nghiệm máu. Khi đó ta muốn xây dựng posterior: f(t|**x**I, **x**B)  distribution
> của T dựa trên vector X-ray image **x**I, và kết quả xét nghiệm máu **x**B
>
> thì đại khái là, bằng cách đặt assumption rằng f(**x**I,**x**B|Ck) =
> f(**x**I|Ck)f(**x**B|Ck) ta sẽ dựa trên Bayes rule như thường lệ để xây dựng
> posterior:
>
> f(t|**xI**,**xB**) = f(**xI**,**xB**|Ck)f(Ck)/f(**xI**,**xB**)
>
> ∝ f(**xI**,**xB**|Ck)f(Ck)
>
> ∝ f(**xI**|Ck)f(**xB**|Ck)f(Ck)
>
> ∝ [f(Ck|**xI**)f**(xI**)/f(Ck)] [f(Ck|**xB**)f(**xB**)/f(Ck)] f(Ck) | dùng Bayes rule với f(xI|Ck),
> f(xB|Ck)
>
> ∝ f(Ck|**xI**) f(**xI**) f(Ck|**xB**) f(**xB**) / f(Ck)
>
> ∝ f(Ck|**xI**) f(Ck|**xB**) / f(Ck) | bỏ f(**xI**), f(**xB**) là constant
>
> f(Ck), prior của T thì có thể xấp xỉ bằng cách dùng tỉ lệ class Ck trong data.
>
> Như vậy là ta đã có thể có f(t|**xB**,**xI**). Đây chính là Naive Bayes. 
>
> Nói nó Naive
> (ngây thơ) là vì, ta đang giả định là dựa trên T = Ck thì **X**_image và **X**_blood
> độc lập. Nhưng sự thật đâu phải vậy, ví dụ, nếu đã biết là Ck rồi, thì việc biết
> ảnh **X_image** có thể đoán được chỉ số máu **X_blood**

<br>

<a id="node-135"></a>

<p align="center"><kbd><img src="assets/0dccf959abb61195a046deb7574ef7ad78420432.png" width="100%"></kbd></p>

> [!NOTE]
> Chuyển qua bài toán decision theory trong linear regression. Trong đó, 
> ta đưa ra dự đóan t = y(**x**) cho mỗi input **x**, mỗi một dự đoán như vậy,
> tạo ra loss L(t, y(**x**)). Và average loss E[L] theo công thức 1.86. Vì sao?
>
> Đơn giản, L(**t**,y(**x**)) là hàm, nên Loss = L(**T**, y(**X**)) là random variable  
> tạo ra bởi việc áp một hàm số lên hai random variable T, **X**. Và như đã học
> ở Stat110, Casella, 2D LOTUS
> cho phép ta tính EZ của Y = g(X,Y) dựa theo joint pdf/pmf f(x,y) của X, Y: 
>
> EZ = Eg(X,Y) = ∫∫g(x,y)f(x,y)dxdy
>
> Vậy thì đây cũng vậy, LOTUS cho phép tính EL dựa theo joint distribution
> của T, **X**
>
> E[L] = ∫∫L(t, y(**x**)) f(t,**x**) d**x** dt

<br>

<a id="node-136"></a>

<p align="center"><kbd><img src="assets/76dfd43ed8e3254d646ad24bf925cd156408d3d1.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f0a1f03a94e7bd2908d8ca537fc813ac315a0eac.png" width="100%"></kbd></p>

> [!NOTE]
> Một lựa chọn phổ biến cho loss trong regression problem là squared loss, L(t, y(**x**)) = (y(**x**)
> \- t)^2
>
> khi đó E[L] = ∫∫[y(**x**) - t]^2 f(**x**, t) d**x** dt
>
> Đến đây, mình hiểu là ta sẽ coi E[L], như một hàm g(y, t) để thử derive y khiến minimize g(y, t).
>
> Dùng đạo hàm, điều kiện cần tối ưu bậc nhất: đạo hàm đối y của g = 0 để tìm critical point:
>
> ∂/∂y g(t,y) = 0
>
> ⇔ ∂/∂y ∫∫[y(x) - t]^2 f(**x**, t) d**x** dt = 0
>
> Đạo hàm của tích phân, mình còn nhớ trong Casella có nói đến theorem nói rằng trong một số
> điều kiện, có thể đổi chỗ hai cái này, (trường hợp này là khi cận tích phân ko phụ thuộc y(**x**))
>
> Ở đây có lẽ là thỏa điều kiện đó.
>
> ⇔ ∫∫ ∂/∂y(**x**) {[y(**x**) - t]^2 f(**x**, t)} d**x** dt = 0
>
> ⇔ ∫∫ [∂/∂y(**x**) [y(**x**) - t]^2] f(**x**, t) d**x** dt = 0
>
> Xét ∂/∂y(x) [y(x) - t]^2
>
> = ∂/∂[y(**x**)-t] [y(**x**) - t]^2 . d/dy(**x**) [y(**x**) - t]
>
> = 2[y(**x**) - t]
>
> .. ⇔ ∫∫ 2[y(**x**) - t] f(**x**, t) d**x** dt = 0
>
> ⇔ 2 ∫∫ [y(**x**) - t] f(**x**, t) dx dt = 0
>
> ⇔ ∫∫ y(**x**) f(**x**, t) d**x** dt - ∫∫ t f(**x**, t) d**x** dt = 0
>
> ⇔ ∫∫ y(**x**) f(**x**, t) d**x** dt = ∫∫ t f(**x**, t) d**x** dt
>
> Xét vế trái:
>
> ∫∫ y(**x**) f(**x**, t) d**x** dt = ∫_range X ∫_range_T y(**x**) f(**x**, t) dt d**x** = ∫_range_**X** y(x) {∫_range_**T**  f(**x**, t) dt}  d**x** ∫_range_T  f(x, t) dt chính là marginalizing joint pdf của **X**, T với mọi mọi T, sẽ được
> marginal pdf của **X** .. = ∫_range_**X** y(**x**) f(**x**) d**x**
>
> Xét vế phải:
>
> ∫∫ t f(**x**, t) d**x** dt = ∫_range **X** [∫_range **T** t f(**x**, t)  dt ] d**x**  Vậy phương trình trở
> thành ∫_range_**X** y(**x**) f(**x**) d**x** = ∫_range **X** [∫_range T t f(**x**, t) dt ] d**x**
>
> Vì tính chất complete flexible của y(**x**), cho phép:
>
> ⇔ y(**x**) f(**x**)= ∫_range T t f(**x**, t) dt
>
> ⇔ y(**x**) = [∫_range T t f(**x**, t) dt] / f(**x**)
>
> = [∫_range T t f(t|**x**) f(**x**) dt] / f(**x**)
>
> = [∫_range T t f(t|**x**) dt] f(**x**) / f(**x**)
>
> = ∫_range T t f(t|**x**) dt
>
> Đây chính là E(T|**x**), trung bình của  T ~ posterior distribution f(t|**x**)
>
> Như vậy, khi dùng squared loss thì cái hàm y(**x**) giúp minimize trung bình loss E[L] chính là
> cái hàm y(**x**) dùng mean của posterior f(t|**x**) để dự đoán.
>
> Thật ra cái này trong Casella đã học rồi cụ thể là khi ta học về Bayes estimator cho θ, thì ta đi
> tìm posterior π(θ|**x**).
>
> Lúc này nếu muốn có point estimator cho θ, ta có thể lấy mean, hoặc median, và chúng đều là
> Bayes estimator.
>
> Nhưng mean, E[θ|**x**] sẽ là cái Bayes estimator giúp **giảm risk function khi loss là square
> error loss**. Còn median của posterior sẽ là Bayes estimator giúp **giảm risk là absolute error
> loss**.
>
> Ôn lại về loss function và risk function học trong Casella:
>
> Loss function, là hàm của estimator L_θ(δ(**X**), θ), có thể là square error loss: [δ(**X**) - θ]^2
> hoặc absolute error loss: |δ(**X**) - θ|.
>
> Risk function: E_θ[L(δ(**X**), θ)], mang ý nghĩa: Average loss over mọi **X**, để còn lại là hàm
> theo θ, để so với nhau giúp evaluate δ(**X**).
>
> Vậy ở đây cũng y chang, cũng là: khi ta muốn từ posterior f(t|**x**) để đưa ra một point estimator
> cho T thì mean E[T|**x**] sẽ là cái giúp giảm thiểu average square loss (chính là risk function đó)
>
> và ở trong sách Bishop đoạn này, dù ko nói, ta cũng đoán được, nếu muốn giảm thiểu average
> absolute loss, thì nên dùng median của posterior.
>
> Và từ đây cũng giúp mình nhớ lại để hiểu vì sao trong bài revising curve fitting, ta thấy gs
> Bishop assume Ti ~ Normal(y(xi,**w**), 1/β), hành động này chính là dùng mean của posterior
> f(ti|xi), tức E[Ti|xi] để làm point estimate cho t, và theo decision theory, nó là tối ưu. Nếu ông
> dùng median của posterior để point estimate cho T thì nó sẽ cũng là tối ưu nhưng theo tiêu chí
> giảm thiểu average absolute error loss.

> [!NOTE]
> Sẵn tiện đang nói bài toán linear regression, sẽ có ích nếu ta ôn lại chút.
>
> Nhớ lại một nhận định khi ta làm bài toán curve-fitting theo Bayesian approach và cũng đã thấy rằng maximize
> likelihood chính là giải bài toán curve fitting với error function là sum squared error. Để thấy rằng vì sao khi đó:
>
> Còn nhớ, trong bài toán đó, cụ thể là phần Revisiting curve fitting problem, nơi mà gs Bishop dắt ta quay lại xem
> xét bài toán polynomial curve fitting theo góc nhìn xác suất thì ông đưa ra những thay đổi sau: đầu tiên, ứng với
> mỗi xi, coi Ti là một random varible, để phản ánh tính uncertainty của nó.
>
> Và assume distribution của nó là Ti ~ Normal(y(xi, **w**), 1/β)
>
> và cái assumption này cũng chính là assume Ei = Ti - y(xi, **w**), tức sai số của dự  đoán và giá trị thật sẽ là một
> Normal(0, 1/β).
>
> Chú ý, cho tới đây, **w**, tham số của polynomial function, vẫn đang được coi như fixed & unknown, nên y(xi,
> **w**) cũng vậy, fixed & unknown, báo hiệu rằng ta vẫn đang ở trong trường phái cổ điển.
>
> Rồi, từ đó, ta mới xây dựng joint distribution của T1,...TM f**T**(**t**). Nhờ tính chất độc lập của các cặp (xi, Ti) ta
> mới phân tách joint probability bằng tích marginal probability
>
> fT(**t**) = Πi=1:N f(ti)
>
> Thể hiện sự phụ thuộc với xi, **w**, β ta sẽ có:
>
> f**T**(**t**|**x**, **w**, β) = Πi=1:N f(ti|**w**, xi, β) Tới đây sao nữa? Nhớ lại các cách tiếp cận trong Casella trong bài toán point estimator cụ thể là maximum
> likelihood estimator.
>
> Theo định nghĩa θ^_ml(**X**) = argmax_θ L(θ|**X**), là θ giúp giải thích hợp lí nhất cho gía trị quan sát được của
> **X**. Với hàm likelihood được định nghĩa là L(θ|**x**) = f(**x**|θ) Do đó θ^_ml(X) = argmax_θ f(**x**|θ).
>
> Vậy thì ở đây, để đi tìm **w** (cũng chính là tìm y(xi,**w**), ta cũng có thể đi theo hướng này, đó là, tìm **w** giúp
> giải thích hợp lí nhất cho giá trị quan sát được t1,t2..tN ứng với x1,..xN (chú ý, chỉ có T là random variable,
> chứ **X** thì không, nên vector **x** không phải là giá trị quan sát được của vector random variable **X** nào cả.
>
> **w**_ML = argmax_**w** L(**w**|**t**)
>
> và likelihood L(**w**|**t**) cũng define bởi f(**t**|**x,w**,β) = Πi=1:N f(ti|xi,**w**,β) với f là pdf của Normal(y(xi,
> **w**), 1/β)
>
> nên bài toán là: maximize Πi=1:N f(ti|xi,**w**,β)
>
> và cũng dùng các trick để đưa về bài toán tối ưu tương đương, như thay maximize objective likelihood bằng
> minimize - log likelihood,..ta sẽ giải ra **w**_ML. và tương tự (1/β)_ML
>
> Và khi làm vậy ta sẽ thấy, bài toán tối ưu tương đương giúp tìm w_ML chính là đi minimize error function là sum
> squared error Σi (y(**w**,xi) - ti)^2 mà trong phần đầu tiên, khi làm quen với bài toán polynomial curve fitting ta đã
> làm (lúc đó chưa theo góc nhìn xác suất gì cả)
>
> \-----
>
> Trước khi recall tiếp phần Bayesian inference, ta nhắc lại nhận định rút ra được trong note liền trước (khi có
> posterior f(t|x) thì dùng mean của nó để point estimator cho T chính là cách để minimize average squared error
> loss)
>
> Khi gs Bishop giả định Ti ~ Normal(y(xi,**w**), 1/β) thì chính là dùng mean của posterior f(ti|xi): E[Ti|xi] để làm
> point estimate cho T thì **theo decision theory**:
>
> Nếu theo tiêu chí giảm thiểu **average square error loss** của decision theory: lấy E[Ti|xi], tức **mean** của f(ti|xi) 
>
> Nếu theo tiêu chí giảm thiểu **average absolute error** **loss** thì ta cần lấy **median** của f(ti|xi)
>
> Nhưng việc nhắc đến square loss của decision theory vừa rồi không liên quan gì đến việc khi ta maximize
> likelihood dưới giả định Ti ~ normal(y(xi,**w**),1/β) ta thấy nó hóa ra cũng là minimize sum squared error, cái này
> chỉ là trùng hợp.
>
> Vì giả sử ta assume Ti là expo(y(xi,**w**)), hay distribution nào khác: tức cũng là mean của posterior f(ti|xi), để
> rồi đi maximize likelihood, khi đó, ta sẽ thấy nó chưa chắc đã là minimize sum squared error. Tuy nhiên, miễn là
> ta lấy mean của posterior f(ti|xi) để làm point estimator cho T thì theo decision theory, đó vẫn là tốt nhất theo tiêu
> chí giảm average squared error loss.
>
> \------
>
> Sẵn trớn recall lại luôn: Sau đó, qua phần Bayesian inference, gs Bishop bắt đầu mới nói về việc trong
> Bayesian, ta sẽ coi tham số **w, cũng là random variable nốt**, từ đó viết hoa **W** để chỉ random variable
> vector. Mà cái này như mình đã biết ở Casella, khi ta bước sang trường phái Bayesian, thì ta cũng coi θ là
> random quantity. Để rồi nó sẽ có prior distribution π(θ), thường được chọn do kinh nghiệm của experimenter,
> sau đó dùng Bayes theorem, ta tìm distribution của θ khi đã biết **X** = **x**:  π(θ|**x**) = f(**x**|θ) π(θ) /
> f(**x**). Áp dụng vài bài toán curve fitting. Ta sẽ chọn Normal(0, (1/α)**I**) làm priori.
>
> Áp dụng Bayes theorem, xây dựng posterior:
>
> π(**w**|**t**,**x**,β,α) = f(**t**|**x**,**w**,β) π(**w**|α) / f(**t**|**x**)
>
> Với f(**t**|**x**,**w**,β) là joint distribution của T1,..Ti, = Πi=1:N f(ti|xi,**w**,β) = Πi=1:N Normal(ti|y(xi,**w**),1/β)
>
> Còn π(**w**|α) là priori = Normal(**w**|0,(1/α)***I**)
>
> Đến đây, nếu trong Casella, khi nói về Bayes estimator, sau khi xây dựng posterior xong, ta sẽ lấy mean hay
> median của nó để làm point estimator cho θ. Cụ thể, E[θ|**x**] chính là Bayes estimator giúp minimize risk
> function khi loss dùng squared error loss. Còn khi loss dùng absolute error  thì Bayes estimator giúp minimize
> risk function sẽ là median của posterior distribution.
>
> Còn trong Bishop, một hướng đi, là ta đi tìm **w** giúp maximize cái posterior π(**w**|t,x) này. Mà thực ra, trong
> bài toán này p**osterior hóa ra cũng là Gaussian**, nên tìm w có posterior lớn nhất **cũng là lấy mean của
> posterior** thôi
>
> Và khi đó ta sẽ thấy cách làm này cũng sẽ chính là tương đương với giải bài toán regularized least square: tức
> là minimize sum squared error với regularization term là hàm bậc hai của **w**.
>
> Và khi có **w*** maximize posterior rồi thì ta có thể dùng nó để dự đoán cho new x: y(x, **w***)
>
> Cũng đồng nghĩa là lấy mean của f(t|x,**w***) là Normal(y(x, **w***), 1/β) để dự đoán cho t.
>
> Nhưng cách làm Bayesian toàn diện hơn: là bằng cách marginalizing over **w** của f(t,**w**|x,**x,t**) ta sẽ có
> f(t|x, **x**,**t**) không phụ thuộc **w**, tức là predictive distribution:
>
> f(t|x,**x**,**t**) = ∫f(t,**w**|x,**x**,**t**)d**w** = ∫f(t|x, **w**) π(**w**|**x**,**t**) d**w** với π(**w**|**x**,**t**) là posterior
> của **w**. 

<br>

