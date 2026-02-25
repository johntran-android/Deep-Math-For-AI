# Lecture 2: Elimination With Matrices

📊 **Progress:** `30` Notes | `31` Screenshots

---
<a id="node-24"></a>

<p align="center"><kbd><img src="assets/3009ba8981503a3b5b98cdedc0935dc3998989b8.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là bài này ta sẽ giải system of equation
> này với **phương pháp elimination.**

<br>

<a id="node-25"></a>

<p align="center"><kbd><img src="assets/9b2b4970680fc4f5d80f27ffe59a2233bd942d99.png" width="100%"></kbd></p>

> [!NOTE]
> Đầu tiên ta nhận định**s**ố 1 (coefficient của
> x ở equation thứ 1: a11) gs gọi nó là **pivot đầu tiên**

<br>

<a id="node-26"></a>

<p align="center"><kbd><img src="assets/282e6d80b22d3111fe173bf240ef03a04326a892.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp thep ta sẽ muốn loại bỏ a21 của equation 2, ta**trừ equation 2 cho equation 1 nhân cho 3 (hệ số của
> hàng 2 cột 3)**. Gọi đây là **bước (2,3)**

<br>

<a id="node-27"></a>

<p align="center"><kbd><img src="assets/9b6a97f25274ec869330377258b4ccfd34c108e8.png" width="100%"></kbd></p>

> [!NOTE]
> Gs nói tạm thời đừng
> quan tâm vế bên phải

<br>

<a id="node-28"></a>

<p align="center"><kbd><img src="assets/3325aa644b71737f7049adbc317bcc46f0eb8108.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp theo là **bước (3,1)** (ý là **hủy đi hệ số tại vị trí hàng
> 3, cột 1**. Nhưng vì **nó (a31) đã = 0 sẵn rồi.**
>
> Ta sẽ làm **bước (3,2): hủy a32 đang bằng 4** bằng cách
> trừ hàng 3 cho 2*hàng 2

<br>

<a id="node-29"></a>

<p align="center"><kbd><img src="assets/dce006a80d1bc6b227fe78ab3c168281d88f8df8.png" width="100%"></kbd></p>

🔗 **Related:** [LECTURE 18: PROPERTIES OF DETERMINANTS](untitled.md#node-590)

> [!NOTE]
> Gs cho biết **pivot phải khác 0**. Và ở đây **ta có một case
> rất tốt khi cả 3 pivot đều khác 0**.
>
> Và ở trường hợp này, để tính **determinant** chỉ việc
> **nhân các pivot lại với nhau,** ra bằng 10 
>
> (me: qua bài về determinant ta sẽ có chứng minh tại sao
> det của triangular matrix là tích các pivot)

<br>

<a id="node-30"></a>

<p align="center"><kbd><img src="assets/3c47a2eabe7fb6fc8bcd7a584784cbc0346f979b.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là gs nói về **case failure**. Thì có **temporary
> fail** khi ví dụ **như number tại 1,1 hoặc 2,2 bằng 0**. Thì
> **ta luôn có thể exchange/switch row để "thoát ra"**.
>
> Ví dụ 1,1 bằng 0 mà 2,1 hoặc 3,1 khác 0 thì ta **chỉ việc
> đổi vị trí các equation**. Rồi lại làm tiếp.
>
> Nhưng **nếu làm tới hàng 2 mà 2,2 và 3,2 đều bằng 0**
> hoặc**tới hàng 3 mà 3,3 = 0** thì sẽ **ko còn row nào mà
> đổi nữa**.
>
> **Khi đó sẽ là failure**, ta sẽ có **non-inversible matrix**

<br>

<a id="node-31"></a>

<p align="center"><kbd><img src="assets/6dc53bc5466bd986bda4e1908ee14f2947f9d568.png" width="100%"></kbd></p>

> [!NOTE]
> Kế tiếp ta sẽ **làm lại những bước biến đổi (nãy giờ ở
> vế trái) đối với vế phải để thành vector c**

<br>

<a id="node-32"></a>

<p align="center"><kbd><img src="assets/5d9c2fb704e17688dee339209adb203c251cd026.png" width="100%"></kbd></p>

> [!NOTE]
> Và đến đây, chỉ việc **viết lại equation system** gọi nó là **Ux=c**. 
>
> **Back substitution**: tính z, thay vào 2 tính y, thay vào 1 tính x

<br>

<a id="node-33"></a>

<p align="center"><kbd><img src="assets/c0dfd1895131af53fff7123310557290b22e46f2.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp theo gs nhắc lại việc **nhân matrix cho vector**,
> như bài trước đã học ở **góc nhìn theo column** thì nó
> là**linear combination của các column** bởi các **coeff là
> các giá trị của vector**

<br>

<a id="node-34"></a>

<p align="center"><kbd><img src="assets/0eb14be0b333bde75eb3f71ca75bd095c7449f9c.png" width="100%"></kbd></p>

🔗 **Related:** [LECTURE 7: SOLVING AX = 0: PIVOT VARIABLES, SPECIAL SOLUTIONS](untitled.md#node-183)

> [!NOTE]
> **matrix** A @ **col x** là **linear combination** của các
> matrix column, với **coeff là components của x** nên sẽ
> **được column**
>
> **row x @ matrix A** thì sẽ là **linear combination của các
> row của matrix A**với**coeff là components của x**, nên
> sẽ **được row.**

<br>

<a id="node-35"></a>

<p align="center"><kbd><img src="assets/08bb66915e259135d6ac3ce6e10621628a47d4dd.png" width="100%"></kbd></p>

> [!NOTE]
> Câu hỏi là **nhân matrix gì cho matrix A** **để tương đương
> với bước thứ nhất trong quá trình eliminating** hồi
> nãy: **trừ hàng 2 cho 3*hàng 1**

<br>

<a id="node-36"></a>

<p align="center"><kbd><img src="assets/07a80ad625181935a467b53c72026e8831b200cf.png" width="100%"></kbd></p>

> [!NOTE]
> Để trả lời ta sẽ đơn giản hiểu rằng **hàng thứ 1 của matrix
> cần tìm sẽ nhân với matrix A** để **ra hàng thứ 1 của
> matrix kết quả**.
>
> Vậy, vì như đã nói **row (row vector) nhân matrix** thì sẽ
> là**linear combination các matrix's row** nên **để hàng 1
> của matrix kết quả  bằng hàng 1 của A** thì**ta sẽ cần:
>
> 1** * row 1 của A + **0** * row 2 của A + **0** * row 3 của A
>
> Vậy **row 1 của**matrix cần tìm là **[1 0 0]**

<br>

<a id="node-37"></a>

<p align="center"><kbd><img src="assets/a0696b21203cf7f1520f85d9aae022fe7ffbf88e.png" width="100%"></kbd></p>

> [!NOTE]
> Tương tự, hàng 3 của matrix cần tìm sẽ nhân A để vẫn
> ra kết qủa vẫn bằng hàng 3 của A nên **hàng 3 của matrix**
> cần tìm sẽ là **[0 0 1]**

<br>

<a id="node-38"></a>

<p align="center"><kbd><img src="assets/354ac76b1a5f808518287299caf19bed905a0dfc.png" width="100%"></kbd></p>

> [!NOTE]
> Đến đây gs hỏi, **thế thì matrix gì sẽ ko thay đổi A**:
> dễ thấy nó sẽ là **Identity matrix**

<br>

<a id="node-39"></a>

<p align="center"><kbd><img src="assets/c4c75088296d8ab91484548848d713f16ffd2bec.png" width="100%"></kbd></p>

> [!NOTE]
> Vậy **nhờ cách hiểu linear combination of A's row** nên ta
> dễ thấy ta cần **(-3)*row 1+ 1*row 2+ 0*row 3**. Nên **row thứ
> 2 của matrix cần tìm là [-3 1 0]**

<br>

<a id="node-40"></a>

<p align="center"><kbd><img src="assets/90fb87e5fcd00b0e06a31c0acd27c69aaf0ec3fd.png" width="100%"></kbd></p>

> [!NOTE]
> Câu hỏi đặt ra là **làm sao để check một entry của matrix**
> **kết quả,** ví dụ **hàng 2, cột 3.**
>
> Là vầy: Hàng 2 của "matrix kết quả" sẽ đến từ**việc nhân
> hàng 2** của "matrix đầu" (ví dụ gọi là matrix M) cho matrix A.
> Tức **nó là linear combination của các row của matrix A**
> với coefficients là các component của hàng 2 của matrix M.
>
> Vậy vị trí đang nói chính là dot product của **hàng 2 matrix
> M** với **col 3 matrix A**

<br>

<a id="node-41"></a>

<p align="center"><kbd><img src="assets/9faf2b4daf78043d419f4adb881c11b4dd1a9771.png" width="100%"></kbd></p>

> [!NOTE]
> Tạm gọi nó là matrix **E_21**, E là **eliminate,** 21 là
> vì nó giúp **eliminate vị trí hàng 2 cột 1 của matrix A**

<br>

<a id="node-42"></a>

<p align="center"><kbd><img src="assets/8deaae9554a4e432d355f2a8b5175aab1d6740e9.png" width="100%"></kbd></p>

> [!NOTE]
> Step 2, tương tự, ta sẽ **cần hàng 1 và 2 giữ nguyên** nên
> r**ow 1, 2 của E_32** sẽ là **[1 0 0], [0 1 0]**
>
> Còn **hàng 3 sẽ là [0 -2 1]**để nó "cộng hàng 3 của A với
> -2*hàng 1 của A" nhờ vậy sẽ khử đi A_32

<br>

<a id="node-43"></a>

<p align="center"><kbd><img src="assets/bb1660ad78963048b3e6d99c8388ec13dff99701.png" width="100%"></kbd></p>

<br>

<a id="node-44"></a>

<p align="center"><kbd><img src="assets/7442e2462f5295b2d2cddf5a826d3853d22d84b4.png" width="100%"></kbd></p>

> [!NOTE]
> Tóm gọn lại các **phép biến đổi** từ **A thành U
> nãy giờ chính là vầy**E21A để khử A21
>
> E32(E21A) để khử tiếp A32

<br>

<a id="node-45"></a>

<p align="center"><kbd><img src="assets/048f8672fc9c64177d05ae1f4ccc131cf428917c.png" width="100%"></kbd></p>

> [!NOTE]
> Gs đặt câu hỏi là**matrix nào biến A
> thành U**

<br>

<a id="node-46"></a>

<p align="center"><kbd><img src="assets/da2ea77187f5d87dbf97b239befbac9ec2f072a4.png" width="100%"></kbd></p>

> [!NOTE]
> Câu trả lời **đó là**: **ta có thể thay đổi vị trí dấu ngoặc**, tức là
> ta có thể t**ính E32*E21 trước**, rồi **nhân nó cho A**.
>
> Đây chính là **associated law (luật kết hợp)**

<br>

<a id="node-47"></a>

<p align="center"><kbd><img src="assets/620646c9d73a757adc528a575b530299096ab3a1.png" width="100%"></kbd></p>

> [!NOTE]
> Thử suy nghĩ **matrix nào sẽ giúp switch/exchange 2
> row của matrix thứ 2.**
>
> Để **dc hàng thứ 1** ra**[c d]**ta cần hàng thứ 1 của
> matrix abcd * 0 + hàng thứ 2 của abcd * 1 -> **row 1
> của matrix cần tìm là [0 1]**
>
> Tương tự, **dễ thấy row 2 của matrix cần tìm là [1 0]**

<br>

<a id="node-48"></a>

<p align="center"><kbd><img src="assets/6801005babc9cec8934d03e21cd07f6f4ced847a.png" width="100%"></kbd></p>

> [!NOTE]
> Đó gọi là **permutations matrix**, **exchange các row của
> identity matrix** thì ta sẽ có **matrix giúp exchange row**

<br>

<a id="node-49"></a>

<p align="center"><kbd><img src="assets/736cb05c1b30982f88d6818224206007c6aa7699.png" width="100%"></kbd></p>

> [!NOTE]
> Tiếp theo **matrix nào
> giúp switch column?**

<br>

<a id="node-50"></a>

<p align="center"><kbd><img src="assets/d1d4d8c42bd8d3bbc79cfdf845c5494656e820b5.png" width="100%"></kbd></p>

> [!NOTE]
> Câu trả lời là **cũng P matrix nhưng để bên phải**Cụ thể: col 1 của AP sẽ là linear combination của A's columns
> với coefficients là col 1 của P. Nên để đổi chỗ hai columns của
> A thì col 1 của P sẽ là [0 1] và [1 0]

<br>

<a id="node-51"></a>

<p align="center"><kbd><img src="assets/ddf5b2aa5a93ff83a7fbf0806af233f8f5c71a33.png" width="100%"></kbd></p>

> [!NOTE]
> Gs nhắc nhở rằng**nhân matrix phải theo thứ tự, A@B
> KHÔNG BẲNG B@A**
>
> hay **commutative law ko áp dụng**

<br>

<a id="node-52"></a>

<p align="center"><kbd><img src="assets/1195d9fb4d88db262fc8fadaa538bbf110b33219.png" width="100%"></kbd></p>

> [!NOTE]
> Đoạn này gs muốn nói về **inverse**, và cho biết nãy
> giờ các matrix ví dụ đều là **invertible matrix**, b**ữa
> sau sẽ bàn đến failure case.**

<br>

<a id="node-53"></a>

<p align="center"><kbd><img src="assets/75afcd5e0dd04a3a7e6605885947a15a09d59c55.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là, nếu **từ identity matrix**, ta **trừ hàng 2 cho 3 lần hàng 1**
> để được matrix mới (gọi là E đi) mà hàng 2 là [-3 1 0], hai hàng kia giữ
> nguyên [1 0 0] và [0 0 1].
>
> Thế thì, **matrix nào sẽ giúp đảo ngược quá trình đó**. Hay nói cách
> khác **matrix nào nhân A để cho ra lại I.**
>
> Thế thì đương nhiên quá trình đảo ngược sẽ là **cộng hàng 2 của A**
> **cho 3 lần hàng 1 của A**. Nên **hàng 2 của matrix cần tìm sẽ là [3 1
> 0]**.
>
> Còn hàng 1 và 3 của A và I như nhau nên hàng 1 và 3 của matrix cần
> tìm sẽ là [1 0 0] và [0 0 1]

<br>

<a id="node-54"></a>

<p align="center"><kbd><img src="assets/1366a5db22ea14cb75fb81293ecf95fd7cb5521a.png" width="100%"></kbd></p>

> [!NOTE]
> Thế thì ta kí hiệu matrix này là là **E^-1**

<br>

