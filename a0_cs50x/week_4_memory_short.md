# Week 4 - Memory (short)

📊 **Progress:** `22` Notes | `44` Screenshots

---

<a id="node-752"></a>
## Call Stack

<br>

<a id="node-753"></a>

<p align="center"><kbd><img src="assets/c1af31e3d4f09329608eb5df904e49ab622df245.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là khi một function được gọi, máy tính nó sẽ
> set một vùng memory dành cho function đó. Được gọi
> là **stack frame hay function frame**
>
> Và khi nhiều function được gọi (cái này gọi cái kia) thì
> mỗi function đều có stack frame.

<br>

<a id="node-754"></a>

<p align="center"><kbd><img src="assets/c5f39f51d7a769698a32bcddda65fc75d809f95b.png" width="100%"></kbd></p>

> [!NOTE]
> Và các frame này được xếp trong một stack. Cái frame
> nào được gọi mới nhất thì nằm trên cùng.
>
> Một khi có function khác được gọi thì nó được push lên
> top.
>
> Và một khi nó hoàn tất, nó sẽ popped off, đẩy thằng nằm
> dưới lên

<br>

<a id="node-755"></a>

<p align="center"><kbd><img src="assets/eec3e51d41328639e054059f3934c58b47da1cfa.png" width="100%"></kbd></p>

<br>

<a id="node-756"></a>

<p align="center"><kbd><img src="assets/3fcddf4826bb709b129f8fb64e44c02141807ffa.png" width="100%"></kbd></p>

<br>

<a id="node-757"></a>

<p align="center"><kbd><img src="assets/891e2460bbf3419af8b6860a4fc91a8dd3b9f388.png" width="100%"></kbd></p>

> [!NOTE]
> Thì đại khái là minh hoạ một function tính factorization (giai thừa) là
> dạng recursive function.
>
> Main gọi printf, main pause, printf lên top
>
> Prinf gọi fact(5), printf pause, fact(5) lên top
>
> fact(5) gọi nhánh else, gọi fact(4). fact(5) pause fact(4) lên top
>
> fact(4) check ifelse -> else, gọi fact(3), fact(4) pause, fact(3) lên top
>
> ...
>
> fact(2) check, gọi fact(1), fact(2) pause, fact(1) lên top
>
> fact(1) chạy và return 1, finished, pop off, fact(2) lên top
>
> fact(2) chạy return 1*2, finished, pop off, fact(3) lên top
>
> ....

<br>

<a id="node-758"></a>

<p align="center"><kbd><img src="assets/f7441da988ef0a2466e9aac73bf672a156292a76.png" width="100%"></kbd></p>

<br>

<a id="node-759"></a>

<p align="center"><kbd><img src="assets/5fa28dcb768fe1758c1282f8832421c6c2b54897.png" width="100%"></kbd></p>

<br>

<a id="node-760"></a>

<p align="center"><kbd><img src="assets/772fa337710430297b206cb174c8410f8a8c65fd.png" width="100%"></kbd></p>

<br>

<a id="node-761"></a>

<p align="center"><kbd><img src="assets/c4d506f2e49aac17d75de1c2aa4a1c9865652ee1.png" width="100%"></kbd></p>

<br>

<a id="node-762"></a>

<p align="center"><kbd><img src="assets/458113ce9d2cfd9598db11499f29da0adfe5330b.png" width="100%"></kbd></p>

<br>

<a id="node-763"></a>

<p align="center"><kbd><img src="assets/c496aa8a25928bf6918ce7fe0596caaffc1f7211.png" width="100%"></kbd></p>

<br>


<a id="node-764"></a>
### Pointer

<br>

<a id="node-765"></a>

<p align="center"><kbd><img src="assets/e8f1e3ff31a2171054e2ef01c98ef2c39604df89.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái nói tuy nó**hơi rắc rối** nhưng pointer cho ta
> **sức mạnh để làm nhiều cái mà bình thường không
> có**. Ví dụ như trong bài giảng của David về việc**làm function swap hai biến x, y.**
>
> Nếu chỉ như cách thông thường - nơi mà khi pass  var
> vào function là **pass copy value của nó**, thì sẽ không
> làm được cái này.
>
> Nhưng với việc pass vào pointer, thì sẽ cho phép làm
> Được.

<br>

<a id="node-766"></a>

<p align="center"><kbd><img src="assets/6475d3f8cf8d0d020a7e91a6ffef70dd6aa3f650.png" width="100%"></kbd></p>

> [!NOTE]
> Nói lại chút về memory, trong cs50 là nhắc đến RAM.
> không phải hard disk. Vì ta **không thể manipulate 
> hard disk**, mà muốn**làm gì thì phải load data vào 
> RAM.**
>
> Như đã biết RAM = Random Access Memory
>
> Memory là một chuỗi huge các byte = 8 bits

<br>

<a id="node-767"></a>

<p align="center"><kbd><img src="assets/541072cf87b56d6f490efa9850caac862cd94d5e.png" width="100%"></kbd></p>

<br>

<a id="node-768"></a>

<p align="center"><kbd><img src="assets/17798b63ceb5f5a16a74debe2459dac042696707.png" width="100%"></kbd></p>

> [!NOTE]
> Ở đây hiểu thêm tại sao nó gọi là RAM
> đó là **Random Access** ý là ta có thể**access
> tới ngẫu nhiên mọi vị trí**được chứ**không phải 
> bắt buộc phải đi từ đầu.**
> Và memory giống như một**huge array các cell
> là các byte**. và mỗi byte đó có **address**, giống
> như item trong array có index.

<br>

<a id="node-769"></a>

<p align="center"><kbd><img src="assets/8642c5db5fa5612355636882c65536762afc3f1b.png" width="100%"></kbd></p>

<br>

<a id="node-770"></a>

<p align="center"><kbd><img src="assets/59d4858041e830055c8312bcf32825c4ba548a90.png" width="100%"></kbd></p>

> [!NOTE]
> Khi gọi char c = 'H', máy tính sẽ cho 1 byte để chứa giá trị 
> chuỗi binary khi tính ra base-10 tương ứng với key của 
> H trong ascii

<br>

<a id="node-771"></a>

<p align="center"><kbd><img src="assets/96037cfc9ebe802d6490680b7e9a067d5bf64632.png" width="100%"></kbd></p>

> [!NOTE]
> Tương tự khi gọi int speed = 65 thì máy tính nó tìm 4 bytes 
> trống để cho speed và gán chuỗi binary sao cho tính ra 
> base-10 là 65

<br>

<a id="node-772"></a>

<p align="center"><kbd><img src="assets/d4937c6064f769fba7ea4c44241bc4cef496f954.png" width="100%"></kbd></p>

<br>

<a id="node-773"></a>

<p align="center"><kbd><img src="assets/3709aaa7815f4c49c064964ea609cf99467bdf5e.png" width="100%"></kbd></p>

> [!NOTE]
> Ở đây ổng nói có cái gì đó liên quan
> đến việc chuỗi 4 bytes sẽ có dạng như
> này chứ không phải kia

<br>

<a id="node-774"></a>

<p align="center"><kbd><img src="assets/257e9493d1cc2a3d4048eb52453479c4f1de9faa.png" width="100%"></kbd></p>

> [!NOTE]
> Còn string, thì mỗi char 1 byte, và như đã biết máy tính 
> nó tự cho 1 byte nữa mang giá trị \0, thật ra là 00000000

<br>

<a id="node-775"></a>

<p align="center"><kbd><img src="assets/55f8695bdef0c0788a29614d8e9bfb7407b98342.png" width="100%"></kbd></p>

> [!NOTE]
> Và address memory "cell" (byte)
> thường được dùng base-16

<br>

<a id="node-776"></a>

<p align="center"><kbd><img src="assets/ade46597d418640651f7da788824cf3593a7a574.png" width="100%"></kbd></p>

> [!NOTE]
> Pointer chỉ đơn
> giản là address

<br>

<a id="node-777"></a>

<p align="center"><kbd><img src="assets/2e7c40e9aab759f9a1dd5ea7d84a43cf50a65b5b.png" width="100%"></kbd></p>

<br>

<a id="node-778"></a>

<p align="center"><kbd><img src="assets/c430b52840ff818dc9eb0dfb26eaa0ea9312f5d3.png" width="100%"></kbd></p>

<br>

<a id="node-779"></a>

<p align="center"><kbd><img src="assets/d68a08a04176a3ee25bb2cb473990b6d2e4de6aa.png" width="100%"></kbd></p>

> [!NOTE]
> Ngắn gọn là khi define int k, máy tính set một vùng 4 
> bytes trong area dành cho k. Thì ổng nói cái này giống
> như lấy cái hộp có size = 4 byte, có label k, có thể dùng 
> để chứa int
>
> Khi cho k = 5. Thì đồng nghĩa lấy chuỗi binary có giá trị
> bằng 5 (khi quy ra base-10) bỏ vào hộp.
>
> Và khi nói đến k, chính là nói đến giá trị trong hộp.
>
> ====
>
> Nhưng int* pk, máy tính sẽ set ra 8 bytes trong memory
> để dành cho pk, để có thể chứa một cái address của một 
> int. Hay nói cách khác, tạo một cái hộp chỉ chuyên dùng
> để đựng ADDRESS
>
> Và vì address có thể lớn nên phải cho loại hộp này có kích
> thước lớn hơn. 
>
> Và khi pk = &k thì tức là bỏ vào cái hộp p này một cái chuỗi
> binary mà khi tính ra base-16 thì là address của k trong memory.
> Và khi nói về p, là nói về ADDRESS của k. Và nhờ p, ta có thể 
> tìm thấy k trong memory

<br>

<a id="node-780"></a>

<p align="center"><kbd><img src="assets/ddbc0bd04e8aa43b2b02c03614f7d2ef15c6c151.png" width="100%"></kbd></p>

<br>

<a id="node-781"></a>

<p align="center"><kbd><img src="assets/fa6f1af4f8c4a3163ea76cb5ec43f9cac0583480.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là pointer và loại data mà value của nó là
> address của một cell nào đó trong memory chứa
> gía trị của một variable nào đó
>
> Và loại của variable đó chính là loại của pointer.
> Pointer chứa address dẫn tới một int (4 byte) thì 
> nó là loại int pointer...
>
> ====
>
> Xong ổng nói pointer giúp replicate ngoài đời thật
> ví dụ như ổng có cái notebook, và mình là một cái
> function giúp check và fix error notebook. Thì nếu
> không có pointer, thì nó sẽ như này: Ổng đưa mình
> cuốn sổ, mình đem photocopy thành 1 cuốn khác.
> Rồi mới sửa error trong đó, cuốn gốc vẫn không đổi
> và trả ra cuốn sửa là cuốn copy. Thế là ổng phải ngồi 
> ghi lại nhưng chỗ được sửa vào cuốn gốc.
>
> Nếu là pointer, thì mình chỉ việc nhận cuốn sổ của ổng
> rồi chỉnh sửa trong đó xong trả lại ổng là xong.

<br>

<a id="node-782"></a>

<p align="center"><kbd><img src="assets/19943466b3c04bcf640deecff830dbf1253cebf3.png" width="100%"></kbd></p>

<br>

<a id="node-783"></a>

<p align="center"><kbd><img src="assets/aa94402cf9717b7b83bde693e1501101d0af8227.png" width="100%"></kbd></p>

> [!NOTE]
> &x: Address của x var

<br>

<a id="node-784"></a>

<p align="center"><kbd><img src="assets/060e9d83e0751bb5f6dbdd6b76871776b99ae470.png" width="100%"></kbd></p>

> [!NOTE]
> Chỗ này hay đây dù biết rồi nhưng đáng nhắc lại đó là **array** 
> ví dụ int numbers[3] -> numbers là array of integer thì thật ra
> **number** chính là **pointer mang giá trị là address tới cái int đầu
> tiên trong array.**Do đó, giả sử viết function setInt() nhận int và ví dụ x2 giá trị
> thì khi gọi nó với một int variable thì giá trị của variable đưa vào
> function không bị thay đổi vì như đã biết, nó chỉ đưa copy của var's
> variable vào.
>
> Còn gỉa sử viết function setArray() nhận array và ví dụ x2 giá trị
> thì bởi**vì bản thân array đưa vào là pointer**, nên t**hực sự array 
> ở bên ngoài sẽ bị thay đổi bởi vì function đã theo ADDRESS
> của pointer đó mà thay đổi gía trị của var chứ không phải 
> chỉ là bản copy của nó**
> Cái này trong Java không có, nhưng C thì nó như vậy

<br>

<a id="node-785"></a>

<p align="center"><kbd><img src="assets/3f60780c60126099431c2433e2a8a0a60a57b272.png" width="100%"></kbd></p>

<br>

<a id="node-786"></a>

<p align="center"><kbd><img src="assets/1825f097a7cd98baa446d3d72125407c3da61e09.png" width="100%"></kbd></p>

> [!NOTE]
> int *p là define một var thuộc loại pointer, chứa address tới 1 int
>
> Thì khi đó nói đến **p** là nói đến pointer, có giá trị là 1 cái ADDRESS
>
> Và muốn nói đến cái giá trị TẠI cái ADDRESS đó thì dùng ***p**Nên print p (tất nhiên với format dành cho pointer là %p) sẽ cho ra
> ADRESS dạng base-16
>
> Còn print *p thì vì là int pointer, nên nó sẽ  cần dùng %i, nó sẽ ĐI TỚI
> ADDRESS đó, nơi đó là 4 bytes chứa gía trị integer

<br>

<a id="node-787"></a>

<p align="center"><kbd><img src="assets/c949a43f24b6c181f7ed7f3150aa9c499b32f966.png" width="100%"></kbd></p>

> [!NOTE]
> Đại khái là việc define một pointer và nếu
> chưa dùng tới thì set = NULL là good habit

<br>

<a id="node-788"></a>

<p align="center"><kbd><img src="assets/af8ebe874ceb332cc8076ab6a904abd07d531cf7.png" width="100%"></kbd></p>

<br>

<a id="node-789"></a>

<p align="center"><kbd><img src="assets/81c03ef212363c95ec3686ac1beadd681c15ab9b.png" width="100%"></kbd></p>

> [!NOTE]
> Ở đây ổng nói có một cái flaw khi đặt syntax cho pointer
> khiến nó rắc rối
>
> Như nãy cũng thấy rồi, int *p là khai báo một cái pointer
> mang giá trị là ADDRESS tới một int
>
> Rồi khi cần ĐI TỚI VÀ LẤY GIÁ TRỊ ở address đó thì dùng 
> *p.
>
> -> Nhiêu đó là thấy flaw rồi, dùng cùng 1 syntax để 2 việc khác
> nhau, declare pointer, và ĐI TỚI ADDRESS 
>
> Thì đây thêm một cái flaw nữa, đó là muốn define 3 cái pointer
> thì phải int *pa, *pb, *pc.
>
> Nên ổng nói có thấy rắc rối cũng đừng có buồn vì ai cũng vậy

<br>

<a id="node-790"></a>

<p align="center"><kbd><img src="assets/5eb791938f6667f59d088fc0c53a5d24e888d0dc.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/5eb791938f6667f59d088fc0c53a5d24e888d0dc.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/a5832d6e549b9f580a02485d979c609b8dfb6bd6.png" width="100%"></kbd></p>

> [!NOTE]
> Và trong lecture David nói pointer var được 8
> bytes thật ra đó là trong 32bit system
>
> Còn trong 16 bít system thì chỉ được 4 byte
> thôi

<br>

<a id="node-791"></a>

<p align="center"><kbd><img src="assets/6b2bcfd70633ac296cc9e458dec21d89fffbded3.png" width="100%"></kbd></p>

> [!NOTE]
> A: Đi vào address hold bởi pk
> (sẽ được k) và sét value = 35,
> vậy k sẽ thành 35

<br>

<a id="node-792"></a>

<p align="center"><kbd><img src="assets/7059dc4aa7fef4bfcc115ec9cb55b4d6ade7de5a.png" width="100%"></kbd></p>

> [!NOTE]
> A: pk là pointer, chuyên chứa address của int,
> vậy pk = &m tức là lấy ADDRESS của m gán
> cho pk
>
> pk sẽ có giá trị mới thay vì address của k,  thì
> nó mang address của m

<br>

<a id="node-793"></a>

<p align="center"><kbd><img src="assets/eeaf244d0fc050c6e29575edce260597f483cb3c.png" width="100%"></kbd></p>

<br>


<a id="node-794"></a>
#### ...

<br>

<a id="node-795"></a>

<p align="center"><kbd><img src="assets/cfcae7776e3ac42f5d359007339f4561d4c9db52.png" width="100%"></kbd></p>

<br>

<a id="node-796"></a>

<p align="center"><kbd><img src="assets/215eb12f761213d91a3b748bd84e0a91119a1d2e.png" width="100%"></kbd></p>

<br>

