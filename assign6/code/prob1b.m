data_path = './../../data/animal/predicate-matrix-continuous.txt';
data = dlmread(data_path);

class_path = './../../data/animal/classes.txt';
fid = fopen(class_path);
class_info = textscan(fid, '%f %s');
class_name = class_info{2};

cluster_num = 10;
idx = kmeans(data, cluster_num);

for i = 1 : cluster_num
	index = find(idx == i);
	fprintf('class %d\n', i);
	for j = 1 : length(index)
		fprintf('%s ', class_name{index(j)});
	end
	fprintf('\n');
end