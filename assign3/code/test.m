% c = 10.^(0:10);
% error_rate = zeros(length(c), 1);
% for i = 1 : length(c)
% 	error_rate(i) = valid(valid_data, gauss, pij, c(i));
% end

load('../../data/MNIST.mat');

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


gauss = cell(10, 1);
for i = 1 : 10
	u = mean(tr_data{i}, 1);
	cov_matrix = cov(tr_data{i});
	gauss{i}.u = u;
	gauss{i}.cov_matrix = cov_matrix;
end

valid(t_data, gauss, pij, 10000);
% save('../../data/prob5.mat', 'valid_data', 'gauss', 'pij');