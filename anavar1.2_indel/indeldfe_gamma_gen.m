(* scriptname n theta1 theta2 shape1 shape2 scale1 scale2 e1 e2 rep filename *)

expected = False;
n = ToExpression[$CommandLine[[4]]];
\[Theta] = {ToExpression[$CommandLine[[5]]], ToExpression[$CommandLine[[6]]]};
shape = {ToExpression[$CommandLine[[7]]], ToExpression[$CommandLine[[8]]]};
scale = {ToExpression[$CommandLine[[9]]], ToExpression[$CommandLine[[10]]]};
e = {ToExpression[$CommandLine[[11]]], ToExpression[$CommandLine[[12]]]};
nrep = ToExpression[$CommandLine[[13]]];
file = ToExpression[$CommandLine[[14]]];
stream = OpenWrite[file, FormatType -> StandardForm]; 
flag =  ! (AllTrue[shape, #1 > 0 & ] && AllTrue[scale, #1 > 0 & ]); 
If[flag, WriteString[stream, "Error in the parameters\n"]; Abort[], 
   \[Tau][(n_)?NumericQ, (i_)?NumericQ, (\[Gamma]_)?NumericQ] := 
      Module[{f, re}, 
   f[x_] := x^(i - 1)*(1 - x)^(n - i - 1)*
     N[If[Abs[\[Gamma]] <= 
        1/10^3, (-(1/24))*(-1 + 
          x)*(24 + \[Gamma]*
           x*(12 + \[Gamma]*(-2 + (4 + \[Gamma]*(-1 + x))*x))), 
                 (1 - E^((-\[Gamma])*(1 - x)))/(1 - E^(-\[Gamma]))]]; 
   re = Binomial[n, i]*NIntegrate[f[x], {x, 0, 1}]; re]; 
    dgi[(\[Gamma]_)?NumericQ] := 
  PDF[GammaDistribution[shape[[1]], scale[[1]]], \[Gamma]]; 
 dgd[(\[Gamma]_)?NumericQ] := 
  PDF[GammaDistribution[shape[[2]], scale[[2]]], \[Gamma]]; 
    ti = ConstantArray[0, n - 1]; td = ConstantArray[0, n - 1]; 
 For[i = 1, i < n, i++, 
  ti[[i]] = \[Theta][[1]]*
    NIntegrate[\[Tau][n, i, -\[Gamma]]*dgi[\[Gamma]], {\[Gamma], 0, 
      Infinity}]; 
       td[[i]] = \[Theta][[2]]*
    NIntegrate[\[Tau][n, i, -\[Gamma]]*dgd[\[Gamma]], {\[Gamma], 0, 
      Infinity}]; ]; sfsi = ConstantArray[0, n - 1]; 
 sfsd = ConstantArray[0, n - 1]; 
    For[i = 1, i < n, i++, 
  sfsi[[i]] = (1 - e[[1]])*ti[[i]] + e[[2]]*td[[n - i]]; 
  sfsd[[i]] = (1 - e[[2]])*td[[i]] + e[[1]]*ti[[n - i]]; ]; 
    For[k = 1, k <= nrep, k++, For[i = 1, i <= Length[sfsi], i++, 
         WriteString[stream, "", 
    FortranForm[
     If[expected, sfsi[[i]], 
      RandomVariate[PoissonDistribution[sfsi[[i]]]]]]]; 
   If[i < Length[sfsi], WriteString[stream, ", "]]; ]; 
       WriteString[stream, "\n"]; For[i = 1, i <= Length[sfsd], i++, 
         WriteString[stream, "", 
    FortranForm[
     If[expected, sfsd[[i]], 
      RandomVariate[PoissonDistribution[sfsd[[i]]]]]]]; 
   If[i < Length[sfsd], WriteString[stream, ", "]]; ]; 
       WriteString[stream, "\n\n"]; ]]
Close[stream]; 