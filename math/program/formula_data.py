# formula_data.py
# 考研数学全量题库：导数、积分、极限、三角、级数、几何应用

data = [
    # =========================================================
    # 第一部分：基本导数公式 (Derivatives)
    # =========================================================
    {
        "desc": "【导数】求正切函数的导数",
        "question": r"(\tan x)'",
        "answer": r"\sec^2 x"
    },
    {
        "desc": "【导数】求余切函数的导数",
        "question": r"(\cot x)'",
        "answer": r"-\csc^2 x"
    },
    {
        "desc": "【导数】求正割函数的导数",
        "question": r"(\sec x)'",
        "answer": r"\sec x \tan x"
    },
    {
        "desc": "【导数】求余割函数的导数",
        "question": r"(\csc x)'",
        "answer": r"-\csc x \cot x"
    },
    {
        "desc": "【导数】求反正弦函数的导数",
        "question": r"(\arcsin x)'",
        "answer": r"\frac{1}{\sqrt{1-x^2}}"
    },
    {
        "desc": "【导数】求反余弦函数的导数",
        "question": r"(\arccos x)'",
        "answer": r"-\frac{1}{\sqrt{1-x^2}}"
    },
    {
        "desc": "【导数】求反正切函数的导数",
        "question": r"(\arctan x)'",
        "answer": r"\frac{1}{1+x^2}"
    },
    {
        "desc": "【导数】求反余切函数的导数",
        "question": r"(\arccot x)'",
        "answer": r"-\frac{1}{1+x^2}"
    },
    {
        "desc": "【导数】一般指数函数的导数",
        "question": r"(a^x)'",
        "answer": r"a^x \ln a"
    },
    {
        "desc": "【导数】一般对数函数的导数",
        "question": r"(\log_a x)'",
        "answer": r"\frac{1}{x \ln a}"
    },
    {
        "desc": "【高阶导数】莱布尼茨公式 (Product Rule)",
        "question": r"(uv)^{(n)}",
        "answer": r"\sum_{k=0}^{n} C_n^k u^{(n-k)} v^{(k)}"
    },

    # =========================================================
    # 第二部分：基本积分公式 (Integrals)
    # =========================================================
    {
        "desc": "【积分】正切函数的积分",
        "question": r"\int \tan x \, dx",
        "answer": r"-\ln|\cos x| + C"
    },
    {
        "desc": "【积分】余切函数的积分",
        "question": r"\int \cot x \, dx",
        "answer": r"\ln|\sin x| + C"
    },
    {
        "desc": "【积分】正割函数的积分（高频考点）",
        "question": r"\int \sec x \, dx",
        "answer": r"\ln|\sec x + \tan x| + C"
    },
    {
        "desc": "【积分】余割函数的积分（高频考点）",
        "question": r"\int \csc x \, dx",
        "answer": r"\ln|\csc x - \cot x| + C"
    },
    {
        "desc": "【积分】sec平方的积分",
        "question": r"\int \sec^2 x \, dx",
        "answer": r"\tan x + C"
    },
    {
        "desc": "【积分】csc平方的积分",
        "question": r"\int \csc^2 x \, dx",
        "answer": r"-\cot x + C"
    },
    {
        "desc": "【积分】a^2 + x^2 型积分",
        "question": r"\int \frac{1}{a^2+x^2} \, dx",
        "answer": r"\frac{1}{a} \arctan \frac{x}{a} + C"
    },
    {
        "desc": "【积分】x^2 - a^2 型积分（平方差）",
        "question": r"\int \frac{1}{x^2-a^2} \, dx",
        "answer": r"\frac{1}{2a} \ln |\frac{x-a}{x+a}| + C"
    },
    {
        "desc": "【积分】sqrt(a^2 - x^2) 分母型积分",
        "question": r"\int \frac{1}{\sqrt{a^2-x^2}} \, dx",
        "answer": r"\arcsin \frac{x}{a} + C"
    },
    {
        "desc": "【积分】sqrt(x^2 + a^2) 对数型积分",
        "question": r"\int \frac{1}{\sqrt{x^2+a^2}} \, dx",
        "answer": r"\ln(x + \sqrt{x^2+a^2}) + C"
    },
    {
        "desc": "【积分】sqrt(x^2 - a^2) 对数型积分",
        "question": r"\int \frac{1}{\sqrt{x^2-a^2}} \, dx",
        "answer": r"\ln|x + \sqrt{x^2-a^2}| + C"
    },
    {
        "desc": "【积分】分部积分公式",
        "question": r"\int u \, dv",
        "answer": r"uv - \int v \, du"
    },
    {
        "desc": "【定积分】华里士公式 (Wallis/点火公式) I_n",
        "question": r"\int_0^{\pi/2} \sin^n x \, dx",
        "answer": r"\frac{n-1}{n} I_{n-2}, \quad (I_1=1, I_0=\frac{\pi}{2})"
    },
    {
        "desc": "【积分】ln x 的积分",
        "question": r"\int \ln x \, dx",
        "answer": r"x \ln x - x + C"
    },

    # =========================================================
    # 第三部分：泰勒公式与麦克劳林展开 (Taylor Series)
    # =========================================================
    {
        "desc": "【泰勒】e^x 的麦克劳林展开",
        "question": r"e^x",
        "answer": r"1 + x + \frac{x^2}{2!} + \dots + \frac{x^n}{n!} + o(x^n)"
    },
    {
        "desc": "【泰勒】sin x 的展开 (奇函数)",
        "question": r"\sin x",
        "answer": r"x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots + (-1)^{k-1}\frac{x^{2k-1}}{(2k-1)!}"
    },
    {
        "desc": "【泰勒】cos x 的展开 (偶函数)",
        "question": r"\cos x",
        "answer": r"1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots + (-1)^k\frac{x^{2k}}{(2k)!}"
    },
    {
        "desc": "【泰勒】ln(1+x) 的展开",
        "question": r"\ln(1+x)",
        "answer": r"x - \frac{x^2}{2} + \frac{x^3}{3} - \dots + (-1)^{n-1}\frac{x^n}{n} + o(x^n)"
    },
    {
        "desc": "【泰勒】(1+x)^α 的二项式展开",
        "question": r"(1+x)^\alpha",
        "answer": r"1 + \alpha x + \frac{\alpha(\alpha-1)}{2!}x^2 + \dots"
    },
    {
        "desc": "【泰勒】1/(1-x) 几何级数",
        "question": r"\frac{1}{1-x}",
        "answer": r"1 + x + x^2 + \dots + x^n + o(x^n)"
    },

    # =========================================================
    # 第四部分：等价无穷小 (x -> 0)
    # =========================================================
    {
        "desc": "【极限】sin x, tan x, arcsin x, arctan x 的一阶等价",
        "question": r"x \to 0",
        "answer": r"\sim x"
    },
    {
        "desc": "【极限】1 - cos x 的等价无穷小",
        "question": r"1 - \cos x",
        "answer": r"\sim \frac{1}{2}x^2"
    },
    {
        "desc": "【极限】e^x - 1 的等价无穷小",
        "question": r"e^x - 1",
        "answer": r"\sim x"
    },
    {
        "desc": "【极限】ln(1+x) 的等价无穷小",
        "question": r"\ln(1+x)",
        "answer": r"\sim x"
    },
    {
        "desc": "【极限】(1+x)^α - 1 的等价无穷小",
        "question": r"(1+x)^\alpha - 1",
        "answer": r"\sim \alpha x"
    },
    {
        "desc": "【极限】a^x - 1 的等价无穷小",
        "question": r"a^x - 1",
        "answer": r"\sim x \ln a"
    },
    {
        "desc": "【极限】x - sin x (三阶小)",
        "question": r"x - \sin x",
        "answer": r"\sim \frac{1}{6}x^3"
    },
    {
        "desc": "【极限】arcsin x - x (三阶小)",
        "question": r"\arcsin x - x",
        "answer": r"\sim \frac{1}{6}x^3"
    },
    {
        "desc": "【极限】tan x - x (三阶小)",
        "question": r"\tan x - x",
        "answer": r"\sim \frac{1}{3}x^3"
    },
    {
        "desc": "【极限】x - arctan x (三阶小)",
        "question": r"x - \arctan x",
        "answer": r"\sim \frac{1}{3}x^3"
    },
    {
        "desc": "【极限】tan x - sin x (三阶小)",
        "question": r"\tan x - \sin x",
        "answer": r"\sim \frac{1}{2}x^3"
    },

    # =========================================================
    # 第五部分：三角函数公式 (Trigonometry)
    # =========================================================
    {
        "desc": "【三角】二倍角公式 sin 2x",
        "question": r"\sin 2x",
        "answer": r"2 \sin x \cos x"
    },
    {
        "desc": "【三角】二倍角公式 cos 2x (含平方)",
        "question": r"\cos 2x",
        "answer": r"\cos^2 x - \sin^2 x = 2\cos^2 x - 1"
    },
    {
        "desc": "【三角】降幂公式 sin^2 x",
        "question": r"\sin^2 x",
        "answer": r"\frac{1 - \cos 2x}{2}"
    },
    {
        "desc": "【三角】降幂公式 cos^2 x",
        "question": r"\cos^2 x",
        "answer": r"\frac{1 + \cos 2x}{2}"
    },
    {
        "desc": "【三角】万能公式：sin x (令 t=tan(x/2))",
        "question": r"\sin x",
        "answer": r"\frac{2t}{1+t^2}"
    },
    {
        "desc": "【三角】万能公式：cos x (令 t=tan(x/2))",
        "question": r"\cos x",
        "answer": r"\frac{1-t^2}{1+t^2}"
    },
    {
        "desc": "【三角】和差化积 sin A + sin B",
        "question": r"\sin A + \sin B",
        "answer": r"2 \sin \frac{A+B}{2} \cos \frac{A-B}{2}"
    },
    {
        "desc": "【三角】和差化积 cos A + cos B",
        "question": r"\cos A + \cos B",
        "answer": r"2 \cos \frac{A+B}{2} \cos \frac{A-B}{2}"
    },
    {
        "desc": "【三角】和差化积 cos A - cos B (注意负号)",
        "question": r"\cos A - \cos B",
        "answer": r"-2 \sin \frac{A+B}{2} \sin \frac{A-B}{2}"
    },
    {
        "desc": "【三角】积化和差 sin A cos B",
        "question": r"\sin A \cos B",
        "answer": r"\frac{1}{2} [\sin(A+B) + \sin(A-B)]"
    },
    {
        "desc": "【三角】积化和差 sin A sin B",
        "question": r"\sin A \sin B",
        "answer": r"-\frac{1}{2} [\cos(A+B) - \cos(A-B)]"
    },
    {
        "desc": "【三角】辅助角公式",
        "question": r"a \sin x + b \cos x",
        "answer": r"\sqrt{a^2+b^2} \sin(x + \phi)"
    },

    # =========================================================
    # 第六部分：多元微积分与场论 (Multivariable)
    # =========================================================
    {
        "desc": "【多元】格林公式 (Green's Theorem)",
        "question": r"\oint_L P dx + Q dy",
        "answer": r"\iint_D (\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}) dx dy"
    },
    {
        "desc": "【多元】高斯公式 (Gauss/Divergence)",
        "question": r"\iint_{\Sigma} (P \cos \alpha + Q \cos \beta + R \cos \gamma) dS",
        "answer": r"\iiint_{\Omega} (\frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}) dv"
    },
    {
        "desc": "【多元】斯托克斯公式 (Stokes) 的旋度部分",
        "question": r"rot \mathbf{A} (旋度)",
        "answer": r"\left| \begin{matrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ P & Q & R \end{matrix} \right|"
    },
    {
        "desc": "【多元】方向导数公式",
        "question": r"\frac{\partial u}{\partial l}",
        "answer": r"\frac{\partial u}{\partial x} \cos \alpha + \frac{\partial u}{\partial y} \cos \beta + \frac{\partial u}{\partial z} \cos \gamma"
    },
    {
        "desc": "【多元】梯度定义",
        "question": r"\mathbf{grad} \, u",
        "answer": r"\frac{\partial u}{\partial x}\mathbf{i} + \frac{\partial u}{\partial y}\mathbf{j} + \frac{\partial u}{\partial z}\mathbf{k}"
    }
]
