data_path = '../../data/data2.txt';

data = dlmread(data_path, ' '); data = data(:, 1:3);

index = find(data(:, 3) == 1);
x_pos = data(index, 1:2);
y_pos = data(index, 3);

index = find(data(:, 3) == -1);
x_neg = data(index, 1:2);
y_neg = data(index, 3);

% prob1a(x_pos, y_pos, x_neg, y_neg);
% prob1b(x_pos, y_pos, x_neg, y_neg);
% prob1c(x_pos, y_pos, x_neg, y_neg);
prob2a(x_pos, y_pos, x_neg, y_neg);
