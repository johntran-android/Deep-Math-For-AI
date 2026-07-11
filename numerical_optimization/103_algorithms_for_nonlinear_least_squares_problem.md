# 10.3 Algorithms for nonlinear least-squares problem

📊 **Progress:** `2` Notes | `2` Screenshots | `2` AI Reviews

---

<a id="node-76os6gb"></a>
## The Gauss-Newton Method

<p align="center"><kbd><img src="assets/att_koqh0n3.png" width="80%"></kbd></p>

> [!NOTE]
> Đầu tiên vẫn là nói về việc giải bài toán least-square: minimize f(x) = Σi ri(x)^2 (10.1)
>
>
>
> Còn nhớ trong 10.2, khi nói rằng hàm Φ(x, ti) là hàm tuyến tính theo x, dẫn đến ri(x) = Φ(x, ti) - yi cũng là linear (đúng hơn là affine) function theo x, thì khi đó hàm vector x → vector r(x) = \[r1(x), r2(x),..\] có thể được thể hiện bởi: r(x) = Jx, để rồi Σi ri(x)^2 có thể được thể hiện bởi ||Jx - y||^2. Lúc này bài toán được gọi là linear least-square.
>
>
>
> Thế thì mình cần hiểu, **không phải là vì hàm objective là hàm tuyến tính theo x**. Không hề, vì **ngay cả khi r(x) là linear thì objective vốn là r(x)Tr(x), vẫn là hàm non-linear theo x**. Ta chỉ gọi là **linear least square bởi vì r(x) là linear function của x mà thôi**, và khi không có điều này, thì dĩ nhiên bài toán là non-linear least square.
>
>
>
> Rồi, thế thì, ở phần trước (10.2) với việc hàm r(x) tuyến tính, dẫn đến bài toán được đơn giản hóa, khiến việc giải ra nghiệm chỉ là giải normal equation, nói cách khác, ta có closed form solution từ ta có thể giải theo cách direct (dùng Cholesky factorization, QR factor based method, hoặc SVD based method) method - mà cơ bản chỉ là dùng đại số tuyến tính để giải, (trừ bài toán lớn thì dùng Conjugate gradient - mới là thuật toán tối ưu)
>
>
>
> Qua phần này, ta phải quay lại thực tế, là bài toán không đơn giản như 10.2, tuy nhiên, ở phần mở màn của chapter này, gs Nocedal đã nói rằng, bài toán least square mang vài đặc điểm thuận lợi hơn các bài toán khác, mà ta có thể khai thác. Cụ thể, là **gradient và Hessian cuả nó trong nhiều trường hợp là dễ tính** (ít tốn kém), thì đây chính là lúc ta nói về chuyện này. (có nghĩa cần hiểu bức tranh là, ở 10.2, ta chưa cần khai thác đặc điểm này, đơn giản là vì với bài toán linear least square, mọi chuyện được đơn giản hóa hơn nhiều, để rồi bây giờ mới nói về việc khai thác đặc điểm "**free Hessian**" của bài toán least-square.

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **95/100**
>
> Ghi chú giải thích rất sâu sắc về sự khác biệt giữa các bài toán least-square tuyến tính và phi tuyến, đồng thời làm rõ tầm quan trọng của việc khai thác cấu trúc gradient và Hessian. Việc liên hệ với phần 10.2 giúp người đọc dễ dàng nắm bắt bối cảnh và lý do tại sao phương pháp này được giới thiệu.

<br>


<a id="node-2yk17h9"></a>
### Gauss-Newton Method Approximation

<p align="center"><kbd><img src="assets/att_kgaeowx.png" width="80%"></kbd></p>

> [!NOTE]
> Rồi, thế thì trước tiên nên nhắc lại công thức của gradient và Hessian của objective mà trong 10.1 mình đã tự derive:
>
>
>
> ∇f(x) = J(x)Tr(x) (10.4)
>
>
>
> ∇^2f(x) = J(x)TJ(x) + Σi {∇^2ri(x) ri(x)} (10.5)
>
>
>
> Thế thì đại khái lập luận là như sau: Như đã nói nhiều lần trong các chapter trước, cũng như trong Convex Optimization S.Boyd, ta đã thấy rằng, với các cách tiếp cận iterative để giải bài toán tối ưu, thì cơ bản đều có cùng một bản chất: Ta bắt đầu từ điểm nào đó, và tìm cách di chuyển dần đến minimizer của hàm mục tiêu. Và việc đánh giá một thuật toán tối ưu hiệu quả nhiều hay ít chỉ xoay quanh một vấn đề: Chi phí. Chi phí ở đây, có thể hiểu bao gồm tính khả thi đạt được sự hội tụ về minimizer cũng như chi phí tính toán và thời gian để đạt được. Thuật toán hiệu qủa sẽ thể hiện ở chỗ hội tụ nhanh cũng như chi phí tính toán các bước thấp.
>
> \
> Và Newton method được chứng minh là có tốc độ hội tụ nhanh, như đã học bên Conv Opt, khi bước vào Newton phase (đủ gần minimizer) thì tốc độ hội tụ sẽ là quadratic (gọi là quadratic convergence)
>
>
>
> Vấn đề là, để có Newton direction, ta sẽ phải có Hessian. Ôn lại nhanh Newton direction:
>
>
>
> Ý tưởng rất đơn giản: tại điểm đang đứng, ví dụ gọi là x0, ta sẽ coi như hàm số là hàm bậc hai: f(x) ≈ f(x0) + ∇f(x0)(x - x0) + (1/2)(x-x0)T ∇^2f(x0)(x-x0). Đặt đây là hàm g(p) = f(x0) + ∇f(x0)p + (1/2)pT∇^2f(x0)p (p = x - x0). Câu chuyện tiếp theo sẽ là, tìm minimizer của hàm quadratic g(p), bằng closed-form solution:
>
>
>
> ∇g(p) = 0 ⇔ ∇^2f(x0)p + ∇f(x0) = 0 (đây là cái mà gs gọi là standard Newton equation ∇^2f(xk)p = - ∇f(xk))
>
>
>
> ⇔ p = - \[∇^2f(x0)\]inv ∇f(x0)
>
>
>
> Đây chính là Newton direction (Newton step), có nghĩa là từ x0 chỉ cần phóng theo p ta sẽ tới x0 - \[∇^2f(x0)\]inv ∇f(x0) chính là điểm sẽ minimize hàm g(p).
>
>
>
> Như vậy, có thể thấy để có được Newton Step, ta sẽ cần gradient và Hessian tại xk.
>
>
>
> Và việc tính Hessian quá tốn kém chính là trở ngại của việc dùng Newton method.
>
>
>
> Thế thì, trong bài toán Least Square, gs nói có 2 đặc điểm:
>
>
>
> i) Đầu tiên, dễ thấy là Hessian có hai term, thì một term là J(x)TJ(x), thì term trong nhiều trường hợp, sẽ lấn át (dominant) term thứ hai, khiến cho việc bỏ đi term thứ hai không gây ra sai lệch nhiều, hay nói cách khác, chỉ dùng term thứ nhất cũng có thể xấp xỉ tốt Hessian, dẫn đến thuật toán này (gọi là Gauss-Newton) sẽ vẫn đạt tốt độ hội tụ nhanh như Newton thứ thiệt.
>
>
>
> ii) Và ý thứ hai đó là, việc tính gradient J(x)Tr(x) rồi thì tính thêm cái cục J(x)TJ(x) sẽ không tốn thêm mấy (là vì đã tính ra J(x) phục vụ cho việc tính gradient rồi thì tính J(x)TJ(x) chỉ là nhân matrix matrix, không tốn thêm gì nhiều)
>
>
>
> Tóm lại, vì hai đặc điểm này, nên ta dùng J(x)TJ(x) thay cho ∇^2f(x), để rồi Newton equation (giúp giải tìm Newton step) sẽ là:
>
>
>
> J(xk)TJ(xk)p = - J(xk)Trk
>
>
>
> hay viết gọn là JkTJk p = - JkTrk
>
>
>
> Một ý cuối đó là, cái vụ term J(x)TJ(x) dominate term thứ hai thường xuất hiện trong các bài toán mà residual nhỏ, hoặc chúng là hàm gần tuyến tính, và đây là những yếu tố xuất hiện nhiều trong cái bài toán thực tế, giúp cho việc dùng Gauss Newton sẽ có tác dụng.

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **97/100**
>
> Bài viết giải thích rất chi tiết và chính xác về lý do và cách thức phương pháp Gauss-Newton sửa đổi so với phương pháp Newton tiêu chuẩn, bao gồm cả hai đặc điểm chính đã được nêu bật trong văn bản. Độ sâu của phân tích rất tốt, tuy nhiên, phần mở đầu có thể ngắn gọn hơn một chút để đi thẳng vào vấn đề chính sớm hơn.

<br>

