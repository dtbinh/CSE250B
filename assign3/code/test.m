% load('../../data/MNIST.mat');

tr_data = cell(10, 1);
t_data = cell(10, 1);
pij = zeros(10, 1);

train_imgs = double(train_imgs);
test_imgs = double(test_imgs);


for i = 1 : 10
	index = find(train_labels == i-1);
	tr_data{i} = train_imgs(index, :);
    pij(i) = length(index);
    
    index = find(test_labels == i-1);
	t_data{i} = test_imgs(index, :);
end

count = sum(pij);
pij = pij / count;


new_gauss = cell(10, 1);
for i = 1 : 10
	u = mean(tr_data{i}, 1);
	cov_matrix = cov(tr_data{i});
	new_gauss{i}.u = u;
	new_gauss{i}.cov_matrix = cov_matrix;
end


num = length(final_abstain);
error_rate = zeros(num, 1);
abstain_fraction =  zeros(num, 1);
for i = 1 : num
	[error_rate(i), abstain_fraction(i)] = valid3(t_data, new_gauss, pij, 10000, final_abstain());
end

save('../../prob6.mat', 'f', 'error_rate', 'abstain_fraction', 'final_abstain');


