# 9.3 Methods Of Evaluating Interval Estimators

📊 **Progress:** `6` Notes | `6` Screenshots

---
<a id="node-812"></a>

<p align="center"><kbd><img src="assets/0eae55c98372c9356603406701388a399e437fa2.png" width="100%"></kbd></p>

> [!NOTE]
> Qua phần này ta sẽ học cách tiêu chí và phương pháp đánh giá các Interval
> Estimator. Dễ hiểu là vì một problem ta có thể có nhiều interval estimator
> nên đương nhiên là ta cần đánh giá xem cái nào tốt hơn cái nào.
>
> Thế thì với set / interval estimator, ta sẽ có hai đặc điểm quan trọng: kích
> thước và coverage probability. Và ta sẽ đương nhiên là muốn kích thước
> nhỏ nhưng độ bao phủ lớn.
>
> Vậy thì, ở đây tác giả nhắc lại cho ta rằng, coverage probability trong phần
> lớn trường hợp, thì là function của θ. Nên không thể dùng nó để so sánh
> được. Do đó ta sẽ dùng confidence coefficient. chính là infimum.
>
> Ý này dễ hiểu thôi. Nhớ lại coverage probability, của một interval estimator
> hay confidence set, là hàm theo θ, defined bởi P_θ(θ ∈ C(**X**)).
>
> Nhưng mình cũng biết, một số confidence set nếu được construct dựa trên
> pivot quantity, Q(**X**, θ) thì nó lại có distribution không phụ thuộc θ. Khi đó,
> coverage probability của confidence set này sẽ là constant theo θ. Đó là các
> case đặc biệt gs nói tới ở đây.
>
> Và ta cũng còn nhớ, định nghĩa của confidence coefficient = inf_θ P_θ(θ ∈
> C(**X**)). và nó sẽ ko còn phụ thuộc θ nữa

<br>

<a id="node-813"></a>

<p align="center"><kbd><img src="assets/2e04e3f63aa720b6e765e8e078636cbd66bad07a.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là đầu tiên ta sẽ bàn đến một cách tiếp cận mà hóa ra sẽ trở thành bài
> toán tối ưu có ràng buộc:  Cố định giá trị mong muốn của coverage probability và
> tìm cách giảm length tối thiểu.
>
> Xét ví dụ này, ta có X1,..Xn là iid n(μ, σ^2) với σ đã biết. Thì a, b thỏa P(a ≤ Z ≤
> b) = 1 - α sẽ cho ta một 1-α confidence interval {μ: xbar - b σ/√n} ≤ μ ≤ xbar
> - a σ/√n
>
> Thử xem là vì sao?
>
> Ôn lại: Là vì bữa trước đã học cách xây dựng một confidence set từ một pivot.
> Pivot là một random variable có dạng Q(**X**, θ) nhưng distribution lại ko phụ
> thuộc θ.
>
> Nên nếu ta thể tìm ra một khoảng a, b sao cho P(a ≤ Q(**X**, θ) ≤ b) = 1-α thì
> điều này sẽ đúng với mọi θ ∈ Θ. Dẫn đến khi xét bài toán testing H0: θ = θ0 thì
> {**x**: a ≤ Q(**x**, θ) ≤ b} chính là một level α acceptance region.
>
> Vì sup_θ∈Θ0={θ0} P_θ(**X** ∈ R) = P_θ0(**X** ∈ R) = 1 - P_θ0(**X** ∈ Rc)  = 1 - P(a
> ≤ Q(**X**, θ) ≤ b) = 1 - (1 - α) = α. ⇨ test có acceptance region này chính là một
> level α test.
>
> Và they Tautology theorem, C(**X**) = {θ: a ≤ Q(**X**, θ) ≤ b} chính là 1-α
> confidence  set.
>
> Để rồi như đã biết, nếu θ là số thực, thì tập này sẽ có dạng là interval.
>
> Và ta có thể chuyển nó về dạng [θL(**X**, a or b), θU(**X,**b or a)] tùy theo là
> hàm Q monotone increasing hay decreasing.
>
> Vậy thì ở đây: Ta biết với X1,...Xn là iid normal(μ, σ^2) thì Xbar là normal(μ,
> σ^2/n) Và normal lại là thuộc location scale family với mean là location param,
> standard deviation là scale param.
>
> Nên theo location scale family thì (Xbar - μ) / (σ/√n) chính là standard member
> ứng với location = 0, scale = 1 → Z = (Xbar - μ) / (σ/√n) chính là normal(0,1). Và
> distribution của nó không còn phụ thuộc μ nữa. Ta sẽ dùng nó làm pivot.
>
> Nên mới nói, nếu có được a, b sao cho P(a ≤ Z ≤ b) = 1-α
>
> thì {x: a ≤ Z(**X**, μ) ≤ b} chính là level α acceptance region của bài toán testing
> H0: μ = μ0
>
> Theo Tautology, {μ: a ≤ Z(**X**, μ) ≤ b} chính là 1-α confidence interval của μ
>
> Và  a ≤ Z(X, μ) ≤ b ⇔ a ≤ (Xbar - μ) / (σ/√n) ≤ b
>
> ⇔ a (σ/√n) ≤ Xbar - μ ≤ b (σ/√n)
>
> ⇔ Xbar - b (σ/√n) ≤ μ ≤ Xbar - a (σ/√n)
>
> ⇨ tập trên có thể thể hiện bởi [μL(X, b), μU(X,a)] = {μ: Xbar - b (σ/√n) ≤ μ ≤ Xbar -
> a (σ/√n)}
>
> chính là 1-α confidence interval của μ
>
> Và phù hợp với nhận định là b sẽ nằm ở chặn dưới, a nằm ở chặn trên do hàm
> Z = (Xbar - μ) / (σ/√n) là hàm monotone decreasing theo μ

<br>

<a id="node-814"></a>

<p align="center"><kbd><img src="assets/25c2d254a193ecac50c990a50f9dd558e5a0fae8.png" width="100%"></kbd></p>

> [!NOTE]
> Vậy thì câu hỏi đặt ra là chọn a , b thế nào để thỏa xác suất trên bằng
> 1 - α để ta có một confidence set có coverage probability là 1 - α nhưng 
> length của nó phải ngắn nhất. Và bởi việc cả hai chặn trên dưới đến
> dính đến σ/√n nên việc minimize (b-a) σ/√n sẽ trở thành minimize b-a
>
> Rồi ông mới nhắc đến trong kết quả bữa trước, ta chọn a, b là -/+ z_α/2
> nhưng chưa chắc nó là optimal.
>
> Nói lại chút xíu về kết quả này: Đơn giản là như trên, ta đã có:
>
> Ta muốn tìm a, b soa cho P(a ≤ Z ≤ b) = 1-α 
>
> Thì đây là diện tích của phần đồ thị của normal(0,1) giữa hai mốc a, b.
> Vậy thì một cách dễ thấy là: chọn b để P(Z > b) = α/2, và a khiến P(Z ≤ a)
> = α/2. khi đó diện tích khúc giữa sẽ là 1 - α/2 - α/2 = 1 - α.
>
> Thế thì b để P(Z > b) = α/2 thì b chính là z_α/2.
>
> Còn a để P(Z ≤ a) = α/2 ⇔ 1 - P(Z > a) = α/2 ⇔ P(Z > a) = 1 - α/2
>
> ⇨ a chính là z_(1-α/2).
>
> Tới đây ta nói luôn khoảng [z_(1-α/2), z_α/2] là cái cần tìm vẫn đúng.
>
> Nhưng n(0,1) lại đối xứng qua 0. Có nghĩa là phần diện tích bên phải mốc
> u sẽ bằng phần diện tích bên trái mốc -u (với u dương), Do đó:
>
> a = -b ⇨ z_(1-α/2) = - z_α/2.
>
> Nên cái khoảng trên cũng chính là [-z_α/2, z_α/2]
>
> -----
>
> Quay lại đây, đại ý cũng dễ hiểu là, ta có thể chọn các mốc khác, để
> xác suất này bằng 1-α, và chúng sẽ cho ra các length khác nhau, và cho
> thấy cái a, b trên chính là cái có lenght nhỏ nhất. Nhưng gs chỉ nói là vì
> về mặt giá trị thì ta thấy vậy, chứ đây ko phải là chứng minh rằng trong case
> này lấy đối xứng lại là tốt nhất.
>
> -----
>
> Có thể dễ hiểu là trong case này chắc chắn phải lấy đối xứng thì mới tối
> ưu (length ít nhất). Là vì cái đám mây chuông đối xứng quanh 0. Khi đó
> nếu ta kéo lệch qua trái hay phải hay thậm chí ra khỏi phạm vi cái đỉnh
> thì vì tại đó cái đám mây sẽ mỏng lét, nên để đủ giá trị xác suất 1-α 
> thì ta sẽ phải kéo nó rất dài mới gom đủ.

<br>

<a id="node-815"></a>

<p align="center"><kbd><img src="assets/7c94b8da36d899e1caaad567416b8ec870f45afd.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp theo đại khái là theorem nói về cái này: nếu pdf thuộc dạng
> unimodal (hiểu nôm na là chỉ có 1 đỉnh, nói bằng toán học là tồn tại x*
> khiến đi x ≤ x* thì hàm không giảm, và x* ≤ x thì hàm không tăng) thì khi
> đó. Nếu tại a, b pdf đều dương và bằng nhau. và xác suất x giữa a, b
> (∫a:bf(x)dx) là 1-α. thì [a,b] chính là đoạn có length ngắn nhất trong số
> những đoạn khiến xác suất là 1-α

<br>

<a id="node-816"></a>

<p align="center"><kbd><img src="assets/c6054853d8d3ef4166e07e6cf20afa498f4dca18.png" width="100%"></kbd></p>

> [!NOTE]
> Phần chứng minh thấy vậy mà dễ hiểu thôi ko có gì khó:  Để chứng
> minh [a, b] là đoạn ngắn nhất trong số những đoạn thỏa P(x ∈ [a,b])
> = 1-α ta chỉ cần chứng minh mọi đoạn [a',b'] ngắn hơn [a,b] đều có
> xác suất không đạt.
>
> Ta xét case a' < a: Khi đó sẽ có hai case để có các thứ tự của các
> mốc như sau
>
> b' < a ⇨ a' < b' < a < b:
>
> xét ∫a':b' f(x)dx, chắc chắn nó sẽ ≤ f(b)(b'-a') vì sao:
>
> vì ∫a':b' f(x)dx là diện tích của phần đồ thị pdf của hàm số từ a' đến
> b'. Mà trong đoạn này hàm non-decresing, do x* là cái mode sẽ
> nằm trong [a,b] như theo đề bài cho. do đó, diện tích này là diện
> tích dưới một đường cong đi lên hoặc đi ngang. Do đó nó phải nằm
> trong diện tích của hình chữ nhật có chiều cao là f(b') (dịện tích là
> f(b)(b'-a').
>
> Còn cách đơn giản hơn, thì lập luận trên cho ta f(x) ≤ f(b') với  mọi
> x ∈ [a',b'] nên ∫a':b' f(x)dx ≤ ∫a':b' f(b')dx = f(b')(b'-a')
>
> Vậy ta có ∫a':b' f(x)dx ≤ f(b)(b'-a')
>
> ≤ f(a)(b-a) do a nằm bên phải b' nên f(b') < f(a) và (b'-a') < (b-a)
>
> ≤ ∫a:b f(x)dx  do cũng vì tính chất đừong cong non-decreasing nên
>
> f(a) ≤ f(x) với mọi x từ a đến b
>
> = 1-α, chứng minh xong cho case này
>
> a < b' ⇨ a' < a < b' < b
>
> Xét ∫a':b' f(x)dx = ∫a:b f(x)dx + ∫a':a f(x)dx - ∫b':b f(x)dx
>
> = (1-α) + ∫a':a f(x)dx - ∫b':b f(x)dx
>
> Ta sẽ chỉ cần chứng minh ∫a':a f(x)dx - ∫b':b f(x)dx âm thì sẽ suy ra
> vế trái < 1-α
>
> ∫a':a f(x)dx ≤ f(a)(a-a')
>
> ∫b':b f(x)dx ≤ f(b)(b-b') ⇨ -∫b':b f(x)dx ≤ -f(b)(b-b')
>
> ⇨ ∫a':a f(x)dx - ∫b':b f(x)dx ≤ f(a)(a-a') -f(b)(b-b')
>
> = f(a)(a-a'-b+b') = f(a)(b'-a'-(b-a)) < 0 do đang nói [a',b'] ngắn hơn
> [a,b]
>
> chứng minh xong

<br>

<a id="node-817"></a>

<p align="center"><kbd><img src="assets/ee4fde69d45340213642a124383722130c5d3b9e.png" width="100%"></kbd></p>

🔗 **Related:** [9.2 METHODS OF FINDING INTERVAL ESTIMATORS](92_methods_of_finding_interval_estimators.md#node-767)

> [!NOTE]
> Tiếp theo, đại khái là gs nhắc lại trong ví dụ 9.2.3 (xem link) mình đã xét
> một bài toán mà trong đó ta xây dựng 1-α confidence set bằng cách invert
> một likelihood ratio test. Với ý tưởng chính đại khái là như sau:
>
> Dựa trên việc một LRT sẽ là cái test có rule reject hay accept H0 dựa trên
> λ(**X**) là likelihood ratio test statistic nhỏ hơn hay lớn hơn một threshold c
> là con số nào đó từ 0 đến 1.
>
> Do đó, nếu ta có một cái LRT cho bài toán testing H0: θ = θ0, thì ta có thể
> chọn c  sao cho sup_θ∈Θ0={θ0) P_θ(reject H0) = P_θ0(reject H0) =
> P_θ0(λ(**X**) ≤ c) ≤ α
>
> Rồi, với cái c đó dĩ nhiên cái tập {**x**: λ(**x**) ≤ c} sẽ là level α rejection
> region, cũng như {**x**: λ(**x**) > c} là level α acceptance region A(θ0) của
> bài toán testing H0: θ = θ0.
>
> Từ đó, theo Tautology theorem, ta sẽ có C(**X**) = {θ: λ(**X**) > c} = {θ:
> L(θ|**x**) / L(θ^_mle|**x**) > c}  sẽ là 1-α confidence  interval cho θ
>
> Và từ đó, ta mới xét hàm số g(θ) = L(θ|**x**) / L(θ^_mle|**x**), và xét nó là
> hàm theo θ, thì nó sẽ là có dạng một đỉnh núi. Để rồi nếu có thể chuyển {θ:
> L(θ|**x**) / L(θ^_mle|**x**) > c} thành [θL(**x**), θU(**x**)] với g(θL) = g(θU)
>
> Vậy thì quay lại đây, ĐẠI Ý GS NÓI RẰNG, với việc ta vừa chứng minh
> Theorem 9.3.2 ta sẽ QUAY LẠI KẾT LUẬN RẰNG, CÁI INTERVAL
> [θL(**X**) ≤ θ ≤ θU(**X**)] CÓ ĐƯỢC BẰNG CÁCH LÀM NÀY CHÍNH LÀ
> TỐI ƯU.
>
> Không phải bằng cách ốp trực tiếp theorem này vào, vì cái hàm g mà ta có
> (và đem cắt ngang mốc c để lấy hai điểm) ko phải là hàm pdf. Nhưng đại ý
> là có thể chứng minh được là theorem này cũng sẽ dẫn đến kết luận cái
> interval đó là tối ưu.
>
> Và gs nói thêm, qua phần sau, ta sẽ thấy, nó cũng chính là cách làm để
> tạo ra cái Bayesian region (credible set) tối ưu.
>
> Và cuối cùng, tiếp theo ta sẽ chứng minh rằng với pdf nào unimodal, thì
> cách làm equal α split (tức là chặt bỏ khúc đầu và khúc sau nơi có diện
> tích = α/2)  sẽ đều cho ra đoạn optimal length.

<br>

