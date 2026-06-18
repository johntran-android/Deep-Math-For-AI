# Deep Math For AI — A Self-Study Learning Lab

> *Learning AI from the mathematical foundations up — through active explanation, derivations, implementation, and product-building.*

**`~12,306 notes` · `~16,720 screenshots` · `19 courses`** · work in progress

---

## What is this?

This is not a perfect textbook, not an encyclopedia, and not an official course.

This is my **public learning lab**: a long-term record of how I am rebuilding the mathematical and statistical foundations beneath AI/ML from first principles.

The notes are raw, personal, evolving, and sometimes imperfect. That is part of the point. This repo shows the learning process: the confusion, the pauses, the explanations, the corrections, and the gradual connection between ideas.

---

## Why does this repo exist?

I do not want to learn AI only as a layer of APIs, tools, prompts, or surface-level frameworks.

The goal is to build a foundation strong enough to:

- read serious textbooks and papers;
- understand models instead of only using models;
- understand loss, risk, inference, uncertainty, optimization, and representation learning;
- connect theory with implementation;
- and eventually build AI products with more depth than a thin wrapper.

This repo is one part of that path: the theory and learning proof-of-work layer.

---

## ⚙️ Method: Feynman-style Active Explanation

My learning method is based on a Feynman-style loop:

1. Study a small piece of material.
2. Pause.
3. Capture the source when useful — a screenshot, a formula, a lecture slide, or a PDF excerpt.
4. Explain the idea again in my own words.
5. Identify what I still cannot explain clearly.
6. Revisit, correct, and connect it with earlier knowledge.

For math-heavy materials, this often means deconstructing formulas, theorems, and derivations until the core mechanism becomes explainable.

But the deeper point is not merely to "break down every formula." The deeper point is **active understanding**: forcing myself to teach the idea back, in plain language, instead of passively reading and moving on.

You will see many moments like:

> *"Wait — what is this actually saying?"*

That is the core of this repo: not polished notes, but visible thinking.

---

## 🗺️ Learning Roadmap

**Status legend:**

| Label | Meaning |
|-------|---------|
| Core Covered | I have covered the core material needed for my current AI/ML path. May revisit advanced chapters later. Not a claim of mastery. |
| Active | Currently studying. |
| Revisiting | Previously covered; returning for deeper understanding or to fill gaps. |
| Planned | Future study — queued but not started yet. |
| Reference Later | Important reference, but not a linear target for now. |

---

### Layer 0 — Mathematical Foundations

| Status | Topic | Source |
|--------|-------|--------|
| Core Covered | Single Variable Calculus | MIT 18.01 |
| Core Covered | Multivariable Calculus | MIT 18.02 |
| Core Covered | Linear Algebra | MIT 18.06 / Gilbert Strang |
| Core Covered | Probability | Harvard STAT 110 / Blitzstein |
| Core Covered | Matrix Calculus / Matrix Methods | MIT 18.S096 |

### Layer 1 — Statistics and Optimization for ML

| Status | Topic | Source | Note |
|--------|-------|--------|------|
| Core Covered | Statistical Inference | Casella & Berger | Ch.1–9 covered; Ch.10–12 planned revisit |
| Core Covered | Convex Optimization | Boyd & Vandenberghe / EE364A | Core chapters covered |
| Active | Numerical Optimization | Nocedal & Wright | Currently around Ch.8 |
| Active | Pattern Recognition and Machine Learning | Christopher Bishop | Currently Ch.2 |
| Planned | Elements of Statistical Learning | Hastie, Tibshirani, Friedman | After Bishop |
| Reference Later | Probabilistic Machine Learning | Kevin Murphy | Deeper path, later |

### Layer 2 — Core Machine Learning and Deep Learning

| Status | Topic | Source |
|--------|-------|--------|
| Core Covered | Machine Learning Foundations | Andrew Ng ML Specialization |
| Core Covered | Deep Learning | Deep Learning Specialization |
| Core Covered | Computer Vision | Stanford CS231n |
| Core Covered | NLP with Deep Learning | Stanford CS224n |
| Planned | Machine Learning | Stanford CS229 |
| Planned | Deep Learning Textbook | Goodfellow, Bengio, Courville |
| Reference Later | Modern LLM Systems | RAG, agents, evaluation, AI engineering |

### Layer 3 — Implementation Practice

| Status | Project |
|--------|---------|
| Planned | Linear regression from scratch |
| Planned | Logistic regression from scratch |
| Planned | Backpropagation from scratch |
| Planned | CS229-style assignments |
| Revisiting / Planned | CS231n-style neural network assignments |
| Planned | Optimization algorithms: gradient descent, Newton, conjugate gradient, BFGS |

### Layer 4 — Product Layer

| Status | Project |
|--------|---------|
| Active | StudyBoard — AI-assisted learning system (see below) |
| Planned | Adaptive review scheduling |
| Planned | Concept mastery tracking |
| Planned | Cross-notebook knowledge graph |
| Planned | Applying ML/AI foundations into real product features |

---

## 🛠️ Product Layer: StudyBoard

StudyBoard is my current product experiment: an AI-assisted learning system built around active explanation, AI feedback, memory review, and knowledge linking.

It started from the same workflow used in this repo:

> study → pause → capture → explain in my own words → get AI feedback → review later

Current and planned product features:
- AI Check — feedback on your own explanation of a concept
- Memory Gym — active recall sessions
- Review Feed — spaced repetition question bank
- Cross-notebook knowledge graph
- Concept mastery tracking

**Live demo:** [studyboard.app](https://the-studying-board.web.app/landing.html)
*Status: early work-in-progress. Not production-ready. Features and stability are actively being built.*

---

## 📱 Shipped Products Before This AI Path

Before going deep into AI foundations, I worked as a self-taught Android developer and shipped consumer apps with real users.

- [Sentence Master](https://play.google.com/store/apps/details?id=com.hungdaovuong.sentencemaster.en) — 1M+ downloads

This background shapes how I think about this AI path: the goal is not only to understand theory, but to eventually ship AI products that are genuinely useful.

---

## What this repo is meant to show

1. I am willing to study difficult foundations seriously — and I have the notes to prove it.
2. I can explain mathematical and AI concepts in my own words, not just copy-paste from textbooks.
3. I am building a bridge: theory → implementation → product.

The long-term goal is not to collect notes.

The goal is to become the kind of engineer who understands AI systems deeply, can implement core ideas, and can build products on top of that foundation.

---

---

# 🧠 Deep Math For AI — Nhật Ký Tự Học

> *Học AI từ nền toán đi lên — bằng cách chủ động giải thích lại, bóc tách công thức, tự triển khai, và cuối cùng áp dụng vào sản phẩm thật.*

---

## Đây là gì?

Đây không phải một giáo trình hoàn hảo, không phải bách khoa toàn thư, cũng không phải tài liệu chính thức của một khóa học.

Đây là **public learning lab** của mình: nơi mình ghi lại quá trình tự xây lại nền tảng toán học, thống kê, tối ưu, và machine learning phía dưới AI.

Các ghi chú trong repo này có thể thô, cá nhân, đang tiến hóa, và chắc chắn không hoàn hảo. Nhưng đó cũng là điểm chính: repo này không chỉ cho thấy kết quả cuối cùng, mà còn cho thấy quá trình suy nghĩ, chỗ vấp, chỗ sửa, và cách các ý tưởng dần được nối lại với nhau.

---

## Vì sao repo này tồn tại?

Mình không muốn học AI chỉ như một lớp API, tool, prompt, hay framework bề mặt.

Mục tiêu của repo này là xây một nền đủ chắc để có thể:

- đọc textbook và paper nghiêm túc hơn;
- hiểu mô hình thay vì chỉ dùng mô hình;
- hiểu loss, risk, inference, uncertainty, optimization, và representation learning;
- nối lý thuyết với implementation;
- và cuối cùng dùng nền đó để build AI products có chiều sâu hơn một thin wrapper.

Repo này là một phần của con đường đó: tầng lý thuyết và bằng chứng học tập công khai.

---

## ⚙️ Phương pháp: Feynman-style Active Explanation

Cách học của mình dựa trên một vòng lặp kiểu Feynman:

1. Học một mảnh kiến thức nhỏ.
2. Dừng lại.
3. Chụp lại nguồn khi cần — screenshot, công thức, slide bài giảng, hoặc một đoạn trong PDF.
4. Giải thích lại ý tưởng đó bằng lời của mình.
5. Tự phát hiện chỗ nào mình vẫn chưa giải thích rõ được.
6. Quay lại sửa, bổ sung, và nối với kiến thức đã học trước đó.

Với các tài liệu nặng về toán, điều này thường dẫn đến việc bóc tách công thức, định lý, và các bước suy luận cho đến khi mình có thể giải thích được cơ chế chính.

Nhưng tinh thần chính không chỉ là "bóc tách mọi công thức." Tinh thần chính là **học chủ động**: buộc bản thân phải dạy lại ý tưởng bằng ngôn ngữ của mình, thay vì chỉ đọc lướt qua rồi tưởng là đã hiểu.

Bạn sẽ thấy rất nhiều khoảnh khắc kiểu:

> *"Khoan — đoạn này thực ra đang nói gì?"*

Đó là tinh thần của repo này: không phải ghi chú bóng bẩy, mà là quá trình suy nghĩ được ghi lại.

---

## 🛠️ Tầng sản phẩm: StudyBoard

StudyBoard là product experiment hiện tại của mình — một AI learning system xây dựng xung quanh active explanation, AI feedback, memory review, và knowledge linking.

Nó bắt đầu từ đúng workflow mình đang dùng trong repo này:

> học → dừng lại → capture → giải thích bằng lời mình → nhận AI feedback → ôn lại sau

**Live demo:** [studyboard.app](https://the-studying-board.web.app/landing.html)
*Trạng thái: đang phát triển, chưa production-ready.*

---

## 📱 Sản phẩm đã ship trước khi đi sâu vào AI

Trước khi đi sâu vào nền tảng AI, mình là Android developer tự học và đã ship app có người dùng thật.

- [Sentence Master](https://play.google.com/store/apps/details?id=com.hungdaovuong.sentencemaster.en) — 1M+ lượt tải

Nền tảng đó giúp mình nhìn con đường AI không chỉ là "học cho biết" mà là "học để ship được thứ có giá trị thật."

---

## Repo này chứng minh điều gì?

1. Mình thật sự nghiêm túc với nền tảng khó — và có notes để chứng minh.
2. Mình có thể giải thích lại các khái niệm toán/AI bằng lời của mình.
3. Mình đang xây cầu nối từ lý thuyết → implementation → sản phẩm.

Mục tiêu dài hạn không chỉ là gom nhiều note.

Mục tiêu là trở thành một engineer có thể hiểu AI system ở tầng sâu, tự triển khai các ý tưởng cốt lõi, và build sản phẩm AI có giá trị thật trên nền đó.

---

## 📚 Syllabus / Mục lục

### 📂 MIT 18.01 — Single Variable Calculus (📝 322 Notes | 📸 331 Screenshots)

- [Lec 1: Rate Of Change](a0_mit1801/lec_1_rate_of_change.md) — `25n / 26i` 
- [Lec 2: Limits](a0_mit1801/lec_2_limits.md) — `28n / 30i` 
- [Lec 3: Derivatives](a0_mit1801/lec_3_derivatives.md) — `21n / 22i` 
- [Lec 4: Chain Rule](a0_mit1801/lec_4_chain_rule.md) — `21n / 22i` 
- [Lec 5: Implicit Differentiaion](a0_mit1801/lec_5_implicit_differentiaion.md) — `29n / 30i` 
- [Lec 6: Exponential & Log](a0_mit1801/lec_6_exponential_log.md) — `39n / 37i` 
- [Lec 9: Linear And Quadratic Approximations](a0_mit1801/lec_9_linear_and_quadratic_approximations.md) — `27n / 28i` 
- [Lec 10: Curve Sketching](a0_mit1801/lec_10_curve_sketching.md) — `28n / 29i` 
- [Lec 11: Max-min](a0_mit1801/lec_11_max_min.md) — `30n / 30i` 
- [Lec 12: Related Rates](a0_mit1801/lec_12_related_rates.md) — `24n / 25i` 
- [Lec 13: Newton's Method](a0_mit1801/lec_13_newtons_method.md) — `26n / 28i` 
- [Lec 14: Mean Value Theorem](a0_mit1801/lec_14_mean_value_theorem.md) — `24n / 24i`

### 📂 MIT 18.02 — Multivariable Calculus (📝 567 Notes | 📸 615 Screenshots)

- [Lec 1: Dot Products](a0_mit1802/lec_1_dot_products.md) — `0n / 4i` 
- [Lec 2: Determinant, Cross Product](a0_mit1802/lec_2_determinant_cross_product.md) — `17n / 21i` 
- [Lec 3: Matrix, Inverse Matrix](a0_mit1802/lec_3_matrix_inverse_matrix.md) — `26n / 31i` 
- [Lec 4: Square System, Equation Of Plane](a0_mit1802/lec_4_square_system_equation_of_plane.md) — `20n / 23i` 
- [Lec 5: Parametric Equations For Lines And Curves](a0_mit1802/lec_5_parametric_equations_for_lines_and_curves.md) — `23n / 24i` 
- [Lec 6: Velocity, Acceleration, Kepler's Second Law](a0_mit1802/lec_6_velocity_acceleration_keplers_second_law.md) — `27n / 28i` 
- [Lec 7: Review](a0_mit1802/lec_7_review.md) — `16n / 17i` 
- [Lec 8: Level Curves, Partial Derivatives, Tangent Plane](a0_mit1802/lec_8_level_curves_partial_derivatives_tangent_plane.md) — `20n / 22i` 
- [Lec 9: Max-min Problems, Least Squares](a0_mit1802/lec_9_max_min_problems_least_squares.md) — `23n / 28i` 
- [Lec 10: Second Derivative Test, Boudaries, Infinity](a0_mit1802/lec_10_second_derivative_test_boudaries_infinity.md) — `24n / 24i` 
- [Lec 11: Differentials, Chain-rule](a0_mit1802/lec_11_differentials_chain_rule.md) — `27n / 21i` 
- [Lec 12: Gradient, Directional Derivative, Tangent Plane](a0_mit1802/lec_12_gradient_directional_derivative_tangent_plane.md) — `35n / 37i` 
- [Lec 13: Lagrange Multiplier](a0_mit1802/lec_13_lagrange_multiplier.md) — `33n / 36i` 
- [Lec 14: Non-independent Random Variables](a0_mit1802/lec_14_non_independent_random_variables.md) — `32n / 35i` 
- [Lec 15: Partial Differentials Equations](a0_mit1802/lec_15_partial_differentials_equations.md) — `18n / 19i` 
- [Lec 16: Double Integrals](a0_mit1802/lec_16_double_integrals.md) — `36n / 37i` 
- [Lec 17: Double Integrals In Polar Coordinates](a0_mit1802/lec_17_double_integrals_in_polar_coordinates.md) — `21n / 21i` 
- [Lec 18: Change Of Variables](a0_mit1802/lec_18_change_of_variables.md) — `34n / 36i` 
- [Lec 19: Vector Fields](a0_mit1802/lec_19_vector_fields.md) — `36n / 44i` 
- [Lec 20: Path Independence & Conservative Field](a0_mit1802/lec_20_path_independence_conservative_field.md) — `38n / 43i` 
- [Lec 21: Gradient Field & Potential Function](a0_mit1802/lec_21_gradient_field_potential_function.md) — `35n / 35i` 
- [Lec 22: Green's Theorem](a0_mit1802/lec_22_greens_theorem.md) — `26n / 29i`

### 📂 MIT 18.06 — Linear Algebra (📝 1260 Notes | 📸 1269 Screenshots)

- [Lecture 1: The Geometry Of Linear Equations](a0_mit1806/lecture_1_the_geometry_of_linear_equations.md) — `19n / 20i` 
- [Lecture 2: Elimination With Matrices](a0_mit1806/lecture_2_elimination_with_matrices.md) — `30n / 31i` 
- [Lecture 3: Multiplication And Inverse Matrices](a0_mit1806/lecture_3_multiplication_and_inverse_matrices.md) — `22n / 24i` 
- [Lecture 4: Factorization Into A = Lu](a0_mit1806/lecture_4_factorization_into_a_lu.md) — `26n / 25i` 
- [Lecture 5: Transpose, Permutations, Spaces R^n](a0_mit1806/lecture_5_transpose_permutations_spaces_rn.md) — `23n / 24i` 
- [Lecture 6: Column Space And Null Space](a0_mit1806/lecture_6_column_space_and_null_space.md) — `24n / 24i` 
- [Lecture 7: Solving Ax = 0:](a0_mit1806/lecture_7_solving_ax_0.md) — `33n / 37i` 
- [Lecture 8: Solving Ax = B: Row Reduced Form R](a0_mit1806/lecture_8_solving_ax_b_row_reduced_form_r.md) — `38n / 37i` 
- [Lecture 9: Independece, Basis, And Dimension](a0_mit1806/lecture_9_independece_basis_and_dimension.md) — `35n / 37i` 
- [Lecture 10: The Four Fundamental Subspaces](a0_mit1806/lecture_10_the_four_fundamental_subspaces.md) — `26n / 29i` 
- [Lecture 11: Matrix Spaces; Rank 1; Small World Graphs](a0_mit1806/lecture_11_matrix_spaces_rank_1_small_world_graphs.md) — `33n / 34i` 
- [Lecture 12: Graphs, Networks, Incidence Matrices](a0_mit1806/lecture_12_graphs_networks_incidence_matrices.md) — `37n / 40i` 
- [Lecture 13: Quiz Review](a0_mit1806/lecture_13_quiz_review.md) — `37n / 40i` 
- [Lecture 14: Orthogonal Vectors And Subspaces](a0_mit1806/lecture_14_orthogonal_vectors_and_subspaces.md) — `37n / 37i` 
- [Lecture 15: Projections Onto Subspaces](a0_mit1806/lecture_15_projections_onto_subspaces.md) — `45n / 47i` 
- [Lecture 16: Projection Matrices And Least Squares](a0_mit1806/lecture_16_projection_matrices_and_least_squares.md) — `38n / 43i` 
- [Lecture 17: Orthogonal Matrices And Gram-schmidt](a0_mit1806/lecture_17_orthogonal_matrices_and_gram_schmidt.md) — `38n / 39i` 
- [Lecture 18: Properties Of Determinants](a0_mit1806/lecture_18_properties_of_determinants.md) — `37n / 39i` 
- [Lecture 19: Determinant Formulas And Cofactors](a0_mit1806/lecture_19_determinant_formulas_and_cofactors.md) — `39n / 41i` 
- [Lecture 20: Cramer's Rule, Inverse Matrix And Volume](a0_mit1806/lecture_20_cramers_rule_inverse_matrix_and_volume.md) — `29n / 30i` 
- [Lecture 21: Eigenvalues And Eigenvectors](a0_mit1806/lecture_21_eigenvalues_and_eigenvectors.md) — `40n / 39i` 
- [Lecture 22: Diagonalization And Powers Of A](a0_mit1806/lecture_22_diagonalization_and_powers_of_a.md) — `43n / 42i` 
- [Lecture 23: Differential Equations And Exp(at)](a0_mit1806/lecture_23_differential_equations_and_expat.md) — `55n / 56i` 
- [18.03 Lec 25](a0_mit1806/1803_lec_25.md) — `27n / 28i` 
- [Lecture 24: Markow Matrices; Fourier Series](a0_mit1806/lecture_24_markow_matrices_fourier_series.md) — `38n / 37i` 
- [Lecture 24b: Quiz 2 Review](a0_mit1806/lecture_24b_quiz_2_review.md) — `33n / 34i` 
- [Lecture 25: Symmetric Matrices And Positive Definiteness](a0_mit1806/lecture_25_symmetric_matrices_and_positive_definiteness.md) — `39n / 30i` 
- [Lecture 26: Complex Matrices; Fast Fourier Transform](a0_mit1806/lecture_26_complex_matrices_fast_fourier_transform.md) — `29n / 30i` 
- [Lecture 27: Positive Definite Matrices And Minima](a0_mit1806/lecture_27_positive_definite_matrices_and_minima.md) — `39n / 39i` 
- [Lecture 28: Similar Matrices And Jordan Form](a0_mit1806/lecture_28_similar_matrices_and_jordan_form.md) — `38n / 32i` 
- [Lecture 29: Singular Value Decomposition](a0_mit1806/lecture_29_singular_value_decomposition.md) — `44n / 37i` 
- [Lecture 30: Linear Transformations And Their Matrices](a0_mit1806/lecture_30_linear_transformations_and_their_matrices.md) — `52n / 46i` 
- [Lecture 31: Change Of Basis; Image Compression](a0_mit1806/lecture_31_change_of_basis_image_compression.md) — `37n / 36i` 
- [Lecture 32: Quiz 3 Review](a0_mit1806/lecture_32_quiz_3_review.md) — `37n / 38i` 
- [Lecture 33: Left And Right Inverse; Pseudoinverse](a0_mit1806/lecture_33_left_and_right_inverse_pseudoinverse.md) — `31n / 33i` 
- [Lecture 34: Final Course Review](a0_mit1806/lecture_34_final_course_review.md) — `32n / 34i`

### 📂 MIT 18.06 — Linear Algebra (Book Notes) (📝 124 Notes | 📸 138 Screenshots)

- [7.4 Geometry Of Svd](a0_mit1806_book/74_geometry_of_svd.md) — `24n / 19i` 
- [3.3 THE COMPLETE SOLUTION TO Ax=b](a0_mit1806_book/33_the_complete_solution_to_axb.md) — `2n / 2i` 
- [Ps 3.5](a0_mit1806_book/ps_35.md) — `0n / 3i` 
- [8.1 Idea Of A Linear Transformation](a0_mit1806_book/81_idea_of_a_linear_transformation.md) — `18n / 20i` 
- [6.2 Diagonalizing A Matrix](a0_mit1806_book/62_diagonalizing_a_matrix.md) — `18n / 22i` 
- [8.2 The Matrix Of Linear Transformation](a0_mit1806_book/82_the_matrix_of_linear_transformation.md) — `21n / 23i` 
- [6.3 System Of Differential Equations](a0_mit1806_book/63_system_of_differential_equations.md) — `5n / 6i` 
- [8.3 In Search Of Good Basis](a0_mit1806_book/83_in_search_of_good_basis.md) — `3n / 4i` 
- [6.4 Symmetric Matrices](a0_mit1806_book/64_symmetric_matrices.md) — `4n / 4i` 
- [11.2 Norm & Condition Number](a0_mit1806_book/112_norm_condition_number.md) — `13n / 15i` 
- [7.2 Basis And Matrices In Svd](a0_mit1806_book/72_basis_and_matrices_in_svd.md) — `3n / 6i` 
- [11.3 Iterative Method & Preconditioner](a0_mit1806_book/113_iterative_method_preconditioner.md) — `4n / 6i` 
- [7.3 Pca By Svd](a0_mit1806_book/73_pca_by_svd.md) — `8n / 7i`

### 📂 STAT 110 — Probability (📝 1132 Notes | 📸 1108 Screenshots)

- [Lec 1: Probability & Counting](a0_stat110/lec_1_probability_counting.md) — `17n / 17i` 
- [Lec 2: Story Proofs, Axioms Of Probability](a0_stat110/lec_2_story_proofs_axioms_of_probability.md) — `30n / 23i` 
- [Lec 3: Birthday Problem, Properties Of Probability](a0_stat110/lec_3_birthday_problem_properties_of_probability.md) — `28n / 23i` 
- [Lec 4: Conditional Probability](a0_stat110/lec_4_conditional_probability.md) — `34n / 26i` 
- [Lec 5: Conditional Probability, Law Of Total Probability](a0_stat110/lec_5_conditional_probability_law_of_total_probability.md) — `36n / 35i` 
- [Lec 6: Monty Hall, Simpson's Paradox](a0_stat110/lec_6_monty_hall_simpsons_paradox.md) — `27n / 23i` 
- [Lec 7: Gambler's Ruin & Random Variables](a0_stat110/lec_7_gamblers_ruin_random_variables.md) — `37n / 35i` 
- [Lec 8: Random Variables & Their Distributions](a0_stat110/lec_8_random_variables_their_distributions.md) — `41n / 36i` 
- [Lec 9: Expectation, Indicator Random Variables, Linearity](a0_stat110/lec_9_expectation_indicator_random_variables_linearity.md) — `63n / 41i` 
- [Lec 10: Expected Value](a0_stat110/lec_10_expected_value.md) — `44n / 41i` 
- [Lec 11: Poisson Distribution](a0_stat110/lec_11_poisson_distribution.md) — `37n / 39i` 
- [Lec 12: Discrete Vs Continuous, The Uniform](a0_stat110/lec_12_discrete_vs_continuous_the_uniform.md) — `51n / 49i` 
- [Lec 13: Normal Distribution](a0_stat110/lec_13_normal_distribution.md) — `44n / 42i` 
- [Lec 14: Location, Scale, Lotus](a0_stat110/lec_14_location_scale_lotus.md) — `58n / 47i` 
- [Lec 15: Midterm Review](a0_stat110/lec_15_midterm_review.md) — `34n / 32i` 
- [Lec 16: Exponential Distribution](a0_stat110/lec_16_exponential_distribution.md) — `31n / 25i` 
- [Lec 17: Moment Generating Functions](a0_stat110/lec_17_moment_generating_functions.md) — `62n / 60i` 
- [Lec 18: MGF Continued](a0_stat110/lec_18_mgf_continued.md) — `53n / 49i` 
- [Lec 19: Joint, Conditional And Marginal Distribution](a0_stat110/lec_19_joint_conditional_and_marginal_distribution.md) — `46n / 41i` 
- [Lec 20: Multinomial And Cauchy](a0_stat110/lec_20_multinomial_and_cauchy.md) — `37n / 44i` 
- [Lec 21: Covariance & Correlation](a0_stat110/lec_21_covariance_correlation.md) — `50n / 38i` 
- [Lec 22: Transformations & Convolution](a0_stat110/lec_22_transformations_convolution.md) — `28n / 28i` 
- [Lec 23: Beta Distribution](a0_stat110/lec_23_beta_distribution.md) — `15n / 13i` 
- [Lec 24: Gamma Distribution & Poisson](a0_stat110/lec_24_gamma_distribution_poisson.md) — `37n / 24i` 
- [Lec 25: Order Statistic & Conditional Expectation](a0_stat110/lec_25_order_statistic_conditional_expectation.md) — `30n / 31i` 
- [Lec 26 Conditional Expectation](a0_stat110/lec_26_conditional_expectation.md) — `35n / 33i` 
- [Lec 27: Conditional Expectation Given An R.v](a0_stat110/lec_27_conditional_expectation_given_an_rv.md) — `34n / 36i` 
- [Lec 28: Inequalities](a0_stat110/lec_28_inequalities.md) — `26n / 21i` 
- [Lec 29: Law Of Large Numbers & Law Of Central Limit](a0_stat110/lec_29_law_of_large_numbers_law_of_central_limit.md) — `38n / 36i` 
- [Lec 30: Chi-square, Student-t, Multi-variate Gaussian](a0_stat110/lec_30_chi_square_student_t_multi_variate_gaussian.md) — `24n / 22i` 
- [Σ Lec 1](a0_stat110/σ_lec_1.md) — `0n / 3i` 
- [Σ Lec 2](a0_stat110/σ_lec_2.md) — `0n / 4i` 
- [Σ Lec 3](a0_stat110/σ_lec_3.md) — `0n / 4i` 
- [Σ Lec 4](a0_stat110/σ_lec_4.md) — `0n / 5i` 
- [Σ Lec 6](a0_stat110/σ_lec_6.md) — `0n / 4i` 
- [Σ Lec 5](a0_stat110/σ_lec_5.md) — `0n / 4i` 
- [Σ Lec 7](a0_stat110/σ_lec_7.md) — `0n / 3i` 
- [Σ Lec 8](a0_stat110/σ_lec_8.md) — `0n / 4i` 
- [Σ Lec 9](a0_stat110/σ_lec_9.md) — `0n / 5i` 
- [Σ Lec 10](a0_stat110/σ_lec_10.md) — `0n / 3i` 
- [Σ Lec 11](a0_stat110/σ_lec_11.md) — `0n / 3i` 
- [Σ Lec 12](a0_stat110/σ_lec_12.md) — `1n / 3i` 
- [Σ Lec 13](a0_stat110/σ_lec_13.md) — `0n / 5i` 
- [Σ Lec 14](a0_stat110/σ_lec_14.md) — `0n / 6i` 
- [Σ Lec 15](a0_stat110/σ_lec_15.md) — `0n / 6i` 
- [Σ Lec 16](a0_stat110/σ_lec_16.md) — `1n / 4i` 
- [Σ Lec 17](a0_stat110/σ_lec_17.md) — `1n / 6i` 
- [Σ Lec 18](a0_stat110/σ_lec_18.md) — `1n / 5i` 
- [Σ Lec 19](a0_stat110/σ_lec_19.md) — `1n / 6i` 
- [Σ Lec 20](a0_stat110/σ_lec_20.md) — `0n / 4i` 
- [Σ Lec 21](a0_stat110/σ_lec_21.md) — `0n / 8i` 
- [Σ lec 22](a0_stat110/σ_lec_22.md) — `0n / 3i`

### 📂 Casella & Berger — Statistical Inference (📝 895 Notes | 📸 1033 Screenshots)

- [1.1 Set Theory](a0_casella/11_set_theory.md) — `6n / 9i` 
- [1.2.1 Axiomatic Foundation](a0_casella/121_axiomatic_foundation.md) — `11n / 10i` 
- [1.2.2 Calculus Of Probability](a0_casella/122_calculus_of_probability.md) — `8n / 9i` 
- [1.2.3 Counting](a0_casella/123_counting.md) — `6n / 8i` 
- [1.2.4 Enumerating Outcome](a0_casella/124_enumerating_outcome.md) — `5n / 9i` 
- [1.3 Conditional Probability & Independence](a0_casella/13_conditional_probability_independence.md) — `18n / 16i` 
- [1.4 Random Variables](a0_casella/14_random_variables.md) — `8n / 5i` 
- [1.5 Distribution Function](a0_casella/15_distribution_function.md) — `17n / 11i` 
- [1.6 PDF & Pmf](a0_casella/16_pdf_pmf.md) — `7n / 5i` 
- [2.1 Distribution](a0_casella/21_distribution.md) — `18n / 21i` 
- [2.2 Expected Value](a0_casella/22_expected_value.md) — `10n / 10i` 
- [2.3 MGF](a0_casella/23_mgf.md) — `18n / 25i` 
- [2.4 Differentiating under integral](a0_casella/24_differentiating_under_integral.md) — `16n / 19i` 
- [2.5 Ex](a0_casella/25_ex.md) — `3n / 2i` 
- [3.1&2 Discrete distribution](a0_casella/312_discrete_distribution.md) — `29n / 32i` 
- [3.3 Continuous distribution](a0_casella/33_continuous_distribution.md) — `31n / 38i` 
- [3.4 Exponential families](a0_casella/34_exponential_families.md) — `12n / 15i` 
- [3.5 Location And Scale Families](a0_casella/35_location_and_scale_families.md) — `12n / 17i` 
- [3.6 Inequalities](a0_casella/36_inequalities.md) — `10n / 12i` 
- [4.1 Joint & Marginal Distribution](a0_casella/41_joint_marginal_distribution.md) — `14n / 19i` 
- [4.2 Conditional Distributions & Independent](a0_casella/42_conditional_distributions_independent.md) — `19n / 27i` 
- [4.3 Bivariate Transformation](a0_casella/43_bivariate_transformation.md) — `23n / 24i` 
- [4.4 Hierarchical Model & Mixture Distribution](a0_casella/44_hierarchical_model_mixture_distribution.md) — `11n / 19i` 
- [4.5 Covariance & Correlation](a0_casella/45_covariance_correlation.md) — `20n / 25i` 
- [4.6 Multi-variate Distribution](a0_casella/46_multi_variate_distribution.md) — `24n / 28i` 
- [5.1 Basic Concepts Of Random Samples](a0_casella/51_basic_concepts_of_random_samples.md) — `13n / 16i` 
- [5.2 Σ Of Random Variables From A Random Sample](a0_casella/52_σ_of_random_variables_from_a_random_sample.md) — `22n / 26i` 
- [5.3 Sampling From The Normal Distribution](a0_casella/53_sampling_from_the_normal_distribution.md) — `23n / 29i` 
- [5.4 Order Statistic](a0_casella/54_order_statistic.md) — `13n / 16i` 
- [5.5 Convergence Concepts](a0_casella/55_convergence_concepts.md) — `45n / 52i` 
- [5.6 Generating Random Sample](a0_casella/56_generating_random_sample.md) — `35n / 43i` 
- [6.1 Introduction](a0_casella/61_introduction.md) — `3n / 4i` 
- [6.2 The Sufficient Principle](a0_casella/62_the_sufficient_principle.md) — `47n / 59i` 
- [6.3 The Likelihood Principle](a0_casella/63_the_likelihood_principle.md) — `21n / 23i` 
- [6.4 The Equivariance Principle](a0_casella/64_the_equivariance_principle.md) — `12n / 14i` 
- [7.1 Introduction](a0_casella/71_introduction.md) — `3n / 3i` 
- [7.2 Method Of Finding Estimators](a0_casella/72_method_of_finding_estimators.md) — `48n / 52i` 
- [7.3 Methods Of Evaluating Estimators](a0_casella/73_methods_of_evaluating_estimators.md) — `68n / 73i` 
- [8.1 Introduction](a0_casella/81_introduction.md) — `5n / 5i` 
- [8.2 Method Of Finding Tests](a0_casella/82_method_of_finding_tests.md) — `21n / 26i` 
- [8.3 Methods Of Evaluating Test](a0_casella/83_methods_of_evaluating_test.md) — `53n / 64i` 
- [9.1 Introduction](a0_casella/91_introduction.md) — `9n / 9i` 
- [9.2 Methods Of Finding Interval Estimators](a0_casella/92_methods_of_finding_interval_estimators.md) — `53n / 61i` 
- [9.3 Methods Of Evaluating Interval Estimators](a0_casella/93_methods_of_evaluating_interval_estimators.md) — `36n / 35i` 
- [Chap 10 Asymtotic Evaluation](a0_casella/chap_10_asymtotic_evaluation.md) — `8n / 8i`

### 📂 ISL — Introduction to Statistical Learning (📝 95 Notes | 📸 233 Screenshots)

- [Introduction To Regression](a0_isl/introduction_to_regression.md) — `8n / 6i` 
- [2.1 What Is Statistical Learning?](a0_isl/21_what_is_statistical_learning.md) — `0n / 2i` 
- [2.2 Assessing Model Accuracy](a0_isl/22_assessing_model_accuracy.md) — `7n / 20i` 
- [2.3 Lab](a0_isl/23_lab.md) — `14n / 19i` 
- [2.4 Exercise](a0_isl/24_exercise.md) — `4n / 9i` 
- [2.4 (2) Applied](a0_isl/24_2_applied.md) — `6n / 8i` 
- [3.0 Intro To Linear Regression & Sáu Câu Hỏi](a0_isl/30_intro_to_linear_regression_sáu_câu_hỏi.md) — `0n / 2i` 
- [3.1 Simple Linear Regression](a0_isl/31_simple_linear_regression.md) — `15n / 27i` 
- [3.2 Multiple Linear Regression](a0_isl/32_multiple_linear_regression.md) — `4n / 11i` 
- [3.3 Other Considerations In The Regression Model](a0_isl/33_other_considerations_in_the_regression_model.md) — `4n / 21i` 
- [3.6 Lab: Linear Regression](a0_isl/36_lab_linear_regression.md) — `7n / 9i` 
- [4.3 Logistic Regression](a0_isl/43_logistic_regression.md) — `1n / 8i` 
- [4.4 Generative Models For Classification](a0_isl/44_generative_models_for_classification.md) — `9n / 23i` 
- [4.5 A Comparison Of Classification Methods](a0_isl/45_a_comparison_of_classification_methods.md) — `8n / 17i` 
- [4.6 Generalized Linear Models](a0_isl/46_generalized_linear_models.md) — `1n / 7i` 
- [4.7 Lab: Classification Methods](a0_isl/47_lab_classification_methods.md) — `6n / 17i` 
- [5.1 Cross Validation](a0_isl/51_cross_validation.md) — `1n / 16i` 
- [5.2 The Bootstrap](a0_isl/52_the_bootstrap.md) — `0n / 9i`

### 📂 MIT 18.S096 — Matrix Methods for ML (📝 175 Notes | 📸 176 Screenshots)

- [Lec 1 Part 2 Derivatives As Linear Operator](a0_18s096/lec_1_part_2_derivatives_as_linear_operator.md) — `13n / 13i` 
- [Lec 2 Part 2: Vectorization Of Matrix Function](a0_18s096/lec_2_part_2_vectorization_of_matrix_function.md) — `6n / 3i` 
- [Lec 3 Part 1 Kronecker Products And Jacobians](a0_18s096/lec_3_part_1_kronecker_products_and_jacobians.md) — `29n / 26i` 
- [Lec 3 Part 2 Finite-difference Approximations](a0_18s096/lec_3_part_2_finite_difference_approximations.md) — `24n / 24i` 
- [Lec 4 Part 1: Gradient And Inner Products](a0_18s096/lec_4_part_1_gradient_and_inner_products.md) — `16n / 16i` 
- [Lec 4 Part 2: Nonlinear Rooting Finding,](a0_18s096/lec_4_part_2_nonlinear_rooting_finding.md) — `15n / 17i` 
- [Lec 5 P1: Derivative Of Matrix Determinant And Invers](a0_18s096/lec_5_p1_derivative_of_matrix_determinant_and_invers.md) — `7n / 6i` 
- [Lec 5 P2: Forward Automatic Differentiation Via Dua Numbers](a0_18s096/lec_5_p2_forward_automatic_differentiation_via_dua_numbers.md) — `21n / 23i` 
- [Lec 7 P1: Derivative Of Random Functions](a0_18s096/lec_7_p1_derivative_of_random_functions.md) — `19n / 19i` 
- [Lec 7 P2: Second Derivatives, Bilinear Form, Hessian](a0_18s096/lec_7_p2_second_derivatives_bilinear_form_hessian.md) — `22n / 22i` 
- [Lecture Note](a0_18s096/lecture_note.md) — `2n / 4i` 
- [Problem Sets 1](a0_18s096/problem_sets_1.md) — `1n / 3i`

### 📂 EE263A — Linear Dynamical Systems (📝 84 Notes | 📸 113 Screenshots)

- [Chap 1 Vectors](ee263a/chap_1_vectors.md) — `4n / 6i` 
- [11.1 Left Right Inverse](ee263a/111_left_right_inverse.md) — `7n / 7i` 
- [11.2 Inverse](ee263a/112_inverse.md) — `10n / 9i` 
- [11.3 Solving linear equation](ee263a/113_solving_linear_equation.md) — `5n / 6i` 
- [11.5 Pseudo inverse](ee263a/115_pseudo_inverse.md) — `7n / 9i` 
- [5.1 Linear Independent](ee263a/51_linear_independent.md) — `5n / 6i` 
- [5.2 Basis](ee263a/52_basis.md) — `2n / 4i` 
- [5.3 Orthonormal vectors](ee263a/53_orthonormal_vectors.md) — `4n / 5i` 
- [5.4 Gram-Smidth algorithm](ee263a/54_gram_smidth_algorithm.md) — `3n / 12i` 
- [Chap 12 Least squares](ee263a/chap_12_least_squares.md) — `18n / 24i` 
- [10. Matrix multiplication](ee263a/10_matrix_multiplication.md) — `4n / 5i` 
- [Chap 13 Least square data fitting](ee263a/chap_13_least_square_data_fitting.md) — `15n / 20i`

### 📂 EE364A — Convex Optimization (📝 937 Notes | 📸 1428 Screenshots)

- [Lec 2](a0_ee364a/lec_2.md) — `55n / 71i` 
- [Appendix C](a0_ee364a/appendix_c.md) — `6n / 7i` 
- [Lec 3](a0_ee364a/lec_3.md) — `60n / 76i` 
- [Appendix A](a0_ee364a/appendix_a.md) — `5n / 15i` 
- [Lec 2](a0_ee364a/lec_2.md) — `34n / 49i` 
- [Lec 1](a0_ee364a/lec_1.md) — `7n / 10i` 
- [Untitled](a0_ee364a/untitled.md) — `37n / 56i` 
- [Lec 1](a0_ee364a/lec_1.md) — `51n / 63i` 
- [Lec 4](a0_ee364a/lec_4.md) — `39n / 43i` 
- [Lec 5](a0_ee364a/lec_5.md) — `61n / 82i` 
- [Lec 6](a0_ee364a/lec_6.md) — `31n / 36i` 
- [Lec 7](a0_ee364a/lec_7.md) — `56n / 77i` 
- [Lec 9b](a0_ee364a/lec_9b.md) — `26n / 50i` 
- [Chap 9.5](a0_ee364a/chap_95.md) — `44n / 81i` 
- [Lec 8 B](a0_ee364a/lec_8_b.md) — `37n / 51i` 
- [Chap 10](a0_ee364a/chap_10.md) — `60n / 99i` 
- [Lec 9](a0_ee364a/lec_9.md) — `48n / 64i` 
- [Chap 9.1 - 9.4](a0_ee364a/chap_91_94.md) — `34n / 68i` 
- [Lec 10b](a0_ee364a/lec_10b.md) — `33n / 60i` 
- [Lec 11](a0_ee364a/lec_11.md) — `48n / 92i` 
- [Chap 11.6](a0_ee364a/chap_116.md) — `32n / 60i` 
- [Lec 8 A](a0_ee364a/lec_8_a.md) — `45n / 59i` 
- [Lec 10](a0_ee364a/lec_10.md) — `35n / 64i` 
- [Chap 11:1,2,3,4,5](a0_ee364a/chap_1112345.md) — `53n / 95i`

### 📂 Numerical Optimization — Nocedal & Wright (📝 345 Notes | 📸 481 Screenshots)

- [2.1 Funds of Unconstrained Optim - What's Solution](numerical_optimization/21_funds_of_unconstrained_optim_whats_solution.md) — `15n / 21i` 
- [2.2 Funds of Unconstrained Optim - Overview of Algorithms](numerical_optimization/22_funds_of_unconstrained_optim_overview_of_algorithms.md) — `24n / 35i` 
- [3.1 Line Search Method: Step Length](numerical_optimization/31_line_search_method_step_length.md) — `13n / 20i` 
- [3.2 Line Search Method: Convergence of Line Search Methods](numerical_optimization/32_line_search_method_convergence_of_line_search_methods.md) — `10n / 13i` 
- [3.3 Line Search Method: Rate of Convergence](numerical_optimization/33_line_search_method_rate_of_convergence.md) — `19n / 23i` 
- [3.4 Line Search Method: Newton’s Method with Hessian Modification](numerical_optimization/34_line_search_method_newtons_method_with_hessian_modification.md) — `24n / 29i` 
- [3.5 Line Search Method: Step-Length Selection Algorithms](numerical_optimization/35_line_search_method_step_length_selection_algorithms.md) — `12n / 15i` 
- [4.0 Trust-Region Methods: Outline of the Trust-Region Approach](numerical_optimization/40_trust_region_methods_outline_of_the_trust_region_approach.md) — `12n / 11i` 
- [4.1 Trust-Region Methods: Algorithms Based on the Cauchy Point](numerical_optimization/41_trust_region_methods_algorithms_based_on_the_cauchy_point.md) — `11n / 17i` 
- [4.2 Trust-Region Methods: Global Convergence](numerical_optimization/42_trust_region_methods_global_convergence.md) — `13n / 16i` 
- [4.3 Trust-Region Methods: Iterative Solution of the Subproblem](numerical_optimization/43_trust_region_methods_iterative_solution_of_the_subproblem.md) — `16n / 26i` 
- [4.5 Trust-Region Methods: Other Enhancements](numerical_optimization/45_trust_region_methods_other_enhancements.md) — `5n / 7i` 
- [5.1 Linear Conjugate Gradient](numerical_optimization/51_linear_conjugate_gradient.md) — `23n / 52i` 
- [6.1 The BFGS Method](numerical_optimization/61_the_bfgs_method.md) — `20n / 27i` 
- [6.2 The SR1 Method](numerical_optimization/62_the_sr1_method.md) — `6n / 15i` 
- [6.4 Convergence Analysis](numerical_optimization/64_convergence_analysis.md) — `5n / 6i` 
- [7.1 Inexact Newton Methods](numerical_optimization/71_inexact_newton_methods.md) — `22n / 28i` 
- [7.2 Limited-Memory Quasi-Newton Methods](numerical_optimization/72_limited_memory_quasi_newton_methods.md) — `19n / 23i` 
- [8.1 Finite-Difference
Derivative Approx](numerical_optimization/81_finite_difference_derivative_approx.md) — `20n / 29i` 
- [8.2 Automatic differentiation(*extremely important for AI)](numerical_optimization/82_automatic_differentiationextremely_important_for_ai.md) — `36n / 46i` 
- [10.1 Least-square problem](numerical_optimization/101_least_square_problem.md) — `9n / 10i` 
- [A.1 Error Analysis & Floating-Point Arithmetic](numerical_optimization/a1_error_analysis_floating_point_arithmetic.md) — `8n / 10i`

### 📂 Numerical Optimization — SimpleMind Notes (📝 101 Notes | 📸 128 Screenshots)

- [8.1 Finite-Difference Derivative Approx](numerical_optimization_sm/81_finite_difference_derivative_approx.md) — `21n / 29i` 
- [7.1 Inexact Newton Methods (continue from StudyBoard notebooks)](numerical_optimization_sm/71_inexact_newton_methods_continue_from_studyboard_notebooks.md) — `9n / 10i` 
- [8.2 Automatic Differentiation (*extremely Important For Ai)](numerical_optimization_sm/82_automatic_differentiation_extremely_important_for_ai.md) — `35n / 46i` 
- [10.1 Least-square Problem](numerical_optimization_sm/101_least_square_problem.md) — `8n / 10i` 
- [A.1 Error Analysis & Floating-Point Arithmetic](numerical_optimization_sm/a1_error_analysis_floating_point_arithmetic.md) — `8n / 10i` 
- [7.2 Limited-Memory Quasi-Newton Methods](numerical_optimization_sm/72_limited_memory_quasi_newton_methods.md) — `20n / 23i`

### 📂 Bishop PRML — Pattern Recognition & ML (📝 221 Notes | 📸 294 Screenshots)

- [2.0 Intro](a0_bishop_prml/20_intro.md) — `4n / 5i` 
- [2.1 Binary Variables](a0_bishop_prml/21_binary_variables.md) — `16n / 24i` 
- [2.2 Multinomial Variables](a0_bishop_prml/22_multinomial_variables.md) — `7n / 9i` 
- [2.3 Gaussian Distribution](a0_bishop_prml/23_gaussian_distribution.md) — `16n / 22i` 
- [1.0 Into](a0_bishop_prml/10_into.md) — `8n / 8i` 
- [1.1 Example: Polynomial Curve Fitting](a0_bishop_prml/11_example_polynomial_curve_fitting.md) — `13n / 20i` 
- [1.2.0 Probability theory](a0_bishop_prml/120_probability_theory.md) — `13n / 21i` 
- [1.2.1&2 Probability densities & Expectations Covariances](a0_bishop_prml/1212_probability_densities_expectations_covariances.md) — `14n / 18i` 
- [1.2.3 Bayesian probabilities](a0_bishop_prml/123_bayesian_probabilities.md) — `11n / 14i` 
- [1.2.4 The Gaussian distribution](a0_bishop_prml/124_the_gaussian_distribution.md) — `10n / 14i` 
- [1.2.5 Curve fitting re-visited.](a0_bishop_prml/125_curve_fitting_re_visited.md) — `10n / 11i` 
- [1.2.6 Bayesian curve fitting](a0_bishop_prml/126_bayesian_curve_fitting.md) — `6n / 7i` 
- [1.3 Model Selection](a0_bishop_prml/13_model_selection.md) — `5n / 6i` 
- [1.4 The Curse Of Dimensionality](a0_bishop_prml/14_the_curse_of_dimensionality.md) — `6n / 15i` 
- [1.5 Decision Theory](a0_bishop_prml/15_decision_theory.md) — `31n / 41i` 
- [1.6 Information Theory](a0_bishop_prml/16_information_theory.md) — `26n / 32i` 
- [Appendix D. Calculus of Variation](a0_bishop_prml/appendix_d_calculus_of_variation.md) — `5n / 7i` 
- [Appendix C - Matrices](a0_bishop_prml/appendix_c_matrices.md) — `19n / 20i`

### 📂 CS50X — Programming Foundations (📝 1259 Notes | 📸 1845 Screenshots)

- [Week 0: Scratch](a0_cs50x/week_0_scratch.md) — `81n / 121i` 
- [Week 7: Sql](a0_cs50x/week_7_sql.md) — `129n / 156i` 
- [Week 1: C](a0_cs50x/week_1_c.md) — `107n / 149i` 
- [Week 8: Html Css Js](a0_cs50x/week_8_html_css_js.md) — `116n / 173i` 
- [Week 1: C (short)](a0_cs50x/week_1_c_short.md) — `39n / 55i` 
- [Week 9: Flask](a0_cs50x/week_9_flask.md) — `136n / 178i` 
- [Week 2 Array](a0_cs50x/week_2_array.md) — `101n / 158i` 
- [Week 2 Array (short)](a0_cs50x/week_2_array_short.md) — `4n / 14i` 
- [Week 3 Algorithm](a0_cs50x/week_3_algorithm.md) — `82n / 129i` 
- [Week 4 - Memory](a0_cs50x/week_4_memory.md) — `129n / 175i` 
- [Week 4 - Memory (short)](a0_cs50x/week_4_memory_short.md) — `22n / 43i` 
- [Week 5 - Data Structure](a0_cs50x/week_5_data_structure.md) — `124n / 157i` 
- [Ghi Chú Tay Cho Lab + Problem Set - Week 4 - Memory](a0_cs50x/ghi_chú_tay_cho_lab_problem_set_week_4_memory.md) — `46n / 85i` 
- [Ghi Chú Tay Cho Lab + Problem Set - Week 5 - Data Structure](a0_cs50x/ghi_chú_tay_cho_lab_problem_set_week_5_data_structure.md) — `7n / 44i` 
- [Ghi Chú Tay Cho Lab + Problem Set - Week 7: Sql](a0_cs50x/ghi_chú_tay_cho_lab_problem_set_week_7_sql.md) — `28n / 33i` 
- [Ghi Chú Tay Cho Lab + Problem Set - Week 3 Algorithm](a0_cs50x/ghi_chú_tay_cho_lab_problem_set_week_3_algorithm.md) — `7n / 8i` 
- [Ghi Chú Tay Cho Lab + Problem Set - Week 9: Flask](a0_cs50x/ghi_chú_tay_cho_lab_problem_set_week_9_flask.md) — `16n / 53i` 
- [Ghi Chú Tay Cho Lab + Problem Set - Week 6: Python](a0_cs50x/ghi_chú_tay_cho_lab_problem_set_week_6_python.md) — `8n / 7i` 
- [Week 6: Python](a0_cs50x/week_6_python.md) — `77n / 105i`

### 📂 Deep Learning Specialization (📝 836 Notes | 📸 1826 Screenshots)

- [C1w1_introduction To N.n](a1_dlspec/c1w1_introduction_to_nn.md) — `4n / 24i` 
- [C1w2_n.n Basic](a1_dlspec/c1w2_nn_basic.md) — `64n / 163i` 
- [C1w3_shalow Neural Networks](a1_dlspec/c1w3_shalow_neural_networks.md) — `27n / 91i` 
- [C1w4_deep Neural Network](a1_dlspec/c1w4_deep_neural_network.md) — `20n / 95i` 
- [C4w1_foundations Of Convolutional Neural Network](a1_dlspec/c4w1_foundations_of_convolutional_neural_network.md) — `59n / 117i` 
- [C4w2_deep Convolutional Models: Case Studies](a1_dlspec/c4w2_deep_convolutional_models_case_studies.md) — `57n / 118i` 
- [C4w3_object Detection](a1_dlspec/c4w3_object_detection.md) — `43n / 138i` 
- [C4w4_face Recognition & Neural Style Transfer](a1_dlspec/c4w4_face_recognition_neural_style_transfer.md) — `42n / 105i` 
- [C2w1_practical Aspects Of Deep Learning](a1_dlspec/c2w1_practical_aspects_of_deep_learning.md) — `54n / 121i` 
- [C2w2_optimization Algorithms](a1_dlspec/c2w2_optimization_algorithms.md) — `49n / 96i` 
- [C2w3_hyperparamter Tuning, Batch](a1_dlspec/c2w3_hyperparamter_tuning_batch.md) — `56n / 85i` 
- [C5w1_recurrent Neural Networks](a1_dlspec/c5w1_recurrent_neural_networks.md) — `67n / 165i` 
- [C5w2_natural Language Processing & Word Embeddings](a1_dlspec/c5w2_natural_language_processing_word_embeddings.md) — `39n / 103i` 
- [C5w3_sequence Models & Attention Mechanism](a1_dlspec/c5w3_sequence_models_attention_mechanism.md) — `43n / 116i` 
- [C5w4_transformer Network](a1_dlspec/c5w4_transformer_network.md) — `130n / 202i` 
- [C3w1_machine Learning Strategy 1](a1_dlspec/c3w1_machine_learning_strategy_1.md) — `43n / 47i` 
- [C3w2_machine Learning Strategy 2](a1_dlspec/c3w2_machine_learning_strategy_2.md) — `39n / 40i`

### 📂 CS231N — Computer Vision (📝 1350 Notes | 📸 2073 Screenshots)

- [Lecture 1/16 - Introduction To CNN](a0_cs231n/lecture_116_introduction_to_cnn.md) — `11n / 31i` 
- [Lecture X: Transformer](a0_cs231n/lecture_x_transformer.md) — `42n / 47i` 
- [Assignment 4 - Transformer Image Captioning](a0_cs231n/assignment_4_transformer_image_captioning.md) — `25n / 36i` 
- [Assignment 1 - KNN](a0_cs231n/assignment_1_knn.md) — `31n / 45i` 
- [LECTURE NOTE: Linear classification: Support Vector Machine, Softmax](a0_cs231n/lecture_note_linear_classification_support_vector_machine_softmax.md) — `24n / 21i` 
- [LECTURE NOTE: Optimization: Stochastic Gradient Descent](a0_cs231n/lecture_note_optimization_stochastic_gradient_descent.md) — `19n / 21i` 
- [Assignment 1 SVM](a0_cs231n/assignment_1_svm.md) — `14n / 23i` 
- [Segmentation](a0_cs231n/segmentation.md) — `20n / 24i` 
- [Classification + Localization](a0_cs231n/classification_localization.md) — `8n / 7i` 
- [Object Detection](a0_cs231n/object_detection.md) — `74n / 88i` 
- [Mở Rộng Hơn Nữa](a0_cs231n/mở_rộng_hơn_nữa.md) — `14n / 25i` 
- [Lecture Note Nn P1](a0_cs231n/lecture_note_nn_p1.md) — `1n / 14i` 
- [Note #4 Backpropagation](a0_cs231n/note_4_backpropagation.md) — `9n / 13i` 
- [EECS 498-007/598-005 (2022) - ASSIGNMENT 4 (Part 1):](a0_cs231n/eecs_498_007598_005_2022_assignment_4_part_1.md) — `63n / 118i` 
- [EECS 498-007/598-005 (2022) - ASSIGNMENT 4 (Part 2):](a0_cs231n/eecs_498_007598_005_2022_assignment_4_part_2.md) — `54n / 123i` 
- [Lecture 7/16 - Training Neural Network Ii](a0_cs231n/lecture_716_training_neural_network_ii.md) — `72n / 90i` 
- [Note - Neural Network Part 2](a0_cs231n/note_neural_network_part_2.md) — `46n / 59i` 
- [Note - Neural Network Part 3](a0_cs231n/note_neural_network_part_3.md) — `53n / 61i` 
- [Eecs 498-007_598-005 (2020) Assignment 4 (part 1):](a0_cs231n/eecs_498_007_598_005_2020_assignment_4_part_1.md) — `95n / 158i` 
- [Note - Convolutional Net](a0_cs231n/note_convolutional_net.md) — `23n / 31i` 
- [Assignment 1 - 2 Layer Nn](a0_cs231n/assignment_1_2_layer_nn.md) — `29n / 38i` 
- [Assignment 2 - Fully Connected Nn](a0_cs231n/assignment_2_fully_connected_nn.md) — `40n / 61i` 
- [Eecs 498-007_598-005 (2020) Assignment 4 (part 2):](a0_cs231n/eecs_498_007_598_005_2020_assignment_4_part_2.md) — `25n / 90i` 
- [Paper: Batch normalization](a0_cs231n/paper_batch_normalization.md) — `19n / 32i` 
- [Assignment 2 - Batch Normalization](a0_cs231n/assignment_2_batch_normalization.md) — `19n / 35i` 
- [Lecture 12/16 - Visualization And Understanding](a0_cs231n/lecture_1216_visualization_and_understanding.md) — `63n / 84i` 
- [Assignment 2 - Dropout](a0_cs231n/assignment_2_dropout.md) — `7n / 14i` 
- [Eecs 498-007_598-005 (2020) Assignment 6:](a0_cs231n/eecs_498_007_598_005_2020_assignment_6.md) — `9n / 33i` 
- [Eecs 498-007_598-005 (2020) Assignment 6: Style Transfer](a0_cs231n/eecs_498_007_598_005_2020_assignment_6_style_transfer.md) — `11n / 39i` 
- [Assignment 2 - Pytorch](a0_cs231n/assignment_2_pytorch.md) — `22n / 32i` 
- [Guess Lecture - Adversarial Machine Learning](a0_cs231n/guess_lecture_adversarial_machine_learning.md) — `9n / 12i` 
- [Eecs498-007 Lecture 17: 3d Vision](a0_cs231n/eecs498_007_lecture_17_3d_vision.md) — `49n / 59i` 
- [Eecs498-007 Lecture 18: Video](a0_cs231n/eecs498_007_lecture_18_video.md) — `56n / 66i` 
- [Lecture 9/16 - CNN Architecture](a0_cs231n/lecture_916_cnn_architecture.md) — `62n / 72i` 
- [Lecture 13/16 - Generative Models](a0_cs231n/lecture_1316_generative_models.md) — `82n / 86i` 
- [Lecture 14/16 - Generative Models Ii](a0_cs231n/lecture_1416_generative_models_ii.md) — `45n / 53i` 
- [Eecs 498-007_598-005 (2022) Assignment 6:](a0_cs231n/eecs_498_007_598_005_2022_assignment_6.md) — `20n / 43i` 
- [Lecture Note Introduction To RNN](a0_cs231n/lecture_note_introduction_to_rnn.md) — `14n / 19i` 
- [Eecs 498-007_598-005 (2022) Assignment 6:](a0_cs231n/eecs_498_007_598_005_2022_assignment_6.md) — `21n / 59i` 
- [Assignment 3 - RNN Captioning](a0_cs231n/assignment_3_rnn_captioning.md) — `12n / 49i` 
- [Lecture 14/16 - Deep Reinforcement Learning](a0_cs231n/lecture_1416_deep_reinforcement_learning.md) — `24n / 28i` 
- [Assignment 3 - Lstm Captioning](a0_cs231n/assignment_3_lstm_captioning.md) — `13n / 34i`

### 📂 CS224N — NLP with Deep Learning (📝 665 Notes | 📸 841 Screenshots)

- [Lecture 1 - Intro & Word Vector](a0_cs224n/lecture_1_intro_word_vector.md) — `28n / 45i` 
- [Lecture Note : Introductiont O Word2vec](a0_cs224n/lecture_note_introductiont_o_word2vec.md) — `18n / 21i` 
- [Reading: Efficient Estimation Of Word](a0_cs224n/reading_efficient_estimation_of_word.md) — `9n / 7i` 
- [Reading: Distributed Representations Of Words](a0_cs224n/reading_distributed_representations_of_words.md) — `5n / 4i` 
- [Lecture 2: Neural Classifiers](a0_cs224n/lecture_2_neural_classifiers.md) — `31n / 39i` 
- [Lecture Note: Glove, Evaluation & Training](a0_cs224n/lecture_note_glove_evaluation_training.md) — `25n / 35i` 
- [Assignment 4 - NMT](a0_cs224n/assignment_4_nmt.md) — `26n / 45i` 
- [Assignment 1](a0_cs224n/assignment_1.md) — `18n / 29i` 
- [Lecture 8: Translation, Seq2seq, Attention](a0_cs224n/lecture_8_translation_seq2seq_attention.md) — `10n / 17i` 
- [Lecture 9: Self-attention And Transformers](a0_cs224n/lecture_9_self_attention_and_transformers.md) — `42n / 45i` 
- [Lecture Note - 03 Backpropagation](a0_cs224n/lecture_note_03_backpropagation.md) — `7n / 24i` 
- [Reading](a0_cs224n/reading.md) — `5n / 6i` 
- [Lecture 9: Pretraining](a0_cs224n/lecture_9_pretraining.md) — `43n / 51i` 
- [....a](a0_cs224n/a.md) — `5n / 15i` 
- [Lecture 10: Prompting & RLHF](a0_cs224n/lecture_10_prompting_rlhf.md) — `51n / 63i` 
- [Lecture 12: Natural Language Generation](a0_cs224n/lecture_12_natural_language_generation.md) — `60n / 68i` 
- [Lecture 4: Syntactic Structure And Dependency Parsing](a0_cs224n/lecture_4_syntactic_structure_and_dependency_parsing.md) — `44n / 53i` 
- [Lecture 11: Question & Answering](a0_cs224n/lecture_11_question_answering.md) — `48n / 55i` 
- [Lecture Note 04 - Dependency Parsers](a0_cs224n/lecture_note_04_dependency_parsers.md) — `14n / 17i` 
- [Lecture 13: Coreference Resolution](a0_cs224n/lecture_13_coreference_resolution.md) — `51n / 52i` 
- [Assignment 3 - Dependency Parsing](a0_cs224n/assignment_3_dependency_parsing.md) — `34n / 47i` 
- [Lecture 14: Insights Between NLP And Linguistic](a0_cs224n/lecture_14_insights_between_nlp_and_linguistic.md) — `32n / 38i` 
- [Lecture 5: Recurrent Neural Network](a0_cs224n/lecture_5_recurrent_neural_network.md) — `16n / 21i` 
- [Lecture 15: Add Knowledge To Language Model](a0_cs224n/lecture_15_add_knowledge_to_language_model.md) — `23n / 27i` 
- [Assignment 5: Self-attention, Transformers And Pretraining](a0_cs224n/assignment_5_self_attention_transformers_and_pretraining.md) — `10n / 9i`

### 📂 NLP Specialization (📝 1446 Notes | 📸 2284 Screenshots)

- [C1w1_logistic Regression](a1_nlpspec/c1w1_logistic_regression.md) — `46n / 113i` 
- [C1w2 - Naive Bayes](a1_nlpspec/c1w2_naive_bayes.md) — `57n / 112i` 
- [C1w3 - Vector Space Models](a1_nlpspec/c1w3_vector_space_models.md) — `81n / 122i` 
- [C1w4 - Machine Translation & Document Search](a1_nlpspec/c1w4_machine_translation_document_search.md) — `77n / 115i` 
- [C3w1_neural Networks For Sentiment Analysis](a1_nlpspec/c3w1_neural_networks_for_sentiment_analysis.md) — `73n / 141i` 
- [C3w2_recurrent Neural Networks For Language Modeling](a1_nlpspec/c3w2_recurrent_neural_networks_for_language_modeling.md) — `67n / 138i` 
- [C3W3_LSTMs AND NAMED ENTITY REGCONITION:](a1_nlpspec/c3w3_lstms_and_named_entity_regconition.md) — `64n / 108i` 
- [C3w4 - Siamese Network](a1_nlpspec/c3w4_siamese_network.md) — `73n / 122i` 
- [C2w1_autocorrect](a1_nlpspec/c2w1_autocorrect.md) — `56n / 123i` 
- [C2w2_part Of Speech Tagging And Hidden Markov Models](a1_nlpspec/c2w2_part_of_speech_tagging_and_hidden_markov_models.md) — `146n / 171i` 
- [C2w3_autocomplete And Language Models](a1_nlpspec/c2w3_autocomplete_and_language_models.md) — `128n / 143i` 
- [C3w4_word Embeddings With Neural Networks](a1_nlpspec/c3w4_word_embeddings_with_neural_networks.md) — `134n / 211i` 
- [C4w1_neural Machine Translation](a1_nlpspec/c4w1_neural_machine_translation.md) — `170n / 220i` 
- [C4w2_text Summarization](a1_nlpspec/c4w2_text_summarization.md) — `77n / 145i` 
- [C4w3 - Question Answering](a1_nlpspec/c4w3_question_answering.md) — `119n / 187i` 
- [C4w4_chatbot](a1_nlpspec/c4w4_chatbot.md) — `78n / 113i`

### 📂 LLM — Large Language Models (📝 492 Notes | 📸 504 Screenshots)

- [Generative Ai & Llms](a1_llm/generative_ai_llms.md) — `6n / 6i` 
- [LLM Use Cases And Tasks](a1_llm/llm_use_cases_and_tasks.md) — `9n / 8i` 
- [Text Generation Before Transformers](a1_llm/text_generation_before_transformers.md) — `7n / 9i` 
- [Transformer. Architecture](a1_llm/transformer_architecture.md) — `21n / 23i` 
- [Generating Text With Transformers](a1_llm/generating_text_with_transformers.md) — `7n / 7i` 
- [Prompting And Prompt Engineering](a1_llm/prompting_and_prompt_engineering.md) — `7n / 8i` 
- [Generative Configuration](a1_llm/generative_configuration.md) — `15n / 13i` 
- [Generative Ai Project Lifecycle](a1_llm/generative_ai_project_lifecycle.md) — `9n / 8i` 
- [Lab 1 - Generative Ai Use Case: Summarize Dialogue](a1_llm/lab_1_generative_ai_use_case_summarize_dialogue.md) — `24n / 28i` 
- [Pre-training Large Languguage Models](a1_llm/pre_training_large_languguage_models.md) — `22n / 14i` 
- [Computational Challenges For Training Llms](a1_llm/computational_challenges_for_training_llms.md) — `17n / 13i` 
- [Optional Video: Efficient Multi-gpu Compute Strategies](a1_llm/optional_video_efficient_multi_gpu_compute_strategies.md) — `14n / 11i` 
- [Scaling Laws And Compute-optimal Models](a1_llm/scaling_laws_and_compute_optimal_models.md) — `18n / 12i` 
- [Pre-training For Domain Adaptation](a1_llm/pre_training_for_domain_adaptation.md) — `4n / 6i` 
- [Reading: Domain-specific Training: Bloombertgpt](a1_llm/reading_domain_specific_training_bloombertgpt.md) — `2n / 1i` 
- [Quiz](a1_llm/quiz.md) — `0n / 11i` 
- [Aligning Models With Human Values](a1_llm/aligning_models_with_human_values.md) — `5n / 4i` 
- [RLHF](a1_llm/rlhf.md) — `11n / 6i` 
- [RLHF: Obtaining Feedback From Human](a1_llm/rlhf_obtaining_feedback_from_human.md) — `5n / 4i` 
- [RLHF Reward Model](a1_llm/rlhf_reward_model.md) — `5n / 3i` 
- [RLHF: Fine-tuning With Reinforcement Learning](a1_llm/rlhf_fine_tuning_with_reinforcement_learning.md) — `11n / 6i` 
- [Optional Video: Ppo](a1_llm/optional_video_ppo.md) — `23n / 12i` 
- [Reward Hacking](a1_llm/reward_hacking.md) — `6n / 10i` 
- [Scaling Human Feedback](a1_llm/scaling_human_feedback.md) — `13n / 7i` 
- [Lab3 Walkthrough](a1_llm/lab3_walkthrough.md) — `14n / 16i` 
- [Lab 3 - Fine-tune Flan-t5 To](a1_llm/lab_3_fine_tune_flan_t5_to.md) — `26n / 37i` 
- [Model Optimizations For Deployment](a1_llm/model_optimizations_for_deployment.md) — `13n / 8i` 
- [Using The LLM Applications](a1_llm/using_the_llm_applications.md) — `8n / 12i` 
- [Interacting With External Applications](a1_llm/interacting_with_external_applications.md) — `5n / 5i` 
- [Helping Llms Reason And Plan With Chain Of Thought](a1_llm/helping_llms_reason_and_plan_with_chain_of_thought.md) — `5n / 5i` 
- [Program-aided Language Model (pal)](a1_llm/program_aided_language_model_pal.md) — `8n / 9i` 
- [React: Combining Reasoning And Action](a1_llm/react_combining_reasoning_and_action.md) — `3n / 11i` 
- [Quiz](a1_llm/quiz.md) — `0n / 10i` 
- [Fine-tuning With Instruction](a1_llm/fine_tuning_with_instruction.md) — `55n / 53i` 
- [Parameter Efficient Fine-tuning](a1_llm/parameter_efficient_fine_tuning.md) — `92n / 103i`

