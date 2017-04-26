# -*- coding: utf-8 -*-

from sklearn import svm
from sklearn.datasets import load_iris
from sklearn_porter import Porter


iris_data = load_iris()
X, y = iris_data.data, iris_data.target

clf = svm.SVC(C=1., gamma=0.001, kernel='rbf', random_state=0)
clf.fit(X, y)

output = Porter(clf).export()
# output = Porter(clf, language='java').export()
print(output)

"""
class Brain {

    public static int predict(float[] atts) {

        int[] n_svs = {50, 50, 50};
        double[][] svs = {{5.0999999999999996, 3.5, 1.3999999999999999, 0.20000000000000001}, {4.9000000000000004, 3.0, 1.3999999999999999, 0.20000000000000001}, {4.7000000000000002, 3.2000000000000002, 1.3, 0.20000000000000001}, {4.5999999999999996, 3.1000000000000001, 1.5, 0.20000000000000001}, {5.0, 3.6000000000000001, 1.3999999999999999, 0.20000000000000001}, {5.4000000000000004, 3.8999999999999999, 1.7, 0.40000000000000002}, {4.5999999999999996, 3.3999999999999999, 1.3999999999999999, 0.29999999999999999}, {5.0, 3.3999999999999999, 1.5, 0.20000000000000001}, {4.4000000000000004, 2.8999999999999999, 1.3999999999999999, 0.20000000000000001}, {4.9000000000000004, 3.1000000000000001, 1.5, 0.10000000000000001}, {5.4000000000000004, 3.7000000000000002, 1.5, 0.20000000000000001}, {4.7999999999999998, 3.3999999999999999, 1.6000000000000001, 0.20000000000000001}, {4.7999999999999998, 3.0, 1.3999999999999999, 0.10000000000000001}, {4.2999999999999998, 3.0, 1.1000000000000001, 0.10000000000000001}, {5.7999999999999998, 4.0, 1.2, 0.20000000000000001}, {5.7000000000000002, 4.4000000000000004, 1.5, 0.40000000000000002}, {5.4000000000000004, 3.8999999999999999, 1.3, 0.40000000000000002}, {5.0999999999999996, 3.5, 1.3999999999999999, 0.29999999999999999}, {5.7000000000000002, 3.7999999999999998, 1.7, 0.29999999999999999}, {5.0999999999999996, 3.7999999999999998, 1.5, 0.29999999999999999}, {5.4000000000000004, 3.3999999999999999, 1.7, 0.20000000000000001}, {5.0999999999999996, 3.7000000000000002, 1.5, 0.40000000000000002}, {4.5999999999999996, 3.6000000000000001, 1.0, 0.20000000000000001}, {5.0999999999999996, 3.2999999999999998, 1.7, 0.5}, {4.7999999999999998, 3.3999999999999999, 1.8999999999999999, 0.20000000000000001}, {5.0, 3.0, 1.6000000000000001, 0.20000000000000001}, {5.0, 3.3999999999999999, 1.6000000000000001, 0.40000000000000002}, {5.2000000000000002, 3.5, 1.5, 0.20000000000000001}, {5.2000000000000002, 3.3999999999999999, 1.3999999999999999, 0.20000000000000001}, {4.7000000000000002, 3.2000000000000002, 1.6000000000000001, 0.20000000000000001}, {4.7999999999999998, 3.1000000000000001, 1.6000000000000001, 0.20000000000000001}, {5.4000000000000004, 3.3999999999999999, 1.5, 0.40000000000000002}, {5.2000000000000002, 4.0999999999999996, 1.5, 0.10000000000000001}, {5.5, 4.2000000000000002, 1.3999999999999999, 0.20000000000000001}, {4.9000000000000004, 3.1000000000000001, 1.5, 0.10000000000000001}, {5.0, 3.2000000000000002, 1.2, 0.20000000000000001}, {5.5, 3.5, 1.3, 0.20000000000000001}, {4.9000000000000004, 3.1000000000000001, 1.5, 0.10000000000000001}, {4.4000000000000004, 3.0, 1.3, 0.20000000000000001}, {5.0999999999999996, 3.3999999999999999, 1.5, 0.20000000000000001}, {5.0, 3.5, 1.3, 0.29999999999999999}, {4.5, 2.2999999999999998, 1.3, 0.29999999999999999}, {4.4000000000000004, 3.2000000000000002, 1.3, 0.20000000000000001}, {5.0, 3.5, 1.6000000000000001, 0.59999999999999998}, {5.0999999999999996, 3.7999999999999998, 1.8999999999999999, 0.40000000000000002}, {4.7999999999999998, 3.0, 1.3999999999999999, 0.29999999999999999}, {5.0999999999999996, 3.7999999999999998, 1.6000000000000001, 0.20000000000000001}, {4.5999999999999996, 3.2000000000000002, 1.3999999999999999, 0.20000000000000001}, {5.2999999999999998, 3.7000000000000002, 1.5, 0.20000000000000001}, {5.0, 3.2999999999999998, 1.3999999999999999, 0.20000000000000001}, {7.0, 3.2000000000000002, 4.7000000000000002, 1.3999999999999999}, {6.4000000000000004, 3.2000000000000002, 4.5, 1.5}, {6.9000000000000004, 3.1000000000000001, 4.9000000000000004, 1.5}, {5.5, 2.2999999999999998, 4.0, 1.3}, {6.5, 2.7999999999999998, 4.5999999999999996, 1.5}, {5.7000000000000002, 2.7999999999999998, 4.5, 1.3}, {6.2999999999999998, 3.2999999999999998, 4.7000000000000002, 1.6000000000000001}, {4.9000000000000004, 2.3999999999999999, 3.2999999999999998, 1.0}, {6.5999999999999996, 2.8999999999999999, 4.5999999999999996, 1.3}, {5.2000000000000002, 2.7000000000000002, 3.8999999999999999, 1.3999999999999999}, {5.0, 2.0, 3.5, 1.0}, {5.9000000000000004, 3.0, 4.2000000000000002, 1.5}, {6.0, 2.2000000000000002, 4.0, 1.0}, {6.0999999999999996, 2.8999999999999999, 4.7000000000000002, 1.3999999999999999}, {5.5999999999999996, 2.8999999999999999, 3.6000000000000001, 1.3}, {6.7000000000000002, 3.1000000000000001, 4.4000000000000004, 1.3999999999999999}, {5.5999999999999996, 3.0, 4.5, 1.5}, {5.7999999999999998, 2.7000000000000002, 4.0999999999999996, 1.0}, {6.2000000000000002, 2.2000000000000002, 4.5, 1.5}, {5.5999999999999996, 2.5, 3.8999999999999999, 1.1000000000000001}, {5.9000000000000004, 3.2000000000000002, 4.7999999999999998, 1.8}, {6.0999999999999996, 2.7999999999999998, 4.0, 1.3}, {6.2999999999999998, 2.5, 4.9000000000000004, 1.5}, {6.0999999999999996, 2.7999999999999998, 4.7000000000000002, 1.2}, {6.4000000000000004, 2.8999999999999999, 4.2999999999999998, 1.3}, {6.5999999999999996, 3.0, 4.4000000000000004, 1.3999999999999999}, {6.7999999999999998, 2.7999999999999998, 4.7999999999999998, 1.3999999999999999}, {6.7000000000000002, 3.0, 5.0, 1.7}, {6.0, 2.8999999999999999, 4.5, 1.5}, {5.7000000000000002, 2.6000000000000001, 3.5, 1.0}, {5.5, 2.3999999999999999, 3.7999999999999998, 1.1000000000000001}, {5.5, 2.3999999999999999, 3.7000000000000002, 1.0}, {5.7999999999999998, 2.7000000000000002, 3.8999999999999999, 1.2}, {6.0, 2.7000000000000002, 5.0999999999999996, 1.6000000000000001}, {5.4000000000000004, 3.0, 4.5, 1.5}, {6.0, 3.3999999999999999, 4.5, 1.6000000000000001}, {6.7000000000000002, 3.1000000000000001, 4.7000000000000002, 1.5}, {6.2999999999999998, 2.2999999999999998, 4.4000000000000004, 1.3}, {5.5999999999999996, 3.0, 4.0999999999999996, 1.3}, {5.5, 2.5, 4.0, 1.3}, {5.5, 2.6000000000000001, 4.4000000000000004, 1.2}, {6.0999999999999996, 3.0, 4.5999999999999996, 1.3999999999999999}, {5.7999999999999998, 2.6000000000000001, 4.0, 1.2}, {5.0, 2.2999999999999998, 3.2999999999999998, 1.0}, {5.5999999999999996, 2.7000000000000002, 4.2000000000000002, 1.3}, {5.7000000000000002, 3.0, 4.2000000000000002, 1.2}, {5.7000000000000002, 2.8999999999999999, 4.2000000000000002, 1.3}, {6.2000000000000002, 2.8999999999999999, 4.2999999999999998, 1.3}, {5.0999999999999996, 2.5, 3.0, 1.1000000000000001}, {5.7000000000000002, 2.7999999999999998, 4.0999999999999996, 1.3}, {6.2999999999999998, 3.2999999999999998, 6.0, 2.5}, {5.7999999999999998, 2.7000000000000002, 5.0999999999999996, 1.8999999999999999}, {7.0999999999999996, 3.0, 5.9000000000000004, 2.1000000000000001}, {6.2999999999999998, 2.8999999999999999, 5.5999999999999996, 1.8}, {6.5, 3.0, 5.7999999999999998, 2.2000000000000002}, {7.5999999999999996, 3.0, 6.5999999999999996, 2.1000000000000001}, {4.9000000000000004, 2.5, 4.5, 1.7}, {7.2999999999999998, 2.8999999999999999, 6.2999999999999998, 1.8}, {6.7000000000000002, 2.5, 5.7999999999999998, 1.8}, {7.2000000000000002, 3.6000000000000001, 6.0999999999999996, 2.5}, {6.5, 3.2000000000000002, 5.0999999999999996, 2.0}, {6.4000000000000004, 2.7000000000000002, 5.2999999999999998, 1.8999999999999999}, {6.7999999999999998, 3.0, 5.5, 2.1000000000000001}, {5.7000000000000002, 2.5, 5.0, 2.0}, {5.7999999999999998, 2.7999999999999998, 5.0999999999999996, 2.3999999999999999}, {6.4000000000000004, 3.2000000000000002, 5.2999999999999998, 2.2999999999999998}, {6.5, 3.0, 5.5, 1.8}, {7.7000000000000002, 3.7999999999999998, 6.7000000000000002, 2.2000000000000002}, {7.7000000000000002, 2.6000000000000001, 6.9000000000000004, 2.2999999999999998}, {6.0, 2.2000000000000002, 5.0, 1.5}, {6.9000000000000004, 3.2000000000000002, 5.7000000000000002, 2.2999999999999998}, {5.5999999999999996, 2.7999999999999998, 4.9000000000000004, 2.0}, {7.7000000000000002, 2.7999999999999998, 6.7000000000000002, 2.0}, {6.2999999999999998, 2.7000000000000002, 4.9000000000000004, 1.8}, {6.7000000000000002, 3.2999999999999998, 5.7000000000000002, 2.1000000000000001}, {7.2000000000000002, 3.2000000000000002, 6.0, 1.8}, {6.2000000000000002, 2.7999999999999998, 4.7999999999999998, 1.8}, {6.0999999999999996, 3.0, 4.9000000000000004, 1.8}, {6.4000000000000004, 2.7999999999999998, 5.5999999999999996, 2.1000000000000001}, {7.2000000000000002, 3.0, 5.7999999999999998, 1.6000000000000001}, {7.4000000000000004, 2.7999999999999998, 6.0999999999999996, 1.8999999999999999}, {7.9000000000000004, 3.7999999999999998, 6.4000000000000004, 2.0}, {6.4000000000000004, 2.7999999999999998, 5.5999999999999996, 2.2000000000000002}, {6.2999999999999998, 2.7999999999999998, 5.0999999999999996, 1.5}, {6.0999999999999996, 2.6000000000000001, 5.5999999999999996, 1.3999999999999999}, {7.7000000000000002, 3.0, 6.0999999999999996, 2.2999999999999998}, {6.2999999999999998, 3.3999999999999999, 5.5999999999999996, 2.3999999999999999}, {6.4000000000000004, 3.1000000000000001, 5.5, 1.8}, {6.0, 3.0, 4.7999999999999998, 1.8}, {6.9000000000000004, 3.1000000000000001, 5.4000000000000004, 2.1000000000000001}, {6.7000000000000002, 3.1000000000000001, 5.5999999999999996, 2.3999999999999999}, {6.9000000000000004, 3.1000000000000001, 5.0999999999999996, 2.2999999999999998}, {5.7999999999999998, 2.7000000000000002, 5.0999999999999996, 1.8999999999999999}, {6.7999999999999998, 3.2000000000000002, 5.9000000000000004, 2.2999999999999998}, {6.7000000000000002, 3.2999999999999998, 5.7000000000000002, 2.5}, {6.7000000000000002, 3.0, 5.2000000000000002, 2.2999999999999998}, {6.2999999999999998, 2.5, 5.0, 1.8999999999999999}, {6.5, 3.0, 5.2000000000000002, 2.0}, {6.2000000000000002, 3.3999999999999999, 5.4000000000000004, 2.2999999999999998}, {5.9000000000000004, 3.0, 5.0999999999999996, 1.8}};
        double[][] coeffs = {{1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -0.0, -1.0, -0.0, -1.0, -0.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -0.0, -0.0, -1.0, -1.0, -1.0, -0.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -0.0, -0.0, -1.0, -1.0, -1.0, -0.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0}, {1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0}};
        double[] inters = {0.043376922607421875, 0.11445245146751404, -0.0031709671020507812};
        int[] classes = {0, 1, 2};

        // exp(-y|x-x'|^2)
        double[] kernels = new double[150];
        double kernel;
        for (int i = 0; i < 150; i++) {
            kernel = 0.;
            for (int j = 0; j < 4; j++) {
                kernel += Math.pow(svs[i][j] - atts[j], 2);
            }
            kernels[i] = Math.exp(-0.001 * kernel);
        }

        int[] starts = new int[3];
        for (int i = 0; i < 3; i++) {
            if (i != 0) {
                int start = 0;
                for (int j = 0; j < i; j++) {
                    start += n_svs[j];
                }
                starts[i] = start;
            } else {
                starts[0] = 0;
            }
        }

        int[] ends = new int[3];
        for (int i = 0; i < 3; i++) {
            ends[i] = n_svs[i] + starts[i];
        }

        double[] decisions = new double[3];
        for (int i = 0, d = 0, l = 3; i < l; i++) {
            for (int j = i + 1; j < l; j++) {
                double tmp = 0.;
                for (int k = starts[j]; k < ends[j]; k++) {
                    tmp += coeffs[i][k] * kernels[k];
                }
                for (int k = starts[i]; k < ends[i]; k++) {
                    tmp += coeffs[j - 1][k] * kernels[k];
                }
                decisions[d] = tmp + inters[d];
                d++;
            }
        }

        int[] votes = new int[3];
        for (int i = 0, d = 0, l = 3; i < l; i++) {
            for (int j = i + 1; j < l; j++) {
                votes[d] = decisions[d] > 0 ? i : j;
                d++;
            }
        }

        int[] amounts = new int[3];
        for (int i = 0, l = 3; i < l; i++) {
            amounts[votes[i]] += 1;
        }

        int class_val = -1,
            class_idx = -1;
        for (int i = 0, l = 3; i < l; i++) {
            if (amounts[i] > class_val) {
                class_val = amounts[i];
                class_idx = i;
            }
        }
        return classes[class_idx];
    }

    public static void main(String[] args) {
        if (args.length == 4) {
            float[] atts = new float[args.length];
            for (int i = 0, l = args.length; i < l; i++) {
                atts[i] = Float.parseFloat(args[i]);
            }
            System.out.println(Brain.predict(atts));
        }
    }
}
"""
