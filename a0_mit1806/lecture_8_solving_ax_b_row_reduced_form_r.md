# Lecture 8: Solving Ax = B: Row Reduced Form R

📊 **Progress:** `38` Notes | `39` Screenshots

---
<a id="node-190"></a>

<p align="center"><kbd><img src="assets/51b43ea6ff446842b01e823216213ed1b136f6cf.png" width="100%"></kbd></p>

> [!NOTE]
> đây là lecture cuối mà ta sẽ finish việc giải một
> **linear equation system Ax = b**
>
> Để trả lời câu hỏi (như trong Ax=0 đã làm) là, nó **có
> solution không?** nếu có thì **nó là gì?**

<br>

<a id="node-191"></a>

<p align="center"><kbd><img src="assets/2d130e9d46cb7b464e4c681a3fc4dba647ed68a1.png" width="100%"></kbd></p>

> [!NOTE]
> đại khái gs nói, nhìn bên trái có thể thấy row 1 + row 2 =
> row 3
>
> Thế thì, ta có thể **đoán** được là,**muốn hệ phương
> trình có nghiệm** thì các giá trị của b **phải sao cho b1 +
> b2 phải bằng b3**. Tí nữa mình **sẽ** **xem elimination
> cho thấy điều đó**.
>
> Còn bây giờ, có thể hiểu được điều này là vì, **vì hàng 3
> không độc lập** nên như đã thấy ở những bài trước,**quá
> trình elimination sẽ biến nó thành [0 0 0].**
>
> Và với Ax=b thì ở **vế bên phải cũng áp dụng các bước
> của quá trình elimination** như bên trái, nên **nếu b3
> không bằng b1 + b2** thì sau khi elimination ở equation
> thứ 3, **bên trái bằng 0 nhưng bên phải khác 0** ->
> phương trình vô nghiệm

<br>

<a id="node-192"></a>

<p align="center"><kbd><img src="assets/8e86c31961a958b8356761093ee4e8deeee23750.png" width="100%"></kbd></p>

> [!NOTE]
> Ta sẽ thực hiện quá trình elimination, và các bước này sẽ
> apply cho cả bên phải và trái. Do đó, ta sẽ **ghép cột b
> thành một cột của A** để có cái gọi là **Augmented matrix**[A b] và ta sẽ làm (elimination) trên nó.

<br>

<a id="node-193"></a>

<p align="center"><kbd><img src="assets/55da281b370757a808f0aa4f091d6f2594a0c264.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi, bắt đầu quá trình elimination: Đầu tiên ta đã có pivot
> đầu tiên ok rồi, nên ta sẽ khử A21, A31 - những vị trí dưới
> pivot (quá trình elimination là tạo ra dạng Row Echelon=
> dạng bậc thang, trong đó bên dưới pivot = 0)
>
> -Khử A22: Trừ hàng 2 cho 2*hàng 1 -> [0 0 2 4 b2-2b1]
> -Khử A32: Trừ hàng 3 cho 3*hàng 1 -> [0 0 2 4 b3-3b1]

<br>

<a id="node-194"></a>

<p align="center"><kbd><img src="assets/3aad05231eab338e11c931d5a662a6e16d7c27d3.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3aad05231eab338e11c931d5a662a6e16d7c27d3.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/2b50af26aa23a9ebc6183650c0e341b05f21e6f3.png" width="100%"></kbd></p>

> [!NOTE]
> vậy ta có **col 2 không có pivot**, nó là **free col**, col 3 có
> pivot là 2, nên nó là pivot column. Nếu có quên thì **pivot**
> là tuân theo rule sau:
>
> - Pivot (đương nhiên phải khác 0) của hàng dưới**luôn
> nằm  bên phải hàng trên.**
>
> - **Bên dưới pivot = 0**.
>
> - Ở dạng **Reduce** Row Echelon thì có thêm yêu cầu
> **chuyển  pivot = 1**, và**khử luôn các giá trị bên trên
> pivot** để trong pivot col **chỉ có pivot là khác 0**.
>
> Rồi, ta tiếp tục bước nữa, hủy A33 để finished col 3.
>
> Có thể thấy sau bước này, **row 4 đã bị set thành 0 hết.**

<br>

<a id="node-195"></a>

<p align="center"><kbd><img src="assets/cb6112e453768b735cf39de1d4a07df7d933ce29.png" width="100%"></kbd></p>

> [!NOTE]
> đến đây ta **xác nhận lại được nhận định ban đầu** về điều
> kiện của b n**ếu muốn equation system có solution:** đó là
> **b3 phải bằng b1 + b2**

<br>

<a id="node-196"></a>

<p align="center"><kbd><img src="assets/7f63fc4d30c78dda13b46d335d4fd5192880df09.png" width="100%"></kbd></p>

> [!NOTE]
> Với nhận định này, **gs giả sử b là [1, 5, 6]**, (thế vào)
> để thấy **quá trình elimination** sẽ **biến phần bên phải
> thành [1 3 0]**

<br>

<a id="node-197"></a>

<p align="center"><kbd><img src="assets/e75b2b5a4685debc5bbf3ef252956a2c110791fb.png" width="100%"></kbd></p>

> [!NOTE]
> Từ đó ta **có thể kết luận rằng**: **nếu có một linear
> combination giữa các row của A tạo ra kết qủa bằng
> 0-row** ... thì system equation chỉ khi có solution khi **cùng
> một linear combination đó của các component của b
> phải cho ra 0**
>
> Theo đó ta đã trả lời được câu hỏi đầu tiên - EquaSys
> có solution không?

<br>

<a id="node-198"></a>

<p align="center"><kbd><img src="assets/4711030bc04388bebba6be2d1bc8dede3f2eaf52.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì tiếp theo ta sẽ **tìm một quy trình để giải ra
> solution.** Đầu tiên gs nói trước rằng, ta có **4 variable**
> với **chỉ có 2 pivot** như vậy đồng nghĩa là **sẽ có vô số
> solution**.
>
> Vậy đầu tiên ta sẽ**tìm cách tìm một "particular"
> solution** bằng cách **cho các free variable bằng giá trị
> nào đó**, rồi**từ đó tìm pivot variable**. Vậy thì đơn giản
> nhất là **cho free variable = 0**. Hệ phương trình trở
> thành như vầy

<br>

<a id="node-199"></a>

<p align="center"><kbd><img src="assets/820374efcbc68d4d7d63a71dcb05fb37642ea680.png" width="100%"></kbd></p>

> [!NOTE]
> **backsubstitution các free variable x2, x4 vào** giải ra x1,
> x3 và ta có **x_particular** (particular solution)
>
> Tuy nhiên, cái ta cần là**tìm ra mọi solution.**

<br>

<a id="node-200"></a>

<p align="center"><kbd><img src="assets/e307ec4713c20f8076999e41577c2f10e33be80b.png" width="100%"></kbd></p>

🔗 **Related:** [LECTURE 13: QUIZ REVIEW](untitled.md#node-378)

> [!NOTE]
> Để có toàn bộ solution (complete solution), gs đề nghị ta tìm
> **nullspace - như đã biết ở bài trước là tập hợp các vector x thỏa
> Ax = 0.**
>
> Khi đó, bằng cách **kết hợp x_particular với bất kì vector x_null
> nào thuộc nullspace**, ta **đều có thêm một solution**.
>
> Hay nói cách khác **x_particular + nullspace** sẽ là **tập hợp
> toàn bộ solution của Ax=b**

<br>

<a id="node-201"></a>

<p align="center"><kbd><img src="assets/55d8d2e94c1c5847483afea09f6cb5d32a88362d.png" width="100%"></kbd></p>

> [!NOTE]
> Tại sao lại như vậy, tại sao một x trong nullspace cộng với
> x_particular cũng sẽ là một solution của Ax=b Để rồi dẫn
> đến nếu ta lấy mọi vector trong nullspace cộng với một
> x_particular thì ta sẽ được toàn bộ  solution của Ax = b?
>
> Thế thì gọi x_p là x_particular, ta có Ax_p = b
>
> và gọi x_null là vector trong nullspace của A, tức là ta có 
> Ax_null = 0
>
> Vậy cộng hai vế của hai equation lại ta có:
>
> Ax_p + Ax_null = b + 0 <=>
>
> A(x_p + x_null) = b 
>
> Và điều này có nghĩa là (x_p + x_null) cũng là solution của
> Ax = b

<br>

<a id="node-202"></a>

<p align="center"><kbd><img src="assets/49e36bfbf8865e8b2f5de365940550ceb8be2cba.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/49e36bfbf8865e8b2f5de365940550ceb8be2cba.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/279df0fd5d31dc11faff934b797347dc7007b402.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì để tìm nullspace thì ta đã biết ở bài trước, nó **chính
> là mọi linear combination của các special solutions.**
>
> Special solutions là cái mà ta có khi cho free variable các 
> giá trị 1,0, và 0,1. Nên**đầu tiên ta sẽ tìm special solution**

<br>

<a id="node-203"></a>

<p align="center"><kbd><img src="assets/a5f35bcfa31a3249d0a873d59ac5bc7151d2b737.png" width="100%"></kbd></p>

> [!NOTE]
> và như vậy ta có **complete solution**

<br>

<a id="node-204"></a>

<p align="center"><kbd><img src="assets/9aaab4f211e962c4b6d57743a150e17d969bc125.png" width="100%"></kbd></p>

> [!NOTE]
> Thầy hỏi là có thể nhân một constant vào x_particular
> không (tương tự như c với d của các special solution)?
>
> Me: Không, vì **tuy Ax=b thì A*constant *x chưa chắc
> bằng b**, nên **scale của x không phải là solution mới của
> Ax=b**

<br>

<a id="node-205"></a>

<p align="center"><kbd><img src="assets/8133ed191a477f914451bda6108bd3a5c4725b0b.png" width="100%"></kbd></p>

> [!NOTE]
> Đúng rồi, vì x_particular là solution của Ax = b, scale
> xp thì nó không còn là solution. **Nhưng scale x_null
> thì nó vẫn là solution của Ax = 0**, tức nó vẫn là thuộc
> nullspace

<br>

<a id="node-206"></a>

<p align="center"><kbd><img src="assets/09e5c4d831f5519192680cb1eb8dacbefe2650e0.png" width="100%"></kbd></p>

> [!NOTE]
> tiếp gs nói chúng ta hãy **plot mọi solution** ra xem nó là cái
> gì, **nó có phải là một subspace không?**
>
> Thì đầu tiên là ta đang trong R4 (vì có 4 variable x1,x2,x3,
> x4)

<br>

<a id="node-207"></a>

<p align="center"><kbd><img src="assets/0da7ad631fe9c9a40ee434b1dfa9ad103dca39d0.png" width="100%"></kbd></p>

> [!NOTE]
> Ok, thế thì như đã thấy tập hợp solution (**complete
> solution**) bao gồm **mọi vector trong nullspace** cộng với
> vector **x_particular.**
>
> Mà **mọi vector trong null-space** là mọi linear combination
> của hai vector special solution - thì nó **tạo thành một 2D
> plane trong không gian 4D**.
>
> Thành ra tập hợp mọi nghiệm sẽ là: vector (tức điểm) x_p
> + một vector bất kì của cái 2D plane của nullspace, thì sẽ
> thành ra là một **CÁI 2D PLANE CÓ ĐI QUA X_P:**Nói rõ
> hơn là, nullspace (mọi linear combination của special solution)
> là một 2D plane (đương nhiên có đi qua O) và x_p là một điểm
> nằm đâu đó (ngoài nullspace). Thế thì khi lấy mọi vector trong 
> nullspace plane + x_p ta sẽ được một plane khác, có đi qua 
> x_p nhưng không đi qua 0.
>
> V**à cái 2D plane này không phải là subspace**, vì nó
> **không đi qua gốc O**, mà như đã biết subspace thì phải đi
> qua gốc O

<br>

<a id="node-208"></a>

<p align="center"><kbd><img src="assets/523f94fb0f117ea32fa6f4cd2c4afd10a4e1d2e7.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi, thế là ta đã có algorithm để **tìm mọi solution của
> Ax=b:** **Tìm particular solution**, rồi **tìm nullspace** bằng
> cách tìm **special solution** của để rồi tạo nên **complete** 
> solution:
>
> **x = x_particular + nullspace** (=linear combination của
> special solution)
>
> Tiếp gs đề nghị ta nghĩ rộng hơn, với matrix m,n có rank
> r, với định nghĩa hiện tại của rank là số pivot. thì gs đặt câu
> hỏi là **m, n quan hệ với rank r như thế nào?**

<br>

<a id="node-209"></a>

<p align="center"><kbd><img src="assets/bbc4d92a07811deda5131998636f7db5c1bb78b4.png" width="100%"></kbd></p>

> [!NOTE]
> nhớ lại rằng **nếu mọi chuyện đều tốt** thì ta sẽ có **mỗi hàng
> một pivot**, vậy **số pivot không thể lớn hơn số hàng**.
>
> Tương tự, **mỗi cột cùng lắm có một pivot** nên **số pivot cũng
> không thể lớn hơn số cột**.
>
> Vậy**r <= m**, và **r <= n**
>
> Vậy ở đây có thể thấy với một matrix m,n thì rank của nó
> có g**iá trị tối đa là cái nhỏ hơn trong hai cái m, n**Ví dụ matrix cao ốm 3x2 thì rank chỉ có thể bằng 2 trở xuống
> vì với 2 cột thì tối đa chỉ có 2 pivot

<br>

<a id="node-210"></a>

<p align="center"><kbd><img src="assets/bff2c8400b06bedf02290eb0546c8075821309a0.png" width="100%"></kbd></p>

> [!NOTE]
> Thầy nói giờ ta sẽ quan tâm đến**FULL RANK**, thế thì
> rõ ràng, **rank có maximum là thằng nhỏ nhất trong  m và
> n**. Ví dụ nếu 3 hàng 2 cột thì rank sẽ maximum là bằng
> 2.
>
> Vậy thầy đặt câu hỏi là **giả sử r = n** (tức rank = số cột)
> thì ta **có thể kết luận gì với Nullspace?**
>
> => Thử trả lời: r = n tức bằng số cột, có nghĩa là ta có
> trạng thái **mọi column đều là pivot column**, hay, ta có
> **n pivot** và **ko có free variable nào.**

<br>

<a id="node-211"></a>

<p align="center"><kbd><img src="assets/88b4019d35829716c4445d5b561d4e23ac193b98.png" width="100%"></kbd></p>

🔗 **Related:** [LECTURE 7: SOLVING AX = 0: PIVOT VARIABLES, SPECIAL SOLUTIONS](untitled.md#node-166)

> [!NOTE]
> và vì **không có free variable nào**, mà ta đã được biết khi 
> tìm nullspace, ta sẽ xác định free column và pivot column
> để rồi với free variable, ta mới chọn giá trị tùy ý cho nó
> và thế vào lại (back-substitution) tính ra pivot variable, để
> thành ra special solution. 
>
> Và **SỐ SPECIAL SOLUTION CHÍNH LÀ SỐ FREE COLUMN** 
> (Theo đường dẫn), vậy suy ra trong trường hợp này ta**ko
> có special solution nào**, đương nhiên cũng không có linear
> combination nào của special solution. Dẫn đến **nullspace chỉ
> tồn tại vector 0**
>
> (Nó**ít nhất cũng có vector 0** vì**nullspace là subspace**, là một
> vector space, nên nó **phải ít nhất cũng chứa origin = vector 0**)

<br>

<a id="node-212"></a>

<p align="center"><kbd><img src="assets/4ab3dca3ff71293dc8b049cf69f008703c847bd1.png" width="100%"></kbd></p>

> [!NOTE]
> Và hệ quả là đối với Ax = b, như đã biết, complete solution
> là bao gồm x_particular solution + nullspace, mà nullspace
> = 0 rồi, thành ra **complete solution của Ax=b chỉ còn là
> x_particular nếu có**. Còn nếu x_particular không có luôn thì
> Ax=b vô nghiệm
>
> Vậy Ax=b có thể VÔ NGHIỆM nếu x_particular không tồn tại
> hoặc CÓ MỘT NGHIỆM là x_particular nếu nó tồn tại.

<br>

<a id="node-213"></a>

<p align="center"><kbd><img src="assets/ea1c444ccbea2db7022c4a6d9630502db29a26a1.png" width="100%"></kbd></p>

> [!NOTE]
> Gs lấy ví dụ của một **full column rank.** matrix A này có
> 2 independent columns, (hai vector này sẽ chỉa ra hai
> hướng khác nhau), rank của nó sẽ = số Independence
> columns = 2.
>
> Và thầy nói khi ta dùng elimination đưa nó về Reduced
> Row****Echelon Form thì nó sẽ có dạng như vầy: hai hàng
> đầu tạo một Identity matrix, hai hàng dưới sẽ tạo Free
> matrix chỉ toàn số 0

<br>

<a id="node-214"></a>

<p align="center"><kbd><img src="assets/fd68432ed939346733832bc1b2d8c12076d3358a.png" width="100%"></kbd></p>

> [!NOTE]
> Rồi như vậy đây là ví dụ của một full column rank ta sẽ có
> nullspace = 0:
>
> Thật vậy, ta có hai linear independent columns, nên không có
> cách nào ngoại trừ hai coefficient đều bằng 0 để tạo linear
> combination của hai vector column thành 0.
>
> Còn nếu xét Ax=b, thì có phải là nó sẽ luôn có solution
> không?
>
> Không, như đã nói nó sẽ nhiều nhất là chỉ có một solution,
> nếu x_particular tồn tại, đó là khi b là một linear combination
> của columns. Ví dụ b là 1*[col 1] + 1*[col 2] thì Ax=b sẽ chỉ
> có một solution là [1 1].

> [!NOTE]
> Full Column Rank: Ax=b chỉ có 1 solution nếu b là linear
> combination của A's columns

<br>

<a id="node-215"></a>

<p align="center"><kbd><img src="assets/6300a79769a196bd8fbd277f93a2897c57b269d6.png" width="100%"></kbd></p>

> [!NOTE]
> Qua trường hợp **Full Row Rank** tức **r = m**. Có nghĩa **mỗi row
> đều có một pivot**. Thầy hỏi là xét điều kiện có nghiệm của
> Ax = b sẽ như thế nào?
>
> -> Mỗi hàng đều có một pivot, nên quá trình elimination sẽ
> **không biến hàng nào thành 0 hết**. Nhớ lại câu chuyện hồi
> nãy, nếu elimination biến một hàng thành 0, thì muốn  Ax=b
> có solution thì phải yêu cầu là cũng các bước elimination đó
> biến phần tử tương ứng của vector b thành 0. (Nếu không
> thỏa điều kiện này đương nhiên ta sẽ có một equation của
> Ux=0 có dạng {0 ..0} = {khác 0} -> không thể solve được ->
> equation system vô nghiệm)
>
> Mà **nguyên nhân gốc rễ** **một hàng bị eliminate thành 0** là do
> **nó bị phụ thuộc tuyến tính** với các hàng khác, thành ra
> muốn thỏa điều kiện trên thì phần tử tương ứng với hàng bị
> set thành 0 cũng phải phụ thuộc tuyến tính với các phần tử
> khác.
>
> Vậy quay lại đây, nếu elimination không tạo ra hàng 0 nào
> thì đồng nghĩa cũng k**hông có yêu cầu nào với b** => Luôn
> có solution với mọi b

> [!NOTE]
> Full Row Rank: Ax=b luôn có solutions với mọi b

<br>

<a id="node-216"></a>

<p align="center"><kbd><img src="assets/45a3ce8f0ee2a1f1257b8e46563d157cc51db7e9.png" width="100%"></kbd></p>

> [!NOTE]
> Thầy: Có bao nhiêu free variable?
>
> -> Mọi hàng đều có pivot, mà ở đây đương nhiên m <= n,
> nên số pivot = m, số free variable sẽ là n - r = n - m

<br>

<a id="node-217"></a>

<p align="center"><kbd><img src="assets/88d54fdbe84558f89e9bc1a066d31cae342d8ee8.png" width="100%"></kbd></p>

> [!NOTE]
> Đúng vậy, ta có n-r = n-m free variable (vì đang xét Full
> Row Rank r = m)
>
> Và ta hiểu rằng như vậy thì sẽ tồn tại special solution (tìm
> bằng cách cho free variable các giá trị 1, 0 và gắn vào tìm
> pivot variable). Thì chúng cũng tạo nên basis của nullspace
> hay có thể kết luận nullspace có dim lớn hơn 0, hay, tồn tại
> non zero vector trong nullspace.
>
> Vậy khi xét complete solution của Ax=b thì như ta biết sẽ là
> x_complete = x_particular (vốn đã kết luận luôn tồn tại với
> mọi b khi A full row rank) + x_null. Và x_null thì có vô số
> (mọi linear combination của special solution / cũng là basis
> tạo nên một line). Do đó nếu A Full Row Rank thì Ax=b có
> vô số solution

> [!NOTE]
> Do đó nếu A Full Row Rank thì
> Ax=b có vô số solution

<br>

<a id="node-218"></a>

<p align="center"><kbd><img src="assets/e71f196e57c70c6c0e413d29c3f4d47f0989d541.png" width="100%"></kbd></p>

> [!NOTE]
> Thầy lấy ví dụ của một full row rank, dùng luôn
> transpose của matrix full column rank hồi nãy. Gs hỏi:
> rank bằng mấy? Và col nào là pivot?
>
> -> Thử trả lời: Rank bằng 2, vì thầy đang ví dụ của
> full row rank, mà matrix này chỉ có 2 row, nên nhiều
> nhất là rank chỉ có thể bằng 2 thôi (again, vì sao - vì
> mỗi row chỉ có thể có một pivot, nên 2 row chỉ có thể
> có 2 pivot là maximum rồi)
>
> Cột 1 và 2 là pivot: Có thể nhẩm: cột một có A11 khác
> không thì đương nhiên là một pivot rồi.
> Nếu làm elimination, thì trừ hàng 2 cho 3*hàng 1 để
> khử A21, khi đó A22 sẽ thành (1-3*2) = -5, là giá trị
> khác không nên đây sẽ là pivot thứ 2. Vậy cột 1 và 2
> là hai pivot.

<br>

<a id="node-219"></a>

<p align="center"><kbd><img src="assets/ecafa0b572351d4e0cf627b4d54243e50f60df9a.png" width="100%"></kbd></p>

> [!NOTE]
> Gs: Đúng vâỵ, nếu ta elimination và đưa nó về RREF thì 
> Ta sẽ thấy nó có dạng mà như thầy nói lúc trước - dạng 
> điển hình [I F]. Phần đầu (pivot cols) tạo thành một Identity
> matrix và phần sau các (free cols) tạo thành Free matrix

<br>

<a id="node-220"></a>

<p align="center"><kbd><img src="assets/26238dad279d360957be3e1385a038e586e75bc7.png" width="100%"></kbd></p>

🔗 **Related:** [LECTURE 9: INDEPENDECE, BASIS, AND DIMENSION](untitled.md#node-245)

> [!NOTE]
> Và case cuối cùng là r=m=n. Gs gọi nó là **FULL RANK.**
> Nó sẽ là square matrix (dĩ nhiên) và gs nói nó sẽ **INVERTIBLE**.
>
> R sẽ là gì?
>
> Me: Identity matrix, vậy A sau khi elimination sẽ thành I. Và vì 
> mình biết elimination apply với A chính là nhân A với matrix E
> thể hiện các bước elimination. Vậy EA = I. Điều này chứng tỏ
> E chính là A_inv, đồng nghĩa A là **INVERTIBLE** MATRIX

<br>

<a id="node-221"></a>

<p align="center"><kbd><img src="assets/8bdc5af1b6d44486036c9a238a7da92e05ae9fb9.png" width="100%"></kbd></p>

> [!NOTE]
> Gs: NullSpace của A là gì?
>
> Me: Cũng giống như trường hợp Full Cols Rank, **các cols
> đều linear independent**, nên **linear combination duy
> nhất của các cols vector trở thành 0** **chỉ có thể khi các
> coeff = 0**.
>
> Vậy Ax=0 chỉ có một solution duy nhất đó là [0 0].T, cho
> nên **nullspace của A chỉ chứa zero vector**
>
> GS: Correct.

<br>

<a id="node-222"></a>

<p align="center"><kbd><img src="assets/14cc4c69328706eb0e7c99fb790af207285562d4.png" width="100%"></kbd></p>

> [!NOTE]
> Gs: Điều kiện nào để solve Ax=b?
>
> Me: Tương tự, vì A là matrix Full Rank, mọi row của nó đều
> linear independent, nên q**uá trình elimination không tạo 
> thành zero row nào**. 
>
> Do đó, **b cũng không cần phải có điều kiện gì**, hệ phương
> trình luôn có nghiệm với mọi b. Và nó **luôn chỉ có 1 solution
> duy nhất với mọi b.**Hoặc lập luận kiểu khác là vì mọi columns đều independent,
> và chúnng là các vector trong Rm (m=n=r). Nên ta có đủ n (=m)
> vector độc lập trong R^m. Do đó **CHÚNG SPAN TOÀN BỘ
> Rm** (cũng là Rn). Nên b (là vector trong Rm) dù có ở đâu (có giá
> trị bao nhiêu) thì **CŨNG LUÔN NẰM TRONG COLUMN SPACE 
> NÊN Ax=b LUÔN CÓ SOLUTION**. 
>
> Còn vì Nullspace chỉ chứa zero, nên không có trường hợp vô số
> nghiệm.

<br>

<a id="node-223"></a>

<p align="center"><kbd><img src="assets/5ce1f4556ccc857ab210f9bfc442af56869c97a4.png" width="100%"></kbd></p>

> [!NOTE]
> Tóm lại:
>
> r=m=n: **FULL RANK**, R = I, và ta sẽ có **chính xác 1 solution với mọi b**.
>
> r=n<m: **FULL COLUMNS RANK**, matrix gầy, cao. R = [I O].T (thông cảm, note
> không ghi được thành cột nên đành ghi là [I O].T nhé)
>
> Vì elimination tạo các zero row ở dưới (cái chữ O ở trong R =[I O].T đó)
> nên **b phải có điều kiện nào đó** đã nói hồi nãy **thì hệ mới có nghiệm**. Vậy
> case này có **0 solution hoặc 1 solution** (nếu tồn tại x_particular). Không có
> dependent columns nên **không có free columns** / special solution / non-zero 
> vector  trong nullspace nên nếu có x_particular thì nó cũng là nghiệm duy nhất 
> chứ không có vụ kết hợp với x_null để ra vô số nghiệm.
>
> r=m<n: **FULL ROWS RANK**, matrix mập lùn, R =[I F] (khúc này gs nói thật
> ra không phải lúc nào các pivot cols cũng xếp ở trước các free cols, nên
> ghi R =[I F] không hẳn là đúng, mà I và F có thể đan xen nhau.
>
> Và vì r=m<n, nên**luôn có các free variable** (số pivot = r, số free variable
> sẽ là n-r, mà r < n nên r-n lớn hơn 0). Dẫn đến có thể chọn tùy ý
> free variable để thế vào tính ra pivot var. Nên có non-zero vector trong 
> nullspace cũng đồng nghĩa có vô số x_null (nên nhớ dù chỉ có một vector
> trong basis của nullspace thì có có vô số combination của nó để có các
> x_null, tạo thành nullspace là một line) 
>
> Còn xét Ax=b thì vì mọi row đều độc lập nên eliminate không cho ra row nào
> bằng 0 dẫn đến b có như thế nào thì vẫn luôn solve được. Nên luôn có solution.
> Hay giải thích cách khác là vì full row rank nên các column độc lập (có m=r cái)
> sẽ span toàn bộ Rm (m hàng, nên column là vector trong Rm). Dẫn đến b (cũng
> là Rm vector) ở đâu thì cũng luôn nằm trong C(A)
>
> Cho nên ở trường hợp này có **VÔ SỐ SOLUTION**
>
> Cuối cùng là r<m, r<n: Không full rank, R sẽ có dạng trong hình [[I F], [0 0]]
> nên có thể VÔ NGHIỆM (nếu b không tạo thành các hàng bằng 0 tương
> ứng với với các hàng bằng 0 của R khi apply elimination) còn nếu b thỏa
> điều kiện này thì ta có VÔ SỐ NGHIỆM do có thể chọn tùy ý các free var
> để thế vào tính pivot var.

<br>

<a id="node-224"></a>

<p align="center"><kbd><img src="assets/05ac96d6e28c13fd6eaa98c6dbe38fdf2de8672b.png" width="100%"></kbd></p>

> [!NOTE]
> Gs: Cái bảng này summarize bài học, và câu này
> summarize: Rank của matrix sẽ cho ta biết mọi thứ về
> solution

<br>

