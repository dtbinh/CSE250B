load('../../data/MNIST.mat');

tr_data = cell(10, 1);
valid_data = cell(10, 1);
pij = zeros(10, 1);

train_imgs = double(train_imgs);


for i = 1 : 10
	index = find(train_labels == i-1);
	num = length(index);
	p = randperm(num);

	valid_num = uint32(0.2 * num);

	tr_data{i} = train_imgs(index(p(valid_num+1:end)), :);
	valid_data{i} = train_imgs(index(p(1:valid_num)), :);

	pij(i) = num - valid_num;
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

save('../../data/prob5.mat', 'valid_data', 'gauss', 'pij');












