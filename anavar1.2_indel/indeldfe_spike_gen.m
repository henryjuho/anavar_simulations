(* scriptname n theta_ins theta_del gamm_i gamma_d ei ed rep filename *)

expected = False;
n = ToExpression[$CommandLine[[4]]];
\[Theta]ins = {ToExpression[$CommandLine[[5]]]};
\[Theta]del = {ToExpression[$CommandLine[[6]]]};
\[Gamma]ins = {ToExpression[$CommandLine[[7]]]};
\[Gamma]del = {ToExpression[$CommandLine[[8]]]};
eins = {ToExpression[$CommandLine[[9]]]};
edel = {ToExpression[$CommandLine[[10]]]};
nrep = ToExpression[$CommandLine[[11]]];
file = ToString[$CommandLine[[12]]];
stream = OpenWrite[file, FormatType -> StandardForm]; 
flag1 = True; 
For[i = 1, i <= Length[\[Gamma]ins], i++, 
  flag1 = flag1 && \[Gamma]ins[[i]] == \[Gamma]ins[[1]]]; 
flag1 = flag1 && Length[eins] != 1; 
flag2 = Length[\[Theta]ins] == Length[\[Theta]del] && 
   Length[\[Theta]ins] == Length[\[Gamma]ins] && 
   Length[\[Theta]ins] == Length[\[Gamma]del] && 
   Length[\[Theta]ins] == Length[eins] && 
       Length[\[Theta]ins] == Length[edel]; 
flag2 =  ! flag2; 
flag3 = True; 
For[i = 1, i <= Length[\[Gamma]del], i++, 
  flag3 = flag3 && \[Gamma]del[[i]] == \[Gamma]del[[1]]]; 
flag3 = flag3 && Length[edel] != 1; 
If[flag1 || flag2 || flag3, 
 WriteString[stream, "Error in the parameters\n"]; Abort[], 
   nc = Length[
   edel]; \[Tau][(n_)?NumericQ, (i_)?NumericQ, (\[Gamma]_)?
    NumericQ] := 
      Module[{f, re}, 
   f[x_] := x^(i - 1)*(1 - x)^(n - i - 1)*
     N[If[Abs[\[Gamma]] <= 
        1/10^3, (-(1/24))*(-1 + 
          x)*(24 + \[Gamma]*
           x*(12 + \[Gamma]*(-2 + (4 + \[Gamma]*(-1 + x))*x))), 
                 (1 - E^((-\[Gamma])*(1 - x)))/(1 - E^(-\[Gamma]))]]; 
   re = Binomial[n, i]*NIntegrate[f[x], {x, 0, 1}]; re]; 
 sfsi = ConstantArray[0, n - 1]; sfsd = ConstantArray[0, n - 1]; 
    For[i = 1, i < n, i++, 
  For[j = 1, j <= nc, j++, 
    sfsi[[i]] += (1 - eins[[j]])*\[Theta]ins[[j]]*\[Tau][n, 
        i, \[Gamma]ins[[j]]] + 
      edel[[j]]*\[Theta]del[[j]]*\[Tau][n, n - i, \[Gamma]del[[j]]]; 
           
    sfsd[[i]] += (1 - edel[[j]])*\[Theta]del[[j]]*\[Tau][n, 
        i, \[Gamma]del[[j]]] + 
      eins[[j]]*\[Theta]ins[[j]]*\[Tau][n, 
        n - i, \[Gamma]ins[[j]]]; ]; ]; 
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