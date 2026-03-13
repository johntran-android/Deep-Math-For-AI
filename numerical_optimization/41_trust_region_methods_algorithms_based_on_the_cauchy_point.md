# 4.1 Trust-Region Methods: Algorithms Based on the Cauchy Point

📊 **Progress:** `11` Notes | `17` Screenshots | `9` AI Reviews

---
> [!NOTE]
> Trust-Region Methods: Algorithms Based on the Cauchy Point


<a id="node-2vr465x"></a>
## The Cauchy Points

<p align="center"><kbd><img src="assets/img_2vr465x.png" width="80%"></kbd></p>

> [!NOTE]
> Đại ý tác giả nói là cũng giống như trong chapter trước (về line searcg), mình đã thấy rằng, ngay cả khi việc chọn step size không phải là optimal (như việc ta không cần giải bài toán exact line search - minimize hàm g(t) = f(xk + tpk)), mà chỉ cần chọn step size đủ tốt (thông qua việc thỏa các điều kiện dừng) thì ta vẫn có thể có hội tụ toàn cục (global convergence).
>
> Thì ở đây tương tự, đó là ta cũng không cần phải tìm pk là solution tuyệt đối của bài toán minimize mk(p) s.t ||p|| ≤ Δ. thay vào đó chỉ cần pk đủ tốt, ý là giúp giảm hàm f đủ tốt (sufficient reduction). Và mức giảm đủ tốt này có thể được thể hiện bởi Cauchy points. 
>
> Để tìm nó cần 2 bước:
>
> Đầu tiên tìm pk_s = argmin fk + gkTp s.t ||p|| ≤ Δk, ý nghĩa của cái này có thể hiểu nôm na là: Nếu coi như đi từ xk → xk + p hàm f ứng xử như hàm tuyến tính thì trong phạm vi cho phép đi tới đâu là thấp nhất.
>
> Sau đó, nếu xét trong cái hướng pk_s, và vẫn trong phạm vi cho phép, thì ở đâu giúp mk thấp nhất.
>
> Mình hình dung vầy: Việc xác định pk_s, giống như là, mình vẽ cái mặt phẳng tiếp tuyến với đồ thị hàm f tại xk, độ dốc của nó (gradient của nó) tại xk = gradient ∇fk. Rồi, rõ ràng mặt phẳng này, với việc ta giới hạn phạm vi trong bán kính Δ, giống như hàng rào bao quanh thì câu chuyển là ta đi trong mặt phẳng này tới đâu trong phạm vi hàng rào để xuống thấp nhất, Khi đó ta xá định được pks và dễ thấy nó phải là điểm chạm vào hàng rào. 
>
> Rồi, tiếp theo thì về cơ bản là ta giới hạn hàm mk theo phương pks, để giải bài toán minimize hàm đơn biến mk(τpks) s.t ||τpks|| ≤ Δ.
>
> Khi đó ta sẽ có pkc = τkpks

> [!TIP]
> **🤖 AI Feedback** — ⚠️ Score: **85/100**
>
> Học sinh thể hiện sự hiểu biết sâu sắc về điểm Cauchy và mối liên hệ với phương pháp tìm kiếm đường và vùng tin cậy. Tuy nhiên, cần chú ý hơn đến tính chính xác trong định nghĩa cuối cùng.

<br>


<a id="node-e8hacdf"></a>
### Close formed solutin pls

<p align="center"><kbd><img src="assets/img_e8hacdf.png" width="80%"></kbd></p>

> [!NOTE]
> Ở đây tác giả nói bài toán 1 tìm pks có thể có closed form solution như vầy, cùng thử xem tại sao:
>
> Bài toán là minimize fk + gkTp s.t ||p|| ≤ Δk
>
> ≡ (equivalent) minimize gkTp s.t ||p|| ≤ Δk
>
> -||gk|| ||p|| ≤ gkTp = ||gk|| ||p|| cos(θ) ≤ ||gk|| ||p|| (công thức tích vô hướng, và tính chất hàm cosine)
>
> Vậy ta có gkTp ≥ -||gk|| ||p|| 
>
> Dùng constraint ||p|| ≤ Δ ⇔ -||p|| ≥ - Δ ⇔ -||gk|| ||p||  ≥ -||gk|| Δ
>
> ⇨ gkTp ≥ -||gk|| ||p||  ≥ -||gk|| Δ
>
> Vậy solution của bài toán là p sao cho gkTp = -||gk|| Δ ⇔ ||gk|| ||p|| cos θ = -||gk|| Δ
>
> ⇔ cos theta = -1, và ||p|| = Δ
>
> tức là p = -(gk Δ)/ ||gk||, hay (- Δ / ||gk||) gk

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **95/100**
>
> Bản giải thích này rất rõ ràng và chính xác, chứng minh được công thức cho điểm Cauchy một cách đầy đủ. Để bài làm hoàn hảo hơn, bạn nên thêm tên gọi chính thức của bài toán này ngay từ đầu.

<br>


<a id="node-06f2kv1"></a>
#### Công thức Cauchy point

<p align="center"><kbd><img src="assets/img_06f2kv1.png" width="80%"></kbd></p>

> [!NOTE]
> Rồi, qua bài toán sau: minimize mk(τ) = fk + gT(τp) + (1/2)(τp)TBk(τp) 
>
> Với p là pks = - (Δk / ||gk||) gk, g là gradient của f tại xk
>
> Thì lập luận là, ta sẽ xét 2 trường hợp:
>
> gkTBkgk ≤ 0: Thì (τp)TBk(τp) = τ^2 pTBkp = τ^2 (Δk / ||gk||)^2 gkTBkgk cũng sẽ ≤ 0 ∀ τ
>
> mk(τ) = fk + τ gkT [-(Δk / ||gk||) gk] + (1/2) τ^2 (Δk / ||gk||)^2 gkTBkgk
>
> = fk - τ gkTgk [(Δk / ||gk||)] + (1/2) τ^2 (Δk / ||gk||)^2 gkTBkgk
>
> = fk - ||gk|| Δk τ + (1/2) τ^2 (Δk / ||gk||)^2 gkTBkgk
>
> Xét đạo hàm theo τ của hàm g(τ) = mk(τpks):
>
> g'(τ) = (Δk / ||gk||)^2 gkTBkgk τ - ||gk|| Δk thì có thể thấy với mọi τ ≥ 0 thì cái này đều luôn âm ⇨ hàm monotone decreasing. ⇨ Hàm luôn giảm nên bài toán minimize sẽ có solution tại boundary: Tức τ là giá trị khiến τ||pks|| = Δ ⇔ τΔ = Δ ⇔ τ = 1
>
> ====
>
> Xét trường hợp 2: gkBkgk > 0:
>
> giải g'(τ) = 0:
>
> ⇔ (Δk / ||gk||)^2 gkTBkgk τ - ||gk|| Δk = 0
>
> ⇔ (Δk / ||gk||)^2 gkTBkgk τ = ||gk|| Δk 
>
> ⇔ [Δk^2 / (||gk||)^2] gkTBkgk τ = ||gk||Δk
>
> ⇔ τ = (||gk||)^3 / ΔkgkTBkgk
>
> g''(τ ) = (Δk / ||gk||)^2 gkTBkgk, và nó sẽ luôn > 0. 
>
> Nên nếu thỏa constraint, tức ||τ*pks|| ≤ Δk
>
> ⇔ (||gk||)^3 / ΔkgkTBkgk Δk ≤ Δk
>
> ⇔ (||gk||)^3 / ΔkgkTBkgk ≤ 1 thì minimizer là (||gk||)^3 / ΔkgkTBkgk
>
> Ngược lại, thì minimize sẽ = 1 vì hàm số chỉ có một cực tiểu, và lúc này nó nằm ngoài biên, nên trong phạm vi cho phép thì tại biên nó thấp nhất
>
> Nên kết luận τk = min(1,  (||gk||)^3 / ΔkgkTBkgk)
>
> Vậy tổng hợp hai case: τk = 1 nếu gkTBkgk ≤ 0 và min(1,  (||gk||)^3 / ΔkgkTBkgk) otherwise.

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **95/100**
>
> Bài làm thể hiện sự hiểu biết sâu sắc và khả năng phân tích xuất sắc đối với bài toán. Các bước đạo hàm và lập luận cho từng trường hợp đều chính xác và đầy đủ. Chỉ một điểm nhỏ cần lưu ý là cách giải thích từ τ||pks|| = Δ để suy ra τ=1 có thể chính xác hơn, nhưng điều này không ảnh hưởng đến kết quả cuối cùng.

<br>


<a id="node-42j2ybl"></a>
##### Bước Cauchy và hội tụ

<p align="center"><kbd><img src="assets/img_42j2ybl.png" width="80%"></kbd></p>

> [!NOTE]
> Hình ảnh này minh họa tình huống mà pkC nằm trong bán kính.
>
> Nói chung tác giả cho rằng việc tính toán Cauchy step không tốn nhiều chi phí, vì quá trình hoàn toàn không cần phải factor matrix.
>
> Vì sao nhỉ, có thể thấy là vì công thức chỉ là tính norm của gk, và gkTBkgk, mà tính cái này thì cơ bản chỉ là nhân matrix với vector. Không phải tính nghịch đảo hay giải hệ phương trình (ví dụ như tìm nghịch đảothì ta sẽ phải phân rã
>
> Và ý chính là, nếu pk giúp tạo ra một mức giảm ít nhất là bằng một con số dương nào đó nhân với mức giảm của Cauchy step thì thuật toán chắc chắn sẽ hội tụ toàn cục.
>
> Mình nghĩ: Nhớ lại, ở trên đã nói, tương tự như bên line search, khi step size có thể không cần tối ưu, mà chỉ cần đủ tốt, bằng cách thỏa điều kiện dừng, là sẽ đảm bảo hội tụ toàn cục thì ở đây cũng tương tự, chỉ cần pk giúp giảm đủ tốt (bằng cách so

<br>

<a id="node-ix5cl2z"></a>
- **Improving on the Cauchy Points**
<p align="center"><kbd><img src="assets/img_ix5cl2z.png" width="80%"></kbd></p>

> [!NOTE]
> Đại khái đoạn này nói là: **Ta có thể thắc mắc rằng**, **nếu như việc tính toán Cauchy step rẻ như vậy**, và như đã nói nếu **pk có thể tạo ra mức giảm đủ tốt dựa theo Cauchy step** thì **sao ta không dùng luôn Cauchy step**, mà phải đi tìm một solution tốt hơn (why we should look any further for a better approximate solution of 4.3)
>
> Thì đại ý là vì một điều tương tự như trong **chap 3 mình đã thấy phân tích hội tụ của steepest descent cho thấy nó rất kém**, ngay cả khi dùng step length tối ưu (mà mình nhớ hình ảnh là nó sẽ nhảy qua nhảy lại giữa hai vách núi, do nó luôn chọn hướng vuông góc với contour, nên nếu optimization landscape giống một thung lũng hẹp thì nó sẽ nhảy qua nhảy lại liên tục)
>
> Và đại khái là **Cauchy point, mình nhớ, bước tính pkS, tức là chọn hướng, về cơ bản chính là đi theo steepest descent direction**. Chính là ý mà tác giả nói, **Bk, vốn là có thể chứa thông tin curvature giúp xác định hướng tốt hơn** (giống như Hessian, giúp chọn Newton step tốt hơn là steepest descent direction vậy) **thì lại không tham gia vào việc tính pkS**. Mà nó **chỉ tham gia vào bước xác định step size**. Xem lại là hiểu.
>
> Do đó, tác giả nói, **có vài trust region method sẽ làm theo cách là tính Cauchy point trước, sau đó cải thiện thêm**. Và **cách thức có thể là bằng cách lôi Bk vào bước tính direction**. Cụ thể là nếu Bk xác định dương là thì nó sẽ tính pkB = - Bkinvgk.
>
> (Chỗ này chưa rõ lắm, pkB là để dùng luôn cho pk hay là sao)
>
> Thế thì phần sau ta sẽ học những phương pháp giúp tìm approximation solution của 4.3.
>
> Ôn lại chút chỗ này: 4.3 là bài toán này:
>
> minimize fk + gkTp + (1/2)pTBkp s.t ||p|| ≤ Δk
>
> Thì đại khái là ta **có thể không cần giải chính xác solution**. Mà chỉ cần approx solution thôi, dựa trên yêu cầu là nó đủ tốt (so sánh bởi / với Cauchy step).
>
> Thì những phần tiếp sẽ nói về cách giải các approx solution của bài toán này.

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **90/100**
>
> Bài làm cho thấy sự nắm bắt vững chắc các khái niệm cốt lõi của việc cải thiện điểm Cauchy và hiểu biết sâu sắc về vai trò của ma trận $B_k$. Tuy nhiên, còn một điểm nhỏ cần làm rõ hơn về chiến lược tích hợp các bước cải tiến.

<br>

<a id="node-pf675m8"></a>
- **The Dogleg method**
<p align="center"><kbd><img src="assets/img_pf675m8.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_d6msru.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_lelpfh.png" width="80%"></kbd></p>

> [!NOTE]
> Đại khái là vầy: Phương pháp này nó sẽ làm như sau:
>
> Đầu tiên mình **xét bài toán minimize m(p) = f + gTp + (1/2)pTBp không constraint**, thì dễ thấy **solution của nó chính là -(B)inv g**
>
> (**giống như công thức Newton step** khi B là Hessian vậy).
>
> Và ta có thể **coi như đây là solution của bài toán có constraint ||p|| ≤ Δ có điều cho Δ rất lớn**. Nên mình **ghi p*(Δ) = - Binv g** thể hiện là nó sẽ là giá trị này nếu Δ rất lớn, nên nó **cũng phụ thuộc Δ**.
>
> Tương tự, **nếu Δ rất nhỏ, thì solution của bài toán này với constraint ||p|| ≤ Δ cũng sẽ có norm rất nhỏ**. 
>
> Mà **khi đó thì m(p) = f + gTp + (1/2)pTBp sẽ ≈ m(p) = f + gTp**. 
>
> Do đó ta **dùng solution của bài toán minimize k(p) = f + gTp s.t ||p|| ≤ Δ để coi như (approx) cho solution của bài toán minimize m(p) = f + gTp + (1/2)pTBp s.t ||p|| ≤ Δ**.
>
> Mà **solution của bài toán minimize k(p) thì cơ bản chính là pkS mà ta biết trong phần định nghĩa của Cauchy points**. Nên nó là = -(Δ/||g||) g
>
> Và do đó với Δ nhỏ thì solution của bài toán minimize mk s.t ||p|| ≤ Δ, p*(Δ) sẽ ≈ -(Δ/||g||) g. Đó là lí do có dấu approx. (Vì ta chỉ mượn solution của bài toán xấp xỉ, minimize k(p), chứ m(p) phải có cái quadratic term)
>
> Vậy thì đại ý là thế này: Ta thấy Δ mà lớn thì p*(Δ) nó khác mà Δ nhỏ thì nó khác. Do đó đại ý là khi Δ tăng từ nhỏ đến lớn thì p*(Δ) sẽ thay đổi từ từ, để **TẠO NÊN MỘT QUỸ ĐẠO (TRAJECTORY)** là cái đường cong cong trong hình.
>
> Vậy thì giờ mới nói về dogleg method: Nó sẽ làm vầy: Đại khái là nó sẽ **dùng một cái quỹ đạo tạm hiểu là xấp xỉ cái đường cong đó**, tạo bởi 2 phần, tạo thành hình chân chó. pU và pB.
>
> Trong đó pU là solution của bài toán **minimize f + gTp + (1/2)pTBp**
> nhưng **RESTRICT TO HƯỚNG STEEPEST: -g**. 
>
> Hay nói cách khác, thì pU là solution của bài toán: 
>
> minimize g(t) = m(tp)|p=-g = f + gT(-gt) + (1/2)(-gt)TB(-gt) 
>
> = f - t||g||^2 + (1/2) t^2 gTBg. 
>
> Đây là **hàm đơn biến bậc hai theo t**. Dễ thấy solution của bài toán này là:
>
> g'(t) = 0 ⇔ - ||g||^2 + 2t gTBg = 0 ⇔ t = ||g||^2 / gTBg
>
> ⇨ pU chính là  ||g||^2 / gTBg (-g) = - [||g||^2 / gTB] g chính là công thức 4.15 trong sách.
>
> Rồi, còn pB thì dễ rồi, nó là -Binv g (cũng là cái p*(Δ) với Δ rất lớn (coi như unconstrain ở trên)
>
> Vậy thì cái chân chó sẽ là: đi từ điểm xuất phát xk đến xk + pU, và từ xk + pU đến xk + pB.
>
> Nên thể hiện như sau: 
>
> p(τ) = τ × pU với τ từ 0 tới 1.
>
> và = pU + (τ - 1)(pB - pU) với τ từ 1 tới 2.
>
> Và **phương pháp dogleg sẽ chọn p để mininize model m theo đường đi này, ràng buộc là trust-region bound**. Và cái bổ đề kế tiếp sẽ cho thấy việc tìm solution của bài toán này có thể dễ.
>
> Vậy thì dừng lại một chút, để nhớ lại bối cảnh hiện tại. Ta đang trong phần improveing on the Cauchy point, mà vấn đề đặt ra là, Cauchy point đại khái là tạo ra mức giảm đủ tốt, vậy tại sao ta không dùng luôn Cauchy point. Thì nguyên nhân là, trong Cauchy point, thì phần direction pkS chính là nó lấy steepest descent direction, và sau đó mới tìm step size theo hướng đó sao cho trong phạm vi cho phép, đi xuống thấp nhất. Vậy thì vì nó chọn hướng theo steepest descent, nên nó sẽ bị cái nhược điểm của phương pháp này mà ta đã phân tích ở chương trước. Cụ thể là vì nó không dùng thông tin curvature, nên dù là cái hướng steepest, nhưng nhiều khi lại là hướng tệ, khiến hội tụ chậm.
>
> Do đó, sắp tới ta mới bàn về các các thức để CẢI THIỆN CAUCHY POINT. Mà dogleg vừa nói trên chính là cách đầu tiên. Và nó làm theo kiểu đã phân tích, tức là, nó sẽ chọn ra một quỹ đạo, mà cái quỹ đạo này bắt chước, xấp xỉ cái quỹ đạo của p* khi phạm vi cho phép từ rất nhỏ đến rất lớn. Nói dễ hiểu hơn: khi nới lỏng trust region từ rất nhỏ đến rất lớn thì p* sẽ thay đổi từ theo hướng steepest descent trở thành hướng Newton. để rồi nó tạo ra một cái quỹ đạo như hình chân chó. Thế thì bằng cách minimize m(p) theo quỹ đạo xấp xỉ cái quỹ đạo chân chó này này ta sẽ thấy nó tạo ra tác dụng là: 
>
> Nếu như trust region nhỏ, thì p* sẽ là hướng steepest (vì khúc đầu của đường gấp khúc chính là steepest descent, khi Δ nhỏ thì cơ bản ta chỉ minimize hàm m(p) trong hướng này)
>
> Còn nếu trust region lớn, thì p* sẽ có thể dần lai lai về hướng Newton, chứ không bị giới hạn chỉ được đi theo hướng steepest không thôi (vì khi Δ mở rộng, nó sẽ chứa đoạn thứ hai của đường gấp khúc, cho phép việc minimize m(p) có thể tìm thấy p gần với hướng Newton hơn)

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **95/100**
>
> Bài phân tích rất sâu sắc và chính xác, đặc biệt là phần dẫn giải chi tiết cách tìm pU và giải thích mối liên hệ cũng như ưu điểm của phương pháp dogleg so với Cauchy point. Tuy nhiên, cần lưu ý cách diễn đạt rằng p*(Δ) 'phụ thuộc Δ' khi Δ rất lớn, vì trong trường hợp này, p*(Δ) thực chất là hằng số pB khi Δ đủ lớn, không biến đổi theo Δ.

<br>

<a id="node-68pwgig"></a>
- **Bổ đề 4.2**
<p align="center"><kbd><img src="assets/img_68pwgig.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_c9yd2.png" width="80%"></kbd></p>

> [!NOTE]
> Rồi, bổ đề này đại ý là, cho B xác định dương, thì i) ||p_tilde(τ)|| là hàm tăng theo τ ii) m(p_tilde(τ)) là hàm giảm theo τ.
>
> Để chứng minh thì tác giả cho là rất dễ khi xét τ ∈ [0,1]. Thử xem sao mà dễ.
>
> Đầu tiên nhắc lại, p_tilde(τ) là = τpU khi τ ∈ [0, 1] và pB + (τ - 1)(pB - pU) khi τ ∈ [1, 2]
>
> với pU = - [gTg / gTBg] g
>
> Vậy thì khi τ ∈ [0, 1], p_tilde(τ) = τpU, ⇨ ||p_tilde(τ)|| = |τ| ||pU|| = τ ||pU||. Để xét xem có phải là hàm tăng không thì xét d/dt ||p_tilde(τ)|| thôi, dễ thấy nó sẽ bằng ||pU||, là không âm → hàm non-dereasing / increasing hoặc nếu giả sử g khác 0, thì cái này còn dương → hàm strictly increasing.
>
> Còn m(p_tilde(τ)): 
>
> = f + gTp_tilde(τ) + (1/2)p_tilde(τ)TBp_tilde(τ)
>
> = f + gTτpU + (1/2)[τpU]TBτpU
>
> = f + τgTpU + (1/2)(τ^2)pUTBpU
>
> Xét đạo hàm theo τ: dễ thấy = gTpU + pUTBpU τ 
>
> = gT {- [gTg / gTBg] g} + {- [gTg / gTBg] g}T B {- [gTg / gTBg] g} τ
>
> = - [gTg / gTBg] gTg + [gTg / gTBg]^2 gTBg τ
>
> = - (gTg)^2 / (gTBg) + [(gTg)^2 / (gTBg)] τ
>
> = (gTg)^2(-1 + τ) / (gTBg)
>
> Với τ ∈ [0,1] thì -1 + τ ∈ [-1, 0] nên cái này ≤ 0 → m decreasing function of τ
>
> ====
>
> Đoạn chứng minh với τ ∈ [1,2]
>
> Thay p_tilde(τ) với τ ∈ [1,2] bởi p_tilde(1+α) với α ∈ [0,1].
>
> ⇨ ||p_tilde(τ)|| = theo công thức nhắc lại khi nãy, = ||pB + (τ - 1)(pB - pU)|| 
>
> = ||pB + α(pB - pU)||
>
> Ta mới đặt hàm h(α) = (1/2) ||p_tilde(1 + α)||^2:
>
> h'(α) = d/dα [(1/2) ||p_tilde(1 + α)||^2] 
>
> = d/d(||p_tilde(1 + α)||) [(1/2) ||p_tilde(1 + α)||^2] . d/dα ||p_tilde(1 + α)|| 
>
> = ||p_tilde(1 + α)|| . d/dα ||p_tilde(1 + α)||
>
> Nếu ta chứng minh h'(α) ≥ 0 với mọi α ∈ [0,1] thì đồng nghĩa ||p_tilde(1 + α)|| . d/dα ||p_tilde(1 + α)|| ≥ 0 ∀ α ∈ [0,1], ⇔ d/dα ||p_tilde(1 + α)|| ≥ 0 ∀ α ∈ [0,1], ⇨ p_tilde(1 + α) là increasing function of α trên ∈ [0,1], cũng chính là chứng minh xong ý i).
>
> (Chú ý, ở đây, thay vì đạo hàm hàm ||p_tilde(1 + α)|| (là hàm cần chứng minh increasing) ta sẽ dễ hơn nếu làm với hàm (1/2) ||p_tilde(1 + α)||^2 theo lí do trên, vì đạo hàm hàm này dễ hơn nhiều)
>
> Quay lại h(α), = (1/2) ||p_tilde(1 + α)||^2
>
> = (1/2) ||pU + α(pB - pU)||^2
>
> = (1/2) (pU + α(pB - pU))T(pU + α(pB - pU)
>
> = (1/2) (pUT + α(pB - pU)T)(pU + α(pB - pU)
>
> = (1/2) [pUTpU + α(pB - pU)TpU + pUTα(pB - pU) + α(pB - pU)Tα(pB - pU)]
>
> = (1/2) [pUTpU + 2α(pB - pU)TpU + α^2 (pB - pU)T(pB - pU)]
>
> = (1/2) ||pU|| + α(pB - pU)TpU + (1/2) α^2 ||pB - pU||^2
>
> h'(α) = (pB - pU)TpU + α ||pB - pU||^2
>
> vì α ||pB - pU||^2 ≥ 0 
>
> ⇨ h'(α) ≥ (pB - pU)TpU, hay -pUT(pU - pB) cho giống sách cũng được.
>
> Thay vô:
>
> .. ≥ -[- [gTg / gTBg] g]T([- [gTg / gTBg] g] - pB)
>
> = [gTg / gTBg] gT([- [gTg / gTBg] g] - (-Binv g))
>
> = [gTg / gTBg] gT([- [gTg / gTBg] g] + Binv g)
>
> ... Khúc cuối do dùng bdt Cauchy và ý ii) quay lại sau

> [!TIP]
> **🤖 AI Feedback** — ❌ Score: **35/100**
>
> Bài làm chứng minh được tính chất cho τ ∈ [0,1] một cách chính xác dựa trên các giả định bên ngoài. Tuy nhiên, bài phân tích này đã bỏ qua hoàn toàn nội dung chứng minh trọng tâm của ảnh (đạo hàm h'(α) cho τ ∈ [1,2]), vốn là phần khó và chi tiết nhất trong ảnh.

<br>

<p align="center"><kbd><img src="assets/img_h1c2dgh.png" width="80%"></kbd></p>

> [!NOTE]
> Rồi, nhắc lại tí cho đỡ quên context, bổ đề vừa rồi cho biết hàm norm của p_tilde(τ), tức τpU khi τ ∈ [0,1] và pU + (τ - 1)(pB - pU) khi τ ∈ [1,2] là increasing function theo τ, và mk(p_tilde(τ)) là hàm decreasing function. Mà ý nghĩa của nó, nôm na là:
>
> KHI TA ĐI TRÊN QUỸ ĐẠO HÌNH GẤP KHÚC thì độ lớn của p_tilde(τ) luôn tăng và hàm m luôn giảm.
>
> Cụ thể thì ||p_tilde(τ)|| sẽ tăng liên tục từ 0, đến ||pU|| (khi τ từ 0 → 1), và từ ||pU|| đến ||pB|| khi τ từ 1 → 2. Và vì nó tăng liên tục, nên dĩ nhiên là nếu ||pB|| mà lớn hơn Δ, thì sẽ **chỉ có một lần** nó vượt qua giá trị Δ, chính là ý nói rằng cái đường gấp khúc này chỉ cắt tại một điểm. Nhưng nếu ||pB|| nhỏ hơn Δ, cũng chính là khi cái đáy của cái bát quadratic nằm bên trong phạm vi trust region, thì dĩ nhiên sẽ không có intersection.
>
> Rồi, vì ý thứ hai của bổ đề nói m giảm liên tục trên đường gấp khúc, nên khi ta tìm điểm trên đó khiến m nhỏ nhất trong phạm vi cho phép, thì dễ hiểu là nếu minimizer nằm trong phạm vi cho phép thì không nói có gì để nói, chứ nếu nằm ngoài thì minimizer chính là giao điểm của đường gấp khúc với boundary.
>
> Do đó trong trường hợp sau, ta sẽ giải phương trình này để tìm giao điểm 
> (tức là tìm τ mà tại đó quỹ đạo gấp khúc cắt boundary, cũng là τ minimizer m(p_tilde(τ)) subject to ||p_tilde(τ)|| ≤ Δ.
>
> ||pU + (τ - 1)(pB - pU)||^2 = Δ^2

> [!TIP]
> **🤖 AI Feedback** — ✅ Score: **90/100**
>
> Bài phân tích rất chi tiết và chính xác, không chỉ tóm tắt mà còn mở rộng và giải thích rõ ràng các khái niệm nền tảng của phương pháp dogleg, đặc biệt là hành vi của chuẩn vector và hàm mục tiêu. Cách diễn giải về điều kiện giao điểm và lựa chọn điểm tối ưu rất logic và thể hiện sự nắm vững kiến thức.

<br>

<p align="center"><kbd><img src="assets/img_6w87m5s.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_4gcwb.png" width="80%"></kbd></p>

> [!NOTE]
> Đại khái là nói về B trong bài toán minimize f + gTp + (1/2)pTBp s.t ||p|| ≤ Δ, thì như đã biết B có thể là Hessian, hay xấp xỉ Hessian. Thì ở đây là nói lại ý đó, cụ thể là nếu trong tình huống mà ta có Hessian avaiable (dĩ nhiên đây là Hessian tại điểm bắt đầu, xk, vì đây thật ra viết đầy đủ là bài toán minimize f(xk) + gkTpk + (1/2)pkTBkpk s.t ||pk|| ≤ Δ, giúp tìm pk gíúp giảm đủ), và available có nghĩa là có thể tính được hay có được mà không quá tốn kém, vì thật ra nguyên nhân chủ yếu của việc không có Hessian là vì chi phí tính toán, thì ta sẽ dùng B = Hessian, tức ∇^2f(xk).
>
> Khi đó cái mà ta có từ phương pháp dogleg gọi là **Newton-doglog step**.
>
> Mặc khác, tức là nếu như exact Hessian không available hoặc Hessian không xác định dương thì ta có thể dùng các matrix Hessian chỉnh sửa (modified Hessian) mà chương trước đã nói (ôn nhanh, đại khái là có các cách thức trong đó ta chỉnh sửa Hessian để cho nó thành xác định dương)
>
> Đoạn sau đại khái nói thế này: Việc dùng modified Hessian trong phương pháp dogleg thật ra không phù hợp lắm bởi vì việc chỉnh sửa Hessian mà ta còn nhớ nó sẽ thay đổi đường chéo của Hessian để giúp nó thành xác định dương, thì việc này xảy ra có tính chất tùy tiện (arbitrary), và lợi ích của phương pháp trust-region có thể không được nhận ra một cách đầy đủ.
>
> Cụ thể là ở phần sau ta sẽ thấy đại ý là khi tính solution của bài toán trên với Bk là Hessian, thì solution nó là (∇^2f(xk) + λI)inv gk trong đó λ được chọn sao cho (∇^2f(xk) + λI) xác định dương rồi, có nghĩa là, bản thân phương pháp trust region thì có thể coi như nó cũng đã thực hiện cái việc chỉnh sửa Hessian rồi, khiến việc chỉnh sửa bởi các thuật toán modified Hessian không cần thiết (redundant)
>
> Rồi, tác giả kết luận Newton-dogleg method sẽ phù hợp với tình huống mà objective function convex (khi đó như đã biết từ Convex Optim Boyd, Hessian luôn xác định bán dương).
>
> Còn trong các trường hợp khác, thì ta sẽ dùng technique khác.

> [!TIP]
> **🤖 AI Feedback** — ❌ Score: **65/100**
>
> Bài phân tích đã nắm bắt được một số ý chính nhưng còn bỏ sót các điều kiện quan trọng về tính xác định dương của ma trận Hessian và kết luận cuối cùng về trường hợp áp dụng phù hợp nhất của phương pháp Newton-dogleg. Sự thiếu sót các chi tiết cốt lõi này cho thấy sự chưa thấu đáo trong việc nắm bắt toàn bộ nội dung.

<br>

<a id="node-nk72thi"></a>
- **Two-dimensional Subspace Minimization**
<p align="center"><kbd><img src="assets/img_nk72thi.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_81232d.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_3xxtdp.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_acwngs.png" width="80%"></kbd></p>

> [!NOTE]
> Đoạn đầu đại ý là: Nói rằng khi B xác định dương, thì ta có thể LÀM CHO PHƯƠNG PHÁP DOGLEG PHỨC TẠP HƠN TÍ, bằng cách mở rộng không gian tìm kiếm chút xíu. Nói rõ hơn, đại khái là vầy: Để hiểu rõ ngọn ngành thì ta cần ôn lại chút về ý tưởng của dogleg method: Mục đích ngắn gọn của nó là CẢI THIỆN CAUCHY POINT. Là sao? 
>
> Là vầy, tác giả đã nói, tương tự như bên line search, ta có thể không cần thiết phải tốn công đi tìm exact (optimal) step length, mà chỉ cần step length đủ tốt, như thỏa Wolfe / Strong Wolfe conditions là được, vì như vậy cũng đủ giúp hội tụ toàn cục rồi. Thì ở đây cũng vậy, ta cũng chỉ cần pk (hay bỏ qua subscript k) p, giúp giảm đủ là được.Thì cái sự đủ ở đây chính là đối chiếu / lấy tấm gương của Cauchy point. Và Cauchy point, là p được tính bởi 2 bước: Tìm pkS là hướng steepest descent, và giải tìm pU = tpkS: minimize hàm m(p) (= f + gTp + (1/2)pTBp) nhưng restrict to hướng pkS (minimize g + gTpkS × t + (1/2)pkSTBpkS × t^2 và ||pkS t|| ≤ Δ)
>
> Thế thì, vấn đề là, cái hướng của Cauchy point, là steepest gradient descent, mà ta đã biết, nó hội tụ rất tệ, vì nó không dùng thông tin curvature (chứa trong Bk, tức B). Thành ra người ta mới tìm cách cải thiện Cauchy point, mà đầu tiên là dogleg: Họ sẽ lập luận thế này: khi Δ thay đổi từ rất nhỏ đến rất lớn, thì solution của bài toán minimize m(p) s.t ||p|| ≤ Δ sẽ thay đổi từ pU đến pB, tạo ra một quỹ đạo hình cẳng chó. Vậy thì dogleg method mới định ra một đường gấp khúc xấp xỉ cái cẳng chó đó, và minimize hàm m(p) s.t ||p|| ≤ Δ restrict to cái đường gấp khúc này.
>
> Vậy thì, quay lại đây, ta sẽ thấy việc vừa nói, chính là tìm kiếm trong một 1D subspace (đường gấp khúc). Thì có khi cái điểm tốt nhất lại nằm ngoài cái đường đó. Lí do là vì ta đang dùng cái cây gậy gấp khúc để xấp xỉ cái đường chân chó chứ không phải là cái quỹ đạo chân chó thật sự, nên điểm tốt nhất có thể không nằm trên cây gậy, mà nằm ở ngoài. Do đó người ta mới mở rộng phạm vi tìm kiếm ra thành subspace span bởi pU và pB, thì cũng là span bởi g và Binvg (vì đã nói pU chính là hướng pkS, tức là hướng steepest descent → -g.
>
> Chỉ vậy thôi, và tác giả nói bài toán này cũng không quá expensive.
>
> Một điểm nữa, đó là Cauchy point dĩ nhiên nằm trong subspace này, nên ý là bài toán mở rộng này ít nhất là tìm ra điểm ngon hơn hoặc bằng Cauchy point, nên sẽ đảm bảo giảm đủ để hội tụ toàn cục.
>
> ====
>
> Rồi, đoạn tiếp theo là nói rằng phương pháp này có thể MỞ RỘNG ĐỂ DEAL VỚI TÌNH HUỐNG MÀ B INDEFINITE. Vậy phải chú ý rằng phương pháp trên chỉ áp dụng với B xác định dương, rõ ràng, là bởi khi B xác định dương thì pB mới là descent direction:
>
> Ta nhớ lại chỗ này: Đạo hàm theo hướng d tại xk: ∇f(xk)Td, hay gTd (xem link Điểm dừng và tối ưu hóa..) ⇨ đạo hàm theo hướng (-Binv g, chú ý nhé, pU = - Binv g, còn span thì dùng Binv g cũng được vì cũng là cùng một phương như nhau) tại xk: - gT Binv g. Và với việc B không xác định dương thì gT Binv g chưa chắc là luôn dương ⇨ - gT Binv g chưa chắc là luôn âm. Mà directional theo hướng d = -Binv g tại xk chưa chắc luôn âm thì có nghĩa là d chưa chắc là descent direction.
>
> Rồi, thế thì đại ý là, nếu như B indefinite, để rồi pB = -Binv g không chắc là descent direction, thì việc tìm kiếm trong span [g, Binv g] có thể sẽ cho ra kết quả không tốt. Do đó người ta sẽ thay span [g, Binv g] bởi span [g, (B + αI)inv g] với α đâu đó từ (-λ1 tới -2λ1] và λ1 là **trị riêng âm nhất** của B. Mục đích là, dễ thấy B + αI sẽ không còn trị riêng âm nữa → ma trận trở thành xác định dương (chú ý cái khoảng của α là (-λ1 tới -2λ1], nên chắc chắn trị riêng của B + αI đều dương). Còn sở dĩ giới hạn bởi -2λ1 thì hiểu đại khái là để không trị riêng không quá lớn (có thể là yếu tố kinh nghiệm, hoặc vì lí do nào đó, ở đây tác giả chỉ nói sơ (salient point), khuyên ta đọc paper của Byrd, Schnabel,....)
>
> Và cũng vì lí do nào đó, mà khi ||(B + αI)inv g|| ≤ Δ, ta sẽ bỏ vụ tìm kiếm trong subspace đi, thay nó bằng p = -(B + αI)inv g + v với v thỏa vT(B + αI)inv g ≤ 0 .
>
> Rồi khi B có trị riêng 0, và ko có trị riêng âm (tức là B xác định dương) thì cho p = pC (cauchy point)
>
> Nói chung là để hiểu cặn kẽ ta có thể phải đọc paper. Tạm thời bỏ qua khúc này.
>
> ====
>
> Cái đoạn áp chót, nói khi exact Hessian available thì ta có thể cho B = Hessian và khi Hessian xác định dương thì bài và  Δ đủ lớn thì bài toán subspace minimization có thể được giải bởi Newton step là sao nhỉ: Thì đơn giản là vì khi đó Newton step - Hinv g thỏa constraint ||p|| ≤ Δ, nó cũng nằm trong span [g, Hinv g] (dĩ nhiên) và đương nhiên ta biết nó sẽ minimize f + gTp + (1/2)pTHp, nên nó là solution chứ sao. 
>
> ====
>
> Nói chung là tác giả nói, cách làm này (2D subspace minimization) giúp đem đến một mức giảm hàm f gần bằng với mức giảm tạo bởi EXACT SOLUTION nhưng tốt ít chi phí tính toán hơn (vì chỉ tốn 1 bước factorizatizion matrix B hoặc B + αI thay vì 2 hoặc 3)

> [!TIP]
> **🤖 AI Feedback** — ⚠️ Score: **82/100**
>
> Bản ghi chú của bạn thể hiện sự hiểu biết sâu sắc về các khái niệm, đặc biệt là trong việc đặt ngữ cảnh cho phương pháp dogleg và điểm Cauchy. Tuy nhiên, có một lỗi đáng kể trong việc diễn giải điều kiện cho vector 'v' khi 'B' là không xác định, điều này cần được chỉnh sửa để đảm bảo tính chính xác hoàn toàn.

<br>

