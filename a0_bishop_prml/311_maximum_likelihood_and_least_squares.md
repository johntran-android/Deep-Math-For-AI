# 3.1.1 Maximum likelihood and least squares

📊 **Progress:** `7` Notes | `9` Screenshots

---
<a id="node-329"></a>

<p align="center"><kbd><img src="assets/16c5987d6f177c63dafa5b8aebd337b71bc85cf5.png" width="100%"></kbd></p>

> [!NOTE]
> Đầu tiên gs nhắc lại là ở chap 1 mình đã học bài toán polynomial curve fitting - về cơ bản là đi tìm một
> hàm đa thức để khớp với các data, bằng cách tìm parameter sao cho giảm thiểu sum of square error
> function. Và trong quá trình làm, ta đã chứng minh hoặc cho thấy rằng, bản chất của việc minimize hàm
> squared error function, thực chất chính là tiếp cận bài toán như bài toán point estimation, theo phương
> pháp maximum likelihood với một gỉa định là noise tuân theo phân phối normal.
>
> Thế thì phần này, mình sẽ quay lại bài toán đó, và bàn thêm về cách tiếp cận least square cũng như liên
> quan của nó với maximum likelihood.
>
> Mình muốn active recall lại tí xíu, để ít nhất có thể làm rõ vì sao nói ý trên.
>
> Nói một cách ngắn gọn, đầu tiên ta thể hiện tính uncertainty của target bằng cách coi nó là random
> variable T
>
> Và giả định sai số Ei = Ti - y(**w**, **x**i) ~ normal(0, 1/β), điều này có nghĩa là, ta xây dựng function để
> dự đoán t, nhưng tin rằng, kể cả có đoán chính xác, thì vẫn tồn tại noise, khiến tạo ra sai số, và noise là
> đại lượng ngẫu nhiên, ta thể hiện nó bởi random variable Ei, có phân phối normal(0, 1/β) (precision β nào
> đó)
>
> Như vậy, theo location family, nếu Ei = Ti - y(**w**, **x**i) ~ normal(0, 1/β), thì Ti ~ normal(y(**w**, **x**i),
> 1/β).
>
> Cần nhấn mạnh: Mấu chốt là lập luận rằng: Coi target variable là một đại lượng mang tính ngẫu nhiên -
> điều này hợp lí vì, với một đối tác là **x**i, ti có thể có nhiều possible value, nó mang tính uncertainty. Và
> hàm dự đoán của ta y(**w**, **x**i) dù có làm tốt đến mấy trong việc nắm bắt được quy luật, thì vẫn còn
> đó sai sót do nhiễu, và nhiễu này, ta cho rằng, tuân theo phân phối chuẩn.
>
> Rồi, như vậy, bài toán trở thành, cho random sample T1,...Tn (n hay m, hay N gì đó, chỉ số sample), với
> Ti ~ normal(y(**w**, xi), 1/β), i = 1,2,...n. Và các random variable Ti này độc lập nhau (vì data được collect
> một cách độc lập). Chú ý, độc lập nhưng không identically distributed, vì các normal đều có mean khác
> nhau, nên không có tính iid, chỉ độc lập thôi.
>
> Dĩ nhiên, ta có bài toán quen thuộc: tìm point estimator cho **w** - tham số chi phối distribution của Ti
> (given **x**i)
>
> Và cách tiếp cận phổ biến là Maximum Likelihood estimation (nhất là sau khi ta học chap 10 Casella,
> mình biết ML estimator sẽ tạo một chuỗi estimator có tính chất (asymptotically) efficient (và consistent))
>
> Thế thì, để làm, đầu tiên cần xét joint pdf của **T** = (T1,...Tn), ta sẽ thấy dù chúng không cùng
> distribution, nhưng vẫn độc lập, cho phép tách joint pdf thành tích các marginal pdf: Πi=1:n f(ti|y(**w**,
> **x**i), 1/β).
>
> Từ đó hàm likelihood, theo định nghĩa, là hàm của parameter, được define bởi giá trị của joint pdf của
> sample tại observed value:
>
> L(**w**, β|**t**, **x**1,...**x**n) = f(**t**|**w**, **x**1,..**x**n, 1/β) = Πi=1:n f(ti|y(**w**,**x**i), 1/β)
>
> Và theo ML, ta sẽ giải bài toán:
>
> maximize (over **w**, β) L(**w**, β|**t**, **x**1,...**x**n)
>
> Tới đây, ta sẽ dùng các kĩ thuật chuyển bài toán tối ưu thành bài toán tương đương bằng cách dùng hàm
> monoton ln, hoặc bỏ đi constant:
>
> L(**w**, β|**t**, **x**1,...**x**n) ∝ ln {L(**w**, β|**t**, **x**1,...**x**n)}
>
> = ln {Πi=1:n f(ti|y(**w**, **x**i), 1/β)} = Σi=1:n ln {f(ti|y(**w**, **x**i), 1/β)}
>
> = Σi=1:n ln {N(ti|y(**w**, **x**i), 1/β)}
>
> = Σi=1:n [ ln { Πi [1/√[2π(1/β)]] exp[-[ti-y(xi,**w**)]^2/2(1/β)] } ] (....biến đổi, thu gọn)
>
> = (n/2) ln β - (n/2) ln (2π) - (β/2) Σi [ti-y(xi,**w**)]^2
>
> = - (β/2) Σi [ti-y(xi,**w**)]^2 + (n/2) ln β - (n/2) ln (2π)
>
> ∝ - Σi [ti-y(xi,**w**)]^2
>
> Như vậy, bài toán euivalent là: maximize (over **w**) - Σi [ti-y(xi,**w**)]^2
>
> equivalent tiếp: minimize (over **w**) {Σi [ti-y(xi,**w**)]^2}
>
> Và như vậy có thể thấy, đây chính là cách tiếp cận bài toán curve fitting theo lối đơn giản là đi tìm w sao
> cho giảm thiểu hàm loss tính bằng tổng bình phương của error Có nghĩa là trong đó ta ko bàn về xác
> suất gì cả, mà chỉ là cố đi tìm param để giảm thiểu loss thôi, nhưng với góc nhìn xác suất, ta thấy nó
> chính là đi giải bài toán tìm Maximun Likelihood estimator với giả định là noise ~ normal(0, 1/β)

<br>

<a id="node-330"></a>

<p align="center"><kbd><img src="assets/1da1dc3541db5feda4f3b104d128ade5a47d62a5.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi, như vừa ôn lại, ta sẽ giả định noise ~ normal(0, β^-1) cũng đồng nghĩa giả định T
> = y(**x**, **w**) + ε ~ normal(y(**x**, **w**), β^-1), nên f(t|**x**, **w**, β) = N(t|y(**x**,
> **w**), β^-1) (đây chỉ là kí hiệu normal(y(**x**, **w**), β^-1))
>
> Tới đây, ông nói, ta đã biết trong chap 1 rằng, khi đã có distribution của T (f(t|**x**,
> **w**, β) thì nếu ta cần **đưa ra dự đoán sao cho tối ưu** (**optimal prediction**), thì khi
> **loss là squared loss**, thì prediction tối ưu đó chính là dùng **conditional mean**.
>
> Cùng làm rõ ý này:
>
> Thật ra cái này y như một điểm mà mình đã viết trong note trước (3.1.0) khi liên hệ với
> Casella, trong đó mình nói rằng, khi đã có posterior distribution của θ, π(θ|**x**), thì
> Bayes estimator cho θ giúp giảm thiểu Bayes risk với loss tính bằng squared loss chính
> là mean của posterior: E[θ|**x**]. Ở đây cũng y vậy, nên mình có thể chứng minh lại:
>
> Bắt đầu lại với việc mượn lập luận của bài toán inference θ trong note (Predicting
> Values and Linear Models, xem link), để liên hệ qua cho dễ:
>
> Squared error loss function: L(W(**X**), θ) = [W(**X**) - θ]^2
>
> Risk function: average over all possible **x**: ∫L(W(**x**), θ) f(**x**|θ) d**x**
>
> Nếu là Bayesian, ta có thêm Bayes risk: average over all possible θ:
>
> ∫ [ ∫L(W(**x**), θ) f(**x**|θ) d**x** ] π(θ) dθ
>
> = ∫ [ ∫L(W(**x**), θ) f(θ|**x**) f(**x**) / π(θ) d**x** ] π(θ) dθ
>
> = ∫∫L(W(**x**), θ) f(θ|**x**) f(**x**) d**x** dθ
>
> = ∫∫L(W(**x**), θ) f(θ|**x**) dθ f(**x**) d**x**
>
> = ∫ [∫L(W(**x**), θ) f(θ|**x**) dθ] f(**x**) d**x**
>
> = ∫ [posterior expected loss] f(**x**) d**x** (posterior expected loss = ∫L(W(**x**), θ)
> f(θ|**x**) dθ)
>
> Và minimize (over W) Bayes risk sẽ trở thành mininize posterior expected loss với mọi
> **x**
>
> ⇔ minimize E[L(W(**x**),θ)], θ ~ π(θ|**x**) với mọi **x**
>
> ⇔ minimize E[(W(**x**) - θ)^2], θ ~ π(θ|**x**) với mọi **x**
>
> Và solution là W(**x**) = E[θ|**x**], là posterior mean.
>
> ⇔ minimize (over W) (W(**x**)- θ)^2 với mọi x
>
> Vậy quay lại đây
>
> Loss function, cụ thể là square error loss: L(T, y(**w**, **x**)) = [T - y(**w**, **x**)]^2
>
> Risk function, là average over all **t**: E([T - y(**w**, **x**)]^2), T ~ n(y(**w**, **x**), 1/β)
>
> Y như trên với T đóng vai θ, y(**w**,**x**) đóng vai W(**x**), ta có bài toán minimize risk
> function:
>
> minimize over y(w,x) {E([T - y(**w**, **x**)]^2)}, với T ~ n(y(**w**, **x**), 1/β)
>
> Và solution cũng sẽ là posterior mean: E[T], T ~ n(y(**w**, **x**), 1/β), và có thể ghi là
> E[T|**w**,**x**,β]
>
> Ở đây phải rạch ròi hai việc, hay nói cách khác, có hai bài toán đặt ra:
>
> Bài toán thứ nhất là: với data quan sát được, và dưới giả định Ti ~ n(y(**w**,**x**i),
> 1/β) thì một estimator tốt của **w** là gì. Và nếu ta làm theo lối tìm maximum likelihood
> estimator cho w, kết quả ta tìm ra là: chính là w khiến minimize sum squared error
> {Σi=1:n [ti - y(**w**, **x**i)]^2}.
>
> Còn bài toán thứ hai, là, giả sử ta có distribution của T là f(t|**x**), gọi là predictive
> distribution, thì để dự đoán t với một **x cho trước** mới, thì hành động tối ưu là gì. Và
> lập luận cho thấy, giá trị tối ưu là E[t|**x**], tức là mean của distribution f(t|**x**) nếu như
> ta chọn loss là square error.
>
> Và đây là chỗ nhập nhằng dễ lú:
>
> Kết hợp hai bài toán: là ta dùng giả định Ti ~ n(y(**w**,**x**i), 1/β), để tìm ra ML
> estimator cho **w**: **w**^ML. Thì khi đó, ta có predictive distribution là T ~ f(t|**x**) =
> pdf của n(y(**w**^ML,**x**), 1/β). Và theo bài toán thứ hai, dự đoán tối ưu cho giá trị t
> của một x cho trước chính là mean của n(y(**w**^ML,**x**), 1/β), và ngay tại đây xảy ra
> sự tiện lợi ở chỗ, nó chính là y(**w**^ML,**x**).
>
> Sự tiện lợi này sẽ không tồn tại nếu các trường hợp sau:
>
> Nếu ta có T ~ f(t|**x**) = pdf của n(y(**w**^ML,**x**), 1/β), nhưng tiêu chí của bài toán
> thứ hai không phải là squared error, khi đó, hành động tối ưu không phải là dùng mean
> của n(y(**w**^ML,**x**), 1/β), mà là dùng cái gì khác, khi đó ta phải tính toán thêm.
>
> Hoặc nếu ta trong bài toán thứ nhất, ta không giả định Ti ~ n(y(**w**,**x**i), 1/β), thì việc
> giải tìm ML estimator của w sẽ không phải là tìm w khiến mininize sum square error. Và
> giả sử ta tìm ra w^ML, thì nó chưa chắc là mean của f(t|**x**).Để rồi nếu trong bài toán
> thứ hai ta vẫn dùng tiêu chí squarer error loss, để có solution tối ưu là mean của
> f(t|**x**), thì lúc này, ta sẽ phải tính tiếp mean của f(t|**x**), thay vì có thể tiện lợi dùng
> y(**x**,**w**)
>
> Ở đây phải rạch ròi hai việc, hay nói cách khác, có hai bài toán đặt ra:
>
> Bài toán thứ nhất là: với data quan sát được, và dưới giả định Ti ~ n(y(**w**,**x**i),
> 1/β) thì một estimator tốt của **w** là gì. Và nếu ta làm theo lối tìm maximum likelihood
> estimator cho w, kết quả ta tìm ra là: chính là w khiến minimize sum squared error
> {Σi=1:n [ti - y(**w**, **x**i)]^2}.
>
> Còn bài toán thứ hai, là, giả sử ta có distribution của T là f(t|**x**), gọi là predictive
> distribution, thì để dự đoán t với một **x cho trước** mới, thì hành động tối ưu là gì. Và
> lập luận cho thấy, giá trị tối ưu là E[t|**x**], tức là mean của distribution f(t|**x**) nếu như
> ta chọn loss là square error.
>
> Và đây là chỗ nhập nhằng dễ lú:
>
> Kết hợp hai bài toán: là ta dùng giả định Ti ~ n(y(**w**,**x**i), 1/β), để tìm ra ML
> estimator cho **w**: **w**^ML. Thì khi đó, ta có predictive distribution là T ~ f(t|**x**) =
> pdf của n(y(**w**^ML,**x**), 1/β). Và theo bài toán thứ hai, dự đoán tối ưu cho giá trị t
> của một x cho trước chính là mean của n(y(**w**^ML,**x**), 1/β), và ngay tại đây xảy ra
> sự tiện lợi ở chỗ, nó chính là y(**w**^ML,**x**).
>
> Sự tiện lợi này sẽ không tồn tại nếu các trường hợp sau:
>
> Nếu ta có T ~ f(t|**x**) = pdf của n(y(**w**^ML,**x**), 1/β), nhưng tiêu chí của bài toán
> thứ hai không phải là squared error, khi đó, hành động tối ưu không phải là dùng mean
> của n(y(**w**^ML,**x**), 1/β), mà là dùng cái gì khác, khi đó ta phải tính toán thêm.
>
> Hoặc nếu ta trong bài toán thứ nhất, ta không giả định Ti ~ n(y(**w**,**x**i), 1/β), thì việc
> giải tìm ML estimator của w sẽ không phải là tìm w khiến mininize sum square error. Và
> giả sử ta tìm ra w^ML, thì nó chưa chắc là mean của f(t|**x**).Để rồi nếu trong bài toán
> thứ hai ta vẫn dùng tiêu chí squarer error loss, để có solution tối ưu là mean của
> f(t|**x**), thì lúc này, ta sẽ phải tính tiếp mean của f(t|**x**), thay vì có thể tiện lợi dùng
> y(**x**,**w**)

<br>

<a id="node-331"></a>

<p align="center"><kbd><img src="assets/abbb91d26607e6e7e0ab43fb006622d7b4c138a4.png" width="100%"></kbd></p>

> [!NOTE]
> Cụ thể, chúng ta giả định rằng nhiễu tuân theo phân phối chuẩn với giá trị
> trung bình bằng 0 và độ chính xác là β. Điều này cũng có nghĩa là biến ngẫu
> nhiên T có phân phối đơn đỉnh là phân phối chuẩn, với giá trị trung bình tại giá
> trị của hàm dự đoán y(x, w) và tham số precision là β.
>
> Điểm chính cần nhấn mạnh ở đây là chúng ta không chỉ giả định T tuân theo
> phân phối chuẩn mà còn giả định nó là một phân phối đơn đỉnh (unimodal).
> Tuy nhiên, trong nhiều trường hợp và bài toán thực tế, giả định này không còn
> phù hợp. Do đó, chúng ta sẽ cần sử dụng mô hình hỗn hợp Gaussian
> (Gaussian mixture), tức là sự kết hợp của nhiều phân phối chuẩn. Chủ đề này
> sẽ được thảo luận chi tiết trong Phần 14 và Chương 14.

<br>

<a id="node-332"></a>

<p align="center"><kbd><img src="assets/cf93d45c4683d4298f69f99a968995df0280fd61.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi, từ cái note hồi đầu của section này đã giúp ta có thể hiểu đoạn này rồi:
>
> Như đã biết, ta có bộ data, là các observed value (**x**i, ti) i=1,...N. Gom lại thành matrix **X** (có thể là mỗi
> **x**i làm một hàng) và vector **t** = (t1,...tN).
>
> Và như đã nói, ta dùng một distribution để thể hiện tính uncertainty của target variable, tức là coi t1,t2,...tN là
> observed value của các random variable T1, ...TN. Và giả định thêm rằng noise εi = Ti - y(**w**, **x**) sẽ ~
> Norm al(0,1/β), nên Ti ~ normal(y(**w**, **x**i), 1/β).
>
> Từ đó xét joint distribution của T1,..TN,
>
> f(**t**|**X**, **w**, β) = f(t1,t2,..tN|**X**, **w**, β).
>
> Vì tính chất các T1,...TN độc lập (do giả định rằng các data point được drawn independently) nên lí thuyết xác
> suất cho ta tách joint pdf thành tích các marginal pdf:
>
> .. = Πi=1:N f(ti|**x**i, **w**, β)
>
> thay kí hiệu f(ti|**x**i, **w**, β) bằng N(ti|y(**x**i, **w**), 1/β) (vì đã nói ở trên, Ti ~ normal(y(**w**, **x**i), 1/β))
>
> .. = Πi=1:N N(ti|y(**x**i, **w**), 1/β)
>
> Tới đây, nhớ lại bối cảnh ở đây là ta đang nói về linear model: với y(**x**i, **w**) = **w**TΦ(**x**i), là hàm
> tuyến tính đối với w và phi tuyến với **x**i (nhờ basis function Φ, nhớ không). Nên ta có:
>
> .. = Πi=1:N N(ti|**w**TΦ(**x**i), 1/β) → Đây là 3.10 (trong sách dùng index variable là n, mình dùng i cũng
> được)
>
> Vậy ta có f(**t**|**X**, **w**, β) = Πi=1:N N(ti|**w**TΦ(**x**i), 1/β)
>
> Ở đây gs nói rằng, trong bài toán regression, ta sẽ chỉ mô hình hóa distribution của T, chứ ko care distribution
> của **X**, (tức các input vector). Cũng như để cho gọn, ta sẽ bỏ bớt **x** trong điều kiện. Đây là bước giải
> thích nếu ko đọc kĩ có thể gây confused.
>
> Vậy ln f(**t**|**X**, **w**, β) = f(**t**|**w**, β) (bỏ **X** cho gọn)
>
> = Πi=1:N N(ti|**w**TΦ(**x**i), 1/β)
>
> Rồi, tiếp theo, như cách làm thông thường đến giờ đã quen, vì kiểu gì mình cũng sẽ đi thiết lập bài toán
> maximize likelihood, và sau đó, chuyển thành bài toán tương đương với hàm ln (nhờ tính monotone của hàm
> ln, nên **w** khiến maximize ln likelihood cũng là maximize likelihood) nên ta sẽ chuẩn bị hàm ln likelihood
> luôn là vừa:
>
> Hàm likelihood, thì như đã nói nhiều lần, theo định nghĩa, là hàm của parameter θ, define bởi L(θ|**x**) =
> f(**x**|θ) (chú ý, đây chẳng có gì là Bayes theorem hay gì cả, nó chỉ là cách người ta define ra hàm likelihood,
> với ý nghĩa là: L(θ|**x**) sẽ thể hiện độ hợp lí của θ, khi giá trị quan sát thấy của **X** là **x**, và độ hợp lí này,
> được tính bằng giá trị của hàm pdf của **X** (**X** ~ f(**x**|θ)) tại observed value **x**. Vậy thì ở đây ln
> likelihood của param **w**, β là:
>
> ln L(**w**, β|**X**,**t**) = ln f(**t**|**X**, **w**, β)
>
> = ln Πi=1:N N(ti|**w**TΦ(**x**i), 1/β)
>
> = ln Πi N(ti|**w**TΦ(**x**i), 1/β) (tự hiểu i chạy từ 1:N)
>
> = ln { Πi { (2π (1/β))^(-1/2) exp{-(ti-**w**TΦ(**x**i))^2/2(1/β)} } }
>
> = ln { Πi { (2π)^(-1/2) β^(1/2) exp{-β(ti-**w**TΦ(**x**i))^2/2} } }
>
> = ln { (2π)^(-N/2) β^(N/2) Πi { exp{-β(ti-**w**TΦ(**x**i))^2/2} } }
>
> = ln[(2π)^(-N/2)] + ln [β^(N/2)] + ln {Πi { exp{-β(ti-**w**TΦ(**x**i))^2/2} }
>
> = (-N/2) ln(2π) + (N/2) ln(β) + Σi { ln {exp{-β(ti-**w**TΦ(**x**i))^2/2} }
>
> = (N/2) ln(β) -( N/2) ln(2π) + Σi {-β(ti-**w**TΦ(**x**i))^2/2}
>
> = (N/2) ln(β) -( N/2) ln(2π) - β Σi {(ti-**w**TΦ(**x**i))^2/2}
>
> Đặt E_D(**w**) = Σi {(ti-**w**TΦ(**x**i))^2/2}
>
> .. = (N/2) ln(β) -( N/2) ln(2π) - β E_D(**w**) → chính là 3.11
>
> (nói chung chỉ là ta dùng tính chất hàm log: log(AB) = log(A) + log(B) thôi ko có gì phức tạp)

<br>

<a id="node-333"></a>

<p align="center"><kbd><img src="assets/0b378ae93d500b65dd4ea8408b4b57ee29873e58.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/2549a27777cb89327f191c0c57672b03e87f97be.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi, như đã biết, đây là bài toán point estimation: tìm hàm số để từ data tính ra estimate tốt cho tham số
> **w**, β. Thì cách tiếp cận phổ biến là MLE: (**w**, β)^mle = argmax_**w**, β {L(**w**, β|**X**, **t**)}.
>
> Và ta có thể giải theo từng biến, tìm **w**^mle trước (hay kí hiệu **w**^ cũng được). Ta có bài toán:
>
> maximize_**w** {L(**w**, β|**X**, **t**)}
>
> và như đã nói trước đây, giải bài toán này (maximum likelhood dưới giả định Gaussian noise) tương
> đương minimize sum squared error:
>
> minimize_**w** E_D(**w**) = Σi {(ti-**w**TΦ(**x**i))^2/2}
>
> Vậy tới đây chỉ là ta đối mặt bài toán tối ưu không ràng buộc, hơn nữa, đây là hàm bậc hai đối với **w**,
> nên ta có bài toán tối ưu lồi, việc tìm được stationary point sẽ đủ kết luận là optimal.
>
> Dùng điều kiện tối ưu cần bậc nhất (first order necessary optimality condition) để tìm stationary point (nơi
> gradient = 0). Đầu tiên chuẩn bị công thức gradient, tức đạo hàm đối với **w**:
>
> ∇ ln L(**w**, β|**X**, **t**) = -∇ E_D(**w**) = - d/d**w** [(Σi {(ti-**w**TΦ(**x**i))^2/2})]
>
> = -(1/2) Σi { d/d**w** ( (ti-**w**TΦ(**x**i))^2)}
>
> Xét d/d**w** (ti-**w**TΦ(**x**i))^2, dùng chain rule:
>
> = d/d(ti-**w**TΦ(**x**i)) [(ti-**w**TΦ(**x**i))^2] . d/d**w** (ti-**w**TΦ(**x**i))
>
> = [2(ti-**w**TΦ(**x**i)) . d/d**w** (ti-**w**TΦ(**x**i))
>
> = [2(ti-**w**TΦ(**x**i)) . [- d/d**w** (**w**TΦ(**x**i))]
>
> = - 2(ti-**w**TΦ(**x**i)) Φ(**x**i)T
>
> (vì **w**TΦ(**x**i) là vector (**w**) → scalar function, áp dụng d/d**x** (**x**T**a**) **=** d/d**x** (aT**x**) =
> aT)
>
> ⇨ ∇ ln L(**w**, β|**X**, **t**) = -(1/2) Σi {- 2(ti-**w**TΦ(**x**i)) Φ(**x**i)T }
>
> = Σi {(ti-**w**TΦ(**x**i)) Φ(**x**i)T}
>
> Điều kiện cần bậc nhất: ∇ ln L(**w**, β|**X**, **t**) = 0
>
> ⇔ Σi {(ti-**w**TΦ(**x**i)) Φ(**x**i)T} = 0
>
> ⇔ Σi {tiΦ(**x**i)T - **w**TΦ(**x**i)Φ(**x**i)T} = 0
>
> ⇔ Σi {tiΦ(**x**i)T} = Σi {**w**TΦ(**x**i)Φ(**x**i)T}
>
> ⇔ Σi {tiΦ(**x**i)T} = **w**TΣi{Φ(**x**i)Φ(**x**i)T}
>
> Phân tích cấu trúc của hai vế:
>
> bên trái, chỉ là tổng của các (scalar ti) × [vector Φ(**x**i) transosed]
>
> bên phải, cái tổng Σi{Φ(**x**i)Φ(**x**i)T}, chính là tổng các N marix rank 1 trong đó mỗi matrix được tạo
> bởi outer product của vector Φ(**x**i) và chính nó. Theo góc nhìn thứ tư của việc nhân hai matrix mình đã
> học trong MIT18.06, nói rằng AB là tích các rank 1 matrix tạo bởi [cột i của A] outer product với hàng i
> của B, thì ta sẽ thấy nếu đặt các cột của A là Φ(**x**i) và các hàng của B là Φ(**x**i)T, thì
> Σi{Φ(**x**i)Φ(**x**i)T} chính là AB. Và dĩ nhiên B = AT, và A = BT, nên cũng có thể thấy đây chính là BTB
> (B tranpose B). Và trong sách, ta sẽ dùng **Φ** thay cho chữ B, là matrix có các hàng là các vector
> Φ(**x**i) transpose, gọi là **DESIGN MATRIX**
>
> Nên từ đó giúp hiểu rằng Σi{Φ(**x**i)Φ(**x**i)T} chính là **Φ**T**Φ**.
>
> Và vế phải sẽ là **w**T(**Φ**T**Φ**)
>
> Đồng thời, với việc đặt ra matrix **Φ** cũng giúp ta thấy vế trái chính là transposed của một linear
> combination của các cột của **Φ**T, bởi bộ hệ số t1,...tN. Vậy, theo góc nhìn nhân matrix với vector trong
> MIT 1806, thì Σi {tiΦ(**x**i)T} chính là (**Φ**T**t**)T = **t**T**Φ**
>
> Do đó Σi {tiΦ(**x**i)T} = **w**TΣi{Φ(**x**i)Φ(**x**i)T} có thể thể hiện bởi:
>
> **t**T**Φ = w**T(**Φ**T**Φ**)
>
> ⇔ **Φ**T**t =** (**Φ**T**Φ**)T**w** (Transposed hai vế)
>
> ⇔ **Φ**T**t =** (**Φ**T**Φ**)**w** (do **Φ**T**Φ** đối xứng nên (**Φ**T**Φ**)T = **Φ**T**Φ**)
>
> Tới đây có thể ôn lại tí, kiến thức MIT 18.06 cũng là sẽ giúp ta hiểu vì sao gs Bishop nói đây là normal
> equation.
>
> Trong 18.06, thầy Strang đã dạy mình về bài toán: Tìm hình chiếu của vector b lên column space của full
> column matrix A, C(A). Lập luận rất đơn giản: Gọi p là hình chiếu của b lên C(A), thì dĩ nhiên vì p ∈ C(A),
> nên p phải có thể được thể hiện bởi linear combination của các C(A) basis, là các cột của A (vì A full
> column rank, nên các cột độc lập, tạo thành một basis của C(A)), nên ta có p = Ax (x bằng nhiêu ko cần
> biết)
>
> Phần dư e = b - p, sẽ vuông góc với C(A), và do đó, nó nằm trong left nullspace của A, kí hiệu N(AT) (N(A
> transpose)), vì hai subspace này orthogonal complement. Như vậy e là solution của equation ATy = 0 ⇨
> ta có ATe = 0.
>
> Thay e = b - p = b - Ax vào, ta có: AT(b - Ax) = 0
>
> ⇔ ATb = ATAx. Đây chính là normal equation.
>
> Nên trong bài toán của ta, **Φ**T**t =** (**Φ**T**Φ**)**w** chính là normal equation.
>
> Nếu tiếp tục với ATb = ATAx, thì ta sẽ lập luận tiếp như sau:
>
> Vì A full column rank, nên ATA full rank, và do đó invertible.Nhân hai vế cho (ATA)inv, ta có x = (ATA)inv
> ATb.
>
> Và như vậy p, là hình chiếu của b lên C(A), sẽ bằng Ax = A(ATA)inv ATb, và từ đó, nếu gọi P = A(ATA)inv
> AT, để rồi p = Pb, thì P chính là matrix giúp chiếu vector b lên C(A) (projection onto C(A) matrix)
>
> Như vậy, y chang như vậy, nhân hai vế cho (**Φ**T**Φ**)inv, ta có:
>
> **Φ**T**t =** (**Φ**T**Φ**)**w** ⇨ **w** = (**Φ**T**Φ**)inv **Φ**T**t**
>
> và đây chính là maximum likelihood estimator của **w**, kí hiệu **w**ML
>
> Và qua việc ôn lại 1806 ở trên thì cũng giúp ta thấy **Φw** chính là **hình chiếu của vector** **t lên
> column space của Φ**, tức C(**Φ**)
>
> Một điểm kiến thức nữa trong MIT 1806 đã học:
>
> Xét equation Ax = b, mình đã biết, nếu A full rank, invertible thì mới có thể có x = Ainv b. Còn trong các
> trường hợp khác thì sao:
>
> Nếu A full column rank, lúc này ATA full rank, nên tồn tại (ATA)inv.
>
> Nhân hai vế của Ax = b với (ATA)inv AT (gọi là left inverse của A), ta có:
>
> (ATA)inv ATAx = (ATA)inv ATb
>
> ⇔ x = (ATA)inv ATb
>
> (chú ý, chưa chắc x là solution của Ax = b, vì Ax = b ⇨ (ATA)inv ATAx = (ATA)inv ATb chứ ngược lại chưa
> chắc đúng, nói cách khác, đây không phải hai phương trình tương đương)
>
> Đặt (ATA)inv ATb này là x', thế ngược vào vế trái: Ax', = A(ATA)inv ATb và lập luận như sau.
>
> Ta thấy với P = A(ATA)inv AT, là matrix chiếu lên C(A) ở trên, thì Ax' ở đây chính là Pb
>
> Tới đây ta chia hai khả năng:
>
> Nếu b ∈ C(A), thì Pb = b, do đó Ax' = b → x' = (ATA)inv ATb chính là solution của Ax = b.
>
> Nếu b không ∈ C(A) thì Pb = p khác b, thì Ax' chỉ là điểm trong C(A) gần với b nhất. x' = (ATA)inv ATb
> **chỉ là hệ số giúp kết hợp C(A) basis để ra hình chiếu của b lên C(A)**.
>
> Hiểu được như vậy, quay lại bài toán machine learning của mình, để thấy rằng:
>
> **w**ML = (**Φ**T**Φ**)inv **Φ**T**t chính là tương ứng với x' trong lập luận trên, để rồi:**
>
> Nó chính là nghiệm của **Φw** = **t** nếu **t** ∈ C(**Φ**), là hệ số giúp combine linearly các cột của **Φ**
> để tạo ra **t**
>
> Còn nếu **t** không thuộc C(**Φ**), thì **w**ML chính là hệ số giúp combine linearly các cột của **Φ** để
> tạo ra điểm trong C(**Φ**) gần với **t** nhất (hình chiếu của t lên C(**Φ**))
>
> Và ta cũng biết trong MIT 1806, cái matrix (ATA)inv AT, là left inverse của A, cũng có tên là
> **Moore-Penrose pseudo-inverse**, kí hiệu A^(+)
>
> Nên giúp ta hiểu ở đây khi gs nói **Φ**^(+) = **Φ**T**Φ**)inv **Φ**T là **Moore-Penrose pseudo-inverse
> của Φ là vậy**
>
> Nói thêm tí xíu rằng cái matrix có tên là **Moore-Penrose pseudo-inverse của Φ** có có nhiều hình dạng.
>
> Như ở trong tình huống trên, nó là **left inverse**, giúp ta giải bài toán khi Ax = b và A full column rank, và
> b nằm ngoài C(A), thì nó sẽ giúp ta có AA^(+)b là điểm nằm trong C(A) gần b nhất, để và x' = A^(+)b có
> thể **coi như nghiệm gần đúng (hay nói theo giáo sư Strang là, nghiệm tốt nhất, best solution)** của bài
> toán Ax = b
>
> Nhưng trong còn trường hợp khác nữa: Khi A là matrix m × n mập lùn, có cột tự do, đồng nghĩa có
> nullspace vector, và giả sử C(A) span toàn bộ R^m, để b ∈ C(A). Thì lúc này, phương trình Ax = b, như
> đã biết, sẽ có vô số nghiệm có dạng x_complete = x_particular
> \+ x_null
>
> Khi đó A^(+) sẽ là **right inverse** = AT (AAT)inv, **giúp tìm ra cái x có norm nhỏ nhất**, như sau:
>
> Bối cảnh lúc này là ta có vô số solution x có dạng = x_particular + x_null, với việc có thể scale x_null tùy
> ý khiến ta có vô số nghiệm của Ax = b. Nhiệm vụ là lấy ra x_particular, vì khi đó, ||x|| = ||x_particular|| sẽ
> luôn ≤ ||x_particular + x_null||.
>
> Thế thì x, là một solitution của Ax = b luôn có thể tách ra làm hai phần: x* nằm trong rowspace, và z nằm
> trong nullspace. Và vì rowspace và nullspace orthogonal complement, nên x* chính là nghiệm có norm
> nhỏ nhất (chú ý, x_particular chưa chắc đã là x*, vì nó có thể không nằm trong rowspace, phải chiếu nó
> lên rowspace thì mới có x*, phần dư sẽ vào nullspace)
>
> Vậy ta lại dựa vào lập luận, vì x* nằm trong rowspace, nên tồn tại linear combination các rows của A tạo
> ra x*: ATy = x*, phần dư nằm trong nullspace x - ATy ⇨ A(x - ATy) = 0 ⇔ Ax - AATy = 0 ⇔ b = AATy ⇔ y =
> (AAT)inv b.
>
> Vậy x* = ATy = AT(AAT)inv b chính là nghiệm có norm nhỏ nhất trong vô số nghiệm của Ax = b
>
> Và cái A^(+) lúc này chính là right inverse của A, AT(AAT)inv, giúp tìm ra nghiệm có norm nhỏ nhất.
>
> Còn khi A invertible, thì đơn giản A^(+) chính là Ainv, vì dùng left hay right inverse thì đều ra Ainv cả:
>
> (ATA)inv AT = Ainv (AT)inv AT = Ainv I = Ainv
>
> AT(AAT)inv = AT (AT)inv Ainv = I Ainv = Ainv
>
> Trong cả hai ta đều dùng tính chất (AB)inv = Binv Ainv (identity này chỉ đúng khi A, B invertible)
>
> Điều này giải thích câu cuối, khi gs nói nếu **Φ** vuông và invertible, thì thì **Φ**^(+) = **Φ**inv

<br>

<a id="node-334"></a>

<p align="center"><kbd><img src="assets/73390c4599f18573bc45944b4ecbce16fc438a99.png" width="100%"></kbd></p>

> [!NOTE]
> Ý tưởng đoạn này đại khái là muốn xem thử với **w**ML, tức maximum likelihood estimator
> của **w** thì **w**0 là cái gì?
>
> Thì lôi cái phần từ đầu tiên của **w**ML ra (chính là w0_ML) sẽ khó hơn là làm theo cách
> này: Dù gì thì **w**ML cũng là cái có được khi ta giải first condition d/d**w** log Likelihood =
> 0, và cũng tương đương d/d**w** E_D(**w**) = 0. Và bản chất cái này cũng chỉ là hệ các
> phương trình ∂/∂wi E_D(**w**) = 0. Trong đó có ∂/∂w0 E_D(**w**) = 0. Nên bằng cách giải
> ∂/∂w0 E_D(**w**) = 0, ta sẽ có w0_ML (phần tử đầu tiên của **w**ML), từ đó thông qua việc
> xem nó là gì sẽ giúp ta hiểu về vai trò của w0, vốn là tham số không gắn với hàm Φi(**x**)
> nào.
>
> Tự làm để hiểu: E_D(**w**), còn nhớ, là hàm đặt cho (1/2) Σi (ti - **w**T**Φ**(**x**))^2 = (1/2)
> Σi (ti - Σj=0:M-1 wj × Φ(**x**i))^2
>
> Dưới đây để cho gọn Σj tức là Σj=1:M-1, Σi tức là Σi=1:N
>
> = (1/2) Σi (ti - w0 × Φ0(**x**j) - Σj wj × Φj(**x**i))^2
>
> = (1/2) Σi (ti - w0 × 1 - Σj wj × Φj(**x**i))^2 (Φ0(**x**j) = 1, nhớ không)
>
> = (1/2) Σi (ti - w0 - Σj wj × Φj(**x**i))^2
>
> d/dw0 = 0
>
> ⇔ d/dw0 [(1/2) Σi (ti - w0 - Σj wj × Φj(**x**i))]^2 = 0
>
> ⇔ (1/2) (-2) (Σi ti - Σi w0 - Σi[Σj wj × Φj(**x**i))] ) = 0
>
> ⇔ (Σi ti - Σi w0 - Σi[Σj wj × Φj(**x**i))] ) = 0
>
> ⇔ Σi w0 = Σi ti - Σi[Σj wj × Φj(**x**i))]
>
> ⇔ N w0 = Σi ti - Σj [wj × Σi Φj(**x**i)]
>
> ⇔ w0 = (Σi ti)/N - Σj [wj × (1/N)Σi Φj(**x**i)]
>
> Đặt (Σi ti)/N là t^ (trong sách là t bar) là trung bình của các t
>
> và (1/N)Σi Φj(**x**i) là Φj^, là trung bình của các phần tử j của các vector Φ(**x**i). Mà Φ(**x**)
> như đã nói, là basis function, là function mà ta dùng để tạo ra một set các non-linear feature,
> nên Φj(**x**) có thể coi là feature thứ j của sample **x**. Vậy (1/N)Σi Φj(**x**i) là trung bình
> các feature thứ j
>
> Như vậy Σj [wj × (1/N)Σi Φj(**x**i)] sẽ là weighted sum của các trung bình của các feature.
>
> Nói cụ thể cho dễ hiểu, giả sử x1 là diện tích nhà, x2 là chiều dài nhà, x3 là số lầu,...thì
> Φ1(**x**) là quy mô căn nhà (là hàm phi tuyến nào đó dựa trên các feature gốc x1, x2,...,
> Φ2(**x**) là ưu thế về vị trí của căn nhà (cũng là hàm phi tuyến nào đó của feature gốc). Khi
> đó (1/N) Σi Φ1(**x**i) sẽ là trung bình các quy mô căn nhà trong mọi căn nhà (**x**i) trong
> dataset, (1/N) Σi Φ2(**x**i) là trung bình ưu thế về vị trí của mọi căn nhà. Và Σj [wj × (1/N)Σi
> Φj(**x**i)] = w1 × (1/N) Σi Φ1(**x**i) + w2 × (1/N) Σi Φ2(**x**i) + ...chính là tổng tất cả các trung
> bình trên, nhưng có trọng số là w1,w2,....
>
> Do đó, từ việc w0 = (Σi ti)/N - Σj [wj × (1/N)Σi Φj(**x**i)]  cho thấy rằng mô hình sẽ học ra cách
> (nói vậy là vì, w0 ta đang xét chính là maximum likelihood estimator của w0, là thứ mà ta tìm
> được để tối ưu likelihood) để BÙ ĐẮP (compensate) cho sự thiếu hụt giữa trung bình target
> value (t^) và weighted sum của trung bình các basis function values.

<br>

<a id="node-335"></a>

<p align="center"><kbd><img src="assets/57749c70b2868c71feac9f283d229b90f6e6bb75.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/99cfbbd39769aace45bb0467eb427d0d84289f44.png" width="100%"></kbd></p>

> [!NOTE]
> Ok, nãy giờ là ta chỉ nói về **w**ML, đương nhiên tham số mô hình còn có
> β - precision của distribution Normal mà ta assump rằng noise ε = T -
> y(**w**,**x**) sẽ theo phân phối này.
>
> Để tìm βML, thì cũng chỉ đơn giản là cho đạo hàm của hàm log likelihood
> (**w** ở đây đều là **w**ML) đối với β = 0:
>
> d/dβ [(N/2) ln(β) -( N/2) ln(2π) - β E_D(**w**)] = 0
>
> ⇔ d/dβ [(N/2) ln(β)] - d/dβ [β E_D(**w**)] = 0
>
> ⇔ d/dβ [(N/2) ln(β)] = d/dβ [β E_D(**w**)]
>
> ⇔(N/2) (1/β) = E_D(**w**)
>
> ⇔ 1/β = 2E_D(**w**)/N = (2/N) (1/2) Σi (ti - Σj=0:M-1 wj × Φj(**x**i))^2
>
> = (1/N) Σi (ti - Σj=0:M-1 wj × Φj(**x**i))^2
>
> Và đây chính là (1/β)ML (tức maximum likelihood estimator của 1/β, hay
> cũng là σ^2_ML)
>
> Chỗ này nói rõ chút: Nên nhớ từ đầu đến giờ ta dựa trên assumption là
> noise, cũng là residual = phần dư, phần sai lệch của T sau khi trừ đi
> y(**w**,**x**), sẽ là random variable tuân theo normal(0, 1/β), và đièu này
> cũng đồng nghĩa rằng ta đang assume T ~ normal(y(**w**,**x**), 1/β). Với
> 1/β là ngịch đảo của precision, cũng chính là variance. Nên giờ khi ta
> dùng maximum likelihood esimator approach để tìm esimator cho 1/β
> (1/β)ML, thì cũng chính là maximum likelihood estimator cho variance của
> Normal distribution noise.
>
> Và kết quả cho ra (1/β)ML = σ^2_ml = (1/N) Σi (ti - Σj=0:M-1 wj ×
> Φj(**x**i))^2, thì cho ta gì?
>
> kết quả này là trung bình bình phương residual, nhưng nhìn theo góc nhìn
> thống kê thì sẽ thấy nó chính là sample variance của ε
>
> Đầu bài ta đã nói rằng T là random variable, nên các data sample hình
> thành một bộ các random variable T1,T2,...TN. Và tương ứng với mỗi T ta
> có εi = Ti - y(w, **x**i), cũng là các random variable.
>
> Như vậy ta cũng có một bộ ε1, ε2,...εN, làm thành một sample, có
> distribution đều là N(0, 1/β). Và ε1,...εN độc lập, nên theo khung xác suất
> thống kê thì ta đang có một random sample size N ε1, ..εN iid independent
> identically distribution, có cùng distribution N(0, 1/β)
>
> Variance, Var(ε) = E[ε^2] - [E(ε)]^2
>
> Nhưng vì residual ε có mean là 0: E[ε] = 0, nên: Var(ε) = E[ε^2]
>
> và (1/N) Σi (εi^2) có thể coi như một giá trị thực nghiệm ước lượng mức
> biến động của ε
>
> và mang ý nghĩa cho thấy trung bình độ biến động của Ti xung quanh
> mean y(**x**i,w)
>
> Và cái này giúp ta hiểu vì sao mr Bishop nói "we see that the inverse of
> the noise precision is given by the residual variance of the target values
> around the regression function"

<br>

