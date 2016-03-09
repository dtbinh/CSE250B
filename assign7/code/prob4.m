distance = csvread('./../../data/distances.txt');

class_path = './../../data/cities.txt';
fid = fopen(class_path);
class_info = textscan(fid, '%s');
class_name = class_info{1};
fclose(fid);

y = cmdscale(distance);
y = y(:,1:2);

figure;
scatter(y(:,1), y(:,2), 100, 'filled');
t = text(y(:,1) + 20, y(:,2) + 20, class_name, 'FontSize', 20);
% title('Classical multidimensional scaling results.');

figure;
scatter(-y(:,1), -y(:,2), 100, 'filled');
text(-y(:,1) + 20, -y(:,2) + 20, class_name, 'FontSize', 20);
% title('Classical multidimensional scaling results after fixing the problem.');