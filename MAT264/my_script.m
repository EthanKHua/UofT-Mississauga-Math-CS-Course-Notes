pkg load symbolic;

syms x a;

x_0 = 0;

f = log(1+x);
f0 = subs(f, x, x_0);

df = diff(f, x);
df0 = subs(df, x, x_0);

ddf = diff(df, x);
ddf0 = subs(ddf, x, x_0);

dddf = diff(ddf, x);
dddf0 = subs(dddf, x, x_0);

