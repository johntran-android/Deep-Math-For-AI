# Lec 5: Implicit Differentiaion

📊 **Progress:** `29` Notes | `31` Screenshots

---
<a id="node-103"></a>

<p align="center"><kbd><img src="assets/408bf79f246911c98de90d5c507362e3734ab12f.png" width="100%"></kbd></p>

> [!NOTE]
> Bài này ta sẽ thảo luận về **IMPLICIT DIFFERENTIATION**
>
> Gs nhắc lại các bài trước ta đã biết derivative của x^a với a = 0,
> +/-1,  +/-2.....
>
> Và bài này ta sẽ xem xét a = m/n với m là số nguyên.
>
> Trong 18.02, gs có nói về implicit differentiation, đó là:
>
> nếu ta có**y = f(x) thì dy = f'(x) dx**.
>
> Thì bài này ta sẽ chính thức được học về **implicit** **differentiation**.

<br>

<a id="node-104"></a>

<p align="center"><kbd><img src="assets/0bba836d2460cbfac3593f8ef33685f36b8adc0a.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì, với y = x^(m/n) gọi là equation (1) thì nó tương đương
> (lũy thừa n hai vế):
>
> y^n = x^m (2)
>
> Để rồi bằng cách APPLY d/dx (mà bài trước ta đã biết, đó là
> một operation, cụ thể là 'take derivative' operation, để khi apply
> vào function sẽ cho ta một function) VÀO HAI VẾ thì ta sẽ có:
>
> (d/dx) y^n = (d/dx) x^m
>
> Gs nói sở dĩ ta apply d/dx vào (2) mà không phải vào (1) là vì nếu
> apply vào (1) thì ta có (d/dx) y (cũng chính là dy/dx) = (d/dx) x^m/n
> mà d x^m/n / dx thì ta không biết cách tính. Trong khi đó (d/dx) y^n, 
> (d/dx) x^m thì ta đều có thể tính bằng công thức đã biết

<br>

<a id="node-105"></a>

<p align="center"><kbd><img src="assets/f60a985583bc78ca3028b39620b80335f0f19896.png" width="100%"></kbd></p>

> [!NOTE]
> Vế trái (d/dx) y^n, thì vì y là function theo x tức y(x) nên cái này ta
> phải dùng chain rule:
>
> d y^n / dx = (d y^n / dy) * (dy / dx)
>
> Và (d y^n / dy) dễ thấy sẽ chính là n*y^n-1
>
> Còn vế phải là (d / dx) x^m hay d x^m / dx chính là (x^m)' = m*x^m-1

<br>

<a id="node-106"></a>

<p align="center"><kbd><img src="assets/dc4d86f87f44eebd10d938eb8d2871eebe49c470.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp theo ta sẽ solve for dy/dx bằng cách chia hai vế cho
> n^y^(n-1) và thay y = x^m/n vào

<br>

<a id="node-107"></a>

<p align="center"><kbd><img src="assets/5cc21ee8fcca621f8088d955d518b7ff2dd50b86.png" width="100%"></kbd></p>

> [!NOTE]
> Triển khai ra ta có (m/n)
> x^[m-1-(n-1)m/n]

<br>

<a id="node-108"></a>

<p align="center"><kbd><img src="assets/eb31c427d22756244f0ba69e85ed968363952e7a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/eb31c427d22756244f0ba69e85ed968363952e7a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f7b18ff40fd7627ee26ee1df554b74fd6e88df51.png" width="100%"></kbd></p>

> [!NOTE]
> Và kết quả là a*x^a-1. Cho thấy công thức derivative của x^a =
> a*x^a-1 đúng với cả a = m/n

<br>

<a id="node-109"></a>

<p align="center"><kbd><img src="assets/80b5e99405e7044dcf9de036fa478cf594e31d07.png" width="100%"></kbd></p>

> [!NOTE]
> Ví dụ thứ 2, ta có equation x^2 + y^2 = 1, và ta muốn tính (d/dx)
> y (again, đương nhiên bây giờ ta biết nó là dy/dx hay y').
>
> Thế thì sở dĩ ở đây ta sẽ nhắc đến khái niệm implicit là bởi y là function
> theo x xuất phát từ equation trên. Và ta có thể tính dy/dx theo hai cách
> mà cách hay hơn chính là dùng IMPLICIT DIFFERENTIATION.
>
> Nhưng trước đó ta sẽ tính Explicit, bằng cách từ equation x^2+y^2=1
> ta giải ra tìm y = +/- sqrt(1-x^2)
>
> Đến đây gs cho rằng ta sẽ chỉ quan tấm phần positive của function thôi.
> thì y trở thành y = sqrt(1-x^2) và ta sẽ thể hiện thành (1-x^2)^(1/2)
>
> Để rồi muốn tính dy/dx ta sẽ áp dụng Chain Rule:
>
> = (d (1-x^2)^1/2 / d(1-x^2)) * d(1-x^2) / dx
>
> Áp dụng (x^a)' = a*x^a-1 với việc đã chứng minh công thức này work
> với cả a = m/n nên ta có (d (1-x^2)^1/2 / d(1-x^2))  = (1/2)*(1-x^2)^(1/2-1)
>
> = (1/2)*(1-x^2)^(-1/2)
>
> Và từ đó dy/dx = (1/2)*(1-x^2)^(-1/2) * -2x

<br>

<a id="node-110"></a>

<p align="center"><kbd><img src="assets/52696fde64296c225becb82ea7d2a7907555f53d.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì với IMPLICIT DIFFERENTIATION, đơn giản là ta giữ nguyên
> function x^2 + y^2 = 1 và chỉ việc apply operator d/dx vào hai vế.
>
> (động cơ xuất phát cho việc này là vì ta quan sát thấy việc tính derivative
> của x^2 + y^2 (theo x) sẽ dễ hơn là solve y = f(x) và tính derivative của
> f(x) là function có dính sqrt ở trỏng)
>
> Vậy ta có (d/dx) d(x^2+y^2) = (d/dx) 1 (chú ý d/dx 1 mang ý nghĩa là
> apply 'take derivative operator d/dx vào function mà function này là
> constant  = 1, và đương nhiên là = 0)
>
> Vế trái d (x^2+y^2) / dx với y = y(x) (ý là y là function theo x), sẽ bằng:
>
> d (x^2+y^2) / dx = d x^2 / dx + d y^2 / dx = 2x + d y^2 / dy * dy / dx
>
> = 2x + 2y * dy/dx = **2x + 2yy'
>
> Vậy ta có 2x + 2yy' = 0**

<br>

<a id="node-111"></a>

<p align="center"><kbd><img src="assets/ef2a1d4cba3d53093456428034b0e6dec262bb44.png" width="100%"></kbd></p>

> [!NOTE]
> Và solve for y' ta được y' = -x / y

<br>

<a id="node-112"></a>

<p align="center"><kbd><img src="assets/fda4784336d43ffff6816a09cca26e91c0c7e854.png" width="100%"></kbd></p>

> [!NOTE]
> Và hai kết quả từ hai cách là như nhau.
>
> Có chú ý là nếu ta xét phần âm tức y = -sqrt(1-x^2) thì dy/dx =
> -x/-sqrt(1-x^2) thì nó vẫn the same với result của implicit method vì
> implicit method cho ra kết quả -x/y hàm chứa cả hai case y dương
> hoặc âm

<br>

<a id="node-113"></a>

<p align="center"><kbd><img src="assets/9aecd79ba01673f9a919021e29ee3e54e19b6f08.png" width="100%"></kbd></p>

> [!NOTE]
> Ví dụ 3, cho equation y^4 + xy^2 - 2 = 0, again, để tính dy/dx ta có
> thể explicitly express y theo x và take derivative. Nhưng trong bài
> toán này nếu làm vậy thì function y rất phức tạp và làm sẽ rất khó

<br>

<a id="node-114"></a>

<p align="center"><kbd><img src="assets/2f9e29e34fe3004cc3752c894cfb5db07ca4575e.png" width="100%"></kbd></p>

> [!NOTE]
> Và sẽ dễ hơn nếu ta làm theo implicit method. Đó là, giữ nguyên
> equation ẩn chứa function y = y(x) ở trong đó (chữ implicit có nghĩa là
> ẩn, ẩn chứa ý nói trong equation ẩn chứa function y(x))
>
> Áp dụng operator d/dx hai vế (cũng là lấy đạo hàm theo x hai vế) ta
> có:
>
> 4y^3*y' + y^2 + x(2yy') = 0
>
> d(y^4) / dx =  d y^4 / dy * dy / dx = 4y^3* dy/dx = 4y^3 * y'
>
> Còn d (xy^2) / dx thì áp dụng cả chain rule và (uv)':
>
> d (xy^2) / dx = dx / dx * y^2 + x * d y^2 / dx = y^2 + x * d y^2 / dy * dy / dx
>
> = y^2 + x * 2y * dy / dx = **y^2 + x * 2y * y'**

<br>

<a id="node-115"></a>

<p align="center"><kbd><img src="assets/a8fd6bf4d23af7419202a7f443021018778256eb.png" width="100%"></kbd></p>

> [!NOTE]
> Từ đó ta solve for y', đương nhiên là ta vẫn cần solve for y
> để có y theo x và gắn vào đây. Nhưng việc tính derivative
> đơn giản hơn

<br>

<a id="node-116"></a>

<p align="center"><kbd><img src="assets/05ef8b21a4227fa3ca161d9d7a6fa196a00805d9.png" width="100%"></kbd></p>

> [!NOTE]
> Ví dụ như để tính derivative y' tại x = 1, ta sẽ cần tính y và nó
> sẽ ra 1. Và từ đó thế vào tính y'(1) theo công thức y' trên để ra 1/6
> chính là độ dốc hàm y(x) tại (1,1)

<br>

<a id="node-117"></a>

<p align="center"><kbd><img src="assets/f6bfd56792fea10c44947f9490cca19e0148e001.png" width="100%"></kbd></p>

> [!NOTE]
> Nhưng với x = 2 thì gs nói ta sẽ gặp trouble trong việc tìm ra y từ (*),
> và do đó cũng trouble trong việc tính ra y' luôn.
>
> Do đó, gs nói trong bài này ta bắt đầu với tuyên bố rằng Implicit
> differentiation sẽ giúp ta dễ dàng hơn trong việc tính derivative nếu
> như ta đã xác định được function.
>
> Nhưng nếu ta cũng không xác định được function, hay chưa có function
> thì đương nhiên không thể dễ dàng tìm ra derivative được. Ví dụ như
> ở đây, ta không tìm được y(x=2) nên cũng khó mà tìm được derivative 
> tại đó y'(x=2).
>
> Tuy vậy rõ ràng là implicit differentiation giúp ta tìm ra formula của
> y' dễ hơn so với explicit method

<br>

<a id="node-118"></a>

<p align="center"><kbd><img src="assets/3a3f7a746132b3803921919478674e6537b3abd2.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp theo gs nói một trong những ứng dụng quan trọng của implicit 
> differentiation là nó giúp ta tìm derivative của inverse function.
>
> Lấy ví dụ y = sqrt(x) với x>0. Tương đương y^2 = x. Vậy thì f(x) = √x
> thì x = g(y) = y^2 là inverse của f(x)

<br>

<a id="node-119"></a>

<p align="center"><kbd><img src="assets/7ce3e9a2060f5f507c187d0741263d91ee65014f.png" width="100%"></kbd></p>

> [!NOTE]
> Khái quát lên thì nếu ta có y = f(x) thì x = g(y) = g(f(x))
>
> và g và f là inverse của nhau: g = f^-1, f = g^-1

<br>

<a id="node-120"></a>

<p align="center"><kbd><img src="assets/65b68f7a853b5f9eb2cc8caaa4c6f84d0e945181.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì giả sử ta muốn thể hiện f và g (tức f^-1) trên cùng một đồ thị.
> Thì đầu tiên ta có đồ thị function f(x) = sqrt(x) là đường màu trắng.
>
> Thế thì đương nhiên đồ thị của hàm y = sqrt(x) là tập hợp các điểm
> x,y sao cho y = sqrt(x). Thì vì y = sqrt(x) cũng tương đương y^2 = x
> tức y = f(x) tương đương g(y) = x. Nên đường cong trên cũng chính
> là đồ thị của g(y) = x.
>
> Tuy nhiên ta muốn thể hiện đồ thị của g(x), tức là tập hợp các điểm (x,y)
> sao cho y = g(x)

<br>

<a id="node-121"></a>

<p align="center"><kbd><img src="assets/87d5c8339076790037a8bdc888b990c5fb7ccfb6.png" width="100%"></kbd></p>

> [!NOTE]
> Thì khi đó ta sẽ thay thế y = x, và x = y. Để rồi đường màu trắng sẽ đối
> xứng qua trục chéo và trở thành đường màu đỏ. Thì đó chính là đồ thị
> của y = g(x) (hay f^-1(x)) và nó chính là đồ thị của parabol y = x^2

<br>

<a id="node-122"></a>

<p align="center"><kbd><img src="assets/86b6d0500195cc4eb8d144dc54fd2956585b0533.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp theo, ta sẽ học về việc implicit differentiation cho
> phép ta tính derivative của bất kì inverse function nếu ta
> biết derivative của function

<br>

<a id="node-123"></a>

<p align="center"><kbd><img src="assets/1171d06c5b8ea039c14c53c90e6758fbd8000a9d.png" width="100%"></kbd></p>

> [!NOTE]
> Lấy ví dụ ta có y = arctan(x) <=> tan(y) = x và đương nhiên ta
> muốn tính dy/dx

<br>

<a id="node-124"></a>

<p align="center"><kbd><img src="assets/0b26adade340ecadacba19e132a819c339daef0d.png" width="100%"></kbd></p>

> [!NOTE]
> Tương tự như đồ thị của f(x) = sqrt(x) và f(x) = x^2 đối xứng nhau
> qua đường chéo y = x,  ta có thể visualize đồ thị của tan(x) và
> arctan(x) sẽ như vầy

<br>

<a id="node-125"></a>

<p align="center"><kbd><img src="assets/c3490763442a1aa4f234f42f182bc617545a5e1c.png" width="100%"></kbd></p>

> [!NOTE]
> Gs nhắc lại cho ta nhớ d tan(y) / dy, thật ra có thể derive dễ dàng
> nhờ Quotient rule vì tan(y)  thực ra là sin(y) / cos(y)
>
> Và d/dy sin(y)/cos(y) áp dụng (u/v)' = (uv' + u'v) / v^2 ta sẽ thấy tử số
> là sin^2(y) + cos^2(y) = 1, mẫu số là cos^2(y)
>
> Kết quả là 1/cos^2(y) và nó gọi là secan^2(y)

<br>

<a id="node-126"></a>

<p align="center"><kbd><img src="assets/dd29626be83c5b121d119903d11e58da8d4c94ba.png" width="100%"></kbd></p>

> [!NOTE]
> Theo cách làm implicit differentiation, tức apply d/dx vào equation ,
> cũng là 2 vế của equation ta có
>
> (d/dx) tan(y) = dx/dx
>
> Áp dụng chain rule cho vế trái:
>
> <=> d tan(y) / dy * dy / dx = 1
>
> áp dụng kết quả tan'(y) = 1/cos^2(y) vừa rồi
>
> <=> (1/cos^2(y)) * y' = 1

<br>

<a id="node-127"></a>

<p align="center"><kbd><img src="assets/9b3fa8fd502c433f37cecf6c29dfaab51af2c6dd.png" width="100%"></kbd></p>

> [!NOTE]
> Và từ đó solve for y' ta có y' = cos^2(y).
>
> Có điều ta cần thể hiện nó theo x, bằng cách gắn y = tan^-1(x)
>
> Hay nói cách khác, ta đang có kết quả: 
>
> d/dx tan^-1(x) = cos^2(tan^-1(x))
>
> Cái này tuy đúng nhưng có thể còn đơn giản hơn

<br>

<a id="node-128"></a>

<p align="center"><kbd><img src="assets/be5cb132bfe1c51fb6f068621519c2597d0284b1.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì tới đây ta sẽ dùng equation:
>
> f^-1(y) = x tức tan(y) = x
>
> Và vì tan(y) đối / kề của hình tam giác vuông. Nên việc
> tan(y) = x  đồng nghĩa với ta có tam giác vuông cạnh x, và
> cạnh 1 với góc có độ lớn theo radian = y như vầy

<br>

<a id="node-129"></a>

<p align="center"><kbd><img src="assets/ac5822a318e1808a3c8332887407e336eaec65cd.png" width="100%"></kbd></p>

> [!NOTE]
> Và do đó để tính cos y ta sẽ lấy kề / huyền = 1 / sqrt(1+x^2) 
>
> Nên cos^2(y) = 1 / (1+x^2)

<br>

<a id="node-130"></a>

<p align="center"><kbd><img src="assets/7edb191982b153ce0be96b1b5435dc12cfcf54c7.png" width="100%"></kbd></p>

> [!NOTE]
> Và từ đó d tan^-1(x) / dx  = 1 / (1 + x^2) là kết quả đơn giản hơn
> nhiều so với cos^2(tan^-1(x))

<br>

<a id="node-131"></a>

<p align="center"><kbd><img src="assets/53fe0b74aa9a41f1b0ac0420ba85d28afba1b570.png" width="100%"></kbd></p>

> [!NOTE]
> Ví dụ nữa là y = sin^-1(x)
>
> nó sẽ tương đương sin(y) = x, apply implicit differentiation = take d/dx
> equation ta có
>
> d sin(y) / dx = dx/dx <=> d sin(y) / dy * dy / dx = 1 <=> cos(y) y' = 1
> <=> y' = 1 / cos(y)
>
> với cos(y) = sqrt(1 - sin^2(y)) = sqrt(1 - x^2)
>
> Vậy y' = 1 / sqrt(1 - x^2)

<br>

