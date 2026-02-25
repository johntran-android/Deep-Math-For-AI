# Lec 2: Limits

📊 **Progress:** `28` Notes | `32` Screenshots

---
<a id="node-29"></a>

<p align="center"><kbd><img src="assets/bccea28f4cd114587a3d84c95b215daadab136c9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/bccea28f4cd114587a3d84c95b215daadab136c9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/77e710e0eaeffc7ebadd6221a981d2dd92fa20d4.png" width="100%"></kbd></p>

> [!NOTE]
> Gs: tuần trước ta đã học về định nghĩa của derivative: là độ dốc (slope)
> của tiếp tuyến. Sau đó ta đã tính derivative của một số function như
> 1/x, x^n

<br>

<a id="node-30"></a>

<p align="center"><kbd><img src="assets/00009ecc5cf5bd64e58cba26c6eb355bcde252d2.png" width="100%"></kbd></p>

> [!NOTE]
> Đại ý là, bài trước ta đã hiểu về derivative là như vậy (độ dốc
> của tiếp tuyến). Nhưng hôm nay ta sẽ tiếp tục bàn về ý nghĩa
> của derivative nhưng ở GÓC NHÌN THỨ 2, gs cho rằng đây là
> cái RẤT QUAN TRỌNG. Đó là hiểu về derivative theo ý nghĩa:
> RATE OF CHANGE

<br>

<a id="node-31"></a>

<p align="center"><kbd><img src="assets/ab03c44bf7f817c69902e05080b76a2735d0b608.png" width="100%"></kbd></p>

> [!NOTE]
> Ở góc nhìn thứ hai này, khi x change một khoảng delta_x, thì /
> và function change một khoảng delta_y. Thì delta_y / delta_x giống 
> như rate of change trung bình. Và khi xét trên một khoảng vô cùng
> nhỏ, thì nó trở thành dy/dx mang ý nghĩa là rate of change tức thời
> (instantaneous)

<br>

<a id="node-32"></a>

<p align="center"><kbd><img src="assets/24960efa11c953f2e7100509eacc0aabebe45559.png" width="100%"></kbd></p>

> [!NOTE]
> Gs lấy ví dụ như s là quãng đường di
> chuỷên thì ds/dt là vận tốc

<br>

<a id="node-33"></a>

<p align="center"><kbd><img src="assets/5fed9164443ead9d6723e92ab5fa31bc546c1320.png" width="100%"></kbd></p>

> [!NOTE]
> Lấy ví dụ ta thả quả dưa từ sân thượng xuống đất, và độ cao của quả
> dưa được thể hiện theo t bởi h = 80 - 5*t^2. Thế thì, tại t = 0, h = 80.
> Còn tại t = 4, h = 0. Từ đó ta tính delta_h / delta_t = -20 m/sec. Và đây
> mang ý nghĩa là average speed

<br>

<a id="node-34"></a>

<p align="center"><kbd><img src="assets/4967686c0d015783651cc4eaec8d1c4525e36ef0.png" width="100%"></kbd></p>

> [!NOTE]
> Nhưng cái mà ta quan tâm là vận tốc tức thời. Ta sẽ lấy derivative
> của h w.r.t t: dh/dt. Và sử dụng công thức mà ta đã chứng minh là d
> x^n / dx = n*x^(n-1) với n=0,1,2...
>
> Thì d 80 / dt coi như d 80*t^0 /dt = 80*0*t^-1 = 0. Và d t^2 / dt = 2t từ
> đó ta có dh/dt = -10t
>
> Từ đó khi t = 4, ta có vận tốc tức thời là -40 m/s

<br>

<a id="node-35"></a>

<p align="center"><kbd><img src="assets/9700233dce282b31803a8e97b05fd63526f7005c.png" width="100%"></kbd></p>

> [!NOTE]
> Ta sẽ học qua Limit và Continuity. Gs cho rằng nó sẽ giúp ta derive
> mọi công thức derivative mà ta sẽ cần cho việc vi tích phân
>
> Thế thì đầu tiên gs nói ông cho rằng có hai loại limit, loại thứ nhất
> là "Easy" limit ví dụ như cái này lim x-> 4 của (x+3)/(x^2+1) thì
> để tính limit này chỉ việc thế x = 4 vào là xong.

<br>

<a id="node-36"></a>

<p align="center"><kbd><img src="assets/45d419008398a91c7400bac1e68f2b22f2f10128.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì loại thứ hai, mà điển hình là khi ta tính derivative, theo định nghĩa
> mà bài trước đã học, nó là limit của tỉ lệ giữa delta f = f(x0+deltax) - f(x0)
> với delta x = x - x0 khi x -> x0
>
> Thì nếu thế x = x0 vào thì ta luôn có dạng 0/0. Do đó ta cần một số cách
> làm khác.

<br>

<a id="node-37"></a>

<p align="center"><kbd><img src="assets/ac737df801f9cb9e3d3565365a52f2a971b1e225.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp gs nói về right-hand limit và left-hand limit. Với right-hand limit
> kí hiệu là lim x-> x0+ f(x) thì có nghĩa là x > x0 và do đó nó tiếp cận
> x0 từ bên phải (right-hand)

<br>

<a id="node-38"></a>

<p align="center"><kbd><img src="assets/9cdd5ea9b8c561e6fe56193ea0bf505e43096faf.png" width="100%"></kbd></p>

> [!NOTE]
> Ngược lại left-hand limit là  lim x->x0- f(x) có nghĩa là x < x0,
> và tiến về x0 ở bên trái

<br>

<a id="node-39"></a>

<p align="center"><kbd><img src="assets/ef660d7bc4d1e21084ba95a09645dac62c46470b.png" width="100%"></kbd></p>

> [!NOTE]
> Gs cho một ví dụ về function f(x) như vầy, tức là khi x>0 thì f(x) = x+1
> và khi x<0 thì f(x) = -x+2
>
> Vậy, khi dễ hiểu tính lim x->0+ của f(x) thì nó sẽ chính là lim x->0 của
> x+1 và bằng 1. Và ngược lại khi tính lim x->0- của f(x) thì nó chính là
> lim x->0 của -x+2 và kết qủa ra 2

<br>

<a id="node-40"></a>

<p align="center"><kbd><img src="assets/34c1be34f02ece4070bb99eb53c8c05fb9b3e483.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì nếu ta muốn define thêm tại x = 0 thì f(x) như thế nào (vì
> vừa rồi vẫn chưa biết x = 0 thì f ra sao) thì ta có thể dùng notation
> như vầy, ví dụ x>=0 thì f(x) = x+1 thì hình ảnh thường được dùng
> là tại x = 0 ở phần đồ thị x+1 sẽ là dấu chấm đặc. Còn tại x = 0 ở
> nhánh -x+2 là vòng tròn rỗng

<br>

<a id="node-41"></a>

<p align="center"><kbd><img src="assets/0adee7709545b050a9e9890612e6fe97fd7cee51.png" width="100%"></kbd></p>

🔗 **Related:** [LEC 4: CHAIN RULE](untitled.md#node-84)

> [!NOTE]
> Ta sẽ biết về định nghĩa của của khái niệm tính continuous của hàm f
> đó là, khi nói hàm f liên tục tại x0 thì điều này có nghĩa là lim x->x0 f(x)
> = f(x0)

<br>

<a id="node-42"></a>

<p align="center"><kbd><img src="assets/4719dc5e2fb0bf1f714be49588a01ee731e241f1.png" width="100%"></kbd></p>

> [!NOTE]
> Và điều đó hàm chứa 3 ý nghĩa sau:
>
> 1) limit của f(x) khi x->x0 tồn tại cả từ bên trái lẫn bên phải (left-hand
> và right-hand) và chúng bằng nhau.
>
> 2) f(x0) có xác định
>
> 3) Và chúng bằng nhau

<br>

<a id="node-43"></a>

<p align="center"><kbd><img src="assets/cbacd1f59562ac838b45b94b84be752ba6bbb542.png" width="100%"></kbd></p>

> [!NOTE]
> Gs nói đại khái là, điều cần lưu ý của định nghĩa này đó là nó có
> nghĩa là hai phần hoàn toàn khác nhau. Ví dụ, phần bên trái khi 
> tính sẽ không dính gì đến x0. Còn phần bên phải thì thì là easy
> limit, tức là có thể gắn x0 vào để có kết quả.
>
> Chưa hiểu lắm nhưng có thể sẽ rõ hơn khi làm qua các ví dụ

<br>

<a id="node-44"></a>

<p align="center"><kbd><img src="assets/5b1d00d5b989b17dbaf992a050e495612284f031.png" width="100%"></kbd></p>

> [!NOTE]
> Và từ đó ta có khái niệm JUMP DISCONTINUITY (bước nhảy gián
> đoạn). Đó chính là trong ví dụ hồi nãy, khi right-hand limit và left-hand
> limit đều tồn tại nhưng hai cái không bằng nhau.

<br>

<a id="node-45"></a>

<p align="center"><kbd><img src="assets/558f76cd3b9490a2f7be0930ed3e752ac6213626.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp theo là một khái niệm nữa gọi là REMOVABLE DISCONTINUITY,
> Đại khái là khi ta có một function có limit bên trái và bên phải bằng nhau
> nhưng giống như tron hình ảnh này, function liên tục nhưng bị thiếu 
> một điểm tạo thành một cái lỗ như vầy, mà tại đó có thể function không
> xác định hoặc thể hiện bởi cái điểm ở trên.

<br>

<a id="node-46"></a>

<p align="center"><kbd><img src="assets/76b7f88295569f59324ab8cb446d4d1e042f3007.png" width="100%"></kbd></p>

> [!NOTE]
> Gs lấy ví dụ là function g(x) = sin(x) / x và h(x) = (1-cos(x)) / x. Cả
> hai đều là các function removable discontinuity tại x = 0.

<br>

<a id="node-47"></a>

<p align="center"><kbd><img src="assets/dca844979643bea87b09cc9ebdd99b5648ed6ff7.png" width="100%"></kbd></p>

> [!NOTE]
> Và cuối bài hoặc bài sau ta sẽ chứng minh, tính ra limit
> của chúng khi x -> 0 thật sự sẽ là 1. Trong khi đó dễ thấy
> cả hai đều không xác định tại x = 0

<br>

<a id="node-48"></a>

<p align="center"><kbd><img src="assets/44e08c13063562eca5a278f1f582b9bdf44babb8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/44e08c13063562eca5a278f1f582b9bdf44babb8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/673865a75cd0eb403e5564ae9a39062c7d368373.png" width="100%"></kbd></p>

> [!NOTE]
> Gs nói tiếp về dạng DISCONTINUITY thứ 3 là INFINITE
> DISCONTINUITY. Lấy ví dụ này, khi ta có hyperbola y = 1/x. Khi đó, ta
> sẽ có right hand  limit tại x sẽ là = + infinity còn left hand limit tại x sẽ là
> -infinity (có thể thấy trên đồ thị nếu ta đi về 0 từ bên phải thí nhánh
> hyperbola sẽ vọt  lên, ngược lại nếu ta đi từ bên trái thì f sẽ cắm đầu
> xuống -> -infinity)
>
> Gs cũng nói một số sách ghi là limit 1/x tại x -> 0 = infinity là sai.

<br>

<a id="node-49"></a>

<p align="center"><kbd><img src="assets/f2472678b56f8c3ffa8d6a697ba8727fd80a9780.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp gs nói về việc ta đã biết derivative của y: y' = -1 / x^2. Và nếu
> vẽ đồ thị của nó ra thì nó sẽ như vầy.
>
> Gs nhấn mạnh rằng, sẽ sai lầm nếu ta nghĩ đồ thị của derivative
> phải giống giống đồ thị của hàm f. Bởi vì nên nhớ ý nghĩa derivative
> là độ dốc. Nên đồ thị của y' sẽ thể hiện sự thay đổi của độ dốc.

<br>

<a id="node-50"></a>

<p align="center"><kbd><img src="assets/32cf2d59d1e7cb056ab82e64387a65a9c38f472e.png" width="100%"></kbd></p>

> [!NOTE]
> Và với f' thì cả left và right limit của nó tại 0 đều bằng -infinity. Nhưng
> again, nó không xác định tại x = 0 và đây cũng là function có tính 
> infinity discontinuity tại 0

<br>

<a id="node-51"></a>

<p align="center"><kbd><img src="assets/f8b2fd026aee2e0353f69b137351fb56c7641cf5.png" width="100%"></kbd></p>

> [!NOTE]
> Một điểm nữa gs cho biết, y = 1/x là hàm lẻ (là hàm mà f(x) = -
> f(-x) thì derivative của nó gs nói rằng sẽ luôn là hàm chẵn
> (event) (là hàm mà g(x) = g(-x))

<br>

<a id="node-52"></a>

<p align="center"><kbd><img src="assets/5c0d3892aea452eb99cea9616aef687d8c6e459b.png" width="100%"></kbd></p>

> [!NOTE]
> Một dạng cuối cùng gọi là OTHER UGLY DISCONTINUITIES, ví
> dụ hàm y =sin(1/x), khi x->0 thì không có cả left lẫn right hand
> limit. Nhưng gs nói trong class này ta sẽ không gặp các function
> như vậy

<br>

<a id="node-53"></a>

<p align="center"><kbd><img src="assets/2ec7f8e15e9117c3d768d0e60c6216c3806590b4.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp theo ta sẽ học một Theorem quan trọng nói rằng: Nếu hàm f
> **differentiable** (khả vi) tại x0 thì đồng nghĩa nó cũng sẽ **continuous**
> tại x0

<br>

<a id="node-54"></a>

<p align="center"><kbd><img src="assets/a93792ecca909680ce465ef8916db2d50b45d3ab.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì để chứng minh theorem này, cái ta chỉ cần chứng minh là
> **limit của f(x) - f(x0) tại x0 là bằng 0**.
>
> Vì khi đó cũng đồng nghĩa là**limit của  f(x) tại x->x0 là bằng f(x0)(*)**
> và đây chính là định nghĩa rằng f continuous tại x0
>
> (*) vì sao vì khi x->0 mà khác biệt giữa f(x) và f(x0) = 0 thì trừ hai vế
> cho f(x0) thì ta sẽ đồng nghĩa với khi x->0 thì f(x) -> f(x0)

<br>

<a id="node-55"></a>

<p align="center"><kbd><img src="assets/1d714121a2b4234c4d3a2e5585646c779c463462.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì ta sẽ nhân thêm và chia bớt cho x-x0, để rồi khi x->x0 thì 
> [f(x)-f(x0)]/(x-x0) chính là f'(x0) mà cái này đã tồn tại như điều kiện
> ban đầu đã nói. Còn là, với x-x0 thì khi x->x0 cái này sẽ -> 0.
>
> Vậy limit = 0 và ta đã chứng minh xong.

<br>

<a id="node-56"></a>

<p align="center"><kbd><img src="assets/3a63b05b7116b11ddcee32b17fc87461eb1fab43.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì trong cách làm vừa rồi, nhìn thì có vẻ có vấn đề khi ta nhân và
> chia đi cho x-x0 trong khi đó khi x->x0 thì x-x0 = 0 khiến việc chia cho 0
> có vẻ không hợp lệ.
>
> Tuy nhiên, gs nhấn mạnh một ý hồi nãy đó là, khi tính limit, ta phải hiểu
> là kiểu như ta chưa / không bao giờ đụng tới x0, để từ đó x-x0 KHÔNG
> BẰNG 0. Nên x-x0 dù nhỏ nhưng vẫn khác 0, giúp cho việc nhân và chia
> cho x-x0 HOÀN TOÀN HỢP LỆ.

<br>

