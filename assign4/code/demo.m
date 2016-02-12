x_neg = [2 1; 1 20; 1 5]; 
x_pos =	[4 1; 1 40; 3 30];
y_neg = [-1 -1 -1]';
y_pos = [1 1 1]';


x = [x_neg; x_pos];
y = [y_neg; y_pos];

x(:,2) = x(:,2) / 10;
alpha = 0.3;
beta = 0.5;
m = 100;

w = LogisticRegression(x, y, m, alpha, beta);

% x(:,2) = x(:,2) * 10;

figure;
scatter(x_neg(:, 1), x_neg(:, 2) / 10, 'filled', 'MarkerFaceColor', 'red', 'MarkerEdgeColor', 'red');
hold on;
scatter(x_pos(:, 1), x_pos(:, 2) / 10, 'filled', 'MarkerFaceColor', 'green', 'MarkerEdgeColor', 'green');
hold on;

% legend('y = -1','y = +1');




lin_x = linspace(0, 6, 200);
lin_y = (w(1) * lin_x + w(3)) / (-w(2));

plot(lin_x, lin_y, 'LineWidth',2);
xlabel('First feature');
ylabel('Second feature');
title(['Decision boundary: m = ' num2str(m)]);
legend('y = -1','y = +1', 'decision boundary');

