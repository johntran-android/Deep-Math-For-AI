# Mở Rộng Hơn Nữa

📊 **Progress:** `14` Notes | `31` Screenshots

---
<a id="node-1454"></a>

<p align="center"><kbd><img src="assets/740b741bde2ddc928a83ce0352989e9f4954b996.png" width="100%"></kbd></p>

> [!NOTE]
> Justin lướt qua một cái mà ổng làm với Andrej: Kết hợp
> object detect và image captioning

<br>

<a id="node-1455"></a>

<p align="center"><kbd><img src="assets/be9b4ab1cc62f10000f9a83c39f4f45f9656caff.png" width="100%"></kbd></p>

<br>

<a id="node-1456"></a>

<p align="center"><kbd><img src="assets/bd1433a325a23f55df97b21b3e6a02b029c47d59.png" width="100%"></kbd></p>

> [!NOTE]
> But the idea here is that once you have this, **you
> can kind of tie together a lot of these ideas** and if
> you have **some new problem** that you're
> interested in tackling like **dense captioning**, you
> can **recycle a lot of the components  that you've
> learned from other problems** like object detection
> and image captioning and kind of**stitch together
> one `end-to-end` network** that produces the outputs
> that you care about for your problem

<br>

<a id="node-1457"></a>

<p align="center"><kbd><img src="assets/45f186f1fdc26d54b1eb391d1b7feeb76d4d5f28.png" width="100%"></kbd></p>

<br>

<a id="node-1458"></a>

<p align="center"><kbd><img src="assets/c18c99a08123905dc8b44330bf69b98668db078a.png" width="100%"></kbd></p>

> [!NOTE]
> đại khái là người ta trong lĩnh vực cv phân biệt ra Things và Stuff. Things
> là những object mà ta sẽ muốn tách bạch từng cái, từng con
>
> còn stuffs thì ngược lại như bãi cỏ, bầu trời, cây cối...

<br>

<a id="node-1459"></a>

<p align="center"><kbd><img src="assets/fa8bfafd020864106ca785955cb0542591f4dcf7.png" width="100%"></kbd></p>

> [!NOTE]
> Cho nên ý nói, với object detection thì chỉ apply với things thôi, đương
> nhiên vì ko ai muốn detect từng ngọn cỏ cả. Còn với semantic segmentation
> thì cả things lẫn stuff

<br>

<a id="node-1460"></a>

<p align="center"><kbd><img src="assets/9aa894b3acc73adea5d24a8e2af21eb63a04253f.png" width="100%"></kbd></p>

> [!NOTE]
> nên Instance Segmentation là ta muốn detect từng object, và
> segmentation chúng

<br>

<a id="node-1461"></a>

<p align="center"><kbd><img src="assets/4caa2533700fd3d2f590ef81dece8d2c251b7a65.png" width="100%"></kbd></p>

> [!NOTE]
> vậh đầu tiên có thể dùng object detector để xác định từng
> object sau đó pass nó qua segmentation object

<br>

<a id="node-1462"></a>

<p align="center"><kbd><img src="assets/73ae3feb55270c90e9e17ecd27e26379d47fedca.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/73ae3feb55270c90e9e17ecd27e26379d47fedca.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/bc985cc120d8d35c4a62ec7192c6d7391bcc21c8.png" width="100%"></kbd></p>

> [!NOTE]
> vậy thì cái này chỉ cần dựa trên object detector model như Faster
> `R-CNN` nhưng có thêm một bước segmentation (mask prediction) nữa

<br>

<a id="node-1463"></a>

<p align="center"><kbd><img src="assets/c0015b1390112f02ec3726905d6b96703f26a63e.png" width="100%"></kbd></p>

> [!NOTE]
> đại khái là khúc đầu cũng giống `R-CNN` `-` dự đoán ra các proposed region.
> Sau đó, với mỗi region. một nhánh predict class và bounding box như trên,
> nhưng thêm một nhánh predict một mask cho mỗi class trong C class
> `-` giống bài toán segmentation
>
> Nói chung ý tưởng chính là kết hợp hết những kiến trúc của các bài toán
> segmentation, localization (**unifies all of these different problems** that we'
> ve been talking about today i**nto one nice jointly `end-to-end` trainable
> model**)

<br>

<a id="node-1464"></a>

<p align="center"><kbd><img src="assets/2c006068fbb7e59aae6a1274c77a812ab65ac533.png" width="100%"></kbd></p>

> [!NOTE]
> đại ý là với cái này thì cái target để train cho cái mask sẽ
> kiểu như là cái mask trên propose region

<br>

<a id="node-1465"></a>

<p align="center"><kbd><img src="assets/bc7b6507f16a38c656ba3f6faf999a12f6e38918.png" width="100%"></kbd></p>

<br>

<a id="node-1466"></a>

<p align="center"><kbd><img src="assets/61c81c3232432ea7429d077d0dd2477079e0047b.png" width="100%"></kbd></p>

> [!NOTE]
> thậm chí là kết hợp cáo
> pose prediction luôn

<br>

<a id="node-1467"></a>

<p align="center"><kbd><img src="assets/02e96d7743e256b411a3126e11053052a122cefc.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/02e96d7743e256b411a3126e11053052a122cefc.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/36e9e8b501973179e75a41d8c516604719a29384.png" width="100%"></kbd></p>

> [!NOTE]
> ngoài ra còn một task nữa mà người ta cũng làm là Panoptic segmentation,
> cũng như segmentation nhưng có phân biệt từng con bò (things) với nhau
> còn với stuff thì nó gộp chung

<br>

<a id="node-1468"></a>

<p align="center"><kbd><img src="assets/8ccbf8308dc8414b61231adaf7b4995a73558ede.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/8ccbf8308dc8414b61231adaf7b4995a73558ede.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f7d05bc734508f383bc68ed78be58815b9a3d969.png" width="100%"></kbd></p>

> [!NOTE]
> rồi còn có cái bài toán này, predict ra keypoints, tương tự chỉ
> cần mở rộng Faster `R-CNN` để nó predict thêm các keypoint
> positions

<br>

<a id="node-1469"></a>

<p align="center"><kbd><img src="assets/1a01290b46bfbce575bcafe96e0f091d7be17c61.png" width="100%"></kbd></p>

<br>

<a id="node-1470"></a>

<p align="center"><kbd><img src="assets/5f305284c9f923a3b00eac1dc268d61f9751f075.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/59420d64c343bddcb48ec1dcf5c13ec7e5658ac6.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/5f305284c9f923a3b00eac1dc268d61f9751f075.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/59420d64c343bddcb48ec1dcf5c13ec7e5658ac6.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d6a0d0966476c8581e07a0f71762da9bb8f821ad.png" width="100%"></kbd></p>

> [!NOTE]
> ý tưởng chung là có thể mở rộng để trở
> thành nhiều mô hình khác

<br>

<a id="node-1471"></a>

<p align="center"><kbd><img src="assets/2b6cfbed8556642f5e3e4f364aada120c0ba7ad2.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/2b6cfbed8556642f5e3e4f364aada120c0ba7ad2.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f6602f56658efbeec096a88f2e749518ac0b246a.png" width="100%"></kbd></p>

> [!NOTE]
> đại ý là có thể mở rộng hơn nữa để thành
> bài toán predict luôn 2D `->` 3D

<br>

<a id="node-1472"></a>

<p align="center"><kbd><img src="assets/db84bdd1b82b87e4a8d286846563f1bcedd8423e.png" width="100%"></kbd></p>

<br>

