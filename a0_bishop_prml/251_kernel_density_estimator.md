# 2.5.1 Kernel density estimator

📊 **Progress:** `4` Notes | `5` Screenshots

---
<a id="node-306"></a>

<p align="center"><kbd><img src="assets/ae1fb7bf84ea9decd6648ac375fe7dfda60c9d74.png" width="100%"></kbd></p>

> [!NOTE]
> Ta qua phương pháp đầu tiên - Kernel density estimator.
>
> Đầu tiên gs cho rằng ta có một distribution có pdf f(**x**) nào đó có dimension. (Ý này nói theo
> ngôn ngữ thống kê chỉ là: xét một random variable vector **X** = (X1,...XD) có pdf là f(**x**). Và ta
> lấy mẫu (sampling) từ nó, với mong muốn là estimate hàm pdf này.
>
> Rồi, đại khái gọi **x** là một điểm nào đó, và gọi vùng nhỏ lân cận **x** là **R**. Còn nhớ theo định
> nghĩa của hàm pdf đã học trong Casella hay Stat110, pdf của biến ngẫu nhiên liên tục X, kí hiệu
> fX(x) là hàm được định nghĩa là P(X ∈ A) = ∫A fX(x)dx. Nên tương tự, với f(**x**) là pdf của **X**,
> thì P(**X** ∈ R) = ∫R f(**x**) d**x**. Và ở đây gs đặt gía trị này là P. (tóm lại 2.242 chỉ là từ định
> nghĩa của hàm pdf, không có gì cao siêu)
>
> Tiếp theo, gs cho biết ta thu thập được N giá trị quan sát từ phân phối f(**x**) này.
>
> Chỗ này, nếu nói theo ngôn ngữ Casella, thì ta có một **random sample** size N, iid **X1**, **X2**,.
> ..**XN** đều ~ f(**x**) (dĩ nhiên phải hiểu, **X1**, viết đậm, là random variable vector trong sample,
> bản thân nó là vector có D phần tử **X1** = (X11, X12,..X1D).
>
> Ôn nhanh định nghĩa của random sample size n: Đó là ta có một đại lượng có tính không chắc
> chắn nào đó, và ta sẽ tiến hành quan sát giá trị của nó n lần, sao cho mỗi lần là độc lập nhau. Vì
> mỗi lần quan sát, do tính không chắc chắn, nên giá trị quan sát được sẽ có thể có nhiều possible
> value, do đó giá trị quan sát sẽ được thể hiện bởi một random variable: X1, ...Xn. Vì thí nghiệm
> được tiến hành độc lập, nên các random variable này đều độc lập lẫn nhau (mutually
> independent), và vì cùng quan sát một đại lượng có tính không chắc, nên các random variable này
> đều có chung một population distribution (indentically distributed), viết tắt lạ iid.
>
> Thế thì, **X1**, **X2**,... **XN**,cần hiểu rằng, là các random variable vector thuộc distribution
> f(**x**), nên:
>
> P(**X1** ∈ R) = ∫R f(**x**) d**x**
>
> và đối với **X2**,..,**XN** cũng vậy
>
> Nên P(**X1** ∈ R) = P(**X2** ∈ R) = ..∫R f(**x**) d**x**, và giá trị này ta đã đặt là **P** ở trên.
>
> Thế thì tiếp theo, ta sẽ gọi K là số data point rơi vào vùng R. Thì vì **X1**,...**XN** như đã nói, là
> các random variable, nên chúng có nhiều possible value dẫn đến việc giá trị của chúng có thuộc
> vùng R không và dẫn đến giá trị của K sẽ có nhiều khả năng, do đó, **K là một random variable**,
> và người ta quan tâm đến distribution của K.
>
> Thế thì, các possible value của K, dễ thấy sẽ từ 0,1,2... đến N. K = 0 khi mọi random variable **Xi**
> đều không ∈ R và K = N khi mọi **X1**, ...**XN** đều ∈ R.
>
> Như vậy, nhớ lại Stat110, ta nhớ story của binomial(n,p), là ta có n Bern(p) trial iid, và ta quan tâm
> đến tổng số trial success. Khi đó, đại lượng này sẽ là một random variable thuộc phân phối
> binomial(n,p). Vậy thì ở đây, ta cũng có N Bern trial. Mỗi trial là check xem Xi có thuộc R hay
> không. Và vì **Xi** đều độc lập, nên ta cũng có các Bern trial độc lập. Hơn nữa, xác suất thành
> công của trial này đều là P, nên đây thỏa mãn story trên: Đó là ta có N iid Bern(P), nên tổng số
> data point rơi vào vùng R, tức là random variable K, sẽ là một random variable ~ Binomial(N, P).
>
> Và pmf của binomial thì biết rồi:
>
> P(K = k) = (N choose k) P^k (1-P)^(N - k)
>
> hay viết theo trong sách
>
> Bin(k|N,P) = (N choose k) P^k (1 - p)(N - k)
>
> Như vậy chỗ này có thể thấy mr Bishop viết sai công thức, phải là N - k chứ không thể nào là 1 -
> p)^(1 - k) được.
>
> Và nhận xét thêm việc ông tương chữ K (viết hoa) vô làm ta dễ rối. vì theo nguyên tắc K là
> random variable, thì giá trị của nó là k (viết thường), ông ghi luôn K viết hoa trong công thức khiến
> khó hiểu.

<br>

<a id="node-307"></a>

<p align="center"><kbd><img src="assets/4132ef4d08094a3c8dc3961c795b0b1583af837b.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi, thế thì với X ~ binomial(n, p) ta đã chứng minh nhiều lần (trong Casella và
> Stat110): EX = np, Var(X) = np(1-p)
>
> Vậy ở đây, K ~ binomial(N, P) ⇨ E[K] = NP ⇨ E[K] / N = P. Vì 1/N chỉ là constant, ta
> dùng tính chất linearity của kì vọng (E[cX] = cEX) đưa nó vào trong: E[K] / N = P ⇔
> **E[K/N] = P**
>
> Tương tự, Var[K] = NP(1-P)
>
> Dùng tính chất của Variance: Var(cX) = c^2 Var(X)
>
> ⇨ Var[K] = Var[NK/N] = N^2 Var[K/N]
>
> ⇨ Var[K] = NP(1-P) ⇔ N^2 Var[K/N] = NP(1-P)
>
> ⇔ **Var[K/N] = P(1-P)/N**
>
> Khi N lớn thì Var[K/N] = P(1-P)/N sẽ tiến về 0.
>
> Vậy ta hiểu thế này: K là random variabel ~ binomial(N, P) như đã nói. Thì K/N là kết
> quả của việc áp một hàm số (g(u) = u/N) lên K, nên nó cũng là random variable,
> distribution của nó là gì ta không cần biết, nhưng biết mean của distribution này là
> E[K/N] = P, và variance là P(1-P)/N, để rồi khi N → inf thì variance → 0. Thế thì ý
> nghĩa của variance ta nhớ, là đại lượng đo tính chất phân tán (dispersion) của một
> distribution, nên nếu variance → 0, thì cũng đồng nghĩa là distribution sẽ ít phân tán
> và tập trung quanh mean P, đây là ý gs nói nó "will be sharply peaked around mean"
>
> Thế thì như vậy K/N, là random variable. Theo lí mà nói, không thể có giá trị nào cụ
> thể, mà nó có nhiều possible value. Nếu tính trung bình, qua các possible value đó,
> với trọng số là pmf thì ta có kì vọng E[K/N]. Nhưng ở đây khi N lớn, ta đã nói, xác
> suất sẽ tập trung hết quanh mean P, tức là coi như K/N = P với xác suất P(K/N = P)
> = 1. Đây là ý nghĩa của việc ghi: K/N ≈ P hay K ≈ NP.
>
> Một điểm nữa, hãy để ý, nếu ta đặt Ij = là indicator random variable gắn với event
> **Xj** ∈ R, j = 1,...N. Khi đó bối cảnh bài toán ta sẽ random sample I1, I2, ...IN iid ~
> Bern(P) Và K/N = (∑j Ij) / N chính là sample mean. Khi đó, nhớ lại Weak Law of
> Large Number theorem, nói rằng: với một số điều kiện, thì sample mean sẽ hội tụ
> phân phối về population mean. Vậy nên ở đây K/N = (∑j Ij) / N sẽ hội tụ về E[Ij] = P:
> K/N → P. Viết ở dạng toán học: lim N→∞ K/N = P, hay có thể ghi là tại limit khi N lớn,
> K/N ≈ P ⇔ K ≈ PN

<br>

<a id="node-308"></a>

<p align="center"><kbd><img src="assets/b46da4d040e43fdf4f396289351035c2b4b2e52d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/5409c075ea8a0a941fc9ca1439b6b0619a77b31f.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì tiếp theo, đại khái là nếu như ta giả định rằng vùng R nhỏ đến nỗi trong phạm vi đó f(**x**) có thể coi
> như là constant, thì khi đó P(**X** ∈ R) = ∫_R f(**x**)d**x** = f(**x**) ∫_R d**x** = f(**x**) × thể tích của vùng R =
> f(**x**) V.
>
> Kết hợp P ≈ f(**x**)V ⇔ f(**x**) = P/V và K ≈ PN ta có f(x) ≈ K/NV.
>
> Ông cũng lưu ý rằng kết quả này dựa trên hai assumption mâu thuẫn nhau:
>
> Giả định thứ nhất là cái vừa nói: là vùng R phải đủ nhỏ để pdf trong vùng đó là hằng số.
>
> Nhưng nhớ lại chút xíu bối cảnh bài toán: Là cho random sample size N tuân theo một distribution f(**x**) nào
> đó, và xét vùng R, với xác suất **X** ∈ R đặt là P, khi đó gọi K = Σj Ij là số data point ∈ R, Ij là indicator random
> variable ứng với event **X**j ∈ R, là một Bernouilly(P) random variable, thì story của K sẽ như số trial success
> trong N iid Bernouilly(P) trial, nên K sẽ ~ Binomial(N, P), và (Σj Ij)/N chính là sample mean I_bar_n (sample
> mean từ sample size N), theo luật số lớn yếu, chuỗi I_bar_n sẽ cMộtonverger về E[Ij] = P.
>
> Vậy thì nó liên quan gì đến việc vùng R phải đủ lớn?
>
> Hiểu thế này:
>
> Một ý cốt lõi để WLLN work đó là Var(Xi) phải < ∞, thì Xbar_n mới hội tụ xác suất về E[Xi].
>
> Vậy thì ở đây, bức tranh lớn mà gs đang dẫn dắt ta là thực hiện cái gọi là ước lượng hàm density (density
> estimation). Nó khác với bài toán parameter inference, trong đó ta đã biết hay giả định biết rằng hàm pdf của
> distribution có dạng gì (f(x|θ), chỉ là không biết giá trị cụ thể của tham số θ. Còn ở đây, cái mà ta làm, thì lại
> chả cần quan tâm hoặc không cần biết hình dạng của nó có dạng gì, mà chỉ là ta đi xây một cái hàm số f(x)
> bằng cách kiểu như vẽ ra tại x bằng các giá trị khác nhau thì f(x) sẽ bằng bao nhiêu (trong cách tiếp cận này,
> ta không nói gì đến tham số, vì ta không cần tham số, ta chỉ cần biết một mapping x f(x) mà thôi)
>
> Thế thì để làm cái việc đó, về cơ bản là như đã nói, ta sẽ ước lượng hàm f(**x**) tại một điểm **x** bất kì. Và ý
> tưởng chủ đạo cho việc này, đó là:
>
> i) Xét một vùng R quanh lân cận điểm **x**.
>
> ii) Cho rằng R đủ nhỏ để trong đó f(**x**) là hằng số, thì P(**X** ∈ R), (đặt là P) = f(**x**) V.
>
> Rồi, lại dựa trên việc ta có N sample (observation) **X**1,...**X**N, thì với việc chúng iid nên khi quan tâm đến
> việc chúng có thuộc R hay không thì ta sẽ có bối cảnh là chuỗi N iid Bernouilly(P) trial nên K = Σj I_(**X**j ∈ R)
> sẽ là một rv ~ Binomial(N, P).
>
> Đồng thời, nếu ta xét [Σj I_(**X**j ∈ R)] / N, thì đây là sample mean size N của random sample size N Bern(P)
> I_(X1 ∈ R), I_(X2 ∈ R),..... viết gọn là I1, I2,...IN. Thì theo WLLN, nếu ta đảm bảo Var[Ij] < ∞, thì [Σj I_(**X**j ∈
> R)] / N sẽ hội tụ xác suất về E[Ij] = P.
>
> Và nếu vậy, thì ta sẽ có thể cho [Σj I_(**X**j ∈ R)] / N xấp xỉ cho P, tương đương K/N xấp xỉ f(**x**) V, cũng là
> f(**x**) xấp xỉ K/NV. Và như vậy ta có được estimate của f(**x**) tại **x**. Làm tương tự với mọi **x** khác trên
> range **X**, thì ta sẽ có được estimatio của hàm density f(**x**).
>
> Vấn đề là có thể thấy ta đã dùng hai giả định: Một là f(**x**) phải là constant trong R, nên R phải đủ nhỏ. Và hai
> là, ta đã viện dẫn WLLN, để cho phép [Σj I_(**X**j ∈ R)] / N xấp xỉ cho P.
>
> Nhưng để viện dẫn WLLN, thì phải thỏa điều kiện của WLLN: Var[Ij] < ∞.
>
> Để có thể dễ hiểu hơn ta sẽ nhìn theo góc độ khác: đó là xét các random variable Zj = Ij/V. Vì Ij iid thì Zj cũng
> iid.
>
> E[Zj] = E[Ij/V] = E[Ij]/V = P/V
>
> Var[Zj] = Var[Ij/V] = Var[Ij]/V^2
>
> Và sample mean size N là (Σj Zj)/N,
>
> nếu Var[Zj] < ∞ thì chuỗi sample mean, (Σj Zj)/N, theo WLLN cũng sẽ converge về E[Zj] = P/V, để rồi tại limit ta
> có:
>
> (Σj Zj)/N = P/V ⇔ Σj Zj = NP/V
>
> ⇔ Σj (Ij/V) = NP/V ⇔ Σj (Ij) = NP
>
> ⇔ P = (Σj Ij) / N
>
> ⇔ f(**x**) = (Σj Ij) / NV = K / NV
>
> Hay xét với N lớn thì ta có xấp xỉ: f(**x**) ≈ K / NV như kết quả trên.
>
> Vấn đề là, với việc xét WLLN theo sample mean của Z ta mới thấy khi V quá nhỏ, V → 0 thì Var[Zj] =
> Var[Ij]/V^2 sẽ → ∞. Để rồi giúp ta chỉ ra rằng, muốn áp dụng được WLLN, để mà có kết quả xấp xỉ trên thì V
> không thể quá nhỏ.
>
> Đó là lí do ở đây ta có hai assumption mâu thuẫn: V phải nhỏ để f(**x**) là constant trong R, nhưng phải lớn để
> có thể áp dụng WLLN để có ước lượng f(**x**) ≈ K / NV.

<br>

<a id="node-309"></a>

<p align="center"><kbd><img src="assets/dab624e15a7fd33cf60d5443b785d612f7ef67be.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì ở đây nói ta có thể khai thác kết quả f(**x**) ≈ K / NV theo hai cách:
>
> Giữ K cố định và dùng data để xác định V, cách này sẽ dẫn đến phương pháo
> K-nearest neigbor
>
> Và Giữ V cố định và tính K từ data sẽ dẫn ta đến kernel approach.
>
> Và người ta đã chứng minh là khi N → inf và cho V nhỏ một cách phù hợp
> theo N, Và K → N thì cả hai kết quả từ hai cách làm để sẽ hội tụ về distribution
> thật.

<br>

