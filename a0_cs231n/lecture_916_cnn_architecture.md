# Lecture 9/16 - CNN Architecture

📊 **Progress:** `62` Notes | `77` Screenshots

---
<a id="node-1060"></a>

<p align="center"><kbd><img src="assets/d349a2db7070d189ca66535cc2be574112f79f0e.png" width="100%"></kbd></p>

<br>

<a id="node-1061"></a>

<p align="center"><kbd><img src="assets/59a169efa42e3a22d3dc53185a263c521f9dddd1.png" width="100%"></kbd></p>

<br>

<a id="node-1062"></a>

<p align="center"><kbd><img src="assets/d5314eb7ff93526c6411b127ff5e620456804bd3.png" width="100%"></kbd></p>

<br>

<a id="node-1063"></a>

<p align="center"><kbd><img src="assets/04729ce7281837c261985eaa7a6b13ab31414dbb.png" width="100%"></kbd></p>

<br>

<a id="node-1064"></a>

<p align="center"><kbd><img src="assets/70bb3713edc2fc9a2a9c81799dcfa3628b66fe61.png" width="100%"></kbd></p>

> [!NOTE]
> AlexNet cơ bản là cũng khá giống LeNet
> với các Conv layer theo sau bởi Pooling,
> cuối cùng là các FC layer

<br>

<a id="node-1065"></a>

<p align="center"><kbd><img src="assets/e31752b29a68b25254582cbf6fcde75c3432aee2.png" width="100%"></kbd></p>

> [!NOTE]
> AlexNet train với input là ImageNet image nên có input size là 227x227x3.
>
> Hỏi sau Convolutional layer đầu tiên với 96 filters 11x11 thì output size là  bao
> nhiêu.
>
> -> Theo công thức output width & height sẽ là: {round down [(input w +
> 2*padding - filter size) /stride} + 1]
>
> Round down [227 + 2p (padding) - filter size] / s (stride)  = round down (227 -
> 2*0 - 11)/4 + 1
>
> = 55
>
> Với 96 filter thì đương nhiên output depth 96, vậy output sẽ là 55x55x96

<br>

<a id="node-1066"></a>

<p align="center"><kbd><img src="assets/e6e8f7207aa680aed23397e03fe33515c4b0fc23.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e6e8f7207aa680aed23397e03fe33515c4b0fc23.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f2b604c08804734476afea78e4f2b4b7e3eccc14.png" width="100%"></kbd></p>

<br>

<a id="node-1067"></a>

<p align="center"><kbd><img src="assets/9de408cd7e428dc3b1b310c30cd4a7e56ca3fdd4.png" width="100%"></kbd></p>

> [!NOTE]
> số parameters của conv1: đương nhiên là tính từ kích thước và số lượng filter:
>
> Mỗi filter: 11x11x3 weights, cộng 1 bias là 11x11x3+1 = 363 + 1 = 364 parameters
>
> Vậy có 96 filters, 364x96 = 34944 params. Nếu không tính bias thì đâu đó cỡ 34848

<br>

<a id="node-1068"></a>

<p align="center"><kbd><img src="assets/6837907334b201fc908ba623e78504106a28ad7b.png" width="100%"></kbd></p>

> [!NOTE]
> Input spatial size là 55x55, pooling với 3x3 filter stride 2 output size sẽ là:
>
> Round down [(Input size - filter size) / stride] + 1 = (55-3)/2+1 = 26+1 = 27
>
> Output sẽ là 27x27x96 (output depth vẫn là 96)
>
> Số params: 0. Pooling chỉ là phép tính max / average nên ko có params

<br>

<a id="node-1069"></a>

<p align="center"><kbd><img src="assets/3cae370229c950e5b10026d31d327e4e70c697ad.png" width="100%"></kbd></p>

> [!NOTE]
> một cái "cặp" conv - pooling layer, cuối cùng là
> vài FC layer trước khi output FC 1000 với
> softmax để ra probability ứng với 1000 class
> của ImageNet dataset

<br>

<a id="node-1070"></a>

<p align="center"><kbd><img src="assets/1047f2e2ea4b6a50fea062934f127f50434c2f7c.png" width="100%"></kbd></p>

> [!NOTE]
> một vài thông tin chi tiết về AlexNet đó là, 
>
> đây là mô hình đầu tiên dùng ReLU. 
>
> - Họ dùng Normalization layer dù hiện nay không còn phổ biến
>
> - Thực hiện data augmentation rất nhiều
>
> - Dropout layer với rate 0.5
>
> - Training với batch size 128.
>
> - Optimizer là SGD Momentum beta 0.9
>
> - Learning rate 1e-2, và dùng learning rate schedule theo chiến
> lược cứ giảm 10 lần mỗi khi accuracy plateaus
>
> - Dùng L2 weight decay (L2 regularization)
>
> - Cuối cùng là họ train 7 cái như vậy để dùng chúng theo
> Ensemble learning

<br>

<a id="node-1071"></a>

<p align="center"><kbd><img src="assets/f22cb4e3cdb160ced4273ffe4d8118ea7704c81e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f22cb4e3cdb160ced4273ffe4d8118ea7704c81e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4f7aed9830072a642606de890bf5d78b1b581fd0.png" width="100%"></kbd></p>

> [!NOTE]
> có nghĩa là vì dung lượng của GPU thời đó không đủ nên họ
> thực hiện chia ra làm hai.
>
> Ví dụ như Conv1, 48 filter sẽ convol input trên GPU thứ 1, 
> 48 filter nữa sẽ convol input trên GPU thứ 2.

<br>

<a id="node-1072"></a>

<p align="center"><kbd><img src="assets/6466a34d8245d861ab35a5a5f34a5efb641a2595.png" width="100%"></kbd></p>

> [!NOTE]
> tương tự, ở các conv1,2, 4,5 đều chỉ connect với feature map trong cùng gpu
>
> ví dụ conv2 256 filter 5x5 thì thật ra sẽ có 128 filter 5x5 convol input (output từ 
> pooling1-norm1) ở gpu 1, tạo ra cái tensor 27x27x128 thứ nhất. và 128 filter kia 
> sẽ convol input ở gpu thứ 2.

<br>

<a id="node-1073"></a>

<p align="center"><kbd><img src="assets/1e66a62b6e3a1f75a388e270e748f2727b34a978.png" width="100%"></kbd></p>

> [!NOTE]
> nhưng conv3 384x3x3 thì sẽ có sự connection từ input feature map ở cả hai
> gpu.
>
> Nói ngắn gọn thì sau conv2-norm2, có sự đồng nhất giữa Hai GPU để mỗi cái
> đều có output từ conv2-norm2 ở cả hai gpu. gọi là f1, f2 mỗi cái đều là
> 27x27x128. Ở cả hai gpu, cả hai mới cộng lại để ra f: 27x27x128
>
> Và rồi mỗi gpu, conv3 sẽ convolution với 192 filter 3x3 với  cái f 27x27x128 này.

<br>

<a id="node-1074"></a>

<p align="center"><kbd><img src="assets/bbdf02193a2e47de1588c7e96c30d385faadb9dc.png" width="100%"></kbd></p>

> [!NOTE]
> AlexNet đã thắng giải ImageNet của năm 2012, với cách biệt rất đáng kể và
> vẫn phổ biến trong một thời gian dài sau đó (là kiến trúc sử dụng với
> transfer learning cho các bài toán khác).
>
> Chú ý trong hình là so sánh các model trên ImageNet theo error rate Những
> năm sau, các VGG, GoogleNet, ResNet đã vượt qua AlexNet
>
> Và đây cũng là cách tiếp cận Deep Learning đầu tiên trên ImageNet, trước
> đó như thấy trong hình, các cách tiếp cận thắng ImageNet năm 2010, 11
> vẫn là shallow

<br>

<a id="node-1075"></a>

<p align="center"><kbd><img src="assets/f4922f3e8b1d72dde7a2b7570401794321b20fb9.png" width="100%"></kbd></p>

> [!NOTE]
> thắng ImageNet 2013 là cơ bản vẫn là AlexNet nhưng với các
> hyperparams được tuned như dùng filter size khác, stride khác...giúp
> giảm error rate xuống hơn nữa tứ 16% của AlexNet xuống còn 11%

<br>

<a id="node-1076"></a>

<p align="center"><kbd><img src="assets/52de6d178f993a8f31fc049441cf4d36c51d59ee.png" width="100%"></kbd></p>

> [!NOTE]
> thắng ImageNet trong hai năm tiếp theo
> chủ yếu là với cách tiếp cận "deeper" khi
> số layer tăng lên nhiều hơn

<br>

<a id="node-1077"></a>

<p align="center"><kbd><img src="assets/a335b7b3dd6db0b8113eb614259d0d1e06da1566.png" width="100%"></kbd></p>

> [!NOTE]
> So với AlexNet, thì VGG sâu hơn như đã nói, với 16 layer
> (thì gọi là VGG16) tới 19 layer (VGG19)
> *nói 16 layer thì chỉ tính các conv và pool layer thôi.không tính input, fc layer
>
> cái thứ hai đó là nó dùng filter size nhỏ là 3x3, stride 1, pad1, và pooling thì
> chỉ 2x2, stride 2.

<br>

<a id="node-1078"></a>

<p align="center"><kbd><img src="assets/ecf7768c37efe53b5d0e436579de3943a048a372.png" width="100%"></kbd></p>

> [!NOTE]
> Input 27x27, filter 7x7 output sẽ là (27-7)/1 + 1 = 21
>
> 27x27 -> f 7x7 -> **21x21**
>
> nếu filter là 3x3:
>
> 27x27 - f 3x3 -> 25x25 - f 3x3 -> 23x23 -f 3x3-> **21x21**Nhưng f 7x7 sẽ có 49 params
>
> f3x3 3 cái thì chỉ có 9x3 = 27 params

<br>

<a id="node-1079"></a>

<p align="center"><kbd><img src="assets/8163a3e87fbd3271afdb43ef2a812205b6e11c0e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/8163a3e87fbd3271afdb43ef2a812205b6e11c0e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d2c09b2dcf2542305db9bdebb6eb23e6d37bc72a.png" width="100%"></kbd></p>

> [!NOTE]
> tức là, qua 3 filter 3x3 thì tạo ra kết quả trong đó mỗi
> vị trí của output được nhận thông tin từ layer đầu
> tương đương với xài 1 filter 7x7

> [!NOTE]
> Nhưng số lượng param sẽ nhỏ hơn đồng thời, deeper sẽ cho phép
> nhiều non-linearity hơn -> tăng độ complexity của model

<br>

<a id="node-1080"></a>

<p align="center"><kbd><img src="assets/b793b8b44a36c6064e3169c1bb088620f578359a.png" width="100%"></kbd></p>

> [!NOTE]
> Chi tiết số parameters của các layer (ta cho rằng nên thử tính
> lại như hồi nãy đã làm, good practice). 
>
> Tổng số các number chứa giá trị trong quá trình tính toán là 24M,
> với mỗi number cần 4 bytes thì tổng cộng sẽ là 96MB khi forward
> một image. Và giảng viên nói thêm là khi backward ta sẽ cần
> gấp đôi con số này vì cần phải save các intermediate value.
>
> Nên mới nói nếu ta có 5GB memory thì với ~100MB / image thì chỉ 
> có thể store khoảng 50 images
>
> Tổng số params là 138M (AlexNet là 60M)

<br>

<a id="node-1081"></a>

<p align="center"><kbd><img src="assets/3fa79557f02f98af33fd5b5b15ebe00ad7742fdd.png" width="100%"></kbd></p>

> [!NOTE]
> câu hỏi đại khái là khi nói đến "deep" thì ý là số filter (ý là deeper có
> nghĩa là tăng depth = tăng số filter trong một convolution layer) hay là
> nói về số layer của model architecture
>
> -> Đúng là depth có thể khiến confuse, nhưng khi nói "deeper model"
> thì luôn đang nói đến số convolutional layer. Deeper tức là nhiều
> layer hơn

> [!NOTE]
> Đại khái câu hỏi là gì chưa rõ nhưng t.a nhắc lại quá trình trong một
> convolution layer đó là, mỗi filter sẽ kiểu như nhìn vào trong input
> mỗi lần là một vùng ví dụ 3x3, để rồi convolution qua hết cái input thì
> cho ra một "feature map".
>
> Và nhiều feature map tạo ra bởi nhiều filter sẽ stack together để thành
> Output

> [!NOTE]
> Đại khái câu hỏi là gì có phải là / có một quy tắc nào trong việc khi go 
> deeper thì số channel / số filter càng tăng hay không.
>
> Thật ra là không, đơn giản chỉ là vì người ta cho rằng, khi gỗ deeper,
> Spatial area ngày càng giảm đi (bề dài, bề rộng của tensor ngày càng
> nhỏ đi) thì cho phép tăng số filter lên mà không làm tăng quá mức số
> lượng tính toán. Chỉ vậy thôi.

> [!NOTE]
> Câu hỏi nữa là có thể dùng SVM loss thay vì Softmax không?
>
> -> Được, chỉ là người ta thử nghiệm thì thấy dùng softmax ok hơn nên
> dùng phổ biến cái này hơn thôi

<br>

<a id="node-1082"></a>

<p align="center"><kbd><img src="assets/da2c64784654f1372630d5ed87b090711bdc6fa9.png" width="100%"></kbd></p>

> [!NOTE]
> Ta sẽ chú ý rằng phần tốn memory nhiều nhất là những
> conv đầu tiên khi nó phải take input original image có
> spatial area lớn cũng như là các fully connected layer
> cuối. Để tí nữa ta sẽ thấy các model sau này sẽ cố gắng
> khắc phục điều này

<br>

<a id="node-1083"></a>

<p align="center"><kbd><img src="assets/9f0ed2c438ba0e900bda81f85f9cae47f670f7df.png" width="100%"></kbd></p>

> [!NOTE]
> một điểm cần để ý nữa đó là người ta
> cũng dùng cách gọi tên các layer theo
> group ví dụ như conv1-1

<br>

<a id="node-1084"></a>

<p align="center"><kbd><img src="assets/a0caa5d760c693fab9ea0f214d8538c4cac122f0.png" width="100%"></kbd></p>

> [!NOTE]
> một số ghi chú:
>
> VGGNet về nhứt ở hạng mục localization, về nhì ở classification trên 
> ImageNet 2014.
>
> Quá trình training tương tự AlexNet
>
> Không sử dụng Local Response Normalization, mà ở trên cũng có nói
> là cái này của AlexNet hiện giờ không còn được phổ biến sử dụng
>
> Dùng VGG16 hay 19 đều được
>
> Nên dùng ensemble technique để có kết quả tốt hơn - tức là ta sẽ train
> vài model và dùng như một team để lấy kết quả đồng thuận
>
> Cuối cùng output của FC7 được cho là nắm bắt được các general 
> pattern tốt để có thể sử dụng cho transfer learning đối với các task khác.
> Có nghĩa là ta có thể dùng output của FC7 của một pretrained VGG để
> train một model giải quyết một bài toán khác

> [!NOTE]
> Đại khái là localization assume là chỉ có một object, và
> model cần predict một bounding bõ cho nó. còn bài toán
> detection tuy rất gần vẫn có điểm khác. Ta sẽ được học
> trong phần sau

<br>

<a id="node-1085"></a>

<p align="center"><kbd><img src="assets/22d0ff2bd9b66cb6a2ad7da70d6a30325828b6d5.png" width="100%"></kbd></p>

> [!NOTE]
> GoogLeNet, giới thiệu "Inception" module.
>
> Như đã hiểu về nhược điểm của FC là sẽ tốn rất nhiều params,
> thì GoogleNet không còn dùng FC nữa.
>
> Để rồi tuy deeper, nhưng chỉ có 5M params = 1/12. AlexNet
>
> Nhưng độ hiệu quả thì hơn rất nhiều

<br>

<a id="node-1086"></a>

<p align="center"><kbd><img src="assets/6e1d4022dab1d252d803420a89534ba44a33713c.png" width="100%"></kbd></p>

> [!NOTE]
> Inception model: GoogleNet giới thiệu việc tạo
> ra các "local network" để rồi stack các module
> này lại để thành network lớn

<br>

<a id="node-1087"></a>

<p align="center"><kbd><img src="assets/520ea2265057f747a5b1c266b3004a3d7be03810.png" width="100%"></kbd></p>

> [!NOTE]
> đại khái là, input sẽ được convolution với nhiều filter có size khác nhau, như
> 1x1, 3x3, 5x5 để rồi concatenate lại depth-wise.

<br>

<a id="node-1088"></a>

<p align="center"><kbd><img src="assets/e61f12d75d9a26f408bf50bade3eeaa83ca5a507.png" width="100%"></kbd></p>

> [!NOTE]
> 28x28x256 -1x1 128 (maintain spatial dimension, tức same padding) -> 28x28x128

<br>

<a id="node-1089"></a>

<p align="center"><kbd><img src="assets/e75f91791d7a844771c643643e0e0f457ba6ef9a.png" width="100%"></kbd></p>

<br>

<a id="node-1090"></a>

<p align="center"><kbd><img src="assets/c211d53b0a31559451b0a2f20837d1e0b6c6e68e.png" width="100%"></kbd></p>

<br>

<a id="node-1091"></a>

<p align="center"><kbd><img src="assets/e48178f994175d77e5346e58332ff3e5c2a094ee.png" width="100%"></kbd></p>

> [!NOTE]
> Số phép tính trong 28x28x256 --1x1x128--> 28x28x128: 
>
> Filter size là 1x1, nhưng input's depth = 256, nên filter size là 1x1x256
> Vậy để convol input, tại mỗi vị trí (trong spacial map) sẽ cần 1x1x256 phép tính.
> Và có w,h = 28x28 vị trí thì sẽ cần 1x1x256x28x28 phép tính cho 1 filter, mà có 128
> filter nên tổng cộng sẽ là **1x1x256x28x28x128**
>
> Tương tự, số phép tính trong 28x28x256 --3x3x192-->28x28x192
> Filter size là 3x3, input depth = 256 nên filter shape là 3x3x256. Vậy mỗi vị trí
> khi convol sẽ cần 3x3x256 phép tính (product, ở đây nãy h không kể đến bias)
> Vậy tổng cộng sẽ có 3x3x256x28x28 phép tính cho 1 filter, mà có 192 filter nên
> sẽ là **3x3x256x28x28x192**Tương tự, cho mấy cái kia, để rồi cộng lại là **854M phép tính (operations)**

<br>

<a id="node-1092"></a>

<p align="center"><kbd><img src="assets/5f462ddfa1c09ae0150e24a9aa18b38836cd0d2d.png" width="100%"></kbd></p>

> [!NOTE]
> một ý nữa đó là pooling chỉ giữ nguyên kích thước depth
> nên qua từng layer, depth chỉ tăng chứ không giảm. nên
> vấn đề ngày càng lớn khi qua các layer, số phép tính cần
> để thực hiện ngày càng lớn

<br>

<a id="node-1093"></a>

<p align="center"><kbd><img src="assets/4671452d84310cc442781a17f33785ac53cf3c94.png" width="100%"></kbd></p>

> [!NOTE]
> cách khắc phục chính là dùng
> 1x1 conv để giữ nguyên spatial
> size nhưng giảm depth

<br>

<a id="node-1094"></a>

<p align="center"><kbd><img src="assets/4243864e18a5c4edad62df99b938927d3beab0fc.png" width="100%"></kbd></p>

> [!NOTE]
> để rồi 1x1 convolution sẽ
> tham gia giúp giảm depth

<br>

<a id="node-1095"></a>

<p align="center"><kbd><img src="assets/b71a2403a78604cfdd8f78d5388abe9fbc685bd8.png" width="100%"></kbd></p>

> [!NOTE]
> Với cách làm này, inception module chỉ tốn
> 358M operations so với 854M

<br>

<a id="node-1096"></a>

<p align="center"><kbd><img src="assets/6cbed009593906f78523b989f8689eb838597c9c.png" width="100%"></kbd></p>

> [!NOTE]
> GoogleNet architecture sẽ bắt đầu với Stem
> Network - chính là các lớp Conv-Pooling
> như đã gặp bên AlexNet

<br>

<a id="node-1097"></a>

<p align="center"><kbd><img src="assets/75b1920b20ca1da38e00fb7dbb9e44126ad6cc37.png" width="100%"></kbd></p>

> [!NOTE]
> Sau đó là đến phần stack lại
> nhiều Inception module

<br>

<a id="node-1098"></a>

<p align="center"><kbd><img src="assets/64460477da0c982fb978eebe2c49725f63928ac2.png" width="100%"></kbd></p>

> [!NOTE]
> Và output với classifier output -
> softmax 1000 unit có điều không
> còn dùng FC layer nữa

<br>

<a id="node-1099"></a>

<p align="center"><kbd><img src="assets/68176164c399f3452a3fc577f7f995639aff4797.png" width="100%"></kbd></p>

> [!NOTE]
> một điểm đặc biệt đó là GoogleNet cũng output ở hai earlier layer.
> Việc này hiểu nôm na là đóng vai trò giúp gradient được bổ sung để
> train param của các layer đầu tiên vốn dĩ do GoogleNet rất sâu nên
> gradient từ 'final' output trở nên yếu khi tới đây. Và cũng cho thấy tại
> những output này, GoogleNet vẫn có thể dùng feature để thực hiện
> dự đoán

<br>

<a id="node-1100"></a>

<p align="center"><kbd><img src="assets/ba289879c2092e153e49116f5e870077d6b5830f.png" width="100%"></kbd></p>

> [!NOTE]
> tổng cộng googlenet có 22 layers

<br>

<a id="node-1101"></a>

<p align="center"><kbd><img src="assets/30aea3ed9254e45d96463e373c92d5e990237325.png" width="100%"></kbd></p>

<br>

<a id="node-1102"></a>

<p align="center"><kbd><img src="assets/6da00db6f1641e7b40db5baebd8876f7103bdd51.png" width="100%"></kbd></p>

> [!NOTE]
> kế đến là RestNet, thì đây là mô hình
> tạo bước nhảy vọt về mức độ 'depth'
> khi có tới 152 layers

<br>

<a id="node-1103"></a>

<p align="center"><kbd><img src="assets/73905a359ec666a3703e9cfe644bd50eb8732d6e.png" width="100%"></kbd></p>

> [!NOTE]
> và nó thắng các model khác ở mọi lĩnh vực
> cả classification và detection.

<br>

<a id="node-1104"></a>

<p align="center"><kbd><img src="assets/407fca15d8e81227d9835611b867fe3f3a30986e.png" width="100%"></kbd></p>

> [!NOTE]
> đại ý là, khi ta tăng số layer lên, trên lí thuyết thì model phải phức tạp hơn,
> từ đó sẽ dần bị overfit. Tuy nhiên thực tế cho thấy cả training error và
> validation error đều cao hơn model với ít layer hơn
>
> Điều này cho thấy model không bị overfit, mà là việc thêm layer gây ra vấn
> đề khiến model học không tốt, từ đó giảm performance.

<br>

<a id="node-1105"></a>

<p align="center"><kbd><img src="assets/390e114e892eb96231fa455ec98c84f44b51d9c2.png" width="100%"></kbd></p>

<br>

<a id="node-1106"></a>

<p align="center"><kbd><img src="assets/76c7dba9b73955d8694b7b5506c84d0ad8ef7b99.png" width="100%"></kbd></p>

> [!NOTE]
> "Use layers to fit residual F(x) thay vì H(x)": Có thể hiểu nôm na ý này đó là**thay vì fit / học một function H(x)**, thì ta có thể **học function F(x) gọi là
> residual function**
>
> Để rồi từ F(x) ta có hàm H(x) = F(x) + x. Vì cuối cùng mục đích cũng chỉ là
> học ra một (mapping) function (thể hiện bởi các parameters) để map giữa
> input và target thôi. Vậy với cách bố trí như vầy, thì ta sẽ cho model tìm
> cách học ra hàm F(x) mang ý nghĩa là **ta cần thêm (add) bớt (subtract) gì
> từ input x**Câu hỏi với t.a là tại sao việc học được một residual function F(x) lại 'dễ' hơn
> (dẫn đến việc dùng residual connection lại hiệu quả) là direct function H(x).
> t.a cho rằng, đây là lý thuyết của paper author, cho rằng đại khái là nếu 
> đặt trường hợp identity mapping lại là tốt (tức là trong mối quan hệ giữa input
> x và output y cần nắm bắt thật sự lại là một identity mapping, hay nói cách khác
> H(x) cần học được thật ra chỉ là H(x) = x, thì residual connection sẽ chỉ việc 
> học ra hàm F(x) = 0.
>
> Có vẻ như ta nên hiểu đây chỉ là lý thuyết đưa ra của tác giả, còn thực tế 
> chỉ đơn giản là nó tỏ ra hiệu quả.

<br>

<a id="node-1107"></a>

<p align="center"><kbd><img src="assets/ec66fa8f880b837157eacef25335cb43c482710a.png" width="100%"></kbd></p>

<br>

<a id="node-1108"></a>

<p align="center"><kbd><img src="assets/2b17e31d2b0843183f9422bba6133c5215b89d5d.png" width="100%"></kbd></p>

<br>

<a id="node-1109"></a>

<p align="center"><kbd><img src="assets/b662f113ce06523a717cdc225cc9de94d465e175.png" width="100%"></kbd></p>

> [!NOTE]
> Đại ý là với resnet 50 layer trở lên người ta có thể dùng
> bottleneck layer để cải thiện efficiency.

<br>

<a id="node-1110"></a>

<p align="center"><kbd><img src="assets/d73c3906ef0f91ba49618c2a292a1d7889353c27.png" width="100%"></kbd></p>

> [!NOTE]
> một số thông số kĩ thuật khi huấn
> luyện resnet trong thực tế

<br>

<a id="node-1111"></a>

<p align="center"><kbd><img src="assets/dac9780b447ac2978c4bd051046a8ed28a2a64ad.png" width="100%"></kbd></p>

> [!NOTE]
> một số thông tin về performance của resnet cho thấy
> nó cho phép huấn luyện một model rất sâu mà không
> ảnh hưởng đến performance. Đánh bại mọi model khác     
> ở các 'bài toán' khác nhau

<br>

<a id="node-1112"></a>

<p align="center"><kbd><img src="assets/205b7128bfc3ad0fb736ca771dae1d4876185341.png" width="100%"></kbd></p>

> [!NOTE]
> đại ý nói rằng resnet đã trở thành một lựa chọn ưu tiên khi
> muốn finetune cho một bài toán computer vision. Mặc dù
> googlenet hay vgg vẫn được dùng

<br>

<a id="node-1113"></a>

<p align="center"><kbd><img src="assets/6e710acec6357fa13dfae28efb3d63be25bbd3c6.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6e710acec6357fa13dfae28efb3d63be25bbd3c6.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c46a6648add1c462f76545a88c0daeb80ee2260a.png" width="100%"></kbd></p>

> [!NOTE]
> biểu đồ cho thấy inception-v4 (có sự kết hợp giữa restnet và inception)
> đạt accuracy cao nhất.

> [!NOTE]
> biểu đồ đường kính cho thấy vgg tốn memory
> nhất cũng như số operation cũng nhiều nhất
> có nghĩa là efficiency thấp

<br>

<a id="node-1114"></a>

<p align="center"><kbd><img src="assets/463ccbef4bad8d219d4d3110219ed87f8558adc8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/463ccbef4bad8d219d4d3110219ed87f8558adc8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1321c3e62dbf89e016f65165c5a479a2ef66ffbf.png" width="100%"></kbd></p>

> [!NOTE]
> googlenet có mức hao memory cũng như operation thấp
> cho thấy nó rất hiệu quả nhưng accuracy kém hơn resnet, vgg

> [!NOTE]
> Alexnet thì tuy mức operation thấp nhưng memory cũng
> tương đối. và accuracy cũng ko cao

<br>

<a id="node-1115"></a>

<p align="center"><kbd><img src="assets/0df599718b3f826f62732a065ec3245276fe9e8b.png" width="100%"></kbd></p>

> [!NOTE]
> Resnet có efficiency trung bình tùy thuộc vào model, nhưng
> accuracy ở mức cao

<br>

<a id="node-1116"></a>

<p align="center"><kbd><img src="assets/5985ebb06036578d0cb0c2f7c45eecf0bddeff02.png" width="100%"></kbd></p>

> [!NOTE]
> thêm những so sánh khác về hiệu
> suất của các architecture

<br>

<a id="node-1117"></a>

<p align="center"><kbd><img src="assets/e0fb73f9d9c08245617bf3c6939d97d92c22ccab.png" width="100%"></kbd></p>

> [!NOTE]
> nói thêm một số kiến trúc, cái này đại khái là dựa trên ý tưởng
> dùng fc layer để **learn more abstract features** cho một local
> patches. Có thể tạm hiểu là filter khi 'tính toán' một receptive
> field thì thay vì sum thì nó sẽ qua một fc layer.
>
> Và cái này chính là tạm gọi là tiền thân của bottleneck layers trong
> GoogleNet và ResNet. Truyền cảm hứng cho GoogleNet

<br>

<a id="node-1118"></a>

<p align="center"><kbd><img src="assets/a955f2e7ba7b3da4c536fff520c586befe8efe62.png" width="100%"></kbd></p>

> [!NOTE]
> nguời ta tìm cách cải thiện hơn nữa resnet. Bằng
> cách tạo nhiều hơn các direct path giúp thông tin
> được propagate throughout network

<br>

<a id="node-1119"></a>

<p align="center"><kbd><img src="assets/0222441101df9e397f8f7c7abee5ad069230c73f.png" width="100%"></kbd></p>

> [!NOTE]
> đại khái là trong paper này người ta lập luận rằng residual connection là
> yếu tố quan trọng, chứ không phải là nhiều layer (not depth). Do đó
> người ta phát triển wide residual net, trong đó wide ở đây chỉ việc sử
> dụng nhiều filter hơn (nhân số filter cho factor k). Kết quả ở đây cho biết
> 50 layer wide resnet làm tốt hơn 152 layer original resnet

<br>

<a id="node-1120"></a>

<p align="center"><kbd><img src="assets/b41ec3a2084e0c1fedce0c59d4ad9c8a01a54abd.png" width="100%"></kbd></p>

> [!NOTE]
> Quay lại sau

<br>

<a id="node-1121"></a>

<p align="center"><kbd><img src="assets/1ae8e2823be3fabffdf7baa12c645b9e07c28211.png" width="100%"></kbd></p>

> [!NOTE]
> Quay lại sau

<br>

<a id="node-1122"></a>

<p align="center"><kbd><img src="assets/7f60c19d6a92cfde398d979b37bbdd91af55dac5.png" width="100%"></kbd></p>

> [!NOTE]
> Quay lại sau

<br>

<a id="node-1123"></a>

<p align="center"><kbd><img src="assets/7ac9e3cdbe3d0e72b6ea925ef1656df478c1e7cd.png" width="100%"></kbd></p>

> [!NOTE]
> DenseNet: các Dense block có các layer được kết nối với mọi layer
> khác theo feedforward fashion.
>
> Khắc phục tình trạng vanishing gradient, củng cố feature propagation
> và khích lệ feature reuse.

<br>

<a id="node-1124"></a>

<p align="center"><kbd><img src="assets/42087265a77fc9f8773b4ba2761b36809e1badba.png" width="100%"></kbd></p>

> [!NOTE]
> Quay lại sau

<br>

<a id="node-1125"></a>

<p align="center"><kbd><img src="assets/42bec258b6ca476fe6d886b597ee6c79c8f08fc7.png" width="100%"></kbd></p>

<br>

<a id="node-1126"></a>

<p align="center"><kbd><img src="assets/97197492fec0b66da8a73c1bace563d051cada10.png" width="100%"></kbd></p>

> [!NOTE]
> Tóm lại, VGG, GoogLeNet, ResNet là những kiến trúc được sử dụng
> rộng rãi, xuất hiện trong mọi model zoos. Trong đó ResNet là cái mặc
> định tốt nhất
>
> Có một xu hướng đến những network cực kì "sâu".
>
> Trọng tâm của các nghiên cứu hiện nay xoay quanh việc thiết kế ra
> layer/skip connection giúp khắc phục gradient flow.
>
> Những xu hướng nghiên cứu gần đây hướng tới việc kiểm tra tính cần
> thiết của 'dept' đối trọng với 'width' + residual connection.

<br>

