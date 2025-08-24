# Assignment 1
## 1. Show that the equation represents a sphere,and find its center and radius $x ^ 2 + y ^ 2 + z ^ 2 + 8x -6y + 2z + 17 = 0$.
We’re asked to show that

$$
x^{2}+y^{2}+z^{2}+8x-6y+2z+17=0
$$

represents a sphere and then find its center and radius.


### Step 1. Group terms

$$
(x^2+8x) + (y^2-6y) + (z^2+2z) + 17 = 0.
$$

### Step 2. Complete the square for each variable

* For $x^2+8x$:

$$
x^2+8x = (x+4)^2 - 16.
$$

* For $y^2-6y$:

$$
y^2-6y = (y-3)^2 - 9.
$$

* For $z^2+2z$:

$$
z^2+2z = (z+1)^2 - 1.
$$

### Step 3. Substitute back

$$
(x+4)^2 -16 + (y-3)^2 -9 + (z+1)^2 -1 +17 = 0.
$$

Simplify constants: $-16-9-1+17=-9.$

So

$$
(x+4)^2+(y-3)^2+(z+1)^2 -9 = 0.
$$

### Step 4. Rewrite in standard sphere form

$$
(x+4)^2+(y-3)^2+(z+1)^2 = 9.
$$

### Conclusion

This is a sphere with

* **Center**: $(-4,\,3,\,-1)$
* **Radius**: $r=\sqrt{9}=3$.

$$
\boxed{\text{Sphere centered at }(-4,3,-1)\text{ with radius }3.}
$$

## 2. Find an equation of a sphere if one of its diameters has endpoint $(2,1,4)$ and $(4,3,10)$
We’re asked for the equation of a sphere if one of its diameters has endpoints $(2,1,4)$ and $(4,3,10)$.

### Step 1. Find the center

The center of the sphere is the **midpoint of the diameter**:

$$
C=\left(\frac{2+4}{2}, \frac{1+3}{2}, \frac{4+10}{2}\right)=(3,2,7).
$$

### Step 2. Find the radius

The radius is half the length of the diameter.

Diameter length:

$$
d=\sqrt{(4-2)^2+(3-1)^2+(10-4)^2}=\sqrt{2^2+2^2+6^2}=\sqrt{4+4+36}=\sqrt{44}.
$$

So the radius is

$$
r=\frac{\sqrt{44}}{2}=\sqrt{11}.
$$

### Step 3. Write the equation

General sphere equation:

$$
(x-x_0)^2+(y-y_0)^2+(z-z_0)^2=r^2.
$$

Here:

$$
(x-3)^2+(y-2)^2+(z-7)^2=11.
$$
**Final Answer:**

$$
\boxed{(x-3)^2+(y-2)^2+(z-7)^2=11}
$$

## 3. What is the angle between the vector $8i+6j$ and the positive direction of the x-axis.
We want the angle $\theta$ between the vector $\mathbf{v} = 8\mathbf{i} + 6\mathbf{j}$ and the positive $x$-axis.

### Step 1. Recall formula

The angle a vector $(x,y)$ makes with the positive $x$-axis is

$$
\theta = \arctan\!\left(\frac{y}{x}\right),
$$

assuming $x>0$.

### Step 2. Substitute components

Here $x=8,\; y=6$.

$$
\theta = \arctan\!\left(\frac{6}{8}\right) = \arctan\!\left(\tfrac{3}{4}\right).
$$

### Step 3. Value

$$
\theta \approx 36.87^\circ \quad \text{(or in radians: } 0.6435\text{ rad)}.
$$
**Final Answer:**
The angle is

$$
\boxed{\arctan\!\left(\tfrac{3}{4}\right) \;\approx\; 36.87^\circ \approx 0.643501 ~ Rad}
$$

## 4. State whether the given vectors $a=\langle 4,6\rangle, b=\langle 3,2\rangle$. are orthogonal, parallel, or neither
We’re asked about

$$
\mathbf{a}=\langle 4,6\rangle,\quad \mathbf{b}=\langle 3,2\rangle.
$$

---

### Step 1. Test for orthogonality

Vectors are orthogonal if $\mathbf{a}\cdot \mathbf{b}=0$.

$$
\mathbf{a}\cdot\mathbf{b}=4\cdot 3+6\cdot 2=12+12=24\neq0.
$$

So they are **not orthogonal**.

---

### Step 2. Test for parallelism

Vectors are parallel if one is a scalar multiple of the other.
Check ratios:

$$
\frac{4}{3}\neq \frac{6}{2}.
$$

So they are **not parallel**.

---

### Conclusion

$$
\boxed{\text{The vectors are neither orthogonal nor parallel.}}
$$

## 5. If a vector has direction angles $\alpha=\frac{\pi}{4}, \beta=\frac{\pi}{3}$, find the third direction angle $\gamma$.
We are asked to find the third direction angle $\gamma$ of a 3D vector when two direction angles are known:

$$
\alpha=\frac{\pi}{4},\quad \beta=\frac{\pi}{3}.
$$


### Step 1. Recall relation between direction cosines

If a vector makes angles $\alpha,\beta,\gamma$ with the $x$-, $y$-, and $z$-axes, then its **direction cosines** are

$$
l=\cos\alpha,\quad m=\cos\beta,\quad n=\cos\gamma
$$

and they satisfy

$$
l^2+m^2+n^2=1.
$$


### Step 2. Plug in known values

$$
l=\cos\left(\tfrac{\pi}{4}\right)=\tfrac{\sqrt{2}}{2}, \qquad 
m=\cos\left(\tfrac{\pi}{3}\right)=\tfrac{1}{2}.
$$

So

$$
\left(\tfrac{\sqrt{2}}{2}\right)^2+\left(\tfrac{1}{2}\right)^2+n^2=1.
$$

### Step 3. Simplify

$$
\frac{1}{2}+\frac{1}{4}+n^2=1
\;\;\;\Rightarrow\;\;\; \frac{3}{4}+n^2=1
\;\;\;\Rightarrow\;\;\; n^2=\frac{1}{4}.
$$

So

$$
n=\pm \frac{1}{2}.
$$


### Step 4. Find $\gamma$

$$
\cos\gamma=\pm \tfrac{1}{2}.
$$

Thus

$$
\gamma=\frac{\pi}{3}\quad\text{or}\quad \gamma=\frac{2\pi}{3}.
$$
**Final Answer:**
The third direction angle is $\boxed{\;\gamma=\tfrac{\pi}{3}\;\text{ or }\;\gamma=\tfrac{2\pi}{3}\;}$ depending on the orientation of the vector.

## 6. Use the scalar triple product to verify that the vectors $u = i + 5j - 2k$, $v = 3i - j$ ,and $w = 5i + 9j - 4k$ are coplanar.
We are asked to check whether vectors

$$
u = \langle 1,5,-2\rangle,\quad v=\langle 3,-1,0\rangle,\quad w=\langle 5,9,-4\rangle
$$

are **coplanar** using the scalar triple product.

---

### Step 1. Recall definition

The scalar triple product is

$$
[u,v,w] = u \cdot (v \times w).
$$

If this equals $0$, then the vectors are coplanar.

---

### Step 2. Compute $v \times w$

$$
v \times w = 
\begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
3 & -1 & 0 \\
5 & 9 & -4
\end{vmatrix}.
$$

Expand:

$$
v \times w = \mathbf{i}[(-1)(-4) - (0)(9)] - \mathbf{j}[3(-4) - (0)(5)] + \mathbf{k}[3(9) - (-1)(5)].
$$

$$
= \mathbf{i}[4-0] - \mathbf{j}[-12-0] + \mathbf{k}[27+5].
$$

$$
= 4\mathbf{i} + 12\mathbf{j} + 32\mathbf{k}.
$$

So

$$
v \times w = \langle 4, 12, 32\rangle.
$$

---

### Step 3. Dot with $u$

$$
u \cdot (v \times w) = \langle 1,5,-2\rangle \cdot \langle 4,12,32\rangle.
$$

$$
= (1)(4) + (5)(12) + (-2)(32).
$$

$$
= 4 + 60 - 64 = 0.
$$

---

### Step 4. Conclusion

Since the scalar triple product is zero, $\boxed{\text{The vectors are coplanar.}}$

## 7.  Find symmetric equation for line of intersection of the planes $z = 2x - y - 5$, $z = 4x + 3y - 5$.
To find the symmetric equation of the line of intersection of the two planes, we follow these steps:

### Given Planes:

1. $z = 2x - y - 5$
2. $z = 4x + 3y - 5$

### Step 1: Set the equations equal to each other

Since both expressions equal $z$, we set them equal to each other to eliminate $z$.

$$
2x - y - 5 = 4x + 3y - 5
$$

Simplify the equation:

$$
2x - y = 4x + 3y
$$

$$
2x - 4x = 3y + y
$$

$$
-2x = 4y
$$

$$
x = -2y
$$

### Step 2: Express $x$ in terms of $y$

From the above, we have $x = -2y$. Now we substitute this expression into one of the original plane equations.

### Step 3: Substitute $x = -2y$ into one of the plane equations (e.g., $z = 2x - y - 5$)

Substitute $x = -2y$ into $z = 2x - y - 5$:

$$
z = 2(-2y) - y - 5
$$

$$
z = -4y - y - 5
$$

$$
z = -5y - 5
$$

Now we have parametric expressions for $x$, $y$, and $z$ in terms of $y$:

$$
x = -2y
$$

$$
z = -5y - 5
$$

### Step 4: Write the parametric equations for the line

Now that we have expressions for $x$ and $z$ in terms of $y$, we can write the parametric equations for the line of intersection:

$$
x = -2y
$$

$$
y = y \quad (\text{Let} \, y = t)
$$

$$
z = -5y - 5 \quad \text{or} \quad z = -5t - 5
$$

Thus, the parametric equations for the line of intersection are:

$$
x = -2t
$$

$$
y = t
$$

$$
z = -5t - 5
$$

### Step 5: Convert to symmetric form

To write the symmetric equations, we solve for $t$ in each of the parametric equations:

$$
t = -\frac{x}{2}
$$

$$
t = y
$$

$$
t = \frac{z + 5}{-5}
$$

Thus, the symmetric equation for the line of intersection is:

$$
\frac{x}{-2} = y = \frac{z + 5}{-5}
$$

This is the symmetric form of the line of intersection of the two planes.

## 8. Find the equation of the normal plane and osculating plane of the curve $x=2\sin{3t}$, $y=t$ and $z=2\cos{3t}$ at $(0,\pi, -2)$.
The parametric curve is

$$
\mathbf{r}(t)=\langle 2\sin(3t),\; t,\; 2\cos(3t)\rangle.
$$

Compute derivatives and evaluate at $t=\pi$:

$$
\mathbf{r}'(t)=\langle 6\cos(3t),\;1,\;-6\sin(3t)\rangle,\qquad
\mathbf{r}''(t)=\langle -18\sin(3t),\;0,\;-18\cos(3t)\rangle.
$$

At $t=\pi$ (where $\cos(3\pi)=-1,\ \sin(3\pi)=0$):

$$
\mathbf{r}'(\pi)=\langle -6,\,1,\,0\rangle,\qquad
\mathbf{r}''(\pi)=\langle 0,\,0,\,18\rangle.
$$

Tangent vector (direction) at the point is $\mathbf{r}'(\pi)=\langle -6,1,0\rangle$.
The binormal (normal to the osculating plane) is proportional to

$$
\mathbf{B}=\mathbf{r}'(\pi)\times\mathbf{r}''(\pi)
=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\-6&1&0\\0&0&18\end{vmatrix}
=\langle 18,\,108,\,0\rangle
=18\langle 1,6,0\rangle.
$$

We may use $\langle 1,6,0\rangle$ as the normal to the osculating plane.

### Normal plane

The normal plane at a point is the plane **perpendicular to the tangent vector** (so its normal is $\mathbf{r}'(\pi)$). Using $\mathbf{r}'(\pi)=\langle -6,1,0\rangle$ and point $P=(0,\pi,-2)$, the plane equation is

$$
\mathbf{r}'(\pi)\cdot\big\langle x-0,\;y-\pi,\;z+2\big\rangle=0
$$

so

$$
-6x+(y-\pi)+0\cdot(z+2)=0.
$$

Or simplified:

$$
\boxed{-6x+y-\pi=0}\qquad\text{(normal plane).}
$$

Equivalently $y=6x+\pi.$

### Osculating plane

The osculating plane is the plane spanned by $\mathbf{r}'(\pi)$ and $\mathbf{r}''(\pi)$; its normal is $\mathbf{B}$. Using $\langle 1,6,0\rangle$ and the same point $P$,

$$
\langle 1,6,0\rangle\cdot\langle x-0,\;y-\pi,\;z+2\rangle=0
$$

gives

$$
x+6(y-\pi)+0\cdot(z+2)=0.
$$

Or simplified:

$$
\boxed{x+6y-6\pi=0}\qquad\text{(osculating plane).}
$$

## 9. Find the curvature of $r(t) = \langle t, t2, t3\rangle$ at the point $(1, 1, 1)$.
We have $\mathbf{r}(t)=\langle t,t^2,t^3\rangle$. The point $(1,1,1)$ corresponds to $t=1$.

Compute derivatives:

$$
\mathbf{r}'(t)=\langle 1,2t,3t^2\rangle,\qquad
\mathbf{r}''(t)=\langle 0,2,6t\rangle.
$$

At $t=1$:

$$
\mathbf{r}'(1)=\langle 1,2,3\rangle,\qquad \mathbf{r}''(1)=\langle 0,2,6\rangle.
$$

Curvature formula:

$$
\kappa(t)=\frac{\big\|\mathbf{r}'(t)\times\mathbf{r}''(t)\big\|}{\|\mathbf{r}'(t)\|^3}.
$$

Cross product at $t=1$:

$$
\mathbf{r}'(1)\times\mathbf{r}''(1)
=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\1&2&3\\0&2&6\end{vmatrix}
=\langle 6,-6,2\rangle,
$$

so $\|\mathbf{r}'(1)\times\mathbf{r}''(1)\|=\sqrt{6^2+(-6)^2+2^2}=\sqrt{76}=2\sqrt{19}.$

Also $\|\mathbf{r}'(1)\|=\sqrt{1+4+9}=\sqrt{14}$, so $\|\mathbf{r}'(1)\|^3=14\sqrt{14}.$

Therefore

$$
\boxed{\displaystyle \kappa(1)=\frac{2\sqrt{19}}{14\sqrt{14}}=\frac{\sqrt{19}}{7\sqrt{14}}\approx 0.1665.}
$$

## 10. Find the equation of the normal plane and osculating plane of the curve $x=2\sin{3t}$, $y=t$ and $z=2\cos{3t}$ at $(0,\pi, -2)$.
The parametric curve is

$$
\mathbf{r}(t)=\langle 2\sin(3t),\; t,\; 2\cos(3t)\rangle.
$$

Compute derivatives and evaluate at $t=\pi$:

$$
\mathbf{r}'(t)=\langle 6\cos(3t),\;1,\;-6\sin(3t)\rangle,\qquad
\mathbf{r}''(t)=\langle -18\sin(3t),\;0,\;-18\cos(3t)\rangle.
$$

At $t=\pi$ (where $\cos(3\pi)=-1,\ \sin(3\pi)=0$):

$$
\mathbf{r}'(\pi)=\langle -6,\,1,\,0\rangle,\qquad
\mathbf{r}''(\pi)=\langle 0,\,0,\,18\rangle.
$$

Tangent vector (direction) at the point is $\mathbf{r}'(\pi)=\langle -6,1,0\rangle$.
The binormal (normal to the osculating plane) is proportional to

$$
\mathbf{B}=\mathbf{r}'(\pi)\times\mathbf{r}''(\pi)
=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\-6&1&0\\0&0&18\end{vmatrix}
=\langle 18,\,108,\,0\rangle
=18\langle 1,6,0\rangle.
$$

We may use $\langle 1,6,0\rangle$ as the normal to the osculating plane.

### Normal plane

The normal plane at a point is the plane **perpendicular to the tangent vector** (so its normal is $\mathbf{r}'(\pi)$). Using $\mathbf{r}'(\pi)=\langle -6,1,0\rangle$ and point $P=(0,\pi,-2)$, the plane equation is

$$
\mathbf{r}'(\pi)\cdot\big\langle x-0,\;y-\pi,\;z+2\big\rangle=0
$$

so

$$
-6x+(y-\pi)+0\cdot(z+2)=0.
$$

Or simplified:

$$
\boxed{-6x+y-\pi=0}\qquad\text{(normal plane).}
$$

Equivalently $y=6x+\pi.$

### Osculating plane

The osculating plane is the plane spanned by $\mathbf{r}'(\pi)$ and $\mathbf{r}''(\pi)$; its normal is $\mathbf{B}$. Using $\langle 1,6,0\rangle$ and the same point $P$,

$$
\langle 1,6,0\rangle\cdot\langle x-0,\;y-\pi,\;z+2\rangle=0
$$

gives

$$
x+6(y-\pi)+0\cdot(z+2)=0.
$$

Or simplified:

$$
\boxed{x+6y-6\pi=0}\qquad\text{(osculating plane).}
$$

## 11. Find the tangential and normal components of the acceleration vector $r(t) = e^ti + \sqrt{2}tj +e ^ {-1}k \quad \boxed{\text{GATE 2022}}$. 

To find the tangential and normal components of the acceleration vector for the given vector function $\mathbf{r}(t) = e^t \hat{i} + \sqrt{2} t \hat{j} + e^{-1} \hat{k}$, we proceed in the following steps:

### Step 1: Compute the velocity vector $\mathbf{v}(t)$

The velocity vector $\mathbf{v}(t)$ is the derivative of the position vector $\mathbf{r}(t)$ with respect to time $t$.

$$
\mathbf{r}(t) = e^t \hat{i} + \sqrt{2} t \hat{j} + e^{-1} \hat{k}
$$

Taking the derivative of each component:

$$
\mathbf{v}(t) = \frac{d}{dt} \left( e^t \hat{i} + \sqrt{2} t \hat{j} + e^{-1} \hat{k} \right)
$$

$$
\mathbf{v}(t) = e^t \hat{i} + \sqrt{2} \hat{j} + 0 \hat{k}
$$

$$
\mathbf{v}(t) = e^t \hat{i} + \sqrt{2} \hat{j}
$$

### Step 2: Compute the acceleration vector $\mathbf{a}(t)$

The acceleration vector $\mathbf{a}(t)$ is the derivative of the velocity vector $\mathbf{v}(t)$ with respect to time $t$.

$$
\mathbf{v}(t) = e^t \hat{i} + \sqrt{2} \hat{j}
$$

Taking the derivative:

$$
\mathbf{a}(t) = \frac{d}{dt} \left( e^t \hat{i} + \sqrt{2} \hat{j} \right)
$$

$$
\mathbf{a}(t) = e^t \hat{i} + 0 \hat{j}
$$

$$
\mathbf{a}(t) = e^t \hat{i}
$$

### Step 3: Find the tangential and normal components of the acceleration

To find the tangential and normal components, we use the following formulas:

* The **tangential component** of acceleration $a_T(t)$ is given by:

  $$
  a_T(t) = \frac{\mathbf{v}(t) \cdot \mathbf{a}(t)}{|\mathbf{v}(t)|}
  $$

* The **normal component** of acceleration $a_N(t)$ is given by:

  $$
  a_N(t) = \sqrt{|\mathbf{a}(t)|^2 - a_T(t)^2}
  $$

### Step 4: Calculate the dot product $\mathbf{v}(t) \cdot \mathbf{a}(t)$

$$
\mathbf{v}(t) = e^t \hat{i} + \sqrt{2} \hat{j}, \quad \mathbf{a}(t) = e^t \hat{i}
$$

$$
\mathbf{v}(t) \cdot \mathbf{a}(t) = (e^t \hat{i}) \cdot (e^t \hat{i}) + (\sqrt{2} \hat{j}) \cdot 0 = e^{2t}
$$

### Step 5: Calculate $|\mathbf{v}(t)|$ (the magnitude of the velocity vector)

$$
|\mathbf{v}(t)| = \sqrt{(e^t)^2 + (\sqrt{2})^2} = \sqrt{e^{2t} + 2}
$$

### Step 6: Calculate the tangential component $a_T(t)$

Using the formula for $a_T(t)$:

$$
a_T(t) = \frac{e^{2t}}{\sqrt{e^{2t} + 2}}
$$

### Step 7: Calculate the normal component $a_N(t)$

Now, we compute the magnitude of $\mathbf{a}(t)$:

$$
|\mathbf{a}(t)| = |e^t \hat{i}| = e^t
$$

Then, use the formula for the normal component:

$$
a_N(t) = \sqrt{e^{2t} - \left( \frac{e^{2t}}{\sqrt{e^{2t} + 2}} \right)^2}
$$

## 12. Find the vector that is perpendicular to the vector $(i + j + k)$ and $(i + 2j + 3k) \quad \boxed{\text{GATE 2021}}$ 
To find a vector that is perpendicular to both $\mathbf{v}_1 = \hat{i} + \hat{j} + \hat{k}$ and $\mathbf{v}_2 = \hat{i} + 2\hat{j} + 3\hat{k}$, we need to compute their **cross product**.

### Step 1: Write the vectors in component form

$$
\mathbf{v}_1 = \hat{i} + \hat{j} + \hat{k} = (1, 1, 1)
$$

$$
\mathbf{v}_2 = \hat{i} + 2\hat{j} + 3\hat{k} = (1, 2, 3)
$$

### Step 2: Compute the cross product $\mathbf{v}_1 \times \mathbf{v}_2$

The formula for the cross product of two vectors $\mathbf{v}_1 = (v_{1x}, v_{1y}, v_{1z})$ and $\mathbf{v}_2 = (v_{2x}, v_{2y}, v_{2z})$ is:

$$
\mathbf{v}_1 \times \mathbf{v}_2 = \begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
v_{1x} & v_{1y} & v_{1z} \\
v_{2x} & v_{2y} & v_{2z}
\end{vmatrix}
$$

Substituting the components of $\mathbf{v}_1 = (1, 1, 1)$ and $\mathbf{v}_2 = (1, 2, 3)$:

$$
\mathbf{v}_1 \times \mathbf{v}_2 = \begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
1 & 1 & 1 \\
1 & 2 & 3
\end{vmatrix}
$$

### Step 3: Evaluate the determinant

Expanding the determinant:

$$
\mathbf{v}_1 \times \mathbf{v}_2 = \hat{i} \begin{vmatrix} 1 & 1 \\ 2 & 3 \end{vmatrix} - \hat{j} \begin{vmatrix} 1 & 1 \\ 1 & 3 \end{vmatrix} + \hat{k} \begin{vmatrix} 1 & 1 \\ 1 & 2 \end{vmatrix}
$$

Now compute the 2x2 determinants:

$$
\begin{vmatrix} 1 & 1 \\ 2 & 3 \end{vmatrix} = (1)(3) - (1)(2) = 3 - 2 = 1
$$

$$
\begin{vmatrix} 1 & 1 \\ 1 & 3 \end{vmatrix} = (1)(3) - (1)(1) = 3 - 1 = 2
$$

$$
\begin{vmatrix} 1 & 1 \\ 1 & 2 \end{vmatrix} = (1)(2) - (1)(1) = 2 - 1 = 1
$$

Thus, the cross product is:

$$
\mathbf{v}_1 \times \mathbf{v}_2 = \hat{i}(1) - \hat{j}(2) + \hat{k}(1)
$$

$$
\mathbf{v}_1 \times \mathbf{v}_2 = \hat{i} - 2\hat{j} + \hat{k}
$$

### Final Result:

The vector that is perpendicular to both $\mathbf{v}_1$ and $\mathbf{v}_2$ is:

$$
\mathbf{v}_1 \times \mathbf{v}_2 = \hat{i} - 2\hat{j} + \hat{k}
$$

or in component form:

$$
\mathbf{v}_1 \times \mathbf{v}_2 = (1, -2, 1)
$$
