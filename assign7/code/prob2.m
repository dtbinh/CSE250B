M = [1 2 3; 4 5 6];
[U, V, S] = svd(M, 'econ');

k = 1;
approx = U(:, 1:k) * V(1:k, 1:k) * S(:, 1:k)';