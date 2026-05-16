# 1.2.4 The Gaussian distribution

📊 **Progress:** `4` Notes | `4` Screenshots

---
<a id="node-70"></a>

<p align="center"><kbd><img src="assets/74babd760f91d65c17ef93aadbb9f3fb1cb6f787.png" width="100%"></kbd></p>

> [!NOTE]
> Gs nói qua về Gaussian distribution, loại phân phối sẽ rất phổ biến trong sách
> này.
>
> Cái này thì biết rồi, nhưng đây là cơ hội để nhìn lại những gì đã học trong
> Stat110 và Casella về cái này.
>
> Trong Stat110, gs Joe Blizstein nói về Normal(0,1) từ standard normal trước,
> có pdf là f(z) = 1/√2π exp[-z^2/2]
>
> Rồi ông nói công thức này dễ nhớ hơn, để từ đó ta mới dùng location scale
> family để derive công thức pdf của normal(μ, σ). Location scale theorem nói
> rằng: nếu ta có X ~ f(x) là pdf thuộc location scale family, ứng với location μ,
> scale σ thì Z = (X - μ) / σ sẽ là random variable có pdf thuộc family ứng với
> location 0, scale = 1 gọi là standard member. Ngược lại nếu Z là rv ~ pdf
> standard member thì σZ + μ  sẽ là thành viên ứng với location μ, scale σ
>
> Và normal là loại của một location scale family, với location trùng với mean, và
> scale trùng với standard deviation.
>
> Nên ở đây ta có f(z) là standard member thì X = σZ + μ sẽ là thành viên có
> location μ, scale σ
>
> Dùng transformation theorem ta derive pdf của X = σZ + μ như sau:
>
> với x = g(z) = σz + u ⇨ z = ginv(x) = (x - μ) / σ
>
> fX(x) = fZ(z) |dz/dx|
>
> fZ(ginv(x)) |d/dx ginv(x)|
>
> = 1/√2π exp[-[(x-μ)/σ]^2/2] . (1/σ)
>
> = 1/√2π exp[-(x-μ)^2/2σ^2] . (1/σ)
>
> = 1/σ√2π exp[-(x-μ)^2/2σ^2]
>
> Và đây là pdf của X, là thành viên trong họ location scale, ứng với location μ,
> scale σ, Mà như đã nói, với Normal thì location cũng là mean, scale cũng là
> standard deviation. Do đó, đây chính là pdf của normal(μ, σ).
>
> Ở đây có thể có điểm mà có thể Casella đã nói nhưng ít để ý, 1/σ^2 gọi là
> precision.

<br>

<a id="node-71"></a>

<p align="center"><kbd><img src="assets/1fdf1c6705239d435a557e4bd10fa61a1380ea08.png" width="100%"></kbd></p>

> [!NOTE]
> Dĩ nhiên nó là một valid pdf nên nó phải thỏa hai tính chất, sum trên toàn miền
> phải  = 1 và không âm.
>
> Và mr Bishop để cập đến mean của distribution là μ.
>
> Còn ở đây, dĩ nhiên để tính mean, tức EX với X ~ normal(μ, σ) có pdf như vậy, thì
> ta sẽ theo định nghĩa của kì vọng mà tính: ∫x f(x)dx
>
> Để cho dễ ta có thể tính EZ (Z ~ normal(0,1)) trước:
>
> EZ = ∫-inf:inf zfZ(z)dz = ∫-inf:inf z (1/√2π) e^-z^2/2 dz
>
> = (1/√2π)∫-inf:inf z e^-z^2/2 dz
>
> = (1/√2π) [nguyên hàm của z e^-z^2/2] | -inf:inf
>
> nguyên hàm của z e^-z^2/2 chính là -e^-z^2/2, 
>
> vì d/dz (-e^-z^2/2) = - d(-z^2/2) e^-z^2/2 . d/dz -z^2/2 (chain rule)
>
> = - e^-z^2/2  (-z)
>
> = z e^-z^2/2
>
> = (1/√2π) [e^-z^2/2] | -inf:inf
>
> z → -inf → -z^2/2 → -inf → [e^-z^2/2] → 0
>
> z → inf → -z^2/2 → -inf → [e^-z^2/2] → 0
>
> → kết quả tích phân = 0.
>
> Cách nhanh hơn là nhận xét hàm k(z) = zfZ(z) là hàm lẻ, vì:
>
> k(-z) = (-z)fZ(-z) = -z (1/√2π) e^-(-z)^2/2 = -z (1/√2π) e^-z^2/2 = -k(z)
>
> Và như vậy thì tích phân từ -inf với inf cũng sẽ = 0.
>
> Vậy EX = E(σZ + μ), theo tính linearity của kì vọng, = σEZ + μ = 0 + μ = μ 
>
> Ở đây mình nhắc lại, Normal distribution là một họ distribution thuộc loại location
> scale family, nhưng nó có tính chất đặc biệt là location chính là mean. và scale
> chính là standard deviation. Nói vậy là vì trong Casella ta đã biết, có những
> location scale familly khác thì location chưa chắc đã là mean.

<br>

<a id="node-72"></a>

<p align="center"><kbd><img src="assets/b50aff4b9a449c5369aa20fce8d67ecf3939333d.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp, còn nhớ trong stat110 và Casella đã học khái niệm mgf (moment generating
> function) - hàm sinh moment. Với moment được định nghĩa là EX là first moment, EX^2
> là second moment.
>
> Hàm mgf, được định nghĩa là mX(t) = E[e^tX].
>
> Thế thì có thể tính second moment bằng cách dùng lotus: ∫x^2fX(x)dx
>
> Cũng có thể derive công thức mgf của X, để rồi Taylor expansion và lấy hệ số của term
> bậc hai, thì nó cũng chính là second moment.
>
> Tính theo cách 1: E[X^2] = ∫x^2fX(x)dx (fX(x) là pdf của normal(μ, σ) nếu muốn ghi rườm
> ra thì ghi là f(x|μ, σ) như trong sách này gs Bishop kí hiệu là chữ N hoa luôn)
>
> = ∫x^2 (1/σ√2π) exp[-(x-μ)^2/2σ^2] dx
>
> = (1/σ√2π) ∫x^2 exp[-(x-μ)^2/2σ^2] dx
>
> Để tính cái này cần dùng kĩ thuật integration by part
>
> Để nhớ lại coi, mình nhớ "story" của cái kĩ thuật này vốn chỉ là bắt nguồn từ product rule
> của gỉai tích:
>
> d(uv) = udv + vdu ⇨ udv = d(uv) - vdu
>
> ⇨ ∫udv = ∫d(uv) - ∫vdu
>
> Ta đã giải cái này trong stat110, Casella rồi, ko viết lại nữa.
>
> Còn làm theo cách kia, thì mgf của X là exp[μt + (1/2)σ^2t^2]
>
> Lấy đạo hàm bậc 1 (cũng chính là expand Taylor và lấy hệ số gắn với term bậc 1)
> evaluate tại t = 0 thì ta có fisrt moment (EX)
>
> d/dt [exp[μt + (1/2)σ^2t^2]]
>
> = d/d[μt + (1/2)σ^2t^2] exp[μt + (1/2)σ^2t^2] . d/dt [μt + (1/2)σ^2t^2]
>
> = exp[μt + (1/2)σ^2t^2] . (μ + σ^2t)
>
> ⇨ d/dt [exp[μt + (1/2)σ^2t^2]] | t = 0 =  exp[0] . (μ) = μ
>
> Lấy đạo hàm bậc 2, evaluate tại t = 0 ta sẽ có second moment, EX^2:
>
> d/dt [đạo hàm bậc nhất] = d/dt [exp[μt + (1/2)σ^2t^2] . (μ + σ^2t)]
>
> = { d/dt exp[μt + (1/2)σ^2t^2] } (μ + σ^2t)] + [exp[μt + (1/2)σ^2t^2]  d/dt  (μ + σ^2t)] |
> product rule
>
> = { đạo hàm bậc nhất } (μ + σ^2t)] + [exp[μt + (1/2)σ^2t^2]  σ^2]
>
> ⇨ [đạo hàm bậc 2] | t = 0 = { đạo hàm bậc nhất | t=0} (μ)] + [exp[0]  σ^2]
>
> = [μ (μ)] + [exp[0]  σ^2]
>
> = μ^2 + σ^2 → như trong sách
>
> Và dùng công thức thứ hai của Variance: VarX = EX^2 - (EX)^2 = μ^2 + σ^2 - μ^2 = σ^2.
>
> ====
>
> Cái ý mà gs Bishop nói rằng với Normal thì mode trùng với mean là một ý mới mà mình
> chưa nghe trong Casella

<br>

<a id="node-73"></a>

<p align="center"><kbd><img src="assets/b6a255282759aab6146cd287b88cf7cd89e35d6a.png" width="100%"></kbd></p>

> [!NOTE]
> Sự thật thì mình nhớ cả Stat110 và Casella đều chưa từng nói về công thức này.
>
> Nhưng có thể xây dựng công thức của trường hợp iid standard normal trước, tức là joint pdf của iid Zi ~n(0,1) Khi
> đó **Z** sẽ có mean E**Z** = **0** và covariance matrix Cov(**Z**) = **I**.
>
> Từ đó, đổi biến **X** = A**Z** + **μ** để E**X** = μ và covariance matrix Cov(**X**) = Σ
>
> Đầu tiên xây dựng joint pdf của **Z**:
>
> f(z1,...zn) = Πi f(zi) (do tính iid) = Πi (1/√2π) exp[-zi^2/2]
>
> = [(2π)^-n/2] Πi exp[-zi^2/2]
>
> = [(2π)^-n/2] exp[-Σizi^2/2]
>
> Thể hiện dưới dạng vector: Σizi^2 = **z**T**z**.. = [(2π)^-n/2] exp[-**z**T**z**/2]
>
> Thế thì, tất nhiên E**Z**= [EZ1, EZ2,...EZn] = [0, ...0] = **0** Bữa trước đã nói covariance của hai random variable
> vector **X**, **Y** sẽ là một matrix: Cov(**X**, **Y**) = E[(**X** - E**X**)(**Y** - E**Y**)T], để rồi phần tử hàng i cột j: ij
> sẽ là E[(Xi - EXi)(Yj - EYj)] chính là Cov(Xi, Yj)
>
> ⇨ Cov(**Z**, **Z**), có thể viết tắt là Cov(**Z**), = E[(**Z** - E**Z**)(**Z** - E**Z**)T]
>
> = E[**ZZ**T] (kì vọng của **Z** outer product với **Z**)
>
> Và matrix này sẽ có phần tử thứ ij là Cov(Zi, Zj). Và phần tử trên đường chéo ii chính là Var(Zi) (Cov(Zi, Zi) chính là
> Var(Zi))
>
> Vấn đề là Zi, Zj độc lập, do ta đang xét iid Zi: Nhớ lại định nghĩa iid đã học trong Stat110 và Casella: Random
> sample of size n X1,....Xn ~ f(x|θ) được định nghĩa là: Ta thực hiện quan sát một đại lượng ngẫu nhiên nào đó, n
> lần Mỗi lần giá trị của nó sẽ được đại diện bằng random variables Xi. Và cách thực hiện đảm bảo sao cho các rvs
> Xi MUTUALLY INDEPENDENT, và chúng đều có chung population distribution f(x|θ), gọi là IDENTICALLY
> DISTRIBUTED.
>
> Và đã biết nếu X, Y độc lập thì E(XY) = EXEY ⇨ Cov(X, Y) = 0. Vậy Cov(Zi, Zj) = 0 ∀ i ≠ j.
>
> Còn Var(Zi) thì vì Zi ~ n(0,1), nên nó bằng 1.
>
> Do đó Cov(**Z**,**Z**) CHÍNH LÀ IDENTITY MATRIX.
>
> Rồi, ta sẽ
>
> Đổi biến **X** = g(**Z**) = **AZ** + **μ**với **Σ = AA**T là covariance matrix mong muốn, **μ**là vector [μ1, ...,μn].
> Và ta sẽ xây dựng pdf của **X**, mà ta cho rằng nó sẽ chính là pdf của multivariate Normal(**μ**, **Σ**)
>
> Do đó cần làm rõ hai điểm:
>
> 1) Đổi biến như vậy, thì **X** có phải là normal không.
>
> 2) Mean và covariance có phải là **μ** và **Σ** không.
>
> Trả lời ý 1:
>
> Điều này đồng nghĩa với việc Xi có phải là normal distribution nữa không.
>
> Với **X** = **AZ** + **μ**, Xi = [hàng i của A]TZ + μi
>
> = Σj=1:n aij Zi + μi
>
> tức là một affine combination của Zi (ko phải là linear combination nhé)
>
> Thế thì hồi Stat110 đã học, nếu X, Y đều là normal rv thì X + Y cũng là normal
>
> Chứng minh thì cũng dễ thôi, dùng một theorem liên quan MGF: Đó là nếu X, Y độc lập thì với U = X + Y thì ΜU(t)
> = MX(t)*MY(t). Chứng minh rất dễ:
>
> Theo định nghĩa, moment generating function mgt của X, kí hiệu là MX(t) được định nghĩa là = E[e^tX].
>
> ⇨ Μ(t) = E[e^tU] = E[e^t(X+Y)] = E[e^tX * e^tY]
>
> Và theo 2D LOTUS, ta tính cái này: ∫∫ e^tx e^ty fXY(x,y)dxdy (fXY(.) là joint pdf của X, Y)
>
> Mà X, Y độc lập thì joint pdf = tích marginal pdf:
>
> ∫∫ e^tx e^ty fXY(x,y)dxdy = ∫∫ e^tx e^ty fX(x)fY(y)dxdy
>
> =  ∫e^tyfY(y) [∫e^tx fX(x)dx] dy | tính tích phân theo x trước coi term liên quan đến y như constant, đưa ra
>
> = ∫e^tx fX(x)dx ∫e^tyfY(y)dy | tính tích phân theo y thì coi ∫e^tx fX(x)dx như constant, đưa ra
>
> = Đây chính là E[e^tX] E[e^tY]
>
> cũng chính là MX(t) * MY(t).
>
> Áp dụng theorem này, nếu X ~ normal(μ1, σ1^2) và Y ~ normal(μ2, σ2^2)
>
> và với normal μ, σ ta biết mgf có dạng: exp(μt + σ^2t^2/2)
>
> thì ΜU(t) = MX(t) * MY(t) = exp(μ1t + σ1^2t^2/2) exp(μ2t + σ2^2t^2/2)
>
> = exp(μ1t+μ2t + σ1^2t^2/2 + σ2^2t^2/2)
>
> = exp[(μ1+μ2)t + [σ1^2/2 + σ2^2/2]t^2)
>
> có dạng một mgf của normal(μ1 + μ2, σ1^2 + σ2^2)
>
> và như đã biết trong Stat110, hay Casella, MGF, cũng như CDF, PDF, PMF có thể định nghĩa một distribution. Có
> nghĩa là ta có thể kết luận U = X + U chính là một normal(μ1 + μ2, σ1^2 + σ2^2).
>
> Vậy thì quay lại đây:
>
> Đầu tiên phải nói a1i Zi, với việc Zi ~ normal(0,1), tức standard normal, mà như đã biết, normal là một location
> scale family, với điểm đặc biệt là location trùng với mean, scale cũng chính là standard deviation. Và theo lí thuyết
> location scale family, thì nếu ta có Z là standard member, tức là pdf có location 0, scale 1, thì σZ + μ sẽ là rv có pdf
> thuộc family nhưng ứng với location μ, scale σ.
>
> Vậy ở đây a1iZi chính là thành viên ứng với location 0, scale a1i. Cũng đồng nghĩa, nó là normal(0, a1i^2) với với i =
> 1,...,n.
>
> Vậy thì xét a11Z1 + a12Z2, đây là tổng của hai rvs: a11Z1~ normal(0, a11^2) và a12Z2 ~ normal(0, a12^2)
>
> Nên theo điều vừa ôn lại, nó chính là rv ~ normal(0+0, a11^2 + a12^2)
>
> Và lặp lại lập luận này, ta sẽ có Σj a1jZj chính là một normal(0, Σj a1j^2), tức là variance của rv này là tổng các phần
> từ hàng 1 của A.
>
> Tiếp, ta, theo location scale cũng dễ thấy Σj a1jZj + μ1 cũng là một normal(μ1, Σj a1j^2)
>
> Vậy X1 là normal(μ1,  Σj a1j^2), ..
>
> Xi ~ normal(μi,  Σj aij^2)
>
> Như vậy ta sẽ trả lời ý 2 luôn:
>
> Với Xi ~ normal(μi,  Σj aij) ⇨ E[**X**] = [EX1,...EXn] = [μ1, ..μn] = **μ**.
>
> Cov(**X**, **X**) = E[(**X** - E**X**)(**X** - E**X**)T]
>
> = E[(**X** - E**X**)(**X**T - (E**X**)T)]
>
> = E[(A**Z** + **μ** - **μ**)((A**Z** + **μ**)T - **μ**T)]
>
> = E[(A**Z**)(**Z**T**A**T + μT - μT)]
>
> = E[**AZZ**T**A**T]
>
> = **A**E[**ZZ**T]**A**T (Linearity)
>
> Xét E[**ZZ**T]: Để thấy nó là cái gì, ta xét Cov(**Z**,**Z**) = E[(**Z**-E**Z**)(**Z**-E**Z**)T] = E[(**Z** - **0**)(**Z**T -
> **0**T] (**0**là vector zero)
>
> = E[**ZZ**T]. À như vậy,E[ZZT] = Cov(**Z,Z**) và như ở trên mình đã biết, nó là Identity matrix: I
>
> Vậy.. = A I AT = AAT và như đã nói, ta chọn A sao cho Σ (covariance matrix mong muuốn) = AAT
>
> ⇨ Cov(**X**,**X**) = **Σ**===== Tới đây ta đã chứng minh xong **X** sẽ là normal(**μ**, **Σ**). Việc bây giờ là xây dựng pdf của **X
>
> Tất nhiên là ko thể tích các marginal pdf của Xi được, vì Xi KHÔNG ĐỘC LẬP, COVARIANCE MATRIX KO PHẢI
> LÀ DIAGONAL MATRIX (các term ngoài đường chéo, là covariance các Xi, Xj)**Ta sẽ dùng công cụ transformation: Thế thì, đã học trong Casella, nếu ta có random vector (vector of random variable) [X**,**Y] và thông qua một
> phép biến đổi để có [U,V] = [g1(X,Y), g2(X,Y)]
>
> Sao cho mapping giữa (X,Y) ∈ support set của [X,Y] và (U,V) là 1-1.
>
> (support set của X còn nhớ, đại khái là subset của range X sao cho tại đó / trên đó pdf/pmf của X dương, vậy thì
> support set của random vector [X, Y], là subset của R^2, sao cho trên đó joint pdf fX,Y(x,y) dương)
>
> Có nghĩa là, với U,V ∈ support set của [U,V] ta có thể tìm được (X, Y) = [h1(U,V), h2(U,V)] thuộc support set của
> random vector [X,Y])
>
> Thì khi đó ta có transformation theorem cho phép tính joint pdf của U,V từ joint pdf của X,Y:
>
> fU,V(u,v) = fX,Y(x,y) |J|
>
> = fX,Y(h1(u,v), h2(u,v)) |∂(x,y) /∂(u,v)|
>
> Như đã biết từ MIT 18.02, kí hiệu này ∂(x,y) /∂(u,v) nhằm chỉ Jacobian matrix, mà hàng 1 sẽ là ∂x/∂u, ∂x/∂v hàng 2
> sẽ là ∂y/∂u, ∂y/∂v.
>
> Thế thì giả sử [U,V]T = A [X,Y]T + μ (tức là cũng là một affine transformation)
>
> Ôn lại kiến thức giải tích nếu ta có f(x) = Ax + b là R^n → R^m function ⇨ ∇f(x), cũng  là Jacobian.
>
> Theo MIT 18s096, ta có thể tính ∇f(x) như sau: df = f(x + dx) - f(x) = Ax + Adx + b - Ax - b = Adx linear operation act
> on dx, Và bản chất của đạo hàm bậc nhất là một linear operation act on dx : f'(x)[dx] Từ đó suy ra matrix Jacobian
> chính là A.
>
> Nếu A invertible, ta có quan hệ ngược lại: x = Ainv(f - b) = Ainvf - Ainvb
>
> Và khi đó ∇x(f), là Jacobian của phép biến đởi f → x chính là Ainv.
>
> Vậy thì quay lại đây nếu gọi vector **f** = [u,v]T và **x**= (x,y) thì Jacobian ∂(x,y) / ∂(u,v) chính là Ainv.
>
> Và cái ta cần là determinant của nó: |det A|
>
> Và ta cũng đã biết trong MIT 1806: det Ainv = 1/ det A. Chứng minh rất dễ: AAinv = Ainv A = I ⇨ det(AAinv) = det I =
> 1  (tính chất đầu tiên của det thầy Strang dạy trong bài định thức chính là det I = 1)
>
> Rồi det(AB) = det A det B ⇨ det (AAinv) = det A det Ainv = 1 ⇨ det Ainv = 1 / det A
>
> Vậy cái cần |∂(x,y) /∂(u,v)|, chính là 1 / |det A|
>
> ====
>
> Tiếp tục: fU,V(u,v) = fX,Y(x,y) |J|
>
> Công thức này (bivariate case) cũng sẽ khát quát lên cho multivariate case.
>
> Nên áp dụng nó, với random vector X = A Z + μ
>
> fX(x) = fZ(z) |J|
>
> Và ta đã hiểu |J| cũng chính là 1/ |det A|
>
> Thay fZ(z) vô: = [(2π)^-n/2] exp[-**z**T**z**/2]
>
> Với **x** = A**z** + **μ** ⇨ z = Ainv**x** - Ainv**μ**
>
> ⇨ **z**T**z**= (Ainv**x** - Ainv**μ**)T(Ainv**x** - Ainv**μ**)
>
> = (**x**TAinv - **μ**TAinvT)(Ainv**x** - Ainv**μ**)
>
> = **x**TAinvTAinv**x** - **μ**TAinvTAinv**x** - **x**TAinvTAinv**μ** + **μ**TAinvTAinv**μ**
>
> Dùng hai identity:
>
> (AB)inv = BinvAinv (nếu A, B invertible). chứng minh dễ ẹt: (AB)(BinvAinv) = A I Ainv = AAinv = I ⇨ invert của AB
> chính là BinvAinv
>
> Và (Ainv)T = (AT)inv, cũng dễ chứng minh: AAinv = I ⇔ (AAinv)T = I ⇔ AinvT AT = I ⇨ inverse của AT chính là
> AinvT
>
> ⇨ AinvTAinv = (AT)invAinv = (AAT)inv = Σinv
>
> ⇨ **x**TAinvTAinv**x** - μTAinvTAinv**x** - **x**TAinvTAinv**μ** + **μ**TAinvTAinv**μ**
>
> = (**x**T - μT)Σinv**x**- (**x**T- **μ**T)Σinv**μ**
>
> = (**x**T - **μ**T)(Σinv**x** - Σinv**μ**)
>
> = (**x**T - **μ**T)Σinv(**x** - **μ**)
>
> = (**x** - **μ**)TΣinv(**x** - **μ**)
>
> Vậy f**X**(**x**) = [(2π)^-n/2] exp[-(**x** - **μ**)TΣinv(**x** - **μ**)/2] [1 / |det A|]
>
> = [(2π)^-n/2]  [1/|det A|] exp[-(**x** - **μ**)TΣinv(**x** - **μ**)/2]
>
> Và Σ = AAT ⇨ det Σ = det A det AT
>
> Và det A = det AT: Vì sao?
>
> Theo MIT 1806, trong bài 18. phần cuối gs Strang có nói vần đề này. Đại khái là vầy:
>
> Khi khử Gaussian đưa A → U, ta có A = LU. ⇨ det A = det L det U.
>
> L và U đều là lower triangular matrix: det = tích đường chéo (tính chất chung của det của triangular matrix)
>
> Và L là matrix đường chéo = 1, vì sao? ⇨ det L = 1
>
> ⇨ det A = det U
>
> AT = (LU)T = LT UT ⇨ det (AT) = det LT det UT
>
> = 1 * det UT = det U
>
> Vậy det A = det AT vì đều bằng det U
>
> VẬY  det Σ = det A det AT = (det A)^2 ⇨ |det A| = (det Σ)^1/2
>
> Và kết quả cuối cùng là f**X**(**x**) = [(2π)^-n/2]  [1/(det Σ)^1/2] exp[(**x** - **μ**)TΣinv(**x** - **μ**)/2]
>
> trong sách gs Bishop dùng R^D vector, và |Σ| chính là kí hiệu của det như đã biết
>
> nên ta có công thức trong sách.
>
> [(2π)^-D/2]  [1/|Σ|^1/2] exp[(**x** - **μ**)TΣinv(**x** - μ)/2]
>
> =====
>
> Cuối cùng để chặt chẽ, ta cần nói về việc vì sao có thể tồn tại A
>
> Σ = AAT, lí do có thể phân tách Σ, hay nói cách khác, có thể tìm được A thỏa điều này là vì Σ là 
> matrix xác định dương (positive definite)

<br>

