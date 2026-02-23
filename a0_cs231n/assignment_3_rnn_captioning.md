# Assignment 3 - RNN Captioning

📊 **Progress:** `12` Notes | `64` Screenshots

---
<a id="node-1218"></a>

<p align="center"><kbd><img src="assets/bab7f7f77783ba96d42643a18dfc7465f5f5b7df.png" width="100%"></kbd></p>

<br>

<a id="node-1219"></a>

<p align="center"><kbd><img src="assets/1d3af1aac8afac6ba3ba6d2bfeded76399c4ad54.png" width="100%"></kbd></p>

> [!NOTE]
> chạy dòng code có sẵn để chạy cái script tải bộ dữ liệu coco về

<br>

<a id="node-1220"></a>

<p align="center"><kbd><img src="assets/150466077303187bcfbf7c729ca3d0cb82c0819c.png" width="100%"></kbd></p>

> [!NOTE]
> không hiểu sao lần này khi nó chạy tới from `cs231n.rnn_layers`
> import * và mấy dòng import sau đều bị lỗi, thử nhiều cách,
> cuối cùng thấy thêm cái path dẫn tới cs231n vào sys.path giúp
> giải quyết được lỗi này.

<br>

<a id="node-1221"></a>

<p align="center"><kbd><img src="assets/2902c6dab2ad4949e2d26393408b1cbffbec51e0.png" width="100%"></kbd></p>

> [!NOTE]
> Nói về COCO dataset, người ta cho biết đây là bộ dữ liệu tiêu chuẩn cho bài
> toán "image captioning". Bộ dữ liệu chứ 80.000 training images và 40000
> validation images. Mỗi bức hình có 5 dòng caption được viết bởi con người sử
> dụng nền tảng Amazon Mechanical Turk.
>
> Image feature: Thì đại ý là **người ta đã extract feature sẵn**, mà như đã nói
> trong bài giảng, người ta**"đưa image qua" một CNN** để có được một
> **embedding feature vector**, mang thông tin của bức hình trước khi được
> chuyển vào RNN để generate caption. Thì ở đây người ta đã làm bước này, với
> mô hình **VGG16**, và cụ thể là họ dùng **output của cái `fully-connection` layer
> fc7**, là một vector có số **dimension là 4096** (dễ hiểu fc7 có **4096** neuron).
> Thế, các image từ training set và validation set đã được chuyển thành các
> embedding vector, lưu trong file tương ứng.
>
> Thêm một bước nữa, họ dùng PCA để giảm chiều không gian `/` "nén" từ `4096-d`
> vector thành**512-d** để nếu cần có thể dùng nó để tiết kiệm memory và compute.
>
> Ngoài ra, trong đây do dung lược của bộ hình gốc quá lớn tới 20GB, nên họ chỉ
> để các url, để cần dùng thì mở ra xem. Vì hình ảnh này thì cũng trên Flicker chứ
> đâu
>
> `===`
>
> Phần caption, họ đã chuẩn bị vocab dict để mình chuyển một từ thành ra id
> Cũng như function để làm ngược lại. Cái này là để `encode-decode` input và
> output của RNN
>
> `===`
>
> Cuối cùng là nói về các special token, họ cũng đã giúp ta thêm <START> và
> <END> token vào đầu và cuối câu (caption). Cũng như là pad các câu ngắn với
> <NULL> token để mình đã có các sequence dài bằng nhau cho việc  Batching.

<br>

<a id="node-1222"></a>

<p align="center"><kbd><img src="assets/943541fd3ca7cd5790a219250c2dea2aed131314.png" width="100%"></kbd></p>

> [!NOTE]
> Có thể thấy `train_caption` đã được tokenized và (zero) padded sẵn
> cho mình rồi
>
> Dùng function `idx_to_word` để chuyển token ra lại word string.

<br>

<a id="node-1223"></a>

<p align="center"><kbd><img src="assets/598815d3e78063c5167907d1a356a9cbdb32ba54.png" width="100%"></kbd></p>

<br>

<a id="node-1224"></a>

<p align="center"><kbd><img src="assets/585a18d6a0d12ba439e9bc43a3f23a146b7836b9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/585a18d6a0d12ba439e9bc43a3f23a146b7836b9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0730bae835c6ef490c8406ed27af47d7a8b0db75.png" width="100%"></kbd></p>

<br>

<a id="node-1225"></a>

<p align="center"><kbd><img src="assets/58969a871daab65e8c259729709ac0f4725c7d46.png" width="100%"></kbd></p>

> [!NOTE]
> cơ bản là dễ, chỉ có điều cần
> xử lý shape cho đúng

<br>

<a id="node-1226"></a>

<p align="center"><kbd><img src="assets/6e546ba56c6b15f35ea25d7d554a548d8dbf7590.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6e546ba56c6b15f35ea25d7d554a548d8dbf7590.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3031d10f032269814c0932c2649bc9c0455b65d8.png" width="100%"></kbd></p>

<br>

<a id="node-1227"></a>

<p align="center"><kbd><img src="assets/57643a16053eb3c589bd968a2f30b4ecd922a325.png" width="100%"></kbd></p>

> [!NOTE]
> Theo computation graph thôi, transpose matrix để ra shape phù
> hợp.
>
> Nhớ rằng b được broadcast, nên nó tham gia với mọi `w_i.x_i` `(+` b)
> để ra `z_i` nên db `=` sum(dz)

<br>

<a id="node-1228"></a>

<p align="center"><kbd><img src="assets/4dcf9045cc56415d293ce4c7aa3c628b5fe3109c.png" width="100%"></kbd></p>

<br>

<a id="node-1229"></a>

<p align="center"><kbd><img src="assets/7cf0595da0c2fcc1e26485d1155d15f8cad53d01.png" width="100%"></kbd></p>

<br>

<a id="node-1230"></a>

<p align="center"><kbd><img src="assets/9e6f9c7ac24a4dd65d17aa7db99c97ee2dc16a6b.png" width="100%"></kbd></p>

<br>

<a id="node-1231"></a>

<p align="center"><kbd><img src="assets/dc8b234bd562a8f07c35c96b9a50b38761f325ed.png" width="100%"></kbd></p>

<br>

<a id="node-1232"></a>

<p align="center"><kbd><img src="assets/577b5afe5f86d8c7b93b25bff17f448ebc5431e4.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/577b5afe5f86d8c7b93b25bff17f448ebc5431e4.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4530d477375a7aa07db3d7e0082eae65f649172c.png" width="100%"></kbd></p>

> [!NOTE]
> 1. Đại ý tại mỗi step, dùng `rnn_step_backward` để từ upstream grad tính các
> dWx, dWh, dxt,  `dh_prev`
>
> Thì, đảm bảo upstream grad (là dh<t>) là tổng của gradient do L<t> mà h<t>
> "Trực tiếp tham gia" và  gradient do các L sau mà h<t> gián tiếp tham gia khi 
> tính `h<t+1>` . Biểu hiện bằng mũi tên màu hồng.
>
> 2. Vì Wh (Wx tương tự) tham gia tính toán tại mỗi `time-step` nên đơn giản
> là tại mỗi `rnn_step_backward` tính được dWh thì cộng dồn vào.
> Và nếu muốn suy nghĩ sâu xa hơn thì vì upstream gradient là "đã gồm ảnh
> hưởng tới L<t> và cả các L sau đó) nên đã có phần gradient của Wh khi nó
> "Trực tiếp tính Lt" và "gián tiếp tính các L sau đó" (Ý là không sợ thiếu gradient
> cho W) nếu đảm bảo ý 1.
>
> 3. Cho dxt thì dễ rồi tại step nào thì assign vào t của dx đó.

<br>

<a id="node-1233"></a>

<p align="center"><kbd><img src="assets/d223286491078464d46bfa3465d418f4dfde8912.png" width="100%"></kbd></p>

<br>

<a id="node-1234"></a>

<p align="center"><kbd><img src="assets/f7d2a0f92b6ff8d05ca7cd2d31f98abcf3d8e7e7.png" width="100%"></kbd></p>

<br>

<a id="node-1235"></a>

<p align="center"><kbd><img src="assets/4652d4a8a3a868e25c0129d138befe701733fa5f.png" width="100%"></kbd></p>

<br>

<a id="node-1236"></a>

<p align="center"><kbd><img src="assets/4602849c567bb11fa864972c1f041b8b2691e81d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/de01f6589987890a526ac217a78697de2dfdc326.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4602849c567bb11fa864972c1f041b8b2691e81d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/de01f6589987890a526ac217a78697de2dfdc326.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d4cd99f461f557869cec6f411948232db4763d79.png" width="100%"></kbd></p>

<br>

<a id="node-1237"></a>

<p align="center"><kbd><img src="assets/3a29cfec05276a98b87d9d3d8032aa1f1c97d07c.png" width="100%"></kbd></p>

<br>

<a id="node-1238"></a>

<p align="center"><kbd><img src="assets/9be089da6131f185ab249a63982f223fe40d0c00.png" width="100%"></kbd></p>

> [!NOTE]
> Cái này chỉ là affine transform từ
> `ht->y^t` nên họ làm giùm

<br>

<a id="node-1239"></a>

<p align="center"><kbd><img src="assets/36ff175e6c94b99529d3cd5844f3be054831cde9.png" width="100%"></kbd></p>

<br>

<a id="node-1240"></a>

<p align="center"><kbd><img src="assets/344a40dbaa03524601a77e2769643782ba003f90.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/344a40dbaa03524601a77e2769643782ba003f90.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d12c31b0d3e6ae8617c36ead6ef98e4f291550ae.png" width="100%"></kbd></p>

> [!NOTE]
> cái này người ta ko bắt làm nhưng vẫn làm
> lại vì nó có vụ T cũng như mask

<br>

<a id="node-1241"></a>

<p align="center"><kbd><img src="assets/9ffdd3544353ef5c397fa3fa507d060a87907106.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/9ffdd3544353ef5c397fa3fa507d060a87907106.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/443d53d1fa82edcfb2ab3322f04e5d99840aff5d.png" width="100%"></kbd></p>

> [!NOTE]
> Solution chuẩn của Standford có thể học theo

<br>

<a id="node-1242"></a>

<p align="center"><kbd><img src="assets/623f0062811fe4c38cb90f1d881f2311d61a54b7.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/623f0062811fe4c38cb90f1d881f2311d61a54b7.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/de80e38d7d5ba23b36668bc1fc3cfc2e5bd1797e.png" width="100%"></kbd></p>

<br>

<a id="node-1243"></a>

<p align="center"><kbd><img src="assets/a30d5bb7d66704b93ea4649944a4dc1b6dc5a1e9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a30d5bb7d66704b93ea4649944a4dc1b6dc5a1e9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c9ec540e6df814aa978030a311b52b8f43469b1c.png" width="100%"></kbd></p>

<br>

<a id="node-1244"></a>

<p align="center"><kbd><img src="assets/1c27d4ba602b2f4e63dce55b604ede35f25279ed.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e5ecca843e51a926d27ede602a37944e0ffb0cbc.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1c27d4ba602b2f4e63dce55b604ede35f25279ed.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e5ecca843e51a926d27ede602a37944e0ffb0cbc.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/39eb207277d1117e220197f466fa95f15ce8db45.png" width="100%"></kbd></p>

<br>

<a id="node-1245"></a>

<p align="center"><kbd><img src="assets/14a24c67e593af409a054b4903691c759f9f1cc0.png" width="100%"></kbd></p>

<br>

<a id="node-1246"></a>

<p align="center"><kbd><img src="assets/6334e5b3632a04d54686d974cb7aee0b0132ff03.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6334e5b3632a04d54686d974cb7aee0b0132ff03.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/039b595f5302dfe054d1cf757e6b1b8b59424296.png" width="100%"></kbd></p>

<br>

<a id="node-1247"></a>

<p align="center"><kbd><img src="assets/12386509482e91faa7086acecdf8c2ed27952a48.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/12386509482e91faa7086acecdf8c2ed27952a48.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ac40f588125f52654ab576b8e48d819c4d82809f.png" width="100%"></kbd></p>

<br>

<a id="node-1248"></a>

<p align="center"><kbd><img src="assets/711e8062c7181e7ffbbd16dc2d8c19fd74b6c63f.png" width="100%"></kbd></p>

<br>

<a id="node-1249"></a>

<p align="center"><kbd><img src="assets/6852b81b95c2a43e9a51709cbf468d6ad28189cb.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6852b81b95c2a43e9a51709cbf468d6ad28189cb.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/151c70c73bc4d019a96d735c58f28509a8a3b783.png" width="100%"></kbd></p>

> [!NOTE]
> Affine layer chuyển image embedding thành h0,
> Chuẩn bị (một batch) các <START> token id.
> Pass qua embedding layer để chuyển thành các
> word encoding vector đưa vào as x0.
>
> Sau đó lần lượt gọi function `rnn_step_forward` để
> tính ht, dùng affine để chuyển thành y^ và Argmax
> để lấy ra in tương ứng từ có p cao nhất, assign
> vào captions (chú ý không cần chuyển qua word
> string, captions yêu cầu chứa word id)
>
> Tiếp tục ht tính bước tiếp theo cùng với từ được
> chọn ở `time-step` trước

<br>

<a id="node-1250"></a>

<p align="center"><kbd><img src="assets/3710f1baf75615914f47282e69413e41591d8916.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3710f1baf75615914f47282e69413e41591d8916.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/2e8f4b60dc36bd7efa96fbfe04d73b63da479622.png" width="100%"></kbd></p>

<br>

<a id="node-1251"></a>

<p align="center"><kbd><img src="assets/4aa1b4854330e319650fef9a3ba82ffe2835d743.png" width="100%"></kbd></p>

> [!NOTE]
> trả lời vài ý, quay lại sau, giờ làm qua
> LSTM Captioning luôn

<br>

