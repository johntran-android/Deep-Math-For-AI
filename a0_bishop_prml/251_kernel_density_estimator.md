# 2.5.1 Kernel density estimator

📊 **Progress:** `2` Notes | `2` Screenshots

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

