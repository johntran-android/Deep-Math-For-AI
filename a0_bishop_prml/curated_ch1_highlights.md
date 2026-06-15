# Selected Notes from Bishop PRML Chapter 1

This is not a polished textbook summary. These are selected Feynman-style notes from my process of studying Bishop PRML Chapter 1, pulled from a longer set of raw notes I took while working through the material. Some moments are clean derivations. Some are me getting confused and working through it live. I'm sharing them because I think the messy parts are actually the most useful.

---

## What I focused on

- **Cross-referencing constantly.** I already had a background in Casella & Berger (*Statistical Inference*), Stat110 (Joe Blitzstein), Boyd's convex optimization (ee364a), and MIT 18.06 (Strang). So instead of just reading Bishop passively, I tried to look at every formula and ask: "where have I seen this before?" This made Bishop click much faster — but also exposed a lot of places where I'd understood something formally without really *getting* it.
- **Working through derivations by hand.** I didn't trust myself to just read a derivation and move on. For the least squares closed-form, the MLE-equals-SSE equivalence, the regularization-as-MAP result, the predictive distribution variance decomposition — I rederived all of them, often making my own notation cleaner or catching Bishop's occasional notational looseness.
- **Connecting frequentist and Bayesian framings explicitly.** Bishop switches back and forth without always flagging it clearly. A lot of my notes are just making that boundary explicit: *this* is where we stop treating w as fixed, *this* is where we integrate over it.
- **Letting confusion sit and then resolving it.** Several moments in the notes are me realizing I was confused, writing out the confusion explicitly, and then working through it. I think this is the most useful kind of note to have.

---

## Selected Highlights

### 1. Least Squares Is Just Projection onto a Column Space

> Thế thì H(HTH)inv HT**t** chính là gì? Nhớ lại, derive lại matrix chiếu lên C(A): Chiếu b lên C(A): được p ∈ C(A), residual: e = b - p sẽ vuông góc C(A) → e ∈ N(AT) ⇨ ATe = 0 ⇨ AT(b - Ax^) = 0 ⇔ ATb = ATAx^ ⇔ x^ = (ATA)inv ATb ⇨ p = Ax^ = A(ATA)invATb ⇨ matrix P chiếu b lên C(A) chính là P = A(ATA)invAT. Vậy H(HTH)inv HT**t** chính là chiếu **t** lên C(H).

**What I was working through.** After deriving the closed-form w* = (HTH)^{-1} HTt for the polynomial curve fitting problem, I realized this wasn't just "the answer" — it was the orthogonal projection of the target vector **t** onto the column space of the design matrix H. The minimum-error weights are literally just finding the closest point in the reachable output space to the observed targets. The whole least-squares problem reframes as a geometry problem in R^N. This is something I learned from Strang (MIT 18.06) but seeing it appear naturally in Bishop made it lock in.

---

### 2. Overfitting: Not a Bug in the Polynomial, a Feature of the Freedom

> Lúc này ta có thể hình dung cây nứa đã trở thành: cuộn dây, có thể map hoàn hảo các cây đinh dữ liệu nhưng, nó "thích map kiểu nào thì map", có VÔ VÀN CÁCH để đi qua hết cây đinh, và do đó, nó có XÁC SUẤT RẤT THẤP để đi theo đường cong mà ta muốn nó đi: đường sin(2πx).

**What I was working through.** When Bishop showed M=9 giving training error = 0 but terrible test error, something clicked. The model didn't fail — it succeeded too well at the wrong task. It learned the noise's specific pattern in the training set. The cuộn dây ("coil of wire") metaphor I wrote is mine: with enough flexibility, the polynomial can pass through every data point in infinitely many ways, so the chance it picks the one path that actually matches the true sin(2πx) is vanishingly small. This is the moment I stopped thinking of overfitting as "the model trying too hard" and started seeing it as "too many degrees of freedom chasing too specific a target."

---

### 3. Regularization = Ridge Regression = MAP Estimation (They Are All the Same Thing)

> Từ đó giúp mình hiểu được rằng: Khi ta giải bài toán curve fitting bằng cách minimize error function dùng sum squared error có regularizer là quadratic function của param thì thật ra ta đang giải bài toán maximizing posterior distribution với prior được chọn là Normal.
>
> minimize_**w** { Σi [ti−y(xi,**w**)]² + (α/β)**w**T**w** }
>
> Và lúc này, nó hiện hình ra đây CHÍNH LÀ BÀI TOÁN MINIMIZE SUM SQUARED ERROR FUNCTION CÓ REGULARIZER mà trong phần 1 mình đã làm: thêm regularizer vào total error để giúp giảm overfit, với regularizer hyperparam là λ = α/β.

**What I was working through.** In section 1.1, Bishop introduces regularization as a practical trick to reduce overfitting — just add λ||w||² to the loss. Then in 1.2.5, after introducing the probabilistic perspective and assuming Gaussian noise, he derives the MAP estimate. When I worked through the algebra of maximizing the log-posterior, I watched the ||w||² term emerge naturally from the log of the Gaussian prior on **w** — and the regularization hyperparameter λ turned out to be exactly the ratio α/β of the prior precision to the noise precision. The "trick" in section 1.1 was actually fully principled Bayesian reasoning in disguise.

---

### 4. MLE with Three Coin Flips — Where Prior Belief Fights Extreme Data

> Và với observed value x1 = x2 = x3 = 1 ⇨ dự đoán (ml estimate) cho θ = (1+1+1)/3 = 1. Như vậy đồng nghĩa, với việc, dựa trên 3 lần tung ra Head, thì MLE dự đoán tham số mô hình là 1, có nghĩa là nó dự đoán lần tung tiếp theo cũng sẽ ra 1.
>
> [Với Bayes estimator và prior Beta(1,1):] Kêt quả ta có: mean của β(Σixi+a, n−Σixi+b) = (3+1)/(3+1+3−3+1) = 0.8.
>
> Nói thêm tí xíu, việc chọn prior là β(a=100, b=100)... thì nó sẽ phản ánh niềm tin ban đầu rằng, θ = 0.5 một cách mãnh liệt hơn. Cụ thể là khi ta tính mean của β(Σixi+a, n−Σixi+b) với a = b = 100 thì nó sẽ là: (3+100) / (3+100+3−3+100) = 0.507.

**What I was working through.** Bishop's coin flip example is short in the text, but I worked it out in full. MLE with 3 heads gives θ̂ = 1 — a certainty claim from 3 data points. I derived the full Bayes estimator from scratch: set up the Bernoulli likelihood, choose Beta(1,1) as a conjugate prior (uniform — "I know nothing"), apply Bayes theorem, recognize the posterior as Beta(4,1), take its mean to get 0.8. Then I asked: what if we choose Beta(100,100) as prior? That corresponds to a very strong prior belief that the coin is fair. Result: 0.507. Three heads barely moves the needle. This made me understand what "strong prior" actually means in practice — it takes a lot more data to override it.

---

### 5. Bayesian Curve Fitting: Two Sources of Uncertainty, Not One

> Cái chính muốn nói, là, cái cấu phần thứ hai là kết quả đến từ việc ta tiếp cận theo Bayesian, để rồi coi **w** như random variable **W** nên kiểu như điều này khiến PHÁT SINH THÊM MỘT YẾU TỐ UNCERTAINTY NỮA (yếu tố uncertainty do coi w là random variable), và cái cấu phần thứ hai trong variance của Ti phản ánh điều này, quả thật, nó là một term liên quan đến covariance variance của posterior distribution của **W**.
>
> Var(Ti) = Φ(x)T (βXTX + αI)inv Φ(x) + 1/β

**What I was working through.** After deriving the full predictive distribution for Bayesian curve fitting, I stopped at the variance formula and tried to understand each piece separately. The 1/β term is noise — it would exist even if we knew **w** perfectly. The second term, Φ(x)^T S Φ(x), is something new: it's the uncertainty in our *estimate of **w*** propagated through to the prediction. MLE gives you only the first kind of uncertainty. Full Bayesian inference gives you both. That second term *shrinks* as you get more data — the posterior on **w** tightens up. This was the moment the phrase "uncertainty in parameters" stopped being abstract.

---

### 6. The Optimal Decision Rule Falls Out of Minimizing Misclassification

> Vậy bài toán tối ưu sẽ được thể hiện như sau:
>
> minimize_{R1,R2} { ∫R2 f(C1,**x**)d**x** + ∫R1 f(C2,**x**)d**x** }
>
> ... Để làm được điều này, về trực giác, ta sẽ chọn các **x** khiến cái cụm này âm... Vậy optimal decision rule là: Assign class C1 nếu f(C2,**x**) < f(C1,**x**) và ngược lại. Từ đó ta hiểu: cách phân loại tốt nhất chính là dựa trên posterior probability.

**What I was working through.** Bishop states the optimal decision rule almost in passing, but I wanted to *derive* it as an optimization problem. The decision regions R1, R2 are the decision variables. I wrote the misclassification probability as a sum of integrals over the wrong regions, then reformulated: minimizing over R1 is equivalent to collecting, into R1, exactly those **x** where f(C2,**x**) < f(C1,**x**). The rule "assign the class with the highest posterior probability" isn't a heuristic — it's the mathematical solution to the misclassification minimization problem. The connection back to Bayesian inference closed the loop.

---

### 7. Entropy from Two Angles, Same Formula

> Nhớ lại chút xíu bài học hôm qua. Mình được học định nghĩa của entropy theo góc nhìn thông tin... Khi đó, entropy được định nghĩa là trung bình (kì vọng) của hàm thông tin này: Entropy = −Σ{xi} log(f(xi))f(xi)...
>
> Xong gs mới nói qua cách định nghĩa Entropy trong vật lí: Nó là đại lượng mô tả sự hỗn loạn... H = lim_{N→∞} −Σi (ni/N) ln(ni/N). Và đặt pi = lim_{N→∞} ni/N... ta có lại công thức định nghĩa entropy theo cách thứ nhất.

**What I was working through.** Bishop introduces entropy twice: once from information theory (expected number of bits needed to transmit a random variable) and once from statistical mechanics (the logarithm of the number of microstates consistent with a macrostate, via Stirling's approximation at large N). Both derivations converge to the same formula −Σ p_i log p_i. I also worked through *why* entropy is maximized by the uniform distribution — because when probability is spread evenly, every outcome carries similar information, and the weighted average is large. When probability concentrates on one outcome, that outcome has near-zero information, and the rest have near-zero weight. Both cancel out toward zero. Two routes, same destination.

---

## Closing Note

These notes are part of the **Deep Math for AI** learning path — a long-form effort to build genuine mathematical foundations for machine learning, rather than just pattern-matching formulas. The full set of notes, screenshots, and derivations lives in a StudyBoard that I've been building alongside this reading. Chapter 1 alone generated over 60 notes. What's here is the curated tenth of them.

The goal isn't to reproduce the textbook. It's to be able to look at a formula and *know* where it came from — because I built it myself at least once.
