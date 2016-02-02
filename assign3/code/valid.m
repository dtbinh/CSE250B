function [error_rate] = valid(valid_data, gauss, pij, c)

% c = 0.0005;
error = 0;
count = 0;
n = size(gauss{1}.cov_matrix, 1);
for i = 1 : 10
	gauss{i}.cov_matrix = gauss{i}.cov_matrix + eye(n) * c;
    % gauss{i}.cov_matrix = gauss{i}.cov_matrix ;
    temp = log(gauss{i}.cov_matrix);
    gauss{i}.det = trace(temp);
    gauss{i}.u = (gauss{i}.u)';
    gauss{i}.inv = inv(gauss{i}.cov_matrix);
end

for i = 1 : 10
	fprintf('%d\n', i);
	data = valid_data{i};
	data = data';
	prob = [];
	for j = 1 : 10
        temp = data - repmat(gauss{j}.u, 1, size(data,2));
		d = gauss{i}.det; 
        d = sqrt(abs(d)); 
		p = temp' * gauss{j}.inv * temp;
		p = diag(-0.5 * p);
		p = p + log(pij(j)) - log(d);
		prob = [prob p];
	end
	[~, index] = max(prob, [], 2);
	count = count + length(index);
	index = find(index ~= i);
	error = error + length(index);
end

error_rate = error / count;

fprintf('%f\n', error_rate);