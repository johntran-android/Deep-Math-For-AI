# 2.4.2 Conjugate priors

📊 **Progress:** `1` Notes | `1` Screenshots

---
<a id="node-290"></a>

<p align="center"><kbd><img src="assets/293786f2e417e32d50227422a65502aada6aecf2.png" width="100%"></kbd></p>

> [!NOTE]
> Gs nói đại khái là mình đã quen với khái niệm prior distribution rồi. Ôn nhanh: Nói
> về prior distribution / posterior distribution thì thường là sẽ đang đi qua trường
> phái Bayesian khi coi tham số θ (ở đây là **η**) là random variable (vector), để rồi
> từ việc chọn một prior distribution cho nó (thường sách toán Casellla kí hiệu π(θ)
> ta sẽ dùng Bayes theorem để xây dựng posterior distribution π(θ|**x**) =
> f(**x**|θ)π(θ)/f(**x**). Thế thì khi prior được chọn là một distribution thuộc loại
> conjugate prior với distribution của sample f(x|θ) thì khi đó, posterior sẽ cho ra kết
> quả là cùng một loại với prior distribution, tạo ra nhiều thuận lợi trong tính toán và
> diễn giải.
>
> Vậy thì vài ví dụ đã gặp, như khi f(x|θ) là Bernuoilly, thì conjugate prior của
> population mean θ chính là beta distribution. Còn khi f(x|μ, σ^2) là pdf của normal
> μ, σ^2, thì conjugate prior của μ cũng là Normal, và conjugate prior của precision
> (1/σ^2) là Wishart distribution.
>
> Vậy thì ở đây ta bàn về conjugate prior (cho **η**) họ exponential family, gs cho
> biết nó là distribution có dạng như sau:
>
> f(**η**|**χ**, ν) = f(**χ**, ν)g(**η**)^ν exp{ν**η**T**χ**}
>
> Để chứng minh, chỉ việc derive posterior và chỉ ra nó cũng có dạng này.
>
> Còn nhớ pdf của exponential family:
>
> f(**x**|**η**) = h(**x**)g(**η**)exp{**η**T**u**(**x**)}
>
> ⇨ Joint pdf của mọi data point f(**x**1,..,**x**N|**η**), như đã biết do tính iid, tách
> thành tích các marginal pdf: f(**x**1,..,**x**N|**η**) = Πi=1:N
> h(**x**i)g(**η**)exp{**η**T**u**(**x**i)}
>
> Posterior distribution của **η**:
>
> f(**η**|**x**1,...**x**N,**χ**, ν) (trong sách là p(**η**|**X**,**χ**, ν)) = f(**x**1,...**,
> x**N|**η**) × f(**η**|**χ**, ν) / f(**x**1,...**,x**N)
>
> Như thường lệ, ta sẽ dùng kí hiệu proportional để chỉ quan tâm đến những term
> chứa **η**, phần constant sẽ tham gia vào normalizing cosntant:
>
> f(**η**|**x**1,...**x**N,**χ**, ν) ∝ f(**x**1,...**,x**N|**η**) × f(**η**|**χ**, ν)
>
> = Πi=1:N [ h(**x**i)g(**η**)exp{**η**T**u**(**x**i)} ] × f(**χ**, ν)g(**η**)^ν
> exp{ν**η**T**χ**}
>
> = [Πi=1:N h(**x**i)] × g(**η**)^N × exp{**η**T[∑i **u**(**x**i)]} × f(**χ**, ν) × g(**η**)^ν
> × exp{ν**η**T**χ**}
>
> = [Πi=1:N h(**x**i)] × f(**χ**, ν) × g(**η**)^N × g(**η**)^ν × exp{**η**T[∑i **u**(**x**i)]}
> × exp{ν**η**T**χ**}
>
> ∝ g(**η**)^(N+ν) × exp{**η**T[∑i **u**(**x**i)] + ν**η**T**χ**}
>
> ∝ g(**η**)^(N+ν) × exp{**η**T[∑i **u**(**x**i) + ν**χ**]}
>
> Tới đây, có thể thấy posteriori có dạng của priori với param là ∑i **u**(**x**i) +
> ν**χ** (so với ν**χ** của priori) và N+ν (so với ν của priori).

<br>

