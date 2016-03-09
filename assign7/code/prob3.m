a1 = [1 0 0];
a2 = [1 0 1];
a3 = [1 1 0];
a4 = [1 1 1];

A = [a1; a2; a3; a4];

D = pdist2(A, A);
D = D.^2;

H = eye(4) - 0.25 * ones(4, 4);
gm2 = -0.5 * H * D * H;

gm = A * A';

A = -1 * A;
gm1 = A * A';