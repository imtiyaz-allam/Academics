# Assignment 2
## 1. Find the values of x for which the function $f(x) = \frac{x ^ 2 - 3x - 4}{x^2+3x - 4}$ is NOT continuous

The function is

$$
f(x)=\frac{x^{2}-3x-4}{x^{2}+3x-4}.
$$

A rational function is discontinuous only where its denominator is zero.

Solve $x^{2}+3x-4=0$:

$$
x^{2}+3x-4=(x+4)(x-1)=0 \;\Rightarrow\; x=-4 \text{ or } x=1.
$$

Therefore, $f(x)$ is **not continuous at $x=-4$ and $x=1$** (vertical asymptotes).

## 2. Find the range of value of $k$ for which the function $f(x) = (k ^ 2- 4)x ^ 2+ 6x ^ 3 + 8x ^ 4$ has a local maxima at point $x=0$
Let $f(x)= (k^{2}-4)x^{2}+6x^{3}+8x^{4}$.

* $f'(x)=2(k^{2}-4)x+18x^{2}+32x^{3}\Rightarrow f'(0)=0$ for all $k$.
* $f''(x)=2(k^{2}-4)+36x+96x^{2}\Rightarrow f''(0)=2(k^{2}-4)$.

For a local **maximum** at $x=0$, we need $f''(0)<0$:

$$
2(k^{2}-4)<0 \;\;\Longrightarrow\;\; k^{2}<4 \;\;\Longrightarrow\;\; -2<k<2.
$$

(At $k=\pm2$, $f(x)=6x^{3}+8x^{4}$, which has an inflection at $0$, not a max.)

$$
\boxed{-2<k<2}
$$

## 3. The quantity of charge $Q$ in columb (C)that has passed through a point in a wire upto time $t$ (measured in seconds) is given by $Q(t) = t^3 - 2t ^ 2+ 6t + 2$.Find the current when (a) $t = 0.5s$ and (b) $t=1s$. At what time is the current lowest?
Given $Q(t)=t^{3}-2t^{2}+6t+2$ (C), the current is

$$
I(t)=\frac{dQ}{dt}=3t^{2}-4t+6 \quad (\text{A}).
$$

(a) At $t=0.5\ \text{s}$:

$$
I(0.5)=3(0.5)^2-4(0.5)+6=0.75-2+6=4.75\ \text{A}.
$$

(b) At $t=1\ \text{s}$:

$$
I(1)=3(1)^2-4(1)+6=3-4+6=5\ \text{A}.
$$

Lowest current: Since $I(t)=3t^{2}-4t+6$ is a convex quadratic, its minimum occurs at

$$
t^*=\frac{-(-4)}{2\cdot 3}=\frac{4}{6}=\frac{2}{3}\ \text{s},
$$

with minimum value

$$
I_{\min}=I\!\left(\tfrac{2}{3}\right)=3\left(\tfrac{4}{9}\right)-4\left(\tfrac{2}{3}\right)+6
=\tfrac{4}{3}-\tfrac{8}{3}+\tfrac{18}{3}=\tfrac{14}{3}\approx 4.667\ \text{A}.
$$

**Answer:**
(a) $4.75\ \text{A}$, (b) $5\ \text{A}$; current is lowest at $t=\tfrac{2}{3}\ \text{s}$ with value $\tfrac{14}{3}\ \text{A}$.

## 4. Use logarithmic definitions to find the derivative of the $y = (ln ~ x) ^ {cos ~ x}$.
We need derivative of

$$
y=(\ln x)^{\cos x}.
$$


### Step 1: Take logarithm

$$
\ln y = \cos x \cdot \ln(\ln x).
$$

### Step 2: Differentiate both sides

$$
\frac{1}{y}\frac{dy}{dx} = \frac{d}{dx}\big[\cos x \cdot \ln(\ln x)\big].
$$

Use product rule:

$$
\frac{d}{dx}[\cos x \cdot \ln(\ln x)] = (-\sin x)\ln(\ln x) + \cos x \cdot \frac{1}{\ln x}\cdot \frac{1}{x}.
$$

So,

$$
\frac{1}{y}\frac{dy}{dx} = -\sin x \ln(\ln x) + \frac{\cos x}{x \ln x}.
$$

### Step 3: Multiply by $y$

$$
\frac{dy}{dx} = (\ln x)^{\cos x}\Bigg[-\sin x \ln(\ln x) + \frac{\cos x}{x \ln x}\Bigg].
$$

 **Final Answer:**

$$
\boxed{\;\;\frac{dy}{dx}=(\ln x)^{\cos x}\left(-\sin x \,\ln(\ln x) + \frac{\cos x}{x \ln x}\right)\;}
$$

## 5. Use implicit differentiation to find an equation of the tangent line to the curve $x ^ 2 + 2xy - y^2+ x = 2$ at the given point $(1, 2)$
Differentiate the equation implicitly:

$$
x^{2}+2xy-y^{2}+x=2.
$$

Differentiate both sides w\.r.t. $x$:

$$
2x + \big(2y+2x\,y'\big) - 2y\,y' + 1 = 0.
$$

Collect $y'$ terms:

$$
(2x-2y)y' + (2x+2y+1)=0
\quad\Rightarrow\quad
y' = -\frac{2x+2y+1}{2x-2y}.
$$

Evaluate at the point $(1,2)$:

$$
y'|_{(1,2)} = -\frac{2(1)+2(2)+1}{2(1)-2(2)} = -\frac{7}{-2}=\frac{7}{2}.
$$

Tangent line with slope $m=\tfrac72$ through $(1,2)$:

$$
y-2=\frac{7}{2}(x-1)
\quad\text{or}\quad
\boxed{\,y=\frac{7}{2}x-\frac{3}{2}\,}.
$$

## 6. Find the local and absolute extreme values of the function $f(x) = x ^ 2 e ^ {-x}$, on the given interval $[-1,3]$.

$f(x)=x^{2}e^{-x}$ on $[-1,3]$.

1. Derivative:

$$
f'(x)=\frac{d}{dx}\big(x^{2}e^{-x}\big)=e^{-x}(2x-x^{2})=e^{-x}\,x(2-x).
$$

Critical points where $f'(x)=0$: $x=0$ and $x=2$. (Note $e^{-x}>0$ never zero.)

2. Evaluate $f$ at critical points and endpoints:

$$
\begin{aligned}
f(-1)&=(-1)^{2}e^{1}=e\approx 2.71828,\\
f(0)&=0^{2}e^{0}=0,\\
f(2)&=2^{2}e^{-2}=4e^{-2}\approx 0.54134,\\
f(3)&=3^{2}e^{-3}=9e^{-3}\approx 0.44726.
\end{aligned}
$$

3. Classify local behavior (or use sign of $f'$):

* For $x<0$ (e.g. $-0.5$) $f'(x)<0$ so $f$ is decreasing to $x=0$.
* For $0<x<2$ $f'(x)>0$ so $f$ increases on $(0,2)$. Hence $x=0$ is a **local minimum** (value $0$).
* For $x<2$ but $>0$ slope positive and for $x>2$ slope negative, so $x=2$ is a **local maximum** (value $4e^{-2}\approx0.54134$).

4. Absolute extrema on $[-1,3]$ (compare values):

* **Absolute maximum:** $f(-1)=e$ at $x=-1$.
* **Absolute minimum:** $f(0)=0$ at $x=0$.

---

**Final answers**

* Local minimum: $x=0$, value $f(0)=0$.
* Local maximum: $x=2$, value $f(2)=4e^{-2}\approx0.54134$.
* Absolute maximum on $[-1,3]$: $x=-1$, value $f(-1)=e\approx2.71828$.
* Absolute minimum on $[-1,3]$: $x=0$, value $0$.

## 7. Find the volume of the largest circular cone that can be inscribed in a sphere of radius $r$.
We want the largest volume of a right circular cone inscribed in a sphere of radius $r$.

Place the sphere with center $O$ at the origin and the cone axis vertical. Let the cone apex be at the topmost point of the sphere and let the base plane be a distance $d$ below the center (so $0\le d\le r$). Then

* the cone height is $h=r+d$ (apex is $r$ above the center, base plane is $d$ below),
* the base radius $a$ satisfies $a^{2}+d^{2}=r^{2}$, so $a^{2}=r^{2}-d^{2}$.

The cone volume is

$$
V(d)=\frac{1}{3}\pi a^{2}h=\frac{1}{3}\pi (r^{2}-d^{2})(r+d).
$$

Expand (optional) and differentiate:

$$
V(d)=\frac{1}{3}\pi\big(r^{3}+r^{2}d-rd^{2}-d^{3}\big),
$$

$$
V'(d)=\frac{1}{3}\pi\big(r^{2}-2rd-3d^{2}\big).
$$

Set $V'(d)=0$:

$$
r^{2}-2rd-3d^{2}=0 \quad\Longrightarrow\quad 3d^{2}+2rd-r^{2}=0.
$$

Solve: $d=\dfrac{-2r\pm\sqrt{4r^{2}+12r^{2}}}{6}=\dfrac{-2r\pm4r}{6}$. The admissible positive root is

$$
d=\frac{r}{3}.
$$

Check this gives a maximum (second derivative $V''(d)=\frac{1}{3}\pi(-2r-6d)$, which at $d=r/3$ is negative), so it is a maximum.

Compute the cone dimensions at this $d$:

$$
h=r+d=r+\frac{r}{3}=\frac{4r}{3},\qquad
a^{2}=r^{2}-\frac{r^{2}}{9}=\frac{8}{9}r^{2}.
$$

Thus the maximal volume is

$$
V_{\max}=\frac{1}{3}\pi a^{2}h
=\frac{1}{3}\pi\cdot\frac{8}{9}r^{2}\cdot\frac{4r}{3}
=\frac{32}{81}\pi\,r^{3}.
$$

$$
\boxed{V_{\text{max}}=\frac{32}{81}\pi r^{3}}
$$

(Attained when the base plane is a distance $\frac{r}{3}$ below the sphere center; cone height $\frac{4r}{3}$, base radius $\tfrac{2\sqrt{2}}{3}r$.)

## 8. Verify that the function $f(x) = x ^ 3 - x ^ 2 - 6x + 2$ satisfies the three hypotheses of Rolle's Theorem on $[0, 3]$. Then find all number $c$ that satisfy the conclusion of Rolle's Theorem
<u>**Step 1**</u> — Check the three hypotheses of Rolle’s theorem on $[0,3]$.

1. $f$ is continuous on $[0,3]$:
   $f(x)=x^{3}-x^{2}-6x+2$ is a polynomial, hence continuous everywhere (in particular on $[0,3]$).

2. $f$ is differentiable on $(0,3)$:
   Polynomials are differentiable everywhere, so $f$ is differentiable on $(0,3)$.

3. $f(0)=f(3)$:

   $$
   f(0)=0-0-0+2=2,\qquad
   f(3)=27-9-18+2=2.
   $$

   So $f(0)=f(3)$.

All three hypotheses are satisfied, so Rolle’s theorem applies: there exists at least one $c\in(0,3)$ with $f'(c)=0$.

---

<u>**Step 2**</u> — Find all $c\in(0,3)$ with $f'(c)=0$.

Compute the derivative:

$$
f'(x)=3x^{2}-2x-6.
$$

Solve $3x^{2}-2x-6=0$. The quadratic formula gives

$$
x=\frac{2\pm\sqrt{(-2)^{2}-4\cdot3\cdot(-6)}}{2\cdot3}
=\frac{2\pm\sqrt{4+72}}{6}
=\frac{2\pm\sqrt{76}}{6}
=\frac{2\pm 2\sqrt{19}}{6}
=\frac{1\pm\sqrt{19}}{3}.
$$

Numerical values:

$$
\frac{1-\sqrt{19}}{3}\approx -1.1196\quad(\text{not in }(0,3)),
\qquad
\frac{1+\sqrt{19}}{3}\approx 1.7863\quad(\text{in }(0,3)).
$$

Thus the only $c$ in $(0,3)$ satisfying Rolle’s conclusion is

$$
\boxed{\,c=\dfrac{1+\sqrt{19}}{3}\, }.
$$

## 9.  Let $f(x) = sin ~ x + cos ~ x$,  $0 \le x \le 2$ . Find the intervals in which $f$ is increasing or decreasing. Find the local maximum and minimum values of $f$. Find the intervals of concavity and the in inflection point of $f$.

$$
f(x)=\sin x+\cos x.
$$

### 1. First derivative and critical points

$$
f'(x)=\cos x-\sin x=\sqrt{2}\cos\!\left(x+\frac{\pi}{4}\right).
$$

Solve $f'(x)=0$:

$$
\cos\!\left(x+\frac{\pi}{4}\right)=0\quad\Longrightarrow\quad
x+\frac{\pi}{4}=\frac{\pi}{2}+n\pi
$$

so

$$
x=\frac{\pi}{4}+n\pi.
$$

On $[0,2\pi]$ the critical points are

$$
x=\frac{\pi}{4},\qquad x=\frac{5\pi}{4}.
$$

Sign of $f'$: since $f'(x)=\sqrt{2}\cos(x+\pi/4)$,

* $f'(x)>0$ when $\cos(x+\pi/4)>0$, i.e. $x\in(-3\pi/4+2k\pi,\ \pi/4+2k\pi)$.
* $f'(x)<0$ when $\cos(x+\pi/4)<0$, i.e. $x\in(\pi/4+2k\pi,\ 5\pi/4+2k\pi)$.

Intersecting with $[0,2\pi]$ gives:

**Increasing:** $0\le x<\dfrac{\pi}{4}$ and $\dfrac{5\pi}{4}<x\le 2\pi$.
**Decreasing:** $\dfrac{\pi}{4}<x<\dfrac{5\pi}{4}$.

(At $x=\pi/4$ and $x=5\pi/4$, $f'(x)=0$.)

### 2. Local maxima and minima

Evaluate $f$ at the critical points:

$$
f\!\big(\tfrac{\pi}{4}\big)=\sin\frac{\pi}{4}+\cos\frac{\pi}{4}=\frac{\sqrt2}{2}+\frac{\sqrt2}{2}=\sqrt2,
$$

$$
f\!\big(\tfrac{5\pi}{4}\big)=\sin\frac{5\pi}{4}+\cos\frac{5\pi}{4}=-\frac{\sqrt2}{2}-\frac{\sqrt2}{2}=-\sqrt2.
$$

Because $f'$ changes $+\to-$ at $x=\pi/4$, $x=\pi/4$ is a **local maximum** with value $\sqrt2$.
Because $f'$ changes $-\to+$ at $x=5\pi/4$, $x=5\pi/4$ is a **local minimum** with value $-\sqrt2$.

Also note endpoint values: $f(0)=1$ and $f(2\pi)=1$. So the global (absolute) max on $[0,2\pi]$ is $\sqrt2$ at $x=\pi/4$, and the absolute min is $-\sqrt2$ at $x=5\pi/4$.

### 3. Concavity and inflection points

Second derivative:

$$
f''(x)=-\sin x-\cos x=-\sqrt{2}\sin\!\left(x+\frac{\pi}{4}\right).
$$

Inflection points satisfy $f''(x)=0$, so

$$
\sin\!\left(x+\frac{\pi}{4}\right)=0\quad\Longrightarrow\quad
x+\frac{\pi}{4}=n\pi,
$$

hence

$$
x=\frac{3\pi}{4},\qquad x=\frac{7\pi}{4}\quad\text{(on }[0,2\pi]\text{)}.
$$

Sign of $f''$:

* $f''(x)<0$ (concave down) when $\sin(x+\pi/4)>0$, i.e. $x\in(-\tfrac{\pi}{4}+2k\pi,\tfrac{3\pi}{4}+2k\pi)$.
* $f''(x)>0$ (concave up) when $\sin(x+\pi/4)<0$, i.e. $x\in(\tfrac{3\pi}{4}+2k\pi,\tfrac{7\pi}{4}+2k\pi)$.

Intersect with $[0,2\pi]$:

**Concave down:** $0\le x<\dfrac{3\pi}{4}$ and $\dfrac{7\pi}{4}<x\le 2\pi$.

**Concave up:** $\dfrac{3\pi}{4}<x<\dfrac{7\pi}{4}$.

Inflection points at $x=\dfrac{3\pi}{4}$ and $x=\dfrac{7\pi}{4}$. Their function values:

$$
f\!\big(\tfrac{3\pi}{4}\big)=\sin\frac{3\pi}{4}+\cos\frac{3\pi}{4}=\frac{\sqrt2}{2}-\frac{\sqrt2}{2}=0,
$$

$$
f\!\big(\tfrac{7\pi}{4}\big)=\sin\frac{7\pi}{4}+\cos\frac{7\pi}{4}=-\frac{\sqrt2}{2}+\frac{\sqrt2}{2}=0.
$$

## 10.  Use Newtons method to approximate the positive root of the equation $sin ~ x = x ^ 2$ correct to six decimal places.
Nice — here are the step-by-step Newton iterations and the conclusion.

Problem setup
We solve $\sin x = x^2$. Put $g(x)=\sin x - x^2$. Newton’s iteration:

$$
x_{n+1}=x_n-\frac{g(x_n)}{g'(x_n)},\qquad g'(x)=\cos x-2x.
$$

Start with $x_0=0.9$. Stopping rule: stop when $|x_{n+1}-x_n|<5\times10^{-7}$ (this guarantees correctness to 6 decimal places).

Iteration table (shown step-by-step)

* n = iteration number
* $x_n$ = current iterate
* $g(x_n)$, $g'(x_n)$
* dx = $\frac{g(x_n)}{g'(x_n)}$
* $x_{n+1}$ = next iterate
* $|x_{n+1} - x_n|$

You can see the printed table above. The iterations produced:

n=0: $x_0=0.900000000000000$ → $x_1=0.877364803117544$<br>
n=1: $x_1=0.877364803117544$ → $x_2=0.876726721490962$<br>
n=2: $x_2=0.876726721490962$ → $x_3=0.876726215395381$<br>
n=3: $x_3=0.876726215395381$ → $x_4=0.876726215395062$<br>(change $<3.2\times10^{-13}$)

Final result

* Converged root (high precision): $x \approx 0.876726215395062$.
* Value of $g(x)$ at the root $\approx 1.11\times 10^{-16}$ (numerical zero).
* Rounded to **six decimal places**:

$$
\boxed{\,x \approx 0.876726\,}
$$
