# 7.1 Inexact Newton Methods

📊 **Progress:** `15` Notes | `18` Screenshots | `13` AI Reviews

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
> Chỗ này đại khái là với line search Newton và trust region Newton thì mình cần factor Hessian bởi vì mình cần tính pk: = (∇^2fk)inv ∇fk
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
>
> Vậy thì nên hiểu thế này: chương 7 ta sẽ học một cách tìm Hessian, nhằm tính Newton step pkNtrong thuật toán line search Newton hay trust region Newton, tuy nhiên không phải là ta sẽ dùng phân rã sparse để giải tìm pkN mà sẽ dùng các tiếp cận iterative, để rồi ngoài cái vòng lặp lớn (outer iteration), tại mỗi step, khi tìm pkN, ta cũng sẽ chạy một cái vòng lặp. Và đây chính là in-exac Newton method

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **98/100**
>
> Bạn đã thể hiện sự hiểu biết xuất sắc về tài liệu tham khảo, tóm tắt chính xác các điểm chính và làm phong phú thêm bài ghi chú của mình bằng kiến thức bên ngoài có liên quan.

<br>

<a id="node-em8ep7s"></a>
- **L-BFGS và Hessian thưa**
<p align="center"><kbd><img src="assets/img_em8ep7s.png" width="80%"></kbd></p>

> [!NOTE]
> Đoạn này đại khái nói rằng các matrix xấp xỉ Hessian có được nhờ quasi-Newton method trong chap 6 mình học thường là dense, kể cả khi Hessian thật sparse, do đó nó rất tốn kém. Thành ra 7.2 ta sẽ học về L-BFGS là thuật toán BFGS khắc phục được vấn đề này. Rất quan trọng trong machine learning.
>
> → Mình nên hiểu, đây là bước nâng cấp phương pháp quasi-Newton cho bài toán quy mô lớn. Cũng nên hiểu, quasi-Newton hoàn toàn khác inexact-Newton: quasi-Newton, ta dùng dùng một cách thức để có matrix Bk XẤP XỈ của Hessian thông qua việc cập nhật matrix Bk trong suốt outer iteration của thuật toán. 
>
> Và thật ra là ta sẽ cập nhật cái inverse của Bk, và dùng nó để tính pk.
>
> Còn inexact Newton là ta dùng cách chạy một iteration để giải phương trình [Hessian thật ] pk = - gradient thật theo lối iteratively (điều này cũng giống như ta dùng pk = -[Hessian thật] gradient thật, nhưng tìm pk này theo lối iteratively.
>
> Còn 7.3 thì ta thảo luận một dạng xấp xỉ Hessian khác nhưng giữ được tính sparse của Hessian nếu nó sparse.

> [!TIP]
> **🤖 AI Feedback** — ⚠️ Score: **85/100**
>
> Bạn đã nắm bắt rất tốt các điểm chính về xấp xỉ Hessian dày đặc, các biến thể bộ nhớ hạn chế và duy trì tính thưa thớt từ văn bản. Để tăng cường độ sâu theo văn bản gốc, bạn nên tập trung phân tích và chỉ rút ra thông tin có trong đoạn văn bản đã cho.

<br>

<a id="node-n0cbr8d"></a>
- **Phương pháp Newton không chính xác**
<p align="center"><kbd><img src="assets/img_n0cbr8d.png" width="80%"></kbd></p>

> [!NOTE]
> Phần này đại khái là ta sẽ học những cách để tính gần đúng Newton step (như đã biết, là nghiệm của hệ tuyến tính ∇^2 fk pkN = - ∇fk) với các phương pháp như dùng Conjugate Gradient hoặc Lanczos method và có chỉnh sửa chút.
>
> Như lúc đầu đã nói sơ, tuy rằng ta có thể giải hệ này bằng phép phân rã matrix nhưng vấn đề là có khi matrix phân rã không sparse, ngay cả khi Hessian thực tế vẫn sparse. (gọi là Fill-in)
>
> Thêm nữa, tác giả nói ta cũng có thể tùy chỉnh thuật toán thêm để đảm bảo tốc độ hội tụ nhanh của Newton's method không bị mất đi khi ta dùng inexact Newton. Bên cạnh đó, ta cũng sẽ nói về cái vụ Hessian - free, tức là hoàn toàn không cần tính toán hay lưu trữ Hessian chút nào.
>
> Phần tiếp theo đại khái là gs Nocedal sẽ đưa ra tính toán để chứng minh rằng dù là inexact Newton nhưng thuật toán sẽ đảm bảo vẫn hội tụ.

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **97/100**
>
> Bản tóm tắt rất chính xác và bao quát đầy đủ các ý chính, đặc biệt là việc giải thích rõ ràng về "fill-in" và phương pháp "Hessian-free". Để hoàn thiện hơn, có thể điều chỉnh cách diễn đạt ở phần cuối về việc Nocedal "chứng minh" thành "phân tích" tính hội tụ để sát với ngữ cảnh gốc.

<br>

<a id="node-ts4mvv1"></a>
- **Local Convergence of Inexact Newtons**
<p align="center"><kbd><img src="assets/img_ts4mvv1.png" width="80%"></kbd></p>

> [!NOTE]
> Theo tư vấn thì nên skip, quay lại sau phần này, vì nó chỉ là phân tích tính hội tụ, nhưng mình có thể hiểu sơ sơ ý chính là vầy:
>
> Đầu tiên nên nhớ khác nhau giữa quasi-Newton và inexact Newton: 
>
> Inexact Newton, là nói về việc ta muốn tìm Newton-step, trong bối cảnh thuật toán line search Newton hoặc trust region Newton (tức muốn pk là Newton step), nhưng thay vì giải hệ ∇^2 fk pkN = - ∇fk theo những cách thông thường: ví dụ phân rã sparse Hessian, mà trong bối cảnh bài toán quy mô lớn sẽ tốn kém, thì ta sẽ dùng cách thức iteratively để giải hệ này để tìm pkN. Đây gọi là inexact Newton.
>
> Còn quasi-Newton hoàn toàn khác: cũng là ta muốn tính pk = -(∇^2 fk)inv ∇fk, thì ta tránh chi phí cao của việc này bằng cách: giả lập Hessian, thay nó bởi Bk, và xây dựng một phương pháp mà trong đó suốt quá trình của thuật toán ta sẽ liên tục cập nhật lại Bk (hay Bkinv dùng các thông tin mới), thì đây là quasi-Newton.
>
> Vậy thì quay lại đây, với inexact Newton, ta sẽ có một vòng lặp khác giúp giải ∇^2fk pkN = -∇fk TRONG MỖI vòng lặp của thuật toán. DO ĐÓ, DĨ NHIÊN PHẢI CÓ CÁCH ĐỂ BIẾT KHI NÀO THÌ DỪNG vòng lặp con này để có pkN mà xài, vậy thì ở đây chính là nói tới điều này: Ta sẽ dùng residual rk = ∇^2fk pk + ∇fk. Là sao, vì sao?
>
> → Thì bởi vì mục đích là giải hệ ∇^2fk pkN = -∇fk chính là tìm pkN sao cho ∇^2fk pkN = .. -∇fk, mà pkN trong quá trình giải theo lối iteratively sẽ là chuỗi pkN_i sao cho ∇^2fk pkN_i ngày càng gần với -∇fk, đồng nghĩa cái khoảng cách giữa ∇^2fk pkN_i với -∇fk sẽ ngày càng tiến đến 0, đó cũng chính là nói chuỗi residual rk_i = ∇^2fk pkN_i + ∇fk → 0.
>
> Và ta sẽ dừng khi rk_i đủ nhỏ (để pkN_i khi đó là xấp xỉ bằng Newton step thật: -(∇^2 fk)inv ∇fk. 
>
> Thế thì ta sẽ giải cái hệ này ∇^2fk pkN = -∇fk bằng cách nào: Đó chính là dùng Conjugate Gradient đã học ở chapter 5:
>
> Theo đó còn nhớ đại khái story hay idea của CG là vầy: Đối mặt với hệ phương trình tuyến tính Ax = b, CG có thể giúp ta đi từ initial x0 ở đâu đó, và chọn p0 là steepest direction tại x0, để đi đến nghiệm x* của Ax = b trong NHIỀU NHẤT là n bước, và nếu A có các tính chất nào đó thì thậm chỉ số bước còn ít hơn. Do đó, ở đây, chính là ta sẽ áp dụng CG để giải hệ ∇^2fk pkN = -∇fk (với một số chỉnh sửa nhất định vì trong CG gốc, matrix A được yêu cầu phải là xác định dương nhưng Hessian thực tế thì ko phải lúc nào cũng xác định dương)
>
> Vậy thì ở đây, ta hiểu là mình sẽ chạy thuật toán CG để giải ∇^2fk pkN = -∇fk tìm pkN nhưng kiểu như là ta sẽ không chạy cho đến khi "xong", mà thay vào đó, chỉ chạy cho đến khi "tạm được", tức là không cần rk_i = 0, mà chỉ cần rk_i thỏa điều kiện nào đó. Và do đó, ở đây gs nói về điều kiện mà ta sẽ dừng thuật toán CG:
>
> ||rk|| ≤ ηk ||∇fk||
>
> Và cái điệu kiện dừng này có thể hiểu thế nào?
>
> → Có thể hiểu là: 
>
> Ví dụ tại outer iteration k = 5, khi chạy inner iteration để tìm p5, thì ta sẽ có điều kiện dừng cho chuỗi tìm kiếm p5_i là ||r5_i|| ≤ η5 ||∇f(x5)||. 
>
> Và phần này người ta muốn chứng minh rằng: chỉ cần độ lớn của chuỗi ηk tránh ra số 1 thì thuật toán inexact-Newton chắc chắn sẽ hội tụ

<br>

<a id="node-zb201bp"></a>
- **Line-Search Newton-CG Method**
<p align="center"><kbd><img src="assets/img_zb201bp.png" width="80%"></kbd></p>

> [!NOTE]
> Nói sơ nhanh về ý tưởng của method này: Ta muốn dùng Newton step (Newton direction) trong các thuật toán lớn nào đó, ví dụ Line Search, Trusted Region. Muốn vậy, ta phải giải hệ này: ∇^2fk pk = - ∇fk. Mà với bài toán quy mô lớn thì việc giải hệ này tìm pk (trong trường hợp này, gọi là pkN, "pk_Newton" sẽ rất tốn kém vì các lí do sau: Tất nhiên nói giải cái này theo công thức pk = -(∇^2fk)inv ∇fk thì cũng không có nghĩa là ta đi tìm Hessian inverse, rồi đem nhân với gradient, mà ta sẽ factor-solve: factor Hessian thành các tích các matrix có cấu trúc đơn giản, và giải lần lượt các hệ đơn giản này. Vấn đề là, sparse factor ko phải lúc nào cũng được: đôi khi Hessian thật thì sparse nhưng factor xong thì dense (= không có simple structure). Do đó, ta sẽ dùng một cách thức để giải hệ ∇^2fk pk = - ∇fk này một cách iteratively, và chapter 5 ta đã học một phương pháp cho việc giải hệ Ax = b theo lối iteratively như vậy: Đó chính là CG: Conjugate Gradient method, là thuật toán mà đã chứng minh rằng nếu matrix hệ số (A, ở đây là Hessian có quy mô n × n thì chỉ tốn nhiều nhất là n step để tìm ra được x* (hay pkN*), thậm chí còn nhanh hơn nếu như cấu trúc của A (ví dụ phân phối của trị riêng của nó) có tính chất đặc biệt nào đó (ví dụ như co cụm lại thành một số ít nhỏ hơn n nhiều lần các cụm). Như vậy, ở đây ta sẽ nói về Line-Search Newton - CG, tức là: dùng thuật toán line search, mà cơ bản là như đã biết, ta sẽ iteratively thực hiện các bước: 
>
> - tìm pk, và ở đây ta sẽ dùng Newton step. Và ta sẽ chạy thuật toán CG để tìm pk.
>
> - line search tìm step size: αk, lúc này có thể dùng exact line search (nhưng chắc chả mấy khi dùng), hoặc dùng backtracking line search để tìm αk thỏa Wolfe / strong Wolfe conditions.
>
> -----
>
> Thế thì vấn đề là trong chap 5 ta đã biết, CG method work với một assumption tiên quyết: matrix A xác định dương: tức là độ cong của hàm f luôn là cong lên ở mọi hướng. Nhưng áp dụng vào đây, dễ thấy Hessian đâu phải lúc nào cũng xác định dương, do đó, CẦN MỘT SỐ CHỈNH SỬA đối với CG: Và cụ thể sự chỉnh sửa chỉ đơn giản thôi: Ngay khi ngay khi CG (trong outer iteration k) tìm ra pk_i chỉ theo hướng mà độ cong âm (tức là hàm sẽ cong xuống theo hướng đó), ta sẽ dừng CG. Điều này tác giả nói sẽ giúp pk luôn là descent direction cũng như giữ được các tính chất hội tụ nhanh của Newton method.

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **98/100**
>
> Phân tích của bạn rất sâu sắc và chính xác, giải thích rõ ràng ý tưởng, lý do cần thiết cho phương pháp này và các điều chỉnh quan trọng của nó. Để hoàn thiện hơn, bạn có thể bổ sung tên gọi khác của phương pháp là "phương pháp Newton bị cắt cụt" (truncated Newton method) như được nhắc đến trong văn bản.

<br>

<a id="node-x4092kb"></a>
- **Vòng lặp trong CG Newton**
<p align="center"><kbd><img src="assets/img_x4092kb.png" width="80%"></kbd></p>

> [!NOTE]
> Vài ghi chú về kí hiệu trước khi tác giả mô tả thuật toán Line Search Newton CG: 
>
> Lí do là vì để ta khỏi lẫn lộn giữa kí hiệu đã học của hai thuật toán line searcg, và CG: Phải hiểu rằng, ta sẽ có hai vòng lặp lồng vào nhau: vòng lặp lớn outer iteration sẽ đi từ x0 → x1 → ...→ xk → xk+1...và cho đến khi về được minimizer của f(x) (với điều kiện dừng là gradient vanish ||∇fk|| = 0 hay < ε nào đó), và trong mỗi iteration. ví dụ thứ k nó sẽ:
>
> Chạy inner iteration để tìm pk bằng cách dùng CG để giải hệ Bk p = -∇fk (Dùng Bk chỉ Hessian ∇^2fk). Mà trong mỗi inner iteration, thuật toán CG sẽ tính ra các direction dj, để sinh ra cái chuỗi zj (là chuỗi p_j này sẽ converge về nghiệm thật sự của Bk p = -∇fk, tức p* = -(Bk)inv ∇fk)
>
> Có lẽ phải nhớ lại thuật toán CG chút xíu: Mục tiêu là giải Ax = b theo cách iteratively: Idea sẽ là ta đang giải bài toán tối ưu minimize hàm F(x) là là nguyên hàm của Ax - b, để cho first order necessary condition của nó chính là ∇F(x) = 0 ⇔ Ax - b = 0. Vậy thì xuất phát từ x0, chọn p0 là steepest descent direction tại x0, ta sẽ có cách generate p1 sao cho nó conjugate wrt matrix A với p0, rồi cũng tính step-size α1, và đi đến x1, tiếp tụ, từ x1, tìm p2 là conjugate wrt matrix A với p1, và cũng là với p0, ròi α2, đến x2,....Để rồi cuối cùng ta sẽ hội tụ dần về x*, chính là solution của Ax = b.
>
> Vậy thì ở đây, ví dụ trong outer iteration k = 4, ta muốn tìm p4 là nghiệm của B4 p = -∇f4. Thì ban đầu ta cũng sẽ chọn p0 (initial point, vai trò như x0) nào đó, chọn d0 là steepest direction, rồi tìm d1 conjugate wrt B4 với d0, tính step size, và đến được p1. Lặp lại, tìm d2 conjugate wrt B4 với d1, d0, tính step size, đến được p2, cứ thế. Và ta sẽ tại ra chuỗi {pi}, nhưng theo sách ta sẽ dùng chữ z: {zi} converge về solution thật sự của B4 p = ∇f4. 
>
> Tất nhiên, như đã nói trước, ta sẽ không chạy hết n iteration đế có chuỗi z0, z1,....zn converge về solution của B4 p = ∇f4, mà sẽ có điều kiện dừng: ||ri|| = B4 zi + ∇f4 ≤ η4 ||∇f4||. với η4 được thiết kế sao cho đảm bảo hội tụ như phần trước đã nói. Cụ thể ta sẽ chọn η4 = min{0.5 √||∇f4||}
>
> Tại đây ta đã có p4, ta tiếp tục qua phần 2 của một outer iteration: tính step size α4, để rồi nhảy từ x4 → x5 = x4 + α4p4. Và tíếp tục outer iteration tiếp theo.

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **98/100**
>
> Ghi chú rất chính xác và có chiều sâu, giải thích rõ ràng cấu trúc lồng nhau của thuật toán và cung cấp nền tảng vững chắc về phương pháp Gradient Liên Hợp. Cần lưu ý một lỗi nhỏ trong công thức $\eta_k$ (thiếu dấu phẩy giữa 0.5 và căn bậc hai của gradient norm).

<br>

<a id="node-rwy213p"></a>
- **Thuật toán Newton-CG**
<p align="center"><kbd><img src="assets/img_rwy213p.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_78gg4r.png" width="80%"></kbd></p>

> [!NOTE]
> nói sơ thuật toán này:
>
> Vòng lặp lớn, gọi là outer iteration ta sẽ làm các việc sau:
>
> 1) Định nghĩa εk, dùng để dừng vòng lặp tìm kiếm pk bởi CG
>
> 2) Khởi tạo z0 = 0. r0 = gradient ∇fk, d0 = -r0 = -∇fk
>
> Đây là điểm khác so với CG trong chap 5, trong đó ta sẽ bắt đầu tại initial point nào đó, chứ không phải 0, xem lại liên kết, trong đó nói ta có initial point x0 (chú ý, x0 chính là tương đương z0 ở đây, giải tìm x thỏa Ax = b chính là giải tìm p thỏa ∇^2fk p = - ∇fk.
>
> Còn r0 chọn bằng ∇fk là sao? → đó là initial residual = residual tại z0 = ∇^2fk × 0 -(-∇fk) = ∇fk (nhớ ko? residual là rk = Axk - b, ở đây thì là ∇^2fk zj + ∇fk)
>
> Còn d0 chọn bằng -∇fk là sao? → chính là theo CG, thì initial direction chọn bằng steepest descent direction tại initial point.
>
> 3) Chạy vòng lặp thuật toán CG: 
>
> Đầu tiên nó có chốt chặn: Kiểm tra djTBkdj (như đã ghi chú, trong phần này, gs kí hiệu nó cho Hessian tại k, ∇^2fk) xem âm hoặc bằng 0 không, nếu có thì dừng thuật toán CG, pk = zj (nếu ngay ở step đầu tiên mà djTBkdj đã ≤ 0 thì dùng ngay cái steepest descent direction -∇fk. 
>
> Chỗ này là sao? → Đây chính là đoạn chỉnh sửa so với CG, vì trong CG chuẩn, ta có giả định matrix hệ số A xác định dương, pkBkpk (tương ứng với djTBkdj ở đây) sẽ luôn dương. Nhưng ở đây, Hessian Bk không chắc luôn xác định dương, nên djTBkdj có thể âm hoặc bằng 0. Khi đó, CG sẽ bị lỗi ở bước tính αj = rjTrj / djTBjdj: Lỗi explode nếu djTBkdj = 0 hoặc αj sẽ âm nếu djTBkdj âm → dẫn tới thuật toán sẽ dẫn ta đi ngược lại hướng dj → tăng residual thay vì giảm. Do đó, LSNCG sẽ stop ngay khi thấy djTBkdj đã ≤ 0.
>
> Các bước tiếp theo trong vòng lặp là các bước của thuật toán CG điển hình, nhưng có thêm một chỉnh sửa nữa, thay vì chạy "cho đến hết" thì ta sẽ dừng / thoát, khi residual đủ nhỏ (so với εk)
>
> 4) Sau khi có pk, thực hiện cập nhật vị trí xk+1 = xk + αkpk (step size αk thỏa Wolfe, Goldstein hay Armijo condition)

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **92/100**
>
> Bài phân tích rất sâu sắc và chính xác, đặc biệt là các giải thích về lý do thay đổi so với thuật toán CG chuẩn. Tuy nhiên, công thức định nghĩa εk có một lỗi nhỏ, thiếu căn bậc hai của ||∇fk||.

<br>

<a id="node-8vcwotc"></a>
- **Newton-CG Hessian gần suy biến**
<p align="center"><kbd><img src="assets/img_8vcwotc.png" width="80%"></kbd></p>

> [!NOTE]
> Tiếp, thầy Nocedal cho biết thuật toán này tốt cho large problem nhưng nó có một điểm yếu: là khi Hessian gần singular, thì line search Newton - CG direction có thể dài và poor quality, dẫn đến cần nhiều bước function evaluation trong line search mà chỉ cho một mức giảm nhỏ của function. Ý này là sao?
>
> Giả sử Bk gần singular, tức là vẫn non-singular ⇨ invertible thì bản chất pk mà CG giúp giải chính là pk = - (Bk)inv gk (Bk, gk là Hessian, gradient).
>
> Bk là Hessian, là matrix đối xứng, nên Bkinv cũng vậy, luôn tồn tại phép phân tách trị riêng vector riêng: (Bk)inv = Q Λ QT, Q là orthogonal matrix bởi eigenvector của cả Bk và Bkinv (hai thằng này có chung eigenvector) và Λ là diagonal matrix trị riêng của Bkinv, cũng là nghịch đảo của trị riêng của Bk. Mà Bk gần singular → tồn trị riêng nhỏ gần bằng 0 → trị riêng tương ứng của (Bk)inv sẽ rất lớn.
>
> Thế thì ta thấy - (Bk)inv gk = - Q Λ QT gk có bản chất là gì ôn lại cho nhớ:
>
> QT gk sẽ chuyển đổi tọa độ của gk trong basis e's sang tọa độ basis q's (eigenvector của Bk) 
>
> (Ôn lại kiến thức linear transformation học với thầy Strang:
>
> Muốn xây dựng matrix A đại diện cho phép biến đổi tuyến tính T(v) thì làm một cách tổng qúat như sau:
>
> Chuẩn bị input basis v's và output basis w's.
>
> Biến đổi tuyến tính các input basis: T(v1), T(v2),...
>
> Thể hiện nó theo output basis: 
>
> T(v1) = α11 u1 + α21u2 + ... = [α11, α21,..]T W (vector cột × matrix U = [u1, u2,...]
>
> T(v2) = α12 u1 + α22u2 + ...= [α12, α22,..]T W (vector cột × matrix U = [u1, u2,...]
>
> Đặt [α11, α21,..]T, [α12, α22,..]T...thành các cột của  A
>
> → [T(v1), T(v2),...] = A W, thì A chính là matrix đại diện cho linear transformation T(v) từ input space basis v's → output space basis w's
>
> Áp dụng với identity transformation:
>
> T(v1) = v1 = [A col 1]W
>
> T(v2) = v2 = [A col 2]W
>
> ...
>
> → V = A W 
>
> ⇨ A = VWinv chính là change of basis matrix chuyển từ tọa độ basis v's sang tọa độ basis w's
>
> Nếu v's là standard basis thì V = I. → Winv chính là matrix chuyển tạo độ basis chuẩn sang basis w's.
>
> Quay lại đây, QT gk cũng chính là Qinv gk chính là chuyển tọa độ của gradient gk từ basis e's sang basis q's. Về mặt hình học, chính là xoay trục tọa độ trở nên sao cho các trục thẳng góc với các vector q's (cũng vuông góc nhau)
>
> Sau đó Λ QT gk chính là kéo giãn không gian theo các hướng q's bởi factor λ's. (cũng là scale các tọa độ của QT gk lên bởi λ's Và cuối cùng Q Λ QT gk sẽ chuyển lại tọa độ theo basis e's.
>
> Thế thì từ đó ta thấy, vì một λ nào đó rất lớn, nên sẽ tạo stretch factor rất lớn, khiến kéo dài vector rất lớn theo phương đó. Kết quả là ta sẽ có pk rất dài.
>
> Và rất dài thì sẽ gây vấn đề, lí do là vì, hướng pk, là Newton step, cơ bản chỉ hướng đi xuống (giảm hàm f) bằng cách coi / ước lượng hàm f bởi hàm bậc hai, và đương nhiên sự ước lượng này chỉ đúng trong phạm vi nhất định quanh xk, chứ xét ở phạm vi xa thì nó ko còn đúng nữa, nói cách khác, pk sẽ giúp đi xuống, nhưng nếu đi qua xa theo hướng đó, hàm chưa chắc đi xuống. 
>
> Thế thì ta nhớ, khi có pk (bởi CG) thì ta còn phải có αk, dùng backtracking để tìm αk thỏa Wolfe / Goldstein / Armijo condition. Mà ta nhớ, với Newton method, cách làm cơ bản là ta sẽ cho intial value = 1, và giảm dần xuống cho đến khi thỏa. Thế thì nếu pk quá dài, cơ bản là sẽ cần giảm rất nhiều lần, mà mỗi lần thì phải tính giá trị f, mà bước này với bài toán quy mô lớn thì cũng rất tốn kém.  
>
> ====
>
> Một cách để giải quyết đó là ta normalize Newton step pk nhưng điều này sẽ mà mất đi cái điểm mạnh của Newton step: Ý này rất dễ hiểu, nếu ta cứ normalize cho ||pk|| = 1, thì sẽ khắc phục được vụ pk rất dài, nhưng sẽ bị vụ khác: ví dụ như khi pk ban đầu ||pk|| = 0.25, thì thay vì dùng intial value của αk = 1 là xong thì ta lại phải tăng pk lên norm 1 và đi lùi xuống → lãng phí.
>
> Một cách nữa, là dùng cái threshold khi check djTBkdj (tức là thay vì dùng threshold = 0, thì dùng giá trị nào đó để check) tuy nhiên việc tìm ra threshold tốt cũng khó.
>
> Do đó gs nói rằng ông khuyến nghị rằng nên dùng thuật toán sau đây: Trust-region Newton CG

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **98/100**
>
> Bài ghi chép của bạn rất xuất sắc và sâu sắc, không chỉ tóm tắt chính xác mà còn giải thích chi tiết cơ chế toán học về vấn đề Hessian gần singular, thể hiện sự hiểu biết vững chắc. Để tối ưu hơn, bạn có thể cân nhắc cô đọng phần ôn tập kiến thức biến đổi tuyến tính để giữ trọng tâm vào vấn đề chính của thuật toán.

<br>

<a id="node-5hnsref"></a>
- **Phương pháp Newton không Hessian**
<p align="center"><kbd><img src="assets/img_5hnsref.png" width="80%"></kbd></p>

> [!NOTE]
> Đoạn này hiểu đại ý là, trong thuật toán Line Search Newton CG, ta không trực tiếp tính Hessian Bk, nhìn lại sẽ thấy, trong các bước có dính đến Bk, thật ra cái ta cần là Bkdj, tức là kết quả nhân matrix Bk với direction vecto dj. Do đó, thật ra không cần phải tính ra Hessian, rồi đem nhân nó với dj, mà có cách cho ra luôn kết quả này.
>
> Và trong chap 8 sẽ nói nhiều hơn về cái này, nhưng đại ý là, ta sẽ dùng công thức finite differencing:
>
> ∇^2fk d ≈ [∇f(xk + hd) - ∇f(xk)] / h.
>
> Công thức này là sao?
>
> Đơn giản thôi, xét hàm g(α) = ∇(xk + αd).
>
> g'(α) = d/dα ∇(xk + αd) = d/d(xk + αd) ∇(xk + αd) . d/dα (xk + αd)
>
> = ∇^2f(xk + αd) d
>
> ⇨ ∇^2f(xk) d = g'(α)|α=0 tức là đạo hàm của hàm  g(α) = ∇(xk + αd) tại α = 0.
>
> Như vậy, dựa theo định nghĩa đạo hàm hàm f(x):
>
> f'(x) = lim δx→0 [f(x + δx) - f(x)] / δx
>
> Nếu δx nhỏ, ta có thể bỏ lim, thay bằng dấu ≈ để có cái gọi là linear approx:
>
> f'(x) ≈ [f(x + δx) - f(x)] / δx 
>
> Như vậy áp dụng cái này:
>
> g'(α) ≈ [g(α + δ) - g(α)] / δ
>
> → g'(α)|α=0 ≈ [g(δ) - g(0)] / δ 
>
> = [∇(xk + δd) - ∇(xk)] / δ
>
> (Thay δ bằng h thì ta có công thức trong sách)
>
> -----
>
> Thế thì nhờ cách này, ta sẽ ko cần phải LƯU TRỮ HESSIAN Bk, (để rồi cũng ko cần phải tính Bkd) mà chỉ cần tính hiệu của hai gradient tại xk và xk + hd, rồi chia h), khiến cho trong thuật toán CG sẽ tăng thêm một bước tính toán, nhưng không cần phải lưu trữ Hessian: Đây chính là "Hessian - free"

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **95/100**
>
> Phần giải thích và đặc biệt là cách bạn suy luận công thức xấp xỉ phân biệt hữu hạn (finite differencing) rất sâu sắc và chính xác. Để hoàn thiện hơn, bạn có thể bổ sung thông tin về bậc chính xác của phép xấp xỉ này.

<br>

<a id="node-8tkd9oh"></a>
- **Phương pháp Trust-Region Newton CG**
<p align="center"><kbd><img src="assets/img_8tkd9oh.png" width="80%"></kbd></p>

> [!NOTE]
> Ok, qua Trust-Region Newton CG. Đầu tiên gs nhắc lại rằng hồi chapter 4 mình đã biết về một số cách tiếp cận giúp tìm approx solution của bài toán trust region subproblem 4.3 mà thực hiện những sự cải thiện đối với Cauchy point. Thử ôn lại tí:
>
> Đầu tiên ý tưởng chính của trust region method tóm gọn như sau: Tại mỗi iteration, xem hàm f như hàm bậc hai, để giải bài toán minimize hàm bậc hai mk(p) có ràng buộc ||pk|| ≤ Δk, với ràng buộc Δk xác định ở iteration trước. Giải ra pk, check thử xem độ uy tín của mô hình mk, bằng tỉ lệ giữa độ giảm bởi mk và độ giảm thực tế (nếu dùng pk để cập nhận vị trí), để nếu độ tỉ lệ này cao (hướng về 1) chứng tỏ mk mô phỏng đúng f, và ||pk|| = Δk, ta sẽ tăng trust region. Ngược lại nếu độ uy tín thấp, chứng tỏ mk mô phỏng sai hàm f, ta sẽ không dùng pk, giảm trust region. Còn uy tín vừa vừa thì vẫn update nhưng giữ nguyên trust region. Ý tưởng chính là vậy.
>
> Còn cụ thể hơn mk(p) là xấp xỉ bậc hai của f tại xk: mk(p) = fk + ∇fkTp + (1/2) pT Bk p. Nếu Bk được chọn là Hessian ∇^2fk, thì ta có trust region Newton, nếu Bk là I thì ta sẽ có trust region steepest descent, còn nếu Bk là ma trận xấp xỉ Hessian thì ta có trust region quasi Newton.
>
> Và bài toán minimize mk s.t ||pk|| ≤ Δk gọi là sub-problem.
>
> Thế thì Cauchy point là gì?
>
> Còn nhớ Cauchy-point là như sau: Xác định hướng dốc nhất tại xk (-∇fk) và đi theo hướng đó cho tới khi đụng hàng rào: Nên pkC là solution của bài toán:
>
> minimize m(-α ∇fk) s.t ||α ∇fk|| ≤ Δk
>
> Để rồi sau đó, ta có thể có những cách tiếp cận cải thiện Cauchy point như: Thuật toán dog-leg,  2D subspace minimization. Và trong chap 4 đã nhắc đến cách thứ 3, chính là dùng CG mà ở đây đang nói tới. (Xem link để quay lại phần "Nói sơ về nội dung sắp tới" có nhắc đến chỗ này)

> [!TIP]
> **🤖 AI Feedback** — ⚠️ Score: **85/100**
>
> Bài viết đã nắm bắt chính xác ý chính của đoạn văn, đặc biệt là phần giới thiệu về việc tìm kiếm giải pháp xấp xỉ và cải thiện điểm Cauchy. Tuy nhiên, nó bỏ qua một số chi tiết cụ thể như tên tác giả (Steihaug) và số hiệu thuật toán (7.2 và 4.1) được đề cập trong văn bản gốc.

<br>

<a id="node-4fbrszp"></a>
- **Trust Region Newton CG**
<p align="center"><kbd><img src="assets/img_4fbrszp.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_xpv8q9.png" width="80%"></kbd></p>

> [!NOTE]
> Vậy thì đại ý là ở đây, ta sẽ bàn về cách tiếp cận, chỉnh sử CG để giải bài toán subproblem, nói cách khác, thuật toán Trust-Region Newton CG tức là ta ÁP DỤNG CG (có chỉnh sửa) ĐỂ GIẢI BÀI TOÁN SUBPROBLEM BÊN TRONG TRUST REGION NEWTON METHOD. (thay vì dùng Cauchy-point, hay các phương pháp cải thiện Cauchy-point như dogleg, 2D subspace) 
>
> Và dĩ nhiên cũng dễ hiểu thuật toán 7.2 (CG Steihaug) chỉ là CG chỉnh sửa để giải subproblem thôi, đặt nó trong vòng lặp lớn của thuật toán 4.1 (Trust Region), cụ thể là cái bước giải subproblem tìm pk thì ta mới có đầy đủ Trust Region Newton CG. 
>
> Có thể vẫn cần nói lại điều này cho khắc sâu hơn: Nên nhớ tác dụng của CG chủ yếu là giúp giải hệ Ax = b. Và khi đối diện với thuật toán nào mà pk của nó là dùng Newton step, thì chính là khi ta muốn giải hệ ∇^2 fk p = -∇fk để tìm pk. Và do đó, CG có thể giúp giải cái hệ này theo lối iteratively. Tuy nhiên vì CG gốc giải định A xác định dương, nên khi áp dụng vào bài toán này, Hessian có thể không xác định dương, thì ta phải chỉnh sửa CG. 
>
> Nếu so với Line Search Newton CG vừa học, thì tại mỗi outer iteration, ta có thêm inner iteration của CG để tìm Newton step.
>
> Thì trong bối cảnh của Trust region, tại mỗi outer iteration, ta cũng có thêm inner iteration dùng CG để giải bài toán sub problem. Có điều bài toán subproblem lại là giải hệ có constraint ||p|| ≤ Δk, nên ta sẽ chỉnh sửa CG thêm để adjust vụ này. Tóm lại, sẽ khác với CG gốc ở 2 điểm: deal với Hessian có thể không xác định dương (giống như CG trong Line Search Newton CG) và deal với vấn đề constraint.
>
> Cho nên, đọc thuật toán 7.2, thì khúc đầu là set up thông thường của CG mà ta đã biết: Cho initial z0 = 0 (trong CG gốc tương ứng với x0), chọn d0 (trong CG gốc là p0) là steepest descent -∇fk, tính initial residual r0 = -(-∇fk) (trong CG gốc là r0 = Ax0 - b).
>
> Trong vòng lặp for j = 1,2....:
>
> Ta sẽ quay lại nói về cái check djTBkdj ≤ 0 sau (1)
>
> Set αj = rjTrj / djTBkdj: Đây là bước tính stepsize của CG. (tương đương bước tính αk = αk = rkTrk / pkTApk 5.24a trong CG gốc Algorithm 5.2)
>
> zj+1 = zj + αjdj: Đây là bước cập nhật (tương đương xk+1 = xk + αkpk 5.24b trong 5.2)
>
> Tại đây có thêm một chỉnh sửa của CG gốc: vì có ràng buộc cho pk, nên ở đây họ sẽ check ||zj+1|| có lớn hơn Δk chưa. Quay lại sau. (2)
>
> rj+1 = rj + αjBkdj (Đây là bước cập nhật residual 5.24c trong Algorithm 5.2)
>
> Tại đây, check điều kiện dừng dựa trên residual norm, cũng là điểm khác so với CG gốc. Quay lại sau (3)
>
> βj+1 = rj+1Trj+1 / rjTrj (tương ứng 5.24d trong Algorithm 5.2)
>
> dj+1 = -rj+1 + βj+1dj (tương ứng 5.24e trong Algorithm 5.2)
>
> Quay lại bàn về (1),(2),(3):
>
> Với (1), ta dừng thuật toán CG khi djTBkdj ≤ 0, đây là deal với vụ Hessian không xác định dương tương tự như Line Search Newton CG. Vậy cái vụ tìm τ sao cho pk = zj + τdj minimize mk(pk) và thỏa ||pk|| = Δk là sao?
>
> Thì mình hiểu là vì cái ta tìm là pk, ứng với x* trong thuật toán CG giải Ax = b, và {zj} ứng với chuỗi {xi}, nên tại thời điểm dừng, ta có dj (ứng với pk trong CG gốc). 
>
> Nhưng trong CG gốc, để có xk+1 ta còn phải tính step size αk nữa (ví dụ cái bước set 5.24a αk = rkTrk / pkTApk) Mà trong CG gốc, vì A xác định dương, nên với hướng pk đã có, việc tìm step size chỉ là / hay công thức 5.24a có bản chất xuất phát từ việc giải bài toán minimize hàm bậc hai là nguyên hàm của Ax - b, restricted bởi hướng pk, và cái hàm đó chỉ là hàm bậc hai đơn biến. Tí nữa mình sẽ derive lại luôn cho nhớ. Nhưng khi Bk không xác định dương, để djBkdj âm và thuật toán rơi vài cái if check này, thì vì nếu giới hạn theo hướng dj này, thì hàm số có thể cắm đầu đi xuống rất xa, vượt qua giới hạn trust region. Thành ra ta sẽ phải tìm step size τ với bài toán minimize mk(pk) với pk = zj + τdj thỏa constraint ||pk|| = Δk là vậy.
>
> Nói đi thì phải nói lại, việc tính αj thật ra cũng phải chịu ràng buộc là step size ko đưa ra vượt quá trust region, và quả thật nó thể hiện ở việc check norm của zj+1 có lớn hơn Δk hay không, nếu chưa lớn thì thôi, đồng nghĩa là step size αj không đưa ta đi quá giới hạn trust region theo hướng dj. Nhưng nếu quá, thì cũng phải tìm lại step size phù hợp, đó cũng chính là (2)
>
> Còn điểm (3) mang ý nghĩa là ta sẽ ko chạy "xong" thuật toán CG. Mà chỉ cho đến khi residual đủ nhỏ là được.
>
> Nói chung nó rắc rối ở chỗ ta phải đặt bài toán CG trong bối cảnh bài toán Trust Region.
>
> Nên có thể đỡ lú hơn nếu mình cứ hiểu là ta đang dùng thuật toán CG gốc, giải Ax = b nhưng với constraint ||x|| ≤ Δ.
>
> Thì ban đầu, ta chọn x0 = 0, r0 = b, và p0 = -r0.
>
> Chạy vòng lặp, ví dụ thứ k:
>
> Tính αk theo 5.24a, cập nhật xk+1 theo 5.24b
>
> Thì vì có constraint nên phải check norm ||xk+1||, nếu vượt quá Δ thì phải tính lại step size: để minimize F(xk + τ pk) s.t ||xk + τ pk|| = Δ. 
>
> Một điểm nữa có lẽ nên nhớ lại thêm nữa: Như trên đã nói, bản chất của thuật toán CG, giúp giải Ax = b theo lối iteratively, thực chất cũng chỉ là coi nó như việc giải bài toán tối ưu (minimize) hàm F(x) = (1/2) xTAx - bTx với đặc điểm ∇F(x) = Ax - b, để rồi x* thỏa Ax - b cũng chính là x* thỏa điều kiện cần tối ưu bậc nhất ∇F(x) = 0.

> [!TIP]
> **🤖 AI Feedback** — ⚠️ Score: **88/100**
>
> Bài phân tích của bạn thể hiện sự hiểu biết sâu sắc và toàn diện về thuật toán Steihaug-CG và vai trò của nó trong phương pháp Trust-Region. Bạn đã nắm vững các điểm cốt lõi về việc điều chỉnh CG để đối phó với ma trận Hessian không xác định dương và ràng buộc vùng tin cậy, đồng thời kết nối tốt với các phương pháp tối ưu khác. Tuy nhiên, cần chú ý đến độ chính xác tuyệt đối trong các chi tiết: giải thích ban đầu về r0 là r0 = -(-∇fk là không cần thiết và có thể gây nhầm lẫn; chỉ cần nói r0 = ∇fk như trong thuật toán. Dù kết quả cuối cùng là đúng, cách diễn đạt cần phải trực tiếp và rõ ràng hơn.

<br>

<a id="node-ngzc1r1"></a>
- **Trust Region & Inexact Newton**
<p align="center"><kbd><img src="assets/img_ngzc1r1.png" width="80%"></kbd></p>

> [!NOTE]
> Đoạn này nói về hai cái if giúp dừng thuật toán thì mình đã hiểu rồi, và mình cũng hiểu đúng là khi dừng, ta sẽ tính lại step size để nó ko vi phạm trust region, thì thật ra cái step size tính lại sẽ là điểm giao giữa direction dj và trust region boudary như gs nói ở đây.
>
> Đoạn sau nói về độ lớn của mức toleance εk trog điều kiện dừng khi check residual mà mình đã hiểu là mục đích ko cần phải chạy rốt ráo CG, mà chỉ cần dừng khi kết quả đủ tốt, như vậy cũng ko khó hiểu khi giáo sư nói để giữ chi phí của cả thuật toán lớn ko quá cao (vì dù sao CG cũng chỉ là giải subproblem, không cần tuyệt đối chính xác làm gì, giống như ta cũng ko cần giải chính xác αk trong line search vậy)
>
> Một ý nữa ông nói khi gần x*, thì trust region bound trở nên inactive và method trở thành inexact Newton, là sao? → À thì là vì khi tiến gần đến x*, thì mk sẽ ngày càng xấp xỉ rất tốt fk, dẫn đến kết quả tốt dần lên khi trust region sẽ dần dần mở rộng ra rất lớn. Khi đó ràng buộc trở nên không còn tác dụng nữa. Và bài toán subproblem ko có ràng buộc thì chỉ là bài toán tìm Newton step theo lối iteratively, như đã biết, gọi là inexact Newton

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **90/100**
>
> Bài phân tích cho thấy sự nắm vững các cơ chế dừng và tầm quan trọng của εk trong việc tối ưu chi phí. Giải thích về việc trust-region bound trở nên không còn tác dụng khi gần nghiệm tối ưu x* là thuyết phục và cho thấy sự hiểu biết sâu sắc về động thái của thuật toán.

<br>

<a id="node-lqxn0xz"></a>
- **Điểm Cauchy và hội tụ**
<p align="center"><kbd><img src="assets/img_lqxn0xz.png" width="80%"></kbd></p>

> [!NOTE]
> Đoạn này là sao: Đại ý là đoạn này gs nói ta có thể chỉ ra rằng mức giảm hàm mk của thuật toán này sau mỗi step là không thua mức giảm mang lại bởi Cauchy point. Nên theo một theorem mà ta đã học ở chap 4 nói rằng chỉ cần mức giảm của thuật toán có thể tương ứng với một scaled version mức giảm bởi Cauchy point thì đảm bảo thuật toán sẽ hội tụ toàn cục.
>
> Lúc nãy mình đã ôn lại Cauchy point về mặt trực giác, nó là khi ta đi theo hướng steepest descent tại xk và muốn giảm tối đa mk(p) trong phạm vi ràng buộc. Tức là nó là solution của bài toán minimize g(α) = mk(α(-∇fk)) s.t ||α(-∇fk)|| ≤ Δk.
>
> Với mk(p) = fk + ∇fkTp + (1/2)p ∇^2fk p thì việc restrict bởi hướng ∇fk sẽ cho ta bài toán mininize hàm đơn biến bậc hai có ràng buộc. 
>
> Chỉ việc giải tìm critical point: g'(α) = 0, để xem điểm cực tiểu của hàm g(α) nằm bên trong hay ngoài phạm vi trust region. Nếu nằm trong thì không có gì để nói, còn nếu nằm ngoài thì vì giới hạn, ta sẽ lấy tại boudary.
>
> g'(α) = d/dα mk(α(-∇fk))
>
> = d/d[α(-∇fk)] mk(α(-∇fk)) . d/dα [α(-∇fk)]
>
> = ∇mk(α(-∇fk)) . (-∇fk)
>
> = [ (∇^2fk p + ∇fk)p=α(-∇fk) ] . (-∇fk)
>
> = [∇^2fk α(-∇fk) + ∇fk] . (-∇fk)
>
> = [-α ∇^2fk∇fk + ∇fk]T (-∇fk)
>
> = α ∇fkT ∇^2fk ∇fk - ∇fkT∇fk
>
> Fisrt order optimality necessary condition: g'(α) = 0 
>
> ⇔ α ∇fkT ∇^2fk ∇fk - ∇fkT∇fk = 0
>
> ⇔ α ∇fkT ∇^2fk ∇fk = ∇fkT∇fk
>
> ⇔ α = ∇fkT∇fk / ∇fkT ∇^2fk ∇fk
>
> ⇨ ||α(-∇fk)|| = (∇fkT∇fk / ∇fkT ∇^2fk ∇fk) ||∇fk||
>
> = ||∇fk||^3 / ∇fkT ∇^2fk ∇fk
>
> Tới đây tính g''(α) = d/dα g'(α) = d/dα [α ∇fkT ∇^2fk ∇fk - ∇fkT∇fk] = ∇fkT ∇^2fk ∇fk
>
> Chia hai case: 
>
> 1) ∇fkT ∇^2fk ∇fk < 0, thì cực trị là maximum của hàm g(α), nên để minimize g(α) trong phạm vi giới hạn, thì điểm cần tìm là nằm ngay trên boudary: → solution là (-∇fk / ||∇fk||) Δk
>
> 2) ∇fkT ∇^2fk ∇fk > 0, thì cực trị là minimum của hàm g(α) nên phải xét thêm việc điểm này nằm trong hay ngoài:
>
> a) ||∇fk||^3 / ∇fkT ∇^2fk ∇fk > Δk thì ta sẽ có solution là:
>
> (-∇fk / ||∇fk||) Δk
>
> b) Ngược lại, thì solution là (∇fkT∇fk / ∇fkT ∇^2fk ∇fk) (-∇fk)
>
> Viết gk, Bk cho gọn:
>
> Nếu gkTBkgk ≤ 0: -(Δk/ ||gk||) gk (A)
>
> Nếu gkTBkgk > 0: 
>
> + Nếu ||gk||^3 / gkTBkgk > Δk
>
> ⇔ ||gk||^3 / ΔkgkTBkgk > 1 thì solution là -(Δk/ ||gk||) gk (B)
>
> + Ngược lại, solution là (||gk||^2 / gkTBkgk) (-gk) (C)
>
> mà cái này = (||gk||^2 / gkTBkgk) (||gk||/Δk)(Δk/ ||gk||) (-gk)
>
> = [(||gk||^3 / ΔkgkTBkgk) [-(Δk/ ||gk||) gk] 
>
> Vậy viết lại lần nữa:
>
> gkTBkgk < 0, solution là 1 × [-(Δk/ ||gk||) gk]
>
> gkTBkgk > 0, solution là min[1, (||gk||^3 / ΔkgkTBkgk)] × [-(Δk/ ||gk||) gk] 
>
> Đây chính là 4.12 trong sách (Xem link Cauchy point)
>
> -----
>
> Tuy nhiên quay lại đây ta chỉ cần dùng công thức A, B, C thôi.

<br>

