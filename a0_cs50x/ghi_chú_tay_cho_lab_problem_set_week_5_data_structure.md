# Ghi Chú Tay Cho Lab + Problem Set - Week 5 - Data Structure

📊 **Progress:** `7` Notes | `50` Screenshots

---

<a id="node-1581"></a>
## Lab

<br>

<a id="node-1582"></a>

<p align="center"><kbd><img src="assets/9b5d7024c1ad5e6aba5b7482073d971dff9b5678.png" width="100%"></kbd></p>

> [!NOTE]
> Có 3 Alen A,B,O mỗi người có 2 cái. Và
> truyền random 1 cái cho con.

<br>

<a id="node-1583"></a>

<p align="center"><kbd><img src="assets/083bd8b5d336b342ddc6b6ed2dab80e90ae4441e.png" width="100%"></kbd></p>

<br>

<a id="node-1584"></a>

<p align="center"><kbd><img src="assets/3f2b4f1906f08a1307c7a7b266c82c2013936d17.png" width="100%"></kbd></p>

<br>

<a id="node-1585"></a>

<p align="center"><kbd><img src="assets/8991398d3f4e57a977164f6dfc60a36c31db14d3.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/8991398d3f4e57a977164f6dfc60a36c31db14d3.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/b00c70b2b51f7605f080c64616be6b87d7450e87.png" width="100%"></kbd></p>

> [!NOTE]
> Cũng không khó lắm

<br>

<a id="node-1586"></a>

<p align="center"><kbd><img src="assets/398e05a6531f4aa44b2b1cc331415d781d0cf8bf.png" width="100%"></kbd></p>

> [!NOTE]
> Chỉ lộn chút xíu ở chỗ khi free child
> lúc đầu để free_family(p)

<br>


<a id="node-1587"></a>
## Problem Set: Speller

> [!NOTE]
> Quay lại sau để Note & Giải thích

<br>


<a id="node-1588"></a>
### Load

<br>

<a id="node-1589"></a>

<p align="center"><kbd><img src="assets/56b5fdfd19b4d3b568fd4d656cd50265c1d05a9d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/56b5fdfd19b4d3b568fd4d656cd50265c1d05a9d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d14d341a1949bb8abe576d567a8a1b304c05a85f.png" width="100%"></kbd></p>

<br>


<a id="node-1590"></a>
#### Walkthrough

<br>

<a id="node-1591"></a>

<p align="center"><kbd><img src="assets/47804ee744c3420e16398f79e70c1406e666d2b9.png" width="100%"></kbd></p>

<br>

<a id="node-1592"></a>

<p align="center"><kbd><img src="assets/353c0799bd6c9b561e139f8072b5dce886f7759a.png" width="100%"></kbd></p>

<br>

<a id="node-1593"></a>

<p align="center"><kbd><img src="assets/ce2890b5cf26bd76c4b522c1ab423bb87acc31a3.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/ce2890b5cf26bd76c4b522c1ab423bb87acc31a3.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f8144520dbdefc27227dae9b901805c6df5b444d.png" width="100%"></kbd></p>

<br>

<a id="node-1594"></a>

<p align="center"><kbd><img src="assets/ffc91f53d8b6b5b3d0c2ca94b656866f759c0544.png" width="100%"></kbd></p>

<br>

<a id="node-1595"></a>

<p align="center"><kbd><img src="assets/f00f92bde519d56133f8b5edad3b652c2c84770d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/f00f92bde519d56133f8b5edad3b652c2c84770d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/7c56ff6bbdbbbe42b959f4d5254c4e4eced7d647.png" width="100%"></kbd></p>

<br>

<a id="node-1596"></a>

<p align="center"><kbd><img src="assets/bbda9e1e876d92bcfc77b7ae856109251d4241ba.png" width="100%"></kbd></p>

<br>

<a id="node-1597"></a>

<p align="center"><kbd><img src="assets/0a471e2f7cdaa852818f9dac7df6c094ec6d3081.png" width="100%"></kbd></p>

<br>

<a id="node-1598"></a>

<p align="center"><kbd><img src="assets/9ab3edf4521d713cb91771260a82696289e49154.png" width="100%"></kbd></p>

> [!NOTE]
> Có thể tự set word vào cũng được
> nhưng dùng strcpy sẽ tiện hơn

<br>

<a id="node-1599"></a>

<p align="center"><kbd><img src="assets/c802f2455ecf395beed22a1c1e5ec060810d65ed.png" width="100%"></kbd></p>

<br>

<a id="node-1600"></a>

<p align="center"><kbd><img src="assets/163e7eb1c85bd32c025ba35901884cc1426fc4ca.png" width="100%"></kbd></p>

<br>

<a id="node-1601"></a>

<p align="center"><kbd><img src="assets/75aa92f3b61fcae99d8eedb0cee765abce36b982.png" width="100%"></kbd></p>

> [!NOTE]
> cái word là char array mà mình muốn nó load
> vào.
>
> Thì ở đây dựa trên việc ta đã biết từ dài nhất
> trong các dictionary là bao nhiêu thì có thể tạo
> sẵn char array[]
>
> char *word[LENGTH];
> while (fscanf(file, "%s", word) != EOF)
> {
> }

<br>

<a id="node-1602"></a>

<p align="center"><kbd><img src="assets/5810789bef3c4263f2b619184b0093796445fc9c.png" width="100%"></kbd></p>

<br>

<a id="node-1603"></a>

<p align="center"><kbd><img src="assets/c84e0b6e87593426ba5ffaf4fd71a2e1aa67b3c7.png" width="100%"></kbd></p>

<br>

<a id="node-1604"></a>

<p align="center"><kbd><img src="assets/421cc21e9526613ba0feb4c1da595a8510338d02.png" width="100%"></kbd></p>

<br>

<a id="node-1605"></a>

<p align="center"><kbd><img src="assets/0ea162bfe855e9e43d22fe3a9aa65627e4d4efc9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/799bc1cf28295d54cce551ac737ca2889ae5f06c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/0ea162bfe855e9e43d22fe3a9aa65627e4d4efc9.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/799bc1cf28295d54cce551ac737ca2889ae5f06c.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/3733ebdffadc0fc4a503b6d9c3918c7b03712cbc.png" width="100%"></kbd></p>

<br>


<a id="node-1606"></a>
### Hash

<br>

<a id="node-1607"></a>

<p align="center"><kbd><img src="assets/b628b5ceeda1125c33dbc54bb90deffd8e29c790.png" width="100%"></kbd></p>

<br>

<a id="node-1608"></a>

<p align="center"><kbd><img src="assets/643bcae405796fb7b0616cadef7d5419521054de.png" width="100%"></kbd></p>

<br>

<a id="node-1609"></a>

<p align="center"><kbd><img src="assets/5d43f6d9d7b79f963d3bffb274b03ca5193d39aa.png" width="100%"></kbd></p>

<br>


<a id="node-1610"></a>
### Size

<br>


<a id="node-1611"></a>
### Check

<br>

<a id="node-1612"></a>

<p align="center"><kbd><img src="assets/8ccb62e9944327e0de10ceb5a1e8d000373d137d.png" width="100%"></kbd></p>

<br>

<a id="node-1613"></a>

<p align="center"><kbd><img src="assets/b598a68ec41e36f0c94f88063ecacd8548e39a54.png" width="100%"></kbd></p>

<br>

<a id="node-1614"></a>

<p align="center"><kbd><img src="assets/79f6bfb7beb40fd0f78b9cd28ac9fe2c4d42ffd4.png" width="100%"></kbd></p>

<br>

<a id="node-1615"></a>

<p align="center"><kbd><img src="assets/5e6cace0c8a180de16077cdd3e7dce0065f76ee7.png" width="100%"></kbd></p>

<br>

<a id="node-1616"></a>

<p align="center"><kbd><img src="assets/c8549f9b785d4c7ffd8289e43b0538502759277f.png" width="100%"></kbd></p>

<br>

<a id="node-1617"></a>

<p align="center"><kbd><img src="assets/7324f901eb0b9e893faddc258acdfcbf30f85937.png" width="100%"></kbd></p>

<br>


<a id="node-1618"></a>
### Free

<br>

<a id="node-1619"></a>

<p align="center"><kbd><img src="assets/5cf948e2b37c9619333c8dd9bbe1df3d6db80df0.png" width="100%"></kbd></p>

<br>

<a id="node-1620"></a>

<p align="center"><kbd><img src="assets/e99c8c26e36797512eb207733d94e9bae3027d2f.png" width="100%"></kbd></p>

<br>

<a id="node-1621"></a>

<p align="center"><kbd><img src="assets/3a77a9f0ba8f2d3d1ebcd294fed9f48c25c81157.png" width="100%"></kbd></p>

<br>

<a id="node-1622"></a>

<p align="center"><kbd><img src="assets/de99a8e4cd7a7a7bf656e8e34e8694a147bdb845.png" width="100%"></kbd></p>

<br>

<a id="node-1623"></a>

<p align="center"><kbd><img src="assets/acb5fea3bdd5ac870661b10dceb439a5ad7d83da.png" width="100%"></kbd></p>

<br>

<a id="node-1624"></a>

<p align="center"><kbd><img src="assets/b31cac918b84ba6060fb38afa198f6260ffab30c.png" width="100%"></kbd></p>

<br>

<a id="node-1625"></a>

<p align="center"><kbd><img src="assets/f987401e9ff0939f0749a36b0d10c3bf353fc0a6.png" width="100%"></kbd></p>

<br>

<a id="node-1626"></a>

<p align="center"><kbd><img src="assets/652d3851889bc40b99d661c33eb514544bfc720c.png" width="100%"></kbd></p>

<br>


<a id="node-1627"></a>
## Practice (không Bắt Buộc)

<br>


<a id="node-1628"></a>
### Trie

> [!NOTE]
> LÀM SAU

<br>

