# Assignment 2 - Batch Normalization

📊 **Progress:** `19` Notes | `48` Screenshots

---
<a id="node-858"></a>

<p align="center"><kbd><img src="assets/d0ee7ab32f27749f54abfeee091b02c32fd1bae2.png" width="100%"></kbd></p>

> [!NOTE]
> Rất rõ, như đã biết ở trong lecture, ở phần weight initialization cho ta thấy
> rằng neural net sẽ p**erform tốt khi input được preprocess sao cho có dạng
> chuẩn** (Gaussian distribution unit variance, zero mean). Thế thì việc đó chỉ
> giúp**layer đầu tiên hưởng lợi,** còn sau đó**các layer sau khi take input từ
> activation của các layer trước thì không còn tính chất này.**
>
> Vấn đề thứ hai là trong quá trình training, param được update khiến
> **distribution của các activation** thay đổi liên tục (**covariate shift**), điều này
> gây **khó khăn cho training.**
> **Batch normalization** sẽ tính (ước lượng) **running** mean và variance của
> một batch các output từ layer và dùng nó để normalize (zero center và unit
> variance). Và trong quá trình training nó sẽ cập nhật, **giữ cái running mean và
> standard dev** này, để mà**normalize cho lúc testing.**
>
> Ngoài ra, vì chưa chắc lúc nào unit variance zero mean distribution cũng là tốt
> nhất cho nên BatchNorm có**learnable shift và scale param**  để nếu cần, nn
> có thể thay đổi, học ra, tự quyết định distribution (với mean nào, variance nào
> là tốt nhất

<br>

<a id="node-859"></a>

<p align="center"><kbd><img src="assets/86aed1f87e1596fd8c8ce78745581d7460f01a75.png" width="100%"></kbd></p>

<br>

<a id="node-860"></a>

<p align="center"><kbd><img src="assets/ffb7913c0865066de72ce59af511b564e6584119.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ffb7913c0865066de72ce59af511b564e6584119.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e507942f83b8f3c9038c608af7a99e7423014ebf.png" width="100%"></kbd></p>

> [!NOTE]
> việc dùng keepdims True giúp sau khi mean và var vẫn
> có dạng matrix. Với batch norm, ta mean và variance
> theo từng cột (feature column) nên từ x có shape (N,D)
> sẽ được (1,D)
>
> x_hat  = x - mean = (N,D) - (1,D) python sẽ broadcast
> mean thành N hàng, để phép tính trở thành (N,D) - (N,D)
> tương tự, (x - mean) / sqrt(var) là (N,D) / (1,D) python sẽ
> broadcast sqrt(var) từ (1,D) thành (N,D) để có phép chia
> element-wise (N,D) / (N,D)
>
> Thật ra nếu không keepdims thì kết quả của mean và var
> sẽ là 1d array (D,) python vẫn tự thêm 1 dimension vào
> trước để thành (1,D) sau đó broadcasting như trên. Tuy
> nhiên việc keepdims sẽ giúp tránh những rắc rối ví dụ
> như khi làm qua  LayerNorm, hoàn toàn tương tự
> BatchNorm, chỉ khác ở chỗ ta sẽ dùng statistic theo hàng
> thay vì cột. Lúc này mean và var nếu không keepdims
> True sẽ có shape là (N,). Lúc này khi thực hiện operation
> x - mean = (N,D) - (N,) thì nó sẽ báo lỗi. Vì khi đó python
> thêm một dimension vào trước để chuyển  (N,) sang (1,
> N) và (1,N) thì không thể broadcast thành (N,D) được.
> Nhưng nếu có keepdims, kết quả sẽ ra (N, 1). Lúc này
> broadcasting sẽ có thể biến (N,1) thành (N,D)

<br>

<a id="node-861"></a>

<p align="center"><kbd><img src="assets/d38b2153c809e49c0e10278b67f316478d8deb11.png" width="100%"></kbd></p>

> [!NOTE]
> Passed!

<br>

<a id="node-862"></a>

<p align="center"><kbd><img src="assets/0062b0936fabc6bd8bb05677a1e71530b81c17cf.png" width="100%"></kbd></p>

<br>

<a id="node-863"></a>

<p align="center"><kbd><img src="assets/e02b2753da3a2928a667ed56ca51f789168c6020.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3a1930c0f7f96ef22e0a0019eca7236267400331.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a0452075f2224996b7903a797224c9f04f8fe8c1.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e02b2753da3a2928a667ed56ca51f789168c6020.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3a1930c0f7f96ef22e0a0019eca7236267400331.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a0452075f2224996b7903a797224c9f04f8fe8c1.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/71192c572cb0dd2a60c72548045fa7bbef6f1822.png" width="100%"></kbd></p>

> [!NOTE]
> Theo công thức mà áp vô thôi, dout chính là dl/dyi. Tuy
> công thức là dx_hat(i) nhưng với dx_hat (mini batch thì
> cũng vậy) (thử check các shape trước)

> [!NOTE]
> Lưu ý ở đây, nếu dgamma tính toán ở đây mà có keepdims true thì nó sẽ
> có dạng matrix shape (1,D) Nên lúc khởi tạo BN weight matrix gamma ở
> fc_net _ini_ cũng phải có shape (1,D) tức là dùng np.ones((1,D)) chứ
> không phải chỉ là np.ones(D)
>
> Ngược lại như hiện tại, khởi tạo với np.ones(D) thì không cần keepdims
> True

<br>

<a id="node-864"></a>

<p align="center"><kbd><img src="assets/38f89d632a4d3fe32535667f49d7717db25f41ed.png" width="100%"></kbd></p>

> [!NOTE]
> Passed! các error đều
> cỡ 1e-8 - 1e-13

<br>

<a id="node-865"></a>

<p align="center"><kbd><img src="assets/d1412e87b86a24ba3e8d9af88e3a4d6eca6b1ac0.png" width="100%"></kbd></p>

> [!NOTE]
> phần này quay lại sau: đại ý là yêu cầu làm
> (backnorm backward) theo một cách khác

<br>

<a id="node-866"></a>

<p align="center"><kbd><img src="assets/086324373503fb3eff0867da6351f04e0613cc1b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/086324373503fb3eff0867da6351f04e0613cc1b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0532411ac6552d550ee8dfea43025563b4076a04.png" width="100%"></kbd></p>

> [!NOTE]
> # You should expect losses between 1e-4~1e-10 for W,
> # losses between 1e-08~1e-10 for b,
> # and losses between 1e-08~1e-09 for beta and gammas.

<br>

<a id="node-867"></a>

<p align="center"><kbd><img src="assets/6ee196fb9a9d5bfd31f0f8683c8d3b1a68a5fe97.png" width="100%"></kbd></p>

> [!NOTE]
> train 5 hidden layer (6
> layer) network

<br>

<a id="node-868"></a>

<p align="center"><kbd><img src="assets/108b5c2e4d5cd06893e8bee08297e623cec02784.png" width="100%"></kbd></p>

> [!NOTE]
> kết quả có thể thấy có BN model converge
> tốt hơn khi train acc đạt 74.1% so với 66.
> 8% khi không có BN

<br>

<a id="node-869"></a>

<p align="center"><kbd><img src="assets/df474ebed4790487883524551f9c1c483df41311.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/5bc69ad2e9951f3cd5f9333fc78ce36610a61bc4.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/df474ebed4790487883524551f9c1c483df41311.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/5bc69ad2e9951f3cd5f9333fc78ce36610a61bc4.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/9d2e3feebe41a2c03023079a33f198c3350d026d.png" width="100%"></kbd></p>

> [!NOTE]
> đồ thị cho thấy BN converge tốt hơn, cụ thể là nhanh hơn và về loss thấp hơn

<br>

<a id="node-870"></a>

<p align="center"><kbd><img src="assets/f363644f816a2095004b867d93d362b00f0c3645.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f363644f816a2095004b867d93d362b00f0c3645.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d46e2ed3d71d6a21dd458f9d05a255738537e491.png" width="100%"></kbd></p>

<br>

<a id="node-871"></a>

<p align="center"><kbd><img src="assets/dcb1d78581a7daf3ec8bd73348d7b49a7c9c50e8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/af4cb6b2379059c7fe61edfd69c66beaa712ac41.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/dcb1d78581a7daf3ec8bd73348d7b49a7c9c50e8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/af4cb6b2379059c7fe61edfd69c66beaa712ac41.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e43360e1fc84ac15508296b729cde789818aa1db.png" width="100%"></kbd></p>

> [!NOTE]
> biểu đồ ở trên cùng: với model không BN, ws từ rất nhỏ đến nhỏ
> (1e-4-1e-3) val acc = 0, và sau tăng dần lên để đạt mức tốt ở tầm 10^-1,
> nhưng quá mức đó val acc liền giảm.
>
> Còn với BN, dù ws nhỏ val acc vẫn ở mức cao hơn khi ko có BN, và nó lên
> cao  dần một chút ở mức 10^-2 nhưng khi ws tăng nó vẫn giữ mức tốt một
> thời gian chỉ khi ws quá lớn thì val acc mới giảm.
>
> Điều này cho thấy rõ, với BN, **model giảm đi sự phụ thuộc vào việc chọn
> weight scale phù hợp, model bớt nhạy cảm với weight weight scale**. Tuy
> nhiên việc chọn weight scale tốt vẫn có ích.
>
> Biểu đồ thứ hai cũng cho thấy tương tự với training acc. Nhìn chung khi
> weight scale lớn quá thì BN cũng không giúp được.
>
> Biểu đồ cuối cùng có thể thấy mức training loss final khi có BN cao hơn khi
> không có
>
> ===== Why?
>
> Bởi vì BN đã **khiến output vào activation function trở nên có (phân phối)
> dạng  tốt hơn**: **không bị nhỏ dần đi để rồi gây vanishing gradient** hoặc
> **lớn dần để gây exploding gradient** (hoặc là cả vanishing gradient do local
> grad của nonlinearity function bị saturate).
>
> Bên cạnh đó, BN có **learnable scale param - gamma và shift param beta**,
> nhờ vậy**model có thể học ra, quyết định dạng distribution nào là tốt nhất**,
> nhờ đó góp phần cho model **thêm công cụ để tăng hiệu quả huấn luyện**

<br>

<a id="node-872"></a>

<p align="center"><kbd><img src="assets/fa960657e6ac87f05faaf4bf57900ab9d366b44f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1baab41a2d871edf14cfcc74fad1f6d2da1a8511.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/fa960657e6ac87f05faaf4bf57900ab9d366b44f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1baab41a2d871edf14cfcc74fad1f6d2da1a8511.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b5d19afb62d300198ab24068d168370d5fb256d8.png" width="100%"></kbd></p>

> [!NOTE]
> nhận xét đầu tiên là với BN, training với batch size lớn thì tăng hiệu quả.
> Điều này có thể hiểu là do nguyên lý của BN là dùng **batch statistic tính
> toán bởi một data mini-batch để normalizing data.**
>
> Vậy **batch size càng lớn thì batch's statistic sẽ càng gần với population
> stats** hơn nên hiệu quả của BN sẽ tốt hơn.

<br>

<a id="node-873"></a>

<p align="center"><kbd><img src="assets/a09ccc2aa9d1d881c573bac80da7f0d0d96cf20c.png" width="100%"></kbd></p>

<br>

<a id="node-874"></a>

<p align="center"><kbd><img src="assets/3f94ac78f836d5bf175f297bda92ddb938a027b5.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3f94ac78f836d5bf175f297bda92ddb938a027b5.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f67b4b85e775c39359dba7bc71b87a5b893bc8ff.png" width="100%"></kbd></p>

> [!NOTE]
> Theo mô tả, Layer Normalization chỉ khác Batch Normalization ở chỗ nó sẽ
> **không cần tính statistic của một batch** (vì đây cũng là lí do mà người ta tạo
> ra Layer Normalization vì **muốn không cần phụ thuộc vào / phải dùng statistic
> của mini-batch mới làm được**)
>
> Thay vào đó, Layer Norm dùng mean và variance của một single feature
> vector, để normalizing feature vector. Vậy ta có thể hiểu ví dụ input vào
> LayerNorm là một batch N cái feature vector, mỗi vector là output từ layer
> trước, ứng với một sample. Thì ta sẽ **cần tính mean và variance của vector
> này**. Vậy nếu batch of Input có shape N,D thì **thay vì mean với axis = 0 để có
> mean của các column = các feature trong batch, ở đây ta sẽ mean (và var)
> với axis = 1 để có mean của mỗi hàng.**
>
> Dùng keepdims True để shape của mean và var là (N,1) giúp khi tính x -mean
> có thể broadcast được thành (N,D). Nếu không kết quả của mean là (N,) sẽ
> không broadcast được (N,) -python sẽ chèn thêm một dimension ở trước -->
> (1,N)   -> không thể thành (N, D) được

<br>

<a id="node-875"></a>

<p align="center"><kbd><img src="assets/7b4ac6979aa4ca288759bd8f76f9ce1c8f65225e.png" width="100%"></kbd></p>

> [!NOTE]
> Passed!

<br>

<a id="node-876"></a>

<p align="center"><kbd><img src="assets/0b71d141e9e3db3215fd7cc02cbc86eeec27a348.png" width="100%"></kbd></p>

> [!NOTE]
> Backward cũng chỉ cần thay đổi axis từ 0 sang 1

<br>

<a id="node-877"></a>

<p align="center"><kbd><img src="assets/fe0a654bd7f649d23cb549b616e2ffcb9510dbb3.png" width="100%"></kbd></p>

> [!NOTE]
> should expect to see relative errors between
> 1e-12 and 1e-8: Passed

<br>

<a id="node-878"></a>

<p align="center"><kbd><img src="assets/cd2e3dd2a84e23753833343937aaafada63493a2.png" width="100%"></kbd></p>

> [!NOTE]
> Quay laị chỗ này sau, qua làm Dropout luôn

<br>

<a id="node-879"></a>

<p align="center"><kbd><img src="assets/053b9753054e9b7f803b81d498b4184786b4b93e.png" width="100%"></kbd></p>

> [!NOTE]
> quay lại sau

<br>

