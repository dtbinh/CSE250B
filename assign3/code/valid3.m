function [error_rate, abstain_fraction] = valid3(valid_data, gauss, pij, c, abstain)

error = 0;
count = 0;
n = size(gauss{1}.cov_matrix, 1);
final_prob = cell(10, 1);

for i = 1 : 10
	gauss{i}.cov_matrix = gauss{i}.cov_matrix + eye(n) * c;
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
	
	final_prob{i} = prob;
end


abstain_fraction = 0;
total_count = 0;

for i = 1 : 10
	prob  = final_prob{i};
	[index, ] = sort(prob, 2);
	prob_1 = index(:, end);
	prob_2 = index(:, end-1);
	temp = prob_2 ./ prob_1;

	index = find(temp > abstain);
	
	abstain_fraction = abstain_fraction + length(temp) - length(index);
	total_count = total_count + length(index);

	[~, index] = max(prob(index, :), [], 2);
	count = count + length(index);
	index = find(index ~= i);
	error = error + length(index);
end

abstain_fraction = abstain_fraction / total_count;
error_rate = error / count;

fprintf('%f\n', error_rate);


