# 2.3 Gaussian Distribution

📊 **Progress:** `11` Notes | `15` Screenshots

---
<a id="node-205"></a>

<p align="center"><kbd><img src="assets/2656ed6afa45bb14b906417a3953011818e62c23.png" width="100%"></kbd></p>

> [!NOTE]
> Phần này ta sẽ nói về Gaussian (hay Normal distribution), là distribution khá
> quan quen thuộc sau khi học xong Stat110 và Casella. Công thức của case
> đơn biến hay đa biến thì mình cũng đã đều bíết rồi. Đặc biệt trong chap 1
> mình đã derive lại công thức Normal đa biến để hiểu công thức 2.43 rồi.
>
> Thế thì gs nói đây là distribution hay dùng, và nó xuất hiện trong nhiều bối
> cảnh. Ví dụ như trong chap 1 mình đã thấy nó chính là **distribution có
> entropy lớn nhất**.

<br>

<a id="node-206"></a>

<p align="center"><kbd><img src="assets/e3b90f424ad27ff3fce28ed3dfd1ab508f7c28b6.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f3db0f9094505b969dca90fd4db8f11f7017169a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c9bc5a3f2529ba9f754d13311151d5541d41ee9f.png" width="100%"></kbd></p>

> [!NOTE]
> đại khái là gs Bishop nói một trường hợp nữa mà ta thấy sự xuất hiện của
> Normal đó là, Central Limit Theorem, còn nhớ trong Stat110 và Casella,
> theorem này nói rằng, xét một random sample size n X1,X2,...Xn ~ distribution
> có mean μ và variance σ^2 thì sample mean  Xbar sẽ converge in distribution
> về một normal(μ, σ^2/n).
>
> Và hình ảnh minh họa cho thấy, X1, ..Xn là uniform, và người ta plot giá trị của
> sample mean Xbar.
>
> Hiểu như sau. Ban đầu ta sẽ chỉ in Xbar của sample size N=1: tức là lấy
> random sample size N = 1 nhiều lần, mỗi lần tính ra Xbar, và plot ra, khi đó có
> thể thấy distribution của Xbar cũng chỉ là uniform.
>
> Nhưng ta làm vậy với N lớn dần thì sẽ thấy distribution của Xbar dần dần có
> dạng của normal.

<br>

<a id="node-207"></a>

<p align="center"><kbd><img src="assets/a32af000becbe928f1f14c6cef241c45f696363f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/69ada0390dc9ebf5ac451c6349d3731538373cb4.png" width="100%"></kbd></p>

> [!NOTE]
> Đại ý là gs nói rằng phần này ta sẽ cần nhiều kiến thức về matrixmà ông
> có nói đến trong Appendix C. Tuy nhiên ông khuyến khích người học nên
> trở nên thành thạo trong việc biến đổi liên quan đến phân phối Normal với
> các kĩ thuật sẽ nói đến ở đây. Vì như vậy sẽ giúp cho ta có thể hiểu được
> các mô hình phức tạp hơn giới thiệu trong các chương sau.
>
> Đầu tiên ta sẽ xem xét khía cạnh hình học của phân phối Gaussian.
>
> Thế thì, ông nói, đại khái là, phân phối Gaussian sẽ phụ thuộc vào x thông
> qua quadratic form (**x** - **μ**)T Σinv (**x** - **μ**), đặt là Δ^2. Ý ông nói
> vậy có nghĩa là, ta thấy trong pdf của multivariate Normal, thì có thể thấy
> nó phụ thuộc với x thông qua cái cụm này, chỉ vậy thôi. Và cụm này, có
> dạng của zTAz, như đã biết trong MIT 1806, gọi là quadratic form (cũng
> chính là cái mà nếu ta có thể chỉ ra zTAz > 0 với mọi z thì ta sẽ kết luận A
> là positive definite matrix đó).
>
> Rồi, ở đây mình được biết một ý mới, rằng Δ được gọi là Mahalanobis
> distance của **μ** và **x**. Và khi Σ là identity matrix I, thì Δ trở thành (**x**
> \- **μ**)T(**x** - **μ**), dĩ nhiên đây chính là ||**x** - **μ**||^2, là L2 hay
> Eucledean distance của **x** và **μ**.
>
> Cuối cùng, đương nhiên ta cũng hiểu ý cuối, là nếu cái cụm này mà là
> constant, thì dĩ nhiên hàm pdf Gaussian cũng là constant theo **x**.

<br>

<a id="node-208"></a>

<p align="center"><kbd><img src="assets/0377f71510b128161ba7508c06ca3cec4fe3ae75.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì chỗ này gs nói matrix Σ có thể coi như là symmetric (đối xứng), mà
> không mất tính tổng quát vì mọi thành phần bất đối xứng đều bị biến mất
> bởi exponent. Là sao ta?
>
> Sau khi thảo luận với gemini, mình hiểu thế này: Một matrix A được gọi là
> đối xứng khi AT = A (A tranpose, chuyển vị, bằng chính nó). Còn nếu AT =
> \-A thì nó gọi là anti-symmetric matrix.
>
> Thế thì giả sử ta xét một matrix A bình thường (bất kì, bằng cách biến đổi
> chút ta sẽ có: A = (1/2)A + (1/2)A
>
> = (1/2)A + (1/2)AT + (1/2)A - (1/2)AT
>
> = (1/2)(A + AT) + (1/2)(A - AT)
>
> Khi đó ta có (1/2)(A + AT) là matrix đối xứng, vì (1/2)(A + AT)T = (1/2)(AT +
> A) = (1/2)(A + AT)
>
> Còn (1/2)(A - AT) là matrix anti-symmetric vì (1/2)(A - AT)T = (1/2)(AT
> \- A) = -(1/2)(A - AT)
>
> Như vậy có thể hiểu mọi matrix Σ bất kì đều có thể thể hiện bởi tổng của
> một matrix symmetric và một matrix antisymmetric.
>
> Thế thì như vậy, nếu ta xét Σ trong Gaussian là matrix bất kì, thì cái cụm
> quadratic form sẽ trở thành (**x** - **μ**)T Σinv (**x** - **μ**)
>
> = (**x** - **μ**)T [Σinv_sym + Σinv_asym] (**x** - **μ**)
>
> = (**x** - **μ**)T Σinv_sym (**x** - **μ**) + (**x** - **μ**)T Σinv_asym (**x** -
> \**μ**)
>
> Xét hạng tử thứ hai:
>
> (**x** - **μ**)T Σinv_asym (**x** - **μ**)
>
> như đã biết, quadratic form thì là một scalar, nên:
>
> (**x** - **μ**)T Σinv_asym (**x** - **μ**) = [(**x** - **μ**)T Σinv_asym (**x** -
> \**μ**)]T
>
> ⇔ (**x** - **μ**)T Σinv_asym (**x** - **μ**) = (**x** - **μ**)T (Σinv_asym)T
> (**x** - **μ**)
>
> ⇔ (**x** - **μ**)T Σinv_asym (**x** - **μ**) = (**x** - **μ**)T (-Σinv_asym) (**x**
> \- **μ**)
>
> ⇔ (**x** - **μ**)T Σinv_asym (**x** - **μ**) = -(**x** - **μ**)T (Σinv_asym) (**x**
> \- **μ**)
>
> Như vậy, nếu coi vế trái là c thì ta có c = -c, suy ra c = 0.
>
> Vậy (**x** - **μ**)T Σinv_asym (**x** - **μ**) = 0
>
> ⇨ (**x** - **μ**)T Σinv_sym (**x** - **μ**) + (**x** - **μ**)T Σinv_asym (**x** -
> \**μ**)
>
> = (**x** - **μ**)T Σinv_sym (**x** - **μ**)
>
> Do đó, dù có xét Σ có không đối xứng thì quadratic form (**x** - **μ**)T Σinv
> (**x** - **μ**) cũng chỉ còn lại phần đối xứng của nó. Thành ra gs mới nói là
> ta coi Σ là matrix đối xứng mà không sợ mất tính tổng quát (loss of
> generality)

<br>

<a id="node-209"></a>

<p align="center"><kbd><img src="assets/5adf6b91640990663f2e772dd21004b5b908e607.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp theo, nhờ MIT 1806 cũng như kiến thức về đại số tuyến tính mà gs Bishop cung cấp ở
> Appendix C, ko có gì khó hiểu ở đoạn này. Là như vầy:
>
> Như đã biết, nếu gọi ui và λi, i = 1,....D là các eigenvector và eigenvalue tương ứng của Σ, thì vì
> định nghĩa của eigenvector/value, ta có Σui = λiui.
>
> Nhưng với Σ, là matrix số thực, và đối xứng thì ta cũng biết rằng nó có tính chất đặc biệt hơn đó là
> mọi eigenvalue sẽ đều là số thực, và tồn tại, có thể chọn một bộ eigenvector orthogonal, và bộ
> vector này đương nhiên là độc lập nhau, nhưng hơn thế nữa, nó còn đủ số lượng (theo cách nói
> của gs Strang trong MIT 1806: matrix đối xứng A shape nxn, luôn có đủ n eigenvector độc lập, và
> điều này có nghĩa là chúng sẽ đủ sức tạo một basis của R^n) để tạo một basis của R^D, hay, nói
> cách khác: span được toàn bộ R^D. Và cũng nên tự hiểu là chúng được normalize để có unit norm
> (length = 1), để vừa orthogonal + unit norm = orthonormal. Tóm lại, với Σ, các eigenvector ui của
> chúng có tính chất:
>
> Unit norm ⇨ ||ui|| = 1, cũng là ||ui||^2 = 1 ⇔ uiTui = 1.
>
> Orthogonal: uiTuj = 0, i ≠ j → đây chính là 2.46
>
> Và như trong MIT18.06 đã học, ta gom ui thành các cột của matrix U thì U là một orthogonal
> matrix: UTU = UUT = I ⇨ UT = Uinv.
>
> Thế thì công thức 2.48 là sao?
>
> Là vầy: Bản chất là từ các equation Σu1 = λ1u1, Σu2 = λ2u2, ...ΣuD = λDuD.
>
> Thì nếu ta gom các u1,...uD thành các cột của matrix U nói trên, và λ1u1, λ2u2,...là các cột của
> matrix V khi đó, dựa vào góc nhìn thứ 3 khi nhân hai matrix AB: cột j của AB = linear combination
> các cột của A bởi bộ hệ số là cột j của B, thì ta sẽ thấy ngay rằng hệ các phương trình trên có thể
> được thể hiện compact bởi: AU = V.
>
> Và tương tự, cũng dựa vào góc nhìn đó, ta sẽ thấy cột j của V, tức λj uj chính là linear combination
> các cột u1,..uD với bộ hệ số là 0,0...1,..0 với số 1 nằm ở vị trí thứ j, Để từ đó có thể thấy V = U
> diag(λ1,..λD), đặt diag(λ1,..λD) = Λ, ta có:
>
> Vậy AU = UΛ, đây chính là identity của phân rã eigenvalue (eigenvalue decomposition).
>
> Rồi, vì UT = Uinv, nên nhân bên phải hai vế cho UT, ta có A = U Λ UT.
>
> Tiếp, với phân tích cái vế phải, theo góc nhìn là nhân hai matrix: (U Λ) với UT theo góc nhìn thứ 4:
> tổng các rank 1 matrix. Theo góc nhìn đó, giả sử ta có AB, thì có thể xem nó là tổng các rank 1
> matrix tạo bởi [cột j của A] outer product [hàng j của B], j = 1,2,...
>
> Nên A = Σj=1:D [cột j của UΛ] outer product [hàng j của UT]
>
> Mà cột j của UΛ chính là λjuj. và hàng j của UT thì cũng là [cột j của U lật ngang lại], tức [cột j của
> U]T, hay ujT. Vậy A = Σj=1:D λjujujT, → 2.48.
>
> (giải thích dài dòng để hiểu bản chất)
>
> Hoàn toàn tương tự với Σinv: Ta dùng kiến thức, nếu u,λ là eigenvector/value của A thì u, 1/λ chính
> là eigenvector/value của Ainv. Nên eigenvalue và vector của Σinv chính là u1, 1/λi, i=1,2...D.
>
> Nên áp dụng lập luận tương tự, ta sẽ thấy Ainv = Σj=1:D ujujT/λj

<br>

<a id="node-210"></a>

<p align="center"><kbd><img src="assets/1fcb8448c5775d5396e953cff67ceebf0da1f8d2.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7dab5b3b3a9d943998871aa93123eb65cfa45c51.png" width="100%"></kbd></p>

> [!NOTE]
> Thay Σinv = Σj=1:D ujujT/λj vào (**x** - **μ**)T Σinv (**x** - **μ**) ta có:
>
> = (**x** - **μ**)T [Σj ujujT/λj] (**x** - **μ**)
>
> = Σj [(**x** - **μ**)TujujT(**x** - **μ**)/λj] | đưa (**x** - **μ**)T và (**x** - **μ**) vào
> trong tổng.
>
> Đặt yj = (**x** - **μ**)Tuj (cũng là ujT(**x** - **μ**) vì cái này là scalar), ta có:
>
> = Σj (yjTyj/λj) = Σj (yj^2/λj) → 2.51
>
> Thế thì với y1 = (**x** - **μ**)Tu1, y2 = (**x** - **μ**)Tu2,...mình có thể thấy: y1 =
> dot product của **x** - **μ** với u1, y2 là dot product của **x** - **μ** với y2,...thì
> với việc gs Bishop đặt U là matrix có các hàng là u1, u2,...để rồi UT là matrix
> có các cột là u1, u2... Thì ta sẽ thấy **y** = (y1, y2...)T chính là U(**x**-**μ**). ⇨
> \**y** = U(**x** - **μ**)
>
> Rồi, chỗ này dùng kiến thức về **change of basis** đã học trong MIT 1806: Ôn
> lại nhanh:
>
> Trong MIT 1806, bài linear transformation, đại khái là mình đã học rằng, một
> phép biến đổi T(.) được gọi là linear transformation là khi nó thỏa mãn: T(c**u**
> \+ d**v**) = cT(**u**) + dT(**v**) (c, d là scalar, u, v là vector) Và vì A(c**u** +
> d**v**) = cA**u** + dA**v**, nên quả thật việc nhân A với vector **x**, chính là
> một phép biến đổi tuyến tính. T(**x**) = A**x**.
>
> Thế thì sau đó gs mới nói về việc, giả sử có một linear transformation T(.), thì
> làm sao xác định matrix A đại diện cho nó? Tức là, giả sử ta có vector **x**
> trong input basis v's, và kết quả T(**x**) trong output basis u's, thì làm sao tìm
> A khiến T(**x**) = A**x**. Câu trả lời là lập luận như sau:
>
> Gọi **v1**,...**vn** là các basis của input space. Thì tọa độ của **x** đang được
> thể hiện theo (linear combination của) basis này, có nghĩa là, **x** = x1**v1** +
> x2**v2** + ...xn**vn** = Σi xi**vi** (x1,x2...là các tọa độ của **x**)
>
> Thế thì, T(**x**), có tọa độ trong output basis T(**x**)1, T(**x**)2,...T(**x**)m:
>
> T(**x**) = Σj=1:m T(**x**)j * **uj**
>
> Và T(**x**) = A**x** = Σi=1:n xi **a**i
>
> ⇨ Σi=1:n xi **a**i = Σj=1:m T(**x**)j * **u**j
>
> vì T(.) là linear transformation, nên T(**x**) = T(Σi=1:n xi**v**i) = Σi=1:n xi
> T(**v**i).
>
> ⇔ Σi=1:n xi **a**i = Σj=1:m { [Σi=1:n xi T(**v**i)]j **u**j }
>
> Xét [Σi=1:n xi T(**v**i)]j có nghĩa là linear combine các T(**v**1), T(**v**2).. với
> hệ số x1,x2.., được một vector, rồi lấy phần tử thứ j của nó. Thì cái này cũng y
> như lấy phần tử thứ j của T(**v**1), T(**v**2),...rồi linearly combine với hệ số
> x1,x2...
>
> ⇨ [Σi=1:n xi T(**v**i)]j = Σi=1:n xi T(**v**i)j
>
> ...⇔ Σi=1:n xi **a**i = Σj=1:m { [Σi=1:n xi T(**v**i)j] **u**j }
>
> Tiếp, xét cụm [Σi=1:n xi T(**v**i)j] **u**j ở bên trong tổng j. ta có thể đưa uj vào
> trong tổng i, vì nó chỉ là thừa số chung:
>
> ⇨ [Σi=1:n xi T(**v**i)j] **u**j = Σi=1:n [xi T(**v**i)j **u**j]
>
> ...⇔ Σi=1:n xi **a**i = Σj=1:m { [Σi=1:n xi T(**v**i)j **u**j] }
>
> Tiếp, ta đang có dạng Tổng j của tổng i, có quyền swap hai dấu tổng:
>
> ...⇔ Σi=1:n xi **a**i = Σi=1:n { Σj=1:m [xi T(**v**i)j **u**j] }
>
> Đến đây xét cái tổng Σj=1:m [xi T(**v**i)j **u**j], có quyền đưa xi ra ngoài:
>
> ⇔ Σi=1:n xi **a**i = Σi=1:n xi { Σj=1:m [ T(**v**i)j **u**j] }
>
> Như vậy tới đây có thể suy ra:
>
> ⇨ **a**i = Σj=1:m T(**v**i) **u**j
>
> Và từ đó ta có quy tắc xây dựng matrix A đại diện cho phép biến đổi tuyến tính
> T(**x**) từ **x** trong input space basis **v**'s sang T(**x**) trong output space
> basis **u**'s:
>
> Biến đổi các basis **v**i's và thể hiện chúng trong tọa độ basis **u**'s. Khi đó
> tọa độ của T(**v**1),..T(**v**n) chính là là hệ số các cột của A.
>
> Từ đó ta xét phép biến đổi identity: Tức T(**x**) = **x**:
>
> Vì đã nói cột i của A là tọa độ của T(**v**i) trong basis u's, nên:
>
> T(**v**i) = linear combination các **u**1,...**u**m bởi các hệ số là cột i của A,
> đặt U là matrix các cột **u**1,..**u**m thì ta có T(**v**i) = U [cột i của A]
>
> Xét phép biến đổi identity: T(**v**i) = **v**i. Ta có:
>
> \**v**i = U[cột i của A], i = 1,..n
>
> Gom **v**1, **v**2...**v**n thành các cột của V, thì **v**i = U[cột i của A], i = 1,..
> n chính là V = UA
>
> Và nhân hai vế cho Uinv: UinvV = A, đây chính là công thức của "change of
> basis" / matrix chuyển cơ sở từ cơ sở v's sang cơ sở u's: A = UinvV.
>
> Xét một case đặc biệt, khi input basis là standard basis: **v**1, **v**2,... =
> \**e**1, **e**2,...Hay cũng là V = I. Ta sẽ có:
>
> A = Uinv I = Uinv. Từ đây giúp kết luận, khi có **x là vector có tọa độ trong
> standard basis**, thì A**x** = Uinv **x**, chính là động tác tính ra tọa độ của nó
> trong basis **u**'s.
>
> Rồi, quay lại công thức y = U(**x**-**μ**):
>
> Đầu tiên chú ý là trong phần ôn lại ở trên, mình nói U là vector tạo bởi các
> \**cột** là các basis u's.
>
> Còn trong bài này, U ở đây được gs Bishop định nghĩa là là **matrix có các
> các hàng là các orthogonal eigenvector ui**. Như vậy **UT là orthogonal
> matrix**, **có các cột là orthogonal eigenvector ui.** Và với orthogonal matrix Q
> thì QT = Qinv, nên (UT)T = UTinv ⇔ U = (UT)inv
>
> ⇨ y = U(**x**-**μ**) = (UT)inv(**x**-**μ**)
>
> Và phần ôn lại ở trên giúp ta hiểu rõ bản chất của cái này chính là:
>
> \**CHUYỂN TỌA ĐỘ CỦA** **x (SAU KHI SHIFT BỞI μ) TỪ CƠ SỞ CHUẨN
> (BASIS e's) SANG HỆ TỌA ĐỘ CƠ SỞ LÀ CÁC CỘT CỦA UT, CHÍNH LÀ ui =
> CÁC EIGENVECTOR CỦA Σ!**
>
> Hơn nữa, với UT là orthogonal matrix,  (để rồi U = (UT)inv) thì UTU = UT
> (UT)inv = I, điều này cho thấy U cũng là orthogonal matrix. Và ta biết với
> orthogonal matrix, thì phép biến đổi bởi nó thực chất là phép xoay trục.
>
> Như vậy có 2 ý quan trọng cần hiểu rút ra từ phân tích trên:
>
> i) y = U(**x**-**μ**) = (UT)inv(**x**-**μ**) có bản chất là: **chuyển tọa độ của
> (x-μ) từ basis e's sang basis tạo bởi các cột của UT, chính là các vector ui, là
> eigenvector của Σ**.
>
> ii) Và UT là orthogonal matrix thì U cũng vậy, nên đây cũng là **phép xoay hệ
> trục tọa độ**.
>
> Gom lại hai ý này, ta sẽ hình dung **bản chất chỉ là tính lại tọa độ của x-μ bằng
> cách xoay trục tọa độ thẳng góc với các eigenvector của Σ.**

<br>

<a id="node-211"></a>

<p align="center"><kbd><img src="assets/10cd1967d9775747fbcab64a80b00cf386020a34.png" width="100%"></kbd></p>

> [!NOTE]
> Nhờ việc phân tích ở note trước, ta có thể hiểu đoạn sau: Đại ý là như
> trước đây đã nói, pdf của multivariate Gaussian sẽ phụ thuộc **x chỉ
> thông qua cái cụm quadratic form (x-μ)T Σinv (x-μ), nên dĩ nhiên tập
> hợp các điểm x trong input space sao cho cụm này bằng constant, thì
> tương ứng sẽ chính là những điểm có cùng mật độ xác suất pdf.**
>
> Thế thì xét một tập hợp như vậy: (**x**-**μ**)T Σinv (**x**-**μ**) =
> constant c, thì như vừa nói sẽ tương ứng với một level set (tập các
> điểm của f(**x**|**μ**, **Σ**), hay N(**x**|**μ**, **Σ**)), câu hỏi đặt ra là
> nó có hình dạng thế nào.
>
> Thế thì như note trước, (**x**-**μ**)T Σinv (**x**-**μ**) = constant c
>
> ⇔ Σj (yj^2/λj) = c
>
> Ta sẽ xét trong case 2 chiều, tức D=2, **x** là vector (x1,x2)T, nó sẽ là:
>
> y1^2 / λ1 + y2^2 / λ2 = c
>
> Còn nhớ cấp hai đã học, phương trình của đường ellips trong mặt
> phải xOy là x^2/a^2 + y^2/b^2 = 1. (a, b gọi là độ dài bán trục lớn và
> nhỏ). Thì chia hai vế cho c, (1) ⇔ y1^2 / cλ1 + y2^2 / cλ2 = 1.
>
> Cho thấy **level set này chính là một hình elipse**.
>
> y là tọa độ của x-μ trong hệ trục tọa độ eigenvector u1, u2.
>
> Vậy ọa độ của tâm ellipse, là 0,0 trong hệ trục này, chính là ứng với
> điểm nào trong hệ tọa độ gốc (basis e's)?
>
> Dùng công thức chuỷển ngược lại thôi: Nãy ta dùng (UT)inv để
> chuyển từ basis e's về basis eigenvector u's thì ((UT)inv)inv = UT sẽ
> chuyển ngược lại: đương nhiên UT**0** (ý là U tranpose nhân vector
> zero **O**) cũng bằng **0**, Nhưng sau đó ta sẽ phải shift lại: + **μ**: 0
> \+ **μ** = **μ** Vậy, tâm của ellipse chính là tại **x** = **μ** trong hệ tọa
> độ ban đầu.
>
> Còn trục của ellipse? Như đã nói, chính là hai vector u1, u2.
>
> Tóm lại, đường đồng mức của Gaussian (level set, nơi có giá trị hàm
> pdf bằng nhau) trong case 2D, sẽ chính là một đường elipse có trục
> trùng với phương của các eigenvector của Σ, và tâm thì nằm tại **μ**
>
> Khái quát lên n-D, nó là ellipsoid trong không gian n chiều, cũng có
> tâm tại μ và trục trùng với eigenvector.
>
> Trong hình 2.7, gs vẽ level set với của pdf với level ứng với exp(-1/2)
> (chú ý, tự hiểu là giá trị pdf là [hằng số gì đó (normalizing constant)]
> exp(-1/2), chứ ko phải pdf = exp(-1/2) nhé)
>
> Ta có exp {-[y1^2 / λ1 + y2^2 / λ2]} = exp(-1/2)
>
> (chú ý, đầu giờ chỉ nói đến cái cụm quadratic form nhưng khi bỏ vào
> exp() của hàm pdf của Normal thì trước cái cụm quadratic form phải
> có dấu trừ)
>
> ⇔ -{y1^2 / λ1 + y2^2 / λ2} = -1/2
>
> ⇔ y1^2 / (λ1/2) + y2^2 / (λ2/2) = 1
>
> và ông vẽ cái đường màu đỏ chính là hình ellipse với a = λ1/2, b =
> λ2/2

<br>

<a id="node-212"></a>

<p align="center"><kbd><img src="assets/1a853b7e95944c1e33a58e664f59113cdf6176dc.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp, đại ý là, covariance matrix của phân phối multivarate Normal, tức Σ có một
> đặc điểm nhằm đảm bảo rằng phân phối này được define đúng (**well
> defined**). Đó là **mọi eigenvalues của Σ đều dương.**
>
> \**Vì sao**? Ở đây có một ý rất hay mà gs Bishop không nói kĩ: Như trong note
> trước, ta đã hiểu cái level set (đường đồng mức của hàm 2D Gaussian là một
> đường ellipse) ứng với exp(-1/2) có tâm tại **μ** và có trục ellipse theo phương
> của các eigenvector với độ dài bán trục là λ1/2 và λ2/2.
>
> Thì như vậy ta sẽ nhận thấy một sự thật rằng: λi chính là phản ánh **mức độ
> phân tán** (**spreading**) **của pdf theo phương eigenvector** **u**i, và đó
> chính là gì: và như vậy, nó phản ánh **variance theo phương u**i.
>
> HIểu nôm na về mặt hình học là vậy, còn ta sẽ **lập luận lại từ định nghĩa của
> Covariance matrix**:
>
> Ở đây tạm quay lại kí hiệu chuẩn toán với việc dùng **X viết hoa** để chỉ
> random variable vector **X**. (**μ**, hay **u** thì cũng là vector như là vector
> fixed value, không phải random variable)
>
> Theo định nghĩa, Σ = Cov(**X**, **X**) = E[(**x** - **μ**)(**x** - **μ**)T]
>
> (covariance của hai random variable X, Y: Cov(X,Y) = E[(X-EX)(Y-EY)])
>
> Thế thì ta gọi λ và **u** là eigenvalue và eigenvector của Σ, ta có Σ**u** = λ**u**.
>
> ⇔ **u**TΣ**u** = **u**Tλ**u** (nhân trái hai vế cho **u**T (**u** transpose))
>
> ⇔ **u**TΣ**u** = λ**u**T**u** (λ là scalar, move tự do)
>
> ⇔ **u**TΣ**u** = λ (vì ta đang luôn làm việc với bộ eigenvector orthogonal và
> unit norm → **u**T**u** = ||**u**||^2 = 1)
>
> ⇔ **u**T E[(**X**-**μ**)(**X**-**μ**)T] **u** = λ
>
> Thế thì E[...] là kì vọng là liên quan đến random variable vector **X**, nên **u**
> chỉ là vector fixed value, hay constant, đưa vào kì vọng nhờ tính linearity: E[cX]
> = cE[X]
>
> ⇔ E[**u**T(**X**-**μ**)(**X**-**μ**)T**u**] = λ
>
> Tới đây, ta đặt Z = (**X** - **μ**)T**u ⇨** E[ZTZ] = E[Z^2] = λ
>
> Vậy λ = E[Z^2] Và từ đây suy ra hai thứ:
>
> Nhưng trước tiên cần hiểu Z **cũng là một random variable** (scalar, ko phải
> random vector). Z = (**X**-μ)T**u**, chính là áp hàm g(**x**) = (x-μ)Tu lên
> random variable vector **X**, đương nhiên, theo Stat110, thầy Joe đã luôn nhắc
> ta khi áp một hàm số lên một random variable (vector) ta luôn được một random
> variable (vector) mới), do đó ta có được random variable scalar Z. Sở dĩ phải
> nói vậy là vì nhờ đó mới bàn tới kì vọng / trung bình của Z: E[Z^2], chứ nếu Z ko
> phải random variable, thì điều này vô nghĩa. Và dĩ nhiên Z^2 cũng lại là một
> random variable, có giá trị không âm
>
> i) Như vậy λ là **trung bình / kì vọng của một biến ngẫu nhiên không âm** nên
> sẽ luôn **không âm**.
>
> ii) Ý thứ hai quan trọng hơn nhiều: λ = E[Z^2], mà Z = (**X** - **μ**)T**u** có bản
> chất hình học là gì?
>
> → Ta biết trong đại số tuyến tính phép tích vô hướng aTb chính là ||a|| ||b||
> cos(a,b), và nếu b là unit vector q, thì aTq chính là hình chiếu của a lên q, có giá
> trị là tọa độ của a theo trục q. Như vậy ở đây u là unit vector. Chính là **hình
> chiếu** của (**x**-**μ**) lên trục tọa độ là **eigenvector** **u**.
>
> Và thật ra ta đã có cùng kết luận này từ trong note trước, khi ta làm phân tích
> cái quadratic form (**x**-**μ**) Σinv (**x**-**μ**) = Σi (yiTyi/λi) = Σi yi^2/λi với yi =
> uiT(**x**-**μ**), cũng là vector **y** = U(**x**-**μ**). Thì ta đã hiểu ý nghĩa của cái
> này chính là chuyển tọa độ **x** bằng cách dời hệ trục về gốc tại **μ**, sau đó
> xoay hệ trục để trùng với các eigenvector ui. Nên y1, y2,...chính là tọa độ của x
> trong hệ trục mới: tâm tại mu, trục trùng với eigenvector **u1**, **u2**,..Mà điều
> này dĩ nhiên có nghĩa là y1 chính là hình chiếu của vector **X** - **μ** lên trục
> \**u1**, y2 là hình chiếu của vector **X** - **μ** lên trục **u2**,...Cùng chính là
> cùng kết luận ở trên.
>
> Xét tiếp EZ = E[(**X**-μ)T**u**] = E[**X**-μ]T**u** = (E**X**-E**μ**)T**u** =
> (**μ**-**μ**)T**u** = **0**T**u** = 0.
>
> Như vậy E[Z^2] thật ra chính là E[Z^2 - (EZ)^2] và đây chính là **VARIANCE**
> của **Z:** Var(**Z**). Và với ý nghĩa của Z là hình chiếu của (**X** - **μ**) lên trục
> eigenvector **u**, thì như vậy ta có thể hiểu vì sao E[Z^2], **CŨNG LÀ**
> \**EIGENVALUE** **λ**, **CHÍNH LÀ PHƯƠNG SAI CỦA DISTRIBUTION THEO
> PHƯƠNG EIGENVECTOR** **u**, và dĩ nhiên, again, phương sai thì không âm
> cũng giúp khẳng định lại λ phải không âm.
>
> Rồi, ở trên ta đã hiểu λi của Σ chính là phương sai của distribution theo phương
> eigenvector ui, và do đó nó phải không âm. Nhưng thậm chí nó phải dương
> luôn. Lí do có thể tạm hiểu nhanh là vì trong công thức pdf của Normal, Σ xuất
> hiện ở dạng inverse Σinv. Mà để invertible, thì Σ phải non-singular / full-rank. Do
> đó mọi eigenvalue phải khác 0.
>
> Và như vậy, từ MIT 1806 (cũng như phần Appendix C đã nhắc lại), mọi
> eigenvalues dương là một trong những cách để check điều kiện matrix là một
> positive definite matrix (bên cạnh các cách khác như check quadratic form,..)
>
> Gs cũng nói trong chap 12 ta sẽ làm việc với một phân phối Normal có
> covariance không đảm bảo mọi eigenvalue đều dương, mà chỉ không âm thôi,
> khi đó chỉ là positive semi definite. Và, nếu có eigenvalue = 0, thì matrix Σ sẽ
> singular. Vì sao singular, singular là sao?
>
> Ôn lại kiến thức trong MIT 18.06: singular là khi matrix tồn tại nonzero vector
> trong nullspace hoặc left nullspace. Khi đó vector khác 0 đó sẽ bị biến thành 0
> bởi matrix. Thế thì, nếu tồn tại eigenvalue bằng 0, thì như đã biết, nếu λ và u là
> eigenvalue và eigenvector tương ứng, thì ta có Au = λu, vậy nếu λ = 0, thì u
> chính là vector bị biến thành 0 bởi A: Au = 0u = 0. Nên nó chính là non-zero
> vector trong nullspace, như vậy nullspace có dimension khác 0, cũng đồng
> nghĩa các cột của A không độc lập, cũng đồng nghĩa luôn là rank của A nhỏ hơn
> số hàng số cột, và matrix A không full-rank, không invertible, hay và gọi là matrix
> suy biến (singular).

<br>

<a id="node-213"></a>

<p align="center"><kbd><img src="assets/b8dfc5ea493c66b54c4fd51c4e882552dc1f976a.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì tiếp theo gs nói là ta sẽ xem xét dạng của Gaussian trong hệ trục tọa độ
> mới. Là sao?
>
> Có nghĩa là, như đã hiểu khi ta ôn lại kiến thức change of basis matrix trong MIT
> 1806 ở note trước, việc ta đặt **y** = U(**x**-**μ**) chính là = (UT)inv(**x**-**μ**), có
> bản chất là ta đã chuyển hệ trục tọa độ về gốc tọa độ mới là **μ** và trục tọa độ bây
> giờ là các eigenvector, và một điểm có tọa độ **x** trong hệ trục gốc (tức basis **e**'
> s) bây giờ sẽ có tọa độ **y** trong basis **u**'s.
>
> Và trong bối cảnh ở đây là hàm pdf, thì ta lại liên hệ với kiến thức đã học trong
> Stat110: **Change of variable**: Ôn lại nhanh: Khi ta có random variable X ~ fX(x), và
> áp dụng hàm g(x) lên nó để có một random variable mới: Y = g(X) sao cho ta có
> mapping 1-1 giữa x belong range X và y belong range Y, đồng nghĩa nếu y = g(x) ⇔
> x = ginv(y), thì ta sẽ có theorem cho phép xây dựng pdf của Y: 
>
> fY(y) = fX(x) |dx/dy| = fX(ginv(y) |d/dy ginv(y)|.
>
> Sau đó, tương tự, khái quát lên cho random variable **VECTOR**: **X**, và **Y** =
> g(**X**) thì f**Y**(**y**) = f**X**(**x**) |d**x**/d**y**| = f**X**(**x**) |d/d**y** ginv(**x**)|.
>
> Lúc này với việc **y** = g(**x**) và ginv(**y**) là vector → vector function, nên đạo
> hàm của ginv(y) đối với y sẽ là gì: Theo kiến thức đã học trong MIT 18s096, đó sẽ là
> một matrix, có mỗi hàng là một gradient vector: hàng i sẽ là vector các partial
> derivative của xi = ginv(y)_i (phần tử thứ i của vector **x**) đối với vector **y:**
> (∂xi/∂y1, ∂xi/∂y2,....).
>
> Và matrix này gọi là Jacobian matrix, nên với case này thì change of variable
> theorem, ta có: f**Y**(**y**) = f**X**(**x**) |J| (thật ra là | |J| |, hay |det(J)| với ý nghĩa:
> giá trị tuyệt đối của determinant của matrix Jacobian).
>
> Thế thì quay lại đây (sách Bishop), chính là ta đang đối mặt với bài toán đổi biến
> (change of variables), khi ta có **X** (hay gs Bishop viết thường **x**, như nói nhiều
> lần, gs Bishop viết thường đối với tên biến có thể gây lú lẫn), có pdf là hàm
> Gaussian pdf f**X**(**x**|**μ**, Σ) = (công thức 2.43). Và nay ta có random variable
> vector **Y có được bằng cách áp hàm g(x) lên X, với g(x) =** U(**x**-**μ**), tức là
> \**Y** = U(**X** - **μ**). Vậy thì áp dụng điều trên ta sẽ có pdf của **Y**:
>
> fY(y) = f**X**(**x**|**μ**,Σ) |J|
>
> Vậy J, trong trường hợp này, cụ thể nó sẽ là thế nào: Ta có thể theo định nghĩa đã
> nói trên, đi tìm Jij, là ∂xi/∂yj. Nhưng MIT 18s096 cho ta một cách làm dễ hơn nhiều -
> tìm đạo hàm theo lối hoslistically:
>
> Ta có hàm **y** = U(**x** - **μ**) ⇨ **x** = Uinv**y** + **μ**, = g(**y**) nếu có thể chỉ ra
> dg(**y**) = một linear operator của d**y**, thì ta sẽ thấy ngay công thức đạo hàm.
> Làm như sau:
>
> dg = g(**y**+d**y**) - g(**y**) = Uinv(**y** + d**y** + **μ**) - Uinv(**y** + **μ**) =
> Uinvd**y**. Và đây chính là linear operator act on d**y**, nên đơn giản ta kết luận
> ngay d/dy g(**y**), chính là Jacobian = Uinv.
>
> Vậy J = Uinv Nên det J = det Uinv, mà U là matrix gì, còn nhớ, gs Bishop, đã define
> U là matrix mà các hàng là các eigenvector ui của Σ, nên UT là matrix tạo bởi các
> cột là các eigenvector ui, và đám này lại orthogonal, và unit norm. Đồng thời mình
> trong note trước cũng cũng đã nói, với orthogonal matrix thì transpose của nó cũng
> vậy. Như vậy UT là orthogonal matrix, thì U cũng vậy. Và như vậy Uinv = UT (tính
> chất của orthogonal matrix)
>
> Như vậy Jacobian **J chính là UT**, đây chính là **giải thích cho công thức 2.53**: Jij
> = Uji (chú ý thứ tự ij ngược nhau, vì Uji thực chất chính là (UT)ij, nên chính là ông
> đang nói J = UT)
>
> Rồi, thế thì tới đây nếu ta còn nhớ kiến thức trong MIT 1806 sau đây thì có thể kết
> luận luôn |det J| = |det UT| = 1: determinant, hay tiếng việt là định thức, có ý nghĩa là
> gì? là tỉ lệ của thể tích của một khối lập phương cạnh bằng 1 sau khi bị linear
> transform bởi matrix J so với thể tích ban đầu của nó (= 1). Hay trong 2D, thì nó là tỉ
> lệ của diện tích của hình vuông cạnh = 1 sau khi bị tranform bởi J. Thế thì, ta vừa
> nói J (chính là UT) là orthogonal matrix, nên **phép biến đổi tuyến tính bởi J chỉ là
> PHÉP XOAY, nó bảo tồn diện tích**. Thành ra tỉ lệ này dĩ nhiên là 1. ⇨ det J = det
> UT = 1.
>
> Còn trong sách, gs tính det J^2 trước, (det J)^2 = (det UT)^2
>
> = (det UT)(det UT)
>
> = (det UT)(det U) (do det A = det AT)
>
> = det(UT U) (det (AB) = det A) (det B))
>
> = det (I) (do U orthogonal → UTU = I)
>
> = 1.
>
> Vậy (det J)^2 = 1 ⇨ det J = +/-1. Nhưng trong công thức change of variable nói trên,
> như đã nói, thật ra ta lấy trị tuyệt đối của det, nên kết quả là 1.
>
> Như vậy ta hiểu rõ hai công thức 2.53, và 2.54 cũng như đoạn này nói gì.

<br>

<a id="node-214"></a>

<p align="center"><kbd><img src="assets/451973f2796c7d22146e3ebc4a60ef3909661930.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp, thử xem vì sao gs nói |Σ| có thể thể hiện bởi tích các eigenvalues?
>
> Là vì đơn giản đây là công thức của det thôi: det A = tích các eigenvalue của nó. Và vì các eigenvalue của Σ như vừa nói, đều dương nên ta có
> |det Σ| = det Σ = Πi λi.
>
> ⇨ √[det Σ] (hay |Σ|^(1/2) = √[Πi λi] = (Πi λi)^1/2 = Πi λi^1/2
>
> Rồi, như vậy ta đã có đủ nguyên liệu để ráp vào công thức đổi biến để có pdf của **Y** = U(**X** - **μ**):
>
> f**Y**(**y**) = f**X**(**x**|**μ**,Σ) |J| với:
>
> |J| = 1
>
> f**X**(**x**|**μ**,Σ) = công thức 2.43 = [1/(2π)^(D/2)] [1/|Σ|^1/2] exp[-1/2(**x**-**μ**)T Σinv(**x**-**μ**)]
>
> = [1/(2π)^(D/2)] [1/|Σ|^1/2] exp[-1/2(Uinv**y**+**μ**-**μ**)T Σinv(Uinv**y**+**μ**-**μ**)]
>
> = [1/(2π)^(D/2)] 1/[Πi λi^1/2] exp[-1/2(UT**y**)T Σinv(UT**y**)]
>
> = [1/(2π)^(D/2)] 1/[Πi λi^1/2] exp[-(1/2)**y**TU Σinv UT**y**]
>
> Xét cụm này: (1/2)**y**TU Σinv UT**y** (bữa trước ta đã phân tích, gọi nó là Δ^2, và thu gọn nó là thành Σj (yj^2/λj)
>
> Ghi lại đoạn đó: "Thay Σinv = Σj=1:D ujujT/λj vào (**x** - **μ**)T Σinv (**x** - **μ**) ta có:
>
> = (**x** - **μ**)T [Σj ujujT/λj] (**x** - **μ**)
>
> = Σj [(**x** - **μ**)TujujT(**x** - **μ**)/λj] | đưa (**x** - **μ**)T và (**x** - **μ**) vào trong tổng.
>
> Đặt yj = (**x** - **μ**)Tuj (cũng là ujT(**x** - **μ**) vì cái này là scalar), ta có:
>
> = Σj (yjTyj/λj) = Σj (yj^2/λj) → 2.51"
>
> Nhưng ở đây mình có thể làm theo cách khác cũng ra: Xét **y**TU Σinv UT**y**, ta phân tách trị riêng (eigenvalue decomposition) đối với Σinv =
> Q H QT với Q là orthogonal matrix có các cột là eigenvector của Σinv, và như đã biết, Σ và Σinv có chung bộ eigenvector : tức là nếu λ, u là
> eigenvalue, eigenvector của Σ thì 1/λ, u cũng là eigenvalue, eigenvector của Σinv. Nên Q chính là UT. Còn H là diagonal matrix có đường chéo là
> các eigenvalue của Σinv. Vậy thì vì ta đang gọi λ1, λ2,... là các eigenvalue của Σ nên eigenvalue của Σinv là 1/λ1, 1/λ2,. ... ⇨ H chính là
> diag(1/λ1, 1/λ2,...,1/λD). Vậy ta có Σinv = Q H QT = UT diag(1/λ1, 1/λ2,...,1/λD) U.
>
> Thay vào **y**TU Σinv UT**y** = **y**TU UT diag(1/λ1, 1/λ2,...,1/λD) U UT **y**
>
> với U thì ta đã biết UT = Uinv nên biểu thức trên = **y**T diag(1/λ1, 1/λ2,...,1/λD) **y**,
>
> và cái này chính là Σi=1:D yi^2/λi.
>
> Vậy tóm lại, f**Y**(**y**) (trong sách gs Bishop ghi là p(**y**)) là:
>
> [1/(2π)^(D/2)] 1/[Πi=1:D λi^1/2] exp[-(1/2)Σi=1:D yi^2/λi]
>
> = [Πi=1:D[1/(2π)^(1/2)] 1/[Πi=1:D λi^1/2] exp[-(1/2)Σi=1:D yi^2/λi]
>
> = Πi=1:D [1/(2πλi)^(1/2)] exp[-Σi=1:D yi^2/2λi]
>
> = Πi=1:D { [1/(2πλi)^(1/2)] exp[-yi^2/2λi] } (cái tổng trong exp(), tách ra thành tích các exp luôn: e^(a+b) = e^a e^b)
>
> → **Và** **đây chính là 2.56**
>
> Và nhận xét quan trọng đó là: xét một thừa số trong tích:
>
> 1/(2πλi)^(1/2)] exp[-yi^2/2λi]
>
> Có thể thấy, nó chính là công thức pdf của Normal(0, λi), nhớ ko, với normal(μ, σ^2) thì pdf là [1/√(2πσ^2)] exp[-(x-μ)/2σ].
>
> Đến đây ta lập luận như sau: Dùng kiến thức của Stat110 đã học: Xét joint pdf của các random variable X1,X2,...Xn. f**X**(x1,x2,..), nếu có thể
> factor nó thành tích các marginal pdf: fX1(x1)fX2(x2)...fXn(xn). Thì có thể suy ra các random variable X1,X2,...Xn **ĐỘC LẬP**. (independent)
>
> Vậy ở đây, f**Y**(**y**), thật ra chính là joint pdf của D random variable Y1, Y2,... YD (các phần tử của vector **Y**). Và cái công thức 2.57, là
> joint pdf của chúng, như đã thấy, lại chính là tích các marginal pdf của các random variable Y1,Y2.... YD đơn lẻ.
>
> \**NHƯ VẬY KẾT LUẬN: Y1, Y2,....YD LÀ CÁC RANDOM VARIABLE ĐỘC LẬP.**
>
> \**Và ý nghĩa của điểu này chính là: Việc đổi biến, từ X sang Y, bằng cách shift bởi μ và xoay trục sao cho trùng với các eigenvector của Σ đã
> giúp cho trong hệ trục tọa độ mới, các tọa độ trở nên hoàn toàn độc lập nhau. Đây chính là ý mà gs Bishop nói ở đây** "\/eigen- vectors therefore
> define a new set of shifted and rotated **coordinates** with respect to which the joint probability distribution factorizes into a product of
> independent distributions"\/
>
> Ý cuối chỉ là gs nói về việc khi ta marginalizing pdf của **Y** over toàn bộ range **Y**, thì bằng cách đưa tích phân của tích thành tích các tích
> phân, và các tích phân này đều bằng 1 do tính valid của pdf nên kết quả là tích của các số 1, nên bằng 1. Cho thấy pdf của Y là một valid pdf. Ví
> dụ, để dễ hiểu thì ta có thể xét case hai biến Y1,Y2:
>
> ta có f**Y**(**y**) = f**Y**(y1,y2) = Πi=1:2 { [1/(2πλi)^(1/2)] exp[-yi^2/2λi] }
>
> = [1/(2πλ1)^(1/2)] exp[-y1^2/2λ1] [1/(2πλ2)^(1/2)] exp[-y2^2/2λ2]
>
> = f(y1) f(y2).
>
> Và xét tích phân trên toàn bộ range **Y**, trong trường hợp này là toàn mặt phẳng 2D:
>
> ∫-inf:inf∫-inf:inf f**Y**(**y**) d**y** = ∫-inf:inf∫-inf:inf f**Y**(y1,y2) dy1dy2
>
> = ∫-inf:inf∫-inf:inf f(y1) f(y2) dy1dy2
>
> Tính tích phân theo y1 trước, thì vì f(y2) ko dính gì tới y1 nên đưa ra ngoài: = ∫-inf:inf [∫-inf:inf f(y1) dy1] f(y2) dy2 Tíếp, xét tích phân theo y2, thì
> vì [∫-inf:inf f(y1) dy1], ko dính gì đến y2, nên đưa ra ngoài
>
> = [∫-inf:inf f(y1) dy1] [∫-inf:inf f(y2) dy2]
>
> Và mỗi cách tích phân này, theo tính valid của một pdf, nên bắt buộc phải bằng 1.
>
> kết quả là 1 x 1 = 1.

<br>

<a id="node-215"></a>

<p align="center"><kbd><img src="assets/454ccfd42413b86c20daddd95d75917be257649d.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp, có thể hiểu đoạn này là gs nói rằng ta sẽ xem xét các moment của nó. Từ Stat110 mình đã biết, nói về moment, khái niệm moment của distribution, được define như
> sau: moment bậc n là E[X^n]. Và như vậy **moment bậc 1, chính là mean** của distribution, EX. Còn **moment bậc 2**, EX^2, sẽ giúp ta tính **variance** với công thức VarX
> = EX^2 - (EX)^2.
>
> Thế thì dù mình vẫn hay mặc định là nói với X ~ normal(μ, σ^2) thì μ chính là mean EX. Nhưng thực ra phải chứng minh. Như trong Stat110 đã làm, ta sẽ dựa vào định
> nghĩa của kì vọng, để chứng minh mean của Z~ Normal(0, 1) là 0 trước, làm như sau: (đây cũng là ôn lại, nhưng sẽ cho ta thấy cái mà gs Bishop làm ở đoạn này thật ra là y
> chang)
>
> EZ = ∫-inf:inf zfZ(z) dz = ∫-inf:inf z [1/√(2π)] exp(-z^2/2) dz
>
> = [1/√(2πσ^2)] ∫-inf:inf z exp(-z^2/2σ^2) dz (đưa constant ra ngoài tích phân)
>
> Thế thì biểu xét biểu thức trong tích phân, coi nó như hàm g(z) = z exp(-z^2/2σ^2) thì nó là một hàm có tính chất:
>
> g(-z) = -z exp(-(-z)^2/2σ^2) = -z exp(-z^2/2σ^2) = -g(z)
>
> Vậy nó là một hàm lẻ (odd function). Mà với hàm lẻ, khi ta tích phân từ -inf tới inf, thì các giá trị sẽ cancel out nhau (hủy nhau). Nên kết quả là 0.
>
> ⇨ EZ = 0. Và từ đó, dùng location scale theorem, nói rằng nếu ta có Z ~ standard member của một location scale family, thì σZ + μ sẽ là thành viên ứng với location μ và
> scale σ. Với normal, nó là một location scalar family, thành ra theo đó, X = σZ + μ chính là một normal có location μ và scale σ: X ~ normal(μ, σ^2)
>
> Chứng minh cũng dễ: X = σZ + μ = g(Z) ⇨ Z = (X-μ)/σ = ginv(X). Dùng change of variable theorem, tính pdf của X:
>
> fX(x) = fZ(z) |dz/dx| = fZ(ginv(x)) |d/dx ginv(x)|
>
> = fZ((x-μ)/σ) |d/dx [(x-μ)/σ]|
>
> = (1/√2π) exp[-((x-μ)/σ)^2/2] |1/σ|
>
> = (1/√2π) exp[-(x-μ)/2σ^2] (1/σ)
>
> = (1/√2πσ^2) exp[-(x-μ)/2σ^2] → đây chính là pdf của normal(μ, σ^2).
>
> Đến đây ta sẽ dùng linearity để tính EX: EX = E(σZ + μ) = σE(Z) + E(μ) = σ0 + μ = μ. Giúp kết luận với normal(μ, σ^2) thì location μ chính là mean của distribution.
>
> Chú ý, thường thì ta cứ nghe người ta nói rằng nói normal(μ, σ^2) thì mean là μ, variance là σ^2. Tuy nhiên, đó là kết luận, ta phải chứng minh. Và việc chứng minh chính là
> như trên vừa làm: Chứng minh nếu X có pdf là 1/√(2πσ^2) exp[-(x-μ)^2/2σ] thì EX = μ.
>
> Rồi, quay lại đây, cái gs Bishop làm cũng là tương tự, ta có **X** có pdf:
>
> f(**x**) = [1/(2π)^(D/2)] [1/|Σ|^1/2] exp[-1/2(**x**-**μ**)T Σinv(**x**-**μ**)],
>
> ta sẽ phải chứng minh E**X** = **μ**.
>
> Theo định nghĩa của kì vọng:
>
> E**X** = ∫**x**f(**x**)d**x** = ∫**x** [1/(2π)^(D/2)] [1/|Σ|^1/2] exp[-1/2(**x**-**μ**)T Σinv(**x**-**μ**)] d**x**
>
> = [1/(2π)^(D/2)] [1/|Σ|^1/2] ∫**x** exp[-1/2(**x**-**μ**)T Σinv(**x**-**μ**)] d**x**
>
> Tới đây, ông Bishop đổi biến tích phân bằng cách đặt **z** = **x** - **μ** thì thực ra cái ổng làm cũng chính là lặp lại những gì ta làm ở trên, chẳng qua là nó hơi khó để thấy,
> như sau:
>
> Đặt **z** = **x** - **μ ⇨** d**z** = d**x**, và cận của tích phân thì vẫn vậy (vẫn là toàn miền R^D)
>
> Khi đó, E**X** = [1/(2π)^(D/2)] [1/|Σ|^1/2] ∫ (**z**+**μ**) exp[-(1/2) **z**T Σinv **z**] d**z**
>
> = [1/(2π)^(D/2)] [1/|Σ|^1/2] ∫ **z** exp[-(1/2) **z**T Σinv **z**] d**z** + [1/(2π)^(D/2)] [1/|Σ|^1/2] ∫ **μ** exp[-(1/2) **z**T Σinv **z**] d**z**
>
> Xét term thứ nhất, và xét cái cụm ∫ **z** exp[-(1/2) **z**T Σinv **z**] d**z**, ta sẽ thấy mr Bishop dùng lập luận y chang: vì hàm exp[-(1/2) **z**T Σinv **z**] là hàm chẵn, do
> exp[-(1/2) **z**T Σinv **z**] = exp[-(1/2) (-**z**)T Σinv (-**z**)], nên **z** exp[-(1/2) **z**T Σinv **z**] là hàm lẻ. Và vì vậy khi tích phân trên toàn miền sẽ ra 0.
>
> (Chú ý nhé, ông nói "exponent is an even function of the components of z" là đang nói cái cục exp[-(1/2) **z**T Σinv **z**] làm hàm chẵn. nhưng ở ngoài còn thằng **z** nữa,
> nên **z** exp[-(1/2) **z**T Σinv **z**] là hàm lẻ, và khi đó thì tích phân trên toàn miền nó mới bị triệt tiêu (vanish) do tính đối xứng (symmetry))
>
> Nên ông mới nói "\/the term in z in the factor (z + μ) will vanish by symmetry\/" là vậy.
>
> Và hãy nhìn kĩ cái term thứ nhất, [1/(2π)^(D/2)] [1/|Σ|^1/2] ∫ **z** exp[-(1/2) **z**T Σinv **z**] d**z**, ta sẽ thấy nó chính là E**Z**.
>
> Vậy chỉ còn cái term thứ 2: [1/(2π)^(D/2)] [1/|Σ|^1/2] ∫ **μ** exp[-(1/2) **z**T Σinv **z**] d**z**
>
> Để làm tiếp, đưa μ ra ngoài tích phân, thật ra là đưa hẳn ra ngoài luôn
>
> \**μ** { [1/(2π)^(D/2)] [1/|Σ|^1/2] ∫ exp[-(1/2) **z**T Σinv **z**] d**z** }
>
> đưa cái cụm constant vào trong tích phân lại:
>
> \**μ** { ∫ [1/(2π)^(D/2)] [1/|Σ|^1/2] exp[-(1/2) **z**T Σinv **z**] d**z** }
>
> thì lúc này, cái cụm { ∫ [1/(2π)^(D/2)] [1/|Σ|^1/2] exp[-(1/2) **z**T Σinv **z**] d**z** } chính là marginalizing pdf của Z over R^D. nên theo tính valid của pdf, nó phải bằng 1.
>
> Kết quả term 2 bằng **μ**. giúp ta có E**X** = **μ**, giúp chứng minh μ chính là mean của Normal(**μ**, Σ).

<br>

