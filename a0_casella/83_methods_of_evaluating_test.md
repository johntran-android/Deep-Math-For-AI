# 8.3 Methods Of Evaluating Test

📊 **Progress:** `28` Notes | `40` Screenshots

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

🔗 **Related:** [8.3 METHODS OF EVALUATING TEST](83_methods_of_evaluating_test.md#node-708)

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
> Ôn tập chút: Theo định nghĩa, size α test là một test mà trong trường hợp θ ∈ Θ0,
> (H0 nên được accept) thì xác suất mắc Type I error (reject H0 trong khi phải accept)
> cao nhất cũng chỉ bằng đúng α
>
> Cao nhất là sao? Là vì ta biết xác suất mắc Type I error, chính là bằng P_θ(**x** ∈ R)
> trong trường hợp θ ∈ Θ0, và đây là hàm theo θ, để rồi nói cao nhất chính là khi ta
> tìm trong mọi θ ∈ Θ0 để maximize hàm này, kết qủa được α là gía trị cao nhất của
> P_θ(x ∈ R): sup_θ ∈ Θ0 P_θ(**x** ∈ R) = α
>
> Vậy bối cảnh ở đây là gì? Là ta muốn tìm cách evaluate test. Mà trong điều kiện có
> thể chọn threshold c cũng như sample size, ta có thể thiết kế ra test có xác suất
> type I, II mong muốn. Nhưng nếu sample size fix, thì cách tiếp cận thường thấy là
> chọn test sao cho thỏa một điều kiện nào đó của Type I error. Sau đó sẽ tìm test có
> Type II error thấp nhất. Vậy thì size α test và level α test là hai khái niệm phục vụ
> điều này.
>
> Thế thì dễ hiểu, size α LRT, sẽ là một LRT (likelihood ratio test) có xác suất mắc
> Type I error cao nhất chỉ bằng α (dĩ nhiên là trong trường hợp θ ∈ Θ0)
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
> Do đó theo định nghĩa của size α test, thì size α LRT sẽ là LRT có P_θ(λ(**X**) ≤ c) =
> α như sách viết là vậy.
>
> Tác gỉa nói thêm, giá trị c quyết định thế nào thì tùy vào từng bài toán cụ thể.
>
> Ví dụ như trong ví dụ 8.2.2, Θ0 chỉ là singleton {θ0} và ta đã thấy rejection region là:
> R = {**x**: |xbar-θ0| ≥ √[-2log(c)/n]}
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
> và trong phần sau ta sẽ thấy nói về z_α/2, là kí hiệu để chỉ giá trị của Z khiến P(Z ≥
> z_α/2) = α/2
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
> Có ý này: Tác giả nói ko quan trọng ý là, ko cần phải tìm ra c cụ thể, mà chỉ cần
> define cái rule theo Z: Reject H0 nếu |Xbar-θ0| ≥ (z_α/2)/√n (z_α/2 là thứ có thể tra
> bảng được, thì ta sẽ có một size α LRT)

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

<a id="node-707"></a>

<p align="center"><kbd><img src="assets/e5ec723960cab3d2a45df3a5700b73aec014f445.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp theo, đại ý là giáo sư cho biết bên cạnh α level, còn có những đặc điểm khác
> của một test mà ta cũng có thể quan tâm. Dừng lại một chút để nhớ lại rằng, α
> level, ý là ta muốn xây dựng, tìm kiếm, đánh giá các phép kiểm tra giả thuyết (nói
> gọn là test) dựa trên xác suất mắc Type I error, trong bối cảnh là ta muốn chọn ra,
> tìm ra test tốt nhất. Thế thì ở đây, tạm hiểu là còn có những " cái kiểu" khác để
> đánh giá test nữa.
>
> Cụ thể ta sẽ học thế nào là một unbiased test. Được định nghĩa là, nếu cái test đó,
> nó thiên về (more likely) việc đưa ra kết luận reject H0 khi θ ∈ Θ0c hơn là đưa ra
> kết luận này khi θ ∈ Θ0. Hay, định nghĩa chính thức là, nếu một test có hàm power
> β(θ) có tính chất rằng khi evaluate tại θ' đến từ Θ0c thì luôn lớn hơn hoặc bằng β
> tại θ'' từ Θ0.
>
> Là sao nhỉ? Cần nhẩm lại các khái niệm để ôn tập lại (bạn nào đọc đến chỗ này
> thì đây chính là lúc ta lôi kiến thức ra một cách chủ động, giúp hiểu và nhớ lâu):
> Thứ nhất, nhớ lại β function là cái gì. Theo định nghĩa, nó là xác suất mà ta reject
> H0. Reject H0 là sao? À là vì định nghĩa của một hypothesis test, đơn giản chỉ là
> ta muốn tạo ra một cái rule, có bản chất là một decision function, nhận vào một bộ
> giá trị quan sát được của random sample **X**, và nhả ra kết quả H0 hay H1.(hay
> reject H0 hay accept H0), và cụ thể thì ta sẽ dùng một cái function nào đó áp lên,
> tính toán lên cái random sample **X**, để có một statistic T(**X**), đó chính là test
> statistic, sau đó ta sẽ so sánh với một ngưỡng (threshold) nào đó, để mà ra quyết
> định H0 hay H1, đó chính là rule. Và tổng hợp lại, thì define cái rule sẽ bao gồm từ
> lúc ta quyết định dùng function nào và dùng cái ngưỡng nào.
>
> Thế thì quay lại đây, sau khi ta đã xây dựng được decision function, thì với một giá
> trị **x** của **X**thì thì ta sẽ có một quyết định reject hau accept H0. Vậy nếu ném
> vào mọi giá trị khả dĩ của **X (**∀**x** ∈ Range **X**), ta sẽ chia không gian ra làm
> hai, và tập các giá trị **x**khiến H0 bị reject tạo thành Rejection Region {**x**:
> T(**x**) khiến reject H0}. Do đó sự kiện H0 bị reject, chính là sự kiện observed
> value **x** của **X** bị rơi vào rejection region. Nên xác suất H0 bị reject chính là
> xác suất **X** ∈ R. P(Reject H0) = P_θ(**X** ∈ R).
>
> Tới đây, ta mới nói đến việc đánh giá chất lượng của một test. Dĩ nhiên ta sẽ
> muốn test làm đúng, không mắc sai sót. Mà sai sót thì chỉ có hai loại thôi: Khi
> đáng ra phải accept H0 thì lại đi reject H0. Đây chính là Type I error: Xảy ra khi θ
> thật sự ∈ Θ0, nhưng H0 bị reject, tức **x** ∈ R. Do đó xác suất Type I error chính
> là xác suất x ∈ R khi θ ∈ Θ0. Ngược lại, khi đáng ra phải reject H0 thì lại đi accept
> nó.Đây chính là Type II error, xảy ra khi θ ∈ Θ0c, nhưng x lại thuộc Rc. ⇨ Xác
> suất Type II error = P_θ(**x** ∈ Rc) khi θ ∈ θ0c. Và cái này thì bằng 1 - P_θ(**x** ∈
> R) Do đó mới nói khi P_θ(X ∈ R) sẽ là xác suất Type I error khi θ ∈ Θ0 và 1 - xác
> suất Type II error  khi θ ∈ Θ0c. Và cái P_θ(**X** ∈ R) chính là define cho power
> function β(θ). Vì sao nó lại phụ thuộc θ? Thì bởi vì **X** là random sample, cũng là
> random variable, theo định nghĩa là một iid các random variable X1,...Xn ~
> population distribution có tham số θ. Nên dĩ nhiên xác suất của event liên quan
> đến X phải phụ thuộc θ.
>
> Thế thì, một test hoàn hảo, dĩ nhiên là phải có xác suất Type I error bằng 0 khi θ ∈
> Θ0 và xác suất Type II error bằng 0 khi θ ∈ Θ0c. Cụ thể là, nếu H0 là nhận định
> bệnh nhân không có bệnh, H1 là bệnh nhân có bệnh. Thì một test tốt là test làm
> việc như sau: khi bệnh nhân không có bệnh (θ ∈ Θ0, H0  phải được accept) thì
> phải cho ra xác suất reject H0 / accept H1 / phán bệnh nhân có bệnh / β(θ) phải
> bằng 0. Còn khi người ta có bệnh, thì phải cho ra xác suất accept H0 / phán bệnh
> nhân không có bệnh = 0, cũng chính là β(θ) = 1.
>
> Nhưng đời không như là mơ, do đó phần lớn ta sẽ làm theo chíến lược:  Vòng 1,
> tuyển chọn các test mà khi H0 nên được accept, θ ∈ Θ0 thì xác suất Type 1 error
> (tức reject H0) cao nhất trong mọi θ ∈ Θ0 chỉ bằng α nào đó (ví dụ 0.01, rất nhỏ).
> Để rồi nếu xài môt trong đám này, và thông qua các thiết kế chọn H0, H1 sao cho
> Type I error là cái loại sai sót nghiêm trọng nhất, thì  hệ quả sẽ là, xác suất mà khi
> mắc Type I error = phải accept H0 mà ta lại reject nó sẽ rất thấp. Trong ví dụ bệnh
> nhân, thì xác suất mà ta kết luận người đó có bệnh trong khi họ thực sự khỏe
> mạnh sẽ rất thấp.
>
> Sau đó, sang vòng 2 ta sẽ tìm test có xác suất Type II error thấp nhất.
>
> Thế thì cần nhắc lại bức tranh toàn cảnh để thấy tại sao ta cần unbiased test:
>
> Nhớ lại: β(θ) = defined là P_θ(**X** ∈ R)
>
> và nó = xác suất Type I error khi (a): H0 phải được accept, θ ∈ Θ0
>
> = 1 - xác suất Type II error khi (b): H0 phải bị reject, θ ∈ Θ0c
>
> ⇨ khi (a) xảy ra, β(θ) nhỏ → Xác suất [reject H0], lúc này chính là [**MẮC Type I
> error] NHỎ → TỐT!**
>
> **NHƯNG**, khi (b) xảy ra, thì β(nhỏ), có nghĩa xác suất [reject H0], lúc này chính
> là **[QUYẾT ĐỊNH ĐÚNG], CŨNG NHỎ → KHÔNG TỐT!!!**
>
> Lấy ví dụ bệnh nhân: Giả sử ta có cái test thuộc lại size α test, α = 0.01 như trên.
> Thì khi người ta không bệnh, dựa vào test này xác suất bác sĩ phán ổng có bệnh
> sẽ rất nhỏ. Nhưng nếu lỡ ổng có bệnh, thì β cũng vẫn nhỏ, → bác sĩ cũng phán
> ổng ko có bệnh → tiêu đời.
>
> Do đó, ta mới cần một test bị lệch để khi (a) xảy ra (H0 phải bị accept, θ ∈ Θ0, ông
> đó ko có bệnh) thì  β NHỎ == xác suất phán ổng có bệnh, để rồi mắc Type I error
> NHỎ.
>
> NHƯNG nếu (b) xảy ra (H0 phải bị reject, θ ∈ Θ0c, ông đó có bệnh) thì β PHẢI
> LỚN == xác suất phán ổng có bệnh (là quyết định đúng) LỚN.
>
> Do đó ta mới có cái định nghĩa của **UNBIASED TEST,** là β tính với θ'' từ trường
> hợp (a) (θ'' ∈ Θ0)  thì luôn NHỎ HƠN β tính với θ' từ trường hợp (b) (θ' ∈ Θ0c)
>
> Cái chữ **unbiased**, phải hiểu thế này: Không lệch, unbiased là khi cái test nó
> work một cách công tâm: Nếu ko bệnh thì nói ko bệnh (β nhỏ) còn có bệnh thì nói
> có bệnh (β lớn). Như vậy mới là unbiased. Ngược lại, biased là khi có bệnh hay
> không có bệnh cũng cho β nhỏ hết.

<br>

<a id="node-708"></a>

<p align="center"><kbd><img src="assets/1543ed88a9407427a42c7a7f72b9c7a7ee31e2b5.png" width="100%"></kbd></p>

🔗 **Related:** [8.3 METHODS OF EVALUATING TEST](83_methods_of_evaluating_test.md#node-697)

> [!NOTE]
> Qua ví dụ này, kế thừa từ ví dụ 8.3.3, nói về một test (thuộc loại likelihood
> ratio test, LRT), kiểm tra hai giả thuyết: H0: θ ∈ Θ0 ⇔ θ ≤ θ0 vs H1: θ ∈ Θ0c
> ⇔ θ > θ0. test này có β function:
>
> β(θ) = P_θ(Z > c + (θ0 - θ)/ (σ/√n)) , Z ~ n(0,1)
>
> (nên nhớ, nó vẫn là hàm theo θ)
>
> Vậy ở đây vì sao nó là unbiased test.
>
> Theo định nghĩa thôi, ta cần chỉ ra rằng β có tính chất là giá trị của nó với θ'
> đến từ Θ0c luôn lớn hơn giá trị của nó tại θ'' đến từ Θ0. Tức là, β(θ) với θ ≤
> θ0 luôn ≤ β(θ) với θ0 < θ.
>
> Nhìn kĩ hàm β, dễ thấy nó là diện tích của phần đồ thị bên phải của pdf của Z,
> standard normal. Khi θ chạy từ -inf → inf, thì -θ chạy từ inf → -inf khiến cả cái
> cụm c + (θ0 - θ)/ (σ/√n) cũng vậy.
>
> Mà cái cụm này chính là cái ngưỡng để bắt đầu tính diện tích nói trên. Nên
> việc nó chạy từ inf → -inf khi θ chạy từ -inf → inf có nghĩa là diện tích của
> phần nói trên sẽ TĂNG DẦN LIÊN TỤC. Do đó mới nói hàm β là increasing
> function.
>
> (lập luận vậy dễ hơn nhiều so với việc ráp pdf của Z vào và tính đạo hàm,
> chứng minh nó luôn không âm)
>
> Vậy hàm β(θ) luôn đơn điệu tăng thì dĩ nhiên là tại θ'' ∈ (-inf, θ0] = Θ0   thì dĩ
> nhiên luôn nhỏ hơn tại θ' ∈ (θ0, inf) = Θ0c → thỏa định nghĩa của unbiased
> test

<br>

<a id="node-709"></a>

<p align="center"><kbd><img src="assets/e095c814119930500b5420574b874f451a6034a7.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e095c814119930500b5420574b874f451a6034a7.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/67a2fc6486918055cd278bf99cfb2561bac76d50.png" width="100%"></kbd></p>

> [!NOTE]
> Qua phần 8.3.2 Đại khái là bữa giờ mình đã thấy nhiều loại hypothesis test.
> Một số loại thì có tác dụng kiểm soát xác suất xảy ra Type I error, điển hình là
> level α test hoặc size α test. Nhớ lại định nghĩa của nó là loại test mà nếu
> trong trường hợp H0 nên được accept, θ ∈ Θ0 thì xác suất Type I Error  lớn
> nhất (khi xét mọi θ ∈ Θ0) chỉ bằng α (size α test) hoặc ≤ α (level α test).
>
> Nhờ đó, nếu ta xét một tập hợp các test thuộc loại size hay level α test, với α
> ví dụ như 0.01 thì cơ bản là ta đang xét những test làm tốt trong việc kiểm
> soát xác suất Type I error.
>
> Để rồi, khi xét trong đám này (class này), nếu cái nào mà khi H0 nên được
> reject, tức θ ∈ Θ0c, thì nó có xác suất xảy ra Type II Error thấp nhất đám. Khi
> đó, nó chính là cái có thể ứng cử cho việc trở thành the best test.
>
> Thế thì, nên nhớ, vì β(θ) được define là P_θ(**X** ∈ R), tức cũng là P_θ(reject
> H0|**X**) nên khi H0 nên được accept, thì ta muốn cái xác suất này rất nhỏ ⇔
> β(θ) rất nhỏ.
>
> Nhưng, khi H0 nên được reject, thì ta muốn xác suất này lớn. Do đó, đại khái
> là khi xét trong một class / đám các test, gọi tập này là C. Thì một test mà với
> mọi θ ∈ Θ0c thì β(θ) của nó đều lớn hơn β(θ) của bất kì test nào khác trong C
> (mà trong sách, ta gọi là β') thì khi đó, test đó coi như là tốt nhất (uniformly
> most powerful UMP) trong class C.
>
> Tất nhiên dễ hiểu class C phải là class các test đã kiểm soát được Type I Error
> ví dụ như đều là các size α test hay level α test. Thì khi đó qua đây việc so 
> sánh β cái nào lớn tức xác suất reject H0 khi thực sự H0 nên được reject mới 
> có ích. Chứ nếu một cái test vớ vẩn luôn cho β = 1, tức luôn reject H0 đương
> nhiên sẽ chả bao giờ bị Type II Error nhưng khi đáng lí phải accept H0 thì 
> xác suất nó mắc Type I Error cũng là 100%
>
> Vậy nên khi ta có một class các Level α test, và ta tìm ra thằng tốt nhất trong
> đó Uniformly Most Powerfull (thằng có xác suất Type II Error thấp nhất) thì
> nó được gọi là **UMP level α test.**

<br>

<a id="node-710"></a>

<p align="center"><kbd><img src="assets/ab03e9633650d1a5ce372763e96f74f98fc8ab8a.png" width="100%"></kbd></p>

> [!NOTE]
> Theorem cực quan trọng 
>
> Đại khái nói là xem xét test giữa hai giả thuyết H0: θ = θ0 vs  H1:
> θ = θ1. Dùng một test có rejection region R như vầy. Hiểu đại ý cái test này sẽ
> reject H0 nếu likelihood của θ1 lớn hơn likelihood của θ0 nhân với factor nào
> đó.
>
> và cho α = P_θ0(**X** ∈ R). Dừng lại chỗ này tí xíu, ta còn nhớ, hàm β(θ) được
> định nghĩa là hàm theo θ, define bởi xác suất reject H0: β(θ) = P_θ(**X** ∈ R)
> Để rồi theo định nghĩa của size α test, là test mà sup_θ∈Θ0 P_θ(**X** ∈ R) = α
> Vậy ở đây, với việc Θ0 chỉ có {θ0}, thì sup_θ∈Θ0 P_θ(X ∈ R) cũng chính là
> sup_θ∈{θ0} P_θ(**X** ∈ R) = P_θ0(**X** ∈ R).
>
> Nên cho α = P_θ0(**X** ∈ R), thì chính là nói test này là một size α test
>
> Vậy thì theorem này nói rằng: Điều kiện đủ để một test thỏa 8.3.1 và 8.3.2 sẽ
> đều là UMP level α test.
>
> Hiểu cái này thế nào? Đầu tiên như đã hiểu ở trên, thỏa 8.3.2 thì đây đương
> nhiên là một size α test. Thế còn thỏa 8.3.1, mình đã thấy rằng đây chính là nói
> về test dùng likelihood để ra quyết định. Thì thực ra có thể viết lại chút xíu để
> thấy cái test này có rule như sau:
>
> reject H0 nếu f(**x**|θ1)/f(**x**|θ0) > k, mà đây cũng chính là
> L(θ1|**x**)/L(θ0|**x**) > k ⇔ L(θ0|**x**)/L(θ1|**x**) < 1/k
>
> Nhớ lại định nghĩa của likelihood ratio test, có rule như sau:
>
> reject H0 nếu λ(**x**) = L(θ^0|**x**)/L(θ^|**x**) = sup_θ∈Θ0 L(θ|**x**) / sup_θ∈Θ1
> L(θ|**x**) ≤ c
>
> Thế thì ở đây không hoàn toàn chính xác là likelihood ratio, nhưng rất gần
> giống ở ý tưởng. Với LRT, việc reject H0 nếu λ(**x**) < c có ý nghĩa là khi quan
> sát thấy data **X** = **x**, thì mức độ hợp lí lớn nhất có được khi tìm kiếm θ từ
> Θ0 chỉ bằng phần nhỏ độ hợp lí lớn nhất khi tìm kiếm θ từ toàn bộ Θ, chứng tỏ
> Θ0 không đủ tin cậy, nên ta reject H0: θ ∈ Θ0.
>
> Còn ở đây, ta reject H0 khi độ hợp lí của θ0 (cũng là sup_θ∈Θ0 L(θ|**x**)) chỉ
> bằng một phần nhỏ của độ hợp lí của θ1 (cũng là sup_θ∈Θ0c L(θ|**x**)). Nói
> cách khác khi độ hợp lí của θ0 nhỏ hơn độ hợp lí của θ1 thì reject H0, thế thôi.
>
> Nhưng nếu suy nghĩ chút ta sẽ thấy thật ra là giống nhau:
>
> Cụ thể là trong trường hợp này, Θ = {θ0, θ1}. Nên sup_θ∈Θ L(θ|**x**) sẽ chỉ là
> L(θ0|**x**) hoặc L(θ1|**x**). ⇨ nếu dùng LRT, thì cái rule sẽ là:
>
> reject H0 khi λ(**x**) = L(θ0|**x**) / max(L(θ0|**x**), L(θ1|**x**) ≤ c
>
> Mà khi θ = θ0 thì λ(**x**) = 1, không thể ≤ c với c < 1.
>
> Nên điều kiện reject H0 chính là L(θ0|**x**) / L(θ1|**x**) ≤ c thì nếu coi c = 1/k
> thì đây ta sẽ thấy điều kiện 8.3.1 chính là likelihood ratio thôi.
>
> Còn điều kiện cần, nó nói là nếu test thỏa 8.3.1 và 8.3.2 với k > 0 thì mọi UMP
> level α test sẽ đều là size α test.
>
> Để hiểu cái này cần nhớ level α test là gì và size α test là gì. Nói ngắn gọn,
> level α test là cái test mà khi sup_θ∈Θ0 β(θ) ≤ α, còn size α test là test mà
> sup_θ∈Θ0 β(θ) = α. Và ý nghĩa của nó phản ánh trong chữ level (đẳng cấp) và
> kích thước (size). Lấy α = 0.1 đi. Thì level 0.1 test, là test có đẳng cấp 0.1 mà
> đẳng cấp, thì ám chỉ một tầng lớp. Tức là có nhiều, và đám test này đều có xác
> suất Type I Error sup_θ∈Θ0c β(θ) dưới 0.1. Và nói vậy thì giá trị này của chúng
> (sup_θ∈Θ0 β(θ)) có thể = 0.05, 0.01,...Thì nếu bằng 0.05, thì nó là một Size 0.
> 05 test. Nếu nó bằng 0.01 thì nó là một Size 0.01 test.
>
> Vậy cái thằng Size 0.1 test có thể thế thấy cũng là một Level 0.1 test, và nó là
> thằng TỆ nhất khi xét khía cạnh xác suất mắc lỗi loại 1 (vì xác suất cao nhất)
> ĐỂ Ý Ý NÀY TÍ NỮA QUAY LẠI.
>
> Nhìn lại 8.3.1, nó là cái rule (giúp quyết định reject/accept H0), dĩ nhiên bản
> thân một cái test cơ bản chỉ là cái rule mà thôi. Còn 8.3.2 nói về cái trần: Nếu
> một cái test thỏa 8.3.1, có nghĩa nó là size α test, có xác suất mắc Type I Error
> (trong trường hợp H0 cần được accept) cao nhất bằng đúng α. Và như vừa nói
> ở trên **NÓ LÀ CÁI TỆ NHẤT TRONG ĐÁM LEVEL α TEST** nếu xét khả năng
> mắc lỗi loại I.
>
> Vậy từ đây ta mới xem điều kiện cần nói gì?
>
> Ý thứ nhất nó nói: Nếu tồn tại một test thỏa 8.3.1, tức là có cái rule như vậy, và
> thỏa 8.3.2 tức là là một size α test. thì khi đó MỌI UMP LEVEL α TEST ĐỀU LÀ
> SIZE α TEST: Có nghĩa là sao?
>
> CHÍNH LÀ NÓI RẰNG: NẾU SO SÁNH ĐÁM LEVEL α TEST THEO TIÊU
> CHUẨN XÁC SUẤT MẮC TYPE II ERROR. THÌ **CÁI THẰNG TỐT NHẤT LẠI
> CHÍNH LÀ CÁI THẰNG TỆ NHẤT Ở TRÊN, THẰNG SIZE α TEST**. HAY
> CHƯA!
>
> Vì sao theorem phải nói về cái vụ existed. Là vì trong phần định nghĩa size /
> level α test, tác giả có nói, không phải lúc nào cũng tồn tại size α test.
>
> Thế còn ý sau, nói là, mọi UMP level α test đều có cùng cái rule 8.3.1. THÌ
> CHÍNH LÀ KHẲNG ĐỊNH RẰNG: **CÁI THẰNG SIZE α TEST TỆ NHẤT Ở
> KHÍA CẠNH  TYPE 1, TỐT NHẤT Ở KHÍA CẠNH TYPE II, LÀ ĐỘC NHẤT.**
>
> Hiểu nôm na cái theorem này thế này: Ta có một biên độ mạo hiểm cho sai sót
> loại I. Lấy ví dụ H0 vs H1 là khi người ta chào mời một đồng tiền cổ, H0: tiền
> giả, đừng mua. H1: tiền thật nên mua, không mua. Thì mình sẽ cho một biên
> độ rủi ro ra quyết định sai loại 1: Đồng xu là giả, đáng ra phải không mua mà lại
> đi mua (reject H0), cao nhất là 0.3. Thì cái test (phương pháp test xu) có khả
> năng mắc sai lầm mua nhầm cao nhất chính là cái Size 0.3 test, là cái tệ nhất
> theo tiêu chí này trong đám level 0.3 test. Mấy cái test khác, chắc cú hơn, thận
> trọng hơn, ví dụ như có xác suất mua đồ giả cao nhất chỉ là 0.1 chẳng hạn.
>
> Tuy nhiên, theorem này nói rằng, trong đám này, thì cái thằng Size 0.3 test lại
> chính là  thằng tốt nhất khi xét cái lỗi Type II: Đồ thật mà lại bỏ qua.
>
> Do đó, để tìm thằng tốt nhất toàn cục: Thì ta phải **mạo hiểm hết mức có thể
> trong biên độ rủi ro (loại I) cho phép**, để c**hấp nhận là thằng test dễ mua
> phải đồ giả nhất nhưng cũng là thằng ít bị miss đồ thật nhất.**

<br>

<a id="node-711"></a>

<p align="center"><kbd><img src="assets/571273b43e14e960926d279b500f4150d48b7f90.png" width="100%"></kbd></p>

> [!NOTE]
> Cùng tìm hiểu phần chứng minh, ý a):
>
> Đầu tiên, gs lưu ý ta thấy rằng bất kì cái test nào thỏa 8. 3.2 thì chính là
> **size α test**, cái này thì trong note trước mình đã tự thấy rồi, nói ngắn gọn
> là vì trong theorem này chỉ đang nói về hypothesis H0: θ = θ0, tức Θ0 chỉ là
> set có 1 elements: {θ0}. Mà theo định nghĩa của size α test, nó là test mà
> sup_θ∈Θ0 β(θ) = α, thì ở đây dĩ nhiên sup_θ∈Θ0 β(θ) chính là β(θ0), hay
> P_θ0(**X** ∈ R) (vì đây là định nghĩa của hàm power function β).
>
> Tiếp theo, tác giả đề nghị ta đặt một indicator function gọi là test function:
> mang giá trị bằng 1 khi **x** ∈ R và 0 khi **x** ∈ Rc. Nói nó là indicator
> function the rejection region hoàn toàn dễ hiểu. Nhớ lại khái niệm indicator
> function, mình đã gặp hồi học Stat110: Indicator function of even A, kí hiệu
> I_A, thì khi A xảy ra nó bằng 1, ngược lại nó bằng 0. Thì ở đây event A có
> thể xem như là event **x** ∈ R.
>
> Tiếp, đặt Φ(**x**) là test function của cái test thỏa 8.3.1 và 8.3.2. Và Φ'(x) là
> test function của bất kì level α test nào. Và cho β(θ), β'(θ) là power function
> tương ứng với test Φ và test Φ'.
>
> Thế thì vì hàm Φ', hay Φ đều chỉ có giá trị là 0 hoặc 1. Nên
>
> [Φ(**x**) - Φ'(**x**)][f(**x**|θ1] - kf(**x**|θ0)] ≥ 0 với mọi **x**. Vì sao nhỉ?
>
> Là vì đã nói Φ và Φ' đều là cái test thỏa 8.3.1, tức là nó đều có rule là: reject
> H0 nếu f(**x**|θ1) > kf(**x**|θ0) và accept H0 nếu f(**x**|θ1) < kf(**x**|θ0)
>
> Vậy xét hai trường hợp:
>
> i) f(**x**|θ1] > kf(**x**|θ0) → test Φ sẽ reject H0, **x**∈R → hàm indicator
> Φ(**x**) = I_(**x**∈R) = 1
>
> Lúc này Φ(**x**) - Φ'(**x**) = 1 - Φ'(**x**) ≥ 0 vì Φ'(**x**) cũng chỉ bằng 1 hoặc
> 0. Và f(**x**|θ1] > kf(**x**|θ0) ⇨ f(**x**|θ1] - kf(**x**|θ0) ≥ 0 ⇨ [Φ(**x**) - Φ'
> (**x**)][f(**x**|θ1] - kf(**x**|θ0)] ≥ 0
>
> ii) f(**x**|θ1] < kf(**x**|θ0) → test Φ sẽ accept H0, **x** ∈ Rc → hàm indicator
> Φ(**x**) = I_(**x**∈Rc) = 0.
>
> Lúc này Φ(**x**) - Φ'(**x**) = 0 - Φ'(**x**) ≤ 0. Và f(**x**|θ1] < kf(**x**|θ0) →
> f(x|θ1] - kf(x|θ0) < 0
>
> ⇨ [Φ(**x**) - Φ'(**x**)][f(**x**|θ1] - kf(**x**|θ0)] ≥ 0
>
> Tóm lại trong cả hai trường hợp thì [Φ(**x**) - Φ'(**x**)][f(**x**|θ1] -
> kf(**x**|θ0)] luôn ≥ 0
>
> Và do đó khi tích phân trên toàn miền R^n, nó cũng phải ≥ 0:
>
> ∫ [Φ(**x**) - Φ'(**x**)][f(**x**|θ1] - kf(**x**|θ0)] d**x** ≥ 0
>
> Triển khai ra:
>
> ⇔ ∫ [Φ(**x**)f(**x**|θ1] - Φ'(**x**)f(**x**|θ1] - Φ(**x**)kf(**x**|θ0) + Φ'
> (**x**)kf(**x**|θ0)]dx ≥ 0
>
> ⇔ ∫Φ(**x**)f(**x**|θ1d**x** - ∫Φ'(**x**)f(**x**|θ1d**x** - ∫Φ(**x**)kf(**x**|θ0)d**x**
> + ∫Φ' (**x**)kf(**x**|θ0)d**x** ≥ 0
>
> ⇔ ∫Φ(**x**)f(**x**|θ1d**x** - ∫Φ'(**x**)f(**x**|θ1d**x** - k[ ∫Φ(**x**)f(**x**|θ0)d**x**
> - ∫Φ' (**x**)f(**x**|θ0)d**x**] ≥ 0
>
> ====
>
> Xét ∫Φ(**x**)f(**x**|θ0)d**x**:
>
> Đây là tích phân trên toàn miền của **x**. Dĩ nhiên ta có thể tách làm hai:
>
> ∫_R Φ(**x**)f(**x**|θ0)**dx** + ∫_Rc Φ(**x**)f(**x**|θ0)**dx**
>
> = ∫_R 1 * f(**x**|θ0)d**x** + ∫_Rc 0* f(**x**|θ0)**dx** | khi **x** ∈ R → Φ(**x**) =
> 1, khi **x** ∈ Rc → Φ(**x**) = 0
>
> = ∫_R f(**x**|θ0)d**x**
>
> Và đây dĩ nhiên chính là P_θ0(**X** ∈ R), hay β(θ0)
>
> Mà β(θ) được định nghĩa là P_θ(**X** ∈ R), để ý nghĩa là θ ∈ Θ0 thì đây
> chính là xác suất mắc Type I error.
>
> Và ở đây, Θ0 = {θ0} ⇨ P_θ0(**X** ∈ R), = β(θ0) CHÍNH LÀ **XÁC SUẤT
> MẮC LỖI LOẠI I.**
>
> ====
>
> Còn ∫Φ(**x**)f(**x**|θ1)**dx**, tương tự
>
> = ∫_R 1 * f(**x**|θ1)**dx**+ ∫_Rc 0 * f(**x**|θ1)**dx**
>
> = ∫_R f(**x**|θ1)**dx**
>
> = P_θ1(**X** ∈ R) = β(θ1)
>
> Thế thì lại nó lại ý nghĩa của P_θ(**X** ∈ R), hay β(θ) chính là 1 - Xác suất
> mắc type II error khi θ ∈ Θ0c. Hay nói cách khác, nó chính là **xác suất đưa
> ra quyết định đúng: chọn H1 khi thật sự nên chọn H1**. Và trong bối cảnh
> này được gọi là power, mà ta gọi nó là năng lực bắt đúng bệnh.
>
> Vậy thì vì Θ0c trong trường hợp này là {θ1}, nên khi θ = θ1, thì chính là θ ∈
> Θ0c đã xảy ra, nên như trên vừa nói, P_θ1(X ∈ R), hay β(θ1) chính là
> power.
>
> ====
>
> Vậy quay lại đây, ta đang có:
>
> ∫Φ(**x**)f(**x**|θ1d**x** - ∫Φ'(**x**)f(**x**|θ1d**x** - k[ ∫Φ(**x**)f(**x**|θ0)d**x** -
> ∫Φ' (**x**)f(**x**|θ0)d**x**] ≥ 0
>
> ⇔ β(θ1) - β'(θ1) - k[β(θ0) - β'(θ0)] ≥ 0
>
> ⇔ β(θ1) - β'(θ1) ≥ k[β(θ0) - β'(θ0)]
>
> Rồi, lập luận như sau:
>
> Vì đã nói ở trên, ta đang xét test Φ là một size α test, nên β(θ0), như đã nói,
> chính là sup_θ∈Θ0 β(θ), và theo định nghĩa của size α test, cái này bằng α.
>
> Còn Φ' là một test bất kì thuộc loại level α test, mà theo định nghĩa,
> sup_θ∈Θ0 β'(θ) ≤ α. Nên ở đây sup_θ∈Θ0 β'(θ) = β'(θ0) ≤ α.
>
> Như vậy [β(θ0) - β'(θ0)] ≥ 0, cộng với k dương, ta có hạng tử k[β(θ0) - β'
> (θ0)] là một số không âm.
>
> Như vậy ta có β(θ1) - β'(θ1) ≥ k[β(θ0) - β'(θ0)] ≥ 0
>
> ⇨ β(θ1) - β'(θ1) ≥ 0
>
> ⇔ β(θ1) ≥ β'(θ1)
>
> Kết luận này cho thấy test Φ, một size α test, mà lại thỏa β(θ1) ≥ β'(θ1) với
> mọi β' là power của level α test bất kì.
>
> mà β(θ1) ≥ β'(θ1) thì cũng chính là β(θ) ≥ β'(θ) ∀ θ ∈ Θ0c (trong trường hợp
> này = {θ1})
>
> Vậy chiếu theo định nghĩa 8.3.11 về uniform most powerful UMP class C
> test, thì cho  ta kết luận: Φ chính là UMP level α test (vì class C ở đây là mọi
> level α test).
>
> Hay nói đầy đủ: size α test Φ chính là UMP level α test.
>
> Nói nôm na dân dã: Trong đám level α test, xét theo xác suất mắc lỗi loại 1,
> thì thằng Φ, một size α test, là thằng tệ nhất. Nhưng xét theo xác suất mắc
> lỗi loại 2, thì nó lại là thằng ít tệ nhất, nói cách khác, nó là thằng có năng lực
> cao nhất trong việc chọn đúng H1 khi θ ∈ Θ0c.

<br>

<a id="node-712"></a>

<p align="center"><kbd><img src="assets/09115abf61ee6e2927255db96bde989163a83af8.png" width="100%"></kbd></p>

> [!NOTE]
> Chứng minh ý b) điều kiện cần: Đại ý của ý này là, thằng UMP level α test
> phải là độc nhất. Có nghĩa nếu có cái test nào khác cũng tự xưng là UMP
> level test, thì nó cũng phải y chang cái Φ. Ví dụ giả sử ta gọi Φ' là cái test
> cũng là một UMP level test. Thì ta sẽ chứng minh rejection region của nó
> cũng y hệt của Φ, điều này đồng nghĩa indicator function Φ(**x**) = Φ'(**x**)
> với mọi **x**, có thể cho phép chúng khác nhau trên những giá trị x không
> thuộc support **X**, tức là những giá trị không thể xảy ra của random sample
> **X**Thế thì chứng minh như sau: Vì ta đang giả sử Φ' cũng là một UMP level α
> test, nên theo định nghĩa của UMP level α test, β'(θ) ≥ β''(θ) ∀ θ ∈ Θ0c với β''
> là β function của một test bất kì trong level α test class.
>
> Với việc Θ0c = {θ1} ⇨ cái trên ⇔ β'(θ) ≥ β''(θ) với θ = θ1 ⇔ β'(θ1) ≥ β'' (θ1)
>
> Trong đó có cả β(θ1), tức là β của Φ, tức là β'(θ1) ≥ β(θ1)
>
> Mà ta cũng có Φ đang là UMP level α test, nên β(θ1) ≥ β''(θ1) bao gồm cả β'
> (θ1): β(θ1) ≥ β'(θ1)
>
> Vậy chúng phải bằng nhau β(θ1) = β'(θ1).
>
> Rồi, hồi nãy ta đã có kết quả này:
>
> β(θ1) - β'(θ1) - k[β(θ0) - β'(θ0)] ≥ 0 với β' là power của level α test bất kì thì ở
> đây khi β' đặt cho UMP level α test Φ' thì bất đẳng thức này vẫn đúng.
>
> Với việc  β(θ1) = β'(θ1) bất đẳng thức này trở thành:
>
> - k[β(θ0) - β'(θ0)] ≥ 0
>
> ⇔ [β(θ0) - β'(θ0)] ≤ 0
>
> ⇔ β(θ0) ≤ β'(θ0)
>
> Và β(θ0) như đã nói nãy giờ, nó là sup_θ∈Θ0={θ0} β(θ) = α, nên ta có:
>
> ⇔ α ≤ β'(θ0) (1)
>
> Tới đây nhìn lại lại việc ta đang giả sử Φ' cũng là một UMP level α test
>
> thì trước hết nó là một level α test
>
> ⇨ sup_θ∈Θ0 β'(θ) (= sup_θ∈{θ0} β'(θ) = β'(θ0)) ≤ α
>
> Vậy β'(θ0)) ≤ α (2)
>
> từ (1) và (2) ⇨ β'(θ0)) = α giúp kết luận:
>
> Φ' cũng phải là một size α test.
>
> Và β'(θ0)) = β(θ0))
>
> cũng như là cái inequality β(θ1) - β'(θ1) - k[β(θ0) - β'(θ0)] ≥ 0
>
> trở thành 0 = 0 tức là vế trái, β(θ1) - β'(θ1) - k[β(θ0) - β'(θ0)], = 0
>
> mà vế trái ta nhớ có xuất thân là ∫ [Φ(x) - Φ'(x)][f(x|θ1] - kf(x|θ0)] dx
>
> Nên ∫ [Φ(**x**) - Φ'(**x**)][f(**x**|θ1] - kf(**x**|θ0)] dx = 0
>
> Mà [Φ(**x**) - Φ'(**x**)][f(**x**|θ1] - kf(**x**|θ0)]  ≥ 0
>
> nên cái tích phân bằng 0 suy ra [Φ(**x**) - Φ'(**x**)][f(**x**|θ1] - kf(**x**|θ0)] = 0
>
> ⇔ Φ(**x**) = Φ'(**x**) hoặc f(**x**|θ1] = kf(**x**|θ0)
>
> Vậy Φ(**x**) = Φ'(**x**) với mọi **x**
>
> hoặc có thể khác nhau tại những **x** thỏa **x** ∈ {**x**: f(**x**|θ1) =
> kf(**x**|θ0)}
>
> Mà cái tập này thực chất là gì: nó là tập các điểm **x** mà tại đó pdf f(**x**|θ1)
> = kf(**x**|θ0), và trong trường hợp đang chứng minh với hàm liên tục thì tập
> này có xác suất = 0 (là tập A nói đến trong sách). Do đó, kết luận là Φ(x) = Φ'
> (x) tại mọi x trừ x thuộc tập A là tập có xác suất bằng 0. Thì theo lí thuyết toán
> học, điều này coi như hai hàm Φ và Φ' là một

<br>

<a id="node-713"></a>

<p align="center"><kbd><img src="assets/1254e949513010f2b04afc2bf32904b3bb2367fe.png" width="100%"></kbd></p>

🔗 **Related:** [8.3 METHODS OF EVALUATING TEST](83_methods_of_evaluating_test.md#node-716)

> [!NOTE]
> Hiểu về bổ đề này đại ý như sau, nó kết nối bổ đề Neyman-Pearson với
> sufficiency. Xét bài toán kiểm định giả thuyết như ở theorem trước, tức là ta
> kiểm tra giữa hai giả thuyết đơn giản H0: θ ∈ Θ0 = {θ0} vs H1: θ ∈ Θ0c  =
> {θ1}.
>
> Và T(**X**) là sufficient statistic của θ, và g(t|θi) là pdf/pmf của T.
>
> Bổ đề này nói rằng mọi test dựa vào T với rejection region S sẽ đều là
> UMP level α test, nếu nó thỏa mãn:
>
> t ∈ S nếu g(t|θ1) > kg(t|θ0) và t ∈ Sc nếu g(t|θ1) < kg(t|θ0)
>
> và α = P_θ0(T ∈ S)
>
> Thế thì mình hiểu test dựa vào T là sao?
>
> Mình hiểu thế này: Như đã biết, test thực chất chỉ là một cái rule, và cái
> rule này dựa vào giá trị có được từ việc áp một một hàm số lên giá trị của
> random sample **X**, rồi dùng cái tiêu chí nào đó, để đưa ra quyết định, ví
> dụ như so với một ngưỡng nào đó. Thì apply hàm số lên random sample
> cho ta một statistic, đó chính là test statistic.Và khi đã define ra cái rule, thì
> nó sẽ chia sample space của random sample thành hai phần: Rejection
> region R và complement của nó  Rc. Trong đó R = {x: test statistic khiến H0
> bị reject}.
>
> Vậy thì ở đây, chỉ đơn giản là cái test statistic đó là một sufficient statistic T
> thôi. và tương tự như test rule sẽ chia sample space ra thành R và Rc, thì
> nó cũng chia sample space của T thành S và Sc, S là tập những giá trị t =
> T(**x**) của T, khiến cho theo test rule thì H0 bị reject.
>
> Còn nhớ theorem vừa rồi, nó nói rằng, nếu một test thỏa hai điều kiện: có
> rule tuân theo 8.3.1 và thỏa 8.3.2 = là một size α test thì nó sẽ chính là một
> UMP level α test, và là duy nhất.

<br>

<a id="node-714"></a>

<p align="center"><kbd><img src="assets/335c93bf6c276c677a916c892482beac50811192.png" width="100%"></kbd></p>

> [!NOTE]
> Chứng minh đại khái là như vầy: Mình sẽ tìm cách cho thấy test thỏa điều
> kiện của bổ đề này nêu lên cũng sẽ thỏa điều kiện 8.3.1 và 8.3.2, để rồi
> theo bổ đề Neiman-Pearson, cái test này đích thị là một UMP α test.
>
> Thế thì test này có rule là:
>
> reject H0, cũng là có rejection region S chứa t khi g(t|θ1) > kg(t|θ0)
>
> và accept H0, cũng là region region S không chứa t khi g(t|θ1) < kg(t|θ0)
>
> trong đó như đã nói, g là pdf/pmf của sufficient statistic T.
>
> Mà trong những chương trước, ta đã biết một theorem gọi là Factorization
> Theorem, nói đại ý là nếu chỉ ra một statistic T có tính chất là pdf của **X**
> có thể được factor thành g(T(**x**)|θ)h(**x**), tức là tích của một hàm có
> phụ thuộc θ nhưng  chỉ phụ thuộc **x** thông qua T(**x**) và một hàm không
> âm và không phụ thuộc θ thì khi đó T(**X**) chính là một sufficient statistic
> (điều kiện cần và đủ)
>
> Như vậy, ở đây vì T là sufficient statistic, nên kiểu gì cũng chỉ có thể factor
> f(**x**|θ) thành g(t|θ)h(**x**), tức là tồn tại hàm h(**x**) để có cái này
>
> Vì nó không âm, nên ta có thể nhân h(**x**) vào hai vế của hai cái điều kiện
> (a1) (a2) để có  cái rule tương đương:
>
> reject H0, t ∈ S khi g(t|θ1)h(**x**) > kg(t|θ0)h(**x**) ⇔ f(**x**|θ1) > kf(**x**|θ0)
>
> và accept H0, t ∈ Sc khi g(t|θ1)h(**x**) < kg(t|θ0)h(**x**) ⇔ f(**x**|θ1) <
> kf(**x**|θ0)
>
> thì đây cũng chính là 8.3.1 vì t ∈ S thì cũng là X ∈ R thôi, đều là reject H0
>
> Tiếp, điều kiện của test này (theo T) cũng có:
>
> α = P_θ0(T ∈ S)
>
> Mà P_θ0(T ∈ S) cũng bằng P_θ0(**X** ∈ R) vì đã nói trên t ∈ S thì cũng là x ∈ R
>
> Nên ta cũng có P_θ0(**X** ∈ R) = α  → Đây là 8.3.2
>
> Vậy kết luận test thỏa Neyman-Pearson lemma ⇨ Thỏa điều kiện để nó là
> một unique UMP level α

<br>

<a id="node-715"></a>

<p align="center"><kbd><img src="assets/b978fd8878bdce4e697720409f482a4549d61e6f.png" width="100%"></kbd></p>

> [!NOTE]
> Qua ví dụ này, UMP binomial test. Cho X ~ binomial(2, θ) và ta muốn test giữa
> hai giả thuyết H0: θ = 1/2 vs H1: θ = 3/4.
>
> Có lẽ cần recall lại chút xíu về bổ đề Neyman-Pearson. Nó nói rằng trong bài
> toán hypo testing giữa hai simple hypothesis: H0: θ ∈ Θ0 ={θ0} và H1: θ ∈ Θ0c
> = {θ1}. Nếu ta xét các test có rule như sau:
>
> reject H0 nếu kf(**x**|θ0) < f(**x**|θ1) và accept H0 nếu kf(**x**|θ0) > f(**x**|θ1)
>
> và α = P_θ0(**X** ∈ R)
>
> thì nó chính là UMP level α test độc nhất.
>
> Vậy thì, mình nên hiểu rằng, thực chất cái bổ đề này đưa ra nhận định về rằng
> khi nào thì ta có một UMP size α test.
>
> Vậy thì ở đây. θ0 = 1/2, θ1 = 3/4.
>
> Xem thử f(**x**|θ) là gì:
>
> Còn nhớ công thức pmf của binomial (n,p): f(k|n,p) = (n choose k) p^k
> (1-p)^(n-k)
>
> ⇨ pdf của binomial(2, θ): f(x|θ) = (2 choose x) θ^x (1-θ)^(2-x)
>
> X ~ binomial(2, θ) thì range of X = {0,1,2}
>
> f(0|θ1)/f(0|θ0) = (2 choose 0) θ1^0 (1-θ1)^(2-0) / (2 choose 0) θ0^0 (1-θ0)^(2-0)
>
> = 1 * 1 * (1-θ1)^2 /  1 * 1 * (1-θ0)^2 = (1-θ1) / (1-θ0)
>
> = (1-3/4)^2 / (1-1/2)^2 =  (1/4)^2 / (1/2)^2 = **1/4**
>
> f(1|θ1)/f(1|θ0) = (2 choose 1) θ1^1 (1-θ1)^(2-1) / (2 choose 1) θ0^1 (1-θ0)^(2-1)
>
> = (θ1/θ0) (1-θ1)/(1-θ0) = (3/4 / 1/2) (1 - 3/4) / (1 - 1/2) = (3/2) (1/4) / (1/2) =
> (3/2)(1/2) = **3/4**
>
> f(2|θ1)/f(2|θ0) = (2 choose 2) θ1^2 (1-θ1)^(2-2) / (2 choose 2) θ0^2 (1-θ0)^(2-2)
>
> = (θ1/θ0)^2 = (3/4 / 1/2)^2 = (3/2)^2 = **9/4**
>
> ====
>
> Rồi thế thì,
>
> Cái ý thứ nhất trong bổ đề thực chất là define cái test rule, cũng chính là tạo ra
> cách chia sample space thành R và Rc
>
> reject kf0(x|θ0) < f(x|θ1) for some k > 0 ⇔ k < f(x|θ1) / f(x|θ0)
>
> Mà với x = 0, tỉ số này là **1/4**, x = 1, là **3/4** và x = 2 là **9/4**
>
> Vậy thì với các giá trị k khác nhau, ta sẽ tạo ra các ngưỡng / các cách chia R,
> Rc khác nhau:
>
> i) Nếu **k < 1/4**
>
> ⇨ k < f(x|θ1) / f(x|θ0) **VỚI MỌI x** = 0,1,2
>
> ⇨ test dùng rule {reject H0 khi k < f(x|θ1) / f(x|θ0)} sẽ reject H0 VỚI MỌI x = 0,
> 1,2
>
> CŨNG CHÍNH LÀ X ∈ R ∀x=0,1,2
>
> CŨNG CHÍNH LÀ R = SUPPORT X
>
> Khi đó, P_θ0(X ∈ R) DĨ NHIÊN LÀ 1
>
> Kết luận nếu k < 1/4 thì cái test có rule:
>
> reject H0 nếu k < f(x|θ1) / f(x|θ0) ∀x=1,2,3,
>
> HOẶC NÓI ĐƠN GIẢN HƠN LÀ
>
> CÁI TEST MÀ REJECT H0 VỚI MỌI X,
>
> HAY
>
> CÁI TEST LUÔN REJECT H0
>
> sẽ là **UMP LEVEL 1 test.**
>
> Và có thể thấy, nếu cái test có rule như vậy thì khi H0 đáng ra phải được
> accept (θ ∈ Θ0) thì cái test này chắc chắn sẽ mắc lỗi loại I, hay, xác suất mắc
> lỗi loại I là 100%. Thì nếu soi chiếu với định nghĩa của size α test, là test mà
> sup_θ∈Θ0 P_θ(X ∈ R) = α thì ta sẽ thấy khớp.
>
> ii) Nếu 1/4 < k < 3/4:
>
> ⇨ k < f(x|θ1) / f(x|θ0) với mọi x = 1,2
>
> ⇨ test reject H0 khi k < f(x|θ1) / f(x|θ0) sẽ là test reject H0 KHI X = 1,2
>
> CŨNG LÀ X ∈ R ∀x=1,2, hay R = {1, 2}
>
> P_θ0(X ∈ R) = P_θ0(X = 1 or X = 2) = P_θ0(X = 1) + P_θ0(X = 2)
>
> = (2 choose 1) θ0^1 (1- θ0)^(2-1) + (2 choose 2) θ0^2 (1-θ0)^(2-2)
>
> = 2 θ0 (1-θ0) + θ0^2
>
> = 2 (1/2) (1-1/2) + (1/2)^2
>
> = 1/2 + 1/4 = 3/4
>
> Kết luận, nếu 1/4 < k < 3/4 thì cái test có rule reject H0 nếu x = 1,2 sẽ là 
> **UMP level 3/4 test.**
>
>
>
> iii) nếu 3/4 < k < 9/4 thì k < f(x|θ1)/f(x|θ0) sẽ xảy ra khi x = 2 ⇔ X ∈ R khi X = 2
>
> P_θ0(X ∈ R) = P_θ0(X = 2) = (2 choose 2) θ0^2 (1- θ0)^(2-2) = 1/4.
>
> Kết luận, nếu 3/4 < k < 9/4 thì test có rule là reject H0 khi X = 2 sẽ là UMP level
> 1/4 test
>
> iv) nếu 9/4 < k thì k < f(x|θ1)/f(x|θ0) sẽ không xảy ra với x nào ⇨ X ∈ R = rỗng
>
> hay nói cách khác, test này luôn accept H0.
>
> ⇨ P_θ0(X ∈ R) = 0
>
> Kết luận: nếu 9/4 < k thì test reject H0 "với không có x nào" / cũng là test luôn
> accept H0 ∀x sẽ là UMP level 0 test.
>
> Và đây là loại test mà khi H0 nên được accept, thì nó chắc chắn sẽ không mắc
> lỗi loại I, hay xác suất mắc lỗi loại I là = 0
>
> ====
>
> Nếu k = 3/4 thì k < f(x|θ1) / f(x|θ0) với x = 2, cũng là R = {2}
>
> P_θ0(X ∈ R) = P_θ0(X = 2) = 1/4
>
> Tức là k = 3/4 thì test reject H0 khi X = 2 (vì tại X = 2 thì k < tỉ lệ f(x|θ1)/f(x|θ0) =
> 9/4
>
> Và test cũng sẽ accept H0 tại X = 0 (vì tại X = 0, tỉ lệ này = 1/4 < 3/4)
>
> Nhưng nếu X = 1 thì ta sẽ **ko biết phải reject hay accept H0** vì tại đó tỉ lệ = 3/4
> không lớn hơn cũng không bé hơn k.
>
> Nhưng **nếu ta accept H0 khi X = 1**, thì lúc này R = {2} ⇨ ta **vẫn có UMP level
> 1/4 test**
> Nếu r**eject H0 khi X = 1**, thì lúc này R = {1,2} ⇨**ta sẽ có UMP level 3/4 test.**

<br>

<a id="node-716"></a>

<p align="center"><kbd><img src="assets/c55c566fe52169ee8bbc6ed0de84041483951773.png" width="100%"></kbd></p>

🔗 **Related:** [3.5 LOCATION AND SCALE FAMILIES](35_location_and_scale_families.md#node-202)

🔗 **Related:** [8.3 METHODS OF EVALUATING TEST](83_methods_of_evaluating_test.md#node-713)

> [!NOTE]
> Qua ví dụ này, X1,...Xn là random sample ~ n(θ, σ^2) với σ^2 đã biết.
>
> Sample mean Xbar là sufficient statist cho θ (cái này những chapter trước đã biết
> rồi)
>
> Ta mới xét bài toán kiểm tra gỉa thuyết giữa H0: θ = θ0, vs H1: θ = θ1 với θ0 > θ1.
>
> Dừng lại chút ôn lại bổ đề 8.3.13, đại ý nó nói rằng: cái test có rule như sau:
> reject H0 nếu g(t|θ1) > kg(t|θ0) và accept H0 nếu ngược lại. Và có α = P_θ0(T ∈
> S) thì chính là một UMP level α test.
>
> Ở đây ta xem thử g(t|θ1)/g(t|θ0) > k sẽ trông như thế nào:
>
> g(t|θ) là pdf của T, ở đây là T(X) = Xbar.
>
> Ở đây Xbar, như đã biết, có distribution là normal(μ, σ^2/n), hay  normal(θ, σ^2/n)
>
> ⇨ g(t|θ) = 1/√(2πσ^2/n) exp[-(t-θ)^2/(2σ^2/n)]
>
> = √n/√(2πσ^2) exp[-n(t-θ)^2/2σ^2]
>
> ⇨ g(t|θ1) / g(t|θ0)
>
> = √n/√(2πσ^2) exp[-n(t-θ1)^2/2σ^2] / √n/√(2πσ^2) exp[-n(t-θ0)^2/2σ^2]
>
> = exp[-n(t-θ1)^2/2σ^2] / exp[-n(t-θ0)^2/2σ^2]
>
> = exp[-n(t-θ1)^2/2σ^2 + n(t-θ0)^2/2σ^2]
>
> = exp[-n((t-θ1)^2 - (t-θ0)^2) / 2σ^2]
>
> ⇨ k < g(t|θ1) / g(t|θ0)
>
> ⇔ k < exp[-n[(t-θ1)^2 - (t-θ0)^2] / 2σ^2]
>
> ⇔ log k < -n((t-θ1)^2 - (t-θ0)^2) / 2σ^2
>
> ⇔ 2σ^2 log k < -n((t-θ1)^2 - (t-θ0)^2)
>
> ⇔ 2σ^2 (log k) / n < -((t-θ1)^2 - (t-θ0)^2)
>
> ⇔ 2σ^2 (log k) / n < -(t^2+θ1^2-2θ1t -(t^2+θ0^2-2θ0t))
>
> ⇔ 2σ^2 (log k) / n < -(t^2+θ1^2-2θ1t -t^2-θ0^2+2θ0t)
>
> ⇔ 2σ^2 (log k) / n < -t^2-θ1^2+2θ1t +t^2+θ0^2-2θ0t
>
> ⇔ 2σ^2 (log k) / n < -θ1^2+2θ1t+θ0^2-2θ0t
>
> ⇔ 2σ^2 (log k) / n < θ0^2-θ1^2 + 2θ1t - 2θ0t
>
> ⇔ 2σ^2 (log k) / n < θ0^2-θ1^2 + 2t(θ1 - θ0)
>
> ⇔ 2σ^2 (log k) / n  - θ0^2 + θ1^2 < 2t(θ1 - θ0)
>
> Vì θ0 > θ1 ⇨ θ1 - θ0 < 0
>
> .. ⇔ [2σ^2 (log k) / n  - θ0^2 + θ1^2] / 2(θ1 - θ0) > t
>
> Hay xbar < [2σ^2 (log k) / n  - θ0^2 + θ1^2] / 2(θ1 - θ0) như sách viết.
>
> Rồi. Thế thì như vậy là sao?
>
> Trả lời: Như vậy có nghĩa là, cái rule: reject H0 khi kg(t|θ0) < g(t|θ1) hay cũng là
> reject H0 khi k < g(t|θ1) / g(t|θ0) trở thành:
>
> reject H0 khi xbar < [2σ^2 (log k) / n  - θ0^2 + θ1^2] / 2(θ1 - θ0), đặt là c(k) là
> constant có giá trị khác nhay khi k thay đổi
>
> Và cũng chính là rejection region S = (-inf, c)
>
> Với k chạy từ 0 → inf thì
>
> ⇨ log k chạy từ -inf → inf
>
> ⇨ [2σ^2 (log k) / n  - θ0^2 + θ1^2] chạy từ -inf → inf
>
> ⇨ c = [2σ^2 (log k) / n  - θ0^2 + θ1^2] / 2(θ1 - θ0) chạy từ inf → -inf
>
> Vậy thì Hệ quả 8.3.13 nói cho ta biết rằng
>
> cái test reject H0 khi k < g(t|θ1) / g(t|θ0) và accept H1 khi k > g(t|θ1) / g(t|θ0)
>
> đồng thời với α = P_θ0(T ∈ S) chính là UMP level α test.
>
> Thì áp dụng vào đây, cái test mà có rule là reject H0 khi Xbar < c và đạt α =
> P_θ0(Xbar < c) cũng sẽ là một UMP level α test.
>
> Để rồi nếu như ta có α cho trước. Thì ta sẽ tính ra c:
>
> α = P_θ0(T < c)
>
> hay P_θ0(T < c) = α với T ~ n(θ0, σ^2/n)
>
> Đến đây lặp lại lập luận:
>
> T < c ⇔ T - θ0 < c - θ0 ⇔ (T - θ0)/(σ/√n) < (c - θ0)/(σ/√n)
>
> ⇨ P_θ0(T < c) = P_θ0(Z < (c - θ0)/(σ/√n)) với Z = (T - θ0)/(σ/√n)
>
> (vì bản chất P_θ0(T < c) chỉ là P({s∈Ω: T(s) < c})
>
> Mà ta có T < c ⇔ Z = (T - θ0)/(σ/√n) < (c - θ0)/(σ/√n)
>
> ⇨ T(s) < c ⇔ Z(s) = (T(s) - θ0)/(σ/√n) < (c - θ0)/(σ/√n)
>
> ⇨  P({s∈Ω: T(s) < c}) =  P({s∈Ω: Z(s) = (T(s) - θ0)/(σ/√n) < (c - θ0)/(σ/√n)})
>
> = P(Z < (c - θ0)/(σ/√n))
>
> Rồi, mà T là một n(θ, σ^2/n), và và normal là một location scale family có location
> chính là mean, và scale chính là standard deviation.
>
> Nên theo một theorem đã học ta biết rằng (T - location) / scale = (T - θ)/(σ/√n)
> phải là một random variable thuộc standard member của family. Tức là,
> distribution của Z = (T - θ)/(σ/√n) chính là  thành viên của family ứng với location
> 0, scale 1. Và như đã nói, với normal thì location = mean, scale = std nên ta kết
> luận Z ~ n(0,1)
>
> Và với Z ~ n(0,1) thì
>
> P(Z < (c - θ0)/(σ/√n)) = Φ((c - θ0)/(σ/√n))
>
> Vậy phương trình cần giải là
>
> P(Z < (c - θ0)/(σ/√n)) = α
>
> ⇔ (c - θ0)/(σ/√n) = -z_α
>
> (Đã học cái vụ này z_α là con số mà P(Z > z_α) = α, nói dễ hiểu z_α là con số mà
> phần diện tích bên phải = α
>
> từ đó nhờ tính đối xứng -z_α là con số mà P(Z < -z_α), tức phần diện tích bên trái
> = α)
>
> ⇔ c - θ0 = -z_α(σ/√n)
>
> ⇔ c = -z_α(σ/√n) + θ0. XONG!
>
> Và có nghĩa là, cái test UMP level α test sẽ là cái mà có rule là reject H0 nếu xbar
> < c  với c = -z_α(σ/√n) + θ0

<br>

<a id="node-717"></a>

<p align="center"><kbd><img src="assets/d2e47e8731f0993f69d1dd35d2347bb7f75b4ae6.png" width="100%"></kbd></p>

> [!NOTE]
> Đoạn này đại ý nói là cái bổ đề Neyman-Pearson chỉ nói về các
> hypothesis đơn giản. Là sao, là vì ta nhớ nó xét bối cảnh ta có H0: θ = θ0
> vs H1: θ = θ1 và hai hypothesis này, gọi là đơn giản, vì subset Θ0 và Θ0c
> chỉ là tập có một phần tử.
>
> Nhưng thực tế, ta sẽ gặp hypothesis mà state / tuyên bố rằng θ ∈ subset
> có vô số phần tử. Ví dụ H: θ ≥ θ0, hay H: θ < θ0 (H ko ghi 0 hay 1, ám chỉ
> là giả thuyết chung chung). Và đây gọi là **ONE-SIZED HYPOTHESIS.**
>
> Hoặc là H: θ ≠ θ0, gọi là **TWO-SIZED HYPOTHESIS**.
>
> Thế thì. Những hypothesis phức tạp này gọi là **COMPOSITE** hypothesis.
>
> Rồi. Nhớ lại định nghĩa của Uniformly Most Powerful level α test, hay nói
> khái quát hơn là Unform Most Powerful class C test (nôm na là thằng
> mạnh nhất của đám test thuộc lớp C) được định nghĩa là thằng có power
> function β(θ) lớn  hơn mọi powerful β'(θ) của mọi thằng khác trong class
> với mọi θ ∈ Θ0c.
>
> Nghĩa là, nếu lấy một thằng bất kì trong class C, và gọi power function của
> nó là β'(θ) thì nếu 1 thằng trong class C có β(θ) ≥ β(θ) với mọi θ ∈ Θ0c thì
> nó chính là thằng mạnh nhất.
>
> Như vậy, đại ý ở đây nói là, với simple hypothesis, Θ0c như đã nói chỉ
> chứa có mỗi một cái à.
>
> Nên với case này, để chứ minh một test là trùm chỉ việc chứng minh β của
> nó lớn hơn mấy thằng khác tại phần tử θ duy nhất của Θ0c
>
> Nhưng qua case phức tạp, thì ta phải chứng minh nó lớn hơn β của mấy
> thằng khác **TẠI MỌI θ TRONG Θ0c**. ví dụ, với β(θ) ≥ β'(θ) ∀ θ > θ0
>
> Do đó, ta sẽ cần một công cụ mới, cho phép deal với bài toán này.

<br>

<a id="node-718"></a>

<p align="center"><kbd><img src="assets/5a9211e5e5d4a9b4e18008b1c5b06cdee1cca4ea.png" width="100%"></kbd></p>

> [!NOTE]
> Một định nghĩa quan trọng chuẩn bị mở đường cho theorem tiếp theo.
>
> Đại khái là định nghiã về một tính chất được gọi là tính đơn điệu của 
> tỉ số likelihood. (monotone likelihood ratio)
>
> Đó là: Một HỌ CÁC PDF/PMF {g(t|θ): θ ∈ Θ} của một univariate random
> variable T với tham số θ giá trị thực, SẼ ĐƯỢC GỌI LÀ MONTONE
> LIKELIHOOD RATION nếu như với mọi θ2 > θ1 thì tỉ số giữa:
>
> g(t|θ2) / g(t|θ1), là một hàm monotone của t trong tập {t: g(t|θ1) > 0 or
> g(t|θ2) > 0}
>
> Gs nói thêm rằng các họ pdf phổ biến như normal, Poison, Binomial hoặc
> nói chung là họ expontial có dạng khái quát g(t|θ) = h(t)c(θ)exp(w(θ)t) với
> w(θ) là hàm non-decreasing thì đều là có tính chất MLR này
>
> Nói chung, định nghĩa thì phải nhớ thôi. Không có gì để nói nhiều

<br>

<a id="node-719"></a>

<p align="center"><kbd><img src="assets/2bb616690be34e9351354701d2e5c14b83ce1ccf.png" width="100%"></kbd></p>

> [!NOTE]
> Theorem Karlin - Rubin, xét test giữa hai hypothesis H0: θ ≤ θ0 vs H1: θ >
> θ0 Cho rằng T là sufficient statistic của θ, và họ pdf/pmf của t: {g(t|θ): θ ∈
> Θ} là một MLR. Thì theorem này nói rằng:
>
> Cái test có rule: reject H0 khi và chỉ khi T > t0 sẽ là một UMP level α test
> với α = P_θ0(T > t0)
>
> Chứng minh đại khái là vầy.
>
> Đầu tiên cần nhắc lại cho nhớ không thừa, bổ đề Neyman-Pearson cho ta
> công cụ để kết luận rằng trong một bài toán kiểm định giữa hai giả thuyết
> đơn giản H0: θ = θ0 vs H1: θ = θ1, nếu một cái test có
>
> Điều kiện thứ nhất là nó **có rule CÓ DẠNG SAU**:
>
> Reject H0 nếu kf(**x**|θ0) < f(**x**|θ1) và accept H0 nếu kf(**x**|θ0) >
> f(**x**|θ1) với k là số dương nào đó.
>
> (Mà đây, ta phải hiểu, cũng chính là, cái test này **dùng test statistic là
> likelihood ratio**: f(x|θ1) / f(x|θ0) và so với threshold k là số dương)
>
> Và điều kiện thứ hai, lại **LÀ MỘT SIZE α TEST**, thể hiện qua: P_θ0(**X**
> ∈ R) = α.
>
> Thì N-P cho biết đích thị **nó chính là thằng mạnh nhất trong đám level α
> test**:
>
> **UMP level α test**.
>
> Rồi, **hệ quả tiếp theo** (Corollary 8.3.13) cũng **cho phép ta phán một
> thằng (test) có phải vua** hay không **thông qua một sufficient statistic T**.
> Cụ thể là nếu cái test có:
>
> Điều kiện thứ nhất, có rule có dạng:
>
> Reject H0 nếu kg(t|θ0) < g(t|θ1) và accept H0 nếu kg(t|θ0) > g(t|θ1) với k là
> số dương nào đó
>
> (tương tự, cái này cũng chính là nói test statistic của cái test này là
> likelihood ratio:
>
> g(t|θ1) / g(t|θ0) (= L(θ1|t) | L(θ0|t)) và cái rule là so nó với một threshold k
> dương)
>
> Điều kiện thứ hai: Test phải là size α test, thể hiện qua P_θ0(**X** ∈ R)
> (Cũng là P_θ0(T ∈ S) = α
>
> thì khi đó đích thị nó là mạnh nhất trong đám level α test.
>
> VẬY CÓ THỂ TA CHƯA ĐỂ Ý RẰNG CÁI Ý MÀ BỔ ĐỀ NEYMAN NÓI LÀ:
>
> **MIỄN LÀ trong bài toán simple-simple,** mà ta có một cái **SIZE α
> TEST** mà **có cái rule có dạng REJECT H0 DỰA VÀO TỈ SỐ
> LIKELIHOOD so với một số dương**
>
> THÌ CÓ THỂ NÓI NGAY nó chính là cái UMP level α test.
>
> Ghim ý này ở đây để quay lại bài toán này. Ta muốn **chứng minh cái test
> có rule T > t0 nào đó**, mà **α = P_θ0(T > t0)** thì **nó là UMP level α test
> của bài toán kiểm tra giữa H0: θ ≤ θ0 vs H1: θ0 > θ**.
>
> Thế thì chiến lược là, ta dựa vào Neyman-Pearson, và nhờ tính chất
> monotone likelihood ratio:
>
> Nhớ rằng, N-P Lemma cho ta **công cụ để tuyên bố UMP level α test** của
> một test **trong bài toán kiểm tra giữa hai simple hypothesis**: H0: θ=θ0 vs
> H1: θ=θ1.
>
> Nhưng để **tuyên bố test đang xét là vua trong bài toán kiểm tra mà
> hypothesis là phức tạp (composite)** với **H1 là θ**∈**(θ0, inf)**, thì ta sẽ
> dùng cách sau đây: **Tách thành vô số bài toán đơn giản**:
>
> **H'0: θ = θ0** vs **H'1: θ = θ'** với **θ'**∈**(θ0, inf)**
>
> Để rồi nếu trong bài toán với θ' ∈ (θ0, inf) bất kì này, **test đang xét là UMP
> level α test**. (Việc này ta sẽ nhờ Neyman-Pearson lemma)
>
> Mà điều này có nghĩa là: Trong các bài toán simple H'0 vs H'1, thì **khi H'1
> nên được accept** (**tức là khi θ thật sự = θ')**, **thì test đang xét là cái sẽ
> cho ra xác suất accept H'1 cao nhất**, **cũng là power β(θ) cao nhất**,
> **cũng là có xác suất Type II error thấp nhất.**
>
> Thế rồi, vì **θ' được chọn là số ngẫu nhiên** **> θ0**. Và logic thế này:
> **Với θ' bất kì** thì **khi θ bằng θ'**, thì **test này đều là test có xác suất
> accept điều này cao nhất**. **VẬY THÌ DĨ NHIÊN**, **NẾU XÉT TRONG
> BÀI TOÁN MÀ H1: θ > θ0 vs H0: θ ≤ θ0**, thì **KHI THẬT SỰ θ > θ0**, thì
> **test đang xét cũng sẽ là cái có xác suất accept điều đó cao nhất**.
>
> Nếu chưa hiểu thì có thể lấy analogy: Ta muốn (test) xem vận động viên
> của mình có mạnh hơn mọi vận động viên khác trong cuộc thi sau: người
> mạnh nhất ở tất cả các mức tạ từ θ0 trở lên.
>
> Thế thì bằng cách cho thấy **với mọi mức tạ θ' > θ0**, thì**vận động viên
> của mình  đều là người thắng**(thắng vòng thi ở mức tạ θ', tức là bài toán
> simple vs simple H'0 θ = θ0 vs H'1 θ = θ'), thì**suy ra nó cũng thắng trong
> cuộc thi này**  (H1: θ > θ0 vs H0: θ ≤ θ0)
>
> Vậy xét bài toán simple vs simple H'0 θ = θ0 vs H'1 θ = θ'. Để dùng được
> N-P giúp tuyên bố test đang xét là mạnh nhất. Nó phải thỏa hai điều kiện
> đã nói trên. Xét điều kiện sau trước: Nó phải là size α test.
>
> Vậy nó có phải là size α test không?
>
> Nhớ lại, test đang xét là test gì (có rule gì): reject H0 khi và chỉ khi T > t0
> với t0 bất kì miễn là α = P_θ0(T > t0). À vậy rejection region cuả nó là: S =
> {t: t > t0},
>
> Theo định nghĩa của size α test, test phải có phải có sup_θ∈Θ0 P(X ∈ R) =
> α, hay ở đây chính là phải có sup_θ=θ0 P_θ(T ∈ S) = α
>
> Điều này tương đương: P_θ0(T ∈ S) = α
>
> ⇔ P_θ0(T > t0) = α.
>
> Vậy câu hỏi là test đang xét có điều này không? → Câu trả lời là có, đó là
> thứ đề bài cho. Vậy nó là size α test (của bài toán H'0 vs H'1)
>
> Tiếp, ta cần xem thử nó có cái rule có dạng là dùng likelihood ratio để so
> với một threshold dương không?
>
> Again, test đang xét có rule là gì? ⇨ Reject H0 khi T > t0.
>
> Đến đây ta mới nhờ tới tính chất Monotone - Likelihood - Ratio MLR: Nhớ
> lại, nó nói rằng: nếu họ các pdf/pmf có tính chất này thì:
>
> với mọi θ2 > θ1 thì g(t|θ2) / g(t|θ1) là hàm monotone theo t. trong tập {t:
> g(t|θ1) > 0 hoặc g(t|θ2) > 0}.
>
> Như vậy: thì đại ý là nhờ đề bài cho họ pdf của T có tính chất MLR nên:
>
> T > t0 sẽ TƯƠNG ĐƯƠNG VỚI g(t|θ2) / g(t|θ1) > k' nào đó.
>
> CÓ NGHĨA LÀ, TỪ ĐÓ, CÁI RULE CỦA TEST NÀY ĐÃ TRỞ THÀNH VIỆC
> SO LIKELIHOOD RATIO VỚI MỘT THRESHOLD K' DƯƠNG NHƯ MONG
> MUỐN RỒI.
>
> Như vậy, theo N-P, trong bài toán H'0: θ = θ0 vs H'1: θ = θ' thì test đang xét
> là thằng mạnh nhất trong đám level α test.
>
> Và như vậy ta, theo lập luận trong chiến lược ở trên, ta có thể kết luận test
> đang xét là test có đặc điểm sau: Đối với bài toán gốc:
>
> Khi H1: θ > θ0 nên được accept, thì nó chính là test có xác suất accept H1
> cao nhất, cũng là test có xác suất mắc Type II error thấp nhất. Hay nói
> cách khác, khi H1 nên được accept, θ ∈ Θ0c thì power function β(θ) của nó
> > power function β'(θ) của level α test bất kì.
>
> Nhưng lưu ý, đến đây chưa xong để kết luận nó là UMP level α test của bài
> toán gốc.  Vì sao. Vì ta chưa chứng minh được nó là một size α test của
> bài toàn composite.
>
> Nên nhớ, trong loại "vòng đấu" simple vs simple, H'0 θ=θ0 vs H'1: θ=θ' thì
> quả thật nó là size α test do đề bài cho, nên nó thỏa điều kiện 2 của N-P,
> và nhờ tính MLR thì ta show ra nó thỏa điều kiện 1. Nên dựa vào N-P, ta
> kết luận nó là UMP level α test trong bài toán simple. Nhưng đó chỉ là bài
> toán simple.
>
> Rồi bằng cách lập luận về tình huống ta chọn θ' ngẫu nhiên từ (θ0, inf) để
> có bài toán simple ngẫu nhiên mà test đang xét đều thắng, nên mới dẫn
> đến kết luận là trong  cái bài toán composite, nó cũng là cái có tính chất
> **NẾU H1 NÊN ĐƯỢC ACCEPT, THÌ NÓ CHÍNH LÀ CÁI CÓ XÁC SUẤT
> ACCEPT H1 CAO NHẤT, CŨNG LÀ CÓ POWER CAO NHẤT TRONG HẾT
> THẢY ĐÁM LEVEL α test.**
>
> NHƯNG LƯU Ý, ĐÂY LÀ KẾT LUẬN THUẦN TÚY LÀ TỪ LẬP LUẬN "
> chọn θ' ngẫu  nhiên". Và tới đây, ta chỉ đang có nhiêu đó, tức là biết rằng
> trong bài toán composite thì khi H1 nên được accept, thì nó là cái có Type
> II error nhỏ nhất.
>
> **ĐỂ KẾT LUẬN NÓ LÀ UMP LEVEL α CỦA BÀI TOÁN COMPOSITE. TA
> CÒN PHẢI LÀM MỘT VIỆC NỮA:
>
> ĐÓ LÀ CHỨNG MINH RẰNG KHI H0 NÊN ĐƯỢC ACCEPT, THÌ NÓ
> CŨNG LÀ CÁI CÓ XÁC SUẤT MẮC LỖI LOẠI I KHÔNG QUÁ α. NÓI
> CÁCH KHÁC, TA PHẢI  CHỨNG MINH NÓ CŨNG LÀ MỘT LEVEL Α
> TEST.**
>
> Vậy, phải chứng minh sup_θ≤θ0 P_θ(T > t0) ≤ α
>
> Cũng là sup_θ≤θ0 β(θ) ≤ α
>
> Again, dựa vào MLR, ta sẽ có thể chứng minh β function non-decreasing.
>
> ⇨  sup_θ≤θ0 β(θ) ≤ α ⇔ β(θ0) ≤ α
>
> ⇔ P_θ0(T > t0) ≤ α, Mà cái này thì vì đề bài cho P_θ0(T > t0) = α nên nó dĩ
> nhiên đã thỏa điều kiện.
>
> Có nghĩa là trong trường hợp này, nó là cái Size α test của bài toán
> composite luôn, (nên dĩ nhiên cũng là một Level α test của bài toán
> composite).
>
> Như vậy cuối cùng tổng kết lại: Ta đã chứng minh rằng **với bài toán
> composite, khi H1 nên được accept thì test đang xét là cái có power cao
> nhất**. Và sau đó ta chứng minh nó**cũng là một level α test của bài toán
> composite**. Nên theo định nghĩa 8.3.11 , thì nó chính là UMP level α test
> của bài toán composite.

<br>

