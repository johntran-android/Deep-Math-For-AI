# 10.1 Asymtotic Evaluation - Point Estimation

📊 **Progress:** `17` Notes | `20` Screenshots

---

<a id="node-848"></a>
## 10.1 Point Estimation

<br>

<a id="node-849"></a>

<p align="center"><kbd><img src="assets/eed3dc9dc2d7bb4ca79c376e49e19bf28ce745b7.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là bữa giờ ta xét các hành vi của các quy trình suy luận trong
> bối cảnh là finite-sample, tức là mẫu có số lượng hữu hạn. Chapter
> này sẽ xem xét tính asymptotic -  tính chất mô tả hành vi của quy trình
> khi kích thước mẫu tăng lên infinite.
>
> Ta sẽ đánh giá tính chất này của cả 3 quy trình suy luận chính: point
> estimation, hypothesis testing và interval estimation. Đặc biệt tập
> trung vào các phương pháp liên quan đến maximum likelihood

<br>

<a id="node-850"></a>

<p align="center"><kbd><img src="assets/578b5873903a6d43f4a0103016bcaa888bf9e3c9.png" width="100%"></kbd></p>

> [!NOTE]
> Đại ý là, gs nói sơ về giá trị của cái này là nó khiến việc tính toán trở nên
> đơn giản hóa khi ta cho phép số lượng mẫu tăng lên indefinite.
>
> Có những cách đánh giá trở nên bất khả thi khi xét trong bối cảnh
> finite-sample nhưng trở nên khả thi khi xét trong bối cảnh infinte bao gồm
> các technique nổi tiếng như bootstrap và M-estimation.

<br>

<a id="node-851"></a>

<p align="center"><kbd><img src="assets/ffb6bcb7d331819d71c5853ef4d216ad2a52d8c5.png" width="100%"></kbd></p>

> [!NOTE]
> Xét vấn đề đánh giá tiệm cận với phương pháp suy luận thuộc loại point 
> estimation. Đầu tiên nói về tính chất nhất quán (consistency)
>
> Thì đại ý là, cái này nó nền tảng đến nỗi nếu một estimator mà inconstent
> thì có thể phải đặt câu hỏi là có đáng để dùng không.
>
> Thế thì đầu tiên, gs nói trong bối cảnh đánh giá tiệm cận, thật ta ta nên
> hiểu là ta sẽ  **XÉT MỘT CHUỖI CÁC ESTIMATOR**, **CHỨ KHÔNG PHẢI
> LÀ MỘT CÁI ĐƠN LẺ DÙ CHO KHI NÓI THÌ TA NÓI "CONSISTENT 
> ESTIMATOR**" trông có vẻ như là tính chất của một estimator đơn lẻ.
>
> Tức là hình dung, với sample X1,X2,...Xn thì kiểu như ta dùng cùng một
> quy trình inference để xây dựng một chuỗi các point estimator với kích
> thước mẫu tăng dần. W1(X1), W2(X1,X2),....Wn(X1,...Xn)
>
> ví dụ, lấy Xbar đi (nó là point estimator cho population mean như đã biết)
>
> thì ta có Xbar1(X1) = X1, Xbar2(X1,X2) = (X1+X2)/2, Xbar_n(X1,..Xn)
> = (Σi=1:n Xi) / n
>
> Mình ghi Xbar1(X1) là hoàn toàn hợp lệ, vì gs Casella trong mấy chương
> trước đã nói, Xbar, hay S^2 thật ra chỉ là ghi cho gọn, ghi rõ phải là Xbar(**X**)
> hay S^2(**X**) để thể hiện nó là function của sample **X**

<br>

<a id="node-852"></a>

<p align="center"><kbd><img src="assets/c9609d8dbe7a347b419b9704db2d16b30389937b.png" width="100%"></kbd></p>

> [!NOTE]
> Ta được học định nghĩa của cái gọi là một chuỗi các estimator có tính nhất 
> quán (consistent) đó là nếu như Wn thỏa: lim n → inf P_θ(|Wn - θ| < ε) = 1.
> Mang ý nghĩa là khi kích thước mẫu tăng lên vô hạn thì xác suất mà estimator
> khác với θ sẽ cực kì nhỏ, hay, xác suất estimator sẽ có giá trị chính xác với θ 
> là cực lớn.
>
> Dừng lại chút xíu, vì sao P_θ(|Wn - θ| < ε) lại là hàm theo θ?
>
> À, đơn giản là vì Wn ở đây là estimator của θ, theo định nghĩa, là một function 
> của sample **X** = (X1,...Xn), cũng còn gọi là một statistic. Và vì vậy, nó là một
> random variable, có distribution sẽ phụ thuộc θ luôn. Nên xác suất của |Wn - θ|
> < ε dĩ nhiên là xác suất của một event liên quan đến rv Wn có distribution
> phụ thuộc θ nên đương nhiên nó phải phụ thuộc θ. Đó mới là lí do có chữ θ 
> ở dưới, chứ ko phải là vì θ xuất hiện trong |Wn - θ|

<br>

<a id="node-853"></a>

<p align="center"><kbd><img src="assets/d577fc03e3a54e9d526c85264d9c6f78bd9bd73f.png" width="100%"></kbd></p>

🔗 **Related:** [5.5 CONVERGENCE CONCEPTS](55_convergence_concepts.md#node-392)

> [!NOTE]
> Nhờ hiểu bản chất chữ θ ở dưới chân chữ P (P_θ(..)) nên ta hiểu đoạn này
> như vầy:
>
> Đại ý là trong định nghĩa 5.5.1, có nói về khái niệm gọi là CONVERGENCE
> IN PROBABILITY: như vầy: Chuỗi các random variable X1,...Xn được gọi là 
> converge in probability to X nếu như lim n → inf P(|Xn - X| < ε) = 1.
>
> Nhưng ở đây, mình hiểu đoạn này nói vầy:
>
> Khi mình nói chuỗi X1,...Xn hội tụ xác suất về X, thì thực ra chúng ta đang
> xét trong một distribution f(x|θ) với θ mang giá trị nào đó.
>
> Còn khi nói chuỗi W1, ...Wn hội tụ xác suất về θ, thì ta đang nói trong bất kì
> một θ nào.
>
> Có nghĩa là, dù giá trị thực sự của θ là bao nhiêu, thì chuỗi các estimator
> W1,..Wn (nhắc lại, là các point estimator được xây dựng từ cùng một "công
> thức", chỉ là với mẫu X có số lượng tăng dần đến infinite) cũng phải hội
> tụ về đó
>
> Thành ra trong bối cảnh của chương 10 này, kiểu như với mỗi θ ta sẽ có
> một thành viên cụ thể trong một họ các distribution index bởi θ. Và trong
> họ nào, thì cũng xảy ra hiện tượng W1,...Wn converge về θ hết.

<br>

<a id="node-854"></a>

<p align="center"><kbd><img src="assets/2305cd1522b6c8afa8998f8716eb4b2287baa306.png" width="100%"></kbd></p>

> [!NOTE]
> Qua ví dụ này, cho X1,X2,...iid ~ n(θ, 1) và xét chuỗi các sample mean của 
> random sample size n: Xbar_n = (Σi Xi) / n.
>
> Còn nhớ, ta đã chứng minh, sample mean Xbar của random sample X1,...
> Xn ~ normal(μ, σ^2) sẽ có distribution normal(μ, σ^2/n). Nên ở đây Xbar_n
> sẽ là random variable ~ normal(θ, 1/n)
>
> Ôn lại mấy bài trước chút xíu: Ta đang bàn về tính consistency của một
> point estimator. Theo định nghĩa là khi khi kích thước mẫu tăng lên đến vô hạn 
> thì ta có một chuỗi các estimator (mỗi cái dựa trên mẫu size tương ứng)
> sẽ converge in probability về θ thể hiện bởi lim n → inf P(|Wn - θ| < ε) = 1
>
> Vậy ở đây ta xét xác suất P_θ(|Xbar_n - θ| < ε).
>
> ⇨ P_θ(|Xbar_n - θ| < ε) = P_θ(-ε < Xbar_n - θ < ε)
>
> = P_θ(-ε√n < Xbar_n - θ/(1/√n) < ε√n)
>
> Ở trên ta đã nói Xbar_n ~ normal(θ, 1/n) thì theo location scale theorem, 
> (Xbar_n - θ)/(1/√n) sẽ là rv ~ normal(0, 1)
>
> ⇨ P_θ(-ε√n < Z < ε√n), với Z = Xbar_n - θ/(1/√n), là normal(0,1)
>
> Vậy thì tới đây dễ thấy khi n → inf, thì P_θ(-ε√n < Z < ε√n) → P_θ(-inf < Z < inf) = 1
>
> Vậy theo định nghĩa Xbar là consistent estimator của θ

<br>

<a id="node-855"></a>

<p align="center"><kbd><img src="assets/415f5d53df86d3159fec16789ee527d032057a3c.png" width="100%"></kbd></p>

🔗 **Related:** [3.6 INEQUALITIES](36_inequalities.md#node-207)

> [!NOTE]
> Thế thì đại ý là gs nói rằng thường thì ta cũng chẳng cần phải chứng minh
> một estimator là consistency theo kiểu chứng minh cái nó hội tụ xác suất
> về θ như trong định nghĩa. Mà có cách khác dễ làm hơn như sau.
>
> Thứ nhất, cần ôn lại cái bất đẳng thức Chebyshev: P(g(X) ≥ r) ≤ Eg(X) / r
>
> Chứng minh rất dễ, làm lại luôn cho vui: 
>
> Xét vế trái, Eg(X), dĩ nhiên LOTUS cho ta tính nó bằng:
>
> Eg(X) = ∫g(x)f(x)dx với f(x) là pdf của X và tích phân là trên toàn miền -inf:inf.
>
> mà tích phân vốn có ý nghĩa là phần diện tích dưới đồ thị hàm số trong 
> khoảng đang xét.
>
> nên ∫g(x)f(x)dx ≥ ∫_{x: g(x) > r} g(x)f(x)dx 
>
> Và vì đang xét trên miền {x: g(x) > r} nên 
>
>  ∫_{x: g(x) > r} g(x)f(x)dx ≥ ∫_{x: g(x) > r} rf(x)dx = r ∫_{x: g(x) > r} f(x)dx
>
> và cái này chính là r P(g(X) > r).
>
> Vậy Eg(X) ≥ r P(g(X) > r) ⇨ P(g(X) > r) < Eg(X) / r.
>
> Quay lại đây, áp dụng vào random variable (Wn - θ)^2, ta cũng có 
>
> P_θ((Wn - θ)^2 ≥ ε^2) ≤ E_θ[(Wn - θ)^2] / ε^2.
>
> ⇔ P_θ(|Wn - θ| ≥ ε) ≤ E_θ[(Wn - θ)^2] / ε^2.
>
> \-----
>
> Thế thì, tới đây nếu ta chứng minh được Wn thỏa E_θ[(|Wn - θ|)^2] / ε^2 → 0
> khi n → inf thì dĩ nhiên vế trái cũng → 0.
>
> Từ đó ta chỉ cần quan tâm vế trái E_θ[(Wn - θ)^2]
>
> Còn nhớ, theo công thức VarX = EX^2 - (EX)^2 ⇨ EX^2 = Var X + (EX)^2
>
> ⇨ E_θ[(Wn - θ)^2] = Var(Wn - θ) + [E_θ(Wn - θ)]^2
>
> = Var(Wn) + [E_θ(Wn - θ)]^2   | Var(X + c) = Var(X)
>
> Và cái E_θ(Wn - θ) = E_θ[Wn] - θ, chính là định nghĩa của Bias(Wn).
>
> ⇨ E_θ[(Wn - θ)^2] = Var(Wn - θ) + [Bias(Wn)]^2
>
> Và như vậy dĩ nhiên chỉ cần chứng minh Var(Wn - θ) → 0 và Bias(Wn) → 0
> khi n → inf, thì E_θ[(Wn - θ)^2] sẽ → 0 → P_θ(|Wn - θ| ≥ ε) → 0, và ta có
> consistent sequence of estimator Wn của θ

<br>

<a id="node-856"></a>

<p align="center"><kbd><img src="assets/bdec415b7c930288181d52ecda097c94f9f77241.png" width="100%"></kbd></p>

🔗 **Related:** [5.2 Σ OF RANDOM VARIABLES FROM A RANDOM SAMPLE](52_σ_of_random_variables_from_a_random_sample.md#node-344)

> [!NOTE]
> Áp dụng theorem này, quay lại ví dụ hồi nãy thì chỉ cần lập luận như sau:
>
> Vì Xbar_n ~ normal(θ, 1/n) ⇨ dĩ nhiên E_θ[Xbar_n] = θ → Bias(Xbar_n) = 0
>
> Và Var(Xbar_n) = 1/n ⇨ khi n → inf dĩ nhiên Var(Xbar_n) → 0
>
> Vậy theo theorem vừa rồi Xbar_n là consistent.
>
> HƠn nữa trong ví dụ đó, là cho X1,...Xn ~ normal(θ, 1) thì ta biết Xbar_n
>  ~ normal(θ, 1/n)
>
> Nhưng theorem 5.2.6 ta đã học, nói rằng X1,...Xn ko nhất thiết là normal
> mà chỉ cần có mean μ và variance hữu hạn σ^2.
>
> Thì khi đó E[Xbar] cũng là μ và Var(Xbar) cũng bằng σ^/n.
>
> Và theo đó, Xbar cũng là consistent estimator của μ 
>
> Như vậy, mọi Xbar_n của một sample iid có population với variance hữu
> hạn sẽ đều là consistent estimator của μ

<br>

<a id="node-857"></a>

<p align="center"><kbd><img src="assets/50a2391a6a4a91fda6b7e160db62d4b911481260.png" width="100%"></kbd></p>

> [!NOTE]
> Đại ý là, gs nói rằng, hồi đầu ta đã đề cập đến việc, có đáng để phải để tâm
> đến  một inconsistent estimator không. Thì ở đây ông nói đại ý là, sở dĩ nói
> vậy là vì theoerem sau đây ta sẽ thấy là, nếu Wm là một consistent estimator
> thì với chuỗi a1,a2,...và b1,b2,...thỏa điều kiện chuỗi a hội tụ về 1, chuỗi b
> hội tụ về 0 thì Un = anWn + bn sẽ cũng là một consistent estimator. Ý nói, có
> rất nhiều consistent estimator, nên ko việc gì phải xem xét một inconsistent

<br>

<a id="node-858"></a>

<p align="center"><kbd><img src="assets/08299323c5a22eb1eb0afeb9947f8d37847f0cc1.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e4bc976c892fbc161baac3940b8d3a1d678ebc04.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi, cuối cùng, gs nói về một theorem nói rằng, bất kì một ML estimator
> θ^ml(**X**) của một parameter θ nào cũng là consistent sequence of
> estimator của θ, và ông nói đây là lần đầu tiên ta gặp một trường hợp
> trong đó một cách tiếp cận cụ thể lại đảm bảo ta sẽ có được một
> estimator có được một tiêu chí tối ưu nào đó. (ông nói vậy là vì, cho đến
> nay, các phương pháp mà ta học để đi xây dựng một estimator chưa đảm
> bảo là nó sẽ là cái tốt nhất theo các tiêu chí nào đó, thì ở đây, với tiêu chí
> consistent, thì MLE approach lại đảm bảo là ta sẽ có được một consistent
> estimator)
>
> Theorem 10.1.6 nói rằng, nếu hàm likelihood mà thỏa tính chất gọi là "
> regularity conditions" thì: τ(θ^) sẽ hội tụ xác suất về τ(θ), thể hiện bởi lim n
> → inf P_θ(|τ(θ^) - τ(θ)| ≥ ε) = 0
>
> Và theo định nghĩa của consistent sequence of estimator rằng: Nếu chuỗi
> Wn, là estimator của θ hội tụ xác suất về θ thì Wn là consistent sequence
> of estimator của θ.
>
> Thì dĩ nhiên ở đâu nếu ta có chuỗi τ(θ^) hội tụ xác suất về τ(θ) thì chuỗi
> τ(θ^) sẽ là consistent sequence of estimator của τ(θ).
>
> Quay lại xem kĩ hơn phần chứng minh và regularity condition sau.

<br>

<a id="node-859"></a>

<p align="center"><kbd><img src="assets/8b69ae999a66883fc2c529a167b034c404f792c2.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là đánh giá chuỗi estimator theo tiêu chí consistency là nói đến
> tính chất liên quan đến việc estimator đó chính xác đến mức nào trong việc
> estimate cái param mà nó đang estimate.
>
> Để rồi, ta sẽ xét một tiêu chí khác, đánh giá estimator ở khía cạnh:
> asymptotic variance của nó.
>
> Có nghĩa là, hiểu đại khái là consistency nói đến việc: à, chuỗi estimator
> (với sample size tăng dần) sẽ có thể ngày càng estimate chính xác giá trị
> của param không. Thì efficiency sẽ đánh giá rằng khi sample size tăng dần
> thì mức biến động của estimator sẽ thế nào.

<br>

<a id="node-860"></a>

<p align="center"><kbd><img src="assets/494a1fe3c6dda96980596685b9b85229a0fe16d1.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e63878636e2e8347c61b261907dcea27bb119c65.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d17c778ccf26ecec2044fcf7b41ae2e22a105696.png" width="100%"></kbd></p>

🔗 **Related:** [5.5 CONVERGENCE CONCEPTS](55_convergence_concepts.md#node-421)

> [!NOTE]
> Rồi, thế thì gs nói đại khái là khi tính **phương sai tiệm cận (asymptotic variance)**, TA CÓ THỂ SẼ
> BỊ CÁM DỖ BỞI (TEMPTING) cách làm như sau: Gọi Tn là estimator (dựa trên sample size n), thì
> Var(Tn) là variance của Tn, khi đó ta xem xét variance của Tn tại limit:
>
> lim n → ∞ {kn Var(Tn)}
>
> Với kn là chuỗi các constant đóng vai trò normalizing constant (chưa hiểu lắm)
>
> Thế thì ta định nghĩa ra một khái niệm khác: giới hạn phương sai (limiting variance) được định
> nghĩa bởi: Nếu một (sequence of estimator) có phương sai tiệm cận lim n→∞ kn Var(Tn) = τ^2 < ∞,
> thì τ^2 được gọi là **limiting variance**.
>
> Lấy ví dụ, Xbar_n, là sample mean của iid normal(μ, σ^2) sample size n, như đã biết, nó sẽ một
> normal(μ, σ^2/n). Như vậy Var(Xbar_n) = σ^2/n ⇨ n Var(Xbar_n) = σ^2. Do đó, với Xbar_n thì lim n
> → ∞ n Var(Xbar_n) = σ^2, là con số hữu hạn (finite), < ∞. Do đó theo định nghĩa trên, σ^2 chính là
> limiting variance. (trong trường hợp này, chuỗi {kn} chính là {1,2,....n}.
>
> Thế thì đại ý là, việc đánh giá asymptotic variance bằng cách lấy giới hạn của variance của Tn sẽ
> không vấn đề gì khi Tn là sample mean, vì lim n → inf Var(Tn) = lim n → inf σ^2/n = 0. Và với một
> số Tn khác cũng vậy.
>
> Nhưng nếu ta quan tâm đến asymtotic variance của Tn = 1/Xbar_n, thì ta sẽ gặp vấn để vì Var(Tn)
> sẽ = inf, vì sao nhỉ?
>
> Chỉ cần hiểu đại khái, theo định nghĩa Var(Tn) = E[Tn^2] - (ETn)^2 = E[(1/Xbar_n)^2] -
> [E(1/Xbar_n)]^2
>
> Với E[(1/Xbar_n)^2], theo LOTUS, = ∫(1/xbar_n)^2 f(xbar_n) d(xbar_n) với f là pdf của xbar_n. Ta
> đã biết, Xbar_n của sample ~ normal(μ, σ) sẽ có limiting distribution là normal(μ, σ^2/n), tức là
> Xbar_n sẽ hội tụ distribution về một rv thuộc phân phối normal(μ, σ^2). thế thì với phân phối này,
> trong tích phân ∫(1/xbar_n)^2 f(xbar_n) d(xbar_n) đang nói, tồn tại xác suất dương nào đó để
> xbar_n = 0, khiến tích phân này = inf (explode), vì sao, vì range của normal là từ -inf, inf, nên có
> nghĩa là tại xbar_n=0, vẫn tồn tại giá trị pdf không âm.
>
> Không cần xét cái term thứ hai, lập luận trên cũng đủ để nói Var(1/Xbar_n) = ∞.
>
> Vấn đề là, trong ví dụ 5.5.23, mình đã học về Delta method giúp ta có công thức tính xấp xỉ mean
> và variance của 1/Xbar_n, có thể ôn lại chút xíu như sau:
>
> Delta method rất đơn giản thôi: Giả sử ta đang muốn xem xét random variable g(T) (T là random
> variable nào đó ~ f(t|μ). Thì lập luận như vầy: Theo giải tích, nếu xét phạm vi t ~ μ, thì ta có xấp xỉ
> bậc một: g(t) ≈ g(μ) + g' (μ)(t-μ) Áp dụng hai cái hàm số xấp xỉ nhau này lên random variable T, ta
> sẽ có hai random variable xấp xỉ:
>
> g(T) ≈ g(μ) + g'(μ)(T-μ)
>
> Thế thì xét E_μ[g(T)], vì xấp xỉ trên nên ta có:
>
> E_μ[g(T)] ≈ E_μ[g(μ) + g'(μ)(T-μ)] = E_μ[g(μ)] + E_μ[g'(μ)(T-μ)]
>
> = g(μ) + g'(μ) E_μ[T-μ]
>
> = g(μ) + g'(μ) (E_μ[T]-μ)
>
> = g(μ) + g'(μ) (μ-μ)
>
> = g(μ)
>
> Vậy E_μ[g(T)] ≈ g(μ)
>
> Còn Var_μ[g(T)] = E_μ{g(T) - E_μ[g(T)]}^2
>
> ≈ E_μ{g(T) - g(μ)}^2 (thay E_μ[g(T)] ≈ g(μ))
>
> ≈ E_μ{g(μ) + g'(μ)(T-μ) - g(μ)}^2 (thay g(T) ≈ g(μ) + g'(μ)(T-μ))
>
> = E_μ[g'(μ)(T-μ)]^2
>
> = (g'(μ))^2 E_μ[(T-μ)]^2
>
> = (g'(μ))^2 Var_μ[T]
>
> Áp dụng với T = Xbar_n là có mean E(Xbar_n) = μ và variance Var(Xbar_n) và g(Xbar_n) =
> 1/Xbar_n:
>
> ⇨ g'(t) = -1/t^2
>
> E[1/Xbar_n] = 1/E[Xbar_n] = 1/μ
>
> Var[1/Xbar_n] = (-1/μ^2)^2Var_μ[Xbar] = **(1/μ^4) Var_μ[Xbar]**
>
> Và như vậy, ý chính muốn nói, với Tn = 1/Xbar_n, thì khi ta t**ính chính xác variance của nó, được
> ∞**. Nhưng tính xấp xỉ, thì lại là **(1/μ^4) Var_μ[Xbar]**
>
> Như vậy, tóm lại, việc tính asymptotic variance của Tn theo kiểu lấy Variance của Tn tại limit (lim n
> → inf Var(Tn), gọi là limiting variance không ổn, trong khi đó, dùng cách làm xấp xỉ thì lại thực tế
> hơn và hữu ích hơn. Thành ra ta sẽ có **định nghĩa chính thức của asymptotic variance** như sau:
>
> đó là, cho chuỗi estimator (dựa trên sample size n) Tn: sao cho kn (Tn - τ(θ)) hội tụ phân phối về
> n(0, σ^2), khi đó σ^2 gọi là asymptotic variance của Tn.
>
> Có nghĩa là, thì **thay vì dùng Var(Tn) tại limit, ta dùng variance của cái phân phối normal là limit
> distribution của kn (Tn - τ(θ)) làm asymptotic variance**.
>
> Như vậy, với Tn = 1/Xbar, thay vì dùng Var(1/Xbar) tại limit (=inf), ta dùng (1/μ^4) Var_μ[Xbar]. Như
> vậy, với Tn = 1/Xbar, thay vì dùng Var(1/Xbar) tại limit (=inf), ta dùng (1/μ^4) Var_μ[Xbar]
>
> Và một điểm thú vị nữa, đó là asymptotic variance thì luôn nhỏ hơn limiting variance.

<br>

<a id="node-861"></a>

<p align="center"><kbd><img src="assets/deb8e722a632fa3051fb8cfccf4f6fc50dfeab6b.png" width="100%"></kbd></p>

> [!NOTE]
> Ví dụ này ta có một hierarchical modal:
>
> Yn|Wn = wn ~ n(0, wn + (1-wn)σn^2)
>
> Wn ~ Bern(pn)
>
> Đã gặp cái này ở mấy chương trước có nghĩa là nếu biết giá trị của Wn (= wn) thì Yn là normal mean 0 có
> variance wn + (1-wn) σn^2. Và bản thân Wn thì là một rn ~ Bern(pn).
>
> Vậy thì ở đây, gs nói cái này cũng chính là mixture model khi ta thấy Yn ~ n(0,1) với xác suất pn và Yn ~
> n(0, σn^2) với xác suất 1 - pn. Là sao ta:
>
> Khái niệm mixture model, trong sách này (Casella) cho đến giờ chưa được nghe. Nhưng, quachapter 2
> của PRML của C.Bishop đã biết khái niệm mixture model, cũng đơn giản, đại khái như sau: f(x) = convex
> combination của các fi(x): ∑i αi fi(x). với fi(x) là các pdf của distribution. Ví dụ f(x|**μ**, **σ^2**) = αi fi(x|μi,
> σi^2) với fi là pdf của Normal(μi, σi^2), và αi ≥ 0 ∀i, và ∑i αi = 1, thì ta sẽ có một Gaussian (normal) mixture.
>
> Vậy thì ở đây, ta có f1(x|0,1) là pdf của Normal(0,1) và f2(x|0, σn^2) là pdf của Normal(0, σn^2) và convex
> combination coefficient là α1 = pn và α2 = 1-pn.
>
> Chú ý là Yn|(Wn=wn) ~ n(0, wn + (1 - wn) σn^2) & Wn ~ Bern(pn), cũng là cái Gaussian mixture nói trên,
> KHÔNG PHẢI LÀ MỘT NORMAL DISTRIBUTION có variance là wn + (1 - wn) σn^2. Mà cách viết n(0, wn
> \+ (1 - wn) σn^2) chỉ có nghĩa là, nếu Wn = 1 (vốn là sự kiện có xác suất xảy ra là pn) thì Yn|Wn=1 sẽ là rv
> ~ normal(0,1), và nếu Wn = 0, là sự kiện có xác suất xảy ra là 1-pn, thì Yn|Wn=1 sẽ là rv ~ normal(0,
> σn^2). Nên gs mới nói câu "ta quan sát thấy Yn ~n(0,1) với xác suất pn và Yn~n(0, σn^2) với xác suất
> 1-pn.
>
> Dùng công thức 4.4.7 (xem link) ta có thể có công thức của Var(Yn) = pn + (1 - pn)σn^2, để rồi ta sẽ nhận
> định rằng cái này tại limit (tức limiting variance) chỉ hữu hạn nếu giá trị tại limit của (1 - pn)σn^2 cũng hữu
> hạn.
>
> Nhưng với asymptotic variance thì ta sẽ tính được = 1. Thử xem họ tính vậy là sao?
>
> P(Yn < a) = pnP(Z < a) + (1-pn) P(Z < a/σn), dòng này là sao?
>
> P(Yn < a) tức là FYn(a) (cdf của Yn tại a)
>
> gọi fYn là pdf của Yn, ta biết theo định nghĩa của cdf và pdf, ta có:
>
> FYn(a) = ∫-inf:a fYn(t)dt
>
> Vì Yn ~ Gaussian mixture → fYn(t) = pn N(t|0,1) + (1-pn) N(t|0, σn^2)
>
> ⇨ FYn(a) = ∫-inf:a fYn(t)dt = ∫-inf:a[pn N(t|0,1) + (1-pn) N(t|0, σn^2)] dt
>
> = ∫-inf:a [pn N(t|0,1)] dt + ∫-inf:a [(1-pn) N(t|0, σn^2)] dt
>
> = pn ∫-inf:a N(t|0,1) dt + (1-pn) ∫-inf:a N(t|0, σn^2) dt
>
> = pn ∫-inf:a N(t|0,1) dt + (1-pn) ∫-inf:a N(t|0, σn^2) dt
>
> ∫-inf:a N(t|0,1) dt chính là cdf tại a của Z ~ normal(0,1), tức FZ(a), cũng là P(Z < a)
>
> còn ∫-inf:a N(t|0, σn^2) dt chính là cdf tại a của W ~ normal(0, σn^2), tức FW(a), và cũng là P(W < a)
>
> Mà theo location scale theorem ta cũng biết W chính là Zσn, nên P(W < a) = P(Zσn < a) = P(Z < a/σn)
>
> Vậy ta có P(Yn < a) = pn P(Z < a) + (1-pn) P(Z < a/σn).
>
> Thế thì, hồi nãy, với limiting variance ta nói, chỉ khi (1-pn)σn^2 → giá trị hữu hạn khi n → inf thì limiting
> variance mới finite.
>
> Vậy thì ở đây, ta thử cho (1-pn)σn^2 → inf luôn (bằng cách cho pn → 1 và σn → ∞, thì ta sẽ thấy khi đó:
>
> P(Yn < a) = pn P(Z < a) + (1-pn) P(Z < a/σn) sẽ → 1 × P(Z < a) + 0 × P(Z < 0) = P(Z < a)
>
> Mà P(Yn < a) → P(Z < a) tức là FYn(a) → FZ(a), theo định nghĩa cuả hội tụ phân phối (converge in
> distribution), đây chính là nói Yn → (d) Z. Và theo định nghĩa của asysmtotic variance, là variance của
> limiting distribution, thì ta có asymtotic variance của Yn = Var(Z) = 1.
>
> Như vậy, khi ta cho pn → 1, σn → ∞ thì:
>
> limiting variance = inf (vì pn + (1-pn)σn^2 → inf)
>
> nhưng
>
> asymptotic variance = 1
>
> Và điều này chỉ rõ một điều nói ở trên: là dùng limiting variance (tức giá trị của Var(Tn) tại limit) là không
> hữu ích và cũng không thực tế bằng việc dùng asymptotic variance (variance của limiting distribution). Mà
> việc khi ta cho pn → 1 và σn → ∞ với hai kết quả trái ngược nhau ở trên có ý nghĩa rất hay như sau:
>
> Cho pn → 1, tức là cho xác suất chọn được n(0,1) là rất rất lớn, đồng nghĩa rất rất hiếm xảy ra việc chọn
> được n(0, σn^2). Nhưng đồng thời cho σn → ∞ tức là cho nó rất rất lớn. Thì cái limiting variance ngu ngốc
> ở chỗ, nó vẫn cho rằng có xác suất dương nào đó (dù vô cùng nhỏ) xảy ra việc chọn cái normal có
> variance khổng lồ, nên nó cho rằng variance tổng (ý là limiting variance) là khổng lồ. Trong khi đó, thực tế
> thì, thật ra với xác suất cực lớn của việc chọn được n(0,1) thì variance = 1 sẽ hợp lí hơn, cũng là nói
> asymptotic variance sẽ thực tế hơn.

<br>

<a id="node-862"></a>

<p align="center"><kbd><img src="assets/6389e9e23f3425fb0cbff838a9d90be1e4479079.png" width="100%"></kbd></p>

🔗 **Related:** [7.3 METHODS OF EVALUATING ESTIMATORS](73_methods_of_evaluating_estimators.md#node-617)

> [!NOTE]
> Nói ngắn gọn, ở đây người ta **định nghĩa** ra cái gọi là khi nào thì **chuỗi estimator Wn** được gọi là
> **ASYMPTOTICALLY EFFICIENT** của một parameter τ(θ), đó là nếu như **asymptotic variance của
> nó có thể đạt được giá trị variance nhỏ nhất được thể hiện bởi giá trị chặn dưới Cramer-Rao (lower
> bound)**.
>
> Để hiểu cái này, ta sẽ cần liên hệ lại (nhớ lại) kiến thức về Cramer-Rao Lower Bound là cái gì), đã học
> ở chap 7, trong phần đánh giá chất lượng của các point estimator. Nói ngắn gọn, khi cần phải đánh
> giá các estimator (evaluating estimator quality), thì một tiêu chí quan trọng là MSE, được định nghĩa là
> một hàm của estimator: MSE(W(**X**)) = E_θ[(W(**X**) - θ)^2], và ta muốn cái này càng nhỏ càng tốt.
> Sau đó, bằng cách biến đổi chút, ta sẽ cho thấy nó = Var_θ [W(**X**)] + [Bias(W(**X**)]^2 với
> Bias(W(**X**)) = E_θ[W(**X**)] - θ. Để rồi, câu chuyện tiếp theo là, giả sử ta **xét một đám các
> estimator có cùng bias** (đồng nghĩa có cùng kì vọng E_θ[W(**X**)]), thì thằng nào có Var_θ[W(**X**)]
> nhỏ nhất sẽ là tốt nhất.
>
> Thế thì, việc tính variance có thể phức tạp, và quan trọng hơn, trong nhiều trường hợp, ta cũng không
> thể biết được rằng, một estimator có variance nào đó có phải là nhỏ nhất hay không. Từ đó, mới nói
> đến một công cụ cho vấn đề này: **Cramer Rao Lower Bound**. Đây chỉ đơn giản là một theorem, nói
> rằng, giả sử ta có bối cảnh thỏa mãn yêu cầu đề ra nào đó (xem cụ thể trong theorem) thì khi đó, ta
> có thể **xác định được cái lower bound của** Var_θ(W(**X**)), từ đó, **nếu ta có một estimator có
> variance bằng với chặn dưới này, thì có thể kết luận nó chính là cái tốt nhất** (cái tốt nhất trong đám
> các estimator có chung bias, và nếu đang xét đám các unbiased estiamtor thì ta gọi nó là uniformly
> minimum variance unbiased estimator)
>
> Thế thì, cái lower bound theo công thức Cramer Rao:
>
> Var_θ(W(**X**)) ≥ [d/dθ E_θ[W(**X**)]^2] / [E_θ[(∂/∂θ log f(**X**|θ))^2]]
>
> Qua lại đây, nhớ rằng 10.1.11, là người ta đang định nghĩa ra cái sequence estimator gọi là
> **asymptotically efficient cho τ(θ)**, rằng nếu asymptotic variance của nó bằng [τ'(θ)]^2 / [E_θ[(∂/∂θ log
> f(**X**|θ))^2]].
>
> Theo Cramer Rao Lower Bound theorem, nói rằng một estimator W(**X**) sẽ có variance bị chặn dưới
> bởi: Var_θ(W(**X**)) ≥ [d/dθ E_θ[W(**X**)]^2] / [E_θ[(∂/∂θ log f(**X**|θ))^2]]
>
> Vậy thì, ở đây lại cho ta có √n[Wn - τ(θ)] → (d) n[0, ν(θ)], thì riêng điều này, theo như định nghĩa của
> asymptotically variance, là variance của limiting distribution, thì như vậy, ν(θ) là asymptotically
> variance của Wn.
>
> Sau đó, nếu giá trị này lại bằng ([τ'(θ)]^2 / [E_θ[(∂/∂θ log f(**X**|θ))^2]])
>
> mà cái này, nếu xét W(**X**) là unbiased estimator của τ(θ), tức E[W(**X**)] = τ(θ), ⇨ τ'(θ) = d/dθ
> E[W(**X**)] ⇔ τ'(θ)^2 = [d/dθ E[W(**X**)]]^2
>
> hoặc, kể của W(**X**) là biased estimator của τ(θ), nhưng tại limit, bias = 0: lim n → inf E[Wn(**X**)] =
> τ(θ) thì trong trường hợp này và trường hợp trên ta đều có:
>
> ([τ'(θ)]^2 / [E_θ[(∂/∂θ log f(**X**|θ))^2]]) chính là [d/dθ E_θ[W(**X**)]^2] / [E_θ[(∂/∂θ log f(**X**|θ))^2]],
> tức Cramer Rao Lower Bound.
>
> Như vậy, về cơ bản, cái định nghĩa này nói rằng nếu một chuỗi estimator Wn của τ(θ) muốn được gọi
> là asymptotically efficient, thì nó phải unbias: E[Wn(**X**)] = τ(θ) đồng thời, asymptotically variance
> của nó, phải bằng đúng Cramer Rao Lower Bound.

<br>

<a id="node-863"></a>

<p align="center"><kbd><img src="assets/9d91dae36abde2d0f58291d343701330510a9d1a.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì, tiếp theo là một theorem nói rằng, dưới một số điều kiện nhất định
> (xem thêm trong phần Miscellanea) của hàm f(x|θ) và gọi θ^ là ML estimator
> của θ, τ là hàm liên tục nào đó. Theorem này nói rằng:
>
> √n (τ(θ^) - τ(θ)) sẽ hội tụ phân phối về n(0, ν(θ)) với ν(θ) là Cramer Rao Lower
> Bound (1)
>
> Điều này có nghĩa là dưới những điều kiện nhất định nói trên, thì **τ(θ^)** **sẽ
> là một consistent và asymptotically efficient estimator** **của** **τ(θ)**.
>
> Nên hiểu, (1) hàm ý hai thứ:
>
> i) τ(θ^) → (p) τ(θ), và theo định nghĩa, đây cho thấy τ(θ^) là consistent
> sequence of estimator của τ(θ). Chứng minh nhanh:
>
> Ta có √n (τ(θ^) - τ(θ)) → (d) n(0, ν(θ)) thì phải hiểu là √n (τ(θ^) - τ(θ)) → (d) Z ~
> n(0, ν(θ)) (√n (τ(θ^) - τ(θ)) sẽ trở thành một random variable có phân phối n(0,
> ν(θ)).
>
> Và 1/√n → 0 (đơn giản là vì lim n→inf 1/√n = 0
>
> Theo Slusky theorem: nếu Xn → (d) X, Yn → constant a thì XnYn → (d) aX,
> vậy áp dụng vào đây √n (τ(θ^) - τ(θ)) × 1/√n → (d) 0 × Z = 0.
>
> Mà theo một theorem 5.5.13, nói rằng, nếu Xn → (d) constant μ ⇔ Xn → (p)
> constant μ. Nên áp dụng theorem này, ta có √n (τ(θ^) - τ(θ)) × 1/√n = τ(θ^) -
> τ(θ) cũng → (p) contant
> 0. Và theo định nghĩa của consistent sequence of estimator, nếu P_θ(|Wn - θ|
> < ε) = 1 ∀ε, cũng chính là nói Wn → (p) θ, thì Wn là consistent sequence of
> estimator. Vậy, theo đó, τ(θ^) là consistent sequence of estimator của τ(θ)
>
> (nói là chuỗi là bởi vì phải tự hiểu θ^ là MLE, có bản chất cũng là một statistic,
> một hàm của sample size n).
>
> ii) phân phối đích có variance là ν(θ), tức là cái này chính là asymptotically
> variance của τ(θ^), mà cái này là CRLB, thì theo định nghĩa của asymtoptically
> efficient, thì τ(θ^) chính là một asymtoptically efficient sequence of estimator
> của τ(θ)
>
> Và nhờ phân tích trên mình cũng sẽ thấy rằng, thật ra efficient chính là sẽ
> consistent. Là sao? Là vì theo định nghĩa của efficient: √n (τ(θ^) - τ(θ)) sẽ hội tụ
> phân phối về n(0, ν(θ)) với ν(θ) là Cramer Rao Lower Bound, thì dựa vào cái
> định nghĩa này, ta chứng minh như ở trên để cho thấy tính consistent. Vậy thì
> một sequence estimator thỏa định nghĩa này, sẽ là efficient và cũng tự nhiên là
> consistent, nên nói cách khác, efficient bao hàm consistent, thành ra nói vừa
> efficient vừa consistent là thừa (redundant), mà trong phần sau gs nói chính là
> này.

<br>

<a id="node-864"></a>

<p align="center"><kbd><img src="assets/1f72e00d8c300a79b9a2e23ff65b0ebc4c5370c6.png" width="100%"></kbd></p>

> [!NOTE]
> Quay lại sau

<br>

<a id="node-865"></a>

<p align="center"><kbd><img src="assets/89f1293b599cc95063f151ac1b33215b00e63b9e.png" width="100%"></kbd></p>

> [!NOTE]
> Phần này như trong note
> trước đã hiểu rồi

<br>

