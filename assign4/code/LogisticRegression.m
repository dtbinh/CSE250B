function w = LogisticRegression(x, y, m, alpha, beta)

% x: input data, each row is a data pont
% y: a label vector, {-1, 1}
% m: number of iterations
% w: regression coefficients

data_dim = size(x, 2);

x(:, data_dim + 1) = 1;
curr_w = zeros(data_dim + 1, 1);
new_w = curr_w;
for iter = 1 : m

	% fprintf('Iter %d\n', iter);
	pr = x * curr_w;
	pr = exp(y .* pr);
	pr = 1.0 ./ (1.0 + pr);

    pr = pr(:);
	coeff = pr .* y;
	coeff = repmat(coeff, 1, data_dim + 1);

	grad_w = -1.0 * sum(coeff .* x, 1)';

	t = BacktrackLineSearch(curr_w, x, y, grad_w, alpha, beta);
    % t = 0.01;
	new_w = curr_w - t * grad_w;
	curr_w = new_w;
    
    fprintf('loss: %f\n', EvaluateTarget(curr_w, x, y));
end

w = curr_w;

end


function t = BacktrackLineSearch(w, x, y, grad_w, alpha, beta)

temp = 1; 

f_x = EvaluateTarget(w, x, y);

t = 1;
while true
	new_w = w - grad_w * t;
	new_f_x = EvaluateTarget(new_w, x, y);

	temp = -1.0 * alpha * t * (norm(grad_w)^2);

	if new_f_x > f_x + temp
		t = beta * t;
	else
		break;
	end
end

end


function v = EvaluateTarget(w, x, y)

top = x * w;
top = -y .* top; 

v = log(1 + exp(top));
v = sum(v, 1);

end