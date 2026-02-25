# Lec 19: Vector Fields

📊 **Progress:** `36` Notes | `52` Screenshots

---
<a id="node-456"></a>

<p align="center"><kbd><img src="assets/cbae1831fe0f37bf8d2309de9a59000401a516ff.png" width="100%"></kbd></p>

> [!NOTE]
> bài này ta sẽ tạm quên double integral để thảo luận về Vector field. Định
> nghĩa đại khái là, tại mỗi điểm x, y ta có vector F  = M*i + N*j với M, N
> phụ thuộc x, y. Có nghĩa là mọi điểm ta có vector F và vector F sẽ khác
> nhau phụ thuộc x, y. Đó là **VECTOR FIELD** - **TRƯỜNG VECTOR.**
>
> Ví dụ có thể nghĩ đến hình ảnh của **Force field - TRƯỜNG LỰC**. Tại
> các điểm trong không gian đều có lực tác dụng từ các hành tinh, thiên
> thể (TRƯỜNG TRỌNG LỰC, HAY TRỌNG TRƯỜNG) Và vector lực sẽ
> tùy thuộc vị trí của điểm đang xét

<br>

<a id="node-457"></a>

<p align="center"><kbd><img src="assets/698a6caaf190b2656566891d58567313d8476f27.png" width="100%"></kbd></p>

> [!NOTE]
> Và gs nói tuy ta sẽ xem xét vector field một cách toán học
> nhưng ta sẽ dùng ví dụ này để xem tại sao ta lại quan tâm
> các tính chất của vector field

<br>

<a id="node-458"></a>

<p align="center"><kbd><img src="assets/1333edf8e1a1fd439a378b669995b35801bfb26c.png" width="100%"></kbd></p>

> [!NOTE]
> Một ví dụ đầu tiên về vector field mà gs cho rằng có thể khá silly là
> F = 2i + 1j. Tức là vector không phụ thuộc x,y. Mà luôn = 2i + j
>
> HÌnh ảnh của nó là đây, tại điểm nào cũng vậy, vector luôn là 2i + j

<br>

<a id="node-459"></a>

<p align="center"><kbd><img src="assets/910cd4cf8592d375e0f11e26a3a47785330782a5.png" width="100%"></kbd></p>

> [!NOTE]
> Ví dụ thứ hai là vector field quy định bởi F = x*i (tức là không có j
> component, nên các vector chỉ song song với trục x)
>
> Thế thì có thể thấy x nhỏ thì F ngắn hơn, khi x tăng lên thì F dài hơn
> và  khi x âm thì vector F quay ngược chiều lại.
>
> Để hình ảnh của vector field này như vầy

<br>

<a id="node-460"></a>

<p align="center"><kbd><img src="assets/40f5356214d7a7f31777e17ff0301bbf110e103c.png" width="100%"></kbd></p>

> [!NOTE]
> gs nói thường thì ta chỉ muốn phác thảo sơ về hình
> dung của vector field chứ không cần vẽ chính xác vì đã
> có máy tính

<br>

<a id="node-461"></a>

<p align="center"><kbd><img src="assets/5b909b1897534aaba6a19c18aac381c0f9c8087a.png" width="100%"></kbd></p>

> [!NOTE]
> Qua ví dụ một vector field khác F = x*i + y*j. Thì hình
> ảnh nó là như này, vector tại x,y thì chính là vector (x,y)
> nhưng dời gốc về điểm (x,y) thôi

<br>

<a id="node-462"></a>

<p align="center"><kbd><img src="assets/358c397064a72cb43e28cb73bc5b19cd168ced53.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/358c397064a72cb43e28cb73bc5b19cd168ced53.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ab305ab4618e61485fbb82ae3c5364023766e554.png" width="100%"></kbd></p>

> [!NOTE]
> Qua vector field này, F = -y*i + x*j thì có nghĩa là tại (x,y) ta sẽ tương ứng
> với vector (-y, x) là vector bằng độ dài và vuông góc với (x,y) và ta dời
> vector đó về điểm (x,y)
>
> Để rồi hình ảnh của nó là như vầy, mô tả dòng chảy quanh gốc 0, với vận
> tốc góc (angular velocity) unit (cũng không quan trọng lắm)

<br>

<a id="node-463"></a>

<p align="center"><kbd><img src="assets/5016333fa54104444cb9d6daf6a49f5826d98f51.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0875d0b0e0fb9c291af825fd2917454eb7fdf1c4.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/5016333fa54104444cb9d6daf6a49f5826d98f51.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0875d0b0e0fb9c291af825fd2917454eb7fdf1c4.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c31ef26dd36abdb9ad48ffcd77e9c4ca70ca29b3.png" width="100%"></kbd></p>

> [!NOTE]
> ta học qua khái niệm CÔNG (WORK) VÀ LINE INTEGRAL. Đại khái gs cho biết
> trong vật lí Công của lực F tạo ra / khiến một object di chuyển một quãng đường
> Delta_r sẽ được tính bởi dot product giữa vector F và vector Delta_r
>
> Và như đã học vật lý phổ thông, công là đại lượng cho biết năng lượng cần thiết
> để thực hiện việc này

<br>

<a id="node-464"></a>

<p align="center"><kbd><img src="assets/df6e2bebfbf0a3c5d7c00affb24e3f9df646417b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/df6e2bebfbf0a3c5d7c00affb24e3f9df646417b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e00ad1aa90c2d54d061051815facf5f8135a969e.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì nếu object di chuyển trên quỹ đạo mà lực F sẽ khác nhau
> giữa các điểm khác nhau trên quỹ đạo. Thì ta cách tính là ta sẽ chia
> nhỏ quỹ  đạo thành các đoạn delta_r. Và ta sẽ tính
>
> 1) TỔNG CỦA DOT PRODUCT CỦA CÁC VECTOR DELTA_R VÀ F.
>
> 2) VÀ TA SẼ TÍNH LIM CỦA CÁI NÀY  VỚI DELTA_R NHỎ DẦN VỀ 0
>
> Để rồi **công của lực trên cả quỹ đạo C** trở thành**tích phân trên
> quỹ đạo C [F dot product dr]**

<br>

<a id="node-465"></a>

<p align="center"><kbd><img src="assets/9dce229658f807e4a8930b30c3f8ecf62e8c30a0.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì  ta có thể viết delta_r = delta_r / delta_r * delta_t Thì (delta_r
> / delta_r) chính là ~ VELOCITY VECTOR dr/dt

<br>

<a id="node-466"></a>

<p align="center"><kbd><img src="assets/7c5ce8b69dc8a9739e4711120adab14ee75efbff.png" width="100%"></kbd></p>

> [!NOTE]
> Để rồi tích phân trở thành tích phân từ t1 đến t2 dot product của
> [F, (dr/dt).dt]
>
> Trong đó F = vector force, như đã biết sẽ tùy vào vị trí của điểm
> và do đó nó khi ta đang chuyển thành tích phân theo thời gian t (vì
> vị trí bây giờ sẽ phụ thuộc t) thì nó sẽ tùy vào t

<br>

<a id="node-467"></a>

<p align="center"><kbd><img src="assets/4528f32d6bf3e3f41fe19bb38bc2d2cae5104f38.png" width="100%"></kbd></p>

> [!NOTE]
> một student thắc mắc, thì gs khẳng định đúng là ta sẽ tính limit khi
> delta_t -> 0 của Tổng [F. (delta_r/delta_t) delta_t]
>
> Mang ý nghĩa là ta cắt quỹ đạo (trajectory) thành các đoạn delta_r
> ngày càng nhỏ và tính tổng của các phép dot product giữa vector F
> và delta_r
>
> Thì delta_r nhỏ dần thì cũng là (velocity . delta_t) với delta_t nhỏ dần

<br>

<a id="node-468"></a>

<p align="center"><kbd><img src="assets/c5d463d0c076fb7de294f87245b9c473cd467f0e.png" width="100%"></kbd></p>

> [!NOTE]
> Ta qua một ví dụ (lấy ví dụ hồi nãy) vector field  = -y*i + x*j
>
> với quỹ đạo C: x = t, y = t^2 với t trong range [0,1]

<br>

<a id="node-469"></a>

<p align="center"><kbd><img src="assets/cd73836e2997d715d0d06a50cd17eb10e6ab4327.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì trajectory x = t, y = t^2 với t trong range [0,1] chính là
> điểm sẽ có quỹ đạo là một đoạn của Parabola y = x^2 từ gốc
> 0 đến (1,1)
>
> Và như vậy cơ bản ta muốn tính Công (work) tạo bởi lực F khi
> di chuyển object trên quỹ đạo này.

<br>

<a id="node-470"></a>

<p align="center"><kbd><img src="assets/c215e150bbf6d6ff4f8123fd16981671ba9404f8.png" width="100%"></kbd></p>

> [!NOTE]
> Và gs nói đại khái là nếu ta hỏi rằng tại sao ta có C như vậy thì câu hỏi
> đó sai. Vì F và c là hai phần của dữ liệu mà ta có. Tức là ta có F như vầy,
> và quỹ đạo như vầy, và ta cần tính công của lực khi khiến điểm di chuyển
> trên quỹ đạo như vậy

<br>

<a id="node-471"></a>

<p align="center"><kbd><img src="assets/03996b7d261fe0dc2080fb50059a5f9c5938708a.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi như vậy ta cần tính tích phân (theo t) từ t = 0 đến t = 1,
> của F dot product với (velocity vector dr/dt * dt)

<br>

<a id="node-472"></a>

<p align="center"><kbd><img src="assets/5e01121583bce97d13a52a1340c5067b571f8e9c.png" width="100%"></kbd></p>

> [!NOTE]
> Và với việc vector field định nghĩa F = - y*i + x*j tức là tại (x,y) thì
> vector F = (-y, x) ta thay x = t, y = t^2 thì ta có F = <-t^2, t>
>
> Và x=t thì dx = dt <=> dx/dt = 1
>
> Cái này dựa trên Implicit differentiation nếu f là hàm theo x: f(x) thì
> df = f'(x)dx
>
> thì tương tự x là hàm theo t: x(t) = t ta có dx = x'(t)dt = 1*dt
>
> và y = t^2 nên dy = 2tdt <=> dy /dt = 2t
>
> vậy dr/dt (chú ý, nhớ rằng nó là VELOCITY VECTOR - SẼ CÓ
> HAI COMPONENT LÀ DX/DT VÀ DY/DT)
>
> Sẽ là: <1, 2t>

<br>

<a id="node-473"></a>

<p align="center"><kbd><img src="assets/e8f94420a0fd577f4d51508e454bd53d3c45e9ca.png" width="100%"></kbd></p>

> [!NOTE]
> Và dot product F và velocity ta có t^2. Tích phân từ 0 đến 1
> của t^2dt = nguyên hàm của t^2 | 0:1 = (1/3)t^3 | 0: 1= 1/3

<br>

<a id="node-474"></a>

<p align="center"><kbd><img src="assets/603d2b0fb2a80d21cf3b386202fd5c8d944f705d.png" width="100%"></kbd></p>

> [!NOTE]
> Có câu hỏi là sao không tính dot product của F và dr (và
> integrate) theo r thì gs nói ta không biết cách làm theo kiểu đó, vì
> r là position vector

<br>

<a id="node-475"></a>

<p align="center"><kbd><img src="assets/6cbac84ba2d0bd29ecaaa9fa2d5fbf0cb4e46bf8.png" width="100%"></kbd></p>

> [!NOTE]
> gs trả lời một câu hỏi của student nội dung đại khái là trong tình
> huống ở đây, ta chỉ cố gắng tính Công của lực tác động lên một
> object di chuyển với quỹ đạo cho trước. Chứ ta không (mặc dù có
> thể) xét đến việc tìm ra quỹ đạo dựa trên lực tác động - đây là bài
> toán khác, liên quan đến giải phương trình vi phân mà ta có thể học
> trong 1803

<br>

<a id="node-476"></a>

<p align="center"><kbd><img src="assets/37d371ae91d96cf2eb529a95ee4228215830ddb5.png" width="100%"></kbd></p>

🔗 **Related:** [LEC 20: PATH INDEPENDENCE & CONSERVATIVE FIELD](untitled.md#node-496)

> [!NOTE]
> Tiếp gs sẽ nói về một cách giải khác, liên quan đến việc dùng trực
> tiếp (vector) dr thay vì chuyển thành [vector velocity dr/dt nhân với
> dt]
>
> Cách làm này, ta có gọi dr là vector có hai component là dx, dy.
>
> Thì tích phân trên C của dot product(F, dr) sẽ trở thành tích phân trên C 
> của (Mdx + Ndy)
>
> Thế thì, gs nói rằng, đại khái là tích phân này trông qua thì có vẻ là tích
> phân của 2 biến x, y. Nhưng thực chất dựa trên một quỹ đạo C thì x,y liên
> quan nhau. Do đó thực ra tích phân này chỉ là của 1 variable và ta sẽ 
> chuyển tích phân này về 1 variable x., hoặc y hoặc t

<br>

<a id="node-477"></a>

<p align="center"><kbd><img src="assets/6c48ff63a9835037a41c79fd3e01aaf8dd8c172f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6c48ff63a9835037a41c79fd3e01aaf8dd8c172f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/82ce556011783a32dc69623793f4f53d326e1810.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì phương pháp ta sẽ làm đó là, thể hiện x, y dưới dạng
> single variable t và thế vào. Ghi lại tích phân Fdr theo  cách
> trên F = <M,N> = <-y, x> (do cho F = -y*i + x*j) ta có tích phân
> của -ydx + xdy.

<br>

<a id="node-478"></a>

<p align="center"><kbd><img src="assets/9fad5d83283b29ee1ba2b80d766a3bf89043d202.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi thì từ x = t, y = t^2, như hồi nãy ta dùng implicit
> differentiation cho ta dx = dt và dy = 2tdy thế vào tích phân ta
> có tích phân (over C) của -t^2dt + t*dtdt

<br>

<a id="node-479"></a>

<p align="center"><kbd><img src="assets/0f88051b7ce08534de03dfd3d24f541bff432040.png" width="100%"></kbd></p>

> [!NOTE]
> Và giải tiếp y như
> hồi nãy ra 1/3

<br>

<a id="node-480"></a>

<p align="center"><kbd><img src="assets/853336972c1b9f2253dfca12dd4ee8edbcc26cf2.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/853336972c1b9f2253dfca12dd4ee8edbcc26cf2.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0b0fb088445d2927685eccb51cc02d12dc8b7e40.png" width="100%"></kbd></p>

> [!NOTE]
> Như vậy phương pháp là cho quỹ đạo c thì ta cần thể hiện x, y theo
> cùng 1 parameter và ta sẽ chọn parameters nào (ở đây là t)
>
> Gs nói rằng ta có thể chọn x = sin(theta) y = sin(theta) ^2 nhưng trong
> trường hợp này sẽ rất khó làm (not practical) (đã nói là ta chọn, nên ta
> cần phải chọn parameter để express x, y sao cho hợp lý)
>
> Hoặc ta có thể express y theo x và tính integral này theo x.

<br>

<a id="node-481"></a>

<p align="center"><kbd><img src="assets/861a914500d122616fd942c468d37ee3404b976c.png" width="100%"></kbd></p>

> [!NOTE]
> Gs nhắc lại vừa rồi là cách general để làm line integral: ta tìm cách
> express mọi parameters bởi một parameter nào đó và từ đó ta có
> một integral theo single parameter duy nhất để tính

<br>

<a id="node-482"></a>

<p align="center"><kbd><img src="assets/83c4554e01af2a68037f6b107956e817a668d97b.png" width="100%"></kbd></p>

> [!NOTE]
> Gs nói qua cách tiếp cận hình học của vấn đề này. Đầu tiên gs muốn
> ta ôn lại về ý nghĩa của dr.
>
> Đó là bắt đầu từ delta_r là một vector thể hiện sự thay đổi rất nhỏ của
> object trên quỹ đạo, thì ta đã biết ở bài trước, rằng khi chia nhỏ quỹ
> đạo ra thành những phần rất nhỏ delta_r -> 0, thì vector delta_r có
> thể coi như trùng với phương của tiếp tuyến của quỹ đạo tại điểm
> đang xét. gọi T là vector tiếp tuyến đơn vị (unit tangent vector) thì ta
> có delta_r trùng phương với T^ (đương nhiên có độ lớn = 1)
>
> Còn độ lớn của delta_r thì bằng delta_s với s là chiều dài của quỹ
> đạo

<br>

<a id="node-483"></a>

<p align="center"><kbd><img src="assets/52b4f3d63645650a72e02cc5995e3c1c7ff1d77c.png" width="100%"></kbd></p>

> [!NOTE]
> Từ đó dr  = <dx, dy> = T^.ds (dấu mũ của T thể hiện là vector
> đơn vị, giống như i^, j^ vậy)
>
> là vector mà trùng phương với tangent và có độ lớn bằng ds

<br>

<a id="node-484"></a>

<p align="center"><kbd><img src="assets/4ccaac4e6dd027111d9c8145b5182aa162aa30e2.png" width="100%"></kbd></p>

> [!NOTE]
> Hoặc là có thể hiểu theo cách khác chia dr cho dt ta có dr/dt là
> velocity vector, khi đó tương ứng sẽ là T^. ds/dt mang ý nghĩa:
> velocity vector sẽ cùng phương với vector tiếp tuyến tại điểm đang
> xét với độ lớn là ds/dt chính là "đạo hàm của "độ dài quãng đường"
> đối với thời gian" - thì chính là độ lớn vận tốc.

<br>

<a id="node-485"></a>

<p align="center"><kbd><img src="assets/c013f7e6bb3286e630351cb8b1037a1ef591a29c.png" width="100%"></kbd></p>

> [!NOTE]
> Từ đó, tích phân (over C) F.dr có thể trở thành (hoặc được tính
> theo cách khác) tích phân (over C) {F dot product với T^} ds với ý
> nghĩa là ta sẽ project vector force F lên hướng / phương của tiếp
> tuyến tại đó và integrate nó dọc theo (along) the curve

<br>

<a id="node-486"></a>

<p align="center"><kbd><img src="assets/edaadd7da5611d8fbb96d3781e42340f98770c59.png" width="100%"></kbd></p>

> [!NOTE]
> Đại ý là gs cho rằng làm theo cách này sẽ phát huy ưu điểm khi quỹ
> đạo và vector field có liên hệ hình học với nhau. Lấy ví dụ ta có quỹ
> đạo (trajectory) C là (đi theo) đường tròn bán kính a tâm tại gốc tọa
> độ và đi theo hướng ngược chiều kim đồng hồ. Còn vector field F =
> x*i^ + y*j^ là vector field mà ta đã nói ở đầu bài
>
> Gs nói khi dùng line integral để tính công của lực F đối với object di
> chuyển theo quỹ đạo này thì nếu ta nắm / nhớ vật lí thì ta sẽ expect
> / dự đoán nó bằng 0, Vì lực luôn vuông góc với hướng di chuyển

<br>

<a id="node-487"></a>

<p align="center"><kbd><img src="assets/4a872f12ddf43a91859400ac5393db799264cad4.png" width="100%"></kbd></p>

> [!NOTE]
> thế thì trong trường hợp này, tại một điểm bất kì trên
> quỹ đạo, ta có vector T - vector tiếp tuyến sẽ vuông
> góc với vector với vector lực F.

<br>

<a id="node-488"></a>

<p align="center"><kbd><img src="assets/08659c949b7ceb6ebd45e2567e0740fb1456d30c.png" width="100%"></kbd></p>

> [!NOTE]
> do đó dot product của vector F và T là bằng 0 nên integral over c của F.
> T. ds dĩ nhiên là bằng 0
>
> Đây là ví dụ cho thấy trong bài toán cụ thể này khi ta có liên hệ hình học
> giữa vector field F và trajectory (F vuông góc với quỹ đạo) thì việc tính
> line integral theo cách này dễ hơn rất nhiều (mặc dù nếu ta tính theo
> cách 2, đó là express x, y theo parameter nào đó chẳng hạn như
> sin(theta) và cos(theta) thì ta cũng sẽ cho ra kết quả như vậy như cách
> kia rõ ràng là nhanh nhất

<br>

<a id="node-489"></a>

<p align="center"><kbd><img src="assets/0ef7a6b985241594e85c9384cd19251c91666457.png" width="100%"></kbd></p>

> [!NOTE]
> Cuối cùng làm một ví dụ: Cùng quỹ đạo C, nhưng vector field F khác
> F = -y*i^ + x*j^
>
> Lúc này vector F song song với vector T, nên ta đã biết F.T = |F|.|T|.
> cos(góc giữ chúng) = |F|*1*1 = |F|
>
> Và |F| = a (vì component của F là -y, x nên |F| = sqrt[(-y)^2 + x^2]
> = sqrt r^2 = r = a

<br>

<a id="node-490"></a>

<p align="center"><kbd><img src="assets/c928ef9304326e4695341cff82de8ef1834e034b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c928ef9304326e4695341cff82de8ef1834e034b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7a0e8e527c74a1d3e505a647a85ac2922c72e657.png" width="100%"></kbd></p>

> [!NOTE]
> Do đó tích phân over C của F. T ds trở thành tích phân over c a ds
>
> Với a là constant đưa ra ngoài ta còn **tích phân over c ds
>
> và tích phân trên quỹ đạo c của ds thí CHÍNH LÀ CHIỀU DÀI 
> QUỸ ĐẠO c -> 2pi*a
>
> Vậy kết quả là 2pi*a^2**

<br>

<a id="node-491"></a>

<p align="center"><kbd><img src="assets/67c60396d39af106469027f344296d59cb3aba52.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/67c60396d39af106469027f344296d59cb3aba52.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/64dcc8f03001cf6a438e6696c7b906c8ca11493e.png" width="100%"></kbd></p>

> [!NOTE]
> Hoặc nếu tính bằng cách '2' đó là thể hiện x, y theo theta  ta sẽ có tích
> phân over c -ydx + xdy = tích phân từ 0 đến 2pi của a^2(sin^2 theta
> +cos^2 theta) dtheta = a^2 tích phân 0:2pi dtheta = a^2 2pi

<br>

