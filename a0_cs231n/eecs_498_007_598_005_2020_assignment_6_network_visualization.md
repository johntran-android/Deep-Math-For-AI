# Eecs 498-007_598-005 (2020) Assignment 6: Network Visualization

📊 **Progress:** `9` Notes | `54` Screenshots

---
<a id="node-1731"></a>

<p align="center"><kbd><img src="assets/019f26bc22da45b7abf2dfe38252d63e485d1963.png" width="100%"></kbd></p>

> [!NOTE]
> đại ý là bình thường, khi train mô hình cho nhiệm vụ nào đó, ta sẽ pass image
> vào mô hình để tính ra prediction và loss, từ đó backpropagation để tính
> gradient của loss w.r. t model parameters.
>
> còn bây giờ, ta sẽ pass image (ban đầu để random), qua model mà model này
> đã được pretrained rồi, để tính loss rồi cũng backprop để tính gradient, có điều
> ta sẽ tính gradient của loss đối với image. Và dùng nó để thay đổi image khiến
> loss giảm chứ không phải thay đổi model params
>
> Vậy ta sẽ làm qua 3 cái liên quan đến cái này là Saliency Maps: giúp cho ta có
> thể hiểu được vùng nào của image ảnh hưởng nhất đến dự đoán của model.
>
> Adversarial Attack: Thay đổi một bức hình sao cho dưới mắt người thì nó vẫn 
> vậy, mà dưới mắt của mô hình thì nó là thứ khác.
>
> Class visualization: tạo image khiến tối đa hóa class score của một class nào đó
> từ đó có thể cho chúng ta hiểu được phần nào rằng khi model nó ra quyết định
> nó sẽ nhìn vào cái gì.

<br>

<a id="node-1732"></a>

<p align="center"><kbd><img src="assets/070ca24565e415edd23e654e939bb85394950b07.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/070ca24565e415edd23e654e939bb85394950b07.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0d0efb69adf502d83130b24c7f54281ff7e013a8.png" width="100%"></kbd></p>

> [!NOTE]
> như mới nói, ta sẽ dùng pretrained cnn model, thế thì họ chọn
> SqueezeNet, là model nhỏ hơn AlexNet nhưng có hiệu suất tương đương
> nhằm tiết kiệm chi phí tính toán và thời gian

<br>

<a id="node-1733"></a>

<p align="center"><kbd><img src="assets/3c0f3fd7edcca429bdc3fd072d6a11b5fa220400.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3c0f3fd7edcca429bdc3fd072d6a11b5fa220400.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/802e419cb25f391907b70aca9f8e963de0268c1f.png" width="100%"></kbd></p>

> [!NOTE]
> Load một vài ImageNet image

<br>

<a id="node-1734"></a>

<p align="center"><kbd><img src="assets/311317149e325f45628d1d94d1505032466fabbf.png" width="100%"></kbd></p>

> [!NOTE]
> để tạo saliency map với gradient, đơn giản là mình tính gradient của
> correct class score output từ last FC layer, đối với image pixel.
> vì image tensor RGB có shape 3xHxW, thì gradient cũng vậy. Nên ta sẽ
> lấy giá trị tuyệt đối và max trên 3 channel tại mỗi pixel để có kết quả là
> HxW.

<br>

<a id="node-1735"></a>

<p align="center"><kbd><img src="assets/eb37b4d1e1b514a01b44fd13cd8b5df64d9ec3e9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a483277eb7554fc6169cb6a8b0d8a198eeb9b334.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/eb37b4d1e1b514a01b44fd13cd8b5df64d9ec3e9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a483277eb7554fc6169cb6a8b0d8a198eeb9b334.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/9eea965ac8462b7925413e63fa0eb52976b07d7b.png" width="100%"></kbd></p>

> [!NOTE]
> Có thể thấy ví dụ như hình con chó, những vùng ảnh hưởng đến class score
> `-` loss nhất chính là vùng ảnh gắn với con chó

<br>

<a id="node-1736"></a>

<p align="center"><kbd><img src="assets/5cd93fb40f79f24a78e7df84f90d1be43bef6d7a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7f9e821a45e9c3b3e01510fd27f46bcdbb0d16d9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/45c0668164290306adeee8a4307115e920328757.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/80f2b0d0b248f56c7612e7c51466e7764aa0bb2d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/5cd93fb40f79f24a78e7df84f90d1be43bef6d7a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7f9e821a45e9c3b3e01510fd27f46bcdbb0d16d9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/45c0668164290306adeee8a4307115e920328757.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/80f2b0d0b248f56c7612e7c51466e7764aa0bb2d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6928de6d1bb94779f8c6e5082830b1374515ea84.png" width="100%"></kbd></p>

> [!NOTE]
> còn với Adversarial Attack, ta sẽ dùng tính gradient của một incorrect class
> core đối với image để update image theo hướng khiến class score này tăng
> lên (gradient ascent), và một khi wrong class score này đã vượt correct class
> score thì dừng. Lúc này mình đã tạo ra sự thay đổi tối thiểu để (hi vọng) mắt
> người ko nhận ra nhưng với model nó đã đoán sai

> [!NOTE]
> Forward qua model để có prediction (predicted class scores)
>
> Argmax để có predicted class id.
>
> Lúc này ta mới so sánh xem predicted class id có bằng với target class id
> `(target_y)` chưa, nếu có tức là model đã bị lừa, ta có thể dừng. Nếu chưa,
> ta sẽ tiếp tục dùng gradient để sửa lại image.
>
> Dùng view(1) để chuyển predicted class id thành vector dù chỉ có 1 phần
> tử, vì khi tính loss cần. Cũng chuyển nó lên cùng device với `pred_scores.`
>
> Tính loss cross entropy. Giữa predicted score và target y. Để rồi ta sẽ
> backprop, rồi update image sao cho loss giảm, có nghĩa là vẫn gradient
> descent với ý nghĩa loss giảm, thì đồng nghĩa là model phải đẩy class
> score của fake class tăng lên.
>
> Sau khi backward.
>
> Tính gradient norm (flatten thành vector, dùng torch.norm, và reshape lại
> thành (B,1,1,1) để `X/norm` sẽ chia mọi vị trí cho norm `(element-wise)`
>
> Normalized gradient xong thì dùng nó để update `X_adv` theo hướng ngược
> với gradient (để loss giảm, như đã nói bằng cách đẩy class score của wrong
> class lên

<br>

<a id="node-1737"></a>

<p align="center"><kbd><img src="assets/5b4fa64ac8fecd0aa9fadc1fcb39c99f9033eea9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/5b4fa64ac8fecd0aa9fadc1fcb39c99f9033eea9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/00e6499365e6c75393dac54225d95868f078c394.png" width="100%"></kbd></p>

<br>

<a id="node-1738"></a>

<p align="center"><kbd><img src="assets/29d1107931142df4fb0800237a13cf20e22580ae.png" width="100%"></kbd></p>

> [!NOTE]
> với cái này, ta sẽ bắt đầu với random noise image, và một target class và
> mục đích là dùng gradient ascent của target class score with respect to
> image để mà thay đổi nó theo hướng target class score ngày càng tăng lên.
>
> Bên cạnh đó có vài regularization technique nhằm khiến generated image
> trông tự nhiên hơn.
>
> Công thức có ý nghĩa là ta sẽ `tìm/tạo` ra image I sao cho tối đa hóa class
> score ứng với class y do model dự đoán khi đánh giá image I, Nhưng đồng
> thời phải giảm regularizer `-` dùng l2 regularizer.
>
> NGoài ra còn một cái gọi là implicit regularizer, bằng cách đều đặn định kì
> làm mờ bức hình.

<br>

<a id="node-1739"></a>

<p align="center"><kbd><img src="assets/3597bf323e6c484f66b63ef132415950a5fd00e0.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0bea8ff70c4c20618f7260ba99fd3622fecad0fa.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3597bf323e6c484f66b63ef132415950a5fd00e0.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0bea8ff70c4c20618f7260ba99fd3622fecad0fa.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e91d9f272ccf957a853c0501e87a79d3992c9a9d.png" width="100%"></kbd></p>

> [!NOTE]
> với cái này, ta sẽ bắt đầu với random noise image, và một target class và
> mục đích là dùng gradient ascent của target class score with respect to
> image để mà thay đổi nó theo hướng target class score ngày càng tăng lên.
>
> Bên cạnh đó có vài regularization technique nhằm khiến generated image
> trông tự nhiên hơn.
>
> Công thức có ý nghĩa là ta sẽ `tìm/tạo` ra image I sao cho tối đa hóa class
> score ứng với class y do model dự đoán khi đánh giá image I, Nhưng đồng
> thời phải giảm regularizer `-` dùng l2 regularizer.
>
> NGoài ra còn một cái gọi là implicit regularizer, bằng cách đều đặn định kì
> làm mờ bức hình.

<br>

<a id="node-1740"></a>

<p align="center"><kbd><img src="assets/ff79cd222d179a5ef1d8105822000944403e17ef.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ff79cd222d179a5ef1d8105822000944403e17ef.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d4035195d3b01bb9d66956c16c101fb4251144c8.png" width="100%"></kbd></p>

<br>

<a id="node-1741"></a>

<p align="center"><kbd><img src="assets/dd3764d0f8d86644ade8d6cac0aa16b851873159.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ae6e63083167865a30795638bfda908a2e980eed.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/8d32f88e3e6b6d626ac67219c39839e0b4967535.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e62924dc412b3b0f686f5be99362f4470a46567a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/46a535a9850ff864b5005031431e0c89d599ed72.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4f8d3c975e456aa8242cf9e39ddc6ebe4cf7b416.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/bfb4b86c727e8ac15929e365d5048e2470d528aa.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/dd3764d0f8d86644ade8d6cac0aa16b851873159.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ae6e63083167865a30795638bfda908a2e980eed.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/8d32f88e3e6b6d626ac67219c39839e0b4967535.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e62924dc412b3b0f686f5be99362f4470a46567a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/46a535a9850ff864b5005031431e0c89d599ed72.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4f8d3c975e456aa8242cf9e39ddc6ebe4cf7b416.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/bfb4b86c727e8ac15929e365d5048e2470d528aa.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/fe840b57fe8c0d9c5b220d55b3379af6183b1d0a.png" width="100%"></kbd></p>

<br>

<a id="node-1742"></a>

<p align="center"><kbd><img src="assets/b8b8a6ab2c22d00eeccd05eb254413da822f9042.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ebb4a2771b784a96d33f7f1fe9865d34c49cb0f1.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b8b8a6ab2c22d00eeccd05eb254413da822f9042.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ebb4a2771b784a96d33f7f1fe9865d34c49cb0f1.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/027f41d512a71dbffb8ed0e03f7bf10d57339934.png" width="100%"></kbd></p>

<br>

