# 5.1 Linear Conjugate Gradient

📊 **Progress:** `5` Notes | `9` Screenshots | `2` AI Reviews

---

<a id="node-5lfpgbu"></a>
## 5.1 Linear Conjugate Gradient

<p align="center"><kbd><img src="assets/img_5lfpgbu.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_a0l33s.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_jom8rf.png" width="80%"></kbd></p>

> [!NOTE]
> Qua một phương pháp mới: Conjugate gradient method. Đại khái là tác giả nói nó có hai ưu điểm: Thứ nhất đây là một trong nhưng phương pháp tốt nhất để giải một hệ phương trình tuyến tính quy mô lớn. Và thứ hai, nó cũng có thể được điều chỉnh để giải hệ phương trình phi tuyến.
>
> Nói sơ, linear conjugate gradient được phát triển năm 1950, là các tiếp cận iterative, để giải hệ tuyến tính với ma trận hệ số xác định dương. Nó phù hợp hơn phép khử Gausse, vốn đã học ở MIT 18.06 cho những bài toán quy mô lớn.
>
> Hiệu quả của phương pháp này chủ yếu là phụ thuộc vào phân bố của trị riêng của matrix hệ số. Bằng cách transforming, còn gọi là pre-conditioning, ta có thể cải thiện sự phân bố của các trị riêng, giúp bài toán hội tụ nhanh hơn. 
>
> Nói sơ về non-linear conjugate gradient method, thì key feature của nó là nó ko đòi hỏi phải lưu trữ matrix, và nó nhanh hơn là phương pháp steepest descent.

<br>


<a id="node-hpdy8sw"></a>
### 5.1 The Linear Conjugate Gradient Method

<p align="center"><kbd><img src="assets/img_hpdy8sw.png" width="80%"></kbd></p>

> [!NOTE]
> Đại khái là, tác giả nói một điều mà mình đã học / tự nhận ra hồi còn học EE364A: Việc giải hệ f(x) = 0 có thể coi như là đang giải điều kiện cần bậc một của bài toán minimize hàm số F(x) là nguyên hàm của f: ∇F(x) = f(x) = 0. Và đây là nguyên lí của root finding Newton method: Bằng cách xấp xỉ hàm F bằng hàm bậc 2 thì ta cũng xấp xỉ hàm f là hàm bậc 1.
> Và giải bài toán minimize F với Newton method cũng chính là gỉai hệ f(x)=0 bằng root finding Newton method.
>
> Thế thì ở đây f(x) = Ax - b, thì nguyên hàm của nó, chính là F(x) = (1/2)xTAx - bTx, ở đây ta sẽ gọi là φ(x) ⇨ ∇φ(x) = Ax - b 
>
> Và như đã nói, cách nhìn này cho ta thấy việc giải hệ Ax = b chính là giải bài toán tối ưu hàm bậc hai F(x), là một convex optimzation problem.

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **98/100**
>
> Your analysis accurately captures the equivalence between solving Ax=b and minimizing φ(x), and correctly derives the gradient. Connecting this specific problem to the broader principle of root-finding and Newton's method demonstrates a profound understanding of the underlying mathematical concepts.

<br>


<a id="node-0lu7h6i"></a>
#### Conjugate Direction Method

<p align="center"><kbd><img src="assets/img_0lu7h6i.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_eda7t.png" width="80%"></kbd></p>

> [!NOTE]
> Đầu tiên, tác giả nói đại ý là một đặc điểm rất tốt của phương pháp này là khả năng của nó trong việc tạo ra một bộvector có tính chất gọi là conjugacy: {p0,...pn-1} được gọi là conjugate wrt matrix xác định dương A nếu như piTApj = 0 ∀i≠j.
>
> Tác giả nói cũng dễ cho thấy bộ vector conjugate cũng sẽ độc lập tuyến tính. Là sao?
>
> Giả sử có pk là vector phụ thuộc tuyến tính, ta có thể thể hiện nó bởi tổ hợp tuyến tính các vector còn lại: pk = Σi pi. Áp dụng tính chất conjugacy:
>
> pkTApj = 0 ∀k≠j
>
> ⇔ pkT(Σi pi)pj = 0 ∀k≠j
>
> ⇔ (Σi pi)TApj = 0 ∀k≠j
>
> ⇔ Σi piTApj = 0 ∀k≠j
>
> Trong cái tổng bên phải, nếu pi khác pj thì hạng tử bằng 0 rồi, nên chỉ còn pjApj.
>
> Tức là ta có pjTApj = 0, mà điều này sẽ mâu thuẫn với việc A xác định dương thì với mọi x khác 0, xTAx > 0. Do đó, đại ý là ta đã chứng minh được bộ vector conjugate cũng sẽ độc lập tuyến tính.
>
> Tiếp theo, tác giả nói về việc, ta có thể chứng minh được rằng, sử dụng bộ vector conjugate, ta có thể minimize hàm φ chỉ trong n bước. Và ta sẽ xét một phương pháp gọi là CONJUGATE DIRECTION method (không phải conjugate gradient method nhé, sự liên hệ giữa chúng sẽ nói sau). Phương pháp này đại khái là như sau:
>
> Bắt đầu với x0, và một bộ vector conjugate {p0,...pn-1}, ta sẽ generate các điểm xk:
>
> xk+1 = xk + αkpk trong đó αk là solution của bài toán tối ưu hàm một biến:
>
> minimize g(α) = φ(xk + αpk) 
>
> Để giải tìm αk, dùng điều kiện cần bậc 1 thôi: 
>
> g'(α) = 0 ⇔ d/dα φ(xk + αpk) = 0 
>
> ⇔ d/d(xk + αpk) φ(xk + αpk) . d/dα (xk + αpk) = 0
>
> ⇔ ∇φ(xk + αpk) . pk = 0 
>
> ⇔ ∇φ(xk + αpk)T pk = 0 
>
> ⇔ [(Ax - b)|x=xk + αpk]Tpk = 0
>
> ⇔ [A(xk + αpk) - b]Tpk = 0
>
> ⇔ [Axk + Aαpk - b]Tpk = 0
>
> ⇔ [rk + Aαpk]Tpk = 0 | Ở đây quên nói, ta sẽ gọi r(x) = Ax-b 
>
> ⇔ rkTpk + αpkTApk = 0
>
> ⇔ α = -rkTpk/pkTApk. Đây chính là 5.7

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **90/100**
>
> Bạn đã nắm vững các định nghĩa cốt lõi và thực hiện xuất sắc việc chứng minh công thức alpha_k một cách chi tiết và chính xác. Để nâng cao hơn nữa, hãy xem xét lại cách thiết lập giả định và các bước chứng minh tính độc lập tuyến tính của các vector liên hợp để đảm bảo tính chặt chẽ.

<br>


<a id="node-g0algzt"></a>
##### Theorem 5.1

<p align="center"><kbd><img src="assets/img_g0algzt.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_rac4od.png" width="80%"></kbd></p>

> [!NOTE]
> Theorem 5.1: Nói rằng với x0 (initial point) bất kì thì chuỗi {xk} được generate bởi thuật toán 5.6 ở trên sẽ converge về solution x* của Ax = b trong nhiều nhất là n step.
>
> Chứng minh như sau: Đầu tiên, vì {pi} độc lập tuyến tính, và đủ số lượng (n) nên dĩ nhiên chúng là một basis của R^n, span {p0,..pn-1} = R^n. Nên mọi vector R^n đều là linear combination của chúng. Do đó gs nói ta có thể thể hiện x* - x0 (cũng là R^n vector) bởi:
>
> x* - x0 = σ0p0 + σ1p1 + ..σn-1 pn-1.
>
> Nhân hai vế cho pkTA ta có:
>
> pkTA(x* - x0) = pkTA(σ0p0 + σ1p1 + ..σn-1 pn-1)
>
> Xét vế phải, phân phối vô ta có tổng các pkTAσipi, vì tính conjugacy nên nếu pi khác pk, kết quả thành 0. Nên chỉ còn pkTApk, ta có pkTA(x*-x0) = σkpkTApk
>
> ⇔ σk = pkTA(x*-x0)/pkTApk (5.8)
>
> Giờ ta sẽ đi chứng minh σk TRÙNG KHỚP với step length αk của công thức 5.7. Là sao?
> ⇨ Thì khi ta chứng minh σk = αk thì cũng đã chứng minh là chuỗi {xk} tạo bởi x1 = x0 + α0p0, x2 = x1 + α1p1,...cũng chính là sẽ là đi từ x0 → x1 = x0 + σ0x0, x2 = x0 + σ0x0 + σ1x1 , ... xn = x0 + σ0p0 + σ1p1 + ...σn-1pn-1 = x0 + x* - x0 = x*! Có nghĩa là ta cũng đã chứng minh được thuật toán sẽ dẫn ta đến x* tại iteration thứ n.
>
> Về mặt hình học hiểu nôm na như sau: Như đã biết về ý nghĩa của x* - x0 = σ0p0 + σ1p1 + ..σn-1 pn-1: Đó là để đi từ x0 → x*, ta sẽ đi thep phương p0 một khoảng có độ lớn σ0, rồi từ đó đi theo phương p1 một khoảng có độ lớn σ1,... Vậy thì nếu chứng minh αk = σk thì dĩ nhiên cũng đã chứng minh chuỗi {xk} tạo bởi thuật toán cũng sẽ dẫn ta tới x* sau n bước.
>
> Quay lại đây, chuỗi {xk} tạo bởi 5.6, 5.7: xk+1 = xk + αkpk, và αk = -rkTpk/pkTApk, cụ thể sẽ là:
>
> x1 = x0 + α0p0
>
> x2 = x1 + α1p1 = x0 + α0p0 + α1p1
>
> ...
>
> xk = xk-1 + αkpk = x0 + α0p0 + α1p1 + ..αk-1pk-1
>
> Nhân hai vế cho pkTA:
>
> pkTAxk = pkTAx0 + pkTA(α0p0 + α1p1 + ..αk-1pk-1)
>
> ⇔ pkTAxk - pkTAx0 = pkTA(α0p0 + α1p1 + ..αk-1pk-1)
>
> ⇔ pkTA(xk - x0) = pkTA(α0p0 + α1p1 + ..αk-1pk-1)
>
> Vế phải, theo tính chất conjugate, dễ hiểu chỉ còn 0, ta có pkTA(xk - x0) = 0
>
> ⇔ pkTAxk = pkTAx0
>
> Từ đó cái tử số của σk = pkTA(x*-x0)/pkTApk sẽ bằng:
>
> pkTA(x* - x0) = pkTAx*- pkTAx0 = pkTAx*-pkTAxk = pkT(Ax*-Axk)
>
> = pkT(b-Axk) Và vì rk = Axk-b nên đây chính là -pkTrk
>
> Vậy σk = pkTA(x*-x0)/pkTApk = -pkTrk/pkTApk, chính là αk. Chứng minh xong

<br>

<p align="center"><kbd><img src="assets/img_aads1j4.png" width="80%"></kbd></p>

> [!NOTE]
> Nếu A là diagonal, A = diag(λ1,...,λn), contour của Φ(x) sẽ có dạng:
>
> Φ(x) = c (c-level set)
>
> ⇔ (1/2)xTAx - bTx = c
>
> ⇔ (1/2)xTdiag(λ1,...,λn)x - bTx = c
>
> ⇔ (1/2)xT(λ1x1, ..λnxn) - bTx = c
>
> ⇔ λ1x1^2 + .. + λnxn^2 - (b1x1+..bnxn) = c

<br>

