# 7.1 (continue from StudyBoard notebooks)

📊 **Progress:** `4` Notes | `7` Screenshots

---
<a id="node-2"></a>

<p align="center"><kbd><img src="assets/531feb622f57c86c0e18f33eab1dd952442ae644.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/531feb622f57c86c0e18f33eab1dd952442ae644.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1cb644826a3dff805de45c3bf0bf0927ad973f60.png" width="100%"></kbd></p>

> [!NOTE]
> Có lẽ nên ôn lại chút xíu về Trust Region Newton CG:
>
> Cơ bản chỉ là ta xét bài toán Trust Region Newton, và dùng CG để giải
> sub-problem:
>
> TRN là ám chỉ trong bài toán sub-problem, ta sẽ dùng Newton direction  cho
> pk.
>
> Và việc dùng CG để giải sub-problem chính là dùng thuật toán CG giúp tìm
> pkN bằng cách giải hệ ∇^2fk pkN = - ∇fk, theo cách iteratively: nói ngắn gọn
> như sau
>
> Ôn nhanh CG cũng như thuật toán 5.2:
>
> Mục đích giải: Ax = b, A xác định dương, ta sẽ coi đây là giải điều kiện cần
> bậc một của bài toán tối ưu hàm số nguyên hàm của Ax - b, tức là hàm f(x) =
> (1/2)xTAx -bTx. Thuật toán đại khái là như sau: Ban đầu ta có x0, và cần đi
> đến x* để thỏa Ax* - b = 0. Chọn p0 = - ∇f(x0) = -Ax0 + b. Thực hiện
> iteratively:
>
> Tính αk, với thuật toán CG, đại khái đây chỉ là giải bài toán minimize hàm
> bậc hai đơn biến, có closed form solution. Thực hiện update tới xk+1 = xk +
> αkpk. Tính pk+1: chính là conjugate wrt A của pk. Ideas chỉ là vậy thôi.
>
> Vậy thì ở đây, cái dễ lú lẫn là kí hiệu.
>
> Vì bài toán cần giải là subproblem: tìm Newton step cho bài toán subproblem
> của thuật toán trust region:
>
> Nói sơ về thuật toán Trust Region:
>
> Cũng là ta sẽ minimize hàm f(x) iteratively
>
> Tại mỗi iteration, thứ k'th ta sẽ giải bài toán subproblem:
>
> Coi hàm f(x) tại k hoạt động như hàm bậc hai: mk(p). Và cùng với trust
> region Δk đã xác định ở iteration trước, ta muốn giải bài toán:
>
> minimize mk(p) = fk + ∇fkTp + (1/2)pT Bk p subject to ||p|| ≤ Δk
>
> (vì đây là Trust Region Newton nên Bk chính là ∇^2fk)
>
> Thế thì, để giải bài toán subproblem, dĩ nhiên ta cũng giải theo lối iterative
> với hai phương pháp đã học trong chap 5: Dogleg và 2D subspace
> minimization. Đều mục đích là tìm ra pk là minimizer của mk(p) s.t ||p|| ≤ Δk.
> thì CG chính là cách thứ
> 3.
>
> Và áp dụng nó vào để giải bài toán subproblem, ta sẽ làm như sau:
>
> Vì thuật toán CG vốn dĩ là giải hệ Ax = b, hay Ax - b = 0. Bằng cách tạo
> chuỗi {xj} đi từ x0 → x1 → ...→ x* sao cho dần dần giảm ||x* - xj|| Nhưng ở
> đây, nó lại phải có constraint. Tức là ta cần giải hệ Bk p = - ∇fk nhưng với
> constraint ||p|| ≤ Δk,
>
> Vấn đề phải hiểu thế này. Việc giải bài toán subproblem là minimize mk(p) s.
> t ||p|| ≤ Δk, về cơ bản đây là bài toán minimize hàm quadratic có inequality
> constraint, ta sẽ thiết lập stationary condition: Gradient của hàm Lagrangian
> = 0, chứ đâu phải là gradient là mk = 0 đâu, có nghĩa là đâu phải là điều kiện
> cần là Ax = b đâu mà lôi CG ra.
>
> Tuy nhiên, cũng chính vì vậy mà mới gọi là modified CG, chỉ lấy cách làm
> của CG, nhưng ko hoàn toàn giống:
>
> Ta sẽ giả sử là không có ràng buộc, và giải hệ Bk p = - ∇fk,
>
> p* đóng vai x*, nên ta sẽ kí hiệu dj, zj đóng vai pk, xj của CG gốc:
>
> Cho z0 = 0, d0 = steepest descent: - (Bk * z0 - ∇fk) = ∇fk
>
> tính α1, cũng là giải bài toán minimize hàm quadratic đơn biến.
>
> tính z1 = z0 + α1d0,
>
> tính d1, là conjugate gradient với d0,
>
> ...
>
> lặp lại, tiếp tục.
>
> Trong quá trình này sẽ đi qua chốt chặn:
>
> zj+1 (= zj + αjdj) (nhớ!: zj ứng với xj của CG gốc, và là thứ sẽ gán cho p để
> trả ra) có khiến ||zj+1|| lớn hơn Δk chưa? → Nếu có thì dừng.
>
> Lúc này, ta mới cơ bản là VẪN LẤY HƯỚNG dj, nhưng khống chế độ dài
> của nó dj) sao cho ||zj+1||= ||zj + τdj|| KHÔNG QUÁ HÀNG RÀO. (gọi là giải
> bài toán minimize zj + τdj). Nó khác với việc ta cứ tính zj+1 = zj + dj rồi cắt
> cụt để norm zj+1 = Δk
>
> (sau đó trust region sẽ đo độ uy tín các kiểu để có quyết định nhảy tới
> không, có tăng / giảm / giữ nguyên trust region không. Chú ý, trust region ko
> có tìm step size gì đâu nhé line search mới tìm step size)
>
> Chốt chặn thứ hai, thật ra sẽ nằm trên chốt chặn thứ nhất: là xem Bk có bị
> xác định âm hay không xác định không, bằng cách check d0Bkd0 ≤ 0. Khi
> đó, đại khái là ta tìm theo hướng d0, như đã biết, chính là steepest descent
> của mk tại điểm ban đầu, sao cho chạm hàng rào. (Thì cái này, chính là
> Cauchy point)
>
> Nếu mọi thứ đều ổn, không bị thoát ở hai cái chốt trên. Và điều kiện dừng
> cuối cùng, tức là z cuối (z*) ko vi phạm ||z*|| ≤ Δk. Thì mình nên hiểu là đó
> cũng ko phải là Newton step. Vì ta sẽ chỉ có Newton step nếu chạy hết n
> iteration để có được p* là solution của Bk p* = - ∇fk. Nhưng người ta sẽ
> không làm vậy, nên dù cho không bị chặn ở hai cái chốt đầu, thì cái ta có
> cũng chỉ là inexact Newton step.
>
> Huống hồ, khả năng là ta sẽ bị chặn ở một trong hai chốt trên. Khi đó, nếu là
> ở chốt thứ nhất: zj+1, ví dụ j = 20, ta có z21, có norm dài hơn Δk, ta sẽ tìm τ
> sao cho ||z20 + τd20|| = Δk (khác với việc ta cắt cụt z21 để ||z21|| = Δk)
>
> Còn nếu nếu bị chặn ở chốt thứ hai: d0Bkd0 ≤ 0. Thì như đã nói trên, đây
> chính là Cauchy point
>
> Ôn nhanh Cauchy point là gì, trong CG gốc: Nó là vầy: Tại x0, lấy hướng
> steepest decent: chính là Ax0-b, và giải bài toán minimize hàm bậc hai đơn
> biến (hàm 1/2xTAx - bTx) nhưng restrict  theo hướng steepest descent và có
> constraint và giải tìm minimizer của nó. Khi đó ta sẽ có hai case, đụng hàng
> rào hoặc nằm trong.
>
> Vấn đề dễ lú là: Trong CG gốc, cái ta giải là Ax - b = 0. và coi như nó là giải
> bài toán minimizer hàm số F(x) = (1/2)xTAx - bTx, mà ∇F(x) = 0 ⇔ Ax - b = 0
> chính là điều kiện cần bậc 1. vài CG giúp giải cái này từ từ. Thành ra nói
> steepest descet tại x0, chính là -∇F(x0) = -Ax0 + b.
>
> Còn trong việc dùng CG giải subproblem. Thì thứ cần giải là Bk p = - ∇fk,
> hay Bk x = - ∇fk. Và cũng chẳng cần phải xem Bk p + ∇fk là gradient của
> hàm nào F nào. Vì F chính là mk(p), là hàm xấp xỉ bậc hai của objective
> function f(x) nguyên thủy. Do đó, chọn d0 là steepest descent direction, thì
> nó chính là -Bkz0 + (-∇fk) = -Bk z0 - ∇fk. Và do chọn z0 = 0, nên là -∇fk.

> [!NOTE]
> Vậy thì quay lại đây, tác giả cho biết một tính chất quan trọng của phương
> pháp này là mỗi iterate **norm zj LUÔN LỚN HƠN cái trước đó zj-1**.
> ({zj},  thứ sẽ converge về z* để gán cho pk (giải Bk pk = - ∇fk), tương ứng
> trong  thuật toán CG  gốc là {xj} converge về x* (giải Ax* = b).
>
> Vậy thì đoạn này đại khái nói là, tính chất này đảm bảo rằng, M**ỘT KHI
> MÀ TA ĐỤNG TRUST REGION**, thì có thể dừng, vì **có iterate thêm thì
> cũng không thể giảm thêm mk trong phạm vi trust region nữa**.
>
> Là sao ta?
>
> Như vừa nói ở note trước, khi giải bài toán subproblem bằng CG, ta cơ
> bản là **dùng CG để giải tìm Newton direction theo lối iteratively**. Mà về
> bản  chất là ta **tìm ra một hướng đi trong vùng tin cậy** sao cho **hướng
> đi đó đủ tốt (inexact Newton step)**. Khi thuật toán chạy cái **giảm dần ở
> trong lúc chạy** CG **norm của error giữa p* với zj** (và cũng là norm giữa
> mk tại p* và mk tại zj).
>
> (Trong thuật toán CG gốc, bản chất là ta minimize hàm quadratic nguyên
> hàm của F(x) = (1/2)xTAx - bTx, nguyên hàm của Ax - b, và mục tiêu là
> giảm  dần ||x* - xj|| cũng là chính là |F(x*) - F(x)| mà trong CG trong
> subproblem  thì zj chính là tương đương với xj)
>
> Thì cái việc **norm zj liên tục lớn dần**, cái sau lớn hơn cái trước  chính là
> ý là **norm của xj cũng lớn dần** trong thuật toán CG gốc, cái sau lớn hơn
> cái trước.
>
> Nhưng trong bối cảnh CG gốc thì ko có ý nghĩa gì đáng nói, nhưng ở đây
> khi  đặt trong bối cảnh có hàng rào bao quanh thì nó có ý nghĩa. Vì điều
> này có nghĩa là **khi chuỗi zj được tạo ra thì mk(j) ngày càng giảm**
> nhưng đồng thời ta cũng **ĐI XA DẦN VỊ TRÍ BAN ĐẦU**: z0 = 0 (tức là
> ngay tại xk). Và do đó, chứng tỏ, nếu đã đụng hàng rào, thì đó là điểm
> giúp đưa mk xuống thấp nhất có thể trong phạm vi cho phép rồi. HÌnh
> dung quỹ đạo là **đường xoắn ốc giảm dần và rộng ra dần**, **thì khi đụng
> biên thì đó là thấp nhất trong phạm vi** cho phép. Đây chính là ý gs
> Nocedal đang nói.

<br>

<a id="node-3"></a>

<p align="center"><kbd><img src="assets/91da0929c1fd572145b8e9ff8546d9a03d0e0031.png" width="100%"></kbd></p>

<br>

<a id="node-4"></a>

<p align="center"><kbd><img src="assets/a67c5f72dada657ee3c888caa48c37afe0ce49a2.png" width="100%"></kbd></p>

> [!NOTE]
> Theorem 7.3 nói rằng chuỗi {zj}} được sinh ra bởi thuật toán 7.2 sẽ
> luôn thỏa cái sau lớn hơn cái trước về norm.
>
> Phần chứng minh đại ý là vầy:
>
> Đầu tiên trong 7.3, việc cập nhật {zj} theo công thức: zj+1 = zj + αjdj
>
> (Ôn nhanh: d0 là hướng steepest descent, d1, d2... sau đó hướng 
> conjugate wrt matrix Bk với d trước đó. Có dj rồi thì giải bài toán 
> minimize hàm bậc hai đơn biến, là hàm mk restrict theo hướng dj 
> để tìm step size αj)
>
> Thế thì: ||zj+1|| = ||zj + αjdj||
>
> ⇨ ||zj+1||^2 = ||zj + αjdj||^2 = (zj + αjdj)T(zj + αjdj)
>
> = (zjT + αjdjT)(zj + αjdj)
>
> = zjTzj + αjdjTzj + zjTαjdj + αjdjTαjdj
>
> = ||zj||^2 + 2αjdjTzj + αj^2||dj||^2
>
> Đến đây, nếu ta chứng minh được djTzj > 0 thì sẽ chứng minh
> được ||zj+1|| > ||zj|| (1)
>
> Và ta sẽ chứng minh bằng quy nạp: Chứng minh nó đúng với k = 1,
> rồi giả sử đúng với k = j, và chứng ninh nó đúng luôn với k = j+1 thì 
> sẽ có thể kết luận nó đúng với mọi k.
>
> Nhưng trước hết tác giả chứng minh một kết quả để lát sau sẽ dùng:
> đó là zjTrj = 0. Cái này dễ thôi:
>
> Theo công thức update {zj}:
>
> z1 = z0 + α0d0, z2 = z1 + α1d1,....zj = zj-1 + αj-1dj-1
>
> ⇨ thay vào liên tục, ta có: zj = z0 + Σi=0:j-1 αidi
>
> = Σi=0:j-1 αidi (vì theo thuật toán 7.2, z0 được initialized = 0. 
>
> Ta có zj = Σi=0:j-1 αidi, nhân hai vế với rjT:
>
> rjTzj = rjTΣi=0:j-1 αidi = Σi=0:j-1 αi rjTdi
>
> Tới đây, mới xem lại Theorem 5.2, nói nói đại khái là residual tại
> vòng sau, thì luôn vuông góc với mọi direction trước đó (trong thuật
> toán CG gốc, ta sẽ có rkTpi với i = 0,1,...k-1): Cho nên ở đây, ta sẽ
> có rj vuông góc với d0,d1,...dj-1. Nên cái bên phải = 0 ⇨ rjTzj = 0
>
> ------ 
> Quay lại đây, chứng minh quy nạp nói ở trên:
>
> Xét k = 1, d1Tz1 có > 0 không? (z0 = 0 rồi nên ta sẽ chứng minh từ
> k = 1)
>
> d1Tz1 = d1T(z0 + α1d1) = d1Tα1d1 = α1 ||d1||^2 cái này > 0, vì sao?
> vì α1 là step-size, luôn dương (vì sao luôn dương, vì α1 là stepsize tìm
> được bằng cách tối thiểu hóa hàm bậc hai đơn biến mk giới hạn bởi
> d1, mà d1. hay dj luôn là descent direction (nếu ko, tưc djTBkdj ≤ thì 
> thuật toán đã return ở chốt đầu rồi, nên đã qua được chốt đó thì tức là
> djTBkdj > 0. Nên αj = rjTrj / djTBkdj sẽ dương do tử và mẫu dương.
>
> Tiếp, gỉa sử nó đúng với k = j: djTzj > 0
>
> Ta sẽ chứng minh nó đúng với k = j+1: dj+1Tzj+1 > 0
>
> dj+1Tzj+1 = (-rj+1 + βj+1dj)Tzj+1
>
> = -rj+1Tzj+1 + βj+1djTzj+1
>
> = 0 + βj+1djTzj+1 (do đã chứng minh rjTzj = 0, và nó cũng đúng với j+1)
>
> = βj+1 djT(zj + αjdj)
>
> = βj+1djTzj + βj+1djTαjdj
>
> = βj+1djTzj + βj+1αj ||dj||^2
>
> Mà ta đã giả sử djTzj > 0 ⇨ βj+1djTzj > 0 (vì βj+1 = rj+1Trj+1 / rjTrj > 0)
>
> và βj+1αj ||dj||^2 cũng dương nốt.
>
> Vậy chứng minh xong là djTzj > 0 với mọi j ⇨ theo (1), ta đã chứng
> minh xong.

<br>

<a id="node-5"></a>

<p align="center"><kbd><img src="assets/690e87456da5eadf392f7d8427412612f5f4efe4.png" width="100%"></kbd></p>

> [!NOTE]
> Ok, nhớ lại về thuật toán Dogleg:
>
> Ideas của nó là như sau:
>
> Nó muốn cải thiện Cauchy points. Cauchy point's story: Đi từ điểm đầu tiên
> x0, theo hướng dốc nhất, ráng đưa mk(p) (giới hạn theo hướng đó) xuống
> thấp nhất trong phạm vi hàng rào. Nó có thể dừng ở trong, hoặc đụng hàng
> rào (Bk xác định âm: đi theo hướng đó sẽ giảm mk vô hạn → đụng hàng
> rào, Bk xác định dương: có thể dừng ở trong hoặc ngoài (đụng hàng rào))
>
> Và ta đã biết vụ Cauchy points là bước nhảy mang lại mức giảm đủ tốt, giúp
> đảm bảo hội tụ toàn cục, đóng vai trò tham chiếu cho các phương pháp
> khác phải  ít nhất là bằng cái này.
>
> Tiếp, mới xét câu chuyện nếu ta cho phạm vi giới hạn tăng từ rất nhỏ đến
> rất rộng. Thì: ở mức nhỏ → hướng Newton cơ bản là trùng hướng dốc nhất.
> Nhưng ở mức lớn, hướng Newton sẽ có thể khác hướng dốc nhất. Nên khi
> đó nếu chỉ một mực dùng hướng dốc nhất, có thể sẽ không lợi ích. Và khi
> mô phỏng việc tăng dần bán kính tin cậy Δ, thì nghiệm của bài toán
> minimize mk với mk dùng Hessian trong Bk, s.t ||p|| ≤ Δ sẽ cho ra / vẽ ra một
> đường cong hình cẳng chó. Và đó là cái quỹ đạo mà ta muốn MEN THEO
> ĐỂ tìm kiếm điểm thấp nhất của mk trong bán kính giới hạn.
>
> Nhưng dĩ nhiên ta ko biết chính xác cái quỹ đạo đó. (vì có cái quỹ đạo đó thì
> cũng đương nhiên là biết p nên bằng gì với Δ cho trước rồi).
>
> Do đó, người ta DỰNG NÊN MỘT XẤP XỈ CỦA QUỸ ĐẠO ĐÓ. Tạo bởi 2
> vector:
>
> pU: là đi theo hướng dốc nhất và tối thiểu hàm mk restrict theo hướng đó
> (tức là pU là γ (-∇fk) với γ là solution của bài toán mininize mk(γ(-∇fk))
>
> pB là hướng Newton: -(Bk)inv ∇fk
>
> Tức là, cái quỹ đạo này sẽ fixed: đầu tiên đi từ 0 → pU. Và sau đó từ pU đi
> theo hướng pB.
>
> Nên phương trình mô tả cái quỹ đạo sẽ là: p~(τ) = pU + (τ - 1) (pB - pU) với
> τ từ 1 → 2.
>
> Từ đó ta sẽ giải bài toán: minimize hàm mk(p) restrict theo quỹ đạo này.
> Giống như ta minimize hàm mk restrict theo hướng steepest, thì nay sẽ là
> restricted theo quỹ đạo này.
>
> Nhưng thật ra ta ko cần giải bài toán này. vì đã có theorem chứng minh
> rằng ĐI THEO QUỸ ĐẠO NÀY THÌ HÀM mk SẼ GIẢM LIÊN TỤC. Do đó bài
> toán  CHỈ ĐƠN GIẢN LÀ TRỞ THÀNH TÌM ĐIỂM XA NHẤT TRÊN QUỸ
> ĐẠO NÀY TRONG PHẠM VI HÀNG RÀO.
>
> Do đó, nếu điểm cuối của hành trình (τ = 2) vẫn trong hàng rào, thì p~* = pU
> + (2-1)(pB - pU) = pB (tức là ta sẽ rất đẹp, lấy luốn Newton step)
>
> còn không thì giải tìm giao điểm của quỹ đạo với hàng rào.
>
> Đó chính là Dogleg algorithm.
>
> ------
>
> VẬY THÌ TẠI SAO CHỖ NÀY GS NÓI THUẬT TOÁN 7.2 CÓ THỂ COI NHƯ
> LÀ GIỐNG GIỐNG DOGLEG:
>
> À thì bởi vì, 7.2 nó cũng
>
> a) BẮT ĐẦU BỞI HƯỚNG DỐC NHẤT: d0 là hướng dốc nhất tại điểm xuất
> phát. Và ta sẽ đi theo hướng đó để giảm mk xuống thấp nhất trong phạm vi
> hàng rao. À, NHƯ VẬY, Y NHƯ pU Ở TRÊN VỪA ÔN LẠI.
>
> b) SAU ĐÓ, các chuỗi d1,d2,...sẽ NHẰM MỤC TIÊU LÀ TẠO z1,z2,....
> converge về z*, hay p* = - Bkinv ∇fk À. NHƯ VẬY, khá tương đương việc
> Dogleg sẽ tiếp tục  đi từ pU theo hướng pB (Newton step), với 7.2 sẽ tạo
> một chuỗi các hướng mà tổng hợp lại cũng dẫn ta đến xấp xỉ pB.
>
> SO SÁNH:
>
> Dogleg: pU → pB (Newton step)
>
> 7.2: z1 cơ bản chính là pU → z1,z2,.. hội tụ về Newton step.

<br>

<a id="node-6"></a>

<p align="center"><kbd><img src="assets/e4c852e49722c87706aebea1ccb09f400d56045d.png" width="100%"></kbd></p>

<br>

