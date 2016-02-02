f = 0.01 : 0.01 : 0.4;
final_abstain = zeros(length(f), 1)

for i = 1 : length(final_abstain)
	fprintf('%d out of %d\n', i, length(final_abstain));
	[error_rate, abstain] = valid2(valid_data, gauss, pij, 10000, f(i));
	final_abstain(i) = abstain;
end

save('../../data/abstain.mat', 'final_abstain', 'f');
