# Problem Set: Speller

📊 **Progress:** `3` Notes | `43` Screenshots

---

Quay lại Note & Giải thích

<a id="node-1070"></a>
## Load

<br>

<a id="node-1071"></a>

<p align="center"><kbd><img src="assets/56b5fdfd19b4d3b568fd4d656cd50265c1d05a9d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/56b5fdfd19b4d3b568fd4d656cd50265c1d05a9d.png" width="100%"></kbd></p>

<p align="center"><kbd><img src="assets/d14d341a1949bb8abe576d567a8a1b304c05a85f.png" width="100%"></kbd></p>

<br>


<a id="node-1072"></a>
### Walkthrough

<br>

  <a id="node-1073"></a>
  <p align="center"><kbd><img src="assets/47804ee744c3420e16398f79e70c1406e666d2b9.png" width="100%"></kbd></p>
  <br>

  <a id="node-1074"></a>
  <p align="center"><kbd><img src="assets/353c0799bd6c9b561e139f8072b5dce886f7759a.png" width="100%"></kbd></p>
  <br>

  <a id="node-1075"></a>
  <p align="center"><kbd><img src="assets/ce2890b5cf26bd76c4b522c1ab423bb87acc31a3.png" width="100%"></kbd></p>
  <p align="center"><kbd><img src="assets/ce2890b5cf26bd76c4b522c1ab423bb87acc31a3.png" width="100%"></kbd></p>
  <p align="center"><kbd><img src="assets/f8144520dbdefc27227dae9b901805c6df5b444d.png" width="100%"></kbd></p>
  <br>

  <a id="node-1076"></a>
  <p align="center"><kbd><img src="assets/ffc91f53d8b6b5b3d0c2ca94b656866f759c0544.png" width="100%"></kbd></p>
  <br>

  <a id="node-1077"></a>
  <p align="center"><kbd><img src="assets/f00f92bde519d56133f8b5edad3b652c2c84770d.png" width="100%"></kbd></p>
  <p align="center"><kbd><img src="assets/f00f92bde519d56133f8b5edad3b652c2c84770d.png" width="100%"></kbd></p>
  <p align="center"><kbd><img src="assets/7c56ff6bbdbbbe42b959f4d5254c4e4eced7d647.png" width="100%"></kbd></p>
  <br>

  <a id="node-1078"></a>
  <p align="center"><kbd><img src="assets/bbda9e1e876d92bcfc77b7ae856109251d4241ba.png" width="100%"></kbd></p>
  <br>

  <a id="node-1079"></a>
  <p align="center"><kbd><img src="assets/0a471e2f7cdaa852818f9dac7df6c094ec6d3081.png" width="100%"></kbd></p>
  <br>

  <a id="node-1080"></a>
  <p align="center"><kbd><img src="assets/9ab3edf4521d713cb91771260a82696289e49154.png" width="100%"></kbd></p>
> [!NOTE]
> Có thể tự set word vào cũng được
> nhưng dùng strcpy sẽ tiện hơn

  <br>

  <a id="node-1081"></a>
  <p align="center"><kbd><img src="assets/c802f2455ecf395beed22a1c1e5ec060810d65ed.png" width="100%"></kbd></p>
  <br>

  <a id="node-1082"></a>
  <p align="center"><kbd><img src="assets/163e7eb1c85bd32c025ba35901884cc1426fc4ca.png" width="100%"></kbd></p>
  <br>

  <a id="node-1083"></a>
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

  <a id="node-1084"></a>
  <p align="center"><kbd><img src="assets/5810789bef3c4263f2b619184b0093796445fc9c.png" width="100%"></kbd></p>
  <br>

  <a id="node-1085"></a>
  <p align="center"><kbd><img src="assets/c84e0b6e87593426ba5ffaf4fd71a2e1aa67b3c7.png" width="100%"></kbd></p>
  <br>

  <a id="node-1086"></a>
  <p align="center"><kbd><img src="assets/421cc21e9526613ba0feb4c1da595a8510338d02.png" width="100%"></kbd></p>
  <br>

  <a id="node-1087"></a>
  <p align="center"><kbd><img src="assets/0ea162bfe855e9e43d22fe3a9aa65627e4d4efc9.png" width="100%"></kbd></p>
  <p align="center"><kbd><img src="assets/799bc1cf28295d54cce551ac737ca2889ae5f06c.png" width="100%"></kbd></p>
  <p align="center"><kbd><img src="assets/0ea162bfe855e9e43d22fe3a9aa65627e4d4efc9.png" width="100%"></kbd></p>
  <p align="center"><kbd><img src="assets/799bc1cf28295d54cce551ac737ca2889ae5f06c.png" width="100%"></kbd></p>
  <p align="center"><kbd><img src="assets/3733ebdffadc0fc4a503b6d9c3918c7b03712cbc.png" width="100%"></kbd></p>
  <br>


<a id="node-1088"></a>
## Hash

<br>

<a id="node-1089"></a>

<p align="center"><kbd><img src="assets/b628b5ceeda1125c33dbc54bb90deffd8e29c790.png" width="100%"></kbd></p>

<br>

<a id="node-1090"></a>

<p align="center"><kbd><img src="assets/643bcae405796fb7b0616cadef7d5419521054de.png" width="100%"></kbd></p>

<br>

<a id="node-1091"></a>

<p align="center"><kbd><img src="assets/5d43f6d9d7b79f963d3bffb274b03ca5193d39aa.png" width="100%"></kbd></p>

<br>


<a id="node-1092"></a>
## Size

<br>


<a id="node-1093"></a>
## Check

<br>

<a id="node-1094"></a>

<p align="center"><kbd><img src="assets/8ccb62e9944327e0de10ceb5a1e8d000373d137d.png" width="100%"></kbd></p>

<br>

<a id="node-1095"></a>

<p align="center"><kbd><img src="assets/b598a68ec41e36f0c94f88063ecacd8548e39a54.png" width="100%"></kbd></p>

<br>

<a id="node-1096"></a>

<p align="center"><kbd><img src="assets/79f6bfb7beb40fd0f78b9cd28ac9fe2c4d42ffd4.png" width="100%"></kbd></p>

<br>

<a id="node-1097"></a>

<p align="center"><kbd><img src="assets/5e6cace0c8a180de16077cdd3e7dce0065f76ee7.png" width="100%"></kbd></p>

<br>

<a id="node-1098"></a>

<p align="center"><kbd><img src="assets/c8549f9b785d4c7ffd8289e43b0538502759277f.png" width="100%"></kbd></p>

<br>

<a id="node-1099"></a>

<p align="center"><kbd><img src="assets/7324f901eb0b9e893faddc258acdfcbf30f85937.png" width="100%"></kbd></p>

<br>


<a id="node-1100"></a>
## Free

<br>

<a id="node-1101"></a>

<p align="center"><kbd><img src="assets/5cf948e2b37c9619333c8dd9bbe1df3d6db80df0.png" width="100%"></kbd></p>

<br>

<a id="node-1102"></a>

<p align="center"><kbd><img src="assets/e99c8c26e36797512eb207733d94e9bae3027d2f.png" width="100%"></kbd></p>

<br>

<a id="node-1103"></a>

<p align="center"><kbd><img src="assets/3a77a9f0ba8f2d3d1ebcd294fed9f48c25c81157.png" width="100%"></kbd></p>

<br>

<a id="node-1104"></a>

<p align="center"><kbd><img src="assets/de99a8e4cd7a7a7bf656e8e34e8694a147bdb845.png" width="100%"></kbd></p>

<br>

<a id="node-1105"></a>

<p align="center"><kbd><img src="assets/acb5fea3bdd5ac870661b10dceb439a5ad7d83da.png" width="100%"></kbd></p>

<br>

<a id="node-1106"></a>

<p align="center"><kbd><img src="assets/b31cac918b84ba6060fb38afa198f6260ffab30c.png" width="100%"></kbd></p>

<br>

<a id="node-1107"></a>

<p align="center"><kbd><img src="assets/f987401e9ff0939f0749a36b0d10c3bf353fc0a6.png" width="100%"></kbd></p>

<br>

<a id="node-1108"></a>

<p align="center"><kbd><img src="assets/652d3851889bc40b99d661c33eb514544bfc720c.png" width="100%"></kbd></p>

<br>

