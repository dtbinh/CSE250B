data_path = './../../data/animal/predicate-matrix-continuous.txt';
data = dlmread(data_path);

class_path = './../../data/animal/classes.txt';
fid = fopen(class_path);
class_info = textscan(fid, '%f %s');
class_name = class_info{2};

% problem 1b
if 0
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
end

% problem 1c
if 0 
	y = pdist(data);
	z = linkage(y, 'average');
	% leafOrder = optimalleaforder(z, y);
	figure2 = figure;
	dendrogram(z, 50, 'Labels', class_name, 'Orientation', 'right');
	title('Problem 1-c: hierarchical clustering result on animal dataset.')
	saveas(figure2, '1c.png');
end

if 1
	coeff = pca(data);
	coeff = coeff(:, 1:2);
	new_data = data * coeff;
	figure3 = figure;
	
	x = new_data(:, 1); y = new_data(:, 2);
	scatter(x,y, 'filled');
	text(x + 2, y + 2, class_name);
	xlabel('First dimension');
	ylabel('Second dimension');
	title('Problem 4: data points after PCA');
	saveas(figure3, '4.png');
	
end