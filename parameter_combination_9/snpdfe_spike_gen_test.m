(* ::Package:: *)

expected = False; 
n = 50; 
folded = False; 
\[Theta] = {0.002, 0.006, 0.002}*10^6; 
\[Gamma] = {0, -5, -30}; 
e = {0.05, 0.02, 0.01}; 
nrep = 1; 
file = "test_3class_sfs.txt";
stream = OpenWrite[file, FormatType -> StandardForm]; 
flag1 = True; 
For[i = 1, i <= Length[\[Gamma]], i++, 
  flag1 = flag1 && \[Gamma][[i]] == \[Gamma][[1]]]; 
flag1 = flag1 && Length[e] != 1; 
flag2 = True; 
For[i = 1, i <= Length[e], i++, flag2 = flag2 && e[[i]] == 0]; 
flag2 = If[folded, If[flag2, False, True], False]; 
flag3 =  ! (Length[e] == Length[\[Gamma]] && 
     Length[e] == Length[\[Theta]]); 
If[flag1 || flag2 || flag3, 
   WriteString[stream, "Error in the parameters\n"]; Abort[], 
   nc = Length[
   e]; \[Tau][(n_)?NumericQ, (i_)?NumericQ, (\[Gamma]_)?NumericQ] := 
      Module[{f, re}, f[x_] := x^(i - 1)*(1 - x)^(n - i - 1)*
             N[If[Abs[\[Gamma]] <= 1/10^3, (-(1/24))*(-1 + x)*
                   (24 + \[Gamma]*
           x*(12 + \[Gamma]*(-2 + (4 + \[Gamma]*(-1 + x))*x))), 
                 (1 - E^((-\[Gamma])*(1 - x)))/(1 - 
          E^(-\[Gamma]))]]; 
         re = Binomial[n, i]*NIntegrate[f[x], {x, 0, 1}]; re]; 
    sfs = If[folded == True, ConstantArray[0, Floor[n/2]], 
        ConstantArray[0, n - 1]]; 
 If[folded, For[i = 1, i <= Floor[n/2], 
        i++, 
   sfs[[i]] = 
    If[i == n - i, Sum[\[Theta][[c]]*\[Tau][n, i, \[Gamma][[c]]], 
              {c, 1, nc}], 
     Sum[\[Theta][[c]]*(\[Tau][n, i, \[Gamma][[c]]] + 
                   \[Tau][n, n - i, \[Gamma][[c]]]), {c, 1, nc}]]], 
      For[i = 1, i < n, i++, sfs[[i]] = If[i == n - i, 
            
     Sum[\[Theta][[c]]*\[Tau][n, i, \[Gamma][[c]]], {c, 1, nc}], 
            
     Sum[\[Theta][[c]]*((1 - e[[c]])*\[Tau][n, i, \[Gamma][[c]]] + 
                   e[[c]]*\[Tau][n, n - i, \[Gamma][[c]]]), {c, 1, 
       nc}]]]]; 
    For[k = 1, k <= nrep, k++, For[i = 1, i <= Length[sfs], i++, 
         If[expected, WriteString[stream, FortranForm[sfs[[i]]]], 
            WriteString[stream, FortranForm[RandomVariate[
                  PoissonDistribution[sfs[[i]]]]]]]; 
   If[i < Length[sfs], 
            WriteString[stream, ", "]]; ]; 
  WriteString[stream, "\n"]; ]]
Close[stream]; 
