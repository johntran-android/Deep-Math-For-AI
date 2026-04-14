# 7.1 Inexact Newton Methods

📊 **Progress:** `4` Notes | `5` Screenshots | `3` AI Reviews

---

<a id="node-pvuqi1m"></a>
## Tối ưu không ràng buộc quy mô lớn

<p align="center"><kbd><img src="assets/img_pvuqi1m.png" width="80%"></kbd></p>

<br>

<p align="center"><kbd><img src="assets/img_sijdcir.png" width="80%"></kbd></p>

> [!NOTE]
> Đại khái là gs nói trong thực tế có nhiều bài toán tối ưu rất lớn (hàng triệu  variable, mà ở thời kì AI ngày nay là hàng trăm tỉ variables) Do đó, yêu cầu đặt ra là cần các thuật toán tối ưu có thể giữ chi phí lưu trữ cũng như tính toán các biến số ở mức chấp nhận được. Từ đó ra đời các thuật toán tối ưu quy mô lớn này.
>
> Cách tiếp cận thì một số dùng trực tiếp các thuật toán cơ bản, một số thì chỉnh sửa sao cho giảm chi phí tính toán. Mà trong số đó non-linear conjugate method là một ví dụ (nhưng ta  bỏ qua method này trong 5.2 vì nhiều nhược điểm khiến ngày nay không ai xài nữa)

> [!TIP]
> **🤖 AI Feedback** — ⚠️ Score: **70/100**
>
> Bạn đã tóm tắt tốt về nhu cầu đối với các thuật toán tối ưu quy mô lớn và cách tiếp cận đa dạng. Tuy nhiên, thông tin về việc phương pháp gradient liên hợp phi tuyến (nonlinear conjugate gradient method) không còn được sử dụng do nhiều nhược điểm chưa hoàn toàn chính xác theo nội dung văn bản gốc, vì đoạn văn chỉ ra ưu điểm của nó cho các bài toán lớn.

<br>


<a id="node-no4xt3p"></a>
#### Phân rã thưa trong Newton

<p align="center"><kbd><img src="assets/img_no4xt3p.png" width="80%"></kbd></p>

> [!NOTE]
> Chỗ này đại khái là với line search Newton và trust region Newton thì mình cần factor Hessian bởi vì mình cần tính pk: = (Hk)inv gk
>
> Vì sao lại factor, là vì đang ám chỉ dùng factor-solve method để tìm inverse của Hessian, hoặc là nói cách khác, là để giải hệ [Hessian tại k] pk = - ∇fk
>
> Vì thực tế khi tìm pk, tuy là công thức nói ta sẽ pk = - (∇^2fk)inv ∇fk nhưng ta sẽ không tính inverse của Hessian, mà dùng factor-solve method để giải tìm pk.
>
> Ví dụ bước 1 ta factor ∇^2fk = LLT, thì giải ∇^2fk pk = - ∇fk tương đương giải LLT pk = - ∇fk. 
>
> bước 2: giải L y = - ∇fk. và sau đó là LT pk = y, đều là hệ tuyến tính với matrix hê số tam giác (L hay LT) ⇨ giải bằng back hay forward substitution chỉ tốn o(n^2)
>
> Do đó, ở đây gs Nocedal nói, nếu việc phân rã này không quá tốn kém và Hessian matrix có thể được hình thành một cách tường minh. Thì ta có thể xài phép phân rã spase (ví dụ = LLT chính là sparse factorization, vì nó tạo ra các matrix spare) để làm.

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **96/100**
>
> Bài giải thích rất chính xác về lý do cần phân rã ma trận Hessian và phương pháp giải hệ tuyến tính bằng factor-solve thay vì tính nghịch đảo. Độ sâu của phân tích, đặc biệt là việc giải thích các bước giải và độ phức tạp O(n^2), cho thấy sự hiểu biết sâu sắc về các phương pháp số.

<br>


<a id="node-ornbsjg"></a>
##### In-exact Newton

<p align="center"><kbd><img src="assets/img_ornbsjg.png" width="80%"></kbd></p>

> [!NOTE]
> Đại khái là, gs nói rằng trong thực tế thì thường là việc phân rã Hessian rất tốt kém, nên không thể dùng sparse factorization như note trước vừa nói được.  Khi đó một cách tiếp cận là GIẢI TÌM NEWTON STEP THEO LỐI ITERATIVELY, gọi là inexact Newton method. Cái này cũng có nhiều tính chất tốt, thậm chí có thể đạt hội tụ siêu tuyến tính. Và nó còn có thể tìm ra hướng đi hiệu quả ngay cả khi Hessian bị indefinite và thậm chí còn có thể có một tính chất tốt hơn nữa, đó là có thể được thực hiện theo lối "Hessian free" - tức hoàn toàn không cần tính hay lưu trữ Hessian.
>
> Nói thêm chút, cái này mình đã học bên Convex với gs Boyd. Ý tưởng giải Newton step theo lối iteratively đơn giản là: Bản chất giải tìm Newton step, chỉ là giải hệ ∇^2f p = - ∇f. Và ta đã biết có cách giải hệ này theo lối iteratively, đây chính là cách tiếp cận đang được nói đến.

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **95/100**
>
> Bài tóm tắt rất đầy đủ và chính xác các ý chính từ đoạn văn, đồng thời thể hiện sự hiểu biết sâu sắc khi giải thích thêm về bản chất của việc giải Newton step theo lối lặp. Cần lưu ý một chút về dấu của phương trình hệ tuyến tính ∇²f p = -∇f để đảm bảo hoàn hảo về mặt công thức.

<br>

<p align="center"><kbd><img src="assets/img_em8ep7s.png" width="80%"></kbd></p>

> [!NOTE]
> Đoạn này đại khái nói rằng các matrix xấp xỉ Hessian có được nhờ quasi-Newton method trong chap 6 mình học thường là dense, kể cả khi Hessian thật sparse, do đó nó rất tốn kém. Thành ra 7.2 ta sẽ học về L-BFGS là thuật toán BFGS khắc phục được vấn đề này. Rất quan trọng trong machine learning.
>
> Còn 7.3 thì ta thảo luận một dạng xấp xỉ Hessian khác nhưng giữ được tính sparse của Hessian nếu nó sparse.

<br>

