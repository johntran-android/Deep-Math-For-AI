# Eecs 498-007_598-005 (2020) Assignment 4 (part 2): Two-stage Detector - Faster Rcnn

📊 **Progress:** `25` Notes | `161` Screenshots

---
<a id="node-1644"></a>

<p align="center"><kbd><img src="assets/ef2c7c6f4c7ec1cc12a4a128799a482313299352.png" width="100%"></kbd></p>

> [!NOTE]
> Phần một của Faster RCNN object detector là Region Proposal Network
> - RPN, nó sẽ làm nhiệm vụ (học cách) classify một anchor có chứa một
> object hay không, và nếu có thì nó sẽ regress / dự đoán ra một phép 
> transformation để convert anchor box thành gt box.
>
> RPN có nhiều điểm chung với Single-Stage detector nơi mà ta cũng dự
> đoán một anchor box có chứa một object hay không (confidence score)
> cũng như là một transformation để transform anchor box thành bounding
> box. Nên về cơ bản là RPN chỉ không predict một grid center là class gì
> mà thôi.
>
> Do đó ta sẽ dùng lại nhiều component của mô hình Single Stage Detector
> YOLO ở phần 1

<br>

<a id="node-1645"></a>

<p align="center"><kbd><img src="assets/efbe49a8fd702139c8ed0f7d17f0c9278ffd12c9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/efbe49a8fd702139c8ed0f7d17f0c9278ffd12c9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e815b8b5ce62d6c148af765cae0de791b9b44402.png" width="100%"></kbd></p>

> [!NOTE]
> Nói về việc "gán ghép" một anchor với một gt box mà ta phân tích function
> ReferenceOnActivatedAnchors. Trong đó với Faster RCNN rules, một anchor
> sẽ được gán ghép với một gt box nếu nó thỏa một trong hai điều kiện:
>
> 1. Đối với một gt box nào đó, trong số mọi iou của các anchor box, thì nó là
> cái có iou lớn nhất.
>
> 2. Anchor box sẽ được gán với gt box nếu IoU của nó với gt box lớn hơn 0.7
>
> Thế thì thật ra phần lớn trường hợp ta sẽ có điều kiện hai, còn điều kiện một
> là để một số hiếm trường hợp, không có anchor nào có iou với box nào lớn
> hơn 0.7.
>
> Ngoài ra, một anchor nếu không có IoU với box nào lớn hơn 0.3, thì nó sẽ 
> là Negative box, cũng tham gia vào quá trình huấn luyện. Còn những anchor
> giữa giữa - Neutral thì bị ignore.
>
> (còn YOLO: một anchor sẽ được gán ghép cho một gt box nếu tâm của nó
> activate - có nghĩa là vị trí tâm là gần với tâm của gt box nhất  trong số các
> grid center, đồng thời, trong số các anchor tại activate center đó thì nó là cái
> có IoU lớn nhất)
>
> Tóm lại, mình sẽ dùng lại các component như GenerateGrid, GenerateAnchor,
> IOU, và ReferenceOnActivatedAnchors

<br>

<a id="node-1646"></a>

<p align="center"><kbd><img src="assets/c02822233a856accd1182668290436333e7b3fbd.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/fd90502970d39edae0539f13f959540a8b970153.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/46ccafe64b1d737f5f128e2083c59928857115c0.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/67a3ff6e23c2e2dbd29a77c8e921f319ff2f7677.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c02822233a856accd1182668290436333e7b3fbd.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/fd90502970d39edae0539f13f959540a8b970153.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/46ccafe64b1d737f5f128e2083c59928857115c0.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/67a3ff6e23c2e2dbd29a77c8e921f319ff2f7677.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/08bdd9d2d91b57ca20b3cfb6d0a6cbebfb3315d3.png" width="100%"></kbd></p>

<br>

<a id="node-1647"></a>

<p align="center"><kbd><img src="assets/4153096f527a100cc50d87581b88d281cdda7303.png" width="100%"></kbd></p>

> [!NOTE]
> Với k, hay A là số anchor tại mỗi location (grid cell center) thì  đại khái là như 
> đã nói ở slice trước về nhiệm vụ của PRN, thế thì cụ thể nó sẽ cần tính toán 
> và output ra:
>
> 1. Hai giá trị class score ứng với hai class: Có hay không có chứa một object
> Như part2 của version 2022, thật ra lúc làm ta chỉ dùng hàm sigmoid để output
> ra một giá trị ứng với P(có object), nhưng thích thì tính ra hai giá trị P(có object)
> và p(không có object) cũng được, khi đó ta sẽ dùng softmax để chuyển hai logit
> thành probabiity.
>
> 2. 4 giá trị box regression: tx, ty, tw, th, làm thành một phép biến đổi để tranform
> anchor box thành object box.

<br>

<a id="node-1648"></a>

<p align="center"><kbd><img src="assets/171f0222e24f77d404bfd62ecc7ddb6ca00514b7.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/171f0222e24f77d404bfd62ecc7ddb6ca00514b7.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b21206547d19bc123e144d3bbc586d91cf6a682c.png" width="100%"></kbd></p>

> [!NOTE]
> kiến trúc của cái này tương tự PredictionNetwork, chỉ khác là nó chỉ output
> ra tại mỗi một location output ra vector có 6*A phần tử  (A anchors/locations,
> 6 giá trị (4 box regression + 2 object-ness classification)
>
> Chú ý là conv layer đầu tiên kernel size = 3x3, để same padding thì thì
> padding = 1. Còn conv layer thứ hai kernel size = 1x1, nên padding = 0.
>
> Ta cũng chuẩn bị anchor_list: define 9 kích thước của các anchors, như ở
> trên nói, ta sẽ dùng các giá trị giống như của part 1

> [!NOTE]
> Tham khảo solution của seloufian: Ổng dùng Dropout2d

<br>

<a id="node-1649"></a>

<p align="center"><kbd><img src="assets/c0fbce44c245ac549afec4dec3ba90b3417fb914.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e39d70438da7594b3c875bd81210fb6b0670a3eb.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/2987a7c1badee5d9fae1b220a69537f13618b661.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1741f1e3e87e85ff3bd79d8dfd924d486b1e6ea9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/623cd00a87d87547ede7b0b988a02b99a814a1bb.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1a1d5c0f62871b11d4b2d35e67978768f538348d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/74960314ca85c6796ff50b328a5a0bf3eac212aa.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c0fbce44c245ac549afec4dec3ba90b3417fb914.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e39d70438da7594b3c875bd81210fb6b0670a3eb.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/2987a7c1badee5d9fae1b220a69537f13618b661.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1741f1e3e87e85ff3bd79d8dfd924d486b1e6ea9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/623cd00a87d87547ede7b0b988a02b99a814a1bb.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1a1d5c0f62871b11d4b2d35e67978768f538348d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/74960314ca85c6796ff50b328a5a0bf3eac212aa.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ea83f48a12148b1656cbe18d2cba0015e8812631.png" width="100%"></kbd></p>

> [!NOTE]
> Quá trình tính toán rất tương tự PredictionNetwork:
>
> - Forward qua prediction layer sau đó dùng permute để
> transpose, view để reshape về dạng phù hợp trong đó ứng với
> mỗi anchor là một 6D vector.
>
> - Thế thì hai phần tử đầu sẽ là confidence scores (binary
> classification logits) và 4 phần tử sau sẽ là box regression. Nên
> ta sẽ slicing cho phù hợp.
>
> - Khi đã có offsets thì nhờ function GenerateGrid,
> GenerateAnchor, và. GenerateProposals để tạo ra grids,
> anchors, và proposals.
>
> Ở đây người ta đã chia giùm hai mode 'train' và 'eval', thì**với
> train mode ta sẽ nhờ function _extract_anchor_data để "lấy ra"
> các kết quả ứng với positive và negative anchor thôi.**
>
> Nói chung là sau khi đã làm ở part1 thì function này tương đối dễ

> [!NOTE]
> Tham khảo solution của seloufian: Hơi khác ở chỗ,
> của mình thì pass offset (mọi offsets và anchors coord)
> vào  GenerateProposals, để có mọi proposals.
>
> Sau đó dựa vào positive anchor indices để lấy ra các
> proposals của các positive anchors.
>
> Còn Seloufian sẽ chỉ pass positive offsets và anchors's
> coord để có proposals

<br>

<a id="node-1650"></a>

<p align="center"><kbd><img src="assets/c7a56df1143a93f2014df93675ff74636a7e7b95.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c7a56df1143a93f2014df93675ff74636a7e7b95.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/81ca67313cd05e10e35c4930e8a22869cd8aa59b.png" width="100%"></kbd></p>

> [!NOTE]
> Xem qua hai function giúp tính loss. Cái đầu có thể thấy input là predicted
> confidence score (2M, 2), với M "hàng" trên là "của" positive anchor, M "
> hàng dưới" là của negative anchor. Vì là bài toán binary classification, họ
> tạo target, ứng với positive class là các vector [1,0], còn target cho negative
> sample là [0,1]. Và dùng binary cross-entropy with logits giúp tính binary
> classification loss.
>
> Còn với box regression thì dùng smooth_l1_loss

<br>

<a id="node-1651"></a>

<p align="center"><kbd><img src="assets/7739e82464023e8c779ddf168dc7d7113e400d6c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/13cb3de04c835a7662e47f3c5c6c2d670b46fc7d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/77722821a7b7146c706f2937be71cbe81fa2a8ff.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/55d9d9222f014cec94e3574cdc7bbbe5847be497.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a0c2dfd3fe1a15bb9d4b5c4a64957dcd35a507c8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7739e82464023e8c779ddf168dc7d7113e400d6c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/13cb3de04c835a7662e47f3c5c6c2d670b46fc7d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/77722821a7b7146c706f2937be71cbe81fa2a8ff.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/55d9d9222f014cec94e3574cdc7bbbe5847be497.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a0c2dfd3fe1a15bb9d4b5c4a64957dcd35a507c8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/9d90f102cef2bb0d5bb06dfa562019da2ff2d584.png" width="100%"></kbd></p>

> [!NOTE]
> 1. Inference qua backbone cnn (feature extractor) để có features (B,depth,
> H',W')
>
> 2. Generate grid, anchors, iou matrix sử dụng các function GenerateGrid,
> GenerateAnchor, IoU từ part 1.
>
> grid: (B,H',W',2)   anchors (B,A,H',W',4)   bboxes (B,N,5)
>
> iou_mat: (B, AH'W', N)
>
> Sau đó pass vào ReferenceOnActivatedAnchor để nó giúp làm  cái bước
> gán ghép (matching) các positive anchor với gt box. Kết quả là các tensor
> liên quan đến positive, negative anchor trong đó M LÀ TỔNG SỐ
> POSITIVE ANCHOR**TRONG BATCH**
>
> pos_anchor_idx: [M],     neg_anchor_idx: [M] :
>
> GT_conf_scores: [M]    GT_offsets: [M, 4]     GT_class: [M]
>
> ====
> Chú ý khúc này:
>
> \/***GT_conf_scores** có shape (M) là thật ra **chính là iou của các positive
> anchor với matched gt box của nó**. Và ta sẽ không dùng cái này, ở part1
> YOLO, có thể xem lại để thấy để tính confidence loss thì trong function
> người ta tạo target là 1 cho positive anchor, và 0 cho negative anchor và
> dùng Mean Square Error 
>
> Với part 2 cũng vậy **chỉ pass predicted confidence score** - (2M,2) (gồm cả
> positive và negative anchor) vào function **ConfScoreRegression**, ở **trong
> đó nó sẽ tạo target cho positive anchor là [1,0]**, và **negative anchor là [0,1]**.
> Và dùng **binary cross entropy loss.**\/
>
> ====
>
> 3. Pass features qua cho Region Proposal module cùng với pos_anchor_idx + 
> pos_anchor_coord để nó predict ra confidence scores, box regression và 
> proposals ở train mode tức là của positive/negative anchors
>
> conf_scores: (2M,2)     offsets (M,4)    proposals(M,4)

> [!NOTE]
> Tham khảo solution của seloufian: Cơ bản là giống, ngoại trừ mình mắc
> một sơ suất trong việc tính giá trị của anc_per_img phát hiện được nhờ 
> đối chiếu với Seloufian's solution

<br>

<a id="node-1652"></a>

<p align="center"><kbd><img src="assets/1c4b8f9b3bb503376540d4fdb3731fd8f280185d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/dd59e74d72074fc361cdd6bbd95b41e2110f9289.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c06bd50ca886f6600f1cf7b476feb2e9b5c6b535.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/1c4b8f9b3bb503376540d4fdb3731fd8f280185d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/dd59e74d72074fc361cdd6bbd95b41e2110f9289.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c06bd50ca886f6600f1cf7b476feb2e9b5c6b535.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e3af2db7e7450e13cce36736fc1b836c5cd9aa96.png" width="100%"></kbd></p>

> [!NOTE]
> Training cho thấy loss nhỏ hơn 3 như họ
> expect cho thấy ta đã làm đúng

<br>

<a id="node-1653"></a>

<p align="center"><kbd><img src="assets/a0c0f3baba461d79ddbc67bea5a4309c9d7992df.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ff07ae2fad9349c53cc553e61cd18e39e4cfcbe2.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/97c7b2bef3596a8105a9bab310b8e9a6974ddba6.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0b7591e89a5192238f067b27699409e3cb2ff1a7.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/2888541d0df107713eadcd9eac4dbc1d5b357760.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/274dce7c3a5e5faac21b9630b9de8f6a58983c03.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a0c0f3baba461d79ddbc67bea5a4309c9d7992df.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ff07ae2fad9349c53cc553e61cd18e39e4cfcbe2.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/97c7b2bef3596a8105a9bab310b8e9a6974ddba6.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0b7591e89a5192238f067b27699409e3cb2ff1a7.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/2888541d0df107713eadcd9eac4dbc1d5b357760.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/274dce7c3a5e5faac21b9630b9de8f6a58983c03.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/73f8c4210754d0717bb892cab889fc9946ef1492.png" width="100%"></kbd></p>

> [!NOTE]
> ==LÀM NGUYÊN BATCH
>
> 1. FEATURE EXTRACTOR: Pass images tensor qua backbone cnn để extract feature
> maps.
>
> 2. PREDICT PROPOSED REGION: Pass features qua ProposalModule để predict 2
> tensor: Mỗi anchor: 2 gía trị object-ness confidence score (hay logit) và 4 giá trị box 
> offsets của mỗi anchors
>
> conf_scores (B,A,2,H',W') và offsets (B,A,4,H',W')
>
> 3. GENERATE GRID, ANCHOR VÀ PROPOSALS. Với predicted offsets, ta sẽ chuyển
> nó thành predicted proposals region nhờ function GenerateProposal đã làm. Thế thì
> nó sẽ cần thêm anchors (coordinate các anchors), nên ta cần tạo grids (với Generate
> Grid, và pass vào GenerateAnchor để có anchors)
>
> grid: (B,H',W',2)    anchors (B,A,H',W',4)    proposals (B,A,H',W',4)
>
> ==LÀM TỪNG SAMPLE
>
> 4. THRESHOLD: Tới đây phải làm CHO TỪNG SAMPLE RIÊNG, vì bước này
> ta sẽ xem thử với mỗi images, proposal box nào có object-ness probability thấp quá
> thì loại bỏ, sau đó loại bỏ bớt lần nữa qua Non-Maximal Suppression.
>
> Đầu tiên ta cần chuyển object confident scores thành object probability thông qua hàm
> \~SOFTMAX \~ **SIGMOID** (Sau khi đọc lại thì thấy học gợi ý dùng sigmoid, dù mình nghĩ hàm 
> softmax vẫn đúng nhưng cứ làm theo gợi ý). 
>
> Ta sẽ thresholding positive probability, là cái đầu trong hai cái. (A,H',W').
> Sau đó ta mới flatten thành ra một AH'W' vector, và pass vào torch.nonzero để lấy ra
> vector chỉ chứa indices (trong range 0-AH'W') của các vị trí khác 0. 
>
> keep_idx: (no.thresholding keep i) #no.thresholding keep i: ý nói số lượng giữ lại sau khi 
> threshold của sample I (mỗi sample sẽ mỗi khác)
>
> Và ta sẽ dùng nó để slicing các tensor proposals (cần chuyển về shape (AH'W',4)) và
> confidence probabilities (cần chuyển về shape (AH'W', 2)) trước khi slicing
>
> final_proposals_i (no.thresholding keep i, 4)
> final_conf_probs_i (np.thresholding keep i, 2)
>
> 5.NMS: Bước cuối cùng là loại bỏ bớt thông qua nms, đơn giản là pass object probabilities
> vào nms() để trả ra keep idx - **nms_keep_idx** vector chứa các id của các proposals sẽ được 
> giữ lại. Và ta sẽ dùng nó để slicing lần nữa trước khi add vào list final_proposals
>
> final_proposals_i (no.nms keep i, 4)
> final_conf_probs_i (np.nms i, 2)

> [!NOTE]
> Function này sẽ nhận tensor images với hai cái threshold, nhiệm vụ là trả
> ra: các proposed region và object confidence (object probability).
>
> Thì vì mỗi image sẽ có các proposal regions khác nhau, nên output sẽ  là
> dạng list, chứa B item, mỗi item ứng với một image. Gọi P_i là số proposed
> box còn lại của sample i sau khi loại bỏ bớt ở bước thresholding (tức là chỉ
> giữ những region có object probability cao) và ở bước nms. Thì ta với
> sample  i, hai tensor vại vị trí i trong hai list sẽ là là proposal i (P_i, 4) và
> confidence (P_i)

> [!NOTE]
> Tham khảo solution của seloufian: Hơi khác chút xíu ở chỗ:
>
> - Họ dùng sigmoid để chuyển thành probability
>
> - Threshold - liên quan đến cách mask và slicing. Tương tự
> như ở part 1 YOLO, đại ý cách làm của anh này là tạo và dùng
> boolean mask để sclicing, còn mình thì tạo non-zero indices để
> slicing.

<br>

<a id="node-1654"></a>

<p align="center"><kbd><img src="assets/9d252c869fb9dcb1b38b5cb796d3565dc4d3ca60.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3dfb4033704579a23d58535bae1b04b4cb75562c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/5020ce415196051aa13c8f96df9c61f51a1e11d7.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/233ef8830684a5f4fadbe2ae078d479ba568ba1d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0a1ab65e8b4913bf712cf351c5203661c4c20725.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/8d4a659413dbceef39f506e74a897bd463314e26.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4381d08d91a5fd796c84e7e4ba4398f4e23a0d95.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/097525cb0182fd0295c63446b3003a46fe00617c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b3e50ced01e4cdb244cea196e82b48d540f6451d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f4179431e0b1b881e74a7e928ac57bdbca47f07e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/9d252c869fb9dcb1b38b5cb796d3565dc4d3ca60.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3dfb4033704579a23d58535bae1b04b4cb75562c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/5020ce415196051aa13c8f96df9c61f51a1e11d7.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/233ef8830684a5f4fadbe2ae078d479ba568ba1d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0a1ab65e8b4913bf712cf351c5203661c4c20725.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/8d4a659413dbceef39f506e74a897bd463314e26.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4381d08d91a5fd796c84e7e4ba4398f4e23a0d95.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/097525cb0182fd0295c63446b3003a46fe00617c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b3e50ced01e4cdb244cea196e82b48d540f6451d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f4179431e0b1b881e74a7e928ac57bdbca47f07e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ef76538fde59c91f7d71f33a7607a48d9e16c5ff.png" width="100%"></kbd></p>

<br>

<a id="node-1655"></a>

<p align="center"><kbd><img src="assets/ed733600de1855d428120de52510726edc93ee45.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/03dcfaf77ac4d2fb22b05da394623c7c2919f407.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ba26f41caa455ad8268b4812ee9900a08a4b7ccb.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0fa8cf0b2e8eddb79277bacee848fc8d969f5b96.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ed733600de1855d428120de52510726edc93ee45.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/03dcfaf77ac4d2fb22b05da394623c7c2919f407.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ba26f41caa455ad8268b4812ee9900a08a4b7ccb.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0fa8cf0b2e8eddb79277bacee848fc8d969f5b96.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3a76f1c4636eb4cdc0f314e0844a65372fd5e8e9.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi, đây sẽ là mô hình Faster RCNN với hai stages, Trong init, ta sẽ define RPN module, và một Classification module đóng vai trò
> stage 2, nhận các feature của các "proposal  region" để dự đoán xem là class gì.
>
> Cấu tạo của classification layers ta hiểu là cần hai fully connected layer (xen kẽ bởi Dropout, ReLU).  FC layer đầu tiên sẽ nhận
> input là từ một tensor có shape [C,H,W] trong đó C - số channel sẽ chính là depth của features output từ backbone cnn, và spatial
> size H, W sẽ chính là quy định bởi roi_out_h và roi_out_w.
>
> *Một điểm nên nhớ trong bài giảng có nói , hai layer này chính là kiến trúc của phần đuôi của mô hình ResNet. (Khúc đầu làm
> backbone)
>
> Để hiểu điều này ta sẽ ôn lại một chút về lí thuyết: Trong Faster RCNN, Images tensor sẽ được pass qua backbone CNN để extract
> features. RegionProposalNetwork sẽ nhận features và dự đoán (đề xuất - propose) ra các " vùng có thể có object". Thế thì, ROI
> module sẽ giúp nôm na là  "trích xuất" features ứng với các proposed region này, đồng thời resize spatial size của chúng thành một
> kích thước định trước, (roi_out_h/w)
>
> Để rồi các roi output tensor này (có shape là (depth, roi_out_h, roi_out_w)) mới có chung size để rồi mới thông qua stage 2,
> classification layers sẽ dự đoán class cho từng proposed region.
>
> \~Như vậy, có thể chỗ này họ hơi sai sót một chút khi gợi ý rằng Linear layer thứ nhất có in_features là in_dim, mà đúng ra phải là:
>
> in_dim*roi_out_h*roi_dim_w, vì như đã nói output từ roi align modul có shape là (depth=in_dim, roi_out_h, roi_out_w).
>
> Điểm thứ hai có thể họ không nói nhưng mình phải tự hiểu đó là trước Linear layer phải có một Flatten layer, để flatten 3D tensor
> (in_dim, roi_out_h, roi_out_w)  thành vector (in_dim*roi_out_h*roi_out_w)
>
> Còn Linear layer thứ hai thì đương nhiên output dimensions sẽ là num_class để cho ra một vector các class scores.
>
> \~\/Lúc đầu, chưa để ý việc sẽ cần meanpool roi feature, còn khi đã meanpool để từ (B, in_dim,2,2) thành (B, in_dim), tức roi
> feature từ mỗi feature sẽ từ 3D  (in_dim, 2,2) trở thành vector (in_dim), thì đúng là Linear layer đầu tiên của  classification layers chỉ
> cần in_features = in_dim\/

> [!NOTE]
> Các bước của forward:
>
> 1. FEATURE EXTRACTING
>
> Đương nhiên là forward images qua RPN module, trong đó, nó sẽ tính toán  rpn loss, confidence scores, proposals, features,
> GT_class, và indices của positive anchors và negative anchors
>
> Vậy điểm chú ý ở đây đó là, đây là 'training' mode, nên như ta biết, khi forward qua RPN, thì bên trong function forward của nó, nó sẽ
> forward qua ProposalModule với positive/negative anchor indices, để rồi ProposalModule sẽ run ở train mode luôn và trả ra CHỈ
> NHỮNG KẾT QUẢ LIÊN QUAN TỚI POSITIVE, NEGATIVE  ANCHOR. Trong đó ví dụ như proposals sẽ có shape (M, 4): là SỐ
> POSITIVE ANCHOR TRONG BATCH.
>
> Và trong đó cũng có GT_class, vốn được tính toán bởi ReferenceOnActivatedAnchor function, có shape (M) mỗi giá trị chính là ground
> truth class id của cái gt box được gán với cái positive anchor tương ứng.
>
> 2.ROI ALIGN: 
>
> Tiếp theo, ta sẽ nhờ torchvision.ops.roi_align để từ các proposals và features nó sẽ chuyển thành tensor: (M, depth, roi_out_h,
> roi_out_w).
>
> *function này nó yêu cầu boxes argument là tensor (K,5) hoặc list các tensor (K,4) nên [\~ta tạo list trước khi pass vào: -> Sai]
>
> \~\/Nhờ Seloufian, đọc kĩ doc của function roi align, cho thấy trong trường hợp ta pass vào proposals là một single tensor thì phải có
> dạng [K,5] với cột đầu là index của sample trong batch - điều này có nghĩa  là phải cho torch biết, cái proposal thứ i (hàng thứ i của
> tensor [M,4]) LÀ THUỘC VỀ SAMPLE NÀO TRONG B SAMPLE. Vậy làm sao ta có cái này, thế thì để ý mình đã có positive anchor
> indices, là (M) vector mà giá trị là index của cái positive anchor trong tổng tất cả anchor trong batch = B*A*H'*W' = B*số anchor trong
> mỗi image. Vậy có nghĩa là các index này có range [0: B*số anchor trong mỗi image], nên nếu mình chia cho "số anchor trong mỗi
> image" thì mình sẽ đưa nó về range [0:B], và nó sẽ trở thành sample id của positive anchor (cũng là proposal) mà ta cần.
>
> Do đó mình mới chia pos_anchor_idx cho anc_per_img (chính là A*H'*W') Tiếp theo, chuyển nó thành shape (M,1) để rồi concat nó với
> proposals (M,4) theo dim = 1 để có boxes (M,5), pass vào as argument boxes.\/
>
> **các argument khác như output_size thì biết rồi, [\~còn spatial_scale sẽ là tỉ lệ giữa feature's spatial size / original image's spatial size
> -> SAI]\~
>
> \/Chỗ này nhờ Seloufian, đọc kĩ doc của arg spatial_scale mới thấy rằng chỉ khi ví dụ như mình dùng thuật toán Region Proposal trên
> original image để có proposals Sau đó project các proposals lên feature map, thì lúc này cần define spatial scale là (spatial size của
> feature map) / (spatial size của original image). Đây chính là  trường hợp của Fast RCNN.
>
> Tuy nhiên, với Faster RCNN, proposal regions được output bởi RPN, tính toán từ feature map, nên spatial scale sẽ là 1 là giá trị mặc
> định.\/
>
> 2B: ROL FEATURE MEAN-POOLING
>
> Sau khi tham khảo mới để ý việc họ nói ở mở đầu phần Faster RCNN về việc ta sẽ meanpool roi features, để chuyển roi aligned có 
> dạng (in_dim,2,2) thành vector (in_dim) bằng cách meanpool ở spatial dim: Hình dung đơn giản là với mỗi miếng 2x2 (có in_dim miếng) 
> ta sẽ tính trung bình. Thì từ 3D tensor sẽ thành 1D vector. Nhờ bước này, mà liên hệ đến việc Linear layer đầu tiên của classification
> layers sẽ có in_features = in_dim, và ko cần phải có nn.Flatten()
>
> 3.CLASSIFICATION
>
> Ta sẽ pass roi features qua classification layers, khi đó M nó sẽ treat như batch size - có nghĩa là, sẽ giống như việc ta pass một
> tensor  (B,C,H,W) vào classification layers thì mỗi 3D tensor (C,H, W) sẽ được flatten thành vector (C*H*W) và pass qua và các  Linear
> layer sau đó để cho ra một vector class scores. Và quá trình này sẽ xảy ra cùng lúc với B tensor. Sở dĩ nói lại chỗ này vì trong bài
> giảng có chi tiết rằng classification layers (tức stage 2) sẽ được apply cho từng proposed region
> - thì quả thực là như vậy nhưng không phải là một cách lần lượt, mà là đồng loạt như tính chất của vectorization mang lại.
>
> output sẽ có shape là (M, num_class) - mỗi một proposed region sẽ ứng với một vector có num_class = 20 class scores.
>
> 4. LOSS:
>
> Cuối cùng ta mới dùng đến GT_class - là vector (M): mỗi positive anchor / cũng là ứng với một proposed region là một giá trị ground
> truth class index. Pass hai tensor này vào nn.function.cross_entropy sẽ cho ra classification loss.
>
> 5.TOTAL LOSS: Cộng với rpn loss để có total loss.

> [!NOTE]
> Tham khảo solution của seloufian cho thấy những lỗi mình mắc phải:
>
> - Không để ý đến việc người ta nói về bước meanpool đối với output của
> roi, cái này sẽ liên quan đến số input features của Linear layer đầu tiên của
> classification layers.
>
> - Input cho argument boxes của ROI align trong trường hợp forward sẽ phải
> là một tensor có shape [K,5], với giá trị đầu tiên của mỗi hàng sẽ là index
> của sample trong batch.
>
> - Mình thấy Selufian không chỉ định spatial_scale đồng nghĩa dùng giá trị
> default = 1, đọc lại mới thấy vậy là đúng vì region propose output từ
> RPN-lấy input từ feature mập chứ không phải là nhờ dùng thuật toán
> Region Proposal trên image gốc rồi project lên feature map.

<br>

<a id="node-1656"></a>

<p align="center"><kbd><img src="assets/69c3e858652fa3b5f5c3839b09840e00cc45873e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4ae5d19365b4f4ba07d7deebedde2b80fce9c733.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/34636bb2254639e3a612abea48869dbb89977df2.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/727646e59e31cd8bdb75be4c9b4301baf859db7b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3eb0d73f22af037f20575bf7f1156b7a07450e86.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/69c3e858652fa3b5f5c3839b09840e00cc45873e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4ae5d19365b4f4ba07d7deebedde2b80fce9c733.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/34636bb2254639e3a612abea48869dbb89977df2.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/727646e59e31cd8bdb75be4c9b4301baf859db7b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3eb0d73f22af037f20575bf7f1156b7a07450e86.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/e591fa9a0350e6d5b5f9a3cc0f9f54095e911e1e.png" width="100%"></kbd></p>

> [!NOTE]
> Chỗ này họ mô tả ngắn gọn lại quá trình tính toán của Faster RCNN:
>
> Cũng như ở slice trước, chỉ nhắc lại thêm chi tiết rằng với mỗi một proposed
> region, thì RoI Align sẽ warp (hiểu nôm na là "cắt ra") một vùng tương ứng
> từ  feature tensor.
>
> Sau đó nó sẽ resize về kích cỡ như 2x2, và qúa trình này được thực hiện
> mean-pooling (hay average pooling). Để rồi classification layer sẽ tính ra
> class scores. CHÚ Ý CHỖ NÀY, có nghĩa là với output từ RoI Align là tensor
> shape (B, depth=in_dim, roi_h=2, roi_w=2), in_dim là depth output từ cnn,
> luôn giữ  nguyên sau đó.
>
> Ta sẽ average pooling để từ 3D tensor  (in_dim,2,2) trở thành một vector
> (in_dim). Do đó ta mới thấy mô tả cấu trúc của classification layer sẽ có FC
> layer đầu tiên có in_features = in_dim. Nếu không có vụ meanpool này thì
> tất nhiên để "gắn" được với FC, phải có bước flatten và FC layer phải có
> in_features = in_dim*2*2
>
> ====
>
> Thế thì, bản đầy đủ của Faster RCNN sẽ có thêm một Box Regression nữa,
> Y như box regression giúp predict ra transformation để convert anchor
> thành Gt box, thì đây lại tiếp tục predict ra một transformation để transform
> proposed box thành gt box, mang hiệu quả là "refine propose region" thêm
> nữa.
>
> Điểm thứ hai, đại khái là nó có thể predict một proposed box là background
> đồng nghĩa là output sẽ là num_class + 1 class score
>
> Muốn làm vậy thì mình sẽ phải tính proposals cho cả các negative anchor,
> rồi chuẩn bị target cho chúng. Có thể thử sau,

> [!NOTE]
> Với những cải thiện từ Seloufian, loss đã nhỏ hơn
> 4 như họ nói

> [!NOTE]
> Trước khi sửa, loss chỉ đạt ngấp nghé mức 4.

<br>

<a id="node-1657"></a>

<p align="center"><kbd><img src="assets/03c3ed406b1df3ec22863c50df75a8c768f9a348.png" width="100%"></kbd></p>

> [!NOTE]
> Phải đọc kĩ yêu cầu của nó

<br>

<a id="node-1658"></a>

<p align="center"><kbd><img src="assets/c5780b0d9901d0cacb91cd3ce6e0b80880f5829c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/636c9c00102983f7cf5d171ae741de81bd524d02.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d18b98ca6697d3fb3bef4fb1f3e68f30d71ef8a0.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/8b5ee5e106daf69d48e809eed2ccc4fe9da6f68f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f670eceecd77bfef304587c5229dca5bebb004e8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/c5780b0d9901d0cacb91cd3ce6e0b80880f5829c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/636c9c00102983f7cf5d171ae741de81bd524d02.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d18b98ca6697d3fb3bef4fb1f3e68f30d71ef8a0.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/8b5ee5e106daf69d48e809eed2ccc4fe9da6f68f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f670eceecd77bfef304587c5229dca5bebb004e8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/00e4c03652d4b13828dcc5a504b603685ed79f71.png" width="100%"></kbd></p>

> [!NOTE]
> 1. Pass images và các threshold vào RPB.inference(), chú ý là phải để mode = ' FasterRCNN' để
> nó trả ra features là cái features output từ backbone cnn.
>
> Lí do của cái vụ này là bởi vì....
>
> Vì là inference nên bên trong, khi qua ProposalModule's forward, nó sẽ trả  ra offsets và
> confidence scores của mọi anchors. Để rồi (trong RPN's forward) mới tính ra Proposals cho mọi
> anchor. Sau đó, qua quá trình làm với từng sample hai bước thresholding và nms. Kết quả cho ta
> các proposals và confidence list chứa proposal và confidence score của mỗi image (số lượng của
> mỗi image mỗi khác như đã biết).
>
> 2. Do đó bước tiếp theo ta cũng xét từng sample trong batch. Pass proposals của nó và features
> vào roi align để có roi feature (P_i,in_dim,2,2)
>
> Chỗ này cần chú ý (lúc đầu cũng làm sai) features pass vào đương nhiên "là của sample" i.
> Nhưng theo yêu cầu trong doc của roi align, **phải giữ batch dimension**, nên ta sẽ unsqueeze
> dim = 0 để feature_i có shape (1, in_dim, H', W')
>
> 2B: (Nhờ Seloufian) ta sẽ meanpool roi feature theo 2 dimension cuối, để  thành (P_i, in_dim)
>
> 3. Pass roi feature qua classification layers để có (P_i, num_class) - ứng với mỗi proposal là một
> vector predicted class scores.
>
> Dùng argmax dim=1 để có predicted class id.
>
> Append các tensor vào các list
>
> (Nhờ Seloufian) ta sẽ bổ sung thêm việc check xem image có proposals nào hay không để tránh
> lỗi trong lúc argmax. Cũng như là run qua classification với trạng thái no_grad.

> [!NOTE]
> Tham khảo solution của seloufian: 
>
> - Again, phải meanpool đối với output của roi
>
> - Feature đương nhiên là feature của sample tương ứng, nhưng 
> cần phải giữ 1st dimension = 1 (N=1, in_dim, H', W'
>
> - Again, spatial_scale phải bằng 1
>
> - Ngoài ra, bổ sung thêm việc inference qua classification với
> torch.no_grad() cũng như là check trường hợp không có proposed
> region nào

<br>

<a id="node-1659"></a>

<p align="center"><kbd><img src="assets/200e991848caa1a08c9b7dd3fc3592a5d5538067.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/bd0f722d4dd9626d17811dad6111ec4217946d19.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6d62b6be2cd2bad60d387321e57d9c8ac230a07c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0b2811e2bb1c0c642fab8feb74261c4c96a9251a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6d67b3a94a04a2d8a5ddccf81a281f3aab39737f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/272cba0e908f8d14fcedcab8bbc9536d433e04d0.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6f8883199dcdab9e4628dd88379c623a8c51ac6c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/98fee1af2b0cd7c4436662387b2a48c31ac5347d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f116ff6d479b00b1e08bc828016ba6a624bc60ca.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4e5625d21e7d5f38e96bdd0669526dff6d08a0b8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/200e991848caa1a08c9b7dd3fc3592a5d5538067.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/bd0f722d4dd9626d17811dad6111ec4217946d19.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6d62b6be2cd2bad60d387321e57d9c8ac230a07c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0b2811e2bb1c0c642fab8feb74261c4c96a9251a.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6d67b3a94a04a2d8a5ddccf81a281f3aab39737f.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/272cba0e908f8d14fcedcab8bbc9536d433e04d0.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/6f8883199dcdab9e4628dd88379c623a8c51ac6c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/98fee1af2b0cd7c4436662387b2a48c31ac5347d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f116ff6d479b00b1e08bc828016ba6a624bc60ca.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/4e5625d21e7d5f38e96bdd0669526dff6d08a0b8.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/23450de341d26a5064c9c3672c22b1889a63cdbf.png" width="100%"></kbd></p>

<br>

<a id="node-1660"></a>

<p align="center"><kbd><img src="assets/16fdcc5b208a1f7b15579a801c9bc4c3acadc912.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f3604367dc158899c8258069d5ec8c613e0e2b4c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/98f81e31eb47191680bbe6d9bd8b83f69a8dbfa9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/264d4dab055b6eb396df98e52d7092a78687511b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/16fdcc5b208a1f7b15579a801c9bc4c3acadc912.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f3604367dc158899c8258069d5ec8c613e0e2b4c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/98f81e31eb47191680bbe6d9bd8b83f69a8dbfa9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/264d4dab055b6eb396df98e52d7092a78687511b.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/017c6b5bd7fd1246a2cab6b0b7b7f5b4226b3e31.png" width="100%"></kbd></p>

> [!NOTE]
> Kết quả training sau khi fix lỗi:
>
> - Tính sai anc_per_img (AH'W' thay vì BAH'W'),
>
> - Dùng sigmoid (thay vì softmax),
>
> - Dropout2d (thay vì Dropout) ProposalModule
>
> -> Loss đã **nhỏ hơn 3** như họ yêu cầu
>
> Eval loss: 1.64
>
> mAP đã đạt 15.33%

> [!NOTE]
> Kết quả training sau khi fix lỗi:
>
> - 1st Linear input feature
>
> - Thêm bước roi features meanpool
>
> - Các lỗi của roi_aligned
>
> + roi align spatial_scale = 1
>
> + vụ [K,5]
>
> -> Loss vẫn chưa nhỏ hơn 3 
>
> Eval loss: 3.634
>
> - mAP vẫn  không được nổi 1%

<br>

<a id="node-1661"></a>

<p align="center"><kbd><img src="assets/0d0101288453d311a0cef8be60b01eb7037dd14e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0d0101288453d311a0cef8be60b01eb7037dd14e.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d2b026d787aeb6665b5fa0eceb5871b16dc2e68d.png" width="100%"></kbd></p>

<br>

<a id="node-1662"></a>

<p align="center"><kbd><img src="assets/9b0784eab4d251a5997aef1710359421e0e696d3.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b42931da5900a6ba4259859054996b13b4de46f1.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/696388f86d738c62f5bf8938b55f98d012ebaf8c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a9f352d0b148a7ccf8bb2b11172fbebaeb1b04f9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/9b0784eab4d251a5997aef1710359421e0e696d3.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b42931da5900a6ba4259859054996b13b4de46f1.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/696388f86d738c62f5bf8938b55f98d012ebaf8c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a9f352d0b148a7ccf8bb2b11172fbebaeb1b04f9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/af6112d6a27569e38ec1748b9897dbd816b7a6a1.png" width="100%"></kbd></p>

<br>

