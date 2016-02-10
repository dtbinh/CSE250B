data = csvread('wine.data');

y = data(:, 1);
x = data(:, 2:3);

index = find(y == 1);
x_1 = x(index(1:50), :);

index = find(y == 2);
x_2 = x(index(1:50), :);

input_x = [x_1; x_2];
input_y = [ones(50, 1); -ones(50,1)];


alpha = 0.3;
beta = 0.5;
m = 20000;

w = LogisticRegression(input_x, input_y, m, alpha, beta);

figure;
scatter(x_1(:,1), x_1(:,2), 'filled', 'MarkerFaceColor', 'red', 'MarkerEdgeColor', 'red');
hold on;
scatter(x_2(:,1), x_2(:,2), 'filled', 'MarkerFaceColor', 'green', 'MarkerEdgeColor', 'green');
hold on;


lin_x = linspace(11, 15, 200);
lin_y = (w(1) * lin_x + w(3)) / (-w(2));

plot(lin_x, lin_y, 'LineWidth',2);
xlabel('First feature');
ylabel('Second feature');
title(['Decision boundary: m = ' num2str(m)]);
legend('y = -1','y = +1', 'decision boundary');