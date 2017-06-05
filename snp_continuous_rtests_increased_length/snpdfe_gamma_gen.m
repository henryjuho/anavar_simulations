(* ::Package:: *)

n = 50; 
folded = False; 
\[Theta] = 0.005*10^6; 
shape = 0.3; 
scale = 50; 
e = 0.05; 
nrep = 100;
file = "100sfs_cont_gamma_long.txt";
stream = OpenWrite[file, FormatType -> StandardForm]; 
flag1 = folded && e != 0; 
flag2 =  ! (shape > 0 && scale > 0); 
If[flag1 || flag2, WriteString[stream, "Error in the parameters\n"]; 
    Abort[], \[Tau][(n_)?NumericQ, (i_)?NumericQ, (\[Gamma]_)?NumericQ] := 
      Module[{f, re}, f[x_] := x^(i - 1)*(1 - x)^(n - i - 1)*
             N[If[Abs[\[Gamma]] <= 1/10^3, (-(1/24))*(-1 + x)*
                   (24 + \[Gamma]*
           x*(12 + \[Gamma]*(-2 + (4 + \[Gamma]*(-1 + x))*x))), 
                 (1 - E^((-\[Gamma])*(1 - x)))/(1 - E^(-\[Gamma]))]]; 
         re = Binomial[n, i]*NIntegrate[f[x], {x, 0, 1}]; re]; 
    dg[(\[Gamma]_)?NumericQ] := 
  PDF[GammaDistribution[shape, scale], \[Gamma]]; 
    sfs = If[folded == True, ConstantArray[0, Floor[n/2]], 
        ConstantArray[0, n - 1]]; If[folded, For[i = 1, i <= Floor[n/2], 
        i++, 
   sfs[[i]] = 
    If[i == n - i, \[Theta]*NIntegrate[\[Tau][n, i, -\[Gamma]]*dg[\[Gamma]], 
                {\[Gamma], 0, Infinity}], \[Theta]*
       NIntegrate[\[Tau][n, i, -\[Gamma]]*dg[\[Gamma]], 
                  {\[Gamma], 0, Infinity}] + \[Theta]*
       NIntegrate[\[Tau][n, n - i, -\[Gamma]]*dg[\[Gamma]], 
                  {\[Gamma], 0, Infinity}]]], For[i = 1, i < n, i++, 
        sfs[[i]] = 
    If[i == n - i, \[Theta]*NIntegrate[\[Tau][n, i, -\[Gamma]]*dg[\[Gamma]], 
                {\[Gamma], 0, Infinity}], \[Theta]*(1 - e)*
       NIntegrate[\[Tau][n, i, -\[Gamma]]*
                    dg[\[Gamma]], {\[Gamma], 0, Infinity}] + 
              \[Theta]*e*
       NIntegrate[\[Tau][n, n - i, -\[Gamma]]*dg[\[Gamma]], 
                  {\[Gamma], 0, Infinity}]]]]; For[k = 1, k <= nrep, k++, 
      For[i = 1, i <= Length[sfs], i++, WriteString[stream, "", 
            RandomVariate[PoissonDistribution[sfs[[i]]]]]; 
          If[i < Length[sfs], WriteString[stream, ", "]]; ]; 
       WriteString[stream, "\n"]; ]]
Close[stream]; 
