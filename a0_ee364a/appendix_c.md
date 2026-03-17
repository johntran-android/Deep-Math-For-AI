# Appendix C

📊 **Progress:** `6` Notes | `7` Screenshots | `0` AI Reviews

---
<p align="center"><kbd><img src="assets/img_5ags6ub.png" width="80%"></kbd></p>

> [!NOTE]
> Nói về một số điểm đáng chú ý khi giải một hệ underdetermined: Ax
> = b  với A là matrix lùn mập (nhiều cột hơn hàng) (p,n) với p < n.
>
> Và giả định là A full row rank, tức p hàng đều độc lập (nên dĩ nhiên
> có p cột độc lập, theo MIT 1806 ta đã biết, b sẽ chắc chắn nằm
> trong C(A) nên Ax = b chắc chắn có nghiệm, mà chính xác hơn thì
> nó chắc chắn có vô số nghiệm dạng x_particular + α x_null, vì có
> cột tự do nên sẽ có non-trivial vector trong nullspace)
>
> Thế thì ở đây nói có khi ta chỉ cần một nghiệm, nhưng cũng có khi
> ta cần thể hiện toàn bộ nghiệm, đó chính là x_particular + α x_null
> ở trên, nhưng ta sẽ thể hiện là x^ + Fz với F là matrix các cột là
> basis của N(A) và z là  vector bất kì, đóng vai trò là hệ số để tạo
> linear combination các N(A) basis để tạo ra nullspace vector.

<p align="center"><kbd><img src="assets/img_dnkr9zh.png" width="80%"></kbd></p>

> [!NOTE]
> Thế thì, xét trường hợp mà matrix A mập lùn có p cột đầu tiên cũng độc lập, điều
> này có nghĩa là p cột đầu tiên của nó sẽ tạo một sub matrix (p, p) non-singular / full
> rank (gọi là A1) và (n - p) cột còn lại là dependent columns (tạo matrix A2, singular)
>
> Khi đó Ax = b có thể hiểu / thể hiện theo dạng [A1, A2] [x1, x2]T = b với x1 là R^p
> vector, x2 là R^(n-p) vector. Để rồi b = A1x1 + A2x2 mang ý nghĩa là p phần tử của
> x1 là hệ số của linear combination p cột đầu tiên của A, và x2 là hệ số combine
> linearly n - p cột sau của A, và cộng lại ra b (bản chất Ax là linear combination các
> cột của A)
>
> Thế thì từ A1x1 + A2x2 = b ⇔ A1x1 = b - A2x2
>
> vì A1 non-singular nên có thể nhân hai vế cho A1inv:
>
> x1 = A1invb - A1invA2x2
>
> Từ đây bằng cách chọn x2 = 0 (tương đương chọn n - p component cuối của x = 0)
> thì ta có thể giải tìm x1 = A1invb để có x = [x1, 0] =  [A1invb, 0] là một solution của
> Ax = b (*)
>
> Và việc giải x1 = A1inv b dĩ nhiên với việc ta đang giải bài toán A1x1 = b với A là
> matrix (p, p) nên chi phí tính toán sẽ là chi phí của bài toán này.
>
> ====
>
> Và tổng quát với x1 = A1invb - A1invA2x2, ta có x như vầy:
>
> x = [x1, x2]T = [A1invb - A1invA2x2, x2]T
>
> = [A1invb, I]T + [- A1invA2x2, x2]T
>
> = [- A1invA2x2, x2]T + [A1invb, I]T
>
> = [- A1invA2, I]T x2 + [A1invb, I]T
>
> Và đây chính là gì, chính là dạng tổng quát (complete solution)
>
> x = F z + x^
>
> với x^ là một particular solution = [A1invb, I]T như đã nói ở (*)
>
> và F chính là [- A1invA2, I]T, z chính là x2. Để với các x2 (z) bất kì ta sẽ có Fz là
> nullspace vector của A
>
> Khúc cuối nói rằng nếu ta chi phí factoring A1 LÀ f , GIẢI HỆ A1x = d là s thì tổng
> chi phí sẽ là f + s
>
> Và để parameterizing mọi solution thì cần f + s(n - p + 1)
>
> Là thế này:
>
> Nói chung ta cần làm những việc gì: Đó là tìm F và tìm x^.
>
> Tìm F với F = [-A1invA2, I] thì cơ bản là ta cần tìm -A1invA2
>
> đặt Y = -A1invA2, thì việc tìm Y tương đương với việc giải A1Y = -A2 có nghĩa là ta
> sẽ không tìm A1inv và nhân A1inv với A2 mà sẽ giải A1Y = - A2 để tìm Y.
>
> Và A1Y = -A2 nên hiểu thế nào. theo một trong những góc nhìn matrix x matrix thì
> có thể nhìn theo cách: cột j của -A2 chính là linear combination của các cột của A1
> với coefficient là cột j của Y. Do đó, tìm cột j của Y chính là giải hệ:
>
> A1yj = -[cột j của A2]
>
> Đây là một hệ phương trình tuyến tính, mà để giải nó cần chi phí đã cho biết là s
> (sách ban đầu đã nói chi phí giải hệ A1x = d là s, từ những phần trước C1->C4 mình
> hiểu rằng giải Ax = b theo phương pháp factor - solver, thì bước một là factorize A
> thành LU, hay nếu A có cấu trúc đặc biệt hơn thì ta có thể có các dạng factorizing
> khác tốt hơn, bước này như đã nói sẽ tốn chi phí là f. Bước hai là solver step: khi 
> ta sẽ giải Ax = b ⇔ LUx = b, thì đầu tiên giải Lz = b, với L là lower triangular thì
> đây chính là quá trình forward substitution và sau đó là giải Uz = z, chíng là quá trình
> back-substitution. Và người ta gọi cost của bước solver, tổng hai bước này là s)
>
> Vậy để tìm một cột của Y ta cần tốn s chi phí. Và Y có mấy cột? (n - p) cột ⇨ cần
> (n - p)s chi phí.
>
> Trước đó, việc giải A1x + d sẽ cần một chi phí để factor A1 là d. factor A1 tức là LU
> factorization (MIT 1806 đã học, chính là đưa A về dạng row echelon form U, từ đó
> giúp chuyển Ax = b thành Ux = b', và chỉ việc back-substitution để giải ra x (mà
> bước này chính là bước tốn s chi phí)
>
> Vậy nên ta hiểu rằng một khi đã factorizing A1 (tốn f chi phí) thì sau đó mỗi lần giải
> Ax = d đều chỉ tốn s chi phí.
>
> Vậy nãy h ta tốn f (factorizing A1) + (n - p)s (giải tìm các cột của Y = -A1invA2, cũng
> chính là các cột của F (F = [-A1invA2, I]).
>
> Còn lại một cái phải làm nữa là tìm x^, = [A1invb, 0]. Cũng chính là tìm A1invb, đặt
> y = A1invb thì giải tìm y chính là giải hệ A1y = b. lại tốn thêm một s chi phí (vì A1 đã
> factor một lần)
>
> Vậy tổng cộng tốn f + (n - p)s + s = f + (n - p + 1)s chi phí tính toán

<br>

<p align="center"><kbd><img src="assets/img_1ddtq3j.png" width="80%"></kbd></p>

<p align="center"><kbd><img src="assets/att_5x8g.png" width="80%"></kbd></p>

> [!NOTE]
> Trường hợp thứ hai, khi A không có vụ có p cột độc lập đứng trước
> thì khi đó, ta sẽ chỉ đơn giản là tìm thêm matrix P (permutation
> matrix) để làm công tác sắp xếp lại các cột của A để đưa các cột
> độc lập lên đầu. Sau đó làm như vừa rồi.
>
> Như vậy dễ hiểu rằng ta sẽ có A~ = AP (sau khi permute column) =
> [A1, A2] (là dạng matrix có p cột độc lập đứng đầu)
>
> Thế thì dĩ nhiên áp dụng các bước vừa rồi, sẽ giúp ta có general
> solution của A~x~ = b là:
>
> x~ = [-A1invA2, I] x2~ + [A1invb, 0]
>
> Thế thì đây là solution của A~x~ = b, tức APx~ = b, và x = Px~
>
> Vậy x = P[-A1invA2, I] x2~ + P[A1invb, 0]
>
> Do đó vấn đề chỉ là tìm P, nên mới nói nếu A có tính chất mà  ta dễ
> dàng nhận ra các cột nào là independent thì ta sẽ dễ dàng xây dựng
> matrix P, và dùng nó để đảo các cột là xong. Cũng có nghĩa là nếu
> không dễ xác định cột nào độc lập thì ta ko biết P là gì để mà dùng

<br>

<p align="center"><kbd><img src="assets/img_qp5m49u.png" width="80%"></kbd></p>

> [!NOTE]
> Về con số chi phí thì:
>
> Nếu theo Gram-Schmidt thì chi phí sẽ là như sau:
>
> Step 1: q1 = a1, q1 = q1/||q1||:
>
> n (*) + n (+) + 1 (√) + n (/) = 3n + 1 ≈ 3n
>
> Step 2: q2 = c2 - (c2Tq1)q1, q2 := q2/||q2||
>
> c2Tq1: n (*) + n (+) = 2n
>
> (c2Tq1)q1: n (*)
>
> c2 - (c2Tq1)q1: n (-)
>
> ⇨ Tổng cộng: 4n 
>
> Và một bước normalizing: 3n 
>
> ⇨ Tổng cộng step 2: 4n + 3n 
>
> Step 3: Project c3 onto q1, q2 và vì q1 vuông góc q2
> thì cơ bản là ta sẽ project lần lượt lên q1, và q2:
>
> nói cách khác q3 = c3 - c3Tq1q1 - c3Tq2q2: tốn 2*4n
>
> Normalizing q3: 3n ⇨ 2*4n + 3n
>
> Tương tự Step 4 sẽ tốn 3*4n + 3n
>
> ...
>
> Step p: sẽ là (p-1)*4n + 3n
>
> Cộng lại hết: 0*4n + 3n + 1*4n + 3n + 2*4n + 3n + ...(p-1)*4n + 3n
>
> = Σi=1:p [(i-1)*4n + 3n] = 4n Σi=1:p (i-1) + Σi=1:p 3n
>
> = 4n p(p-1)/2 + 3np = 2np(p-1) + 3np = 2npp - 2np + 3np 
>
> = 2np^2 + np
>
> ====
>
> Thế thì trong sách nói chi phí là 2np^3 - 2/3 p^3 theo GPT là vì
> người ta dùng cái gọi là Householder reflection để xóa các phần
> tử dưới đường chéo, giúp giảm chi phí tính toán xuống
>
> Rồi đại khái là nếu ta có C là matrix full column rank cao ốm [n, p] thì nó
> có thể được factor bởi QR factorization thành dạng QR (mà một trong
> những phương pháp là Gram-Schmidt mà mình đã học)
>
> Cơ bản về Gram-Schmidt thì như đã biết quy trình sẽ là:
>
> 1) lấy cột 1 của C giữ nguyên, normalize nó để làm cột 1 (q1) của Q.
>
> q1 = c1/||c1||
>
> 2) Project cột 2 (c2) của C lên spanq1 và lấy phần dư, normalize, thành
> cột q2: q2 = c2 - c2Tq1q1, q2 = q2/||q2||
>
> ⇔
>
> 3) Project cột 3 (c3) của C lên spanq1, q2, lấy phần dư, normalize, gán
> thành q3 (vì q1, q2 orthogonal nên phép chiếu chỉ đơn giản là chiếu lần
> lượt lên q1, và q2 rồi lấy phần dư:
>
> q3 = c3 - c3Tq1q1 - c3Tq2q2 ; q3 = q3/||q3||
>
> ...tương tự như vậy đến qp
>
> Khi đó ta sẽ có Q là matrix có các cột orthonormal nhưng không vuông
> nên không phải orthogonal matrix.
>
> Và Gram-Schmidt procedure ở trên chính là:
>
> q1 = c1/||c1||
>
> ⇨ c1 = ||c1|| q1 = ||c1|| q1 + 0*q2 + ...0*qp = Q [||c1||, 0,..0]T
>
> = Q [R11, 0, ...0]T
>
> q2 = c2 - c2Tq1q1, q2 = q2/||q2||
>
> ⇨ c2 = (q1Tc2)q1+q2 = (q1Ta2)q1 + q2||q2||
>
> = R12q1 + R22q2 = R12q1 + R22q2 + 0*q3 + ...0*qp
>
> = Q [R12, R22, 0, ...0]T
>
> Tiếp tục như vậy để thấy tại sao C = QR với R là upper triangular matrix
>
> Thế thì chú ý ở đây, rằng với C là n,p matrix thì Q cũng là n,p matrix
> nhưng cái mà đang nói trong sách là expanded version. Hiểu nôm na là
> sau khi làm xong p columns của C, chính là chuyển từ p basis của
> column space C(C) thành một bộ basis ngon hơn (orthogonal / unit norm)
> của C(C). Thì ta sẽ làm tiếp với n - p basis của left nullspace N(CT) để có
> một bộ orthogonal basis của toàn bộ R^n
>
> Nên ta thấy C = [Q1 Q2][R 0]T = Q1R + Q20 chính là vậy.
>
> Q1TQ1 = I: vì như đã nói các cột của Q1 là orthogonal basis của C(C)
>
> Q2TQ2 = I cũng vậy, các cột của Q2 là orthogonal basis của left null
> space N(CT)
>
> Và Q1TQ2 = 0 thể hiện column space C(C) và left nullspace N(CT)  là hai
> subspace orthogonal complement.

<br>

<p align="center"><kbd><img src="assets/img_dwg4vo3.png" width="80%"></kbd></p>

> [!NOTE]
> Thế thì quay lại vấn đề đang muốn giải hệ under-determined Ax = b 
> (A mập lùn full row rank) thì ý chính là nói QR factorization cũng có
> thể giúp giải hệ này.
>
> Như đã nói để QR factorization, ta cần full column rank. Vậy A full
> row rank nên AT full column rank. Nên giả sử dùng QR factorization
> ta có AT = [Q1 Q2] [R; 0] = Q1R + Q20
>
> Thì khi đó Ax = b ⇔ (Q1R + Q20)Tx = b 
>
> ⇔ (Q1R)Tx = b ⇔ RTQ1Tx = b 
>
> Khi đó x^ = Q1(Rinv)Tb chính là solution, vì nó thỏa:
>
> Vế trái với x = x^: RTQ1Tx^ = RTQ1TQ1(Rinv)Tb
>
> = RTQ1TQ1(Rinv)Tb = RT(Rinv)Tb = b = vế phải
>
> Từ đó ta có particular solution x^
>
> Ngoài ra, như đã hiểu, khi C = [Q1 Q2] [R; 0]
> thì Q2 chính là (orthogonal) basis của left nullspace của C
>
> Nên ở đây nó chính là basis của left nullspace của AT,
> và dĩ nhiên chính là basis của NULLSPACE CỦA A. Và do đó
> nó chính là matrix F mà ta cần
>
> Vậy complete solution chính là x = x^ + Q2z
>
> Và họ cho biết QR factorization chính là phương pháp phổ biến
> nhất để giải hệ under. Chỉ có vài nhược điểm chưa hiểu lắm

<br>

<p align="center"><kbd><img src="assets/img_ysog8ja.png" width="80%"></kbd></p>

> [!NOTE]
> Cuối cùng là nói về LU factorization cũng có thể giúp giải
> hệ under. QUAY LẠI SAU

<br>

