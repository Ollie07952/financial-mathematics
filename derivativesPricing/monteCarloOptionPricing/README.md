# Monte Carlo Option Pricing

### Introduction

This projects introduces foundational concepts from risk-neutral option pricing through the discrete time binomial model, as proposed by Cox, Ross, and Rubinstein in their 1979 paper \[1]. We also explore the applications of a Monte Carlo method for pricing options, including convergence to the analytical solution (when it exists) and inherent utility of such methods for more exotic contracts. Finally, we briefly discuss extensions of these methods to the continuous-time setting where we observe analytical solutions are rare and bolster the case for the Monte Carlo method as an effective pricing tool.

### Project Structure

* *Risk-Neutral\_Pricing\_and\_Monte\_Carlo\_Methods.tex* — Written report .tex covering risk-neutral option pricing, discrete time binomial models, and Monte Carlo pricing methods.
* *\\figuresTables* — Copies of figures and tables used in the report .tex, for reproducibility purposes.
* *Risk-Neutral\_Pricing\_and\_Monte\_Carlo\_Methods.pdf* — A .pdf copy of the above .tex file.
* *Discrete\_Monte\_Carlo\_Pricing.ipynb* — Accompanying Jupyter notebook containing analytical and convergence experiments used to produce figures in the written report. Includes multiperiod binomial models with analytical pricing computations, Monte Carlo convergence plots and tables, and Monte Carlo pricing methods for both European and Asian contracts.

### Bibliography

\[1] John C. Cox, Stephen A. Ross, and Mark Rubinstein. “Option pricing: A simplified approach”. In: Journal of Financial Economics 7.3 (1979), pp. 229–263. issn: 0304-405X. doi: https://doi.org/10.1016/0304-405X(79)90015-1.

\[2] Steven E. Shreve. Stochastic Calculus for Finance I: The Binomial Asset Pricing Model. Springer, 2004. isbn: 978-0387249681.

\[3] A.G.Z. Kemna and A.C.F. Vorst. “A pricing method for options based on average asset values”. In: Journal of Banking and Finance 14.1 (1990), pp. 113–129. issn: 0378-4266. doi: https://doi.org/10.1016/0378-4266(90)90039-5.

\[4] Fischer Black and Myron Scholes. “The Pricing of Options and Corporate Liabilities”. In: Journal of Political Economy 81.3 (1973), pp. 637–654. issn: 00223808, 1537534X. url: http://www.jstor.org/stable/1831029.

### Disclaimer

All materials herein are intended solely for educational purposes and not financial advice, trading, or decision making in any capacity.

### Contact
Regarding any queries, bug reports, or suggestions please reach out via email at: o.cole1-24@student.lboro.ac.uk.
