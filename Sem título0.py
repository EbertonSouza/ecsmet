# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 16:29:46 2018

@author: ebert
"""

i




a, b = 1, 4

# Define x and y arrays.
x = np.linspace(a,b)
y = f(x)

# parametro da figura espessura da linha e limites em x e y
#class matplotlib.figure.Figure( linewidth=0.0)
fig, ax = pl.subplots()
pl.plot(x, y, 'b', linewidth = 2)
pl.xlim(xmin = -1, xmax = 6)
pl.ylim(ymin = 0)


# Shade area de integração abaixo da curva
#class matplotlib.figure.Figure( facecolor=None,edgecolor=None, o 10 significa area que 
#aparece abaixo da curva list(zip) lista as colunas ix e iy)
ix = np.linspace(a, b,10)
iy = f(ix)
verts = [(a, 0)] + list(zip(ix, iy)) + [(b, 0)]
poly = Polygon(verts, facecolor = '0.8', edgecolor = '0.2')
ax.add_patch(poly)

#parametros do texto da itegral impressa  em que 200 ou seja n é o numero de retangulo
#quanto maior, maior a aproximação do valor real
pl.text(0.5 * (a + b), 2, r"$\int_{1}^{4}f(x)dx=%.2f$" %res, err = quad(f, 1, 4),
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
##########