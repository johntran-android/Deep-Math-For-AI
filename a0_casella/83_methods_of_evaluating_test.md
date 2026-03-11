# 8.3 Methods Of Evaluating Test

📊 **Progress:** `7` Notes | `13` Screenshots

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

