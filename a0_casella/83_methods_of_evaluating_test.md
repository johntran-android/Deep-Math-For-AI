# 8.3 Methods Of Evaluating Test

📊 **Progress:** `15` Notes | `25` Screenshots

---
<a id="node-692"></a>

<p align="center"><kbd><img src="assets/b16b261077605b943cf8f3753c96824e58fc2e03.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái mình hiểu thế này: 8.2 chỉ mới nói về cách tìm / xây dựng cái
> decision rule, để quyết định reject hay ko reject H0. Mà công thức chung là
> ta sẽ dựa vào việc tính toán một statistic gọi là test statistic T(**x**), để rồi
> đặt ra rule để mà reject H0 hay không dựa vào T(**x**) này. Cụ thể là với
> LRT, ta sẽ tính LRT statistic λ(**X**), và đặt rule: reject H0 nếu λ(**X**) ≤ c.
> Hoặc với Bayes test, ta sẽ tính test  statistic là P(θ ∈ Θ0|**X**), để rồi có thể
> đặt rule là: reject H0 khi P(θ ∈ Θ0|**X**) ≤ c.
>
> Như vậy ta thấy, đầu tiên ta phải xây dựng test statistic. Nhưng sau đó phải
> đặt ra cái rule, để ra quyết định dựa trên giá trị của test statistic đó, mà trong
> hai case trên, chính là quyết định c là bao nhiêu.
>
> Thế thì, đại ý là ta có thể mắc sai lầm khi làm việc này. Và do đó, ta cần
> công cụ để mà đánh giá chất lượng của hypothesis test procedure.
>
> Và thường thường, người ta sẽ dùng cách tiếp cận là tính xác suất mắc sai
> lầm, và dùng nó để so sánh các hypothesis test và trong một số trường hợp
> có thể còn giúp chọn ra cái tốt nhất nữa.

<br>

<a id="node-693"></a>

<p align="center"><kbd><img src="assets/e6597f427034d1845d0cd17f5e79c0424daf1962.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là một hypothesis test có thể mắc một trong hai loại sai
> sót: Type I Error:  là khi θ ∈ Θ0 nhưng test lại reject H0. Và Type I
> error là khi θ ∈ Θ0c nhưng test là accept H0.
>
> Thế thì khi θ ∈ Θ0, mà test cho kết luận reject H0 (Type I error), 
> thì tức là sao?
>
> → Thì có nghĩa observed value **X,** **nằm trong rejection region** của
> test.
>
> Như vậy có thể hiểu, việc (event) "Test mắc Type I error" chính
> là = (event) **X** ∈ Rejection region R.
>
> ⇨ P(Type I error) = P_θ(**X** ∈ R)
>
> Ngược lại.
>
> Khi θ ∈ Θ0c, mà test cho kết luận accept H0, (Type II error), thì
> có nghĩa là, **x không nằm trong rejection region, cũng chính
> là nằm trong Rc**(complement của R)****⇨ P(Type II error) = P_θ(**x** ∈ Rc) = 1 - P_θ(**x** ∈ R)
>
> ⇨ P_θ(**x** ∈ R) = 1 - P(Type II error)
>
> Kết luận:
>
> P_θ(**x** ∈ R) = P(Type I error) khi θ ∈ Θ0
>
> P_θ(**x** ∈ R) = 1 - P(Type II error) khi θ ∈ Θ0c

<br>

<a id="node-694"></a>

<p align="center"><kbd><img src="assets/a9c0d8648a9c79ca1d99156f91fb0283e2684eab.png" width="100%"></kbd></p>

> [!NOTE]
> Từ đó ta có định nghĩa của POWER FUNCTION CỦA MỘT HYPOTHESIS
> TEST với rejection region R:
>
> Nó được định nghĩa là một function theo θ: β(θ) = P_θ(**X** ∈ R).
>
> Vì sao nó là function theo θ? Đơn giản là vì đây là xác suất của event liên
> quan đến **X**, mà **X** là random sample size n các rv X1,..Xn ~ f(xi|θ) nên dĩ
> nhiên đây phải là function theo θ.
>
> Thế thì như đã nói ở note trước: P_θ(**X** ∈ R) = Xác suất xảy ra Type I Error
> khi θ ∈ Θ0 và P_θ(**X** ∈ R) = 1 - Xác suất xảy ra Type II Error khi θ ∈ Θ0c
> nên ta muốn khi θ ∈ Θ0 thì β(θ) = 0 và khi θ ∈ Θ0c thì β(θ) = 1.
>
> Điều này cũng có nghĩa là, nếu ta có hàm β sao cho:
>
> β(θ) = 0 ∀ θ ∈ Θ0 và β(θ) = 1 ∀ θ ∈ Θ0c. Thì đó là hàm β lí tưởng.

<br>

<a id="node-695"></a>

<p align="center"><kbd><img src="assets/f6880c05ac0b7488091e9c5bf4fb7dcffad33d44.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f6880c05ac0b7488091e9c5bf4fb7dcffad33d44.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/75e7d1b12aa3f6b58ba22747f3a54cd4d1ff03fe.png" width="100%"></kbd></p>

> [!NOTE]
> Qua ví dụ này, cho X ~ binomial (5, θ). Và xem xét hypothesis test giữa
> H0: θ ≤ 1/2 vs H1: θ > 1/2. Ở đây mình hiểu ta đang có một random sample
> size 1 ~ binomial(5, θ) (để có thể không khó hiểu khi dùng X thay vì **X**).
>
> Thế thì, tác giả cho là ta sẽ xem xét phép test đầu tiên: reject H0 khi và chỉ
> khi mọi "success" đều observed. Tức là sao? 
>
> Ta biết story của một random variable ~ binomial(n, p) là: tổng của các trial
> success trong n iid Bern(p) trials. Nên, event mọi success chính là X = n.
> Tức là ở đây test procedure là: reject H0 khi X = 5.
>
> Ôn lại một chút: Bản chất của bài toán hypothesis testing, là ta muốn xây
> dựng một rule, một decision function, giúp đưa ra quyết định reject hoặc 
> accept H0, dựa trên observed value của random sample. Để xây dựng rule,
> dựa trên observed value, dĩ nhiên ta sẽ tính toán một function nào đó của
> **X**, để rồi ra quyết định dựa trên đó, thì đó chính là testing statistic.Tuy nhiên
> sau đó ta phải đặt ra rule để chọn H0 hay H1 dựa trên test statistic. Thế thì
> ở đây, rule của phép thử đầu tiên: reject H0 khi X = 5. Thì test statistic chính
> là X (có thể coi như là identity function của X, T(X) = X), và cái rule chính là
> reject H0 khi T(X) = 5.
>
> Thế thì, dĩ nhiên dễ hiểu rằng, khi đặt ra rule, ta có thể có nhiều cách. Và
> mỗi cách sẽ có thể tốt hay tệ. Do đó để đánh giá, người ta sẽ tính toán xác 
> suất mà test rule mắc một trong hai sai lầm: Type I error và Type II error.
>
> Type I error là khi θ ∈ Θ0 nhưng test kết luận reject H0. Mà việc test reject
> H0 sẽ xảy ra khi random sample X có giá trị rơi vào rejection region, vì theo
> định nghĩa rejection region là tập R = {x: T(x) khiến H0 bị reject}. Vậy nên
> Type I error xảy ra khi θ ∈ Θ0 và x ∈ R. Nên xác suất Type I error xảy ra chính
> là P(x ∈ R), chú ý, ta sẽ không nói là P(θ ∈ Θ0, x ∈ R) vì đây không phải là 
> Bayesian approach, θ không phải là random variable, nên việc không biết θ 
> khiến không ích gì khi thể hiện như vậy. Thay vào đó, ta sẽ chỉ thể hiện là
> P(Type I error) = P_θ(X ∈ R)
>
> Type II error xảy ra khi θ ∈ Θ0c và test kết luận accept H0, việc này đồng
> nghĩa x không ∈ R. ⇨ P(Type II error) = P_θ(x not ∈ R) = 1 - P_θ(x ∈ R) 
>
> Vậy:
>
> P_θ(X ∈ R) = P(Type I error) khi θ ∈ Θ0
>
> P_θ(X ∈ R) = 1 - P(Type II error) khi θ ∈ Θ0c
>
> Từ đó ta định nghĩa ra β function: β(θ) = P_θ(x ∈ R) và muốn nó rất nhỏ khi
> θ ∈ Θ0 và rất lớn (≈ 1) khi θ ∈ Θ0c hay nói cách khác, ta muốn β(θ) ≈ 0 với
> mọi θ ∈ Θ0 và β(θ) ≈ 1 với mọi Θ0c
>
> Quay lại đây. Beta function là gì? Theo định nghĩa vừa nói, nó = P_θ(x ∈ R)
> và R của test rule này (reject H0 ⇔ X = 5), là {x: x = 5} nên:
>
> β(θ) = P_θ(X ∈ R) = P_θ(X = 5), áp dụng pmf của binomial: 
>
> P(X=k) = (n choose k)p^n(1-p)^(1-k), ta có
>
> β(θ) = (5 choose 5) θ^5(1-θ)^(5-5) = 1*θ^5*1 = θ^5.
>
> Và với θ ∈ [0,1] thì ta có đồ thị của hàm β(θ), (β1(θ)). 
>
> Nhận xét thấy khi θ tăng từ 0 đến 0.6, 0.7 thì β rất nhỏ, sau đó tăng lên nhanh
> đến 1. Có nghĩa là khi θ ≤ 1/2 (nhớ để ý Θ0 ở đây chính là [0, 1/2]) thì β(θ) rất 
> nhỏ → xác suất Type I error đều nhỏ, là điều tốt. Nhưng khi θ > 1/2 trong phần
> lớn θ từ 1/2 đến 1 thì β(θ) đều < 1 → Type II error lớn, ko tốt.
>
> Ta mới so sánh với một test rule khác: (nhắc lại, cùng test statistic, nhưng rule
> có thể có nhiều): reject H0 khi X = 5 hoặc 4 hoặc 3.
>
> β(θ) = P_θ(X ∈ R) = P_θ(X = 5 U X = 4 U X = 3), theo axiom 2, đây là ∪
> các disjoint event, = tổng xác suất từng event:
>
> = P_θ(X = 5) + P_θ(X = 4) + P_θ(X = 3)
>
> = θ^5 + (5 choose 4) θ^4(1-θ)^(5-4) + (5 choose 3) θ^3(1-θ)^(5-3)
>
> = θ^5 + (5 choose 4) θ^4(1-θ) + (5 choose 3) θ^3(1-θ)^2
>
> Để rồi vẽ đồ thị cái hàm β này ra (β2) ta thấy:
>
> Đại khái là trong θ ∈ [0, 1/2] thì β(θ) không nhỏ trong phần lớn quãng đường
> so với β1, cho thấy Type I error của nó tệ hơn, nhưng bù lại, nó gần 1 hơn
> so với β1 trong đoạn θ ∈ [1/2, 1], cho thấy type II error tốt hơn (ý là nhỏ hơn)
>
> Và một kết luận quan trọng của tác giả: **TA PHẢI QUYẾT ĐỊNH CẤU TRÚC
> ERROR NÀO ĐỂ DÙNG**. HIểu đại khái là, tùy vào bài toán thực tế cụ thể,
> thì ta sẽ xem trong đó, ta ưu tiên loại error nào hơn, từ đó chọn test rule nào.
> Ví dụ, nếu trong thực tế, việc reject nhầm H0 gây hậu quả lớn hơn, tức Type
> I error cần được ưu tiên giảm thiểu hơn. Ta có thể dùng rule 1.

<br>

<a id="node-696"></a>

<p align="center"><kbd><img src="assets/7605deee8a3b4add023c59feee5a72a24fd822fc.png" width="100%"></kbd></p>

🔗 **Related:** [8.3 METHODS OF EVALUATING TEST](83_methods_of_evaluating_test.md#node-699)

> [!NOTE]
> Cho X1,...Xn random sample ~ n(θ, σ^2), với σ^2 đã biết. Xét một LRT testing 
> giữa H0: θ ≤ θ0 và H1: θ > θ0, với rule là: reject H0 khi (Xbar - θ0) / (σ/√n) > c.
> Với c là số dương bất kì.
>
> Làm rõ ý này:
>
> Nhớ lại thế nào là LRT (Likelihood Ratio Test), nó là phương pháp tạo test rule
> có dạng reject H0 khi λ(**X**) ≤ c, với c ∈ [0,1] và 
>
> λ(**X**) = sup_Θ0 L(θ|**x**) / sup_Θ L(θ|**X**)
>
> Mẫu số là likelihood function tại mle của θ, thử làm lại:
>
> Likelihood function: L(θ|**x**) = f(**x**|θ) = f(x|(θ,σ^2))
>
> = Πi f(xi|(θ,σ^2)) = Πi (1/√2πσ^2) exp[-(xi-θ)^2/2σ^2] 
>
> Maximize L(θ|**x**) sẽ equivalent maximize log L(θ|**x**):
>
> = log [(1/√2πσ^2)^n exp Σi [-(xi-θ)^2/2σ^2]] 
>
> = log [(1/√2πσ^2)^n] + log exp Σi [-(xi-θ)^2/2σ^2]
>
> = n log (1/√2πσ^2) + Σi [-(xi-θ)^2/2σ^2]
>
> ⇔ maximize Σi [-(xi-θ)^2] / 2σ^2
>
> ⇔ maximize - Σi(xi-θ)^2
>
> ⇔ minimize g(θ) = Σi(xi-θ)^2 = 
>
> Điều kiện cần bậc 1: g'(θ) = 0 ⇔ d/dθ [Σi(xi-θ)^2] = 0 ⇔ Σi d/dθ [(xi-θ)^2] = 0
>
> ⇔ Σi d/d(xi-θ) [(xi-θ)^2] . d/dθ (xi-θ) = 0
>
> ⇔ Σi 2(xi-θ) . (-1) = 0
>
> ⇔ - 2 Σi (xi-θ) = 0
>
> ⇔ Σixi - nθ = 0
>
> ⇔ θ = Σixi / n = xbar
>
> g''(θ) = d/dθ [-2Σi(xi-θ)] = -2 Σi d/dθ(xi-θ) = -2 Σi (-1) = 2n > 0 
>
> ⇨ xbar minimizer của g ⇨ MLE của θ là Xbar, 
>
> và L(xbar|**x**) = 
>
> = (1/√2πσ^2)^n exp Σi [-(xi-xbar)^2/2σ^2] 
>
> = (1/√2πσ^2)^n exp (1/2σ^2) Σi [-(xi-xbar)^2] 
>
> Cũng giải bài toán đó, nhưng restrict trong θ ∈ Θ0, tức θ ≤ θ0
>
> Nếu xbar ≤ θ0 thì tử số chính là L(xbar|**x**)
>
> nếu θ0 < xbar thì tử số chính là L(θ0|**x**), lí do là vì hàm L(θ|**x**) chỉ có một
> optimal là θ^mle = xbar, nên nếu θ0 < xbar thì khi đồng nghĩa trong (-inf, θ0)
> hàm monotone increasing → đạt max tại θ0.
>
> Khi đó λ(**x**) = L(θ0|**x**) / L(xbar|**x**) 
>
> = (1/√2πσ^2)^n exp (1/2σ^2) Σi [-(xi-θ0)^2] / 1/√2πσ^2)^n exp (1/2σ^2) Σi [-(xi-xbar)^2] 
>
> = exp (1/2σ^2) Σi [-(xi-θ0)^2] / exp (1/2σ^2) Σi [-(xi-xbar)^2] 
>
> = exp (1/2σ^2) Σi [-(xi-θ0)^2] - (1/2σ^2) Σi [-(xi-xbar)^2] 
>
> = exp (1/2σ^2) Σi {[-(xi-θ0)^2] - [-(xi-xbar)^2]}
>
> = exp (1/2σ^2) Σi [-(xi-θ0)^2 +(xi-xbar)^2] 
>
> = exp (1/2σ^2) Σi [-(xi-xbar-θ0+xbar)^2 +(xi-xbar)^2] 
>
> = exp (1/2σ^2) Σi [-[(xi-xbar)+(xbar-θ0)]^2 +(xi-xbar)^2] 
>
> = exp (1/2σ^2) Σi [-[(xi-xbar)^2+2(xi-xbar)(xbar-θ0)+(xbar-θ0)^2] +(xi-xbar)^2] 
>
> = exp (1/2σ^2) Σi [-(xi-xbar)^2-2(xi-xbar)(xbar-θ0)-(xbar-θ0)^2+(xi-xbar)^2] 
>
> = exp (1/2σ^2) Σi [-2(xi-xbar)(xbar-θ0)-(xbar-θ0)^2]
>
> = exp (1/2σ^2) [-2(xbar-θ0)Σi(xi-xbar)-Σi(xbar-θ0)^2] 
>
> = exp (1/2σ^2) [-2(xbar-θ0)(nxbar-nxbar)-n(xbar-θ0)^2] 
>
> = exp (1/2σ^2) [-n(xbar-θ0)^2]
>
> = exp [-n(xbar-θ0)^2/2σ^2] 
>
> Tóm lại:
>
> λ(**x**) = 1 khi xbar ≤ θ0
>
> λ(**x**) = exp [-n(xbar-θ0)^2/2σ^2] khi khi θ0 < xbar
>
> Vậy thì, test rule trở thành: 
>
> Khi xbar ≤ θ0, luôn accept H0 do λ(x) = 1 > c ∀c ∈ [0,1]
>
> Khi θ0 < xbar, reject H0 khi exp [-n(xbar-θ0)^2/2σ^2] ≤ c
>
> ⇔ [-n(xbar-θ0)^2/2σ^2] ≤ log c
>
> ⇔ -(xbar-θ0)^2/(2σ^2/n) ≤ log c
>
> ⇔ -(xbar-θ0)^2/2(σ/√n)^2 ≤ log c
>
> ⇔ (xbar-θ0)^2/(σ/√n)^2 > -2log c
>
> ⇔ [(xbar-θ0)/(σ/√n)]^2 > -2log c (a)
>
> vì đang xét θ0 < xbar ⇨ (xbar-θ0)/(σ/√n) dương 
>
> Với c ∈ [0,1] ⇨ log c < 0 → -2log c dương
>
> nên cho phép (a) 
>
> ⇔ (xbar-θ0)/(σ/√n) > -√2log(c)
>
> Đây chính là (xbar-θ0)/(σ/√n) > c'
>
> Như vậy LRT test của bài toán này chính là reject H0 khi (Xbar-θ0)/(σ/√n) > c' như trong
> sách. (chú ý, c trong sách, là c' của mình, nên dĩ nhiên nó là số dương bất kì, không phải 
> là ∈ [0,1])

<br>

<a id="node-697"></a>

<p align="center"><kbd><img src="assets/e0ddc27471a0924a295adf550050112fbf851217.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b94d79814aa6b5763b2019218e6c3a470596f97a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e0ddc27471a0924a295adf550050112fbf851217.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b94d79814aa6b5763b2019218e6c3a470596f97a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/5d498b822e1260a4754c3d29312903992e1b7fd7.png" width="100%"></kbd></p>

🔗 **Related:** [3.5 LOCATION AND SCALE FAMILIES](35_location_and_scale_families.md#node-202)

🔗 **Related:** [5.2 Σ OF RANDOM VARIABLES FROM A RANDOM SAMPLE](52_σ_of_random_variables_from_a_random_sample.md#node-348)

🔗 **Related:** [3.5 LOCATION AND SCALE FAMILIES](35_location_and_scale_families.md#node-201)

> [!NOTE]
> Thế thì, power function β(θ) sẽ là gì?
>
> Theo định nghĩa, β(θ) = P_θ(**X** ∈ R), và Rejection region của test rule vừa
> tự derive lại là R = {**x**: H0 bị reject} = {**x**: (xbar-θ0)/(σ/√n) > c} (chuyển
> thành c cho giống sách, nhưng hiểu nó là c' trong phần derive của mình)
>
> ⇨ β(θ) = P_θ(**X** ∈ R) = P_θ((Xbar-θ0)/(σ/√n) > c)
>
> (Xbar-θ0)/(σ/√n) > c
>
> ⇔ Xbar/(σ/√n) > c + θ0/(σ/√n)
>
> ⇔ (Xbar-θ)/(σ/√n) > c + (θ0-θ)/(σ/√n)
>
> Đến đây nhớ lại kiến thức về location scale family. Được định nghĩa là,  Cho
> f(x) là pdf bất kì thì họ các pdf (1/σ)f((x-μ)/σ) được gọi là location-scale family
> với standard pdf f(x).
>
> Lại có theorem location scale (3.5.6) nói rằng: cho f là một pdf thì X ~ (1/σ)
> f((x-μ)/σ)  ⇔ tồn tại Z có pdf f(z) và X = σZ + μ (μ số thực bất kì và σ dương).
>
> Vậy theo theorem này:
>
> Nếu X là member có location μ và σ thì (X - μ)/σ là standard member
> (location 0, scale 1)
>
> Mà Xbar ta đã biết trong các phần trước (xem link) Xbar ~ n(θ, σ/√n)
>
> Do đó (Xbar - θ)/(σ/√n) (đặt là Z), chính là standard member của family, tức
> location 0, scale 1. Mà với normal, thì location chính là mean và scale param
> chính là standard deviation.
>
> Do đó Z =  (Xbar - θ)/(σ/√n) ~ n(0,1)
>
> ====
>
> Thử chứng minh lại theorem location scale (3.5.6):
>
> Chứng minh điều kiện cần: Khi X ~ (1/σ) f((x-μ)/σ) thì tồn tại Z có quan hệ
> với X bởi X = σZ + μ, và có pdf f(z)
>
> Có nghĩa là ta chỉ cần chứng minh Z = (X - μ)/σ là rv ~ f(z).
>
> Áp dụng transformation theorem:
>
> Cho Y = g(X) ta có theorem và g là hàm mapping 1-1: y = g(x) ⇔ ginv(y) = x
>
> fY(y) = fX(x) |dx/dy|
>
> Áp dụng vào đây: Với x = g(z) = σz + μ ⇨ z = ginv(x) = (x - μ)/σ
>
> fZ(z) = fX(x) |dx/dz|
>
> Jacobian: dx/dz: x = σz + μ ⇨ dx/dz = σ
>
> Trị tuyêt đối det của dx/dz = σ
>
> fZ(z) = fX(σz + μ) σ
>
> = [(1/σ) f((x-μ)/σ) |x=σz + μ] σ
>
> = [(1/σ) f((σz + μ-μ)/σ)] σ
>
> = f((σz + μ-μ)/σ)
>
> = f(σz/σ)
>
> = f(z) Chứng minh xong.
>
> Chứng minh điều kiện đủ: Z = (X - μ) / σ ~ f(z) thì X ~ fX(x) = (1/σ) f((x-μ)/σ)
>
> Lại áp dụng transformation:
>
> fX(x) = fZ(z) |dz/dx|
>
> = f(z) |1/σ|
>
> = f((x - μ)/σ) / σ
>
> Chứng minh xong.
>
> ====
>
> Vậy β(θ) = P_θ(Z > c + (θ0-θ)/(σ/√n))
>
> = 1 - P_θ(Z ≤ c + (θ0-θ)/(σ/√n))
>
> Và P_θ(Z ≤ a), chính là cdf của A, tại a, FZ(a) và với Z là standard normal, 
>
> ta có kí hiệu riêng cho cdf là Φ
>
> = 1 - Φ(c + (θ0-θ)/(σ/√n))
>
> Với θ chạy từ -inf tới inf thì c + (θ0-θ)/(σ/√n) sẽ chạy từ +inf → -inf
>
> ⇨ Φ(c + (θ0-θ)/(σ/√n)) chạy từ 1 → 0
>
> ⇨ - Φ(c + (θ0-θ)/(σ/√n)) chạy từ -1 → 0
>
> ⇨ 1 - Φ(c + (θ0-θ)/(σ/√n)) chạy từ 0 → 1
>
> Vậy β(θ) là hàm increasing

<br>

<a id="node-698"></a>

<p align="center"><kbd><img src="assets/3fb2380cbe572dff5025a0ed6d6f2a00d0adb832.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp theo đại ý là thường thường, power function của một phép test sẽ phụ
> thuộc vào sample size n. Và khi n có thể được phép chọn, thì power function
> có thể giúp ta trả lời câu hỏi là nên chọn size của sample thế nào.

<br>

<a id="node-699"></a>

<p align="center"><kbd><img src="assets/c6b6f3062ad2e5fd9f3a34844ee2ceeaa518ce7e.png" width="100%"></kbd></p>

🔗 **Related:** [8.3 METHODS OF EVALUATING TEST](83_methods_of_evaluating_test.md#node-696)

> [!NOTE]
> Tiếp nối ví dụ trước đại khái là ta muốn làm sao đó để xác suất Type I Error chỉ
> lớn nhất là bằng 0.1 thôi (tức là P_θ(Type I error) ≤ 0.1) và xác suất Type II Error
> chỉ lớn nhất là .2 nếu θ > θ0 + σ. Và ví dụ này sẽ cho thấy cách để chọn c
> (ngưỡng) và n (sample size) để đạt mục tiêu này. Dùng test rule reject H0: θ ≤ θ0
> nếu (Xbar - θ0) / (σ/√n) > c.
>
> Trong note trước ta đã có power function:
>
> β(θ) = P_θ(Z > c + (θ0-θ)/(σ/√n))
>
> Dừng lại chút để ôn lại:
>
> Phần này bối cảnh là ta đang học cách để đánh giá các phép kiểm tra giả thuyết.
> Nói một cách ngắn gọn, một phép kiểm tra giả thuyết đơn giản bao gồm một test
> statistic, và một rule, để ra quyết định chọn giả thuyết nào. Vậy thì đã là ra quyết
> định, thì cách ra quyết định có thể sai, và ta sẽ muốn giảm thiểu sai lầm.Và ta
> làm vậy bằng cách tiếp cận theo hướng xác suất, tức là ta muốn giảm thiểu xác
> suất của việc mắc sai lầm (error).
>
> Thế thì việc ra quyết định chỉ có một trong hai. Nên sẽ có 2 loại sai lầm:  Khi
> reject H0 trong khi đáng lẽ phải accept (θ ∈ Θ0), gọi là Type I Error và accept H0
> trong khi phải reject (θ ∈ Θ0c), gọi là Type II Error.
>
> Thế thì, khi mà đã hình thành cái rule, thì tự nhiên ta sẽ có một thứ gọi là
> rejection region. Ý là, vì cái rule bản chất chỉ là một hàm số, nhận vào giá trị khả
> dĩ của random sample, và trả ra quyết định reject H0 hay accept H0. Nên hình
> dung ta lấy trong mọi possible value của random sample **X** (range **X**) và
> ném vào function này để lựa ra những cái khiến kết quả là reject H0. Thì cái tập
> đó, gọi là rejection region R = {**x** ∈ range **X**: T(**x**) khiến kết quả test là
> reject H0}
>
> Vậy thì, một event Type I Error xuất hiện khi giả sử H0 nên được accept, mà
> quan sát **X** = **x**, mà T(**x**) khiến H0 bị reject, hay cũng là **x** ∈ R
>
> Viết lại:
>
> Khi H0 nên được accept, tức θ ∈ Θ0: Event Type I Error xảy ra nếu **x**∈****R.
>
> Chú ý, nếu θ ∈ Θ0c. thì không có chuyện Type I Error xảy ra.
>
> Tương tự, event Type II Error xuất hiện khi H0 nên được reject (θ ∈ Θ0c) nhưng
> T(**x**) lại khiến H0 được accept, tức **x** không thuộc R.
>
> Viết lại:
>
> Khi θ ∈ Θ0c, Event Type II Error xảy ra khi x không thuộc R, điều này tương
> đương x thuộc Rc (complement của R).
>
> Như vậy việc tính xác suất của các sự kiện các error như sau:
>
> Khi θ ∈ Θ0, thì mới nói đến xác suất của Type I Error, và nó bằng:
>
> P(Type I Error) = P_θ(**X** ∈ R)
>
> ⇔ P_θ(**X** ∈ R) = P(Type I Error)
>
> Khi θ ∈ Θ0c, thì mới nói đến xác suất của Type II Error, và nó bằng:
>
> P(Type II Error) = P_θ(**X** ∈ Rc) = 1 - P_θ(**X** ∈ R)
>
> ⇔ P_θ(**X** ∈ R) = 1 - P(Type II Error)
>
> Như vậy: P_θ(X ∈ R) là xác xuất Type I Error khi θ ∈ Θ0, và là 1 - xác suất Type
> II Error khi θ ∈ Θ0c.
>
> ====
>
> Rồi, quay lại bài toán này: ta muốn xác suất Type I Error ≤ 0.1 và xác suất Type II
> Error ≤ 0.2 khi θ > θ0 + c. Là sao?
>
> Giả sử θ ∈ Θ0 ⇔ θ ≤ θ0, thì xác suất Type I error sẽ bằng P(x ∈ R)
>
> khi đó để xác suất Type I error ≤ 0.1
>
> ⇔ P_θ(x ∈ R) = β(θ) ≤ 0.1
>
> ⇔ P_θ(Z > c + (θ0-θ)/(σ/√n)) ≤ 0.1
>
> ⇔ 1 - P_θ(Z ≤ c + (θ0-θ)/(σ/√n)) ≤ 0.1
>
> ⇔ P_θ(Z ≤ c + (θ0-θ)/(σ/√n)) ≥ 0.9
>
> ⇔ Φ(c + (θ0-θ)/(σ/√n)) ≥ 0.9
>
> ⇔ ∫-inf:a f(z)dz ≥ 0.9, a = c + (θ0-θ)/(σ/√n)
>
> ⇔ ∫-inf:a (1/√2π) exp(-z^2/2) ≥ 0.9
>
> ====
>
> Nhìn nhận lại, cái ta đang muốn làm là tìm c và n sao cho với mọi θ ≤ θ0 (∈ Θ0)
> thì P_θ(x ∈ R) = β(θ) đều ≤ 0.1.
>
> Và để giải cái inequality này thì sẽ khó.
>
> Tuy nhiên, có một chi tiết ở note trước nói rằng, β là strictly increasing function.
>
> Có nghĩa là khi θ chạy từ -inf → inf thì β(θ) chạy từ 0 → 1
>
> Nên khi xét θ từ -inf → θ0 thì dĩ nhiên β(θ) đạt max tại β(θ0).
>
> Vậy nên để tìm c và n sao cho β(θ) ≤ 0.1 ∀ θ ∈ (-inf, θ0] 
>
> ⇔ tìm c, n sao cho β(θ0) = 0.1.
>
> Hoàn toàn tương tự. Ta muốn xác suất Type II Error ≤ .2 khi θ ≥ θ0 + σ.
>
> Mà khi θ ∈ Θ0c, ⇔ θ ≥ θ0 thì β(θ) = 1 - Xác suất Type 2 Error
>
> ⇨ P(Type II Error) ≤ .2 ⇔ 1 - β(θ) ≤ .2
>
> ⇔ β(θ) ≥ .8
>
> Có nghĩa là ta muốn tìm n, c sao cho với mọi θ0 + σ ≤ θ thì .8 ≤ β(θ)
>
> Mà β increasing, nên khi θ0 + σ ≤ θ thì β(θ0 + σ) ≤ β(θ)
>
> Do đó, bài tóan tương đương tìm n, c sao cho β(θ0 + σ) = 0.8 là vậy. 
>
> Tóm lại: bài toán trở thành:
>
> Tìm c, n sao cho: β(θ0) = 0.1 và β(θ0 + σ) = 0.8. Tức là giải hệ phương trình.
>
> Dĩ nhiên n là số nguyên dương. c là số dương bất kì (nhớ, trong note trước,
> mình đã tự làm, thì đây chính là c', là số dương bất kì, ko, phải là c ∈ [0,1]
>
> Và khúc cuối đại khái là cách giải theo kiểu chọn và kiểm tra.
>
> Đầu tiên tìm c, n thỏa β(θ0) = 0.1 
>
> ⇔ P_θ(Z > c + (θ0-θ)/(σ/√n))|θ=θ0 = 0.1
>
> ⇔ P_θ(Z > c + (θ0-θ0)/(σ/√n)) = 0.1
>
> ⇔ 1 - P_θ(Z ≤ c) = 0.1
>
> ⇔ P_θ(Z ≤ c) = 0.9 
>
> ⇔ Φ(c) = 0.9 
>
> Vế trái là cdf của standard norm, đại khái là có một cái bảng tra (Z-table), để tìm c khiến
> diện tích phần bên trái = 0.9. Giá trị đó là 1.28. Dĩ nhiên cái này không phụ thuộc n,
> vì đây là cdf của standard normal Z tại c, không dính gì đến n. 
>
> Sau đó với c = 1.28, ta sẽ tìm n để thỏa phương trình sau:
>
> β(θ0 + σ) = 0.8
>
> ⇔ P_θ(Z > c + (θ0-θ)/(σ/√n))|θ=θ0+σ = 0.8
>
> ⇔ P_θ(Z > c + (θ0-θ0-σ)/(σ/√n)) = 0.8
>
> ⇔ P_θ(Z > c - 1/(1/√n)) = 0.8
>
> ⇔ P_θ(Z > c - √n) = 0.8
>
> ⇔ 1 - P_θ(Z ≤ c - √n) = 0.8
>
> ⇔ 1 - Φ(c - √n) = 0.8
>
> ⇔ Φ(c - √n) = 0.2
>
> Lại tra bảng, ta sẽ có c - √n ≈ -0.84 ⇔ √n = 1.28 + 0.84 = 2.12 ⇨ n = (2.12)^2 =4.494.
>
> Dĩ nhiên n phải là số nguyên, nên ta cho n = 5 ( khi đó β(θ0 + σ) > 0.8 một chút.
>
> Vậy c = 1.28, n = 5 cho ra một test rule đạt yêu cầu về xác suất của error như mong
> muốn.

<br>

<a id="node-700"></a>

<p align="center"><kbd><img src="assets/d941961bbb2bb93d308da829324663d8c6604db2.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d941961bbb2bb93d308da829324663d8c6604db2.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/2e66cc1b07765bc9c7f1f882dfd37f9b21149b0a.png" width="100%"></kbd></p>

> [!NOTE]
> Cách tra Z-table đại ý là tìm giá trị Φ(z) mong muốn. và cột dọc chính là phần
> nguyên và thập phân thứ nhất, hàng ngang là thập phân thứ hai. Cũng dễ
> hiểu

<br>

<a id="node-701"></a>

<p align="center"><kbd><img src="assets/c164fd50dc3c48909872a1abc70c61ee4fd9cc74.png" width="100%"></kbd></p>

> [!NOTE]
> Đại ý là, như ví dụ vừa rồi ta đã thấy, nếu được chọn random sample
> size và c thì ta có thể có được mức error mong muốn. Nhưng, nếu như
> sample size cố định, thì thường sẽ không thể có cả hai loại error đều
> nhỏ (xác suất).
>
> Do đó, để tìm phép kiểm tra tốt, lúc này thường ta sẽ giới hạn các ứng
> cử viên sao cho chúng đều đạt một mức độ nào đó của Type I error,
> sau đó, ta sẽ tìm cái có error loại kia (Type II error) nhỏ nhất.
>
> Thế thì từ đó, ta có định nghĩa của size α test và level α test:
>
> Size α test theo định nghĩa, là một phép kiểm tra (hypothesis test) dựa
> trên power function β(θ) với β(θ) thỏa: sup_θ ∈ Θ0 β(θ) = α.
>
> Còn Level α test là phép kiểm tra dựa trên power function β với sup_θ
> ∈ Θ0 β(θ) ≤ α.
>
> Làm rõ vài ý: Còn nhớ power function, là function of θ, defined bởi β(θ)
> = P_θ(**X** ∈ R), để nếu θ ∈ Θ0 thì nó là xác suất Type 1 Error và khi θ
> ∈ Θ0c thì nó là 1 - Xác suất Type II Error.
>
> Tác giả nói thêm có nhiều sách không phân biệt hai loại này.Nhưng ở
> đây ta phân biệt để dễ hơn cho các bài toán phức tạp hoặc những
> trường hợp ta ko thể xây dựng size α test.
>
> Vậy thì mình hiểu ở đây rằng khi với một α có giá trị từ 0 đến 1, thì nếu
> phép kiểm tra có giá trị lớn nhất của β function khi search mọi θ trong
> Θ0 bằng α, thì được gọi là Size α test. Còn nếu giá trị này chỉ ≤ α thì nó
> gọi là Level α test.
>
> Vậy ví dụ α = 0.7. Thì một phép kiểm tra có sup_θ ∈ Θ0 P_θ(**X** ∈ R) = 0.7 
> thì nó gọi là Size 0.7 test. Còn nếu phép kiểm tra có sup_θ
> ∈ Θ0 P_θ(X ∈ R) ≤ 0.7 thì nó gọi Level 0.7 test
>
> Vậy thì nếu θ ∈ Θ0 thì với Size 0.7 test, thì xác suất type I error lớn nhất
> chỉ là 0.7. Còn Level 0.7 test sẽ có xác suất type I error lớn nhất cũng chỉ từ
> 0.7 trở xuống.
>
> Và giả sử ta có một đám các phương pháp test đều là Size 0.7 test thì ta có
> thể yên tâm là nếu θ ∈ Θ0, thì xác suất Type I error của chúng đều nhiều nhất
> chỉ là 0.7
>
> Nhớ lại, ta đang trong bối cảnh là muốn tìm / đánh giá các phương pháp
> test. Bằng cách vòng một là lọc ra những thằng nào có xác suất type I error
> đạt một mức độ nào đó của Type I error rồi trong đám đó, vòng 2 mới xem
> type II error thằng nào thấp nhất. 
>
> Vậy thì việc lọc ra những thằng có xác suất type I error cao nhất cũng chỉ
> đạt α = 0.7 chính là vòng 1. Vòng 2 ta sẽ xem trong đám này.cái nào có 
> xác suất type II error thấp nhất.
>
> Chú ý xác suất Type I hay Type II error đều là hàm theo θ, chứ ta ko biết.
> Nên nói cái nào có xác suất type II error thấp nhất, mình dự đoán chính là
> xem thử cái nào có upper bound thấp nhất. (Giống như cách vòng 1: Đám
> pass vòng 1 là đám có upper bound đều ≤ α). Hoặc, thậm chí ta sẽ tìm
> phép test có β(θ) nhỏ nhất trong đám β(θ) với mọi θ.
>
> Khi đó, ta sẽ làm đúng như ý tưởng: Lọc ra một đám có Type I error đạt tiêu
> chuẩn (lọc bằng upper bound) và trong đám đó tìm ra thằng tốt nhất

<br>

<a id="node-702"></a>

<p align="center"><kbd><img src="assets/995784699fcf0c62a7a12cb22b499f3ceccceeeb.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/995784699fcf0c62a7a12cb22b499f3ceccceeeb.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/611d512481f816ba385e4915f6f334f7c02c6d73.png" width="100%"></kbd></p>

> [!NOTE]
> Đoạn này rất quan trọng: Đại ý là như vừa rồi ta đã hiểu định nghĩa của Type
> α  test và Level α test. Thì bằng cách chỉ định α nhỏ, điển hình là 0.1, hoặc 0.
> 01 để đại ý là vòng loại đầu tiên chỉ xét các phép test mà nếu như θ thật sự ∈
> Θ0, tức phải accept H0, thì xác suất mắc Type I error - (accept H1 thay vì
> H0) lớn nhất cũng chỉ bằng 0.01.
>
> Nói dễ hiểu hơn là: Bằng cách đạt α rất nhỏ, ta chỉ chọn những thằng test mà
> xác xuất mắc lỗi loại I của nó cao nhất cũng rất nhỏ.
>
> Thế thì dễ hiểu là việc chọn α rất nhỏ này, chỉ giúp ta lọc các phép test ứng
> cử bởi xác suất mắc lỗi loại I, chứ ko đánh giá gì đến xác suất mắc lỗi loại II.
> Thành ra, giáo sư mới nói, nếu làm theo cách tiếp cận này, thì ta phải thiết kế
> vấn đề sao cho cái lỗi loại I là dạng lỗi nghiêm trọng nhất cần phải tránh.
>
> Mình lấy ví dụ: Giả sử mình viết ra một quy trình kiểm tra để giúp khi mua
> tiền  cổ, thì ko bị mua phải tiền giả. Vậy thì, cái lỗi nguy hiểm nhất ta muốn
> tránh là bỏ một tỷ để mua một đồng tiền giả, nó nghiêm trọng hơn việc gặp
> đồng thật mà lại bỏ qua. Do đó ta muốn cái phương pháp kiểm tra của mình
> của mình, trong trường hợp đồng tiền là giả, thì nó xác suất mắc lỗi "giả mà
> bảo là thật" rất thấp, chỉ 0.01.Điều này cũng đồng nghĩa, giả sử đồng tiền là
> giả, thì xác suất phép test cho ra kết luận đừng mua sẽ là 99.99%.
>
> Tương tự, trong sách giáo sư lấy ví dụ experimenter có thể là đang muốn
> kiểm tra xem nghiên cứu của mình có đúng không. Ví dụ, loại thuốc mới thật
> sự tốt hơn thuốc cũ. Thì khi đó, họ nên thiết kế vấn đề test theo kiểu H0 là "
> thuốc mới không tốt hơn thuốc cũ", H1 à "thuốc mới tốt hơn thuốc cũ". Để khi
> đó, nếu H0 đúng thì xác suất mà phép kiểm tra mắc sai lầm rất nhỏ. Dĩ nhiên
> điều này đồng nghĩa, khi H0 đúng, thuốc là đồ bỏ, thì xác suất phép kiểm tra
> kết luận chọn H0 sẽ là 99.99 %.
>
> Mình hiểu là hoàn toàn ko nói đến case θ ∈ Θ0c, thì xác suất phép test chọn
> H1 thế nào.Hay trong ví dụ đi mua tiền cổ thì, chỉ đang là cái này giúp bảo vệ
> khỏi tình huống, đáng lẽ nên từ chối mua, vì tiền đó là giả, thì lại xách tiền đi
> mua. Chứ chưa hề nói đến việc, giả sử là tiền thật thì phép thử có phán là
> thật hay không.
>
> ====
>
> Và ý cuối, dễ hiểu thôi, là cái này nó giúp ta ít nhiều trong việc chọn test.
> Nhắc lại một chút: Định nghĩa của một hypothesis test, là một cái rule, mà
> trong đó ta sẽ tính toán giá trị của một test statistic (function của random
> sample) để rồi dựa vào một cái rule để quyết định H0 hay H1. Ví dụ như  với
> phương pháo likelihood ratio test, ta tính λ(**x**), và quyết định reject H0 nếu
> λ(**x**) ≤ c, và accept H0 nếu λ(**x**) > c. Thế thì với c là số từ 0, tới 1. Thì ta
> CÓ VÔ SỐ PHÉP TEST. Vì mỗi một giá trị c, sẽ cho ta một cái rule có thể
> dùng để accept hay reject H0. Có nghĩa là, likelihood ratio testing method,
> chỉ đang giúp ta thu hẹp hơn chút xíu không gian các phép thử có thể dùng
> trên đời (để chỉ còn là các phép thử dùng likelihood ratio), nhưng nó vẫn là
> vô số cái.
>
> Thì nay, với α, ta có thể thu hẹp đáng kể các phép thử (tức là bằng cách
> chọn α ví dụ = 0.1, thì c sẽ phải nhỏ hơn mức sao đó)

<br>

<a id="node-703"></a>

<p align="center"><kbd><img src="assets/9e8b9c436c6cb108b0375d9dbf5540cd745556aa.png" width="100%"></kbd></p>

🔗 **Related:** [8.2 METHOD OF FINDING TESTS](82_method_of_finding_tests.md#node-673)

> [!NOTE]
> Ôn tập chút: Theo định nghĩa, size α test là một test mà trong trường hợp θ ∈
> Θ0,  (H0 nên được accept) thì xác suất mắc Type I error (reject H0 trong khi
> phải accept) cao nhất cũng chỉ bằng đúng α
>
> Cao nhất là sao? Là vì ta biết xác suất mắc Type I error, chính là bằng
> P_θ(**x** ∈ R) trong trường hợp θ ∈ Θ0, và đây là hàm theo θ, để rồi nói cao
> nhất chính là khi ta tìm trong mọi θ ∈ Θ0 để maximize hàm này, kết qủa được
> α là gía trị cao nhất của P_θ(x ∈ R): sup_θ ∈ Θ0 P_θ(**x** ∈ R) = α
>
> Vậy bối cảnh ở đây là gì? Là ta muốn tìm cách evaluate test. Mà trong điều
> kiện có thể chọn threshold c cũng như sample size, ta có thể thiết kế ra test
> có xác suất type I, II mong muốn. Nhưng nếu sample size fix, thì cách tiếp
> cận thường thấy là chọn test sao cho thỏa một điều kiện nào đó của Type I
> error. Sau đó sẽ tìm test có Type II error thấp nhất. Vậy thì size α test và level
> α test là hai khái niệm phục vụ điều này.
>
> Thế thì dễ hiểu, size α LRT, sẽ là một LRT (likelihood ratio test) có xác suất
> mắc Type I error cao nhất chỉ bằng α (dĩ nhiên là trong trường hợp θ ∈ Θ0)
>
> Nhớ lại LRT, nó work như sau: Reject H0 nếu λ(**x**) ≤ c, với λ(**x**)
>
> = sup_θ∈Θ0 L(θ|**x**) / sup_θ∈Θ L(θ|**x**)
>
> = L(θ^0|**x**) / L(θ^|**x**)
>
> Và do đó rejection region: R = {**x**: λ(**x**) ≤ c}
>
> Như vậy khi θ ∈ Θ0, P(Type I error) = P_θ(**x** ∈ R) = P_θ(λ(**X**) ≤ c)
>
> Do đó theo định nghĩa của size α test, thì size α LRT sẽ là LRT có
> P_θ(λ(**X**) ≤ c) = α như sách viết là vậy.
>
> Tác gỉa nói thêm, giá trị c quyết định thế nào thì tùy vào từng bài toán cụ thể.
>
> Ví dụ như trong ví dụ 8.2.2, Θ0 chỉ là singleton {θ0} và ta đã thấy rejection
> region là: R = {**x**: |xbar-θ0| ≥ √[-2log(c)/n]}
>
> Để rồi P_θ(**X** ∈ R) = P_θ(|Xbar-θ0| ≥ √[-2log(c)/n])
>
> = P_θ(|Xbar-θ0| ≥ √[-2log(c)/n])
>
> = P_θ(Xbar-θ0 ≥ √[-2log(c)/n] U Xbar-θ0 ≤ -√[-2log(c)/n])
>
> = P_θ(Xbar-θ0 ≥ √[-2log(c)/n]) + P(Xbar-θ0 ≤ -√[-2log(c)/n])
>
> Nhớ rằng trong ví dụ này, σ = 1
>
> = P_θ((Xbar-θ0)/(σ/√n) ≥ √[-2log(c)]) + P((Xbar-θ0)/(σ/√n) ≤ -√[-2log(c)])
>
> = P_θ((Xbar-θ0)/(σ/√n) ≥ √[-2log(c)]) + P((Xbar-θ0)/(σ/√n) ≤ -√[-2log(c)])
>
> Với Z = √n (Xbar - θ0) ~ n(0,1) = (Xbar - θ)/(σ/√n) ~ n(0,1)
>
> ..= P_θ(Z ≥ √[-2log(c)]) + P(Z ≤ -√[-2log(c)])
>
> Do tính đối xứng của normal(0,1)
>
> = 2P_θ(Z ≥ √[-2log(c)])
>
> ⇨ P_θ(**X** ∈ R) = α
>
> ⇔ 2P_θ(Z ≥ √[-2log(c)]) = α
>
> ⇔ P_θ(Z ≥ √[-2log(c)]) = α/2
>
> và trong phần sau ta sẽ thấy nói về z_α/2, là kí hiệu để chỉ giá trị của Z khiến P(Z ≥ z_α/2) = α/2
>
> Nên điểm z_α/2 lúc này chính là √[-2log(c)] 
>
> để từ đó có thể hiểu vì sao trong sách nói test rule viết thành:
>
> Reject H0 nếu |Xbar-θ0| ≥ √[-2log(c)/n]
>
> ⇔ Reject H0 nếu |Xbar-θ0| ≥ √[-2log(c)]/√n
>
> ⇔ Reject H0 nếu |Xbar-θ0| ≥ (z_α/2)/√n
>
> Thế thì, bằng cách chọn c sao cho √[-2log(c) là z_α/2
>
> ⇔ -2log(c) = (z_α/2)^2
>
> ⇔ log(c) = -(z_α/2)^2/2
>
> ⇔ c = exp[-(z_α/2)^2/2], thì ta sẽ có một size α LRT
>
> Có ý này: Tác giả nói ko quan trọng ý là, ko cần phải tìm ra c cụ thể, mà chỉ
> cần  define cái rule theo Z: Reject H0 nếu |Xbar-θ0| ≥ (z_α/2)/√n (z_α/2 là thứ
> có thể tra bảng được, thì ta sẽ có một size α LRT)

<br>

<a id="node-704"></a>

<p align="center"><kbd><img src="assets/9a83f75c50b107c294aa10a1fde2d21897be4809.png" width="100%"></kbd></p>

🔗 **Related:** [8.2 METHOD OF FINDING TESTS](82_method_of_finding_tests.md#node-675)

🔗 **Related:** [5.4 ORDER STATISTIC](54_order_statistic.md#node-386)

> [!NOTE]
> Đại khái là trong ví dụ vừa rồi (8.2.2) thì Θ0 chỉ là một single point set, {θ0} nên
> cơ bản là khi xét tình huống θ ∈ Θ0 để có thể "nói về" Type I error, thì chỉ đơn
> giản là ta có θ = θ0. Từ đó, việc xây dựng size α test chỉ là tìm c sao cho sup_θ
> ∈ Θ0 P_θ(x ∈ R) = α
>
> ⇔ sup_θ∈Θ0 P_θ(λ(**X**) ≤ c) = α
>
> ⇔ sup_θ∈Θ0 P_θ(L(θ^0|**X**) / L(θ^|**X**) ≤ c) = α
>
> (Nhớ, θ^0 là restricted on Θ0 MLE, và θ^ là unrestricted MLE)
>
> hay viết rõ ra:
>
> sup_θ∈Θ0 P_θ(sup_θ ∈ Θ0 L(θ|**X**) / sup_θ∈Θ L(θ|**X**) ≤ c) = α
>
> Dùng sự thật Θ0 = {θ0} thì lúc này, sup_θ∈Θ0 L(θ|**X**) chỉ là L(θ0|**X**)
>
> sup_θ∈Θ0 P_θ(sup_θ ∈ Θ0 L(θ|X) / sup_θ∈Θ L(θ|X) ≤ c)
>
> Và lúc này P cũng ko còn phụ thuộc θ:
>
> = sup_θ∈{θ0} P_θ(L(θ0|**X**) / L(θ^|**X**) ≤ c)
>
> = P_θ0(L(θ0|**X**) / L(θ^|**X**) ≤ c)
>
> Do đó sup_θ∈Θ0 P_θ(λ(**X**) ≤ c) = α ⇔ P_θ0(L(θ0|**X**) / L(θ^|**X**) ≤ c)
>
> và ta giải ra như note vừa rồi.
>
> Ý CHÍNH MUỐN NHẤN MẠNH Ở ĐÂY LÀ: VÌ Θ0 CHỈ CÓ θ0, NÊN CÁI
> sup_θ∈Θ0 P_θ(..) TRỞ NÊN ĐƠN GIẢN, KHÔNG CÒN PHỤ THUỘC θ. GIÚP
> BÀI TOÁN TRÊN TRỞ NÊN DỄ.
>
> NHƯNG VỚI VÍ DỤ 8.2.3, Θ0 LÀ {θ ≤ θ0} khi đó vấn đề trở nên phức tạp hơn.
>
> Lúc này để tìm size α test, ta phải tìm: c sao cho:
>
> sup_θ≤θ0 P_θ(**X** ∈ R) = α . Và trong ví dụ này, rejection R là:
>
> reject region: {x: θ0 - log(c)/n ≤ x(1)}
>
> ⇨ sup_θ≤θ0 P_θ(**X** ∈ R) = α
>
> ⇔ sup_θ≤θ0 P_θ(θ0 - log(c)/n ≤ X(1)) = α
>
> ⇔ sup_θ≤θ0 P_θ(θ0 - log(c)/n ≤ X(1)) = α
>
> ⇔ sup_θ≤θ0 P_θ(X(1) ≥ θ0 - log(c)/n) = α
>
> Tới đây lập luận như sau: Trong ví dụ 8.2.3, X1,..Xn là random sample từ  một
> exponential location family f(x) = e^(-(x-θ))
>
> ⇨ nên X(1) (order statistic) cũng vậy.
>
> ⇨ θ là location parameter của X(1)
>
> Nên khi thay đổi θ trong (-inf, θ1) thì distribution của X(1) chỉ tịnh tiến để thay đổi
> location chứ hình dạng ko đổi.
>
> Rồi, P_θ(X(1) ≥ θ0 - log(c)/n), chính là diện tích của phần đồ thị pdf ở bên phải
> mức θ0 - log(c)/n). Cái này dễ hiểu.
>
> Nênn khi kéo đồ thị qua lại như trên vừa nói, thì diện tích này cũng sẽ thay đổi.
>
> Do đó bài toán đang là:
>
> Tìm c sao cho khi kéo đồ thị qua lại thì diện tích lớn nhất có thể đạt được cũng
> chỉ nhỏ hơn α.
>
> Vậy diện tích lớn nhất có thể có là bao nhiêu? khi nào?
>
> Vậy phải xem lại hình dạng của pdf. Nhưng thật ra cũng không cần, vì đã là pdf,
> thì tổng diện tích bằng 1, nên quy luật bất biến là càng kéo cái hình về bên trái
> một mức nào đó thì cái phần bên phải sẽ càng nhỏ lại. Điều này đúng với mọi
> pdf.
>
> Do đó, dù là distribution nào, thì cái diện tích phần bên phải sẽ lớn nhất khi ta
> KÉO ĐỒ THỊ HẾT CỠ VỀ BÊN PHẢI. CÓ NGHĨA LÀ, CHO θ ĐỤNG θ0.
>
> Khi đó ta sẽ có sup_θ≤θ0 P_θ(X(1) ≥ θ0 - log(c)/n) = P_θ0(X(1) ≥ θ0 - log(c)/n)
>
> Và đây cũng chính là chỗ tác giả nói P_θ(X(1) ≥ c) ≤ P_θ0(X(1) ≥ c) với mọi θ ≤
> θ0.
>
> Vậy bài toán trở thành tìm c để:
>
> P_θ0(X(1) ≥ θ0 - log(c)/n) = α
>
> (tất nhiên mình hiểu vế trái là tính bằng pdf của X(1) với θ = θ0)
>
> Theo link, trong 5.4.4 ta đã có một theorem nói vè pdf của order statistic:
>
> fX(j)(x) = [n!/(j-1)!(n-j)!] fX(x)[FX(x)]^j-1[1 - FX(x)]^n-j
>
> ⇨ fX(1)(x) = n!/0!(n-1)! fX(x)[FX(x)]^0[1 - FX(x)]^n-1
>
> = nfX(x)[1 - FX(x)]^n-1
>
> ⇨ fX(1) = ne^-(x-θ)[1 - ∫-inf:x e^-(t-θ)dt]^n-1
>
> Tính ∫-θ:x e^-(t-θ)dt
>
> = [Nguyên hàm của e^-(t-θ)]|-θ:x
>
> = [-e^-(t-θ)]|-θ:x
>
> = -e^-(x-θ) - (-e^-(θ-θ))
>
> = -e^-(x-θ) + 1
>
> = 1 - e^-(x-θ)
>
> ⇨ fX(1) = ne^-(x-θ)[1 - 1 + e^-(x-θ)]^n-1
>
> = ne^-(x-θ)[e^-(x-θ)]^n-1
>
> = n[e^-(x-θ)]^n
>
> = ne^-n(x-θ)
>
> ⇨ P_θ0(X(1) ≥ θ0 - log(c)/n)
>
> = ∫a:inf ne^-n(x-θ)dx,  với a = θ0 - log(c)/n
>
> = n∫a:inf e^-n(x-θ)dx,  với a = θ0 - log(c)/n
>
> = n[nguyên hàm của e^-n(x-θ)]|a:inf = α
>
> [nguyên hàm của e^-n(x-θ)] = -e^-n(x-θ)/n
>
> = n[-e^-n(x-θ)/n]|a:inf
>
> = [-e^-n(x-θ)]|a:inf
>
> = [-e^-n(inf-θ)+e^-n(a-θ)]
>
> = e^-n(a-θ)
>
> Viết lại P_θ0(X(1) ≥ θ0 - log(c)/n) = P_θ0(X(1) ≥ a) = e^-n(a-θ)
>
> Thay a = θ0 - log(c)/n,
>
> = e^-n(θ0 - log(c)/n - θ0)
>
> = e^-n(log(c)/n)
>
> = e^(log(c))
>
> = c
>
> Viết lại P_θ0(X(1) ≥ θ0 - log(c)/n) = c
>
> Vậy để P_θ0(X(1) ≥ θ0 - log(c)/n) = α
>
> ⇔ c = α
>
> Khi đó a = θ0 - log(α)/n sẽ là cái ngưỡng giúp P_θ0(X(1) ≥ a) = α để rồi ta có một
> size α test.
>
> Trong sách, mr Casella gọi nó là c do từ đầu ông dùng rule reject H0 nếu X(1) ≥
> c} còn mình thì dùng rule reject H0 nếu X(1) ≥ θ0 - log(c)/n derive ở bài trước.
>
> Tức là giống như ta đặt a = θ0 - log(c)/n, thì nó chính là c trong sách. Để rồi, cái
> c (trong sách)  khiến có size α test chính là cái a khiến có size α test, và a đó =
> θ0 - log(α)/n

<br>

<a id="node-705"></a>

<p align="center"><kbd><img src="assets/b0b42a2e4a4069318559f0884ef1d5a05e8514bd.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là ở note trước, có cái vụ P_θ(Z ≥ z_α/2) = α/2
>
> tức là z_α/2 là kí hiệu để chỉ một điểm (giá trị của Z) mà xác suất Z ≥ nó là α/2
>
> Tương tự z_α, là con số mà P(Z > z_α) = α 
>
> Thì đây là quy ước chung cũng dành cho các distribution khác.
>
> Ví dụ như ta có Tn-1 (Student t, bậc tự do n-1) thì tn-1,α/2 là con số mà  
> P(Tn-1 > tn-1,α/2) = α/2
>
> Hay với Chi-square_p random variable X^2_p, thì x^2_p,1-α  là con số mà
> P(X^2_p > 1-α) > 1-α
>
>  Và chúng gọi là CUTOFF POINTS

<br>

<a id="node-706"></a>

<p align="center"><kbd><img src="assets/262f57ddc6ca3be6967bc616c614dccdddcb27c6.png" width="100%"></kbd></p>

🔗 **Related:** [8.2 METHOD OF FINDING TESTS](82_method_of_finding_tests.md#node-688)

🔗 **Related:** [5.3 SAMPLING FROM THE NORMAL DISTRIBUTION](53_sampling_from_the_normal_distribution.md#node-370)

🔗 **Related:** [8.2 METHOD OF FINDING TESTS](82_method_of_finding_tests.md#node-687)

🔗 **Related:** [5.3 SAMPLING FROM THE NORMAL DISTRIBUTION](53_sampling_from_the_normal_distribution.md#node-372)

> [!NOTE]
> Qua ví dụ này, nói về Size α union-intersection test. Dừng một chút, mình
> nên hiểu rằng xuất phát từ định nghĩa của size α test, là một test (mà định
> nghĩa của nó, nhắc lại, là một rule, tính toán một function nào đó của
> random sample, để có test statistic, và áp dụng cái rule nào đó để chọn H0
> hoặc H1) mà trong trường hợp θ ∈ Θ0, thì xác suất Type I Error cao nhất
> sup_θ∈Θ0 P_θ(**x** ∈ R) cũng chỉ bằng α.
>
> Vậy thì hồi nãy, khi test được dùng là thuộc loại likelihood ratio test, thì ta có
> size α LRT. Nên với Bayes test, ta sẽ có size α Bayes test. Hay ở đây, với
> union-intersection test thì ta có size α union-intersection test.
>
> Ôn lại về union-intersection, đại khái ideas của nó là vầy:
>
> Đó là khi Θ0 có thể được thể hiện bởi intersection của các Θ0_γ:
>
> Θ0 = ∩{γ∈Γ} Θ0_γ
>
> Và ta có các hypothesis test con: test giữa H0_γ: θ ∈ Θ0_γ vs H1_γ: θ ∈
> Θ0c_γ có rule: Reject H0_γ nếu x ∈ R_γ, R_γ, là rejection region con, được
> define cũng thông qua một test statistic "con" T_γ(**x**) và cái threshold nào
> đó: R_γ = {**x**: T_γ(**x**) ∈ R_γ}
>
> Thì khi đó, ta có thể có rule của test gốc define bởi các rule của test con:
> Lập luận cũng dễ thôi: Nếu tất cả các H0_γ đều bị reject, thì tức là các test
> con đều kết luận θ not ∈ Θ0_γ  ∀γ. Thì khi đó cũng chính là kết luận "θ cũng
> sẽ not ∈ ∩{γ∈Γ} Θ0_γ.
>
> ⇔  kết luận Reject H0.
>
> Vậy nên rule gốc sẽ là: Reject H0 nếu một H0_γ bất kì bị reject.
>
> Và cũng chính là: chỉ cần **x** ∈ R_γ với γ nào đó, thì x sẽ thuộc R của bài
> toán gốc,
>
> nên rejection region của bài toán gốc define R = U{γ∈Γ} R_γ, hay U{γ∈Γ}
> {x:T_γ(**x**) ∈ R_γ}
>
> Và khi các rule "con" đều là: Reject H0_γ khi T_γ(x) > c, đồng nghĩa rejection
> region "con" là {**x**: T_γ(**x**) > c} thì rule "mẹ" sẽ là:
>
> Reject H0 khi T_γ(**x**) > c với γ nào đó.
>
> Và rejection region "mẹ" sẽ là: {**x**: T_γ(**x**) > c, for some γ} và điều này dễ thấy
> chính là tương đương với {**x**: sup_γ∈Γ T_γ(**x**) > c} → test statistic của test "mẹ"
> là sup_γ∈Γ T_γ(**X**)
>
> ====
>
> Thế thì trong ví dụ 8.2.8, mình đã đi đến kết luận:
>
> H0 bị reject khi H0L bị reject hoặc H0U bị reject
>
> ⇔ (Xbar - μ0) / (S/√n) ≥ tL hoặc (Xbar - μ0) / (S/√n) ≤ tU, 
>
> Tức T_γ1(**X**) chính là (Xbar - μ0) / (S/√n), và cái rule là reject H0L khi T_γ1(**X**) ≥ tL
>
> Và T_γ2(**X**) chính là (Xbar - μ0) / (S/√n), và cái rule là reject H0U khi T_γ2(**X**) ≤ tU
>
> Dẽ hiểu test statistic của bài toán gốc cũng là T(**X**) = (Xbar - μ0) / (S/√n)
> và rule của bài toán mẹ là: reject H0 khi T(x) ≤ tU hoặc T(x) ≥ tL
>
> ====
>
> Vậy thì, quay lại bài toán này, tìm size α union-intersection test, áp định nghĩa
> vào: Khi θ ∈ Θ0 thì xác suất Type I Error lớn nhất phải = α.
>
> ⇔ sup_θ∈Θ0 P_θ(**X** ∈ R) = α
>
> ⇔ sup_θ∈Θ0 P_θ(T(**X**) ≤ tU or T(**X**) ≥ tL) = α
>
> ⇔ sup_θ∈Θ0 [P_θ((Xbar - μ0) / (S/√n) ≤ tU or (Xbar - μ0) / (S/√n) ≥ tL)] = α
>
> (đây là cái tác giả viết trong sách)
>
> =====
>
> Tiếp theo. Đại khái là ta nhớ về định nghĩa của Student's t distribution. Nó được
> định nghĩa là distribution của (Xbar - μ) / (S/√n) của một normal(μ, σ^2) random
> sample.Tức là, lấy random sample X1,...Xn ~ normal(μ, σ). Thì random variable
> tạo bởi sample  mean Xbar và sample variance S theo công thức trên sẽ có distri
> được đặt cho cái tên là Student's t.
>
> Thế thì ở đây cần nhớ trong ví dụ 8.2.8 thì H0: μ = μ0 vs H1: μ khác μ0.
>
> Cũng chính là nói Θ0: θ = (μ, σ^2) sao cho μ = μ0. Và Θ0c là {(μ, σ^2): μ khác μ0}
>
> Nên khi ta đang xét sup_θ∈Θ0 ..thì cũng là đang xét mọi (μ, σ^2): μ = μ0.
>
> Và khi đó ta đang có μ0 chính là true mean của population (Xbar - μ0) / (S/√n)
> (chỗ này có thể hơi khó hiểu, nhưng chỉ cần hiểu đơn giản là, khi ta đang tìm
> trong Θ0 = {(μ, σ^2) sao cho μ = μ0} thì (Xbar - μ0) / (S/√n) dĩ nhiên chính là
> (Xbar - μ) / (S/√n), và do đó, nó là một Student's t với n-1, kí hiệu t_n-1 statistic.
>
> Kí hiệu Student's t statistic đó là T_n-1(X) = (Xbar - μ0) / (S/√n)
>
> ⇨ sup_θ∈Θ0 [P_θ((Xbar - μ0) / (S/√n) ≤ tU or (Xbar - μ0) / (S/√n) ≥ tL)] = α
>
> ⇔ sup_θ∈Θ0 [P_θ(T_n-1 ≤ tU or T_n-1 ≥ tL)] = α
>
> Lúc này, sup không còn ý nghĩa gì nữa. Vì T_n-1 không phụ thuộc σ^2 mà nó
> chỉ phụ thuộc bậc tự do (xem link để thấy, lúc chap 5 mình cũng đã derive pdf
> của nó rồi)
>
> ⇔ P_θ(T_n-1 ≤ tU or T_n-1 ≥ tL) = α
>
> Dĩ nhiên, trong equation này, cái ta cần là tìm tU, tL sao cho thỏa cái này thì
> ta sẽ có một size α union-intersection test.
>
> Và yêu cầu chỉ là tìm tU, tL chứ ko phải tìm hết mọi nghiệm
> nên ta chỉ việc có thể chọn nghiệm để thỏa phương trình.
>
> Vậy đầu tiên ta có thể chọn tU, tL sao cho event trên là union của hai disjoint event
> Tức tU ≤ tL, khi đó theo Axiom 2, phương trình tương đương:
>
>  P_θ(T_n-1 ≤ tU) + P_θ(T_n-1 ≥ tL) = α 
>
> ⇔ 1- P_θ(T_n-1 > tU) + P_θ(T_n-1 ≥ tL) = α 
>
> Rồi, tới đây, nếu chọn tU = t_n-1,1-α1, là con số mà hồi nãy mình vừa học,
> để chỉ con số mà khiến P_θ(T_n-1 > t_n-1,1-α1) = 1-α1
>
> và chọn tL là t_n-1,α2, là con số mà P_θ(T_n-1 ≥ α2) = α2
>
> Và chọn α1, α2 sao cho α1 + α2 = α 
>
> Thì khi đó vế trái sẽ là: 1 - (1 - α1) + α2 = α1 + α2 = α, thỏa phương trình.
>
> Kết luận: Mọi tU, tL sao cho tU = t_n-1,1-α1, tL = t_n-1,α2, α1+α2 = α đều sẽ tạo ra
> một size α union-intersection test. Tức là test mà trong trường hợp θ ∈ Θ0 thì chúng 
> đều có xác súất Type I Error = α.
>
> Và thường thường người ta chọn tL = -tU = t_n-1, α/2

<br>

