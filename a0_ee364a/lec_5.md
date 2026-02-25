# Lec 5

📊 **Progress:** `61` Notes | `82` Screenshots | `0` AI Reviews

---
<p align="center"><kbd><img src="assets/img_hc27qau.png" width="80%"></kbd></p>

> [!NOTE]
> Tuần này ta có thể install Python để bắt đầu code.
> Nhớ làm homework

<br>

<p align="center"><kbd><img src="assets/img_g6flaac.png" width="80%"></kbd></p>

> [!NOTE]
> đại khái là nói về log concave function gs cho rằng cái này nó
> xuất hiện rất nhiều, nhiều hơn hẳn so với loc convex.
>
> Về định nghĩa thì một function f gọi là log concave nếu log f là
> concave function:
>
> f(mixture của x, y) >= f(x)^θ f(y)^(1-θ) 
>
> (f(x)^θ f(y)^(1-θ) gọi là weighted arithmetic mean
>
> (ta đã biết mixture hay convex combination hay line segment, của
> x, y là khi θx + (1-θ)y với θ nằm trong khoảng [0,1])
>
> Nếu θ = 1/2 thì nó gọi là geometric mean
>
> Một ví dụ là pdf của multi-variate Normal. 
>
> f(x) = [1/√(2π)^n det Σ] e^(-1/2)(x-x_bar)T Σinv (x-x_bar)
>
> Chưa hiểu lắm, nhưng gs nói ta có thể check bằng cách lấy log 
> của nó và xem kết quả là convex (thì f sẽ là log convex) hay concave
> (thì f sẽ là log concave)
>
> Lấy log f ta sẽ có log [1/√(2π)^n det Σ] e^(-1/2)(x-x_bar)T Σinv (x-x_bar)
>
> log [1/√(2π)^n det Σ] e^(-1/2)(x-x_bar)T Σinv (x-x_bar):
>
> Đưa constant ra ngoài.
>
> log [1/√(2π)^n det Σ] + log e^(-1/2)(x-x_bar)T Σinv (x-x_bar)  | log uv = log u + log v
>
> log [1/√(2π)^n det Σ] - [(1/2)(x-x_bar)T Σinv (x-x_bar)]     |  log e^a = a
>
> Ta có function (1/2)(x-x_bar)T Σinv (x-x_bar) là quadratic form. 
>
> Và Hessian matrix sẽ dễ chứng minh chính là Σinv và nó là matrix diagonal
> có các entries là 1/σ^2 với σ^2 là variance của các random variables nên sẽ 
> không âm => mọi eigenvalues đều không âm
>
> Do đó, đây là positive semidefinite matrix. Và từ đó function là convex.
>
> Có thể hiểu Σ là covariance matrix, là diagonal matrix: diag([σ1^2, ...σn^2])
> Để rồi từ đó Σinv đương nhiên sẽ là diag([1/σ1^2, ..., 1/σn^2]). Đơn giản
> là bởi diag([σ1^2, ...σn^2]) diag([1/σ1^2, ..., 1/σn^2]) = I
>
> => với dấu âm thì nó sẽ là concave.
>
> Vậy f là log concave
>
> CHAPTER 3.4 - LOG CONCAVE &
> LOG CONVEX
>
> LOG CONCAVE & LOG CONVEX

<br>

<p align="center"><kbd><img src="assets/img_cr3cy3g.png" width="80%"></kbd></p>

> [!NOTE]
> một cái nữa mà gs cho rằng trong homwork. đó là
> cdf của Gaussian, cũng là log concave.
>
> Và có quy tắc chung là cdf của các density function
> có tính log concave cũng là log concave

<br>

<p align="center"><kbd><img src="assets/img_7b5t0uo.png" width="80%"></kbd></p>

> [!NOTE]
> Một số tính chất của log-concave function.
>
> Gs chỉ nói sơ. Đầu tiên là nếu ta có function khả vi hai lần (twice
> differentiable) với convex domain. Thì nó sẽ log-concave khi và
> chỉ khi f(x) ∇^2f(x) ⪯ ∇f ∇fT
>
> Gs đề nghị ta để ý vế phải là outer product của gradient vector. Và
> không khó để thấy nhờ đã học 1806, nó là rank 1 matrix. Để rồi ông
> nói có một sự thật rằng nếu một matrix ⪯ rank 1 matrix thì nó sẽ
> không thể có rank quá 1 và đồng nghĩa không thể có quá 1
> positive eigenvalue
>
> Hai tính chất sau là:
>
> Tích của hai log-concave function cũng sẽ là log concave
>
> Tổng của hai log-concave function thì chưa chắc là log concave
>
> Integration: Nếu có function log concave, ví dụ như function hai biến x,
> y Thì bằng cách integration over mọi giá trị của một biến (giống như khi
> ta tính marginal pdf của x từ joint pdf f(x,y) bằng cách integrating mọi
> possible value của x ∫-inf:inf f(x,y)dx thì ta sẽ cũng có log concave
> function
>
> PROPERTIES OF LOG-CONCAVE FUNCTIONS

<br>

<p align="center"><kbd><img src="assets/img_pq5dedf.png" width="80%"></kbd></p>

> [!NOTE]
> Một hệ quả của tính chất vừa rồi, là nếu ta có hai rv có pdf có tính
> log concave. Thì tổng của chúng, sẽ là rv có pdf cũng log concave.
>
> Hệ quả nữa đó là nếu ta có set C convex set và y là random variable
> với log-concave pdf. Thì khi đó f(x) = P(x+y ∈ C) sẽ là một log concave
> function theo x
>
> Biết sơ vậy thôi

<br>

<p align="center"><kbd><img src="assets/img_wajp941.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_sn5n1.png" width="80%"></kbd></p>

> [!NOTE]
> Ta sẽ gặp là và hiểu về Yield function
> sau, Khúc này chưa hiểu lắm

<br>

<p align="center"><kbd><img src="assets/img_ib4sv62.png" width="80%"></kbd></p>

<br>

<p align="center"><kbd><img src="assets/img_wubnz9l.png" width="80%"></kbd></p>

> [!NOTE]
> Qua nội dung này "Convexity with respect to generalized
> inequalities"
>
> Nó nói rằng, ta có vector function f R^n -> R^m
>
> Và có một cái giống như Jensen's inequality nhưng chỉ khác là
> hai vế là vector.
>
> f(θx+(1-θ)y) ⪯K θf(x) + (1-θ)f(y)
>
> Để rồi dấu "bé hơn hoặc bằng" ở đây sẽ là ⪯K có ý nghĩa đã biết
> đó là nếu x ⪯K y thì y - x phải thuộc cone K.
>
> FUNCTION f GỌI LÀ K-CONVEX NẾU DOMAIN CỦA NÓ CONVEX
> VÀ NÓ THỎA f(θx+(1-θ)y) ⪯K θf(x) + (1-θ)f(y)
>
> Ví dụ cho hàm f Sm->Sm tức là hàm f take input là symmetric
> matrix mxm và output symmetric matrix mxm
>
> Cụ thể f(X) = X^2. Thì ta sẽ nói f là hàm "S^m+ convex" 
>
> Chưa hiểu phần chứng minh lắm, quay lại sau
>
> CHAPTER 3.4 - CONVEXITY WRT
> GENERALIZED INEQUALITIES

<br>

<p align="center"><kbd><img src="assets/img_umgs1ms.png" width="80%"></kbd></p>

> [!NOTE]
> gs nói tới đây là ta đã đi qua những kiến thức toán khô khan
> nhưng cần thiết để bắt đầu thấy ứng dụng của nó, đề nghị đọc
> Chapter 1,2,3
>
> Và ông cho rằng, convex problem là bài toán có thể giải được
> (tractable)

<br>

<p align="center"><kbd><img src="assets/img_pz0xmuq.png" width="80%"></kbd></p>

> [!NOTE]
> Tiếp theo ta sẽ luớt qua nói sâu hơn về CONVEX
> OPTIMIZATION PROBLEM
>
> CHAPTER 4 - CONVEX
> OPTIMIZATION PROBLEM
>
> 4.1 OPTIMIZATION PROBLEM

<br>

<p align="center"><kbd><img src="assets/img_vrjdtqq.png" width="80%"></kbd></p>

> [!NOTE]
> Đầu tiên ông nói vè bài toán tối ưu ở dạng tiêu chuẩn (standard form)
> thì ông lưu ý ta rằng min và minimize là hai thứ khác nhau.
>
> Thế thì bài toán là ta muốn minimize f0(x) gọi là objective function
> nhưng với constrains có thể là equalities hoặc inequalities (nôm na là
> muốn minimize objective nhưng ràng buộc bởi (list) các đẳng thức
> hi(x) = 0 hoặc list các bất đẳng thức fi(x) ≤ 0 hoặc cả hai
>
> ? inequalities có thể bao gồm >= ko? Gs: Yes.
>
> ====
>
> Và OPTIMAL VALUE, được định nghĩa chính là GIÁ TRỊ NHỎ NHẤT
> (kí hiệu inf = infimum, gs cho rằng cứ hiểu là minimum) của objective
> function f0(x) sao cho x VẪN THỎA CÁC EQUALITIES hi(x)
> = 0 VÀ CÁC INEQUALITIES fi(x) <= 0
>
> p* = inf f0(x) | fi(x) <= 0, i=1,2..m; hi(x) = 0, i=1,2...p = f0(x*)
>
> Gs lưu ý thêm đây là p_"star", kí hiệu cho optimal. Còn "asterrisk" 
> thì kí hiệu dành cho "conjugate" (đọc thì khác thôi chứ cũng chung
> là một kí hiệu)
>
>
> Và nếu TỒN TẠI X KHIẾN THỎA CÁC CONSTRAINTS, thì TA
> GỌI VẤN ĐỀ LÀ FEASIBLE.
>
> Còn nếu không, tức là không có x nào khiến thỏa các
> constrains thì ta gọi vấn đề là INFEASIBLE
>
> Và THEO ĐỊNH NGHĨA p* sẽ = infinity tức là theo định nghĩa,
> thì minimum của một empty set là infinity
>
> Và case còn lại là "UNBOUNDED BELOW" : hiểu nôm na là tồn
> tại x khiến thỏa các constrained nhưng muốn f0(x) nhỏ cỡ nào
> cũng được không có giới hạn. Hay có thể thỏa các constrains
> nhưng không thể tìm được f0(x) nhỏ nhất
>
> OPTIMIZATION IN
> STANDARD FORM

<br>

<p align="center"><kbd><img src="assets/img_l7cs5is.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_s15ok8.png" width="80%"></kbd></p>

> [!NOTE]
> Trong sách chỉ nói thêm về DOMAIN CỦA PROBLEM D, được
> định nghĩa là intersection của domain của các objective &
> constraint functions. Và dĩ nhiên trước khi x là optimal thì (tức
> khiến f0(x) nhỏ nhất) thì nó phải feasible (thỏa constraint) và
> trước khi thỏa constraint thì nó phải thuộc domain của problem
> nữa. Và cái này trong bài gs gọi là một dạng IMPLICIT 
> CONSTRAINT, ràng buộc ẩn, đối nghịch với explicit constraint
> (fi(x) <= 0, hi(x) = 0)
>
> Có một điểm đáng để ý nữa. Có hai cách nói tuy gần nhau nhưng
> hơi khác về optimal point:
>
> Mình hay nói rằng OPTIMAL của problem là x thỏa
> constraint và mà minimize f0(x).
>
> Thì có thể nói theo cách khác, là theo OPTIMAL VALUE p*
> bằng cách nói định nghĩa của p* trước: p* là giá trị nhỏ nhất của
> f0(x) với mọi x thuộc feasible set. Và từ đó optimal point x* là tập
> những điểm trong feasible set khiến f0(x) có giá trị optimal value
> p*
>
> Thật ra cách định nghĩa sau tốt hơn, giúp dễ thấy rằng optimal
> point có thể có nhiều, làm thành nên một set là OPTIMAL SET.
> Bên cạnh đó, việc định nghiã như thế này còn giúp nói về trường
> hợp mà tuy ta có optimal value p* nhưng lại KHÔNG CÓ
> OPTIMAL POINT
>
> 4.1 OPTIMIZATION PROBLEMS
>
> 4.1.1 BASIS TERMINOLOGY

<br>

<p align="center"><kbd><img src="assets/img_9hz1esb.png" width="80%"></kbd></p>

> [!NOTE]
> Ta qua thêm vài định nghĩa: x gọi là feasible nếu nó nằm
> trong domain của f0 (có nghĩa là có xác định f0(x)) và đồng thời
> như vừa nói, đó là nó thỏa các constrains
>
> Thế thì khi có x feasible, thì CÁI NÀO KHIẾN f0(x) MANG OPTIMAL
> VALUE p* THÌ ĐÓ LÀ OPTIMAL POINT
>
> Và Xopt là SET CÁC OPTIMAL POINTS (có thể có nhiều optimal
> points)
>
> Còn LOCAL OPTIMAL thì đại khái là nếu tồn tại một khoảng R nào đó
> mà khi tìm trong đó (thể hiện bởi constraint ||z-x|| <= R) thì ta được f0(x)
> nhỏ nhất và x vẫn thỏa các constraint thì x là local optimal
>
> OPTIMAL POINTS &
> LOCALLY OPTIMAL POINTS

<br>

<p align="center"><kbd><img src="assets/img_vzno2dm.png" width="80%"></kbd></p>

> [!NOTE]
> Trong nói thêm về khả năng OPTIMAL SET RỖNG: Tức là TUY
> TA CÓ OPTIMAL VALUE p*, nhưng KHÔNG CÓ x NÀO GIÚP
> f0(x) ĐẠT GÍA TRỊ NÀY. Khi đó problem gọi là UNATTAINABLE
> & UNSOLVABLE 
>
> Sau đó đề cập đến khái niệm ε-suboptimal, hiểu nôm na nếu x* là
> ε-suboptimal thì f0(x) chỉ các p* một khoảng nhỏ từ ε trở xuống:
> Mà dĩ nhiên là p* là nhỏ hơn f0(x*) nên điều này tương đương
> f0(x*) - p* <= ε hay f0(x*) <= p* + ε 
>
> Và mọi x thỏa như vậy tạo nên ε-suboptimal set
>
> ====
>
> Qua khái niệm LOCAL OPTIMAL thì trong bài đã nói rồi
>
> Ngoài ra còn vài khái niệm như ACTIVE / INACTIVE và REDUNDANT
> CONSTRAINT, cũng ko có gì khó

<br>

<p align="center"><kbd><img src="assets/img_9sq0ies.png" width="80%"></kbd></p>

> [!NOTE]
> hàm f0(x) = x^3 - 3x. sẽ có p* = -infi vì ko có constrain nào thì 
> x càng nhỏ thì f0(x) càng nhỏ, nên bài toán này thuộc diện UNBOUNDED
> BELOW, không có optimal point
>
> Nhưng nếu quy định trong đoạn -1,1 thôi thì khi đó local optimal
> là +1 vì trong đoạn này tại đó thì f0(x) nhỏ nhất.
>
> Một số ví dụ khác:
>
> f0(x) = 1/x thì vì hàm số này sẽ giảm dần về 0, tiệm cận 0 khi x->inf
> nên ko có x nào khiến f0(x) nhỏ nhất cả. Nên p*=0 tức optimal
> value = 0 nhưng KHÔNG CÓ OPTIMAL POINT, cái này trong sách
> gọi là "unattainable"

<br>

<p align="center"><kbd><img src="assets/img_j1mayh8.png" width="80%"></kbd></p>

> [!NOTE]
> nói về constrains, Đại khái là những cái constraint hi(x)=0, fi(x)<=0
> kiểu như là những constrain rõ ràng, thấy rõ. Nhưng ngoài ra,
> ngầm ẩn (implicit) trong đó còn một loại constrain khác.
>
> Đó là X PHẢI NẰM TRONG DOMAIN CỦA fi, hi
>
>  Cái này ko có gì khó hiểu, bởi lẽ nếu x ko nằm trong miền xác định
> của các constraint function thì thậm chí nó còn tệ hơn là không thỏa
> các constrain đó nữa.
>
> Do đó implicit constraint là x phải nằm trong phần giao của các
> domain của hi,fi. Và đây gọi là DOMAIN của PROBLEM.
>
> Nó giống như khi ta ghi f(x) = 1/x thì ngay lập tức phải ngầm quy
> định rằng x phải khác 0 vẫy
>
> Nói ngắn gọn, là trước khi muốn check xem x có thỏa các constraint
> hi,fi hay không thì đầu tiên NÓ PHẢI KHIẾN CHECK ĐƯỢC CÁI ĐÃ
>
> Và khi KHÔNG CÓ EXPLICIT CONSTRAIN (chỉ optimize objective
> function) thì ta gọi là UNCONSTRAINED problem.
>
> Ví dụ ở dưới là một unconstrained problem nhưng dễ hiểu là vì ta có
> hàm log, mà với hàm log thì miền xác định là x phải dương nên ta có
> implicit constraints là aiTx < b
>
> IMPLICIT CONSTRAINT

<br>

<p align="center"><kbd><img src="assets/img_kfce7n5.png" width="80%"></kbd></p>

> [!NOTE]
> Ta biết qua FEASIBILITY PROBLEM. Đại khái là "ta chả cần
> minimize objective f0(x)" gì hết, MIỄN LÀ CÓ X FEASIBLE -
> tức là thỏa các constraint là đủ, thì x nào cũng được.
>
> Để rồi ta có thể coi nó là một trường hợp đặc biệt của bài toán tiêu
> chuân đó là coi như cũng có objective, nhưng có cho vui thôi:
>
> f0(x) = 0.
>
> Cũng đồng nghĩa là ko cần minimize f0 gì hết, miễn là tìm được
> x thỏa các constrain là đủ.
>
> Và khi đó nếu có x thỏa constrain, thì ta cho nó là optimal luôn
> với optimal value = 0.
>
> Còn nếu ko có x thỏa constraint thì optimal value là infinity
> như thông thường
>
> FEASIBILITY PROBLEM

<br>

<p align="center"><kbd><img src="assets/img_41smoem.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_ygqabn.png" width="80%"></kbd></p>

> [!NOTE]
> Cái này đơn giản trong bài nói đủ hết rồi. Chỉ muốn nhắc lại một ý là
> ta có một quy ước rằng khi minimize một tập rỗng thì kết quả là
> infinity.  Tức inf x rỗng = +infinity.
>
> Do đó, bài toán feasible problem, nếu không có điểm nào feasible
> thì optimal value là +infinity (còn nếu có thì nó bằng 0 vì ta đặt
> objective function cho vui là f0(x) = 0)

<br>

<p align="center"><kbd><img src="assets/img_2fkew72.png" width="80%"></kbd></p>

> [!NOTE]
> Rồi, sau đây là một loại các vấn đề mà trong bài giảng gs không
> nói tới.
>
> Đầu tiên là việc ta có thể CHUYỂN / THỂ HIỆN MỘT BÀI TOÁN
> VỀ DẠNG CHUẨN (STANDARD FORM) của bài toán tối ưu.
>
> Thế thì đầu tiên, có một QUY ƯỚC rằng, khi thể hiện
> constraint thì ta sẽ thể hiện theo dạng:
>
> fi(x) <= 0 và hi(x) = 0
>
> Ví dụ như gặp bài toán mà constraint là li <= xi <= ui thì ta sẽ đưa
> nó về dạng chuẩn với hai inequality constraint:
>
> li - xi <= 0 và xi - ui <= 0
>
> 4.1 OPTIMIZATION PROBLEMS
>
> 4.1.2 EXPRESSNG PROBLEMS IN STANDARD 
> FORM

<br>

<p align="center"><kbd><img src="assets/img_jplfxvo.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_pe3sph.png" width="80%"></kbd></p>

> [!NOTE]
> Và ta cũng gặp rất nhiều bài toán tối ưu đặt ra ở dạng maximize
> thay vì minimize. Thì ta cũng đưa nó về dạng chuẩn là maximize
> f0(x) sẽ tương đương minimize - f0(x)
>
> Và trong bài toán maximize thì objective gọi là UTILITY

<br>

<p align="center"><kbd><img src="assets/img_gmucc46.png" width="80%"></kbd></p>

> [!NOTE]
> 4.1 OPTIMIZATION PROBLEMS
>
> 4.1.3 EQUIVALENT PROBLEMS
>
> Một điểm kiến thức quan trọng mà gs lướt qua, là
> EQUIVALENT PROBLEM (vấn đề tương đương)
>
> Đại khái là sẽ rất phổ biến xảy ra việc ta khi đối diện một bài toán
> tối ưu, ta thiết lập một bài toán khác tương đương. Mà việc giải
> bài toán kia cũng giúp tìm ra optimal của bài toán này.
>
> Đó cũng là định nghĩa của equivalent: Hai problem gọi là
> equivalent khi tìm ra solution (tức optimal của cái này) giúp tìm
> ra ngay optimal  của cái kia
>
> Lấy ví dụ đơn giản là bài toán mà objective và constraint của bài
> toán gốc đều được scale bởi scalar dương.
>
> Objective f~0(x) = α0 f0(x), f~i(x) = αi fi(x), h~i(x) = βi hi(x)
>
> thì rõ ràng dễ thấy là nếu ta tìm được x* của bài toán sau, thì nó
> cũng là cái thỏa constraint của bài toán gốc, và cũng là cái khiến
> minimize f0(x). Nên nó cũng là optimal của bài toán gốc.
>
> Do đó hai problem là equivalent.

<br>

<p align="center"><kbd><img src="assets/img_t1cvt2j.png" width="80%"></kbd></p>

> [!NOTE]
> Dạng thứ nhất
> là ĐỔI BIẾN.

<br>

<p align="center"><kbd><img src="assets/img_mbf0tzj.png" width="80%"></kbd></p>

> [!NOTE]
> Rồi, thế thì dạng thứ hai mà ta tạo ra equivalent problem đại khái
> là ta apply hàm đơn điệu tăng vào các objective và các  hàm
> inequality constraints, và equality constraint cũng được apply các
> function sao cho nếu x feasible trong bài toán gốc thì nó cũng
> feasible trong bài toán equivalent và ngược lại.
>
> Và cái ví dụ trước, chính là một dạng của cái này khi ta appy hàm
> tuyến tính (nhân scalar hệ số dương ) vào objective và constraint
> function.
>
> Một ví dụ khác là bài toán gốc có objective là norm (nên không
> âm) và bài toán tương đương có objective là bình phương của
> norm (tức apply hàm square f(u) = u^2, với u không âm thì f là
> monotonic increasing).
>
> Thì đây là ví dụ rất hay gặp, khi ta giải bài toán sau với objective
> ||Ax - b||^2 sẽ dễ hơn và solution của nó cũng là solution của bài
> toán gốc với objective ||Ax - b||
>
> ====
>
> Gs cũng lưu ý: Hai bài toán là EQUIVALENT, nhưng KHÔNG
> THE SAME

<br>

<p align="center"><kbd><img src="assets/img_6zywl35.png" width="80%"></kbd></p>

> [!NOTE]
> Một dạng thứ bai giúp tạo ra equivalent problem là dựa trên cái này:
>
> a <= 0 thì <=> 0 - a >= 0, nếu đặt b = 0 - a, thì ta sẽ có b >= 0 và a +
> b = 0
>
> Do đó constraint fi(x) <= 0 sẽ tương đương fi(x) + si = 0 và si
> >= 0
>
> Và cái hay của cách làm này đó là nó giúp ta chuyển constraint dạng
> chuẩn fi(x) <= 0 THÀNH MỘT EQUALITY CONSTRAINT fi(x) + si =
> 0 và MỘT CONSTRAINT CÓ DẠNG ">=": si >= 0   Nói chung là
> nhiều trường hợp cái này sẽ rất hữu ích.
>
> Và có thể thấy cách làm này làm phát sinh VARIABLE  MỚI LÀ si,
> được gọi là SLACK VARIABLE

<br>

<p align="center"><kbd><img src="assets/img_i46tk9b.png" width="80%"></kbd></p>

> [!NOTE]
> Dạng thứ ba giúp tạo ra equivalent problem là khi xét các inequality
> constraint của bài toán gốc (ý là standard form): hi(x) = 0 i = 1,...p
>
> Thì ta có thể dùng cách thứ 3, nếu như có thể solve x explicitly:
>
> hi(x) = 0 <=> x = Φ(z)
>
> Khi đó, thế x vào objective và inequality constraint ta sẽ chuyển
> bài toán gốc thành bài toán tương đương trong đó không còn
> inequality constraint nữa:
>
> minimize f~0(z) = f0(Φ(z)) constraint f~i(z) = fi(Φ(z)) <= 0
>
> Thế thì khi giải ra z* là optimal của bài toán sau, thì Φ(z*) chính là
> optimal của bài toán gốc.

<br>

<p align="center"><kbd><img src="assets/img_g5ub9m0.png" width="80%"></kbd></p>

> [!NOTE]
> Đại khái là cái này nói cụ thể hơn cách tiếp cận vừa rồi khi equality
> constraint hi(x) = 0 có dạng tuyến tính. Tức là các phương trình  hi(x)
> = 0 là tuyến tính thì với mọi i nó tạo thành hệ phương trình tuyến
> tính, và có thể được thể hiện bởi Ax = b (aiTx = bi tương đương hi(x)
> = 0)
>
> Khi đó nếu mà problem feasible (tức là tồn tại feasible point) thì đồng
> nghĩa Ax = b có nghiệm, và nghiệm này như đã học trong MIT 18.06
> là x_complete (hay x), là kết hợp của x_particular( hay x0) và x_null.
> Để rồi nếu nullspace của A khác 0 thì ta có vô số nghiệm còn
> ngược lại thì hệ có nghiệm duy nhất.
>
> Và x = x0 + x_null chính là x0 + Fz với F là matrix có các cột là basis
> của nullspace của A: R(F) hay C(F) = N(A), thì Fz dĩ nhiên là x_null:
> linear combination của nullspace basis).
>
> Khi đó ta sẽ bỏ đi p equality constraint hi(x) = 0 với equivalent problem:
>
> minimize f~0(z) = f0(x0 + Fz) với constraint f~i(z) = fi(x0 + Fz) <= 0
>
> Gs nói equivalent problem cũng giảm đi số variable = rank A. Là sao?
>
> Đó là vì, với A là matrix [m, n] thì x là R^n vector, tức là ta có n
> optimization variables.
>
> Nhưng equivalent problem, thì xét vector z, có bao nhiêu
> component?
>
> Câu trả lời là số component của z chính là số cột của F, tức số basis
> vector của C(F) cũng là N(A), hay nói cách khác chính là dim N(A).
>
> Mà dim N(A) thì bằng gì, chính bằng n - dim C(AT) (column space và
> rowspace orthogonal complement) và n = rank (A)
>
> Vậy số component của z sẽ ít hơn số component của z một số lượng
> là rank(A)
>
> Trong sách có nói đến vụ ta chọn F full rank, tức là full column rank,
> và cái này đồng nghĩa dùng các basis của C(A) là cột của F (ko dư
> cột nào)

<br>

<p align="center"><kbd><img src="assets/img_aq19g9q.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_ipradi.png" width="80%"></kbd></p>

> [!NOTE]
> Một dạng nữa (thứ 4) đối ngược lại với bỏ bớt equality constraint là
> tạo thêm equality constraint.
>
> Đại khái gs nói cái này nói chung chung thì khó và ko ích lợi nên
> ta nói dạng cụ thể mà sẽ hay gặp. 
>
> Rất dễ hiểu là khi ta có objective của bài toán gốc có dạng:
>
> f0(A0x + b0) = 0 và inequality constraint al2 fi(Aix + bi) <= 0
>
> Khi đó đặt y0 = A0x + b0, yi = Aix + bi i = 1,2...
>
> thì ta sẽ có equivalent problem: minimize f0(y0) constraint fi(yi) <= 0
> và có thể các constraint y0 = A0x + b0, yi = Aix + bi
>
> Dễ thấy objective là f0(y0) chỉ liên quan đến variable y0 còn 
> các inequality constraint fi(yi) <= 0 chỉ liên quan đến yi. Thành ra 
> gọi là objective và inequality constraint INDEPENDENT

<br>

<p align="center"><kbd><img src="assets/img_s7d00or.png" width="80%"></kbd></p>

> [!NOTE]
> Rồi, dạng tiếp theo mà ta có thể xây dựng equivalent problem là ta
> dựa vào một (có thể gọi là) định lý:
>
> Nôm na là giả sử ta có hàm hai biến f(x, y) thì việc minimize hàm f
> over x, y sẽ có thể làm bằng cách lần lượt minimize over x,  rồi sau đó
> minimize over y.
>
> inf x,y f(x,y) = inf x {inf y f(x,y)} = inf x{f'(x)}
>
> Và tính chất này giúp ta có cách xây dựng equivalent mà nói chung
> chung thì khó, nên gs lấy dạng cụ thể là hàm f(x) với x là R^n  Thì ở
> đây x có thể tách thành (x1, x2) với x1 ∈ R^n1, x2 ∈ R^n2 với n1 + n2
> = n.
>
> Và bài toán gốc là minimize f0(x1, x2) với constraint của x1: fi(x1) <= 0
> và constraint của x2: fi(x2) <= 0
>
> Khi đó, đầu tiên ta minimize over x2 trước:
>
> f~0(x1) = inf z {f0(x1, z) với z feasible (z thỏa các constraint liên quan
> đến x2)}
>
> thì bài toán gốc sẽ equivalent với bài toán sau:
>
> minimize f~0(x1) constraint fi(x1) <= 0 (tức là các constraint liên quan
> đến x1)

<br>

<p align="center"><kbd><img src="assets/img_yryfr5b.png" width="80%"></kbd></p>

> [!NOTE]
> Một ví dụ của cái này, hàm theo biến x1, x2. 
>
> thì ta minimize over x2 trước để có f~0(x1) thì bài toán gốc sẽ
> equivalent với minimize f~0(x1) với constraint của x1
>
> Hàm f0 là quadratic nên minimize over x2 ta chỉ việc tìm gradient
> wrt x2, và giải tìm critical point

<br>

<p align="center"><kbd><img src="assets/img_sjcvue1.png" width="80%"></kbd></p>

> [!NOTE]
> QUAY LẠI SAU

<br>

<p align="center"><kbd><img src="assets/img_la3nsah.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_nsz37s.png" width="80%"></kbd></p>

> [!NOTE]
> Một loại nữa, cũng rất hay dùng, và cũng không có gì khó hiểu.
>
> Xét bài toán standard optimization với các constraint fi(x) <= 0
> và hi(x) = 0. Thì như đã hiểu, để x là optimal thì đầu tiên nó
> phải feasible và trước đó nữa thì nó phải ∈ domain của problem
> D. Trong đó yêu cầu tiên quyết là phải thuộc domain của D chính
> là một dạng implicit constraint còn các constraint kia là explicit.
>
> Vậy thì rất dễ hiểu là bây giờ ta QUY ĐỊNH LẠI DOMAIN CỦA 
> PROBLEM D PHẢI BAO GỒM FEASIBLE SET, thì khi đó ta có 
> thể bỏ các explicit constraint fi(x) <= 0, hi(x) <= 0.
>
> Và ta làm vậy bằng cách đơn giản là thay f0(x) bằng F(x) sao cho
> nếu x feasible thì F(x) = f0(x) còn ngược lại x infeasible thì F(x) = 
> + infinity.
>
> Để rồi ta cũng có kết quả equivalent rằng khi ko có feasible x nào
> thì việc minimize objective là hàm có giá trị = +infinity thì cũng
> y như minimize bài toán gốc với feasible set rỗng. (kết quả đều
> là optimal value = infinity)
>
> ====
>
> Và ngược lại, thì ta cũng có thể biến implicit constraint trở thành
> explicit. Ví dụ như minimize f0(x) với f(x) = xTx khi Ax = b, và = inf
> khi otherwise. Dĩ nhiên ở đây để f xác định thì x phải thỏa Ax = b
> nói cách khác domain của f0 (trong tường hợp này ko có constraint
> function, nên cũng là domain của problem) là solution set của Ax = b
>
> Nên như đã nói, có thể coi Ax = b là implicit constraint.
>
> Vậy ta có thể đưa nó thành explicit constraint và có bài toán eqiovalent:
>
> minimize xTx constraint Ax = b. Ko có gì khó hiểu

<br>

<p align="center"><kbd><img src="assets/img_0kekkka.png" width="80%"></kbd></p>

<br>

<p align="center"><kbd><img src="assets/img_bxddgml.png" width="80%"></kbd></p>

> [!NOTE]
> 4.1 OPTIMIZATION PROBLEMS
>
> 4.1.4 PARAMETERS & ORACLE PROBLEM DIS
>
> QUAY LẠI SAU

<br>

<p align="center"><kbd><img src="assets/img_wp45aid.png" width="80%"></kbd></p>

> [!NOTE]
> Tiếp, ta sẽ chuyển từ bài toán STANDARD OPTIMIZATION
> sang CONVEX OPTIMIZATION
>
> Đơn giản là, nó chỉ là bài toán standard optimization có thêm
> điều kiện là các hàm objective và inequality constraints đều là
> CONVEX function, và các equalities đều là AFFINE function
>
> Và với việc các equalities constraint là các affine, tức là linear
> equation (mà trong standard optimization problem, thì nó ko nhất
> thiết phải là bậc 1) thì ta có thể thể hiện list các linear constraints
> này ở dạng matrix Ax = b

<br>

<p align="center"><kbd><img src="assets/img_shlsz3m.png" width="80%"></kbd></p>

> [!NOTE]
> Đại khái là trong ví dụ này ta có một "not a convex problem"
>
> Vì f1 không convex. h1 cũng không phải affine.
>
> Tuy nhiên nó tương đương (equivalent) với một problem bên dưới.
> Nói tương đương có nghĩa là nếu solve được cái này thì solve
> được cái trên.
>
> Nhưng điểm đáng chú ý, cái bên dưới thì lại là convex optimization
> problem

<br>

<p align="center"><kbd><img src="assets/img_w4bwn5s.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_gf39z.png" width="80%"></kbd></p>

> [!NOTE]
> 4.2 CONVEX OPTIMIZATION PROBLEMS
>
> 4.2.1 CONVEX OPTIMIZATION IN STANDARD
> FORM
>
> Trong sách bổ sung nhiều ý quan trọng mà gs ko nói trong bài
> hoặc có nói mà mình ko hiểu / để ý.
>
> Đầu tiên định nghĩa thì dễ rồi, optimization sẽ là convex
> optimization problem nếu objective và inequality constraint là
> convex và equality constraint là affine.
>
> Thế thì như ta đã biết địh nghĩa một convex function là gồm hai ý:
> 1) domain của nó là convex set và 2) nó thỏa tính chất nôm na là
> f của mixture <= mixture của f.
>
> Vậy nay các domain của f0 và inequality constraint trở thành
> convex set. Do đó DOMAIN CỦA PROBLEM (vốn là intersection
> của domain các function) cũng sẽ là CONVEX SET.
>
> Rồi FEASIBLE SET, là tập những điểm trong domain và thỏa
> constraint
>
> Thế thì thỏa equality constraint hi(x) = 0 (mà nay là các linear
> function aiTx = bi) thì đây là intersection của các HYPERPLANE.
>
> Thỏa inequality constraint fi(x) <= 0 với fi(x) convex thì set các
> điểm thỏa fi(x) <= 0 chính là một SUB-LEVEL SET, mà với hàm f
> convex trong các phần trước ta đã học là sub-level set của nó
> CŨNG LÀ CONVEX SET.
>
> Vậy tóm lại, FEASIBLE SET LÀ INTERSECTION CỦA CONVEX
> SET (DOMAIN), HYPERPLANES VÀ CONVEX SUB-LEVEL SET
> => FEASIBLE SET CŨNG LÀ CONVEX SET
>
> Thành ra bài toán convex optimization có bản chất là minimize
> objective over CONVEX SET

<br>

<p align="center"><kbd><img src="assets/img_6acopdi.png" width="80%"></kbd></p>

> [!NOTE]
> Rất đơn giản, nếu ta có hàm f0(x) concave thì -f0(x) là convex
> Nên khi bài toán maximize f0(x) mà f0(x) concave thì nó tương
> đương minimize -f0(x) là convex.
>
> Nên bài toán MAXIMIZE HÀM CONCAVE OBJECTIVE CŨNG LÀ
> BÀI TOÁN CONVEX  OPTIMIZATION
>
> (nhưng inequality constraint vẫn phải convex và equality vẫn phải
> affine)

<br>

<p align="center"><kbd><img src="assets/img_88348jr.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_9fq0yg.png" width="80%"></kbd></p>

> [!NOTE]
> Rồi đại khái là người ta cho ví dụ này trong đó tuy equality không
> affine nên theo định nghĩa đây không phải là convex optimization
> problem.
>
> Nhưng feasible set của nó và objective của nó cũng là convex set
> / function.
>
> Thành ra có người gọi nó là bài toán ABSTRACT CONVEX
> OPTIMIZATION PROBLEM

<br>

<p align="center"><kbd><img src="assets/img_w0x6iww.png" width="80%"></kbd></p>

> [!NOTE]
> gs nói qua một cái tuy nghe có vẻ đơn giản nhưng thực sự rất
> mạnh:
>
> Đó là ĐỐI VỚI CONVEX PROBLEM THÌ BẤT KÌ LOCALLY
> OPTIMAL POINT CŨNG CHÍNH LÀ GLOBAL OPTIMAL

<br>

<p align="center"><kbd><img src="assets/img_vjrchgu.png" width="80%"></kbd></p>

> [!NOTE]
> Để chứng minh gs cho local optimal x_loc và giả sử ta có global
> optimal x~ với f0(x~) < f0(x_loc). Ta sẽ chứng minh với convex
> problem thì điều này ko thể xảy ra mà xloc phải chính là x~
>
> Đầu tiên gs hỏi những điểm trên line segment có feasible không, nếu
> như xloc và x~ đã feasible rồi (thỏa các constraints)
>
> Thử lập luận:
>
> Những điểm trên line segment này đều sẽ feasible (tức thỏa
> constraints) vì ta đang nói về convex optimization, thì trong đó, các
> equalities là các affine, các inequalities là các convex function.
>
> Mà x_loc và x~ đều thỏa các constraint, tức fi(x_loc) = 0 và fi(x~) = 0
> thì xét mixture của chúng,
>
> f(θx_loc + (1-θ)x~) 
>
> Với f là affine thì cái này sẽ là = θf(x_loc) + (1-θ)f(x~) | đây là tính chất
> hay điều kiện của affine function (với convex function thì điều kiện trở 
> thành f(θx_loc + (1-θ)x~) <= θf(x_loc) + (1-θ)f(x~) chính là Jensen's 
> inequality
>
> Vậy tiếp tục ở đây ta có f(θx_loc + (1-θ)x~) = θ*0 + (1-θ)*0 = 0
>
> Vậy mixture của chúng thỏa các equalities constraints.
>
> Còn với các inequalities constrain:
>
> hi(θx_loc + (1-θ)x~) theo Jensen's inequality:
>
> hi(θx_loc + (1-θ)x~) <= θhi(x_loc) + (1-θ)hi(x~)
>
> Với x_loc, x~ đã thỏa các constraints hi(x_loc) <= 0, hi(x~)<=0 thì có
> thể suy ra θhi(x_loc) + (1-θ)hi(x~) cũng <= 0 từ đó suy ra
>
> hi(θx_loc + (1-θ)x~) <= 0 => mixture của x_loc và x~ cũng thỏa các
> inequalities constraint

<br>

<p align="center"><kbd><img src="assets/img_8esoutn.png" width="80%"></kbd></p>

> [!NOTE]
> gs nói, đại khái ko phải là proof nhưng hình ảnh này sẽ giúp ta dễ
> hiểu. Đó là, khi ta đi từ x_loc đến x~, thì hàm objective function sẽ đi
> từ f0(x_loc) đến f0(x~)
>
> Thì rất dễ thấy ngay lập tức nó khiến mâu thuẫn xảy ra. đó là, vì đang
> cho rằng f0(x~) < f0(x_loc), mà function f0 theo định nghĩa của bài
> toán convex optimization thì nó phải là convex function, do đó nó có
> non-negative curvature.
>
> Điều này khiến để đi từ f0(x_loc) đến f0(x~) nó BẮT BUỘC PHẢI ĐI
> XUỐNG chứ không thể đi lên, vì khi đi cong lên rồi mới xuống lại thì
> nó sẽ có curvature âm
>
> Và đây là điều tạo ra mâu thuẫn: x_loc là local optimal. Mà theo định
> nghĩa local optimal thì tại những điểm rất gần x_loc thì f(x_loc + ε)
> phải > f(x_loc) nên đại khái là "khi đi ra khỏi x_loc thì nó phải đi lên
> chứ ko thể có vụ đi xuống được
>
> Đây có thể coi là phản chứng hình học

<br>

<p align="center"><kbd><img src="assets/img_nsxk5re.png" width="80%"></kbd></p>

> [!NOTE]
> Trong sách đưa ra chứng minh chuẩn hơn cho tính chất trong
> convex problem thì local optimal và global optimal là một.
>
> Nhưng chứng minh theo gs dễ hiểu dễ nhớ hơn
>
> 4.2 CONVEX OPTIMIZATION PROBLEMS
>
> 4.2.2 LOCAL & GLOBAL OPTIMA

<br>

<p align="center"><kbd><img src="assets/img_bwy9own.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_1btvqb.png" width="80%"></kbd></p>

> [!NOTE]
> ở đây nói đến tiêu chí CẦN VÀ ĐỦ để x là optimal của một objective
> function f0 khả vi (differentiable):
>
> Như đã biết, nó sẽ phải thỏa các constraints cái đã, gọi X là feasible
> set thì x PHẢI THUỘC FEASIBLE SET.
>
> Thế rồi, điều kiện tiếp theo là nó phải khiến f0(x) MANG GIÁ TRỊ
> OPTIMAL VALUE p* tức là minimize f0 trong các x thuộc X.
>
> Vậy thì, trong hình các đường chấm chấm chính là các LEVEL CURVE,
> từ 18.02 ta biết khi di chuyển trên các level curve thì giá trị hàm f0 sẽ
> không đổi. Và từ đó cũng dễ dàng chứng minh gradient vector ∇f sẽ
> vuông góc với level curve:
>
> Giả sử ta di chuyển một đoạn nhỏ theo level curve từ x đến x+ε (dĩ
> nhiên x, và x + ε, trong hình này coi như trong R2, thì là các 2D vector).
> Thì theo dùng linear approximation:
>
> trong phạm vi ε rất nhỏ ta có: f(x+ε) ~= f(x) + ∇fTε. Và như đã nói, vì ta
> đang di chuyển trên level curve, nên f không đổi. Từ đó
>
> f(x+ε) - f(x) = 0. Vậy f(x+ε) ~= f(x) + ∇fTε ~ = f(x+ε) - f(x) ~= ∇fTε
>
> <=> ∇fTε ~= 0
>
> Điều này suy ra gradient vector vuông góc với ε. Mà ε với độ lớn vô
> cùng nhỏ thì nó sẽ parallel với tiếp tuyến của level curve tại x, do đó
> gradient vector tại x, vuông góc với tiếp tuyến của level curve tại x và
> cũng là vuông góc với level curve.
>
> Và có thể mở rộng ra, để nói rằng với bất kì level curve đi qua x nào lập
> luận trên cũng đúng. Từ đó giúp kết luận gradient vector vuông góc
> với level surface
>
> Quay lại đây, có thể hiểu rằng nếu x thuộc feasible set X và gradient
> vector tại x ∇f TẠO NÊN MỘT SUPPORT HYPERPLANE - the định
> nghĩa sẽ là hyperplane, hay ở đây là đường thẳng mà MỌI ĐIỂM
> TRONG FEASIBLE SET X ĐỀU NẰM MỘT BÊN CỦA HYPERPLANE,
> ∇f(y-x) >= 0, thì khi đó x  chính là OPTIMAL  Tại sao, thử lập luận xem
> ?
>
> RẤT ĐƠN GIẢN, vì BỞI ĐỊNH NGHĨA CỦA SUPPORTING
> HYPERPLANE Thì ngoài x ra thì mọi điểm trong set C sẽ đều nằm một
> bên của hyperplane Ở đây, điều này có nghĩa là mọi điểm trong feasible
> set X đều nằm một bên của đường thẳng tạo bởi normal vector là -
> gradient ∇f0(x) này.
>
> Thế thì cũng theo định nghĩa, di chuyển trong feature set từ x theo
> bất kì hướng nào cũng sẽ đều là đi theo hướng khiến tăng f0 bởi
> các vector đó đều hợp với gradient vector một góc nhỏ hơn 90 độ.
>
> Muốn giảm f0, ta phải "bước sang" bên đây của haft-plane. Có nghĩa là
> phải đi theo hướng hợp với gradient một góc > 90 độ. Tuy nhiên như đã
> nói, không có điểm nào trong feasible set X bên đó cả. Do đó x là điểm có
> f0 nhỏ nhất.
>
> Và có thể lập luận thêm để chứng minh rằng khi đi trong feasible set X
> theo ví dụ như vector màu tím.Ta có f(x+ε) ~= f(x) + ∇fTε. Thế mà vì như
> đã nói ta di chuyển trong haft-plane có chứa feasible set X, thì dĩ nhiên
> các vector này đều hợp với ∇f0(x) một góc < 90 độ. Và dẫn tới ∇fTε sẽ
> mang giá trị dương, vì ∇fTε = ||∇f||*||ε||*cos α(∇f, ε) với góc < 90 độ thì cos
> > 0 => ∇fTε > 0 => f(x + ε) > f(x) vậy là đi theo hướng nào từ x trong 
> feasible set đều làm tăng f(x)
>
> OPTIMALITY CRITERION

<br>

<p align="center"><kbd><img src="assets/img_deflq6e.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_9twk9n.png" width="80%"></kbd></p>

> [!NOTE]
> 4.2 CONVEX OPTIMIZATION PROBLEMS
>
> 4.2.3 AN OPTIMALITY CRITERION FOR 
> DIFFERENTIABLE f0

<br>

<p align="center"><kbd><img src="assets/img_14hyln5.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_mwx8v9.png" width="80%"></kbd></p>

> [!NOTE]
> Chứng minh OPTIMALITY CONDITION.
>
> Chứng minh nếu x thỏa ∇f0(x)T(y-x) >= 0 với mọi y ∈ X thì x là optimal:
>
> Đầu tiên ta sẽ cần dùng đến một theorem quan trọng của convex function:
> gọi là FIRST CONDITION: Trong đó nói rằng:
>
> f(x) convex <=> với mọi x, y ∈ dom f : f(y) >= f(x) + ∇f(x)T(y - x)
>
> Vậy thì ở đây, ta có f0 là convex, nên f0(y) >= f0(x) + ∇f0(x)T(y - x) (1)
>
> Mà đang chứng minh chiều đi, ta có ∇f0(x)T(y - x) >= 0 với mọi y ∈ X:
> nên (1) => f0(y) >= f0(x) với mọi y ∈ X. => x là optimal
>
> ====
>
> Chứng minh nếu x là optimal thì ∇f0(x)T(y-x) >= 0 với mọi y ∈ X
>
> Để chứng minh chiều ngược, ta chỉ cần giả sử x là optimal mà tồn tại y ∈ X
> sao cho ∇f0(x)T(y-x) < 0.
>
> Thế thì đơn giản là: áp dụng linear approx.:
>
> f0(y) ~= f0(x) + ∇f0(x)T(y-x)  ta sẽ có ngay f0(y) < f0(x)
>
> Cái này nôm na là, nếu tại tồn tại y khiến ∇f0(x)T(y-x) âm thì chỉ cần đi
> về phía đó từ x, thì hàm f sẽ còn giảm thêm nữa.
>
>  dẫn đến kết luận x không phải optimal

<br>

<p align="center"><kbd><img src="assets/img_d8owu8l.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_4wfk.png" width="80%"></kbd></p>

> [!NOTE]
> Nếu là unconstraint. thì gs cho rằng cái tiêu chuẩn trên sẽ trở thành/
> đồng nghĩa với việc gradient vector vanish.
>
> Có nghĩa là, với unconstraint convex optimization problem. Việc tìm
> optimal chỉ đơn giản là tìm solution của ∇f0(x) = 0 
>
> Lí do là vì, nếu không có (explicit) constraint, tức feasible set X mở
> rộng ra toàn bộ R2. 
>
> Thì điểm OPTIMAL PHẢI LÀ NƠI CÓ GRADIENT = 0 VÌ NẾU KHÔNG
> TA CÓ THỂ TIẾP TỤC ĐI THEO HƯỚNG CỦA - GRADIENT ĐỂ
> TIẾP TỤC GIẢM f0
>
> Hay nói như gs, giả sử tại optimal mà gradient khác 0, gọi là a đi thì
> vẫn có thể tìm ra điểm y khiến không thỏa criterion ∇f0(x)T(y-x) >= 0
>
> (đơn giản chỉ việc tìm y sao cho aT(y-x) < 0)
>
> Và với việc ta đang trong bài toán convex, thì đó sẽ chính là global
> optimal, nơi gradient vanish, tức gradient = 0
>
> Gs nói thêm, như calculus đã biết, ví dụ như mình học 1802 đi, thì
> gradient = 0 chỉ giúp giải ra critical point, hay gs gọi là stationary point
> vốn dĩ nó có thể là minima, maxima hoặc saddle point. Còn với convex
> thì đây chắc chắn là global minimum
>
> ====
>
> OPTIMALITY CRITERION ĐỐI VỚI
> UNCONSTRAINED PROBLEM

<br>

<p align="center"><kbd><img src="assets/img_ncglgo5.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_0tee2h.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_rkeut.png" width="80%"></kbd></p>

> [!NOTE]
> Trong sách đưa ra chứng minh cho nhận định khi bài toán convex
> optimization không có constraint thì optimal đơn giản là giải nghiệm
> của ∇f0(x) = 0. (chưa xem kĩ lắm)
>
> Thì ý chính là, lúc này ta quan tâm phương trình ∇f0(x) = 0 có
> nghiệm hay không. Nếu vô nghiệm thì tức là optimization problem
> không có optimal. Và việc này có thể đến từ việc problem có
> optimal value p* nhưng không có x nào khiến f0(x) = p*.
>
> Đây chính là case UNACHIEVALBE
>
> Trường hợp còn lại là không có optimal value luôn, tức là hàm f0(x)
> muốn nhỏ nhiêu thì nhỏ = UNBOUND BELOW
>
> Nhưng cũng có thể giải ra nhiều nghiệm, khi đó ta có một set các
> optimal.
>
> ====
>
> Ví dụ ở dưới với f0 là quadratic function thì ∇f là Px + q (cái này giờ
> quá dễ để derive rồi).
>
> Vậy thì ∇f(x) = 0 <=> Px = -q. Và đây là hệ phuong trình tuyến tính.
> Nhờ 1806 đã quá hiểu, nó sẽ vô nghiệm khi q (cũng là -q) nằm
> ngoài columns space của P C(P) hay R(P).
>
> Ngược lại thì hệ có nghiệm, khi đó nếu nullspace chỉ có zero vector,
> thì hệ có nghiệm duy nhất là x_particular. Thì ở đây P là S^n+, tức
> positive semi definite  symmetric matrix. Nên khi nullspace chỉ có
> zero thì cũng chính là P full rank, và positive definite (≻0). Khi đó P
> invertible và từ đó x_particular = Pinv(-q).
>
> Còn nếu nullspace có nonzero vector thì nghiệm sẽ là x_particular
> + x_null
>
> Lúc này dĩ nhiên là P không còn nonsingular nữa. Nhưng ta vẫn có
> thể nhờ pseudo inverse P^+ để có x_particular:
>
> Do đó solution (cũng là optimal) có công thức là (P^+)(-q) + N(P) là vậy

<br>

<p align="center"><kbd><img src="assets/img_uxiwsk7.png" width="80%"></kbd></p>

> [!NOTE]
> một vài điểm đáng chú ý, vì đây là bài toán unconstrained nên optimality 
> condition trở thành ∇f0(x) = 0.
>
> Hàm f0(x) = - Σi log(bi - aiTx). Tính ∇f0(x):
>
> Viết lại f0(x) = - 1Tlog(b - Ax) 
>
> Đặt u(x) = b - Ax => f0(u) = - 1Tlog(u)
>
> df0(u) = f0(u + du) - f0(u) = -1Tlog(u + du) + 1Tlog(u)
>
> = - Σi log(ui + dui) + Σi log(ui) (1)
>
> Xét f(x) = log(x). Với x ~= x0: linear approx. cho ta biết:
>
> f(x) ~= f(x0) + f'(x0)(x - x0) 
>
> tức là log(x) ~= log(x0) + (1/x0)(x - x0)
>
> Hoặc với δx ~= 0 thì f(x + δx) ~= f(x) + f'(x) δx
>
> <=> log(x + δx) ~= log(x) + (1/x) δx
>
> => log(ui + dui) ~= log(ui) + dui/ui
>
> => (1) = - Σi [log(ui) + dui/ui] + Σi log(ui)
>
> = Σi [- log(ui) - dui/ui + log(ui)] = - Σi dui/ui = -1T(du/u)
>
> Xét du: u(x) = b - Ax => du(x) = u(x + dx) - u(x)
>
> = b - Ax - Adx - b + Ax = - Adx => du(x)_i = - aiTdx
>
> => - Σi dui/ui = - Σi (- aiTdx) / (bi - aiTx) = Σi aiTdx / (bi - aiTx)
>
> = Σi [1 / (bi - aiTx)]  aiTdx
>
> Thế thì theo mit 18s096, khi ta đã có df = linear operator act on dx (f'(x)[dx])
> thì linear operator đó chính là derivative. Ở đây kết quả ra df = vector
> dot product với dx => gradient chính là ∇f = Σi [1 / (bi - aiTx)] ai
>
> (đây quả thật là vector, dù có dấu Σ, vì ai là row vector, hàng thứ i của
> A, chia cho (bi - aiTx) là một scalar, vẫn ra một vector. Và Σ các vector
> lại vẫn là một vector. Nên gradient vector là vector mà phần tử thứ
> ith là tổng phần tử thứ i của các hàng của A sau khi scale với scalar
> tương ứng
>
> Vậy optimality condition là Σi [1 / (bi - aiTx)] ai = 0
>
> và dĩ nhiên x phải thuộc domain của f0, và f0 là tổng các log (bi - aiTx)
> nên tập xác định của hàm log(u) là u phải không âm => bi - aiTx >= 0
> <=> Ax - b ⪯ 0
>
> Thế thì việc có optimal hay không sẽ tùy vào việc ∇f0(x) = 0 có nghiệm
> thỏa Ax - b ⪯ 0 hay không.

<br>

<p align="center"><kbd><img src="assets/img_esr03ny.png" width="80%"></kbd></p>

> [!NOTE]
> Một cái nữa đó là minimize f0(x) subject to Ax = b, cái này gs nói ta
> sẽ quay lại nói về nó sau. Nhưng đây là cái 1802 đã học: Lagrange
> multiplier.

<br>

<p align="center"><kbd><img src="assets/img_w1kns1y.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_gz38uc.png" width="80%"></kbd></p>

> [!NOTE]
> Đây là một case quan trọng. Khi chỉ equality constraint là affine 
> Ax = b
>
> Dĩ nhiên feasible set là affine set. Thế thì optimality condition như 
> đã biết sẽ là:
>
> ∇f0(x)T(y - x) >= 0 với mọi y ∈ feasible set, tức là ở đây y phải là
> solution của Ax = b.
>
> Thế thì dĩ nhiên nếu Ax = b vô nghiệm (khi b không thuộc C(A) thì
> feasible set rỗng, bài toán thành infeasible problem)
>
> Vậy thì vì y phải là solution của Ax = b, nên nó phải có dạng là
> x_particular + x_null, với x_particular trong row-space, và x_null
> là nonzero vector của nulls-pace. Nên nếu gọi x là (particular) 
> solution thì y = x + v với v ∈ N(A)
>
> Khi đó điều kiện ∇f0(x)T(y - x) >= 0 với mọi y feasible 
>
> Vậy thì với x, y thuộc feasible set thì x, y đều có dạng là x_particular
> + nullspace vector ⇨ y - x nhất định là nullspace vector v
>
> Sẽ tương đương: 
>
> ∇f0(x)Tv >= 0 với mọi v ∈ N(A)
>
> Rồi, xét ∇f0(x)Tv, nó là linear function của v, trong sách lập luận
> rằng, với v thuộc subspace (nulls-pace) thì cái này nó sẽ chỉ ko
> âm nếu nó bằng 0. Có thể hiểu ý này giống như xét f(x) = ax thì 
> để ax >= 0 với mọi x thì chỉ xảy ra khi ax = 0 với mọi x.
>
> (Cái ý này tạm thời vẫn hiểu nhưng có thể suy nghĩ và bàn
> thêm)
>
> Vậy điều kiện trở thành ∇f0(x)Tv = 0 với mọi v ∈ N(A)
>
> Và đây chính là thể hiện ∇f0(x) vuông góc với nullspace, đương
> nhiên dẫn tới nó nằm trong rowspace C(AT)
>
> Và điều kiện optimality condition trở thành:
>
> "∇f0(x) nằm trong rowspace C(AT)"
>
> Tới đây ta lập luận như sau:
>
> Nếu u ∈ C(AT) thì -u cũng belong C(AT) thì khi đó u và -u sẽ đều
> có thể thể hiện bởi linear combination của các A's row (chưa
> chắc A full row rank nhưng nhận định này đúng kể cả các row của
> A dependent vì trong đó nhất định có một basis)
>
> Và do đó ta có thể thể hiện -u = ATv
>
> Vậy -∇f0(x) = ATv từ đó ta có ∇f0(x) + ATv = 0
>
> Vậy optimality condition cuối cùng trở thành ∇f0(x) + ATv = 0
> đây chính là LAGRANGE MULTIPLIER NỔI TIẾNG TRONG
> CALCULUS

<br>

<p align="center"><kbd><img src="assets/img_d06u51s.png" width="80%"></kbd></p>

> [!NOTE]
> một điểm nữa là minimization over non-negative orthant:
>
> minimize f0(x) subject to x ≽ 0.
>
> Gs chi nói sơ, ta sẽ tìm hiểu sâu sau vài bài nữa

<br>

<p align="center"><kbd><img src="assets/img_i2cl6vh.png" width="80%"></kbd></p>

> [!NOTE]
> qua ví dụ này, khi constraint là x ≽ 0, (sau này sẽ học đây chính là
> x ≽K 0 với K = R^n+ non-negative orthant), và nó có nghĩa là mọi
> component của x đều ko âm.
>
> Thế thì để giải bài toán này minimize f0(x) subject to x ≽ 0, dùng
> optimal condition ta sẽ có nếu x là optimal thì x phải thỏa:
>
> ∇f0(x)T(y-x) >= 0 với mọi y ∈ feasible set X, tức với mọi y ≽ 0. Và
> dĩ nhiên là x phải feasible x ≽ 0.
>
> Thế thì ∇f0(x)T(y-x) >= 0 <=> ∇f0(x)Ty - ∇f0(x)Tx >= 0
>
> Thế thì xét ∇f0(x)Ty, = Σ ∇f0(x)_i * y_i , và y ≽ 0 nên y_i >= 0 
> Vậy thì nói cái này Σ ∇f0(x)_i * y_i unbound below trừ khi ∇f0(x) >= 0
>  là vì nếu chỉ cần một phần tử của ∇f0(x) âm (ví dụ ∇f0(x)_j , thì cái tích 
> ∇f0(x)_j y_j sẽ âm và khi y_j càng lớn thì càng nhỏ (âm) dẫn đến chỉ
> cần chọn y với y_j ngày càng lớn thì ∇f0(x)Ty có thể nhỏ đến -infinity.
>
> Do đó nếu muốn ∇f0(x)Ty - ∇f0(x)Tx >= 0 thì đầu tiên ∇f0(x)Ty phải 
> unbounded below đã, nếu không ∇f0(x)Ty - ∇f0(x)Tx cũng sẽ unbound
> below. Do đó ta phải có ∇f0(x) ≽ 0 (1)
>
> Rồi,∇f0(x)Ty - ∇f0(x)Tx >= 0 <=> ∇f0(x)Ty >= ∇f0(x)Tx  (2)
>
> mà ∇f0(x) ≽ 0, y ≽ 0 nên ∇f0(x)Ty >= 0 (scalar).
>
> Do đó (2) <=> ∇f0(x)Tx <= 0 hay - ∇f0(x)Tx >= 0 (3)
>
> Rồi vậy là ta có các điều kiện:
>
> x ≽ 0, ∇f0(x) ≽ 0 thì ∇f0(x)Tx <= 0 chỉ có thể <=> ∇f0(x)Tx = 0
>
> Và từ đó ta có kết quả là Σ ∇f0(x)_i * x_i = 0
>
> và again, vì x ≽ 0, ∇f0(x) ≽ 0 nên xi >= 0, ∇f0(x)_i >= 0 
>
> Vậy điều kiện lại trở thành ∇f0(x)_i * x_i = 0 với mọi i
>
> VÀ CÁI NÀY GỌI LÀ COMPLEMENTARY (tạm dịch là "bù trừ cho
> nhau") lí do đơn giản là, vì ∇f0(x)_i không âm, x_i cũng không âm
> nên để hai thằng nhân nhau bằng không thì ít nhất một thằng
> bằng 0. Kết quả là vector ∇f0(x) và vector x sẽ có cái kiểu là thằng
> này bằng 0 thì thằng kia khác 0 hoặc cả hai đều bằng 0

<br>

<p align="center"><kbd><img src="assets/img_fnb052r.png" width="80%"></kbd></p>

> [!NOTE]
> Đại khái là gs nói thêm về equivalent convex problem mà đã nhắc
> đến hồi nãy. Ý tưởng là giả sử ta có convex optimization problem
> này trong đó như đã nói equalities sẽ là các affine function và có
> thể thể hiện chúng bởi Ax = b
>
> Thế thì ý chính ở đây là có thể chuyển nó thành bài toán tương
> đương trong đó ta bỏ đi cái equalities. Bằng cách thay x = Fz
> + x0
>
> Với F và x0 được tạo ra sao cho Ax = b <=> x = Fz + x0
>
> Cái này đơn giản là vầy: Bài toán gốc, equalities constraint của nó
> về cơ bản mang ý nghĩa là "x phải là solution của Ax = b"
>
> Thế thì ta biết Ax = b có thể có vô số nghiệm với dạng tổng quát
> là x_particular + x_null: trong đó ở đây gs ghi x0 và Fz
> chính là cái này x0 là x_particular: Ax0 = b. Còn x_null, hay Fz
> là nullspace vector của A: F là matrix các columns là nullspace
> basis nên Fz là một linear combination của nullspace basis = một
> nullspace vector
>
> để rồi AFz = 0 Dẫn tới A(Fz+x0) = AFz + Ax0 = 0 + b = b tức Fz+x0
> là solution của Ax=b
>
> Để rồi việc solve bài toán tương đương trong đó ta minimize
> over z f0(Fz+x0) với inequalities fi(Fz+x0) <= 0 thực chất vẫn là
> đang tìm trong số solution của của Ax=b xem cái nào thỏa
> inequalities constraint và  minimize f0
>
> EQUIVALENT CONVEX PROBLEM

<br>

<p align="center"><kbd><img src="assets/img_tzys8j7.png" width="80%"></kbd></p>

> [!NOTE]
> Bởi lẽ nếu có solution Ax=b thì x0 (x_particular) là unique.
>
> Nên có tìm là tìm x_null (ý là thay đổi để thỏa các inequalities
> constrains và minimize f0)
>
> Gs nói thêm nếu b không nằm trong range của A (chính là C(A))
> thì sao thì khi đó như đã biết, sẽ ko tồn tại x_particular, hay x0.
> Khi đó chỉ việc return kết quả là: ko có feasible set.
>
> Một điểm nữa đó là sở dĩ bài toán convex tương đương là
> bởi f0(Fz + x0) chính là convex function bởi f0 convex, và
> đây là case "convex function precompose with an affine
> function" (cho nên nó cũng convex)

<br>

<p align="center"><kbd><img src="assets/img_b9t15tk.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_qmg57n.png" width="80%"></kbd></p>

> [!NOTE]
> Cái này trong bài đã nói rất rõ rồi. Nói chung là vì đối với bài toán
> convex optimization problem thì equality constraint là affine Ax = b
> cho nên ta có thể dùng phương pháp tạo equivalent problem
> theo cách tiếp cận là thay x = x0 + Fz vào f0(x), fi(x) < 0
>
> 4.2 CONVEX OPTIMIZATION PROBLEMS
>
> 4.2.4 EQUIVALENT CONVEX PROBLEMS

<br>

<p align="center"><kbd><img src="assets/img_1865ut7.png" width="80%"></kbd></p>

> [!NOTE]
> ngược lại với loại bỏ các equalities constraint là ta sẽ thêm vào
> chuyển thành bài toán tương đương nhưng thêm vào equalities
> constraints. Cái này nghe khá silly như gs cho biết vài bữa ta
> sẽ thấy nó rất hữu ích
>
> Cái dưới ko hiểu lắm nhưng dù sao đây là biết sơ, vài bữa ta sẽ
> đi sâu

<br>

<p align="center"><kbd><img src="assets/img_qcrx91k.png" width="80%"></kbd></p>

> [!NOTE]
> Những cách thức khác thì trong phần nói về equivalent problem thì
> đã biết rồi. Có nghĩa là những cách thức này áp dụng cho các bài
> toán cả convex hoặc không convex.
>
> Chỉ có điều yêu cầu là nếu dùng cách introduce thêm equality
> constraint thì để vẫn là convex problem thì equality constraint function
> phải là affine.

<br>

<p align="center"><kbd><img src="assets/img_n1wb2mq.png" width="80%"></kbd></p>

> [!NOTE]
> cái epigraph form chưa hiểu lắm, nhưng quay lại sau.
>
> Còn cái ở dưới đại khái là nếu ta có thể minimize f0(x1,x2) over x2 
> trước để có f~0(x1). Đây là giá trị của f0(x1,x2) nhỏ nhất khi ta tìm kiếm
> các x2.
>
> Khi đó việc giải bài toán là tìm x1 để f~0(x1) nhỏ nhất sẽ cũng là giải
> bài toán ban đầu (tìm x1, x2 khiến minimize f0(x1,x2))
>
> Gs nói đây là nguyên lý của dynamic programming

<br>

<p align="center"><kbd><img src="assets/img_ufqzcmd.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_9ufi3.png" width="80%"></kbd></p>

> [!NOTE]
> QUAY LẠI SAU

<br>

<p align="center"><kbd><img src="assets/img_4npnik8.png" width="80%"></kbd></p>

> [!NOTE]
> gs nói sơ về bài toán Quasiconvex optimization. Trong đó ta có
> f0(x) (objective function) chỉ quasi-convex chứ không convex. Và
> ta có thể có locally optimal points chứ không phải global
> optimal.
>
> (nhớ lại rằng, với convex optimization, nói rằng local optimal cũng
> sẽ là global optimal, nhưng với quasi-convex optimization problem
> thì không)

<br>

<p align="center"><kbd><img src="assets/img_4jo4pj4.png" width="80%"></kbd></p>

> [!NOTE]
> QUAY LẠI SAU
>
> 4.2 CONVEX OPTIMIZATION PROBLEMS
>
> 4.2.5 QUASICONVEX OPTIMIZATION

<br>

<p align="center"><kbd><img src="assets/img_9vkop4m.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_mggb9o.png" width="80%"></kbd></p>

> [!NOTE]
> QUAY LẠI SAU

<br>

<p align="center"><kbd><img src="assets/img_xypbe8j.png" width="80%"></kbd></p>

> [!NOTE]
> mấy phút cuối gs nói sơ về việc ta có thể giải bài
> toán này. CHưa hiểu lắm

<br>

<p align="center"><kbd><img src="assets/img_k67regl.png" width="80%"></kbd></p>

<br>

