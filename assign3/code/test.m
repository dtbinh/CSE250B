c = 10.^(0:10);
error_rate = zeros(length(c), 1);
for i = 1 : length(c)
	error_rate(i) = valid(valid_data, gauss, pij, c(i));
end