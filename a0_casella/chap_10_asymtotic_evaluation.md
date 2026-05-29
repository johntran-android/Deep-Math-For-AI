# Chap 10 Asymtotic Evaluation

📊 **Progress:** `8` Notes | `8` Screenshots

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

