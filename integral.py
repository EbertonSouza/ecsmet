# -*- coding: utf-8 -*-
"""Created on Sat Apr 14 00:25:39 2018
@author: eberton
"""
'''
Regra de quadratura gaussiana ->quad
 largura (b - a) / n
 primeiro ponto é a em x, e f(a) em y
 segundo ponto é a= a+largura em x e f(a)=a+largura em y
 Área do retângulo1 = f (a + largura) × largura
 Área do retângulo2 = f (a + 2*largura) × largura
 Área do retângulo3 = f (a + 3*largura) × largura
 Área do retângulo n-1 = f (a + (n-2)*largura) × largura
 Área do retângulo n = f (a + (n-1)*largura) × largura
  no caso i esta sendo a largura que começa em 1 que é primeiro ponto ate o proximo que é n+1
 área de um retângulo = largura × altura ->  largura * f (a + (i-1) * largura)
 o valor da função no ponto      "a + (i-1) * largura"
 altura do retângulo i = f (a + (i-1) * largura) 
'''
import numpy as np
import matplotlib.pylab as pl
from matplotlib.patches import Polygon
from scipy.integrate import quad

####################################################################################################
#PARTE 1
# Definição dos parametros graficos
def f(x):
    return np.sqrt(x)
   
# Integration calculation.
def integration(a, b, n): 
    dx = (b - a) / n  
    integration = 0. 
    for i in np.arange(1, n + 1):
     integration += f(a + i * dx)
     # += pega a variavel integração e atribui +1 na proxima operação
     # quem varia é i que é numero de intervalo, mais o proximo
     # manta integrar em relação a altura que é f(a + i * dx)
    integration *= dx # *=, multiplica a variável e um valor, tornando o resultado a variável
    return integration

# Define integral limits.
a, b = 1, 4
n=10

# Define x and y arrays.
x = np.linspace(0, 5)
y = f(x)

# parametro da figura espessura da linha e limites em x e y
#class matplotlib.figure.Figure( linewidth=0.0)
fig, ax = pl.subplots()
pl.plot(x, y, 'red', linewidth = 2)
pl.xlim(xmin = -1, xmax = 6)
pl.ylim(ymin = 0)

# Shade area de integração abaixo da curva
#class matplotlib.figure.Figure( facecolor=None,edgecolor=None, o 10 significa area que 
#aparece abaixo da curva list(zip) lista as colunas ix e iy)
ix = np.linspace(a, b,8)
iy = f(ix)
verts = [(a, 0)] + list(zip(ix, iy)) + [(b, 0)]
poly = Polygon(verts, facecolor = '0.8', edgecolor = '0.2')
ax.add_patch(poly)

#parametros do texto da itegral impressa  em que 200 ou seja n é o numero de retangulo
#quanto maior, maior a aproximação do valor real
pl.text(0.5 * (a + b), 2, r"$\int_{1}^{4}f(x)dx=%.2f$" %integration(a, b, 1000),
horizontalalignment = 'right', fontsize = 20)

# Add x and y axes labels.
#parametro de onde aparece(x e Y)
pl.figtext(0.9, 0.05, '$x$')
pl.figtext(0.1, 0.9, '$y$')

# Remove right and top plot delimeter lines.
ax.spines['right'].set_visible(True)
ax.spines['top'].set_visible(True)
ax.xaxis.set_ticks_position('bottom')

# Add a and b ticks on x axis.a=1 e b=4
ax.set_xticks((a, b))
ax.set_xticklabels(('$a=%d$' %a, '$b=%d$' %b))
ax.set_yticks([])

# Show the plot.
pl.show()

#---------------------------------------------------------------------------------------------------

# funcao analitica
def integra1(x):
    return np.sqrt(x)

# chama  quad para integrate f de 1 to 4
res, err = quad(integra1, 1, 4)



#---------------------------------------------------------------------------------------------------
# Integração numerica 1
a = 1.0
b = 4.0
n = 10 #aumentei para aparecer perto do real
h = (b-a)/n
eq1 = lambda x: np.sqrt(x)

# Criando n+1 pontos igualmente espacados 
X = np.linspace(a, b, n+1)

#---------------------------------------------------------------------------------------------------
# Regra dos retangulos usando funções do numpy
def calculate_dx (a, b, n):
	return (b-a)/float(n)

def rect_rule (f, a, b, n):
	total = 0.0
	dx = calculate_dx(a, b, n)
	for m in range (1, n):
         total = total + f((a + (m*dx)))
	return dx*total

def f(x):
    return np.sqrt(x)



# Regra dos trapézios usando funções do numpy
trap1 = (h/2)*(eq1(X[0]) + 2*np.sum(eq1(X[1:n:1])) + eq1(X[-1]))
erro_trap1 = integration(a,b,n) - trap1;


# Regra 1/3 de Simpson usando funções do numpy
si1 = (h/3)*(eq1(X[0]) + 4*np.sum(eq1(X[1:n:2])) + 2*np.sum(eq1(X[2:n:2]))+ eq1(X[-1]))
erro_si1 = integration(a,b,n) - si1;


# Regra 3/8 de Simpson usando funções do numpy
si2 = (3*h/8)*(eq1(X[0]) + 3*np.sum(eq1(X[1:n:3])+eq1(X[2:n:3])) + 2*np.sum(eq1(X[3:n:3]))+ eq1(X[-1]))
erro_si2 = integration(a,b,n) - si2;

print("Resultado Integração Analítica da função 1:",res)
print("Regra Retangulo:",rect_rule(f, a, b, n))
print("Regra Trapézio: ", trap1)
print("Regra 1/3 Simp.:", si1)
print("Regra 3/8 Simp.:", si2)
print("Erro  Trapézio: ",erro_trap1)
print("Erro  1/3 Simp. ",erro_si1)
print("Erro  3/8 Simp. ",erro_si2)



####################################################################################################
#PARTE 2
# Definição dos parametros graficos

def f(x):
    return np.exp(-x)
   

# Integration calculation.
def integration2(a, b, n): 
    dx = (b - a) / n  
    integration = 0. 
    for i in np.arange(1, n + 1):
     integration += f(a + i * dx)
     # += pega a variavel integração e atribui +1 na proxima operação
     # quem varia é i que é numero de intervalo, mais o proximo
     # manta integrar em relação a altura que é f(a + i * dx)
    integration *= dx # *=, multiplica a variável e um valor, tornando o resultado a variável
    return integration

# Define integral limits.
a, b = 1, 4


# Define x and y arrays.
x = np.linspace(0, 5)
y = f(x)

# parametro da figura espessura da linha e limites em x e y
#class matplotlib.figure.Figure( linewidth=0.0)
fig, ax = pl.subplots()
pl.plot(x, y, 'red', linewidth = 2)
pl.xlim(xmin = -1, xmax = 6)
pl.ylim(ymin = 0)

# Shade area de integração abaixo da curva
#class matplotlib.figure.Figure( facecolor=None,edgecolor=None, o 10 significa area que 
#aparece abaixo da curva list(zip) lista as colunas ix e iy)
ix = np.linspace(a, b,8)
iy = f(ix)
verts = [(a, 0)] + list(zip(ix, iy)) + [(b, 0)]
poly = Polygon(verts, facecolor = '0.8', edgecolor = '0.2')
ax.add_patch(poly)

#parametros do texto da itegral impressa  em que 200 ou seja n é o numero de retangulo
#quanto maior, maior a aproximação do valor real
pl.text(0.3 * (a + b), 0.85, r"$\int_{1}^{4}f(x)dx=%.2f$" %integration(a, b, 1000),
horizontalalignment = 'left', fontsize = 20)

# Add x and y axes labels.
#parametro de onde aparece(x e Y)
pl.figtext(0.9, 0.05, '$x$')
pl.figtext(0.1, 0.9, '$y$')

# Remove right and top plot delimeter lines.
ax.spines['right'].set_visible(True)
ax.spines['top'].set_visible(True)
ax.xaxis.set_ticks_position('bottom')


# Add a and b ticks on x axis.a=1 e b=4
ax.set_xticks((a, b))
ax.set_xticklabels(('$a=%d$' %a, '$b=%d$' %b))
ax.set_yticks([])

# Show the plot.
pl.show()

#---------------------------------------------------------------------------------------------------
# funcao analitica
def integra2(x):
    return np.exp(-x)

# chama  quad para integrate f de 1 to 4
res2, err = quad(integra2, 1, 4)
#---------------------------------------------------------------------------------------------------


# Dados do enunciado
a = 1.0
b = 4.0
n = 10
h = (b-a)/n
eq2 = lambda x: np.exp(-x)

# Criando n+1 pontos igualmente espacados 
X = np.linspace(a, b, n+1)

#---------------------------------------------------------------------------------------------------
# Regra dos retangulos usando funções do numpy
def calculate_dx2 (a, b, n):
	return (b-a)/float(n)

def rect_rule2 (f, a, b, n):
	total = 0.0
	dx = calculate_dx2(a, b, n)
	for m in range (1, n):
         total = total + f((a + (m*dx)))
	return dx*total

def f(x):
    return np.exp(-x)

#--------------------------------------------------------------------------------------------------

# Regra dos trapézios usando funções do numpy
trap2 = (h/2)*(eq2(X[0]) + 2*np.sum(eq2(X[1:n:1])) + eq2(X[-1]))
erro_trap2 = integration(a,b,n) - trap2;

#--------------------------------------------------------------------------------------------------
# Regra 1/3 de Simpson usando funções do numpy
si11 = (h/3)*(eq2(X[0]) + 4*np.sum(eq2(X[1:n:2])) + 2*np.sum(eq2(X[2:n:2]))+ eq2(X[-1]))
erro_si11 = integration(a,b,n) - si11;

#--------------------------------------------------------------------------------------------------
# Regra 3/8 de Simpson usando funções do numpy
si22 = (3*h/8)*(eq2(X[0]) + 3*np.sum(eq2(X[1:n:3])+eq2(X[2:n:3])) + 2*np.sum(eq2(X[3:n:3]))+ eq2(X[-1]))
erro_si22 =si22- integration(a,b,n);


print("Resultado Integração Analítica da função 2:",res2)
print("Regra Retangulo:",rect_rule2(f, a, b, n))
print("Regra Trapézio: ", trap2)
print("Regra 1/3 Simp.:", si11)
print("Regra 3/8 Simp.:", si22)
print("Erro  Trapézio:",erro_trap2)
print("Erro  1/3 Simp.",erro_si11)
print("Erro  3/8 Simp. ",round(erro_si22,4))