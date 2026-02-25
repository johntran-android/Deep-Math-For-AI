# Lec 6: Velocity, Acceleration, Kepler's Second Law

📊 **Progress:** `27` Notes | `29` Screenshots

---
<a id="node-104"></a>

<p align="center"><kbd><img src="assets/5a2bbdc8cbde963534369f166530c12faa630011.png" width="100%"></kbd></p>

> [!NOTE]
> Bài trước ta đã biết về **parametric equation**, giúp **mô tả chuyển
> động của một điểm** theo **biến số thời gian** hoặc biến số nào đó
>
> Cụ thể là bài trước ta xem xét chuyển động của một điểm trên vành
> bánh xe

<br>

<a id="node-105"></a>

<p align="center"><kbd><img src="assets/22a2ee0fefc2f22f0313030b90622f432f244c56.png" width="100%"></kbd></p>

🔗 **Related:** [LEC 12: GRADIENT, DIRECTIONAL DERIVATIVE, TANGENT PLANE](untitled.md#node-251)

> [!NOTE]
> Đại khái là trong bài toán đó ta **thể hiện tọa độ của điểm làm các
> function theo t: [x(t), y(t), z(t)]**, từ đó ta có **position vector OP = r(t)**
> (cũng là tọa độ của điểm) theo t
>
> Và bữa trước ta đã tìm ra **r(t) = < t - sin(theta), 1 - cos(theta)>**
>
> Nếu bánh xe quay với **unit speed**, thì **theta = t** (theta vốn là hàm theo
> t, và nếu tốc độ quay là unit tức là bằng 1 thì theta = 1*t)

<br>

<a id="node-106"></a>

<p align="center"><kbd><img src="assets/2e6f6f2a323b0f3a5c8e9fdca40b560406a583b7.png" width="100%"></kbd></p>

🔗 **Related:** [LEC 6: VELOCITY, ACCELERATION, KEPLER'S SECOND LAW](untitled.md#node-123)

> [!NOTE]
> Đại khái là ta có thể có **vector vận tốc (velocity)** vừa chỉ **độ lớn** vừa
> chỉ **hướng của chuyển động.** Và ta sẽ có vector này bằng cách **lấy
> đạo hàm của r đối với t**
>
> Và component của vector v sẽ có được bằng cách lấy derivative của 
> từng component của r(t) đối với t: dx/dt, dy/dt, dz/dt

<br>

<a id="node-107"></a>

<p align="center"><kbd><img src="assets/c5145b06c36d779e537e7d62f44da5bc1d59812b.png" width="100%"></kbd></p>

> [!NOTE]
> Lấy ví dụ của **cycloid** thì ta có vector velocity như vầy (dễ dàng
> tìm được đạo hàm của x(t), y(t) đối với t:
>
> d [t - sin(t)] / dt = 1 - cos(t) và d [1 - cos(t)] / dt = -(-sin(t)) = sin(t)
>
> Để rồi **với t = 0** (thời điểm xuất phát) thì **v = zero vector**(<1 -
> cos(0), sin(0)> = <1-1, 0> = <0, 0>
>
> Còn **độ lớn** của vận tốc, thì ta sẽ lấy **l2 norm** của vector v, với
> ví dụ cycloid thì nó là sqrt(2-2cost(t)) (để rồi với t = 0 thì 2-2*cost(t) =
> 2-2 = 0
>
> Khi t = pi, thì vector v sẽ song song với hướng di chuyển, với độ lớn
> thế t vào sqrt(2-2*cost(t)) = sqrt(2-2*cost(pi)) = sqrt(2-(-2)) = sqrt(4) =
> 2.  Cho thấy nó **di chuyển nhanh gấp 2 lần tốc độ di chuyển của
> bánh xe**(unit speed)

<br>

<a id="node-108"></a>

<p align="center"><kbd><img src="assets/59b18bd1ee0dc5d9d54a22b8255ae64ef330363b.png" width="100%"></kbd></p>

> [!NOTE]
> Gia tốc cũng là vector, và là **derivative của vector v**(đương nhiên là
> đối với t vì v chỉ là hàm theo t).
>
> Với cycloid example thì vector a là <sin(t), cost(t)> Và **tại t = 0, ta có
> vector a = <0,1>**
> Điều này cho thấy khi đó dù chưa di chuyển, vận tốc của điểm P bằng 0
> nhưng nó có**gia tốc hướng lên với độ lớn sqrt(1^2+0) = 1**

<br>

<a id="node-109"></a>

<p align="center"><kbd><img src="assets/2238d5319cb3fa75a5ca63208b349ea6a6264c2e.png" width="100%"></kbd></p>

> [!NOTE]
> Gs lưu ý là **length của dr/dt mới là length của vector vận tốc**, và
> là độ lớn của vận tốc.
>
> Còn nó **hoàn toàn khác với d|r|/dt** và **đạo hàm của độ lớn** của r
> đối với t **không phải là khái niệm gì cả**

<br>

<a id="node-110"></a>

<p align="center"><kbd><img src="assets/1ad34aa124fa84a7a01408cf59ae541ed9e11aef.png" width="100%"></kbd></p>

> [!NOTE]
> Học qua khái niệm **arc length**, là khoảng cách, **độ lớn của
> quãng đường di chuyển dọc theo quỹ đạo.**

<br>

<a id="node-111"></a>

<p align="center"><kbd><img src="assets/ff157f4f33d4cdd7f75d0f28bbf4437a5148c073.png" width="100%"></kbd></p>

> [!NOTE]
> đại khái là **theo định nghĩa**, derivative của s đối với t, **ds/dt
> = speed = |v|**
>
> Do đó **để tính s**, ta sẽ tính **tích phân vận tốc theo thời gian**

<br>

<a id="node-112"></a>

<p align="center"><kbd><img src="assets/68edd444085c85e275b88dd2227c9eb425a85f14.png" width="100%"></kbd></p>

> [!NOTE]
> Ví dụ, **chiều dài của một arch** trong ví
> dụ cycloid sẽ là **tích phân từ 0:2pi của speed**

<br>

<a id="node-113"></a>

<p align="center"><kbd><img src="assets/74960f1131a6b64bce152cc6afe2e7190942c360.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/74960f1131a6b64bce152cc6afe2e7190942c360.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f70e435327c1dbf30fa3158df393fa5c1bf3e76b.png" width="100%"></kbd></p>

> [!NOTE]
> Ta cũng làm quen một kí hiệu mới t^, chỉ **tangent unit vector** -
> vector tiếp tuyến đơn vị.
>
> Thế thì, ta có **vector v sẽ tiếp tuyến với quỹ đạo**, nên **để có
> vector tiếp tuyến đơn vị** ta chỉ cần **scale vector v về unit length**
> bằng cách **chia vector v cho độ lớn của nó. Nên t^ = v / |v|**

<br>

<a id="node-114"></a>

<p align="center"><kbd><img src="assets/5c9237c1f6ca1c10965313f0e74512f0225289cb.png" width="100%"></kbd></p>

> [!NOTE]
> Vậy thì từ việc ta biết khi đạo hàm vector r theo t ta có vector v.
> Áp dụng chain rule (bài 4 1801) ta có dr/ds ds/dt.
>
> Với ds/dt là độ lớn của vận tốc như đã biế thì dẫn đến:
>
> v = dr/ds |v|. Chia hai vế cho |v|, ta có dr/ds = v/|v| và như vậy nó
> (tức dr/ds) chính là tangent unit vector t^

<br>

<a id="node-115"></a>

<p align="center"><kbd><img src="assets/f91c61d064308bec018121e5b1dd542793e34670.png" width="100%"></kbd></p>

> [!NOTE]
> Và cái này thể hiện rằng, vector v có hướng là vector tiếp tuyến đơn
> vị t^, cũng là tiếp tuyến với quỹ đạo. Và độ lớn của nó, chính là tốc
> độ, và là đạo hàm của s đối với t ds/dt

<br>

<a id="node-116"></a>

<p align="center"><kbd><img src="assets/496e392a3e3fec5f3bde3b0189a83da533cfd5a2.png" width="100%"></kbd></p>

> [!NOTE]
> Gs giải thích **vì sao dr/ds chính là T^**
>
> Thế thì. Khi điểm di chuyển trong khoảng thời gian delta_t, nó sẽ từ
> vị trí thể hiện bởi position vector r(t) để trở thành r(t+delta_t)
>
> Và hiệu của hai vector: r(t+delta_t) - r(t) = vector delta_r.
>
> Thế thì quãng đường nó di chuyển trong delta_t thời gian, là delta_s
> nên delta_s / delta_r sẽ cho ta xấp xỉ (độ lớn) vận tốc. 
>
> Và vector delta_r có thể coi như xấp xỉ delta_s * vector T^: 
> delta_r ~= T^ delta_s. Để rồi chia hai vế cho delta_t, ta có:
>
> delta_r / delta_t ~= T^ delta_s / delta_t

<br>

<a id="node-117"></a>

<p align="center"><kbd><img src="assets/ec12e8f99832ffb8085489c908e904db63bb13bd.png" width="100%"></kbd></p>

> [!NOTE]
> Và tính limit khi delta_t -> 0, sẽ
> cho ta dr/dt = T^ ds/dt

<br>

<a id="node-118"></a>

<p align="center"><kbd><img src="assets/6e599329c6f7b224b80289dae2e57fec91bbcee0.png" width="100%"></kbd></p>

> [!NOTE]
> vector delta_r ko có hướng tiếp tuyến (vector T^), như hình ảnh này gs
> cho thấy điều đó. Tuy nhiên khi delta_t -> 0 thì vector delta_r và T^ sẽ
> ngày càng trở nên trùng hướng nhau vì khi đó cung (đường cong) sẽ
> ngàg càng trở nên thẳng

<br>

<a id="node-119"></a>

<p align="center"><kbd><img src="assets/bca31c0954c3babb9b0104f8588a2e859ebb67e5.png" width="100%"></kbd></p>

> [!NOTE]
> Ta sẽ học qua định luật thứ 2 của Kepler nói rằng: Chuyển động của
> hành tinh quanh mặt trời là trên một mặt phẳng, và diện tích bị quét
> bởi đường nối giữa hàng tinh và mặt trời sẽ theo một tỉ lệ hằng số

<br>

<a id="node-120"></a>

<p align="center"><kbd><img src="assets/0ff04cadebf7a8dd9e8f0b18fcf651243a0327cf.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái gs cho biết cái này có nghĩa hành tinh khi gần mặt trời hơn
> khi nó quanh quanh mật trời theo quỹ đạo elip thì nó sẽ đi nhanh
> hơn và chậm lại khi ra xa. 
>
> Và sau này Newton giải thích lại dùng công thức của luật hấp dẫn.

<br>

<a id="node-121"></a>

<p align="center"><kbd><img src="assets/a1810a638e649b4b9c69f9a2c11a1291efde5b1d.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì hình ảnh là vầy, hành tinh chuỷen động trên quỹ đạo elip.
> Ta có position vector r(t), và trong delta_t, nó di duyển đến
> r(t+delta_t) từ đó ta có vector delta_r

<br>

<a id="node-122"></a>

<p align="center"><kbd><img src="assets/8ac93933a54da6ababcae1b4a32915d295ad3f89.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì gs cho rằng khi delta_t vô cùng nhỏ, thì như đã biết, cung
> (đường cong) có thể coi như thẳng để diện tích của vùng giữa hai
> vector r(t) và r(t_delta_t) có có thể coi như diện tích tam giác tạo bởi 3
> vector. Và diện tích này có thể được tính bằng 1/2 diện tích hình bình
> hàng tạo bởi hai vector delta_r và r.
>
> Và bài 2 ta đã biết, với 3D vector, ta có thể tính diện tích hình bình hành
> này bằng cách tính độ lớn của vector cross product giữa hai vector.

<br>

<a id="node-123"></a>

<p align="center"><kbd><img src="assets/96df90ad83f8923dc5411e0f88f940e109c21069.png" width="100%"></kbd></p>

🔗 **Related:** [LEC 6: VELOCITY, ACCELERATION, KEPLER'S SECOND LAW](untitled.md#node-106)

> [!NOTE]
> Tiếp theo ta sẽ dùng định nghĩa của velocity vector hồi nãy rằng 
> đạo hàm của vector r đối với t là velocity vector.
>
> Thế thì dr/dt = v và ta cũng biết, khi **thay các d bằng delta sẽ cho
> ta linear approximation**
>
> delta_r / delta_t ~= v <=> **delta_r ~= v * delta_t**

<br>

<a id="node-124"></a>

<p align="center"><kbd><img src="assets/de21a798b6eaa52c18210fcd0c9ae6f73b9fb0e1.png" width="100%"></kbd></p>

> [!NOTE]
> Từ đó, thế vector delta_r bằng ~ v * delta_t ta có Area ~= (1/2) | r x
> v| delta_t (vì delta_t là constant nên có thể đưa ra ngoài)
>
> Lúc này ý nghĩa của định luật Kepler khi nói diện tích được swept
> theo tỉ lệ hằng số chính là ý nói diện tích sẽ tỉ lệ thuận với thời gian
> delta_t (Area / delta_t = constant)
>
> Điều này đồng nghĩa nói rằng độ lớn của cross product vector tạo
> bởi vector và vector v là hằng số

<br>

<a id="node-125"></a>

<p align="center"><kbd><img src="assets/9a38317bab3b6afcecbda5ce0fad6b02e232b2ab.png" width="100%"></kbd></p>

> [!NOTE]
> Nhận định tiếp theo là, mặt phẳng chuyển động sẽ chứa cả r, và v.
>
> Thế thì, vì cross product vector tạo bởi r và v ta đã biết sẽ vuông góc
>  với mặt phẳng tạo bởi r, v. mà, vậy r x v vuông góc với mặt phẳng
> chuyển động
>
> Và ý (1) đã nói r x v có constant length, và ý (2) này nói hướng của nó
> vuông góc với mặt phẳng chuyển động vốn là cố định. Do đó cả hai
> ý hàm nghĩa (r x v) là constant vector

<br>

<a id="node-126"></a>

<p align="center"><kbd><img src="assets/233869715fb8d03426c6e3d7b8b345b6b35c0267.png" width="100%"></kbd></p>

> [!NOTE]
> Và điều đó có nghĩa là đạo hàm của vector cross
> product r x v đối với t sẽ là 0

<br>

<a id="node-127"></a>

<p align="center"><kbd><img src="assets/205e07f8cf8d3161b940f7fb08c928eaeae2b178.png" width="100%"></kbd></p>

> [!NOTE]
> Gs cho biết ta có thể áp dụng product rule đối với dot product
> và cross product chỉ cần chú ý giữ thứ tự của hai vector trong
> cross product  chứ đừng đảo lộn
>
> Có nghĩa là d(r x v) / dt = (dr / dt) x v + r x (dv / dt)
>
> (dr / dt) x v có nghĩa là cross product vector tạo bởi vector dr/dt
> với vector v

<br>

<a id="node-128"></a>

<p align="center"><kbd><img src="assets/e6d81f3b704e38c8ccfd8db1e3b7a4b9a64ba36e.png" width="100%"></kbd></p>

> [!NOTE]
> Và dr/dt chính là vector v, và dv/dt
> chính là vector a (vector gia tốc)

<br>

<a id="node-129"></a>

<p align="center"><kbd><img src="assets/de79ec4a2ebb340152eb66b17c5dd371b5457f67.png" width="100%"></kbd></p>

> [!NOTE]
> v x v = 0 (ý nghĩa của cross product a x b là vector vuông góc với
> plane  tạo bởi a, b và có độ lớn bằng hình bình hành tạo bởi hai
> vector a, b. mà v, với v tạo hình bình hành có diện tích bằng 0, nên v
> x v = 0)
>
> Nên điều trên tương đương r x a = 0. và again điều này tương
> đương a và r song song (cùng phương)

<br>

<a id="node-130"></a>

<p align="center"><kbd><img src="assets/547593590a99b853342b4bcef07eb3f1191a0261.png" width="100%"></kbd></p>

> [!NOTE]
> Và dựa theo kiến thức vật lý ta biết gia tốc sẽ có phương
> của lực trọng trường.

<br>

