# Lecture 5: Transpose, Permutations, Spaces R^n

📊 **Progress:** `23` Notes | `24` Screenshots

---
<a id="node-106"></a>

<p align="center"><kbd><img src="assets/5d235f406219cfd7bd58d38bfd47417599f38b57.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là, tóm tắt lại, là ta có **quá trình elimination** để **dần dần đưa
> A thành U**, và quá trình đó **đảo ngược lại bằng L (để biến U ngược lại
> thành A)**.
>
> Thế thì, gs nói đương nhiên để làm được vậy **A phải là good matrix**
> tức **invertible matrix**. Nhưng sẽ c**ó lúc ta cần row exchange**. Vậy
> thể hiện sự tham gia của row exchange vào chính là bằng **matrix P để
> ta có PA=LU**

<br>

<a id="node-107"></a>

<p align="center"><kbd><img src="assets/be54d355f2e27138edd3de172e030107fc57fa28.png" width="100%"></kbd></p>

> [!NOTE]
> Từ bài trước mình đã thấy **Permutation matrix là identity matrix nhưng
> thay đổi row**. Và có thể **coi** **I là basic permutation matrix**

<br>

<a id="node-108"></a>

<p align="center"><kbd><img src="assets/b098d4ea5546605bb2011c798916a7684db3b4ea.png" width="100%"></kbd></p>

> [!NOTE]
> **Số lượng các reordering khả dĩ là n giai thừa**. Và permutation matrix
> có tính chất đặc biệt là **P**_**inv chính là `P_transpose`
>
> `P_inv` `=` P.T**

<br>

<a id="node-109"></a>

<p align="center"><kbd><img src="assets/421a187d739580dd2da483ed6b5227fb18919e98.png" width="100%"></kbd></p>

<br>

<a id="node-110"></a>

<p align="center"><kbd><img src="assets/2d7539fcd376e9326802b09769005b4654055a74.png" width="100%"></kbd></p>

> [!NOTE]
> Khái quát của transpose

<br>

<a id="node-111"></a>

<p align="center"><kbd><img src="assets/844250914a09eee3d162702be82563c210643999.png" width="100%"></kbd></p>

> [!NOTE]
> **Symmetric matrix** là matrix
> transpose ko thay đổi gì

<br>

<a id="node-112"></a>

<p align="center"><kbd><img src="assets/c53e753bd20d9450aa9c3970d7aa23e62903405c.png" width="100%"></kbd></p>

> [!NOTE]
> Gs nói tôi nghĩ là **nếu lấy một rectangular matrix
> nhân với transpose của nó ta sẽ dc một symmetric
> matrix**

<br>

<a id="node-113"></a>

<p align="center"><kbd><img src="assets/94ceb8ec17be23451293b570ea48bb2334c942de.png" width="100%"></kbd></p>

> [!NOTE]
> Tính thử thì thấy nó đối xứng thật. Nhưng **ta cần
> chứng minh điều này theo cách chính thức hơn**

<br>

<a id="node-114"></a>

<p align="center"><kbd><img src="assets/d2c4bea589be2a899e24af7a9c1e929e3f5feb40.png" width="100%"></kbd></p>

> [!NOTE]
> Bằng cách **xem thử transpose của (RT)R có là chính nó hay ko**. Thế
> thì dựa vào luật giống như inverse: (AB)T `=` (BT)(AT) ta có ((**RT)R**)T ra
> dc lại (RT)((RT)T) là (**RT)R
>
> Như vậy (RT)R khi lấy transpose được chính nó suy ra nó là symmetric
> matrix**

<br>

<a id="node-115"></a>

<p align="center"><kbd><img src="assets/a54ea5c25f3aa83cb8f38bf4cb019d564aae7e03.png" width="100%"></kbd></p>

> [!NOTE]
> Gs nói qua **VECTOR SPACE**. Thế thì đầu tiên gs cho rằng ta **có thể
> add hai vector**, **có thể nhân vector với một số (scalar)**. Vậy **vector
> space là một không gian vector** cho phép ta **thực hiện hai operations
> đó và một số rule.**
>
> Ta đã gặp khái niệm **linear combination** ở bài trước. Trong không
> gian vector **R2**, tức là **số thực (Real `-` R), 2 chiều**

<br>

<a id="node-116"></a>

<p align="center"><kbd><img src="assets/5ae4aa53613bf6ccb1dbe249964b9ea52286a250.png" width="100%"></kbd></p>

> [!NOTE]
> Ví dụ một số vector

<br>

<a id="node-117"></a>

<p align="center"><kbd><img src="assets/ffdf2d8447c13524d9e95583ced6f9f47f6cf99e.png" width="100%"></kbd></p>

> [!NOTE]
> Như đã biết ta có thể vẽ nó ra như vầy. Thế thì gs định nghĩa v**ector
> space R2 chính là toàn bộ mặt phẳng**.
>
> Ta có thể nói **toàn bộ** là bởi vì, **giả sử ta lấy đi vector [0,0]**, để có
> **kiểu như mặt phẳng nhưng thủng một lỗ** thì **ta sẽ không còn thỏa
> mãn yêu cầu,** là, **ví dụ vector [3 2] nhân với một scalar 0 sẽ dc một
> vector cũng trong vector space đó** hay khi cộng với vector `[-3` `-2]` thì dc
> vector cũng nằm trong vector space

<br>

<a id="node-118"></a>

<p align="center"><kbd><img src="assets/dcebf883b4fda7f06c38717511cccb9587f317f1.png" width="100%"></kbd></p>

> [!NOTE]
> Như vậy vector space **R^n** là **mọi vector có n** **component giá trị
> thực**. Thỏa quy định **cộng 2 vector hay nhân vector với scalar sẽ dc
> một vector vẫn nằm trong space**

<br>

<a id="node-119"></a>

<p align="center"><kbd><img src="assets/8091044eebc72c8f897a079cfbf1e612ed58f313.png" width="100%"></kbd></p>

> [!NOTE]
> Gs **ví dụ một cái ko phải là vector space**: **tập mọi vector ko âm**..
> thì cái này **thỏa mãn khi cộng hai vector nó vẫn nằm trong góc phần
> tư này**. Nhưng **ko thỏa yêu cầu nhân, vì nhân với số âm nó sẽ ko
> còn trong góc này nữa**

<br>

<a id="node-120"></a>

<p align="center"><kbd><img src="assets/5e0564aa1722cfbe1a89848680e11bfbc044b61d.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì ta sẽ đi **tìm một "vùng" thỏa tính chất của vector
> space,** **nằm trong R2**. Nó dc gọi là **SUBSPACE của R2**

<br>

<a id="node-121"></a>

<p align="center"><kbd><img src="assets/909d6932bb01b245a99f38107388a283d348a55d.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì, thử check một line ta thấy rằng **khi nhân một
> vector trên line này với bất kì số nào** ta cũng **vẫn dc một
> vector nằm trên line đó**. Và **dễ thấy cộng cũng vậy**. Vậy
> nó**(line) là một subspace của R2**

<br>

<a id="node-122"></a>

<p align="center"><kbd><img src="assets/38010d95a5fde65c930a107d44b0c9dee41328a9.png" width="100%"></kbd></p>

🔗 **Related:** [LECTURE 6: COLUMN SPACE AND NULL SPACE](untitled.md#node-145)

🔗 **Related:** [LECTURE 6: COLUMN SPACE AND NULL SPACE](untitled.md#node-152)

> [!NOTE]
> Nhưng check **một line khác ko đi qua origin** thì thấy
> **ko thỏa luật**. À **như vậy line phải đi qua O thì mới là
> subspace.**
>
> Và **MỌI SUBSPACE PHẢI CHỨA GỐC 0**, vì **nó phải cho
> phép một vector nhân với 0** **để ra kết quả vẫn thuộc
> vector space.**

<br>

<a id="node-123"></a>

<p align="center"><kbd><img src="assets/7186cc786aca8358af4a7deab50d62234749565b.png" width="100%"></kbd></p>

> [!NOTE]
> Thử **list các subspace của R2**. Thì có
>
> 1. Là **bản thân R2**
>
> 2. Là **mọi line đi qua gốc 0**
>
> 3. Và một cái thú vị **chính là bản thân cái gốc 0** **cũng
> là một subspace** vì nó **cũng thỏa luật**. Lấy vector
> trong đó, đương nhiên chỉ có 1 vector là [0,0] đem nhân
> với mọi số đều ra [0,0] thuộc subspace và cộng [0,0] với
> [0,0] cũng ra [0,0] thuộc subspace

<br>

<a id="node-124"></a>

<p align="center"><kbd><img src="assets/a8c8576ee6413d6872a8e42730e542a214946bea.png" width="100%"></kbd></p>

> [!NOTE]
> Với R3 thì subspace của nó có thể là một line đi qua O,
> một plane đi qua O hoặc bản thân O

<br>

<a id="node-125"></a>

<p align="center"><kbd><img src="assets/b272c0225c4114358fdf85ba9dbdf588eae240de.png" width="100%"></kbd></p>

🔗 **Related:** [LECTURE 9: INDEPENDECE, BASIS, AND DIMENSION](untitled.md#node-238)

> [!NOTE]
> Gs mới nói qua việc **tạo subspace từ các column của matrix.**vậy đương nhiên nó phải thỏa:
>
> 1. **Nhâ**n với column với **scalar bất kì** cũng được **vector
> thuộc vector space** và
>
> 2. **Cộng hai column vector** a với b cũng **vẫn thuộc vector
> space.**
>
> Vậy gs cho rằng **subspace này chính là mọi linear
> combination của hai column vector**Nói thêm chỗ này để hiểu rõ hơn một chút. Như ta đã biết
> định nghĩa của vector space, là phải thỏa điều kiện rằng khi
> cộng hai vector với nhau hoặc khi nhân vector với một scalar
> bất kì thì kết quả ta được một vector vẫn nằm trong tập hợp
> đó. Khi đó nó mới thỏa điều kiện là  vector space.
>
> Vậy thì, khi xét mọi linear combination của hai columns vector
> của một matrix, thì ta sẽ dễ thấy rằng, khi lấy hai vector (mà
> mỗi cái là một linear combination của hai cols vector) cộng với
> nhau, đương nhiên ta vẫn sẽ được một linear combination
> khác của hai cols vector, do đó vector kết quả này vẫn nằm
> trong tập hợp mọi linear combination của hai cols vector.
>
> Tương tự khi scale một linear combination của hai cols vector
> ta cũng có một linear combination khác của hai cols vector.
> Thành ra khi xét tập mọi linear combination của hai cols
> vector của một matrix, thì nó thỏa hai tính chất cần thiết của
> vector space. Vậy nó là một vector space. Và nó có tên là
> Column Space

<br>

<a id="node-126"></a>

<p align="center"><kbd><img src="assets/cadbe4cd2000d43fca1f97382f0083c76bbe50bf.png" width="100%"></kbd></p>

> [!NOTE]
> Và nó có tên gọi là **Column Space** của **matrix A kí hiệu
> là C(A)**

<br>

<a id="node-127"></a>

<p align="center"><kbd><img src="assets/089666a5141182b3e7ddea5ca8253e16edc177de.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì, nếu ta **vẽ col1 col2 ra thì Column space sẽ vầy.**
> Chính là **mặt phẳng tạo bởi hai col**

<br>

<a id="node-128"></a>

<p align="center"><kbd><img src="assets/e430985911bda78174a5424dc6d60248c5caa621.png" width="100%"></kbd></p>

> [!NOTE]
> Đúng là vậy, nó **chính là một plane đi qua hai column vector** và
> **đương nhiên qua gốc 0**.
>
> Gs cho rằng cái này **rất quan trọng**. Hình ảnh**lấy 2 vector trong
> R3  sẽ tạo một subspace của R3 là một không gian 2 chiều `-` plane**
> (chú ý là **ko phải R2 nhé, vì vector có 3 component**)
>
> Giúp ta**hình dung bài toán khác trong vector space R10**,**lấy
> combination của 5 vector** sẽ **tạo một subspace của R10** là
> **một không gian 5 chiều**. (ko phải R5, vì vector có 10 component)
>
> Tất nhiên **còn tùy 5 vector ntn**, **vì nếu chúng cùng trên 1 line thì
> subspace đó sẽ chỉ là 1 line đi qua gốc 0** như đã biết, nhưng "
> maximum" thì chúng nó sẽ tạo một không gian 5D trong R10 (giống
> như mặt phẳng 2D trong không gian 3D R3)

<br>

<a id="node-129"></a>

<p align="center"><kbd><img src="assets/7b427d851bd7398fab6aef5f03637a3ef0863884.png" width="100%"></kbd></p>

> [!NOTE]
> Bài sau ta sẽ bắt đầu **nhìn nhận Ax=b** ở một cấp
> độ cao hơn với **vector space** và **subspace**

<br>

