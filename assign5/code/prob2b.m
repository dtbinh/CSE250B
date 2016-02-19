function [] = prob2b(x_pos, y_pos, x_neg, y_neg)

x_pos(:, 3) = 1;
x_neg(:, 3) = 1;

all_x = [x_pos; x_neg];
all_y = [y_pos; y_neg]; 

data_num = size(all_x, 1);
data_dim = size(all_x, 2);

w = zeros(1, data_num);

T = 10;

sigma = 1;

for i = 1 : T
	% random permute data points
	index = randperm(data_num);
	x = all_x(index, :);
	y = all_y(index, :);

	for j = 1 : data_num
		temp = all_x - repmat(x(j, :), data_num, 1);
		temp = sum(temp.^2, 2);	
		temp = temp / (2 * sigma * sigma);
		temp = exp(-1.0 * temp);
		temp = w * temp;


		if sign(temp) ~= y(j)
			w(index(j)) = w(index(j)) + y(j);		
		end
	end
end



x_1_min = min(all_x(:, 1)) - 1;
x_1_max = max(all_x(:, 1)) + 2;

x_2_min = min(all_x(:, 2)) - 1;
x_2_max = max(all_x(:, 2)) + 2;

x_range = [x_1_min x_1_max];
y_range = [x_2_min x_2_max];

inc = 0.01;

[x, y] = meshgrid(x_1_min:inc:x_1_max, x_2_min:inc:x_2_max);

xy = [x(:) y(:)];
xy(:, 3) = 1;

xy_num = size(xy, 1);

image_size = size(x);

idx = zeros(xy_num, 1);



all_x = all_x';
pred = repmat(xy, 1, data_num) - repmat(all_x(:)', xy_num, 1); 
pred = pred .^ 2.0;
pred = pred';
pred = reshape(pred, 3, []);
pred = sum(pred, 1);
pred = -1.0 * pred / (2 * sigma * sigma);
pred = exp(pred);

pred = reshape(pred, data_num, []);
pred = w * pred;




idx(pred >= 0) = 1;
idx(pred < 0) = 2;


decisionmap = reshape(idx, image_size);


figure1 = figure;
imagesc(x_range, y_range, decisionmap);
hold on;

set(gca,'ydir','normal');

cmap = [1 0.8 0.8; 0.95 1 0.95];
colormap(cmap);

scatter(x_pos(:, 1), x_pos(:, 2), 'filled', 'MarkerFaceColor', 'red', 'MarkerEdgeColor', 'red');
scatter(x_neg(:, 1), x_neg(:, 2), 'filled', 'MarkerFaceColor', 'green', 'MarkerEdgeColor', 'green');

legend('+1', '-1', 'Location','NorthOutside','Orientation', 'horizontal');

saveas(figure1, '2a-data-1.png');






