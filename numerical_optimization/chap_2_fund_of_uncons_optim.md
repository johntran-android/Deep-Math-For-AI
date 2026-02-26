# Chap 2 - Fund Of Uncons Optim

📊 **Progress:** `37` Notes | `56` Screenshots | `31` AI Reviews

---

<a id="node-7y0mp72"></a>
## Tổng quan thuật toán tối ưu

<p align="center"><kbd><img src="assets/img_7y0mp72.png" width="80%"></kbd></p>

> [!NOTE]
> gs nói về cái nhìn tổng quan của thuật toán tối ưu ko ràng buộc. Ta sẽ phải có điểm ban đầu x0, và thuật toán sẽ generate chuỗi điểm x(1),x(2)...cho đến khi dừng là khi ta ko tiến triển thêm nữa (hàm f ko giảm nữa) hoặc khi solution đã xấp xỉ gần đúng được optimal với mức độ chính xác chấp nhận được.
>
> x0 thì có thể được chọn bởi kinh nghiệm trong ngành. 
>
> Hoặc cũng có thể do thuật toán tạo ra một cách tùy tiện hoặc có phương pháp đàng hoàng.
>
> tại mỗi điểm x(k), thuật toán sẽ dùng thông tin tại đó để mà generate điểm kế tiếp, sao cho hàm f giảm. Nhưng cũng có dạng nonmonotone, khi có thể sau mỗi bước không giảm f liên tục nhưng đều phải giảm f sau một số bước nào đó.
>
> nói chung mấy cái này đều biết cả rồi.

> [!TIP]
> **🤖 AI Feedback** — ⚠️ Score: **88/100**
>
> Bài ghi rất chính xác và bao quát được nhiều ý chính quan trọng về thuật toán tối ưu. Để hoàn thiện hơn, bạn có thể bổ sung thêm việc thuật toán dùng thông tin từ các điểm lặp trước đó để tìm điểm tiếp theo và hai chiến lược cơ bản để chuyển từ điểm hiện tại sang điểm mới.

<br>


<a id="node-91pamkz"></a>
### Chiến lược Line Search

<p align="center"><kbd><img src="assets/img_91pamkz.png" width="80%"></kbd></p>

> [!NOTE]
> Thế thì giáo sư cho biết có hai chiến lược chính để di chuyển: Line search và Trust region
>
> Với line search thì đã biết rồi, thuật toán sẽ chọn một hướng p_k, (có thể ý nói là descent direction), và tìm theo hướng này giúp đến một điểmthấp hơn
>
> Và bước đi dài bao nhiêu có thể được giải một cách chính xác bằng cách giải bài toán tối ưu hàm đơn biến: minimize α > 0: f(x_k + α p_k) (đây chính là exact line search trong Convex Optimization)
>
> Thì dĩ nhiên nếu giải bài toán này thì ta có bước đi tối ưu theo hướng p_k, nhưng thường là ko cần thiết vì việc giải bài toán này tăng chi phí.
>
> Thay vào đó thuật toán có thể dùng cách khác, tạo các step length cho đến khi tìm được một cái có thể gần gần với cái minimum của bài toán tối ưu
>
> (có thể gs đang nói về backtracking line search)
>
> Rồi sau đó, lại lặp lại, tìm p_(k+1) và search theo hướng đó để tìm x_(k+2)

> [!TIP]
> **🤖 AI Feedback** — ⚠️ Score: **75/100**
>
> Bài làm của bạn đã nắm bắt được hầu hết các điểm chính và có chiều sâu tốt, đặc biệt là việc liên hệ với các thuật toán cụ thể. Tuy nhiên, cần lưu ý rằng trong chiến lược line search, bước tìm độ dài alpha thường được giải quyết một cách gần đúng để tối ưu hóa hiệu quả, chứ không phải luôn chính xác như đã nêu ban đầu.

<br>


<a id="node-5xc69wg"></a>
#### Chiến lược Trust Region

<p align="center"><kbd><img src="assets/img_5xc69wg.png" width="80%"></kbd></p>

> [!NOTE]
> Chiến lược thứ hai là TRUST REGION. 
>
> Đại khái là ta sẽ dùng thông tin về hàm f mà ta có được tại x_k (f, hay gradient, hay Hessian tại x_k) để xây dựng một mô hình m_k sao cho nó hành xử giống hàm f nếu giới hạn trong phạm vi lân cận x_k 
>
> (Mô hình, chữ này có nghĩa là ta mô hình, mô phỏng một quan hệ thực tế define bởi hàm f, nên nói ta xây dựng mô hình m_k thì ý là **xây dựng hàm m_k sao cho m_k(x) hành xử giống hàm f(x)**)
>
> Và vì **nó chỉ hành xử giống f tại vùng lân cận x_k, nên ta mới giới hạn nó trong một trust region**
>
> Khi đó ta sẽ giải bài toán **minimize p m_k(x_k + p) với ràng buộc x_k + p nằm trong trust region, để tìm p**.
>
> (rất dễ hiểu, bằng cách xây dựng mô phỏng của f khiến nó có thể bắt chước được f nếu xét quanh vùng gần x_k, thì ta có thể dùng nó để tìm p giúp đi từ x_k đến x_(k+1)  = 𝐱_k + p.Vì sao phải dùng m_k, thì vì m_k thường sẽ đơn giản hơn là f)
>
> Thế thì nếu như giải bài toán này **tìm thấy p khiến f ko giảm bao nhiêu, thì ta kết luận là trust region quá lớn** mà nguyên nhân là do khi đó **vì t.r quá lớn nên m_k ko còn hành xử giống f nữa**, nên ko dùng m_k để thay f được) 
>
> Khi đó ta sẽ **thu nhỏ trust region lại, và giải lại, và đến lúc nào đó với trust region nhỏ đủ thì m_k nhất định sẽ hành xử giống f, khi đó giải ra p sẽ giúp có thể thực hiện bước đi giảm f**
>
> Mình nghĩ: có cái gì đó rất đẹp ở đây: m_k giống như kẻ đóng thế của f, có thể làm tốt khi bảo nó làm những việc nhỏ thôi, khi đó, nếu ta chia nhỏ công việc ra thì hoàn toàn có thể m_k mô phỏng được f.
>
> Trust region thường là ball / hình như vòng tròn trong bivariate case, define bởi : 
>
> ||p|| ≤ Δ với Δ là bán kính 
>
> Và mô hình m_k thường được chọn là quadratic function (nhớ nhé, mô hình, là mô hình để mô phỏng lại f, nên là function)
>
> m_k(x_k + p) = f_k + pT ∇f_k + (1/2) pT B_k p
>
> f_k, ∇f_k thì là hàm f và gradient tại x_k rồi,
>
> còn B_k có thể dùng Hessian ∇^2 f(x_k) hoặc dùng một xấp xỉ của nó

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **98/100**
>
> Bài ghi chép này cực kỳ chính xác và chi tiết, giải thích sâu sắc về phương pháp trust region, từ việc xây dựng mô hình m_k đến cách điều chỉnh vùng tin cậy. Cách diễn giải bằng ví dụ "m_k như kẻ đóng thế của f" cùng với việc giải thích lý do ẩn sau các bước cho thấy sự nắm bắt vấn đề vượt trội.

<br>


<a id="node-jed1zsj"></a>
##### Vùng tin cậy: Bước và hướng

<p align="center"><kbd><img src="assets/img_jed1zsj.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_mns2tj.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_gaigh.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_d2lbr9.png" width="80%"></kbd></p>

> [!NOTE]
> Một minh họa
>
> QUAY LẠI XEM KĨ SAU

> [!TIP]
> **🤖 AI Feedback** — ❌ Score: **25/100**
>
> Bạn đã nhận diện đúng đây là một minh họa và có ý thức quay lại xem kỹ hơn, điều này rất tốt cho việc học. Để ghi chú hiệu quả hơn, hãy cố gắng trích xuất các ý chính như ý nghĩa của đường đồng mức, vùng tin cậy hoặc sự khác biệt với tìm kiếm đường thẳng.

<br>

<a id="node-ixn27an"></a>
- **Line Search và Trust Region**
<p align="center"><kbd><img src="assets/img_ixn27an.png" width="80%"></kbd></p>

> [!NOTE]
> Đại ý là, line search và trust region khác nhau cơ bản ở:
>
> Line search **chọn một hướng p_k**, và **tìm bước đi** phù hợp theo hướng đó.
>
> Trust region **chọn một bán kính**, sau đó **tìm p_k và step**. Nếu không giảm đủ thì thu nhỏ bán kính và làm lại.
>
> Vậy thì chap 3,4 sẽ bàn sâu về hai cái này,  nhưng trước hết ta sẽ tìm hiểu hai bước quan trọng trong hai cái này:
>
> **Chọn search direction p_k trong line search** và **chọn Hessian B_k của mô hình m_k trong trust region method**

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **97/100**
>
> Ghi chú tóm tắt rất hiệu quả sự khác biệt cốt lõi giữa hai phương pháp và xác định chính xác các vấn đề chính sẽ được thảo luận. Để sâu sắc hơn, bạn có thể bổ sung chi tiết rằng hai vấn đề chính (lựa chọn hướng tìm kiếm và Hessian) có "liên quan chặt chẽ" với nhau.

<br>

<a id="node-6xvbag7"></a>
- **Hướng dốc nhất và Taylor**
<p align="center"><kbd><img src="assets/img_6xvbag7.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_segdtxc.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_1ts3i9.png" width="80%"></kbd></p>

> [!NOTE]
> Bàn về chọn p_k của line search, gs cho rằng cách dể hiểu nhất, hợp lí nhất là chọn hướng dốc nhất, chính là - ∇f_k (tức gradient -∇f(x)|x = x_k)
>
> Và dùng Taylor theorem ta có thể chứng minh điều này (cũng không hiểu sao phải viện dẫn Taylor theorem, vì ta đã biết directional derivative theo hướng p evaluate tại x_k sẽ là ∇f_k Tp, và nó cũng chính là độ dốc của hàm xét theo hướng p, nếu muốn xét p nào có độ dốc lớn nhất, ta sẽ so các p có length bằng 1, tức giải bài toán: 
>
> minimize p ∇f_k Tp subject to ||p|| = 1 thì lập luận tiếp như sách để có p = -∇f_k / ||∇f_k||
>
> Có thể gs viện Taylor theorem để chỉ ra rằng ∇f_k Tp chính là độ dốc của hàm f theo hướng p tại x_k (là thứ mà mình nói "ta đã biết" ở trên).
>
> Ôn lại Taylor theorem: Nói rằng:
>
> Khi đi từ a → b, thì f(b) = f(a) + ∇f(a)T(b-a) + (1/2) (b-a)T ∇^2 f(c) (b-a) với some c in (a, b) 
>
> Cũng là áp dụng ở đây:
>
> f(x_k + αp) = f(x_k) + ∇f_k T(αp) + (1/2) (αp)T ∇f(c) αp với some c in (x_k, x_k + αp)
>
> tương đương: 
>
> f(x_k + αp) = f(x_k) + ∇f_k T(αp) + (1/2) (αp)T ∇f(x_k + tαp) αp với some t in (0,1)
>
> tương đương
>
> f(x_k + αp) = f(x_k) + ∇f_k T(αp) + (1/2) (αp)T ∇f(x_k + tp) αp với some t in (0, α)
>
> viết lại chút:
>
> f(x_k + αp) = f(x_k) + α ∇f_k Tp + (1/2) (α)^2 pT ∇f(x_k + tp) p với some t in (0, α)
>
> Và như vậy, tương đương tiếp:
>
> [f(x_k + αp) - f(x_k)] / α = ∇f_k Tp + (1/2) α pT ∇f(x_k + tp) p
>
> Lấy lim α → 0:
>
> thì vế trái là lim α → 0 [f(x_k + αp) - f(x_k)] / α, nó chính là đạo hàm theo hướng p, directional derivative, cũng là rate of change theo hướng p của hàm f tại x_k
>
> Còn vế phải sẽ là lim α → 0 ∇f_k Tp + (1/2) α pT ∇f(xk + tp) p = ∇f_k Tp
>
> Nói chung, có thể coi như giáo sư đã liên hệ định nghĩa directional derivative với Taylor theorem
>
> Và p_k như vầy sẽ luôn vuông góc với contour (level set): Đã học trong mit 1802, nhưng ở đây Taylor theorem cho ta thấy luôn:
>
> xét d là hướng tiếp tuyến với level curve của f tại x_k
>
> khi đó lim α → 0 [f(x_k + αd) - f(x_k)] / α là độ dốc của hàm theo hướng tiếp tuyến với level curve, mà đi theo level curve thì f ko đổi, nên độ dốc này bằng 0.
>
> nên ta có vế trái = 0,
>
> còn vế phải là ∇f_k Td như trên. Vậy ∇f_k vuông góc d và dĩ nhiên cũng - ∇fk cũng vậy 
>
> ⇨  steepest direction pk = - ∇f_k sẽ vuông góc với level curve

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **98/100**
>
> Bản phân tích rất sâu sắc và chính xác, giải thích chi tiết việc sử dụng Định lý Taylor để chứng minh tốc độ thay đổi và lý do hướng dốc nhất vuông góc với đường đồng mức, làm rõ những điểm mà hình ảnh chỉ đề cập vắn tắt.

<br>

<a id="node-k9sqzy0"></a>
- **Steepest descent và bước nhảy**
<p align="center"><kbd><img src="assets/img_k9sqzy0.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_ne4fgj.png" width="80%"></kbd></p>

> [!NOTE]
> Đại khái là, trong line search, dùng steepest descent có một ưu điểm là **chỉ phải tính gradient mà không cần Hessian**
>
> Tuy nhiên nó có thể **rất chậm nếu gặp bài toán khó**.
>
> Và line search cũng có thể dùng search direction khác ko nhất thiết -∇f.
>
> Đó là bất kì hướng nào có góc tù với gradient, và miễn sao là giữ cho step size nhỏ đủ thì đều có thể chắc giảm được f khi đi theo hướng đó.
>
> Mình nghĩ: Tại sao lúc này lại nói về việc phải giữ step size đủ nhỏ, bộ khi dùng steepest descent thì không cần hay sao?
>
> Không phải vậy, mà là đây sẽ là lập luận chứng minh chỉ cần đi theo hướng có góc tù với gradient và sải bước đủ nhỏ thì hướng nào cũng sẽ giảm f. Trong đó có steepest direction, chứ không phải là nếu đi theo hướng khác steepest thì mới phải giữ sải bước đủ nhỏ.
>
> Và chứng minh như sau:
>
> Dùng Taylor theorem, với p là hướng góc tù với gradient nói trên, bắt đầu tại x_k
>
> f(x_k + αp) = f(x_k) + ∇f(x_k)T(αp) + (1/2) (αp)T ∇^2 f(x_k + tαp) (αp) for some t in (0, 1)
>
> ≡ f(x_k + αp) = f(x_k) + ∇f(x_k)T(αp) + (1/2) (α)^2 pT ∇^2 f(x_k + tp) p for some t in (0, α)
>
> Và ta gọi (1/2) (α)^2 pT ∇^2 f(x_k + tp) p là O((α)^2) chỉ term sẽ tăng theo lũy thừa 2 của α.
>
> Viết lại f(x_k + αp) = f(x_k) + ∇f(x_k)Tαp + O((α)^2)
>
> ⇔ f(x_k + αp) = f(x_k) + α||∇f(x_k)||.||p||.cos(θ) + O((α)^2), θ là góc giữa p và ∇f(x_k)
>
> Khi đó, ý là vầy, với góc θ tù thì α||∇f(x_k)||||p||cos(θ) < 0
>
> Kh đó f(x_k) - f(x_k + αp) = - α||∇f(x_k)||||p||cos(θ) - O((α)^2)
>
> Thế thì - α||∇f(x_k)||||p||cos(θ) sẽ là một số dương và mà O((α)^2) (cũng là số dương), nên đây là hiệu của hai số dương, nếu O((α)^2) là số dương nhỏ thì cái hiệu này sẽ dương.
>
> Và vế trái chính là độ giảm của f khi từ x_k → x_k + αp
>
> Vậy, lập luận là, nếu giữ α đủ nhỏ, để O((α)^2) rất nhỏ coi như bỏ qua, = 0 
>
>  thì khi đó vế phải sẽ dương. Bất kể p có là hướng nào (miễn θ tù)
>
> Đó là lí do phải nói về step size đủ nhỏ, vì lớn quá có thể O((α)^2) sẽ dương lớn hơn cái kia, thành ra vế phải âm, hàm tăng

> [!TIP]
> **🤖 AI Feedback** — ⚠️ Score: **88/100**
>
> Bạn đã nắm vững các ưu và nhược điểm của phương pháp steepest descent và hiểu đúng về khái niệm hướng giảm tổng quát. Đặc biệt, cách bạn tự đặt câu hỏi và giải thích bằng chuỗi Taylor cho thấy tư duy phản biện và khả năng đào sâu vấn đề rất tốt.

> [!IMPORTANT]
> **🎤 Review Session 1** — Score: **55/100**
>
> Em đã nắm được khái niệm cơ bản về Steepest Descent và vị trí của nó trong Line Search. Tuy nhiên, em cần bổ sung thêm các điểm quan trọng khác như ưu điểm (chỉ cần tính gradient), nhược điểm (có thể rất chậm), và điều kiện về hướng giảm chung cũng như tầm quan trọng của việc chọn bước nhảy đủ nhỏ. Hãy thử đào sâu vào lý do tại sao bước nhảy phải nhỏ đủ để đảm bảo hàm giảm nhé.

<br>

<a id="node-wqcshqx"></a>
- **Hướng Newton qua xấp xỉ Taylor**
<p align="center"><kbd><img src="assets/img_wqcshqx.png" width="80%"></kbd></p>

> [!NOTE]
> Rồi, ta gặp lại người bạn cũ **Newton direction**, tác giả nói một search direction quan trọng có thể là quan trọng nhất chính là Newton direction. Đựơc derive bằng cách dùng xấp xỉ Taylor bậc hai của f(x_k + p).
>
> f(x_k + p) ≈ f(x_k) + ∇f(x_k)T p + (1/2) pT∇^2 f(x_k) p 
>
> Ghi gọn vế trái là f_k + ∇f_k Tp + (1/2) pT∇^2 f_k p 
>
> (đây là xấp xỉ Taylor bậc hai, ko phải Taylor theorem)
>
> Hàm bậc hai mà ta dùng để xấp xỉ hàm f, tại x_k, chính là m_k(p) là mô hình trust region tại x_k.
>
> Thế thì như đã biết ở ee364a, để tìm Newton step chính là ta xấp xỉ, hàm f, nói dễ hiểu hơn là ta coi hàm f như hàm bậc hai, để rồi giải tìm minimum của nó: 
>
> minimize f_hat (p) = f_k + ∇f_k Tp + (1/2) pT∇^2 f_k p 
>
> Và để giải tìm local minimizer ta cũng dùng điều kiện bậc 1: gradient = 0.
>
> Gradient của f_hat (p): Đây là hàm quadratic, mà gradient của hàm quadratic f(x) = (1/2)xTPx + qTx + r dễ dàng derive công thức là PTx + q.
>
> ⇨ ∇f_hat (p) = ∇^2 (f^)_k p + ∇f_k (Hessian đối xứng nên bỏ transpose)
>
> Cho gradient = 0 ⇨ ∇^2 f_k p + ∇fk = 0 ⇔ ∇^2 f_k p = -∇f_k
>
> Tới đây, trong sách giáo sư mới assume Hessian positive definite, ta hiểu để mà ∇^2 f_k khả nghịch
>
> ⇨ p = - ∇^2(f_k)^(-1) ∇f_k. Và đây chính là Newton step

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **98/100**
>
> Phân tích của bạn rất chính xác và thể hiện sự hiểu biết sâu sắc về hướng Newton và quá trình đạo hàm của nó. Bạn đã kết nối các khái niệm một cách xuất sắc.

<br>

<a id="node-u8epw6t"></a>
- **Độ tin cậy phương pháp Newton**
<p align="center"><kbd><img src="assets/img_u8epw6t.png" width="80%"></kbd></p>

> [!NOTE]
> Đoạn này rất hay: Đại khái là vì ta tìm Newton direction bằng cách xấp xỉ hàm f tại x_k bởi quadratic function, cũng chính là m_k, nên dĩ nhiên Newton direction chỉ tốt nếu như sự xấp xỉ này là tốt (khác biệt ko quá lớn)
>
> Vậy thì, công thức 2.6 của Taylor theorem cho ta cái hàm chính xác có thể thay f(x_k + p):
>
> f(x_k + p) = f(x_k) + ∇f(x_k)T p + (1/2) pT ∇^2 f(x_k + tp) p for some t in (0,1)
>
> Còn khi ta mô phỏng f bởi xấp xỉ bậc hai:
>
> f(x_k + p) ≈  f(x_k) + ∇f_k Tp + (1/2) pT ∇^2 f_k p
>
> Thì **cơ bản là ta đã thay ∇^2 f(x_k + tp) bởi ∇^2 f(x_k), nên từ dấu bằng, trở thành xấp xỉ ≈** 
>
> Và **mức độ sai khác giữa hai cái này sẽ quyết định mức độ sai khác của f(x_k + p) (chính xác) và mk(p)**.
>
> Thế thì, ở đây tác giả cho biết **nếu hàm f ĐỦ TRƠN**, thì sự khác biệt khi thay ∇^2 f(x_k + tp) bởi ∇^2 f(x_k) SẼ CHỈ THÊM VÀO MỘT TERM O((||p||)^3), tạm hiểu đại khái là, như vậy chỉ cần giữ p đủ nhỏ thì cái sai khác này ko đáng kể. 
>
> Và mình nghĩ: đây cũng chính là lí do cần giới hạn trust region trong phương pháp trust region: Vì trong đó ta cũng xây dựng mô hình mk là xấp xỉ bậc hai của f, nên nó chỉ đúng khi xét trong phạm vi nhỏ

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **98/100**
>
> Bạn đã nắm vững các khái niệm chính về độ tin cậy của hướng Newton và vai trò của xấp xỉ bậc hai. Khả năng kết nối kiến thức với phương pháp Trust Region là rất ấn tượng.

<br>

<a id="node-yw2hzjc"></a>
- **Hướng Newton là hướng giảm**
<p align="center"><kbd><img src="assets/img_yw2hzjc.png" width="80%"></kbd></p>

> [!NOTE]
> Đại khái là chỗ này tác giả muốn nói **Newton direction CŨNG LÀ DESCENT DIRECTION**, nên nó cũng có thể được dùng trong line search (vì trong line search, ta nhớ đầu tiên là chọn hướng để đi, p, là một descent direction. Sau đó mới chọn sải bước tối ưu hoặc chấp nhận được.
>
> Nhưng điều này chỉ đúng khi Hessian tại x_k, ∇^2 f_k positive definite. Nói sơ trước khi đi vào chi tiết, là vì ta tính ra directional derivative theo hướng Newton tại x_k của f sẽ thấy nó là (âm) quadratic form của Hessian của f tại x_k, do đó, chỉ khi Hessian tại x_k positive definite thì ta mới đảm bảo là cái giá trị đạo hàm theo hướng Newton tại x_k âm, để cho thấy là đi theo hướng đó sẽ giảm f.
>
> Ta sẽ muốn xem thử directional derivative theo hướng Newton có âm không (để đi theo hướng đó, với xải bước nhỏ đủ, thì như lập luận lúc nãy, nhất định hàm f sẽ giảm)
>
> Gọi (p_k)^N, hay ở đây mình ghi là pkN, là hướng Newton tại x_k:
>
> Directional derivative theo hướng Newton tại x_k:
> ab
> (∇)_(pkN) f(x) | (x=x_k) = (∇)_(pkN) f_k = ∇f_k T pkN,
>
> với Newton direction (step) : pkN như nãy đã biết, = - (∇^2f_k)inv ∇fk
>
> ⇨ (∇)_(pkN) f_k = - ∇f_k T (∇^2f_k)inv ∇f_k
>
> Tới đây thì theo mình thì đã có thể kết luận cái này âm rồi:
>
> Lí do là nếu ∇^2 f_k positive definite, thì mọi eigenvalue của nó đều dương và dĩ nhiên mọi nghịch đảo của eigenvalue cũng dương ⇨ (∇^2f_k)inv cũng positive definite.
>
> Mà với positive definite A thì ta biết tính chất là quadratic form xTAx luôn dương với mọi x khác 0,  và chỉ bằng 0 khi x = 0.
>
> Vậy thì từ đó  ∇f_k T (∇^2fk)inv ∇f_k, sẽ luôn dương khi gradient tại x_k, tức ∇f_k khác 0, và chỉ bằng 0 khi gradient bằng 0 
>
> Do đó -  ∇f_k T (∇^2f_k)inv ∇f_k luôn âm khi gradient khác 0.
>
> Còn ở trong sách, ta có thể biến đổi thêm chút: nhân cho Identity matrix:
>
> (∇)_(pkN) f_k = - ∇f_k T (∇^2f_k)inv ∇f_k
>
> = - ∇f_k I (∇^2f_k)inv ∇f_k
>
> = - ∇f_k T (∇^2f_k)inv ∇^2 f_k (∇^2f_k)inv ∇f_k
>
> = - [(∇^2f_k)inv ∇fk]T ∇^2 f_k [(∇^2f_k)inv ∇f_k]
>
> = - (pkN)T ∇^2 f_k pkN
>
> Và lập luận tương tự, cái này luôn âm nhờ tính positive definite của Hessian và chỉ bằng 0 khi pkN = 0 ⇔ (∇^2f_k)inv ∇f_k = 0. 
>
> Và vì (∇^2f_k)inv positive definite nên dĩ nhiên là full rank, nên nullspace chỉ có {0}, dẫn tới là (∇^2f_k)inv ∇f_k = 0 ⇔ ∇f_k = 0: 
>
> Còn cái vụ - (pkN)T ∇^2 f_k pkN ≤  - σk (||pkN||)^2?
>
> Đó là eigen-decomposition của một symmetric matrix A thành dạng QΛQT (hoặc gọi cụ thể hơn còn gọi là diagonalization, dù bản chất vẫn là eigen-decomposition vì nó phân rã matrix thành một matrix diagonal)
>
> Đặt u = pkN, A =∇^2 f_k
>
> ⇨ (pkN)T ∇^2 f_k pkN = uTAu 
>
> = uTQ Λ QTu. Đặt v = QTu, cái ta có sẽ là vTΛv = Σ_i=1:n λ_i (v_i)^2 (λ_i là các eigenvalues của Hessian ∇^2 f_k)
>
> Và cái này Σi λmin (v_i)^2 ≤ Σ λi (v_i)^2 ≤  Σi λmax (v_i)^2
>
> ⇨ - Σ λi (v_i)^2 ≤ - Σi λmin (v_i)^2 = - λmin Σi (v_i)^2 = - λmin (||v||)^2
>
> ⇔ - Σ λi (v_i)^2 ≤ - λmin (vTv)
>
> ⇔ - Σ λi (v_i)^2 ≤ - λmin (QTu)T(QTu)
>
> ⇔ - Σ λi (v_i)^2 ≤ - λmin uTQQTu
>
> ⇔ - Σ λi (v_i)^2 ≤ - λmin uTu
>
> ⇔ - Σ λi (v_i)^2 ≤ - λmin (||u||)^2
>
> Áp dụng vào đây, - (pkN)T ∇^2 f_k pkN ≤ - λmin (||pkN||)^2
>
> nên σk ở trên chính là λmin của Hessian ∇^2 f_k

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **98/100**
>
> Bài làm của bạn thể hiện sự hiểu biết sâu sắc và toàn diện về hướng Newton như một hướng giảm, bao gồm cả các chứng minh toán học chi tiết vượt xa tài liệu tham khảo.

<br>

<a id="node-vwfz9t9"></a>
- **Sải bước tự nhiên của Newton**
<p align="center"><kbd><img src="assets/img_vwfz9t9.png" width="80%"></kbd></p>

> [!NOTE]
> Đây cũng là một ý rất hay mà mình từng suy nghĩ: Newton direction tuy cũng là một hướng, nhưng nó có một sải bước tự nhiên, bằng 1, khác với steepest descent.
>
> Lí do là với steepest descent, có thể hiểu là nó, cho ta một hướng có độ dốc lớn nhất tại điểm đang đứng, và theo Taylor theorem, miễn là ta giữ sải bước đủ nhỏ, thì theo hướng đó nó sẽ đưa ta đi xuống.
>
> Nhưng nó ko hề nói gì về sải bước (step size)
>
> Còn động cơ của Newton method thì khác, tại xk, ta thay hàm f, bởi xấp xỉ bậc hai của nó, và từ đó tìm local minimizer của hàm bậc hai. Và kết quả nó cho ta một vector chỉ hướng từ xk đến minimizer, nhưng đồng thời cũng cho ta độ lớn của sải bước, để theo hướng đó, đi đến minimizer. Có nghĩa là, một cách tự nhiên, Newton direction có step factor bằng 1, tức là tính ra Newton direction vector có độ dài bao nhiêu thì lấy bấy nhiêu
>
> Và như ta đã thấy chỉ cần Hessian tại xk positive definite thì Newton direction là descent direction, nhưng chưa chắc full step size là step size tối ưu. Có nghĩa là tuy ta có thể dùng Newton direction cho line search nhưng chưa chắc dùng step factor  = 1 là tối ưu, đơn giản là vì ta chỉ đang xấp xỉ bậc hai hàm f mà đương nhiên là nó ko chắc chắc là đúng.
>
> Do đó ở đây gs cho biết phần lớn line search  nếu đã dùng Newton step thì họ dùng luôn unit step tuy nhiên vẫn có khi ta adjust nó

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **98/100**
>
> Ghi chú rất chính xác và giải thích sâu sắc về sải bước tự nhiên của phương pháp Newton, cùng với sự khác biệt so với steepest descent. Nội dung cũng nắm bắt tốt việc khi nào bước nhảy được điều chỉnh, thể hiện sự hiểu biết toàn diện về phương pháp.

<br>

<a id="node-nv3sbgy"></a>
- **Newton: Điều kiện và chi phí**
<p align="center"><kbd><img src="assets/img_nv3sbgy.png" width="80%"></kbd></p>

> [!NOTE]
> Tiếp, khi Hessian ko positive definite, thì dĩ nhiên ko có Hessian inverse nên ta không có (không define được) Newton direction.
>
> Nhưng ngay cả khi nó define, thì cũng chưa chắc nó là descent direction.
>
> Chỗ này là vì, để có Newton direction, ta chỉ cần Hessian invertible, nhưng để là descent direction, thì ta còn cần Hessian positive definite nữa.
>
> Do đó trong những case này, có khi người ta sẽ điều chỉnh pk để giúp nó thỏa descent property,
>
> Đoạn tiếp theo nói về một thứ mình đã học trong Convex Optimization, đó là nó có tỉ lệ / tốc độ hội tụ nhanh, khi mà ta đã tiếp cận được vùng lân cận của solution (local minimizer) thì khi đó đại khái là trạng thái well condition ngày càng tốt, hiểu nôm na là "bề mặt" của optimization landscape ngày càng giống một hàm bậc hai, khiến cho việc xấp xỉ bậc hai hàm f ngày càng chính xác. 
>
> Dẫn tới việc tìm ra approximated solution (minimizer của hàm bậc 2 xấp xỉ f) sẽ ngày càng chính xác so với solution thật. Và dẫn tới cái gọi là quadratic convergence, trong giai đoạn gọi là Newton phase.
>
> Tuy nhiên cái nhược điểm lớn nhất của Newton direction là Hessian, phải tính Hessian: Dễ sai, phức tạp và tốn kém.
>
> Nên qua chương 8 mình sẽ học về finite-difference và automatic differentiation (thật ra đã học ở MIT 18s096)

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **98/100**
>
> Ghi chú này rất chính xác và sâu sắc, thể hiện sự hiểu biết rõ ràng về các khái niệm trong bài đọc. Đặc biệt, phần giải thích cơ chế hội tụ bậc hai và sự cần thiết của Hessian positive definite đã bổ sung thêm giá trị đáng kể.

<br>

<a id="node-p3pvsbu"></a>
- **Nguyên lý phương pháp Quasi-Newton**
<p align="center"><kbd><img src="assets/img_p3pvsbu.png" width="80%"></kbd></p>

> [!NOTE]
> Đây là lúc mình được học về phương pháp rất nổi tiếng Quasi-Newton đây.
>
> Đại khái là, ta sẽ muốn đạt được hiệu quả tương tự như Newton's method, như tốc độ hội tụ nhanh, nhưng không phải tính toán Hessian.
>
> Và người ta sẽ t**ính toán một matrix xấp xỉ của Hessian tại xk, gọi là Bk** theo cách làm là ta sẽ tận dụng thông tin có được sau mỗi step để update B và nó tận dụng sự thật là: 
>
> **SỰ THAY ĐỔI CỦA GRADIENT SAU MỖI STEP CÓ ĐEM ĐẾN MỘT LƯỢNG THÔNG TIN NÀO ĐÓ VỀ ĐẠO HÀM BẬC HAI THEO HƯỚNG SEARCH DIRECTION**
>
> Lập luận như sau:
>
> Đầu tiên ta dùng lại 2.5 của Taylor theorem (mà mình đã hiểu = tự chứng minh từ FTC)
>
> ∇f(x + p) = ∇f(x) + ∫0:1 ∇^2 f(x + tp) p dt
>
> Cộng và trừ cho ∇^2 f(x)p:
>
> ∇f(x + p) = ∇f(x) +  ∇^2 f(x)p - ∇^2 f(x)p + ∫0:1 ∇^2 f(x + tp) p dt
>
> Coi - ∇^2 f(x)p = ∫0:1 ∇^2 f(x)p dt, vì vế phải đúng là bằng vế trái nếu tính tích phân ra: ∇^2 f(x)p t|0:1 = ∇^2 f(x)p*1  - ∇^2 f(x)p*0 = ∇^2 f(x)p
>
> ⇔ ∇f(x + p) = ∇f(x) + ∇^2 f(x)p -  ∫0:1 ∇^2 f(x)p dt + ∫0:1 ∇^2 f(x + tp)p dt
>
> Gom hai tích phân lại:
>
> ⇔ ∇f(x + p) = ∇f(x) + ∇^2 f(x)p +  ∫0:1 [∇^2f(x + tp) - ∇^2 f(x)] p dt
>
> Xét cái term thứ 3:  ∫0:1 [∇^2 f(x + tp) - ∇^2 f(x)] p dt
>
> Đại khái là, nếu đặt G = ∫0:1 [∇^2 f(x + tp) - ∇^2f(x)] p dt,
>
> (lưu ý, đây tích phân này kết quả là vector)
>
> ||G|| = ∫0:1 ||[∇^2 f(x + tp) - ∇^2 f(x)]|| ||p|| dt,
>
> xét lim ||p|| → 0 ||G|| / ||p||
>
> thì khi ||p|| → 0 tức là xét vector p có length ngày càng nhỏ về 0, thì x + tp cũng → x 
>
> Do hàm f liên tục nên Hessian tại x + tp cũng → Hessian tại x
>
> ⇨ ||[∇^2 f(x + tp) - ∇^2 f(x)]|| → 0
>
> và ||p|| cũng → 0, 
>
> Nên tích của hai cái này còn → 0 nhanh hơn cả p nữa.
>
> Nên mới ghi là kích thước của ∫0:1 [∇^2 f(x + tp) - ∇^2 f(x)] p dt sẽ là o(||p||) ý là nhỏ về 0 rất nhanh, nhanh hơn cả ||p||
>
> Do đó, mới nói cái tích phân này là o(||p||), mang ý nghĩa là  nó là cái term
> tiến về 0 rất nhanh, nhanh hơn cái khi norm p (||p||) tiến về 0.

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **98/100**
>
> Ghi chú của bạn thể hiện sự hiểu biết sâu sắc và chính xác về phương pháp Quasi-Newton, đặc biệt là phần giải thích chi tiết về đạo hàm bậc hai và ký hiệu o(||p||).

<br>

<a id="node-cp5fa4k"></a>
- **Hessian xác định dương gần x***
<p align="center"><kbd><img src="assets/img_cp5fa4k.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_4j5dqf.png" width="80%"></kbd></p>

> [!NOTE]
> Rồi, ta cho x = xk, p = xk+1 - xk:
>
> ∇f(x + p) = ∇f(x) + ∇^2 f(x)p +  o(||p||)
>
> trở thành:
>
> ⇔ ∇f_(k+1) = ∇f_k + ∇^2 f_k (x_(k+1) - x_k) + o(||x_(k+1) - x_k||)
>
> Tới đây là lập luận quan trọng: 
>
> Khi ngày càng gần x*, thì thì bước sải xk+1 - xk sẽ nhỏ lại, lí do là:
>
> Ví dụ như ở đây dùng Newton direction, pk = - ∇^2 f_k ∇f_k
>
> thì khi x_k → x* thì ∇f(x_k) → ∇f(x*) do hàm liên tục, mà ∇f(x*) = 0
>
> ⇨ pk = - ∇^2 f_k ∇f_k → - ∇^2 f(x*) ∇f(x*) = - ∇^2 f(x*) × 0 = 0
>
> Từ đó cho ta được phép nói rằng: 
>
> **Khi càng gần x* thì x_(k+1) - x_k ngày càng nhỏ về 0**
>
> Thế thì xét hai cái term ∇^2 f_k(x_(k+1) - x_k), và o(||x_(k+1) - x_k||) 
>
> khi x_(k+1) - x_k → vector 0, cũng là ||x_(k+1) - x_k|| → scalar 0, 
>
> Và như vậy **sẽ đến lúc nó bị dominated bởi  ∇^2 f_k(x_(k+1) - x_k)**
>
> VÌ SAO?
>
> VÌ ∇^2 f_k(x_(k+1) - x_k) chỉ giảm tuyến tính theo độ lớn của sải bước x_(k+1) - x_k
>
> Trong khi o(||x_(k+1) - x_k||)  thì giảm nhanh hơn là giảm tuyến tính độ giảm của sải bước sải bước x_(k+1) - x_k (vì như trên đã phân tích)
>
> Do đó, chỉ cần ∇^2 f_k(x_(k+1) - x_k) KHÔNG ĐỘT NHIÊN BẰNG 0, THÌ CHẮC CHẮN NÓ SẼ CÓ LÚC DOMINATE o(||x_(k+1) - x_k||).
>
> VÌ SAO NÓI NÓ KHÔNG ĐƯỢC ĐỘT NHIÊN BẰNG 0? 
>
> Là vì nếu x_(k+1) - x_k trở thành nullspace vector của matrix  ∇^2 f_k, thì ∇^2 f_k (x_(k+1) - x_k) sẽ = 0. Khi đó ta sẽ **không có cái vụ dominate, nên không được quyền bỏ o(||x_(k+1) - x_k||) và cũng là nếu dùng xấp xỉ sẽ là sai**
>
> Chính vì vậy, mới nhắc đến việc tại gần x*, Hessian **POSITIVE DEFINITE**
>
> **VÌ ĐIỀU NÀY ĐẢM BẢO LÀ ∇^2 f_k FULL RANK, NON-SINGULAR, NULLSPACE CHỈ CÓ {0}, giúp ta đảm bảo có thể bỏ đi o(||xk+1 - xk||) và xấp xỉ là ĐƯỢC PHÉP**
>
> VẬY THÌ VÌ SAO GẦN x* THÌ HESSIAN LẠI POSITIVE DEFINITE?  
>
> LÀ VÌ Ở ĐÂY NGƯỜI TA ĐANG ĐẶT RA ASSUMPTION NHƯ VẬY (ko phải là điều luôn đúng, vì theo điều kiện cần bậc 2, thì nếu x* là local minimizer thì chỉ có thể kết luận Hessian tại đó xác định bán dương)
>
> Tóm lại nếu những giả định trên thỏa mãn (Hessian xác định dương khi gần x*) thì giúp ta có thể nói rằng: *khi x_k, x_(k+1) gần solution x* thì o(||xk+1 - xk||) coi như quá nhỏ, coi như bỏ đi dẫn đến ta có xấp xỉ:
>
> ∇f_(k+1) ≈ ∇f_k + ∇^2 f_k (x_(k+1) - x_k) 
>
> ⇔ ∇f_(k+1) - ∇f_k ≈ ∇^2 f_k (x_(k+1) - x_k)
>
> ⇔ ∇^2 f_k (x_(k+1) - x_k) ≈ ∇f_(k+1) - ∇f_k 
>
> Và đây không phải để chơi, mà chính là cơ sở cho việc dùng một matrix B_k xấp xỉ cho Hessian tại x_k: Ta sẽ dùng matrix cũng thỏa cái tính chất trên.

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **98/100**
>
> Ghi chú này cung cấp một phân tích rất sâu sắc và chính xác về lý do các điều kiện (Hessian xác định dương, bước nhảy nhỏ) dẫn đến sự trội hơn của một số hạng trong khai triển Taylor. Nó không chỉ lặp lại nội dung mà còn giải thích tường tận từng yếu tố toán học liên quan, thể hiện sự hiểu biết sâu sắc về ngữ cảnh.

<br>

<a id="node-j9epg7b"></a>
- **Xấp xỉ Hessian và Secant**
<p align="center"><kbd><img src="assets/img_j9epg7b.png" width="80%"></kbd></p>

> [!NOTE]
> Dựa trên sự thật này, là với Hessian thật, thì nó có tính chất khi gần x* thì: 
>
> ∇^2 f_k (x_(k+1) - x_k) ≈ ∇f_(k+1) - ∇f_k 
>
> Người ta mới **chọn** B_(k+1), là một xấp xỉ của Hessian sao cho nó thỏa tính chất trên. 
>
> Và đó chính là **SECANT EQUATION**:
>
> B_(k+1) s_k = y_k với s_k = x_(k+1) - x_k, y_k = ∇f_(k+1) - ∇f_k
>
> Nhắc lại, lập luận xuất phát từ việc, nếu ta (thỏa) giả định local minimizer có **Hessian  positive definite**, thì **tồn tại một vùng lân cận Hessian cũng positive definite**, cùng với lập luận ở trên, cho phép ta có quyền nói rằng, à, khi tới gần x*, thì ta có một phương trình xấp xỉ như vầy: 
>
> ∇^2 f_k (x_(k+1) - x_k) ≈ ∇f_(k+1) - ∇f_k
>
> Và dựa trên phương trình này, hay tính chất này của Hessian "thật", ta sẽ làm giả một cái Hessian (xấp xỉ nó), thay vì tính ra Hessian thật phiền phức, mà **việc làm giả nếu như vẫn thỏa tính chất trên thì khi dùng nó ta cũng có thể có được lợi ích từ Newton method.**
>
> Rồi, thêm nữa, khi "làm giả", ta cũng bắt chước một tính chất nữa của Hessian là tính đối xứng, và làm thêm một tính chất nữa, là **chế ra B sao cho Bk+1 - Bk, tức hiệu hai cái kế nhau là một matrix low rank** (có thể là để phục vụ ý đồ nào đó)

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **98/100**
>
> Ghi chú tóm tắt rất chính xác các khái niệm cốt lõi từ văn bản, bao gồm phương trình secant và các điều kiện bổ sung. Ghi chú cũng cung cấp độ sâu ngữ cảnh tuyệt vời về động cơ của việc xấp xỉ ma trận Hessian.

<br>

<a id="node-bduulna"></a>
- **Công thức xấp xỉ Hessian SR1, BFGS**
<p align="center"><kbd><img src="assets/img_bduulna.png" width="80%"></kbd></p>

> [!NOTE]
> Và hai công thức để CHẾ ra Bk (xấp xỉ cho Hessian) thông dụng là SR1 và BFGS trong đó cái đầu thì hiệu hai B là rank 1, cái sau là rank 2.
>
> Ta sẽ gặp lại ở các phần sau

<br>

<a id="node-q82d1ll"></a>
- **Cập nhật nghịch đảo Quasi-Newton**
<p align="center"><kbd><img src="assets/img_q82d1ll.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_kcpsl.png" width="80%"></kbd></p>

> [!NOTE]
> Thế thì, khi ta t**hay Hessian (∇^2)_k, bằng cách dùng B_k**, thì cái mà ta có sẽ là **Quasi-Newton search direction** (thay vì Newton direction)
>
> pk = - (Bk)inv ∇f_k
>
> Tiếp, một số cách thực hiện của quasi-Newton method **cố gắng tránh việc phải mỗi lần iterate là mỗi lần factorized Bk**, và họ làm việc này bằng cách** update inverse của Bk thay vì update Bk.**
>
> Thế thì ở đây nói phải factorized Bk là sao? là vì giả sử ta chế ra Bk, thì để tính ra Quasi-Newton direction ta sẽ phải tính (Bk)inv
>
> Mà như đã học ở phần phụ lục của Convex Optimization, việc tìm Ainv vốn dĩ là giải một loạt các hệ A u_i = e_i, với e_i là standard basis vector, để có u_i là cột i của Ainv. 
>
> Thì việc giải hệ phương trình thì như đã biết, ta sẽ làm bằng **factor-solve approach**, tức đầu tiên là factor A thành tích các matrix có cấu trúc đơn giản. Ví dụ CDE, sau đó giải A u_i =  e_i chính là giải lần lượt C v_i = e_i, D z_i = v_i, E u_i = z_i. Mà lí do là vì tổng chi phí sẽ ít hơn là gỉải trực tiếp A u_i = e_i
>
> Bởi vậy ở đây người ta mới update, tính ra (Bk)inv luôn, khỏi phải tính Bk rồi tính (Bk)inv
>
> Và cái (Bk)inv của hai công thức SR1 và BFGS là như này.
>
> Khi đó pk chỉ việc dùng, pk = -Hk ∇fk
>
> Chapter 7 sẽ nói đến hai biến thể của quasi-Newton dùng cho bài toán lớn

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **98/100**
>
> Ghi chú giải thích rất chính xác các khái niệm từ hình ảnh, đặc biệt làm rõ lý do cần tránh việc phân tích nhân tử ma trận và phương pháp cập nhật nghịch đảo trực tiếp. Độ sâu kiến thức về đại số tuyến tính được thể hiện rõ ràng.

<br>

<a id="node-p2dwwvl"></a>
- **Tổng quan Conjugate Gradient phi tuyến**
<p align="center"><kbd><img src="assets/img_p2dwwvl.png" width="80%"></kbd></p>

> [!NOTE]
> Một cái nữa mà ta sẽ học kĩ ở chương 5 là **nonlinear conjugate gradient method**
>
> Thì ở đây tác giả cho biết, ý tưởng, cảm hứng của nó ban đầu là để giải hệ Ax = b, mà cụ thể là giải hệ này thông qua việc giải bài toán tương đương: 
>
> minimize hàm Φ(x) = (1/2)xTAx - bTx
>
> Cái này mình đã gặp ở **Convex Optimization** rồi, nên hiểu. Là vì khi ta giải Ax = b, chính là giải Ax - b = 0 Vậy nếu coi Ax - b là gradient của một hàm số nào đó, thì tìm x để Ax - b = 0 chính là tìm local minimizer của hàm số đó. 
>
> Và ∇f(x) = Ax - b, là hàm tuyến tính, thì f là hàm bậc hai: f(x) = 1/2 xTAx - bTx. 
>
> Và từ đó cho ta phương pháp để giải hệ Ax = b bằng cách dùng các tiếp cận iterative trong việc giải bài toán tối ưu.
>
> Tác giả nói thêm, cái **direction của phương pháp này tốt hơn cả steepest descent** dù nó **ko mang lại convergence rate nhanh như Newton nhưng nó có ưu điểm là ko phải lưu trữ matrix**

> [!TIP]
> **🤖 AI Feedback** — ⚠️ Score: **85/100**
>
> Ghi chú giải thích rất tốt về cảm hứng và sự tương đương của bài toán. Tuy nhiên, cần bổ sung điều kiện rằng ma trận A phải đối xứng và xác định dương, cũng như đặc tính "conjugate" của các hướng tìm kiếm pk và pk-1 để ghi chú hoàn chỉnh hơn.

<br>

<a id="node-fzsjy59"></a>
- **Steepest Descent trong Trust Region**
<p align="center"><kbd><img src="assets/img_fzsjy59.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_7pluf.png" width="80%"></kbd></p>

> [!NOTE]
> Đại khái là, những **search direction** thảo luận ở trên **đều có thể dùng trực tiếp trong line search để tạo thành steepest descent, Newton, quasi-Newton, conjugate gradient line search** 
>
> Và trừ cái conjugate gradient thì những cái đó **đều có phiên bản tương đương của trust region**
>
> Thế thì tác giả nói, nếu ta cho Bk = 0 trong 2.12 (Chiến lược Trust Region)
>
> m_k(x_k + p) = f_k + pT ∇f_k + (1/2) pT B_k p
>
> sẽ trở thành m_k(x_k + p) = f_k + pT ∇f_k
>
> ====
>
> Ôn lại một chút về trust region: Ý tưởng sẽ là, ta dùng một sự thật là, **khi xét trong một phạm vi đủ nhỏ nào đó (quanh x_k), thì hàm số sẽ hành xử giống như hàm bậc hai**. Cụ thể là như sau: Dựa vào Taylor theorem, nói rằng khi đi từ x đến x + p thì ta có:
>
> f(x + p) = f(x) + ∇f(x_k)Tp + (1/2) pT ∇^2 f(z) p với z là điểm nào đó ∈ (x, x+p)
>
> ≡ f(x + p) = f(x) + ∇f(x_k)Tp + (1/2) pT ∇^2 f(x + tp) p với t là giá trị nào đó ∈ (0, 1)
>
> Và nếu xét trong phạm vi nhỏ nào đó khiến ∇^2 f(x + tp) ≈ ∇^2 f(x) thì ta sẽ có:
>
> f(x + p) ≈ f(x) + ∇f(x_k)Tp + (1/2) pT ∇^2 f(x ) p đây là chính là nói nếu xét trong phạm vi đủ nhỏ quanh x thì có thể coi hàm số hành xử như quadratic function: 
>
> g(p) = f_hat (x + p) = (1/2) pT ∇^2 f(x) p + ∇f(x_k)Tp +  f(x) 
>
> Từ đó, ta sẽ **mô phỏng hàm f bởi một hàm bậc hai, nhưng đảm bảo là chỉ trong một trust region nhất định.**
>
> Để rồi, để tìm pk, ta giải bài toán **minimize quadratic function có constraint**:
>
> minimize m_k (x_k + p) = f_k + pT∇f_k + (1/2)pT B_k p 
>
> constrained ||p|| < trust region radius Δk
>
> Giải ra nếu kiểm tra thấy mức giảm hàm f thực tế ko đạt, thì có nghĩa là trust region đang quá rộng, khiến việc dùng hàm quadratic để mô phỏng hàm f bị sai, ta sẽ thu nhỏ radius lại và làm lại.
>
> Bk trong mk có thể dùng Hessian hoặc dùng một xấp xỉ của Hessian
>
> ====
>
> Quay lại đây, khi Bk = 0, thì ta có bài toán minimize f_k + pT∇f_k subject to ||p|| ≤ Δk
>
> Thế thì, solution có nó có thể có dạng đóng là pk = - Δk ∇f_k / ||∇f_k||
>
> Là sao ta?
>
> Hàm m_k(x_k + p) = f_k + pT∇f_k lúc này là hàm tuyến tính
>
> Và f_k fixed rồi, nên đơn giản là ta minimize pT∇f_k = ||p|| ||∇fk|| cos(θ) subject to ||p|| ≤ Δk
>
> Mà -1 ≤ cos(θ) ≤ 1 ⇨ - ||p|| ||∇f_k|| ≤ ||p|| ||∇f_k|| cos(θ) ≤ ||p|| ||∇f_k|| nên nó sẽ đạt giá trị nhỏ nhất khi:
>
> 1) cos(θ) = -1, tức p = - ∇f_k và
>
> 2) ||p|| = Δk (vì p = max khả năng thì -||p|| mới âm nhỏ nhất)
>
> Do đó solution p là vector:  -(∇f_k / ||∇f_k||) Δk
>
> Và lúc này, đây chính là **steepest descent direction** với step length giới hạn = trust region radius.
>
> Ý tác giả là, à, khi **dùng quadratic function để làm m_k** (mô phỏng hàm f trong phạm vi nhỏ) và **chọn B_k = 0, thì cái descent direction giải ra hóa ra chính là steepest descent direction**

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **100/100**
>
> Bài làm của bạn rất xuất sắc! Bạn không chỉ nắm vững thông tin từ tài liệu mà còn mở rộng và giải thích sâu sắc về phương pháp Trust Region, cùng với việc tự suy luận chính xác về trường hợp đặc biệt.

<br>

<a id="node-rlyd3im"></a>
- **Thuật toán vùng tin cậy Hessian**
<p align="center"><kbd><img src="assets/img_rlyd3im.png" width="80%"></kbd></p>

> [!NOTE]
> QUAY LẠI SAU

<br>

<a id="node-00nhamu"></a>
- **Vấn đề Scaling trong tối ưu**
<p align="center"><kbd><img src="assets/img_00nhamu.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_7tqrr.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_euyls.png" width="80%"></kbd></p>

> [!NOTE]
> Đại khái là, hiệu quả của thuật toán tối ưu sẽ **PHỤ THUỘC CỰC LỚN VÀO CÁCH MÀ VẤN ĐỀ ĐƯỢC FORMULATED.**
>
> Và một vấn đề quan trọng của cái này là **SCALING**.
>
> Trong bài toán tối ưu ko ràng buộc, một problem được gọi là **POORLY SCALED nếu thay đổi x theo một hướng này  khiến hàm số tăng hay giảm nhanh hơn là hướng khác** (nhạy cảm hơn)
>
> Và ông nói đại khái là vấn đề này xuất hiện trong các ví dụ như trong **các hệ thống mà có nhiều process diễn ra với tốc độ khác nhau**.
>
> Và đại khái như có 4 feature x1, x2,...x4 thì **x1 có các value scale** khác nhau. ví dụ như x1 thì cỡ 10^(-10), x2, x3 thì cỡ 1 (ý là 1-10) còn x4 cỡ 10^5
>
> Đại khái là bằng cách **tạo một feature vector khác z**, **liên hệ với x bởi matrix này**, thì **z sẽ có range xem xem** với nhau hơn. 
>
> Đây gọi là diagonal scaling (mình nghĩ: đây chính là một dạng feature scaling)

> [!TIP]
> **🤖 AI Feedback** — ⚠️ Score: **82/100**
>
> Bản ghi chú tóm tắt rất chính xác và đầy đủ các thông tin có trong hình ảnh. Tuy nhiên, phần cuối về "feature vector z" và "diagonal scaling" không xuất hiện trong hình ảnh được cung cấp, do đó ghi chú không hoàn toàn dựa trên nguồn ảnh này.

<br>

<a id="node-bcna8vy"></a>
- **Scaling, Steepest Descent, Newton**
<p align="center"><kbd><img src="assets/img_bcna8vy.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_t5c1h8.png" width="80%"></kbd></p>

> [!NOTE]
> Như ở đây, chính là nói cái mà ta gặp trong machine learning, **khi các feature có các đơn vị đo khác nhau dẫn đến range của chúng khác nhau ⇨ tạo ra vấn đề poorly scaled**.
>
> Do đó trong quá trình modeling (phát triển mô hình) ta** cần thay đổi units của các variable sao cho chúng có range xem xem nhau** (đây chính là feature scaling, hay standardization)
>
> Cuối cùng **một số thuật toán như steepest descent rất bị ảnh hưởng bởi poor scaling**, như mình đến giờ này thì đã hiểu, và sẽ còn gặp lại phân tích này ở chương sau nữa, **đó là vì nó chọn hướng dốc nhất nên gặp poorly scaled, nó sẽ nhảy qua nhảy lại giữa hai sườn dốc** → chậm hội tụ
>
> Còn **Newton method THÌ LẠI ÍT BỊ  ẢNH HƯỞNG**, do nó dùng quadratic approx, nên về cơ bản **kể cả là poorly scale, thì miễn là hàm số có thể được approx tốt ở dạng quadratic** (mà trong hình thì chính là vậy, dù hình trên hay hình dưới) thì newton direction & step sẽ đều chính xác - chỉ ngay đến minimum

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **98/100**
>
> Phân tích của bạn rất chính xác và chi tiết, thể hiện sự hiểu biết sâu sắc về khái niệm scaling và ảnh hưởng của nó đến các thuật toán tối ưu hóa khác nhau.

<br>

<a id="node-2myt2fm"></a>
- **Thiết kế thuật toán bất biến tỉ lệ**
<p align="center"><kbd><img src="assets/img_2myt2fm.png" width="80%"></kbd></p>

> [!NOTE]
> Cuối cùng, việc thiết kế một thuật toán tối ưu mà ít nhạy cảm với scaling thì tốt hơn.
>
> Và người ta sẽ cố gắng thiết kế tính chất này vào mọi khía cạnh của thuật toán tối ưu như line search, trust region và convergence test
>
> Đó gọi là tính chất **SCALE INVARIANCE**

<br>


<a id="node-azejzbf"></a>
## Tối ưu không ràng buộc

<p align="center"><kbd><img src="assets/img_azejzbf.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_ylovhq.png" width="80%"></kbd></p>

> [!NOTE]
> Vì nhận thấy cuốn **Algorithm For Optimization** có đặc điểm là cover
> rộng, nhiều thuật toán, nhưng với mỗi cái chỉ nói sơ sơ, do đó nên
> đọc cuốn Numerical Optimization trước, sau đó mới quay lại cuốn kia
>
> Thế thì ở đây có mở đầu có vài điểm cũng đáng chú ý. Mở đầu tác gỉa
> giới thiệu về bài toán tối ưu không có ràng buộc (unconstrained) - tức là
> ko có giới hạn nào đối với các giá trị của variable.
>
> Ông nói rằng, thường thì chúng ta chỉ có thể biết giá trị của function
> (objective function, cái mà chúng ta muốn minimize) và có thể biết thêm
> giá trị của đạo hàm của nó tại một tập các điểm. Chứ ta không biết gì 
> về global perspective (tạm hiểu là góc nhìn toàn cục, khái quát về hành
> vi của hàm số). Tuy nhiên, ta có thể xây dựng những thuật toán để
> có thể chọn ra những điểm sao cho dần dần nó sẽ có thể xác định
> được solution của bài toán một cách đáng tin cậy. Mà quan trọng là
> không tốn quá nhiều thời gian (tính toán) và lưu trữ,
>
> Một điểm nữa là, dù ta có thể có giá trị hàm f, nhưng việc tính toán
> nó không rẻ, nên ta phải làm sao đó dùng ít lần gọi / tính giá trị hàm 
> số thôi (mình có thể hiểu ý này, ví dụ như trong mô hình deep learning,
> việc tính toán forward prop qua mô hình là rất tốn kém khi nó có hàng 
> triệu hoặc hàng tỉ tham số)

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **95/100**
>
> Ghi chú đã nắm bắt chính xác định nghĩa về tối ưu hóa không ràng buộc từ hình ảnh, đặc biệt là ý "không có giới hạn nào đối với các giá trị của variable". Nó còn cung cấp thêm nhiều thông tin chuyên sâu và các khía cạnh thực tế liên quan đến bài toán này, cho thấy sự hiểu biết sâu sắc về chủ đề.

<br>


<a id="node-uw3qu1k"></a>
### Bài toán khớp đường cong

<p align="center"><kbd><img src="assets/img_uw3qu1k.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_hbben.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_pe5zu.png" width="80%"></kbd></p>

> [!NOTE]
> tác giả cho một ví dụ, đại khái là ta sẽ muốn tìm một đường cong sao cho
> nó khớp được một bộ dữ liệu có được từ thực nghiệm. Đại khái là ta có
> các giá trị y1,...ym là giá trị của việc đo một yếu tố nào đó, tại các thời
> điểm t1, t2....tm
>
> Thế thì từ dữ liệu (ý là nhìn vào dữ liệu) và những gì ta biết về loại data
> này, thì ta sẽ đoán (đại khái là vậy) rằng có thể dùng một hàm số như vầy,
> để mô hình hóa
>
> Vậy thì trong hàm số này, x1,..x5 đóng vai trò là parameters và là thứ 
> mà ta muốn tìm giá trị. sao cho với bộ giá trị đó thì hàm Φ(t, x) sẽ khớp
> được sát nhất với bộ data set (t1, y1),...(tn, yn)
>
>
> Thế thì ta mới xây dựng vector x và định nghĩa residual (giống như error):
>
> rj(x) = yj - Φ(tj, x) tức là sai khác giữa giá trị dự đoán của hàm Φ với input
> là tj, dựa trên giá trị của parameters là vector x, với giá trị thực tế đo được
> yj
>
> Để rồi bài toán này, có thể được thể hiện ở dạng unconstrained optimization
> problem:
>
> minimize x Σj [rj(x)]^2 | rj tức là residual yj - Φ(tj, x), và hàm objective này
> là sum of squared error
>
> Bài toán này gọi là nonlinear least square, dễ thấy là vì hàm Φ(tj, x) là hàm
> nonlinear đối với parameters x
>
> Thế thì đại ý là tác giả muốn minh họa rằng bài toán này tuy có ít param
> nhưng vì có rất nhiều data nên để tính toán ra giá trị của objective function
> f = Σj [rj(x)]^2 cũng sẽ rất tốn kém

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **90/100**
>
> Bản tóm tắt và diễn giải rất tốt, đặc biệt là việc liên hệ bài toán với tối ưu hóa không ràng buộc và bình phương nhỏ nhất phi tuyến tính. Cần lưu ý rằng các tham số của mô hình là từ x1 đến x6, không phải x1 đến x5.

<br>


<a id="node-hthgns2"></a>
#### Giải pháp: Toàn cục và Cục bộ

<p align="center"><kbd><img src="assets/img_hthgns2.png" width="80%"></kbd></p>

> [!NOTE]
> đại khái là để mà đi tìm solution của bài toán tối ưu thì ta đầu tiên phải
> định nghĩa solution là gì cái đã.
>
> Thế thì dĩ nhiên là khi đặt ra bài toán tối ưu minimize hàm f(x) over x
> thì dĩ nhiên ta muốn tìm ra global minimizer, tức là tìm trong mọi giá
> trị x của x thì cái nào làm f nhỏ nhất. Định nghĩa chính thức là:
>
> x* gọi là global minimum nếu như f(x*) ≤ f(x) với mọi x.
>
>
> Vấn đề là, (đây là một ý rất hay), ta khó để biết / tìm thấy global minimizer,
> VÌ TA THƯỜNG CHỈ BIẾT VỀ HÀM F Ở PHẠM VI MANG TÍNH CÁCH
> ĐỊA PHƯƠNG, CỤC BỘ.
>
> Đó là vì, thuật toán của chúng ta chỉ xét xét hàm f tại một tập có số lượng
> hữu hạn các điểm khác nhau, vì đại khái là số lượng cũng không nhiều
> (vì lí do như đã nói hồi nãy, việc evaluate giá trị của hàm số là ko rẻ, nên
> phải hạn chế) Thế thì vì vậy, TA KHÔNG THỂ NÀO CHẮC CHẮN RẰNG
> KHÔNG CÓ MỘT CÁI HỐ SÂU, VỰC SÂU NÀO ĐÓ MÀ TRONG QUÁ
> TRÌNH CHẠY THUẬT TOÁN, TA ĐÃ BỎ QUA NHỮNG ĐIỂM TRONG 
> CÁI VỰC NÀY 
>
> (mình hiểu ý này đại khái là giống như ta có thể có vài báo cáo về độ sâu
> đáy biển tại một số điểm, và từ đó cố gắng phác họa, phán đoán bề mặt
> đáy biến, tuy nhiên không thể nào loại trừ khả năng rằng ta đã bỏ xót
> một điểm nào đó mà tại đó có một cái hụp sâu xuống)
>
> Vậy thì, từ đó ta có khái niệm local minimizer, tức là f(x*) chỉ nhỏ hơn những
> f(x) với x trong phạm vi local quanh đó

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **95/100**
>
> Bạn đã nắm vững các khái niệm về cực tiểu toàn cục và cực tiểu địa phương, cũng như lý do tại sao việc tìm cực tiểu toàn cục lại khó khăn, với một ví dụ minh họa rất rõ ràng. Để hoàn thiện hơn, bạn có thể bổ sung định nghĩa hình thức hơn cho cực tiểu địa phương bằng ký hiệu toán học và giải thích ngắn gọn "vùng lân cận" là gì.

<br>


<a id="node-54tf956"></a>
##### Cực tiểu địa phương và toàn cục

<p align="center"><kbd><img src="assets/img_54tf956.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_7p4j2l.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_che8hj.png" width="80%"></kbd></p>

> [!NOTE]
> Tuy nhiên cũng chia ra weak và strong local minimizer:
>
> Dễ hiểu weak là chỉ định nghĩa với dấu ≤, còn strong thì dấu <
>
> Có nghĩa là weak local minimizer thì x* là thằng mà f(x*) không lớn hơn
> những f(x) với x lân cận.
>
> Còn strong local mimizer thì x* là cái mà f(x*) NHỎ HƠN mọi f(x) của x lân
> cận.
>
> Ròi còn khái niệm isolated local minimizer (đơn độc, cô độc) nôm na là khi
> có một tập hàng xóm của x* sao cho chỉ có mỗi  mình x* là local minimizer
>
> Trong hình 2.2 minh họa một tính huống có rất nhiều local  minimizer
>
> Và tác giả cho biết thuật toán rất dễ bị mắc kẹt trong các local minimizer
>
> Và cuối cùng, đôi khi một kiến thức mang tính chất phổ quát nào đó mà ta
> biết về hàm số có thể giúp xác định global minimizer ví dụ như khi ta biết nó
> là hàm lồi (convex) thì khi có local minimizer thì ngay lập tức nó cũng chính
> là global minimizer
>
> (điều này đã biết ở Convex Optimization)

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **95/100**
>
> Bài làm thể hiện sự nắm vững và diễn đạt chính xác các khái niệm quan trọng về local minimizer, strict local minimizer, isolated local minimizer, cũng như vai trò của hàm lồi trong việc xác định global minimizer. Chất lượng công việc là rất cao.

<br>

<a id="node-slr4bzx"></a>
- **Cực tiểu cục bộ: Gradient, Hessian**
<p align="center"><kbd><img src="assets/img_slr4bzx.png" width="80%"></kbd></p>

> [!NOTE]
> đại ý: sau khi đã biết khái niệm local minimizer thì có lẽ ta sẽ nghĩ rằng
> muốn tìm xem một điểm x' có phải là local minimizer không thì ta phải
> check xem giá trị f(x') tại đó có nhỏ hơn mọi f(x) của các điểm x lân cận
> hay không. 
>
> Tuy nhiên, nếu như ta biết hàm có tính chất smooth, thì có thể có cách
> hiệu quả hơn
>
> Cụ thể là khi hàm f liên tục và khả vi kép (tức là tồn tại Hessian - matrix
> đạo hàm bậc 2) tại mọi điểm, thì ta có thể dùng gradient ∇f(x) và Hessian
> ∇^f(x) để giúp xác định xem x có phải là local minimizer không.
>
> Và công cụ toán học để làm nền tảng cho cái này là Taylor's theorem,

> [!TIP]
> **🤖 AI Feedback** — ⚠️ Score: **75/100**
>
> Bản tóm tắt đã nắm bắt được các ý chính của đoạn văn một cách rõ ràng. Tuy nhiên, việc sử dụng ký hiệu ∇^f(x) cho Hessian là không chính xác. Đồng thời, cần diễn đạt chính xác hơn về điều kiện "khả vi kép tại mọi điểm", vì phương pháp này chủ yếu dựa trên tính chất của hàm tại điểm cực trị tiềm năng x* và vùng lân cận của nó.

<br>

<a id="node-zekxi9u"></a>
- **Theorem 2.1 Taylor's theorem, Taylor theorem**
<p align="center"><kbd><img src="assets/img_zekxi9u.png" width="80%"></kbd></p>

> [!NOTE]
> #Theorem 2.1 Taylor's theorem, Taylor theorem
>
> đầu tiên ta có công thức 2.4: 
>
> f(x + p) = f(x) + ∇f(x + tp)Tpvới t ∈ (0, 1). Công thức này ở đâu ra ?
>
> Nhớ lại hồi học mit 1801 mình được học một theorem tên là **Mean Value Theorem**: đại khaí nói là, cho interval [a, b], thì nhất định có điểm c nào đó trong đoạn này (a < c < b) sao cho:
>
> f'(c) = [f(b) - f(a)] / (b - a) 
>
> ⇔ f'(c)(b - a) = f(b) - f(a) ⇔ (b) =(a) + f'(c)(b - a)
>
> Nhìn vào cái này, mình có thể đóan ràng với multivariate case, thì mean value theorem sẽ là, (cho interval [a, b] thì sẽ **tồn tại c nằm trên đoạn [a,b]**
> sao cho:
>
> **f(b) = f(a) + ∇f(c)T(b - a)** (b, a lúc này là vector, và derivative lúc này là gradient  vector)
>
> Vậy nếu gọi a là điểm x, và b = a + p (p = b - a)
>
> thì ta có: f(x + p) = f(x) + ∇f(c)Tp
>
> và vì **c là điểm nằm đâu đó trong đoạn [a, b]**, nên **có thể thể hiện c ở dạng  là mixture** (hay line segment, hay convex combination của a và b): 
>
> **c = αb + (1 - α)a**, với α ∈ (0, 1)để khi α nhỏ thì c ở gần a và khi α lớn thì c chạy
> đến gần b.
>
> Vậy ở đây, người ta dùng t thay cho α: nên c = tb + (1 - t)a = tb + 1 - ta = 1 + t(b-a)
>
> = 1 + tp
>
> Nên ta có (x + p) = f(x) + ∇f(x + tp)Tp là vậy
>
> =====
>
> Tiếp, công thức 2.5 khi họ nói nếu **f twice continuously differentiable** thì ta có:
>
> **∇f(x + p) = ∇f(x) + ∫0:1 ∇^2 f(x + tp)pdt**
>
> Để hiểu cái này có thể thấy nó có dạng của FTC2:
>
> Hồi học mit 1801 đã học FTC2, nói rằng: nếu G là nguyên hàm của f, thì ta sẽ có:
>
> **G(b) - G(a) = ∫_a^b f(t)dt**
>
> **đặt G(t) = ∇f(x + tp)**, 
>
> ⇨ G(0) = ∇f(x), G(1) = ∇f(x + p)
>
> và f(t) = G'(t) = d/dt ∇f(x + tp) = d/d(x + tp) ∇f(x + tp) ∘ d/dt (x + tp)
>
> = ∇^2 f(x + tp) ∘ p
>
> Áp dụng cái này, vì dĩ nhiên G là nguyên hàm của f:
>
> G(1) -  G(0) = ∫_0^1 f(t)dt
>
>  Ta có ∇f(x + p) - ∇f(x) = ∫_0^1 ∇^2 f(x + tp) . p dt
>
> ⇔ ∇f(x + p) = ∇f(x)  + ∫_0^1 ∇^2 f(x + tp) . p dt
>
> =====
>
> Còn cái 2.6: f(x + p) = f(x) + ∇f(x)Tp + (1/2)p ∇^2f(x + tp)p
>
> Đầu tiên phải dùng / nói đến định lý Taylor trước:
>
> f(b) = f(a) + f'(a)(b - a) + (1/2) f''(t)(b - a)^2 + ...+(1/n!) f^(n)(a)(b - a)^n
>
> + (1/(n+1)!)f^(n+1)(c)(b - a)^(n+1)/(n+1)! với c ∈ (a, b)
>
> Cái này thật ra ko có gì khó hiểu: Mình đã quen với Taylor expansion mà đúng hơn là Taylor approximation:
>
> Ví dụ xấp xỉ bậc 1: f(x) ≈ f(x0) + f'(x0)(x-x0)
>
> Và xấp xỉ bậc 2: f(x) ≈ f(x0) + f'(x0)(x-x) + (1/2) f''(x0)(x-x0)^2
>
> Thì đó là ta xấp xỉ. Còn cái này nó sẽ cho phép có dấu bằng, bằng cách nói về / thêm vào một phần dư (gọi là phần dư Lagrange)
>
> f(x) = f(x0) + f'(x0)(x-x0) + (1/2) f''(c)(x-x0)^2 với c nào đó nằm trong (x,x0)
>
> Tương tự,
>
> f(x) = f(x0) + f'(x0)(x-x0) + (1/2) f''(x0)(x-x0)^2 + (1/3!) f^(3)(x)(x-x0)^3  với c nằm trong (x,x0)
>
> Và mean value theorem chính là phiên bản của cái này:
>
> f(x) = f(x0) + f'(c)(x-x0) c ∈ (x,x0)
>
> ====
>
> Vậy thì áp dụng cái này:
>
> Ta sẽ đặt hàm g(t) = f(x + tp) với t ∈ [0,1] 
>
> Để t = 0 thì g(0) = f(x), t = 1, g(1) = f(x + t)
>
> Tức là hàm đơn biến t sẽ mô tả sự thay đổi của hàm số theo hướng x → x + p
>
> Thế thì, áp dụng Taylor theorem với a = 0, b = 1
>
> g(1) = g(0) + g'(0)(1 - 0) + (1/2) g''(t)(1 - 0)^2 với t nào đó ∈ (0,1)
>
> Tính g'(0):
>
> g'(t), tức d/dt g(t) = d/dt f(x + tp) = d/d(x + tp) f(x + tp) . d/dt (x + tp) 
>
> = ∇f(x + tp)Tp
>
> ⇨ g'(t)|t=0 = ∇f(x + tp)Tp|t=0 = ∇f(x)Tp
>
> Tính g''(t):
>
> g''(t) = d/dt g'(t) = d/dt ∇f(x + tp)Tp
>
> d/d(x + tp) ∇f(x + tp)Tp . d/dt (x + tp)
>
> Xét d/d(x + tp) ∇f(x + tp)Tp:
>
> Đặt u = x + tp ⇨ d/du ∇f(u)Tp
>
> đặt h(u) = ∇f(u)Tp ⇨  dh = h(u+du) - h(u)
>
> = ∇f(u+du)Tp - ∇f(u)Tp = [∇f(u+du) - ∇f(u)]Tp = d∇f(u)Tp 
>
> Mà d∇f(u) = ∇^2f(u) du  (vì đạo hàm của hàm ∇f chính là Hessian ∇^2f)
>
> Do đó dh = d ∇f(u)Tp = [∇^2f(u)du]Tp 
>
> = duT ∇^2f(u)T p . Và vì cái này là scalar (u, du là scalar)
>
> = (duT ∇^2f(u)T p)T
>
> = (∇^2f(u)T p)T duTT
>
> = (pT∇^2f(u)TT) du
>
> = pT∇^2f(u) du
>
> Vậy dh(u) = = pT∇^2f(u) du 
>
> ⇨ d/du h(u) = pT∇^2f(u) = pT∇^2f(x + tp)
>
> Vậy d/d(x + tp) ∇f(x + tp)Tp = pT∇^2f(x + tp)
>
> ⇨ d/d(x + tp) ∇f(x + tp)Tp . d/dt (x + tp) = pT∇^2f(x + tp) . d/dt (x + tp) 
>
> = pT∇^2f(x + tp) . p
>
> = pT∇^2f(x + tp)p
>
> Vậy g''(t)  = pT∇^2f(x + tp)p
>
> ⇨ g''(t)|t=ξ = pT∇^2f(x + ξp)p
>
> g(1) = g(0) + g'(0)(1 - 0) + (1/2) g''(ξ)(1-0)^2
>
> Thay vào hết:
>
> g(1) = f(x + p)
>
> g(0) = f(x)
>
> g'(0) = ∇f(x)Tp
>
> g''(t) = pT∇^2f(x + tp)p
>
> Vậy f(x + p)  = f(x) + ∇f(x)Tp + (1/2) pT∇^2f(x + tp)p
>
> Chứng minh xong

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **95/100**
>
> Học sinh đã phân tích cực kỳ chính xác và sâu sắc công thức (2.4) và (2.5) bằng cách liên hệ với các định lý cơ bản trong giải tích. Bài giải thể hiện kiến thức nền tảng vững chắc và khả năng suy luận xuất sắc.

> [!IMPORTANT]
> **🎤 Review Session 1** — Score: **65/100**
>
> Học sinh đã nắm vững mục đích của Định lý Taylor và mối liên hệ của nó với Định lý Giá trị Trung bình một biến, cùng với cách biểu diễn điểm trung gian (X + T * P). Tuy nhiên, bài giải còn thiếu các điều kiện quan trọng của định lý và hoàn toàn bỏ qua việc giải thích công thức 2.5 và 2.6, vốn là một phần đáng kể của tài liệu gốc.

<br>

<a id="node-v0zxbya"></a>
- **Điều kiện cần bậc nhất**
<p align="center"><kbd><img src="assets/img_v0zxbya.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_krorwb.png" width="80%"></kbd></p>

> [!NOTE]
> đại khái là nói rằng **điều kiện cần của optimality** (điều kiện cần để một điểm là
> điểm local minimizer của bài toán tối ưu) sẽ được xây dựng từ việc **giả định
> rằng x là một local minimizer** và **những sự thật đã được chứng minh liên quan
> đến gradient và Hessian**
>
> Vậy thì theorem 2.2 có tên là **First Order Necessary Condition**: nói rằng: **nếu
> x* là local minimizer** và hàm f khả vi liên tục trong một khoảng lân cận của x*
> thì ∇f(x*) phải bằng 0.
>
> Để chứng minh thì đại khái là họ dùng **chứng minh phản chứng**. Ta **giả sử**
> theorem này sai, tức là **cho x* là local minimizer nhưng tại đó gradient vẫn
> khác 0**. Thế thì ta sẽ lập luận để thấy điều này không thể xảy ra, mâu thuẫn
>
> Đầu tiên, vì **x* đang được assume là local minimizer**, nên theo định nghĩa tại
> đó **so với vùng lân cận của x* thì f(x*) phải nhỏ nhất**.
>
> Thế thì ta có **∇f(x*) khác 0** (tức là vector khác 0, ta phải hiểu ∇f(x) là vector,
> gradient, không phải scalar). Thì, bằng cách **chọn một vector p = - ∇f(x*)**, ta sẽ
> có **∇f(x*)Tp = -∇f(x*)T∇f(x*) = -(||∇f(x*)||)^2**
>
> Vậy thì có thể thấy ∇f(x) là vector khác 0 thì dẫn đến ||∇f(x*)||^2 là square
> norm của nó, phải là số dương ⇨ pT ∇f(x*) = -||∇f(x*)||^2 phải **âm**.
>
> Tiếp, ta sẽ xét hàm **g(t) = pT∇f(x* + tp)**, đại ý là thể hiện **giá trị của pT∇f(x)**
> sẽ thay đổi như thế nào **khi đi từ x → x + p**, hay, đi theo hướng vector p
>
> Cái hàm g(t) này, để ý, nó là hàm theo t (scalar), và output cũng là scalar (dot
> product của vector p và vector gradient tại x* + tp
>
> Vậy thì đại khái là, **tại t = 0, ta đã có g(t)|t=0 = pT ∇f(x*) mang giá trị âm vì **.
>
> Mà, **f là hàm liên tục, nên g(t) cũng vậy**. Vậy thì, g(t) là hàm liên tục, mà tại t =
> 0 nó mang giá trị âm. Thế thì, tính liên tục của hàm số nói rằng, khi tăng hay
> giảm t trong một phạm vi lân cận thì hàm số này **nếu có đang tăng lên (để trở
> thành dương) thì nó cũng phải TĂNG TỪ TỪ, để rồi trong khoảng nào đó lân
> cận t thì hàm vẫn mang giá trị âm**. Chứ **không thể nào đùng một phát khi t
> thay đổi mà nó từ âm sang dương** được.
>
> Do đó ta hiểu đại khái chỗ này là như vậy, nên sách nói, **tồn tại T sao cho t
> trong khoảng [0, T] thì g(t) = pT ∇f(x* + tp) vẫn âm**
>
> Còn tại sao lại xét hàm g(t) = pT ∇f(x* + tp) là vì để phục vụ cho việc lập luận
> tiếp với Taylor theorem:
>
> Rồi, tới đây ta áp dụng Taylor theorem ở trên, nói là: 
>
> f(x + p) = f(x) + ∇f(x + tp)Tp với t nào đó ∈ (0,1) 
>
> ⇨ Áp dụng vào đây với t_bar p đóng vai trò của p trong công thức (1) ta có: 
>
> f(x* + t_bar p) = f(x*) + ∇f(x + t t_bar p)T(t_bar p)
>
> vế phải = f(x*) + t_bar ∇f(x + t t_bar p)Tp  for some t in (0,1)
>
> (Đưa scalar t_bar lên trước, vì nó là scalar  nên có thể di chuyển tùy ý)
>
> Tới đây đại khái là, với t và t_bar, thì t là số ∈ (0,1), ⇨ t nhân t_bar sẽ là một
> số nào đó ∈ (0, t_bar), có nghĩa là thay t tbar for some t in (0,1) thành some t
> in (0, tbar)
>
> thay t t_bar bằng t luôn (ý là gom lại dùng một cái để dùng)
>
> f(x* + t_bar p) = f(x*) + t_bar ∇f(x + t p)Tp   | t ∈ (0, t_bar)
>
> Tới đây vì **∇f(x + t p)Tp âm** như trên đã nói, nên có thể kết luận:
>
> f(x* + t_bar p) < f(x*) với mọi t_bar ∈ (0, T]
>
> ⇨ x* không phải là local minimizer. Mâu thuẫn giả thiết.
>
> ====
>
> Tóm tắt ý tưởng đại khái là:
>
> 1) Giả sử ∇f(x*) khác 0 thì  p = - ∇f(x*) thì pT ∇f(x) = -∇f(x*)T ∇f(x*) < 0
>
> Xét g(t) = pT∇f(x* + ptbar) thì nó ẫn âm trong khoảng x* → x* + p tbar nào
> đó, tức là từ tbar = 0 đến tbar = T nào đó.
>
> Mà Taylor theorem nói rằng trong khoảng từ x* → x* + p tbar thì nhất định có
> một điểm c  mà tại đó
>
> f(x* + p tbar) = f(x*) + ∇f(c)Tp với c nào đó in (x*, x* + p tbar)
>
> Tương đương
>
> f(x* + p tbar) = f(x*) + ∇f(x* + t tbar p)Tp với t nào đó in (0,1)
>
> Tương đương
>
> f(x* + ptbar) = f(x*) + ∇f(x* + tp)Tp với t nào đó trong (0, tbar)
>
> và với t này thì ∇f(x* + tp)Tp âm cho nên f(x* + p tbar) < f(x*)
>
> Nên ý nghĩa của cái này là
>
> ù tbar có bằng bao nhiêutrong khoảng từ 0 đến T thì ôn tồn tại một số
> t nằm trong khoảng từ 0 đến tbar ến ta có f(x* + ptbar) = f(x*) +
> somethingmà ý chính là:
>
> ới mọi tbarta ôn được phépf(x* + p tbar) bởi f(x*) +
> something  Và ái something đó âm, suy ra :
>
> ới mọi tbar ∈(0,T), f(x* + p tbar) luôn < f(x*)

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **95/100**
>
> Ghi chú của bạn cực kỳ chi tiết, chính xác và cho thấy sự hiểu biết sâu sắc về cả khái niệm và cấu trúc chứng minh, đặc biệt là giải thích về tính liên tục và định lý Taylor. Bạn có thể cải thiện bằng cách sử dụng ngôn ngữ nhất quán và chính xác hơn một chút ở một vài điểm nhỏ.

<br>

<a id="node-lvmdfpg"></a>
- **Điều kiện cần bậc hai**
<p align="center"><kbd><img src="assets/img_lvmdfpg.png" width="80%"></kbd></p>

> [!NOTE]
> Đại khái là theorem này nói về Second-order Necessary condition: Nếu là  local
> minimizer thì ∇^2f(x) sẽ là positive semi definite matrix (và ∇f(x*) = 0, cái này
> cũng là First order Necessary condition)
>
> Chứng minh Phản chứng, giả sử x* là local minimizer nhưng Hessian tại đó
> không positive semi definite. Mà như vậy thì từ mit 1806 đã biết, sẽ có nghĩa là
> **tồn tại vector p nào đó khiến quadratic form của nó âm pT ∇f(x*) p < 0 **
>
> Tiếp, dựa vào tính liên tục (Hessian là liên tục như đề cho thì g(t) cũng phải là hàm liên tục). Thì ta đặt hàm g(t) = pT ∇f(x* + tp) p thì, phải tồn tại một khoảng (0,T) nào đó sao cho pT ∇f(x* + tp) p vẫn âm. Vì như đã nói, không thể nào hàm g(t) đang âm mà nhảy kịch một phát thành dương ngay khi dịch t một tí được
>
> Thì dựa vào Taylor theorem:
>
> f(x* + p) = f(x*) + ∇f(x*)Tp + (1/2) pT∇^2 f(x + tp)p for some t in (0,1)
>
> Áp dụng vào đây với t_bar p đóng vài trò p, ta có:
>
> f(x* + t_bar p) = f(x*) + ∇f(x*)T t_bar p + (1/2) (t_bar p)T ∇^2 f(x + t t_bar p) t_bar p
>
> = f(x*) + t_bar∇f(x*)Tp + (1/2) (t_bar)^2 pT ∇^2 f(x + t t_bar p) p
>
> với t_bar ∈ (0, T), và some t in (0,1) ⇨ t × t_bar thay bằng some t in (0, t_bar)
>
> = f(x*) + t_bar∇f(x*)Tp + (1/2) (t_bar)^2 pT ∇^2 f(x + t p) p for some t in (0, t_bar)
>
> = f(x*) + (1/2) (t_bar)^2 pT ∇^2f(x + t p) p for some t in (0, t_bar)
>
> (gradient ∇f(x*) = 0)
>
> Và như trên ta có với t ∈ (0,T) thì pT ∇f(x* + tp) p < 0
>
> thì ở đây ta có tồn tại t nào đó trong (0, t_bar) thì ta có cái equation:
>
> f(x* + tbar p) = f(x*) + (1/2) (t_bar)^2 pT ∇^2 f(x + t p) p for some t in (0, t_bar)
>
> Và dĩ nhiên trong khoảng này thì cũng là trong khoảng (0, T)
>
> ⇨ pT ∇^2 f(x + t p) p < 0
>
> ⇨ f(x* + t_bar p) < f(x*) ⇨ ta đã có thể đi thêm theo hướng p để giảm f 
>
> ⇨ x* ko phải là local minimizer. Điều này trái với giả thiết 
>
> ⇨ ∇^2 f(x) phải positive semi definite tại x*
>
> =====
>
> Tóm tắt ý chính cái này chút:
>
> Ta giả sử x* là local minimizer nhưng Hessian tại đó ∇^2 f(x*) không positive
> semi definite. Tức tồn tại p sao cho pT ∇^2 f(x*) p < 0
>
> Theo tính liên tục, thì nếu đặt g(tbar) = pT ∇^2f(x* + ptbar) p thì g(tbar) phải tiếp
> tục âm trong một khoảng nào đó từ x* (tbar = 0) đến x* + p T (tbar = T), nói cách
> khác là tồn tại T nào đó mà từ tbar = 0 đến T, thì g(tbar) = pT ∇^2 f(x* + ptbar) p
> nhất định âm
>
> Thế thì, theo Taylor theorem nói rằng:
>
> Dù tbar có bằng bao nhiêu thì trong khoảng từ x* đến x* + p tbar thì sẽ luôn có
> một thằng t nào đó khiến ta được phép thể hiện f(x* + p tbar) bởi f(x*):
>
> f(x* + p tbar) = f(x*) + ∇f(x*)Tp + (1/2) (p tbar)T∇f^2(x* + t p tbar)(p tbar)
>
> = f(x*) + 0Tp + (1/2) tbar^2 pT∇f^2(x* + t p tbar)p
>
> = f(x*) + (1/2) tbar^2 pT∇f^2(x* + t p tbar)p
>
> Và ý chính của cái này, nhắc lại là với mọi tbar in (0,T) thì ta luôn được phép thể
> hiện f(x* + p tbar) = f(x*) + something.
>
> mà cái something này âm vì pT∇f^2(x* + t p tbar)p với some t in (0,1) thì cũng
> như pT∇f^2(x* + tp)p với some t in (0, tbar) và do đó nó âm
>
> Do đó ⇨ với mọi tbar in (0,T) thì f(x* + p tbar) < f(x*)

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **92/100**
>
> Điểm mạnh của bạn là giải thích rất chi tiết và sâu sắc về từng bước chứng minh, đặc biệt là vai trò của tính liên tục và các bước triển khai chuỗi Taylor. Tuy nhiên, bạn cần cẩn thận hơn về ký hiệu, đôi khi bạn dùng "∇f" thay vì "∇²f" trong biểu thức dạng toàn phương pT (...) p, điều này có thể gây nhầm lẫn.

<br>

<a id="node-4x41639"></a>
- **Chứng minh điều kiện đủ cấp hai**
<p align="center"><kbd><img src="assets/img_4x41639.png" width="80%"></kbd></p>

> [!NOTE]
> Qua cái theorem về điều kiện ĐỦ (của optimality condition): Nó nói rằng, nếu
> ∇^2 f  liên tục trong khoảng lân cận của x* và ∇f(x*)  = 0 và ∇^2 f(x*) positive
> definite Thì x* là **strict local minimizer**
>
> Chứng minh. Đại khái là vì Hessian liên tục và positive definite tại x* nên có thể
> chọn một bán kính r sao cho những điểm trong open ball D = z: ||z - x*|| < r
> đều có Hessian positive definite.
>
> Cần làm rõ để hiểu ý này:
>
> Đại khái là, có thể hiểu vầy cho đơn giản: Gọi hàm λmin(x) là hàm lấy ra
> eigenvalue nhỏ nhất của matrix Hessian tại x: λmin(x) = minimum eigenvalues
> of ∇^2 f(x)
>
> Dĩ nhiên nó là scalar function.
>
> Và vì Hessian liên tục, nên λmin(x) CŨNG LÀ HÀM LIÊN TỤC.
>
> Và dùng lập luận về tính liên tục như cách ta đã lập luận ở trước đây, là:
>
> Nếu tại x* λmin(x*) DƯƠNG (*), thì khi thay đổi từ x* → x (ý là di chuyển qua
> điểm khác thì giá trị của nó phải thay đổi từ từ, có nghĩa là trong một khoảng
> nào đó mà khoảng này có nghĩa là một vòng tròn (quả banh) trong đó λmin(x)
> vẫn tiếp tục dương
>
> Và như vậy, có nghĩa là tại những điểm này Hessian tiếp tục positive definite
>
> Còn (*) tại x* λmin(x*) dương là vì đề bài đã cho Hessian tại đó positive definite.
>
> Và kiến thức mit 1806 thì mình đã biết matrix positive definite thì mọi eigenvalue
> đều  dương ⇨ cái nhỏ nhất phải dương

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **98/100**
>
> Bài ghi rất chính xác về định lý và chứng minh. Đặc biệt, phần làm rõ bằng cách sử dụng hàm eigenvalue nhỏ nhất và tính liên tục là rất sâu sắc, giúp người đọc hiểu rõ bản chất của điều kiện đủ.

<br>

<a id="node-e5vd9lq"></a>
- **Chứng minh điều kiện đủ bậc hai**
<p align="center"><kbd><img src="assets/img_e5vd9lq.png" width="80%"></kbd></p>

> [!NOTE]
> Và phần chứng minh tiếp theo cũng dễ hiểu thôi khi ta đã biết Taylor theorem:
>
> Đại ý là, ta đứng từ x*, và đi theo hướng p bất kì với độ lớn nhỏ hơn r (ý là không
> ra khỏi vòng tròn / quả banh này)
>
> Thì Taylor theorem nói rằng:
>
> f(x* + p) = f(x*) + ∇f(x*)Tp + (1/2) pT ∇^2 f(z) p với z là điểm nào đó nằm giữa 
> x* và x* + p, tức khoảng (x*, x* + p), cũng có thể ghi là z = x* + pt với t là giá trị
> nào đó trong (0,1).
>
> Với ∇f(x*) = 0 ta có f(x* + p) = f(x*) + (1/2) pT ∇^2 f(z) p  với z = x* + pt với some 
> t ∈ (0,1).
>
> Và có nghĩa là f(x* + p) có thể được thể hiện bởi f(x*) + something mà something
> này, là bằng (1/2) pT ∇^2 f(z) p sẽ DƯƠNG vì z vẫn trong quả banh nói trên có
> mọi điểm trong đó đều có Hessian positive definite
>
> Vậy, f(x* + p) = f(x*) + số dương ⇨ f(x* + p) > f(x*) với mọi p sao cho ||p|| < r
> và như vậy x* thỏa định nghĩa là điểm "thấp" hơn mọi điểm lân cận (f(x*) < f(x)
> ∀ x lân cận) ⇨ x* là strict local minimizer

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **100/100**
>
> Ghi chú này cực kỳ rõ ràng và chính xác, giải thích chi tiết từng bước của chứng minh bằng định lý Taylor. Nó làm sâu sắc thêm sự hiểu biết bằng cách kết nối các phép toán với định nghĩa và các điều kiện đã cho.

> [!IMPORTANT]
> **🎤 Review Session 1** — Score: **45/100**
>
> Bạn đã giải thích rất chi tiết và chính xác về lý do tồn tại một vùng lân cận quanh x* mà tại đó Hessian vẫn xác định dương, thể hiện sự hiểu biết sâu sắc về tính liên tục của hàm số và giá trị riêng của ma trận. Tuy nhiên, bạn đã bỏ qua hoàn toàn phần cốt lõi của chứng minh liên quan đến việc áp dụng định lý Taylor và suy luận f(x* + p) > f(x*), đây là điểm thiếu sót nghiêm trọng trong việc tái hiện toàn bộ chứng minh.

> [!IMPORTANT]
> **🎤 Review Session 2** — Score: **85/100**
>
> Học sinh đã trình bày rất tốt các bước chứng minh và giải thích vai trò của định lý Taylor cũng như các điều kiện của bài toán. Tuy nhiên, có một chi tiết quan trọng về dấu bất đẳng thức ở bước kết luận cuối cùng cần được làm rõ hơn để phản ánh đúng tính "strict" của local minimizer.

<br>

<a id="node-qb85dvq"></a>
- **Cực tiểu: cần, đủ, chặt**
<p align="center"><kbd><img src="assets/img_qb85dvq.png" width="80%"></kbd></p>

> [!NOTE]
> Giải lú ba cái theorem trên:
>
> Đầu tiên: Nhớ lại điều kiện cần và đủ là sao:
>
> Điều kiện cần: Tức là ⇨ , ở đây là:
>
> [x* là local minimizer] ⇨ thì sao?
>
> Vậy ở đây điều kiện cần bậc 1 là:
>
> [x* là local minizer ] ⇨ thì gradient tại đó vanish ∇f(x*) = 0
>
> Điều kiện cần bậc 2:
>
> [x* là local minizer ] ⇨ thì Hessian tại đó xác định bán dương ∇^2 f(x*) ≻ 0
>
> Còn điều kiện đủ: Tức là ⇐: 
>
> [thì x* là local minimizer] ⇐ điều kiện đủ
>
> Vậy ở đây điều kiện đủ bậc 2 nói là:
>
> [thì x* là STRICT local minimizer] ⇐ Hessian tại x* xác định dương và
> gradient = 0
>
> Vậy ở đây người ta nói rằng Cái điều kiện đủ bậc 2 không phải là điều kiện
> cần, thì ý là ta ko có dấu ngược lại
>
> [thì x* là STRICT local minimizer] ⇨  Hessian tại x* xác định dương và
> gradient = 0
>
> Vậy tóm lại:
>
> Nếu x* là local minimizer ⇨ gradient vanish, Hessian xác định bán dương
>
> Nếu gradien vanish, Hessian xác định dương ⇨ x* là strict local minimizer
>
> Chỉ vậy thôi, chứ ta ko có chiều ngược lại ví dụ như:
>
> gradient vanish, Hessian xác định bán dương → (SAI) x* là local minimizer
>
> hay
>
> x* là strict local minimizer → (SAI) gradien vanish, Hessian xác định dương

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **95/100**
>
> Phân tích rất rõ ràng và chính xác, làm sáng tỏ các khái niệm điều kiện cần và đủ liên quan đến nội dung trong ảnh. Để hoàn hảo hơn, có thể lưu ý sử dụng ký hiệu chuẩn cho ma trận Hessian xác định bán dương (ví dụ ≽ 0) để tránh nhầm lẫn với xác định dương.

<br>

<a id="node-9dw0mi9"></a>
- **Hàm lồi: Local minimizer là global**
<p align="center"><kbd><img src="assets/img_9dw0mi9.png" width="80%"></kbd></p>

> [!NOTE]
> Ta gặp lại theorem này (gặp bên EE364A): Khi hàm lồi thì local minimizer cũng trở thành global minimizer.
>
> Mình tóm tắt phần chứng minh ở đây trước, có vẻ cũng rất dễ hiểu:
>
> Ta sẽ giả sử hàm f convex, x* là local minimizer nhưng không phải là global minimizer (và ta sẽ chứng minh nó vô lí). Vì ko phải là global minimizer nên tồn tại z nào đó "thấp" hơn nó f(z) < f(x*). Khi đó ta xét line segment (đoạn thẳng nối x*, z, tập convex combination của x*, và z: x: x = λz + (1 - λ)x* với 0 < λ < 1.  
>
> Ta mới dùng tính chất của hàm lồi (cũng đã gặp ở ee365):
>
> f(x) ≤ λf(z) + (1 - λ)f(x*)
>
> mà f(z) < f(x*) như giả thiết 
>
> ⇨ f(x) ≤ λf(z) + (1 - λ)f(x*) ≤ λf(x*) + (1 - λ)f(x*) = f(x*)
>
> Tức f(x) ≤ f(x*), hay x sẽ nằm thấp hơn x*
>
> Thế thì đại khái ta sẽ lập luận là dù cho z ở đâu thì để đi từ x đến z ta đều phải đi qua một các điểm x thuộc line segment như này và do đó chắc chắn có điểm nằm trong vùng lân cận neighborhood N của x*.
>
> Và mọi điểm trong line segment này đều "thấp hơn" x*, nên chắc chắn phải có điểm trong lân cận N của x* thấp hơn nó. ⇨ điều này chứng tỏ x* ko phải là local optimizer Mâu thuẫn giả thiết ⇨ x* phải là global minimizer
>
> ====
>
> Thầy Boyd có cách chứng minh cũng hay: Dựa vào tính non negative curvature
>
> Đại khái cũng giả sử x* là local minimizer nhưng không global. Tồn tại z thấp hơn nó: 
> Vậy thì để đi từ x* đến z, vì x* là local minimizer nên kiểu như khi đi ra khỏi x* trong phạm vi lân cận thì đều phải là "đi lên", nhưng sau đó để tới z nằm thấp hơn x* thì phải là đi xuống, có nghĩa là phải có lúc nào đó hàm số phải "cong xuống", mà điều này
> vi phạm tính chất non-negative curvature của hàm lồi

<br>

<a id="node-iqziy0r"></a>
- **Điểm dừng và tối ưu toàn cục**
<p align="center"><kbd><img src="assets/img_iqziy0r.png" width="80%"></kbd></p>

> [!NOTE]
> Để chứng minh phần sau ta cũng phản chứng, giả sử x* là stationary point mà x* ko phải global minimizer ⇨ tồn tại z thấp hơn.
>
> ∇f(x*)T(z - x*) = d/dλ f(x* + λ(z - x*)) | λ = 0 là sao?
>
> có thể thấy vế trái, chính là directional derivative đối với vector d = z - x* (chỉ 
> hướng từ x* → z) và evaluate tại x* ta đã biết công thức là ∇f(x*)Td 
>
> Nếu đặt g(λ) = f(x* + λ(z - x*)) thì g là hàm đơn biến thể hiện giá trị của f 
> trên hướng vector d, khi λ = 0, g(0) = f(x*), λ = 1, g(1) = f(z). Và đạo hàm
> của g tại λ = 0 cũng chính là ∇f(x*)Td
>
> (vì bản chất định nghĩa của directional derivative đối với hướng d):
>
> lim δ→0 [f(x + δ) - f(x)] / δ)
>
> và dòng tiếp theo cũng chính là viện dẫn định nghĩa này:
>
> .. = lim λ→0 [f(x* + λ (z - x*)) - f(x*)] / λ  
>
> Tới đây mới dùng tính chất hàm convex:
>
> f(x* + λ(z - x*)) = f(x* + λz - λ x*) = f((1 - λ)x* + λz)
>
> và cái này thì theo convexity ≤ (1 - λ) f(x*) + λ f(z)
>
> ⇨ [f(x* + λ (z - x*)) - f(x*)] / λ  ≤ [(1 - λ) f(x*) + λ f(z) - f(x*)] / λ  
>
> và vế phải = [f(x*) - λf(x*)  + λ f(z) - f(x*)] / λ = - f(x*) + f(z)
>
> Nên ta có lim λ → 0 [f(x* + λ (z - x*)) - f(x*)] / λ  ≤ lim λ → 0 - f(x*) + f(z) 
>
> = f(z) - f(x*) 
>
> và đây là con số âm do f(z) < f(x*)
>
> ⇨ ∇f(x*)T(z - x*) < 0 điều này chứng tỏ ∇f(x*) khác vector 0 ⇨ x* không phải
> stationary point
>
> Và giáo sư nhận xét: Như mọi thuật toán đều tìm kiếm điểm gradient
> vanish

<br>

<a id="node-n5yeozz"></a>
- **Minimizer hàm không trơn**
<p align="center"><kbd><img src="assets/img_n5yeozz.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_au9mg.png" width="80%"></kbd></p>

> [!NOTE]
> đại khái là dù sách này tập trung vào smooth function, và non-smooth function thường là KHÔNG THỂ TÌM MINIMIZER ĐƯỢC, nhưng nếu hàm f smooth từng phần trên từng đoạn, và chỉ bị discontinuous tại giữa các đoạn, khi đó ta vẫn có cách để tìm minimizer, bằng cách ta sẽ minimizing từng đoạn
>
> Nhưng nói chung là gs chỉ nói sơ vậy thôi đề nghị đọc sách khác

<br>

