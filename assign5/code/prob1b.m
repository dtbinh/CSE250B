function [] = prob1b(x_pos, y_pos, x_neg, y_neg)

% add an extra feature
x_pos(:, 3) = 1;
x_neg(:, 3) = 1;

l = 1;
c = {};
c{1} = 0;
w = {};


all_x = [x_pos; x_neg];
all_y = [y_pos; y_neg]; 

data_num = size(all_x, 1);
data_dim = size(all_x, 2);

w{1} = zeros(1, data_dim);


T = 50;

for i = 1 : T
	% random permute data points
	index = randperm(data_num);
	x = all_x(index, :);
	y = all_y(index, :);

	for j = 1 : data_num
		temp = sum(x(j, :) .* w{l});
		if sign(temp) ~= y(j)
			w{l+1} = w{l} + y(j) * x(j, :);
			c{l+1} = 1; l = l + 1;
		else
			c{l} = c{l} + 1;
		end
	end

end


% find range of first and second feature of x
x_1_min = min(all_x(:, 1)) - 2;
x_1_max = max(all_x(:, 1)) + 2;

x_2_min = min(all_x(:, 2)) - 2;
x_2_max = max(all_x(:, 2)) + 2;

x_range = [x_1_min x_1_max];
y_range = [x_2_min x_2_max];

inc = 0.1;

[x, y] = meshgrid(x_1_min:inc:x_1_max, x_2_min:inc:x_2_max);

xy = [x(:) y(:)];
xy(:, 3) = 1;

xy_num = size(xy, 1);

image_size = size(x);

idx = zeros(xy_num, 1);


final_w = zeros(data_dim, l); 
final_c = zeros(1, l);
for i = 1 : l	
	final_w(:,i) = w{i};
	final_c(i) = c{i};
end




fprintf('Number of w: %d\n', l);

pred = xy * final_w;
pred = sign(pred);
pred = repmat(final_c, xy_num, 1) .* pred;
pred = sum(pred, 2);
pred = sign(pred);

idx(pred >= 0) = 1;
idx(pred < 0) = 2;


decisionmap = reshape(idx, image_size);


figure1 = figure;
imagesc(x_range, y_range, decisionmap);
hold on;

set(gca,'ydir','normal');

cmap = [1 0.8 0.8; 0.95 1 0.95]
colormap(cmap);

scatter(x_pos(:, 1), x_pos(:, 2), 'filled', 'MarkerFaceColor', 'red', 'MarkerEdgeColor', 'red');
scatter(x_neg(:, 1), x_neg(:, 2), 'filled', 'MarkerFaceColor', 'green', 'MarkerEdgeColor', 'green');

legend('+1', '-1');

title('Problem 1-b: T = 50, use all w');
saveas(figure1, '1b-full.png');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% downsample w and c
L = 50;
[~, index] = sort(final_c, 'descend');
index = index(1:L);

final_w = final_w(:, index);
final_c = final_c(:, index);

pred = xy * final_w;
pred = sign(pred);
pred = repmat(final_c, xy_num, 1) .* pred;
pred = sum(pred, 2);
pred = sign(pred);

idx(pred >= 0) = 1;
idx(pred < 0) = 2;


decisionmap = reshape(idx, image_size);


figure2 = figure;
imagesc(x_range, y_range, decisionmap);
hold on;

set(gca,'ydir','normal');

cmap = [1 0.8 0.8; 0.95 1 0.95]
colormap(cmap);

scatter(x_pos(:, 1), x_pos(:, 2), 'filled', 'MarkerFaceColor', 'red', 'MarkerEdgeColor', 'red');
scatter(x_neg(:, 1), x_neg(:, 2), 'filled', 'MarkerFaceColor', 'green', 'MarkerEdgeColor', 'green');

legend('+1', '-1');
title('Problem 1-b: T = 50, L = 50');
saveas(figure2, '1b-select.png');
