import numpy as np
from sklearn.ensemble import RandomForestClassifier

domain_list = []


def init_data(filename):
    f = open(filename)
    for line in f:
        line = line.strip()
        if line == "" or line.startswith("#"):
            continue
        tokens = line.split(",")
        domain = tokens[0]
        label = tokens[1]
        domain_list.append(Domain(domain, label))
    f.close()

# calculate the entropy of strings
def calc_entropy(s):
    letter_list = set(s)
    entropy = 0.0
    for letter in letter_list:
        p = s.count(letter) / len(s)
        logp = np.log(p)
        entropy -= p * logp
    return entropy

# analyse domain_name_length, domain_numbers_count and domain_name_entropy
def analyse_domain(s):
    domain_analyse_list = []
    domain_numbers = 0
    for character in s:
        if character.isdigit:
            domain_numbers += 1

    domain_analyse_list.append(len(s))
    domain_analyse_list.append(domain_numbers)
    domain_analyse_list.append(calc_entropy(s))
    return domain_analyse_list


class Domain:
    def __init__(self, domain, label):
        self.domain = domain
        self.label = label
        self.domain_analyse_list = analyse_domain(self.domain)

    def return_data(self):
        return self.domain_analyse_list
        # return domain_name_length, domain_numbers, letters_entropy

    def return_labels(self):
        if self.label == "notdga":
            return 0
        else:
            return 1


def main():
    init_data("train.txt")
    feature_matrix = []
    label_list = []

    for domain in domain_list:
        feature_matrix.append(domain.return_data())
        label_list.append(domain.return_labels())

    test_domains = []
    test_domain_analyse = []
    f = open("test.txt")
    for line in f:
        line = line.strip()
        if line == "" or line.startswith("#"):
            continue
        test_domains.append(line)
        test_domain_analyse.append(analyse_domain(line))

    clf = RandomForestClassifier(random_state=0)
    clf.fit(feature_matrix, label_list)
    test_labels = clf.predict(test_domain_analyse)
    output = list(zip(test_domains, test_labels))

    f = open("result.txt", "w+")
    for domain, label in output:
        line = domain
        if label == 0:
            line = line + ",notdga\n"
        else:
            line = line + ",dga\n"
        f.write(line)
    f.close()


if __name__ == '__main__':
    main()
