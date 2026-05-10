# 1.2 Probability Theory

📊 **Progress:** `9` Notes | `14` Screenshots

---
<a id="node-29"></a>

<p align="center"><kbd><img src="assets/c758fa0d99e5c22df5fbcc611b49de0611b225ac.png" width="100%"></kbd></p>

> [!NOTE]
> Mở đầu gs nói một ý mình nghĩ rằng rất quan trọng. Đó là, một yếu tố
> quan trọng của pattern recognition là tính uncertainty (tính không chắc).
> Và yếu tố này khởi nguồn có thể là từ nhiễu (noise) trong quá trình đo đạc
> (measurement) hoặc cũng có thể là từ việc ta chỉ có một mẫu với số
> lượng hữu hạn. Do đó, đại ý là ta cần lí thuyết xác suất, nó sẽ mang lại
> cho ta những công cụ để định lượng hóa cũng như là thao tác với các
> yếu tố uncertainty này. Để rồi kết hợp với lí thuyết ra quyết định sẽ giúp ta
> đưa ra những hành động, quyết định tối ưu trên cơ sở những thông tin
> mà ta có, kể cả khi nhưng thông tin này là không đầy đủ (incomplete) và
> mơ hồ (ambiguous)

<br>

<a id="node-30"></a>

<p align="center"><kbd><img src="assets/14415571827ae58a99d031665d70b4f7d6db0167.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a6a04ab5fba3c214a1fecdd732d4d665f46e517f.png" width="100%"></kbd></p>

> [!NOTE]
> Gs sẽ dùng ví dụ đơn giản này để nói về các khái niệm nền tảng của xác suất:
> Nói ngắn gọn, có 2 hộp xanh đỏ. Hộp đỏ có 2 táo 6 cam, hộp xanh có 3 táo
> 1 cam. Rồi, làm thí nghiệm thế này: Chọn đại một hộp (ngẫu nhiên), rồi bốc đại
> một trái trong đó (dĩ nhiên cũng ngẫu nhiên). xem là trái gì rồi bỏ vào lại. Và
> lặp lại như vậy nhiều lần.
>
> Đến đây ta sẽ giả sử rằng (suppose) sau nhiều lần làm thì 40% ta chọn hộp đỏ
> 60% chọn hộp xanh (có nghĩa là xác suất chọn hộp đỏ nhỏ hơn). Nhưng khi
> chọn trái trong hộp nào thì xác suất chọn trái nào cũng như nhau (equally likely)

<br>

<a id="node-31"></a>

<p align="center"><kbd><img src="assets/e5be5fe5580146d9d989f6e13dbcf0e03deae168.png" width="100%"></kbd></p>

> [!NOTE]
> Đến đây là gặp lại một trong những khái niệm nền tảng nhất của xác suất:
> random variable. Cụ thể là nếu quan tâm danh tính của cái hộp được
> chọn, thì nó là một đại lượng mang tính ngẫu nhiên (vì dĩ nhiên là ta đâu
> biết là hộp nào sẽ được chọn trước khi diễn ra hành động thử nghiệm),
> nhưng ta biết nó sẽ mang một trong hai giá trị: xanh hay đỏ.
>
> Trong xác suất, ta mới đặt nó là biến B, với hai possible value là r, b. Nhờ
> stat110 và Casella đã nhắc đi nhắc lại bản chất của B là MỘT
> FUNCTION: Function này maping một possible outcome s trong original
> sample space Ω với các possible value trong range của B. Trong trường
> hợp này, original sample space là không gian mẫu chứa các kết quả mà
> hành động thực hiện thử nghiệm có thể tạo ra: "chọn hộp, chọn trái" và
> range B= {r,b}. Để rồi nếu s là "chọn hộp xanh, chọn trái ..." thì B(s) = b,
> nếu s là "chọn hộp đỏ, chọn trái .." thì B(s) = r
>
> Tương tự, danh tính của trái mà ta chọn cũng là biến ngẫu nhiên, đặt là F,
> nó cũng sẽ có hai possible value là {a, o}. Để rồi nếu s là "(chọn hộp ... ,
> chọn trái táo" thì F(s) = a, nếu s là "chon hộp ...m chọn trái cam" thì F(s) =
> o
>
> Sẵn nói luôn, còn nhớ, rv với hai possible values thì nó chính là Bernoulli
> random variable. Nếu gọi chọn hộp đỏ là một success event, thì B ~
> Bern(0.4) còn F thì cũng là Bern(p). p bằng bao nhiêu thì ta sẽ phải dùng
> LOTP để  tính:
>
> P(F=a) = P(F=a, B=r) + P(F=a, B=b) (marginalizing joint pmf over mọi p.v
> của B)
>
> = P(F=a|B=r)P(B=r) + P(F=a|B=b)P(B=b) (conditional probability theorem)

<br>

<a id="node-32"></a>

<p align="center"><kbd><img src="assets/89755ed0012de26410640da8773c7d6e3551278c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/46c9f4d6e91cf6e02f02afcd769450686ec73c29.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp chỗ này gs Bishop thật ra đang định nghĩa xác suất theo trường phái cổ
> điển (Frequentist) khi ông nói ta sẽ define xác suất của một event là tỉ lệ xuất
> hiện của nó khi lặp lại vô hạn lần thử nghiệm. (nếu là trường phái Bayesian,
> xác suất của event sẽ phản ánh độ tin tưởng rằng event sẽ xảy ra)
>
> Và vì lúc nãy ta nói cho rằng thử nghiệm vô số lần thì 40% trong số đó sẽ
> chọn hộp đỏ, nên P(B=r) = 0.4, và P(B=b) = 0.6.
>
> Gs nói, theo định nghĩa, nó sẽ phải là con số trong [0,1]. Dễ hiểu là với cách
> định nghĩa này, thì nó là con số tỉ lệ, nên dĩ nhiên nó phải không âm và ≤ 1.
>
> mình nhớ, đây thực ra là từ Axiom 1,2 (2 trong 3 tiên đề của xác suất) : xác
> suất của một biến cố P(A) không âm với mọi A ∈ Ω và P(Ω) = 1.
>
> Câu cuối, gs nói nếu các event loại trừ lẫn nhau (mutually exclusive) và
> chứa mọi possible outcomes thì tổng xác suất sẽ = 1. Là sao?
>
> À thì đây chính là nói khi đó (B = r) và (B = p) sẽ làm thành một partition:
>
> (B = r) U (B = p) = Ω, (B = r) ∩ (B = b) = ∅ thì khi đó:
>
> P[(B = r) U (B = p)] = P(Ω) = 1 theo axiom 2.
>
> mà vế trái, là xác suất của một union của các disjoint event, nên theo axiom
> 3, nó sẽ là tổng xác suất đơn lẻ: 
>
> P[(B = r) U (B = p)] = P(B = r) + P(B = b)
>
> Do đó P(B = r) + P(B = b) = 1

<br>

<a id="node-33"></a>

<p align="center"><kbd><img src="assets/6d3454153e9ad888be5de6c8c8471d7ff40f7d39.png" width="100%"></kbd></p>

> [!NOTE]
> Definition 1.2.4 sách Casella
> nêu 3 tiên đề xác suất

<br>

<a id="node-34"></a>

<p align="center"><kbd><img src="assets/cd270ad2ebafc5c32fabaed58d6b5e45c3609e6b.png" width="100%"></kbd></p>

> [!NOTE]
> Đoạn này tác giả đặt câu hỏi, làm sao ta có thể tính được xác suất của việc
> bốc được một trái táo. Hoặc một câu hỏi khác là nếu đã chọn trái cam thì xác
> xuất ta đã chọn hộp xanh là bao nhiêu.
>
> Thì ông cho rằng, hai cái rule quan trọng của xác suất là sum rule và product
> rule sẽ giúp ta trả lời hai câu hỏi này

<br>

<a id="node-35"></a>

<p align="center"><kbd><img src="assets/15d24879f0e702d7ec2170162a29baceb11055f7.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4eaa3f115bb2bbf0bafb2fb7dc0fed03df3b6fb8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d49e90bc762c2890897c0d89d1687253f11ad3a0.png" width="100%"></kbd></p>

> [!NOTE]
> Đại ý là ông dùng ví dụ này để ta hiểu về sum rule và product rule: Cho X, Y là hai rvs với
> possible values là x1,....xM, và y1,...yL. Thực hiện thử nghiệm nào đó để có hai gía trị cụ
> thể của X, Y, và làm vậy N lần. Trong đó gọi ci là số lần ông X = xi (ví dụ c2 là số lần X ra
> bằng x2),  rj là số lần ông Y ra yj.
>
> Thế thì câu hỏi như hồi nãy đặt ra là ta muốn tính xác suất mà khơi khơi bốc được trái táo
> (ko biết bốc hộp nào), cũng chính là muốn tính P(B = a)
>
> Thì ở đây, nó tương ứng với việc ta đặt câu hỏi tính xác suất X = xi.
>
> Thế thì trong sách, gs Bishop dùng lập luận theo kiểu này, nhưng mình có thể lập luận
> theo lối đã học trong Casella
>
> Về mặt bản chất như đã học trong Casella + Stat110:
>
> P(X = xi) = P({s ∈ Ω: X(s) = xi}), ý nghĩa tổng xác suất các biến cố (possible outcome) trong
> không gian mẫu mà map với X ra xi.
>
> Giờ xét cái tập {s ∈ Ω: X(s) = xi},
>
> Dĩ nhiên nó là tập con của Ω: {s ∈ Ω: X(s) = xi} ⊂ Ω
>
> Theo lí thuyết tập hợp: nếu A ⊂ B ⇨ A ∩ B = A
>
> ⇨ {s ∈ Ω: X(s) = xi} = {s ∈ Ω: X(s) = xi} ∩ Ω
>
> Thể hiện Ω = U{mọi possible value yj} {s ∈ Ω: Y(s) = yj}
>
> ⇨ {s ∈ Ω: X(s) = xi} ∩ Ω = {s ∈ Ω: X(s) = xi} ∩ [U{mọi possible value yj} {s ∈ Ω: Y(s) = yj}]
>
> Dùng distributive law: A ∩ (B U C) = (A ∩ B) U (A ∩ C):
>
> .. = U{mọi possible value yj} [{s ∈ Ω: X(s) = xi} ∩ {s ∈ Ω: Y(s) = yj}]
>
> = U{mọi possible value yj} {s ∈ Ω: X(s) = xi, Y(s) = yj}
>
> Viết lại {s ∈ Ω: X(s) = xi} = U{mọi possible value yj} {s ∈ Ω: X(s) = xi, Y(s) = yj}
>
> ⇨ P[{s ∈ Ω: X(s) = xi}] = P{U{mọi possible value yj} {s ∈ Ω: X(s) = xi, Y(s) = yj}]
>
> Vế phải, là xác suất của union của các disjoint events, nên theo Axiom 3:
>
> = Σ_{mọi possible value yj} P({s ∈ Ω: X(s) = xi, Y(s) = yj})
>
> Viết lại P[{s ∈ Ω: X(s) = xi}] = Σ_{mọi possible value yj} P({s ∈ Ω: X(s) = xi, Y(s) = yj})
>
> Và cái này chính là:
>
> P(X = xi) = Σj=1:L P(X = xi, Y = yj), là sum rule, hoặc gọi là marginalize joint pmf trên mọi
> possible value của Y, cũng là lí do ta P(X = xi) gọi là marginal distribution của X

<br>

<a id="node-36"></a>

<p align="center"><kbd><img src="assets/4ac8c51dd67b33eea54dac1a43a8dee0efd2708a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7f2a3346729bef4ce5d9d2552424a9aa6cd0bcb8.png" width="100%"></kbd></p>

> [!NOTE]
> Gs quy ước một chút về kí hiệu, p(B) sẽ chỉ distribution của B, p(r) sẽ chỉ  giá trị
> xác suất tại B = r.
>
> Và hai rule của xác suất sẽ thể hiện bởi:
>
> p(X) = ΣY p(X, Y)
>
> và p(X, Y) = p(Y|X)p(X)
>
> Đối chiếu với stat110, Casella:
>
> Thì đây là fX(x) = Σy fX,Y(x,y), cũng là marginalizing joint pdf/pmf, và cũng là,
> bản chất  chính là LOTP
>
> Và fX,Y(x,y) = fX|Y(x|y)fX(x)
>
> Chính là dựa định nghĩa của conditional probability: P(A|B) = P(A,B) / P(B) ⇨
> P(A,B) = P(A|B)P(B), cái này gs Joe Blizstein gọi nó là Conditional probability
> theorem.
>
> Tóm lại mình nên hiểu: Chỗ này ông Bishop sẽ không theo lối kí hiệu chặt chẽ
> của toán thống kê.
>
> Vì nếu theo đó, phải ghi rõ ra:
>
> Biến rời rạc:
>
> P(X=x) = Σy P(X=x, Y=y),
>
> P(X=x, Y=y) = P(X=x|Y=y)P(Y=y)
>
> Biến liên tục:
>
> fX(x) = ∫_range Y fX,Y(x,y)dy
>
> fX,Y(x,y) = fX|Y(x|y)fY(y)
>
> Còn ở đây, gs Bishop đặt lại quy định về kí hiệu:
>
> p(X) sẽ chỉ **HÀM DISTRIBUTION CỦA**X, (pmf hoặc pdf)
>
> p(x) sẽ là **GÍA TRỊ HÀM PMF/PDF CỦA X TẠI x
>
> Nếu ko nhớ convention này của gs Bishop thì rất dễ lú sau này**

<br>

<a id="node-37"></a>

<p align="center"><kbd><img src="assets/07e07dbdc0cf196e307bfd5715bb340f63362118.png" width="100%"></kbd></p>

> [!NOTE]
> Ở đây nói về Bayes' theorem, stat110 ta đã biết nó chỉ là hệ quả của 
> định nghĩa về conditional probability.
>
> Nhưng cái ý cuối là quan trọng: nói nói cái mẫu số có thể coi như normalizing
> constant để đảm bảo tổng xác suất điều kiện = 1.

<br>

