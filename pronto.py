# -*- coding: UTF-8 -*-



import numpy as np

################################################################
h = 0.5;
x = np.arange(temp_prev);
#############################################################
eq1 = x*np.exp(-x);
eq2 = np.sqrt(x);
eq3 = np.exp(-x);
##############################################################
# Regra dos trapézios: 
trap1 = np.trapz(eq1, x);
trap2 = np.trapz(eq2, x);
trap3= np.trapz(eq3, x);

###############################################################
int1 = 1 - (6 + 1)*np.exp(-6);
int2 = 2*(6**(3/2))/3;
int3 = 1 - np.exp(-6);







###########################################################
erro_trap1 = trap1 - int1;
erro_trap2 = trap2 - int2;
erro_trap3 = trap3 - int3;
############################################################
# Regra dos 3/8 de Simpson: 
sim1 = eq1[0];
sim2 = eq2[0];
sim3 = eq3[0];
n = 1;
tam = len(x);

sim1 = sim1 + 3*eq1[n] + 3*eq1[n+1] + 2*eq1[n+2];
sim2 = sim2 + 3*eq2[n] + 3*eq2[n+1] + 2*eq2[n+2];
sim3 = sim3 + 3*eq3[n] + 3*eq3[n+1] + 2*eq3[n+2];
n = n + 3; 
 
###########################################################
# integral pela regra de Simpson composta:
sim1 = sim1 - eq1[tam-1];  
sim1 =h/8* (3*sim1); 
sim2 = sim2 - eq2[tam-1];  
sim2 = h/8*(3*sim2) ; 
sim3 = sim3 - eq3[tam-1]; 
sim3 =h/8 *(3*sim3) ; 

erros1 = int1 - sim1;
erros2 = int2 - sim2;
erros3 = int3 - sim3;
######################################################################
print('Rg. Trap., Rg. Simpson, Erro Trap,   Erro Simpson:')
print("%1.6f" % trap1, "  %1.6f" % sim1, "    %1.6f" % erro_trap1, "   %1.6f" % erros1);
print("%1.6f" % trap2, " %1.6f" % sim2, "     %1.6f" % erro_trap2, "  %1.6f" % erros2);
print("%1.6f" % trap3, "  %1.6f" % sim3, "     %1.6f" % erro_trap3, "   %1.6f" % erros3); 

 