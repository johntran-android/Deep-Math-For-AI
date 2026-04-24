# 7.1 (continue from StudyBoard notebooks)

📊 **Progress:** `1` Notes | `1` Screenshots

---
<a id="node-2"></a>

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

<br>

