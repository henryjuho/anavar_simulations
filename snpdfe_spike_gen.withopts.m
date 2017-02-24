(* scriptname n theta gamma e filename*)
n = ToExpression[$CommandLine[[4]]];
folded = False; 
\[Theta] = {ToExpression[$CommandLine[[5]]]};
\[Gamma] = {ToExpression[$CommandLine[[6]]]};
e = {ToExpression[$CommandLine[[7]]]};
nrep = 2; 
file = ToString[$CommandLine[[8]]];
stream = OpenWrite[file, FormatType -> StandardForm]; 
flag1 = True; 
For[i = 1, i <= Length[\[Gamma]], i++, 
  flag1 = flag1 && \[Gamma][[i]] == 0]; 
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
           x*(12 + \[Gamma]*(-2 + (4 + \[Gamma]*(-1 + x))*x))), (1 - 
          E^((-\[Gamma])*(1 - x)))/
                   (1 - E^(-\[Gamma]))]]; 
   re = Binomial[n, i]*NIntegrate[f[x], {x, 0, 1}]; re]; 
    sfs = 
  If[folded == True, ConstantArray[0, Floor[n/2]], 
   ConstantArray[0, n - 1]]; 
    If[folded, For[i = 1, i <= Floor[n/2], i++, 
        sfs[[i]] = 
    If[i == n - i, 
     Sum[\[Theta][[c]]*\[Tau][n, i, \[Gamma][[c]]], {c, 1, nc}], 
            
     Sum[\[Theta][[c]]*(\[Tau][n, i, \[Gamma][[c]]] + \[Tau][n, 
          n - i, \[Gamma][[c]]]), {c, 1, nc}]]], 
      For[i = 1, i < n, i++, 
   sfs[[i]] = 
    If[i == n - i, 
     Sum[\[Theta][[c]]*\[Tau][n, i, \[Gamma][[c]]], {c, 1, nc}], 
            
     Sum[\[Theta][[c]]*((1 - e[[c]])*\[Tau][n, i, \[Gamma][[c]]] + 
         e[[c]]*\[Tau][n, n - i, \[Gamma][[c]]]), 
              {c, 1, nc}]]]]; For[k = 1, k <= nrep, k++, 
      For[i = 1, i <= Length[sfs], i++, WriteString[stream, "\t", 
             RandomVariate[PoissonDistribution[sfs[[i]]]]]; ]; 
  WriteString[stream, "\n"]; ]]
Close[stream]; 