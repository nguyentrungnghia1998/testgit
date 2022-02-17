function D   = nhung(V,I,T)
persistent P2  P1  dP d dd n;
if isempty(V)
    V=20;
end
if isempty(I)
    I=0;
end
if isempty(P2)
    P2=0;
end
if isempty(P1)
    P1=0;
end
if isempty(dP)
    dP=0;
end
if isempty(d)
    d=1;
end
if isempty(dd)
    dd=0;
end
if isempty(n)
    n=1;
end
%%%%%%%%%%%%%%%%%%%%%
    if  (T > n*0.02)   %chu ki lay mau 0.02s
    n = n + 1;
    P1=P2;
    P2=V*I;
    dP=P2-P1;
    if (dd==0)
        if dP>1
            dd=0.01;
            d=d+dd;
        else
            if dP<-1
                dd=-0.01;
                d=d+dd;
            else
                dd=0;
            end
        end
    else
        if ((dP<1)&&(dP>-1))
        dd=0;
        d=d+dd;
        else
            if ((dP/dd)>0)
                dd=0.01;
                d=d+dd;
            else
                dd=-0.01;
                d=d+dd;
            end
        end
    end    
    end
D=d/(d+1);
if D<0.1
    D=0.1;
    d=D/(1-D);
else
    if D>0.9
        D=0.9;
        d=D/(1-D);
    else
    end
end
end






